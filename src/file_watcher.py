import fnmatch
import os
import time

from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder, is_link

from .util import *

try:
	# lets the user actually stop the watch loop by hitting "Cancel" in the UI,
	# instead of it looping forever until the server process is killed.
	from comfy.model_management import \
	    throw_exception_if_processing_interrupted as _check_interrupted
except ImportError:
	def _check_interrupted():
		pass


FLOWCONTROL_NOTE = "You need to connect the `flow_control` from a `FileWatcherBegin` to a `FileWatcherEnd` node."
DESCRIPTION = f"""Watch a directory for new files and run a sub-workflow once for every file that shows up, one at a time, forever.
{FLOWCONTROL_NOTE}
Unlike `IterateBegin`/`IterateEnd`, this does not iterate a fixed, pre-existing list: it polls `directory` and waits until a new file's size and modification time have stopped changing for `stability_delay` seconds (i.e. it looks fully written), then runs the sub-workflow on it. A file whose name was already processed is picked up again if it later shows up with a different size, modification time, or creation date (e.g. it got overwritten or recreated).
Internally uses the node expansion mechanism which duplicates the sub-workflow again after every processed file, so the loop never really "ends" on its own - cancel the queued prompt to stop it.
On `FileWatcherEnd`, connect every passthrough/output node of the sub-workflow (`Preview Image`, `Save Image`, etc.) into a `termination` slot so the loop only advances once the whole sub-workflow has actually finished running.
"""


