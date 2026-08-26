from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder, is_link

from .util import INPUTLIST_NOTE, OUTPUTLIST_NOTE

FLOWCONTROL_NOTE	= "You need to connect the `flow_control` from a `IterateBegin` to a `IterateEnd` node."
DESCRIPTION = f"""Iterate a sub-workflow by executing it from a data list sequentially in item-major order (as opposed to node-major)."
{FLOWCONTROL_NOTE}
Only use this if a sub-workflow takes a long time to process without any visible progress (see [execution stalling problem](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner#the-execution-stalling-problem)).
Make sure to use the passthrough output slots on output nodes (`Preview Image`, `Save Image` etc.) so the intermediate results are visible.
Internally uses the node expansion mechanism which duplicates the sub-workflow multiple times for each list item.

`lists` {OUTPUTLIST_NOTE}
"""

class IterateBegin(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description 	= DESCRIPTION,
			node_id     	= "IterateBegin",
			display_name	= "Iterate Begin",
			category    	= "Utility",
			inputs      	= [
				io.AnyType	.Input("datalist"	, display_name="datalist"            	, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType	.Input("_results"	, display_name="_", optional=True    	, tooltip="Ignore! Only used internally"),
				#io.String	.Input("label"   	, display_name="label", optional=True	, tooltip=""),
			],
			outputs=[
				io.FlowControl	.Output("flow_control"	, display_name="flow_control"	, tooltip=FLOWCONTROL_NOTE	),
				io.AnyType    	.Output("item"        	, display_name="item"        	, tooltip=""              	),
				io.Int        	.Output("index"       	, display_name="index"       	, tooltip=""              	),
			],
			is_input_list    	= True,
			accept_all_inputs	= True,
			hidden           	= [io.Hidden.unique_id],
			#is_output_node  	= True,
		)
		return ret

	@classmethod
	def execute(cls, datalist: list, _results: list = [], **kwargs) -> io.NodeOutput:
		results     	= _results[0] if isinstance(_results, list) and len(_results) == 1 else []
		flow_control	= (cls.hidden.unique_id, results, len(datalist))
		index       	= len(results)
		item        	= datalist[index]
		ret         	= io.NodeOutput(flow_control, item, index)
		return ret


class IterateEnd(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description 	= DESCRIPTION,
			node_id     	= "IterateEnd",
			display_name	= "Iterate End",
			category    	= "Utility",
			inputs      	= [
				io.FlowControl	.Input("flow_control"	, display_name="flow_control"        	, tooltip="Connect it to a `IterateBegin` node"	),
				io.AnyType    	.Input("item"        	, display_name="item"                	, tooltip=FLOWCONTROL_NOTE                     	),
				#io.String    	.Input("label"       	, display_name="label", optional=True	, tooltip=""),
			],
			outputs	= [
				io.AnyType.Output("datalist", display_name="datalist", is_output_list=True, tooltip=f"{OUTPUTLIST_NOTE}"),
			],
			enable_expand 	= True,
			hidden        	= [io.Hidden.unique_id, io.Hidden.dynprompt],
			is_output_node	= True, # always execute this node so users don't have to put an output node afterwards
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
					IterateEnd._explore_dependencies(parent_id, dynprompt, upstream)
				upstream[parent_id].append(node_id)

	# from nodes_looping -> _WhileLoopClose
	@staticmethod
	def _collect_contained(node_id, upstream, contained):
		if node_id not in upstream:
			return
		for child_id in upstream[node_id]:
			if child_id not in contained:
				contained[child_id] = True
				IterateEnd._collect_contained(child_id, upstream, contained)

	@classmethod
	def execute(cls, flow_control, item, **kwargs):
		iterate_begin_id, results_prev, length = flow_control[0]
		results = results_prev + (item if len(item) == 1 else [item]) # check if item is a unit or a data list and convert to python list

		if len(results) >= length:
			# HACK why do I have to add a list layer for every recursion?
			results_rec = results
			for _ in range(length - 1):
				results_rec = [results_rec]
			ret = io.NodeOutput(results_rec)
			return ret

		# from nodes_looping -> _WhileLoopClose
		# BEGIN
		dynprompt = cls.hidden.dynprompt
		unique_id = cls.hidden.unique_id

		upstream = {}
		cls._explore_dependencies(unique_id, dynprompt, upstream)

		contained = {}
		cls._collect_contained(iterate_begin_id, upstream, contained)
		contained[unique_id] = True
		contained[iterate_begin_id] = True

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

		iterate_begin_new	= graph.lookup_node(iterate_begin_id)
		iterate_end_new  	= graph.lookup_node("Recurse")
		iterate_begin_new.set_input("_results", results)

		ret = io.NodeOutput(iterate_end_new.out(0), expand=graph.finalize())
		return ret
