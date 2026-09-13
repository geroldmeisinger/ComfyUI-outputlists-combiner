import fnmatch
import os
import queue
import time

from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder, is_link

from .util import *

try:
	# optional dependency: pip install watchdog
	# gives us real OS-level notifications (inotify / FSEvents / ReadDirectoryChangesW)
	# instead of pure polling.
	from watchdog.events import FileSystemEventHandler
	from watchdog.observers import Observer
	_HAS_WATCHDOG = True
except ImportError:
	_HAS_WATCHDOG = False

try:
	# lets the user actually stop the watch loop by hitting "Cancel" in the UI,
	# instead of it looping forever until the server is killed.
	from comfy.model_management import \
	    throw_exception_if_processing_interrupted as _check_interrupted
except ImportError:
	def _check_interrupted():
		pass


FLOWCONTROL_NOTE = "You need to connect the `flow_control` from a `FileWatcherBegin` to a `FileWatcherEnd` node."
DESCRIPTION = f"""Watch a directory for new files and run a sub-workflow once for every file that shows up, one at a time, forever.
{FLOWCONTROL_NOTE}
Unlike `IterateBegin`/`IterateEnd`, this does not iterate a fixed, pre-existing list: it blocks and waits (using an OS-level filesystem notification if the `watchdog` package is installed, otherwise by polling) until a new file appears in `directory`, then runs the sub-workflow on it.
Internally uses the node expansion mechanism which duplicates the sub-workflow again after every processed file, so the loop never really "ends" on its own - cancel the queued prompt to stop it.
Make sure to use the passthrough output slots on output nodes (`Preview Image`, `Save Image` etc.) so the intermediate results are visible.
"""


class FileWatcherBegin(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= DESCRIPTION,
			node_id		= "FileWatcherBegin",
			display_name	= "File Watch Begin",
			search_aliases	= ["Watch Folder Begin", "Watch Directory Begin", "File Watcher Begin", "Directory Watch Begin", "New File Begin"],
			category	= CATEGORY,
			inputs		= [
				io.String	.Input("directory"	, display_name="directory"	, tooltip="Folder to watch for new files."),
				io.String	.Input("file_pattern"	, display_name="file_pattern"	, default="*" , optional=True, tooltip="Only files whose name matches this glob pattern are considered, e.g. `*.png`."),
				io.Float	.Input("poll_interval"	, display_name="poll_interval"	, default=1.0 , min=0.05, max=60.0, optional=True, tooltip="Seconds between checks when no OS-level notification fires (and a safety-net rescan interval even when it does)."),
				io.Float	.Input("stability_delay"	, display_name="stability_delay"	, default=1.0 , min=0.0 , max=60.0, optional=True, tooltip="Seconds a candidate file's size must stay unchanged before it's considered fully written and safe to hand off. Set to 0 to disable."),
				io.AnyType	.Input("_processed"	, display_name="_"	, optional=True, tooltip="Ignore! Only used internally"),
			],
			outputs=[
				io.FlowControl	.Output("flow_control"	, display_name="flow_control"	, tooltip=FLOWCONTROL_NOTE),
				io.String	.Output("filepath"	, display_name="filepath"	, tooltip="Full path of the new file."),
				io.Int	.Output("index"	, display_name="index"	, tooltip="How many files have been fully processed so far (0-based)."),
				io.AnyType	.Output("file_info"	, display_name="file_info"	, tooltip="dict with ctime/mtime/atime of the file at the moment it was picked up. Note: st_ctime is creation time on Windows but inode-change time on Linux/Mac."),
			],
			is_input_list	= True,
			hidden		= [io.Hidden.unique_id],
		)
		return ret

	@staticmethod
	def _unwrap(value, default):
		# every input arrives as a list of length 1 because of is_input_list=True,
		# except _processed on the very first (unconnected) call, which is just None.
		if isinstance(value, list):
			return value[0] if len(value) else default
		return value if value is not None else default

	@staticmethod
	def _list_candidates(directory, processed, pattern):
		try:
			names = os.listdir(directory)
		except OSError:
			return []
		candidates = []
		for name in names:
			if not fnmatch.fnmatch(name, pattern):
				continue
			full = os.path.join(directory, name)
			if not os.path.isfile(full) or full in processed:
				continue
			try:
				st = os.stat(full)
			except OSError:
				continue
			candidates.append((full, st))
		candidates.sort(key=lambda c: c[1].st_mtime) # oldest first -> FIFO processing order
		return candidates

	@staticmethod
	def _is_stable(path, stability_delay):
		if stability_delay <= 0:
			return True
		try:
			size_before = os.path.getsize(path)
		except OSError:
			return False
		_check_interrupted()
		time.sleep(stability_delay)
		try:
			size_after = os.path.getsize(path)
		except OSError:
			return False
		return size_before == size_after

	@staticmethod
	def _wait_for_activity(directory, poll_interval):
		"""Block until something changes in `directory`, or `poll_interval` elapses - whichever comes first."""
		if _HAS_WATCHDOG:
			event_queue = queue.Queue()

			class _Handler(FileSystemEventHandler):
				def on_any_event(self, event):
					event_queue.put(True)

			observer = None
			try:
				observer = Observer()
				observer.schedule(_Handler(), directory, recursive=False)
				observer.start()
			except Exception:
				observer = None # e.g. directory doesn't exist yet - fall back to polling below

			if observer is not None:
				try:
					event_queue.get(timeout=poll_interval)
				except queue.Empty:
					pass
				finally:
					observer.stop()
					observer.join(timeout=poll_interval)
				return

		_check_interrupted()
		time.sleep(poll_interval)

	@classmethod
	def execute(cls, directory, file_pattern=None, poll_interval=None, stability_delay=None, _processed=None, **kwargs) -> io.NodeOutput:
		directory	= cls._unwrap(directory	, None)
		file_pattern	= cls._unwrap(file_pattern	, "*")
		poll_interval	= cls._unwrap(poll_interval	, 1.0)
		stability_delay	= cls._unwrap(stability_delay	, 1.0)
		processed	= cls._unwrap(_processed	, {})
		if not isinstance(processed, dict):
			processed = {}

		candidate = None
		while candidate is None:
			_check_interrupted()
			for full, _ in cls._list_candidates(directory, processed, file_pattern):
				if cls._is_stable(full, stability_delay):
					candidate = (full, os.stat(full)) # re-stat: it just proved stable, get a fresh timestamp
					break
			if candidate is None:
				cls._wait_for_activity(directory, poll_interval)

		filepath, st = candidate
		file_info    = {"path": filepath, "ctime": st.st_ctime, "mtime": st.st_mtime, "atime": st.st_atime}
		flow_control = (cls.hidden.unique_id, processed)
		index        = len(processed)

		ret = io.NodeOutput(flow_control, filepath, index, file_info)
		return ret