class FileWatcherBegin(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description   	= DESCRIPTION,
			node_id       		= "FileWatcherBegin",
			display_name  	= "File Watcher Begin",
			search_aliases	= ["Watch Folder Begin", "Watch Directory Begin", "File Watch Begin", "Directory Watch Begin", "New File Begin"],
			category      	= CATEGORY,
			inputs        		= [
				io.String 	.Input("directory"      	, display_name="directory"      	, tooltip="Folder to watch for new files."),
				io.String 	.Input("file_pattern"   	, display_name="file_pattern"   	, default="*" , optional=True, tooltip="Only files whose name matches this glob pattern are considered, e.g. `*.png`."),
				io.Float  	.Input("poll_interval"  	, display_name="poll_interval"  	, default=1.0 , min=0.05, max=60.0, optional=True, tooltip="Maximum seconds between directory rescans. Also caps how long a single wait can be, even if a file looks like it needs longer to stabilize."),
				io.Float  	.Input("stability_delay"	, display_name="stability_delay"	, default=1.0 , min=0.0 , max=60.0, optional=True, tooltip="Seconds a file's size must stay unchanged before it's considered fully written and safe to hand off. Set to 0 to disable and grab files as soon as they're seen."),
				io.AnyType	.Input("_tracked"       	, display_name="_"              	, optional=True, tooltip="Ignore! Only used internally"),
			],
			outputs=[
				io.FlowControl	.Output("flow_control"	, display_name="flow_control"	, tooltip=FLOWCONTROL_NOTE),
				io.String     	.Output("filepath"    	, display_name="filepath"    	, tooltip="Full path of the new file."),
				io.Int        	.Output("index"       	, display_name="index"       	, tooltip="How many files have been claimed so far (0-based)."),
				io.AnyType    	.Output("file_info"   	, display_name="file_info"   	, tooltip="dict with ctime/mtime/atime of the file at the moment it was picked up. Note: st_ctime is creation time on Windows but inode-change time on Linux/Mac."),
			],
			is_input_list	= True,
			hidden       		= [io.Hidden.unique_id],
		)
		return ret

	@staticmethod
	def _unwrap(value, default):
		# every input arrives as a list of length 1 because of is_input_list=True,
		# except _tracked on the very first (unconnected) call, which is just None.
		if isinstance(value, list):
			return value[0] if len(value) else default
		return value if value is not None else default

	@staticmethod
	def _scan(directory, tracked, pattern, stability_delay, now):
		"""One non-blocking pass over `directory`.

		Every file we've ever seen gets an entry in `tracked` (mutated in place): its last known
		`size`, `mtime` and `ctime`, the timestamp it was last seen changing (`last_checked`), and
		whether it has already been claimed (`is_processed`). A file becomes a "stable" candidate
		once all three have stayed the same for at least `stability_delay` seconds - measured by
		wall-clock time elapsed since `last_checked`, not by blocking here, so scanning a big
		backlog of files costs one pass, not one `stability_delay` sleep per file.

		A file whose name we've already processed is re-queued instead of skipped if its size,
		mtime, or ctime no longer match what they were when it was claimed - i.e. it was
		overwritten, or recreated, with a new version since. (Note: ctime is the creation time on
		Windows but the inode-change time on Linux/Mac, so there it also flags e.g. permission or
		metadata changes, not just content changes.)

		Returns (stable_candidates, min_wait): stable_candidates is a list of paths ready to be
		claimed (oldest-stabilized first); min_wait is the shortest remaining time before any
		still-settling file might become stable (or None if there's nothing to wait on).
		"""
		try:
			names = os.listdir(directory)
		except OSError:
			return [], None

		seen      = set()
		stable    = []
		min_wait  = None

		for name in names:
			if not fnmatch.fnmatch(name, pattern):
				continue
			full = os.path.join(directory, name)
			if not os.path.isfile(full):
				continue
			seen.add(full)

			try:
				size  = os.path.getsize(full)
				mtime = os.path.getmtime(full)
				ctime = os.stat(full).st_ctime
			except OSError:
				continue

			entry = tracked.get(full)
			if entry is not None and entry["is_processed"]:
				if size == entry["size"] and mtime == entry["mtime"] and ctime == entry["ctime"]:
					continue # unchanged since it was last processed - stays skipped
				entry = None # overwritten/recreated with a new version since - treat like a brand new file

			if entry is None or size != entry["size"] or mtime != entry["mtime"] or ctime != entry["ctime"]:
				# first time we've seen it, or it's still being written (or was just overwritten) - (re)start its timer
				tracked[full] = {"size": size, "mtime": mtime, "ctime": ctime, "last_checked": now, "is_processed": False}
				min_wait = stability_delay if min_wait is None else min(min_wait, stability_delay)
				continue

			remaining = stability_delay - (now - entry["last_checked"])
			if remaining <= 0:
				stable.append(full)
			else:
				min_wait = remaining if min_wait is None else min(min_wait, remaining)

		# drop bookkeeping for anything that vanished before it was ever claimed (renamed mid-copy, etc.)
		for path in list(tracked.keys()):
			if path not in seen and not tracked[path]["is_processed"]:
				del tracked[path]

		stable.sort(key=lambda p: tracked[p]["last_checked"]) # first to go stable, served first
		return stable, min_wait

	@classmethod
	def execute(cls, directory, file_pattern=None, poll_interval=None, stability_delay=None, _tracked=None, **kwargs) -> io.NodeOutput:
		directory      	= cls._unwrap(directory      	, None)
		file_pattern   	= cls._unwrap(file_pattern   	, "*")
		poll_interval  	= cls._unwrap(poll_interval  	, 1.0)
		stability_delay	= cls._unwrap(stability_delay	, 1.0)
		tracked        	= cls._unwrap(_tracked       	, {})
		if not isinstance(tracked, dict):
			tracked = {}
		tracked = dict(tracked) # this node's own claim below must not leak into anyone else's copy

		claimed = None
		while claimed is None:
			_check_interrupted()
			now = time.time()
			stable, min_wait = cls._scan(directory, tracked, file_pattern, stability_delay, now)
			if stable:
				claimed = stable[0]
				break
			wait_time = poll_interval if min_wait is None else min(poll_interval, max(0.0, min_wait))
			_check_interrupted()
			time.sleep(wait_time)

		st       	= os.stat(claimed)
		file_info	= {"path": claimed, "ctime": st.st_ctime, "mtime": st.st_mtime, "atime": st.st_atime}

		# Claim the file right here, not in FileWatcherEnd: FileWatcherEnd only sees generic
		# passthrough/trigger values from the sub-workflow, which can't be trusted to still be (or
		# contain) this filepath. FileWatcherBegin is the only place that reliably knows it, so
		# `tracked` must already mark it processed before it's handed off to the sub-workflow -
		# otherwise every re-expansion would rediscover the same file and loop on it forever.
		# size/mtime/ctime are kept even once processed so a later overwrite of this same filename
		# can still be detected and re-queued (see _scan).
		tracked[claimed] = {"size": tracked[claimed]["size"], "mtime": file_info["mtime"], "ctime": file_info["ctime"], "last_checked": time.time(), "is_processed": True, **file_info}

		flow_control	= (cls.hidden.unique_id, tracked)
		index       	= sum(1 for entry in tracked.values() if entry["is_processed"]) - 1

		ret = io.NodeOutput(flow_control, claimed, index, file_info)
		return ret