class FileWatcherEnd(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= DESCRIPTION,
			node_id		= "FileWatcherEnd",
			display_name	= "File Watch End",
			search_aliases	= ["Watch Folder End", "Watch Directory End", "File Watcher End", "Directory Watch End", "New File End"],
			category	= CATEGORY,
			inputs		= [
				io.FlowControl	.Input("flow_control"	, display_name="flow_control"	, tooltip="Connect it to a `FileWatcherBegin` node"),
				io.AnyType	.Input("item"	, display_name="item"	, tooltip="Connect the (pass-through) result of the sub-workflow here. Its value isn't used for anything except forcing the sub-workflow to finish before the next file is picked up."),
			],
			outputs		= [
				io.Int	.Output("processed_count", display_name="processed_count", tooltip="How many files have been fully processed so far. This value is only ever seen by nodes outside the loop, which never actually fire since the loop never ends."),
			],
			enable_expand	= True,
			hidden		= [io.Hidden.unique_id, io.Hidden.dynprompt],
			is_output_node	= True, # always execute this node so users don't have to put an output node afterwards; this is also what keeps the watch loop alive
			is_input_list	= True, # prevent data lists from executing this node multiple times
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
	def execute(cls, flow_control, item, **kwargs):
		filewatch_begin_id, processed_prev = flow_control[0]
		filepath = item[0] if isinstance(item, list) and len(item) else item

		# mark this file as done - record ctime/mtime/atime at completion time
		processed = dict(processed_prev)
		if isinstance(filepath, str) and filepath:
			try:
				st = os.stat(filepath)
				processed[filepath] = {"ctime": st.st_ctime, "mtime": st.st_mtime, "atime": st.st_atime}
			except OSError:
				processed[filepath] = {"ctime": None, "mtime": None, "atime": None}

		# no termination condition: always clone the sub-workflow and keep watching
		# from nodes_looping -> _WhileLoopClose
		# BEGIN
		dynprompt = cls.hidden.dynprompt
		unique_id = cls.hidden.unique_id

		upstream = {}
		cls._explore_dependencies(unique_id, dynprompt, upstream)

		contained = {}
		cls._collect_contained(filewatch_begin_id, upstream, contained)
		contained[unique_id] = True
		contained[filewatch_begin_id] = True

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

		filewatch_begin_new = graph.lookup_node(filewatch_begin_id)
		filewatch_end_new   = graph.lookup_node("Recurse")
		filewatch_begin_new.set_input("_processed", processed)

		ret = io.NodeOutput(filewatch_end_new.out(0), expand=graph.finalize())
		return ret