class FileWatcherEnd(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		terminations_template = io.Autogrow.TemplatePrefix(
			input 	= io.AnyType.Input("termination", tooltip="Connect a passthrough/output node here (Preview Image, Save Image, etc). Its value is discarded - it's only used to force that branch of the sub-workflow to finish before the next file is picked up."),
			prefix	= "termination",
			min   	= 0,
			max   	= 50,
		)
		ret = io.Schema(
			description   	= DESCRIPTION,
			node_id       		= "FileWatcherEnd",
			display_name  	= "File Watcher End",
			search_aliases	= ["Watch Folder End", "Watch Directory End", "File Watch End", "Directory Watch End", "New File End"],
			category      	= CATEGORY,
			inputs        		= [
				io.FlowControl	.Input("flow_control"	, display_name="flow_control"	, tooltip="Connect it to a `FileWatcherBegin` node"),
				io.Autogrow   	.Input("terminations"	, template=terminations_template, optional=True, tooltip="(optional, but you almost always want at least one) Connect every branch of the sub-workflow that must finish before watching for the next file, e.g. both a `Save Image` and a `Preview Image` passthrough. With nothing connected here, the loop may advance before the sub-workflow has actually finished running."),
			],
			outputs		= [
				io.Int	.Output("processed_count", display_name="processed_count", tooltip="How many files have been claimed so far. Only ever seen by nodes outside the loop, which never actually fire since the loop never ends on its own."),
			],
			enable_expand 	= True,
			hidden        		= [io.Hidden.unique_id, io.Hidden.dynprompt],
			is_output_node	= True, # always execute this node so users don't have to put an output node afterwards; this is also what keeps the watch loop alive
			is_input_list 	= True, # prevent data lists from executing this node multiple times
		)
		return ret

	# from nodes_looping -> _WhileLoopClose
	@staticmethod
	def _explore_dependencies(node_id, dynprompt, upstream):
		node_info = dynprompt.get_node(node_id)
		if "inputs" not in node_info:
			return
		for value in node_info["inputs"].values():
			if is_link(value):
				parent_id = value[0]
				if parent_id not in upstream:
					upstream[parent_id] = []
					FileWatcherEnd._explore_dependencies(parent_id, dynprompt, upstream)
				upstream[parent_id].append(node_id)

	# from nodes_looping -> _WhileLoopClose
	@staticmethod
	def _collect_contained(node_id, upstream, contained):
		if node_id not in upstream:
			return
		for child_id in upstream[node_id]:
			if child_id not in contained:
				contained[child_id] = True
				FileWatcherEnd._collect_contained(child_id, upstream, contained)

	@classmethod
	def execute(cls, flow_control, **terminations):
		# terminations are pure triggers - we never look at their values, only rely on ComfyUI not
		# scheduling this node until every connected one of them has produced something.
		filewatcher_begin_id, tracked = flow_control[0]

		# from nodes_looping -> _WhileLoopClose
		# BEGIN
		dynprompt = cls.hidden.dynprompt
		unique_id = cls.hidden.unique_id

		upstream = {}
		cls._explore_dependencies(unique_id, dynprompt, upstream)

		contained = {}
		cls._collect_contained(filewatcher_begin_id, upstream, contained)
		contained[unique_id] = True
		contained[filewatcher_begin_id] = True

		graph = GraphBuilder()

		for node_id in contained:
			original_node = dynprompt.get_node(node_id)
			node = graph.node(original_node["class_type"], "Recurse" if node_id == unique_id else node_id)
			node.set_override_display_id(node_id)

		for node_id in contained:
			original_node = dynprompt.get_node(node_id)
			node = graph.lookup_node("Recurse" if node_id == unique_id else node_id)

			for name, value in original_node.get("inputs", {}).items():
				if is_link(value) and value[0] in contained:
					parent = graph.lookup_node("Recurse" if value[0] == unique_id else value[0])
					node.set_input(name, parent.out(value[1]))
				else:
					node.set_input(name, value)
		# END

		filewatcher_begin_new = graph.lookup_node(filewatcher_begin_id)
		filewatcher_end_new   = graph.lookup_node("Recurse")
		filewatcher_begin_new.set_input("_tracked", tracked)

		ret = io.NodeOutput(filewatcher_end_new.out(0), expand=graph.finalize())
		return ret
