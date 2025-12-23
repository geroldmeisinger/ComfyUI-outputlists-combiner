import re
from collections import defaultdict
from json import dumps, loads

from comfy_api.latest import io
from deepdiff import DeepDiff
from jsonpath_ng import parse

from .util import *

NOTE = "`objs_0` and `more_objs` will be concateneted together and exist for convinience, if you only want to compare two objects."
class WorkflowDiscriminator(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Compare workflows and discriminate differences as JSON paths.
Note that ComfyUI's `IMAGE` doesn't contain the workflow metadata and you need to load the images with specialized image+metadata loaders and connect the metadata to this node.
Custom nodes with metadata loaders include:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`
""",
			node_id      	= "WorkflowDiscriminator",
			display_name 	= "Workflow Discriminator",
			category     	= "Utility",
			is_input_list	= True,
			inputs=[
				io.AnyType 	.Input("objs_0"          	, display_name="objs_0"          	, optional=True                                	, tooltip=f"(optional) A single object (or a list of objects), usually of a workflow. {NOTE}"),
				io.AnyType 	.Input("objs_1"          	, display_name="more_objs"       	, optional=True                                	, tooltip=f"(optional) Another object (or a list of objects), usually of a workflow. {NOTE}"),
				io.String  	.Input("ignore_jsonpaths"	, display_name="ignore_jsonpaths"	, optional=True                                	, tooltip=f"(optional) A list of JSONPaths to ignore in case you want to chain multiple discriminators together."),
				#io.Boolean	.Input("mode"            	, display_name="mode"            	, default=True, label_on="most_frequent", =True	, tooltip=f"Another object (or a list of objects), usually of a workflow. {NOTE}"),
			],
			outputs=[
				io.AnyType	.Output("list_a"   	, display_name="list_a", is_output_list=True   	, tooltip=""),
				io.AnyType	.Output("list_b"   	, display_name="list_b", is_output_list=True   	, tooltip=""),
				io.AnyType	.Output("list_c"   	, display_name="list_c", is_output_list=True   	, tooltip=""),
				io.AnyType	.Output("list_d"   	, display_name="list_d", is_output_list=True   	, tooltip=""),
				io.String 	.Output("jsonpaths"	, display_name="jsonpaths", is_output_list=True	, tooltip=""),
			],
		)
		return ret

	@classmethod
	def execute(self, objs_0: list[any] = [], objs_1: list[any] = [], ignore_jsonpaths: list[str] = []):
		objs 	= [*objs_0, *objs_1]
		datas	= []
		for obj in objs:
			data = None
			if isinstance(obj, str):
				try:
					data = loads(obj)
				except Exception:
					data = obj	# treat raw string as value
			else:
				data = obj
			datas.append(data)
		list_a, list_b, list_c, list_d, jsonpaths = extract_top_changes(datas, 4, ignore_jsonpaths)
		ret = io.NodeOutput(list_a, list_b, list_c, list_d, jsonpaths)
		return ret

def deepdiff_path_to_jsonpath(path: str) -> str:
	if not path.startswith("root"):
		raise ValueError("Invalid DeepDiff path")
	jsonpath	= "$"
	tokens  	= re.findall(r"\['([^']+)'\]|\[(\d+)\]", path[len("root"):])
	for key, index in tokens:
		if key:
			if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", key):
				jsonpath += f".{key}"
			else:
				jsonpath += f"['{key}']"
		else:
			jsonpath += f"[{index}]"
	return jsonpath

def extract_top_changes(objs: list[any], top_n: int, ignore_jsonpaths: list[str] = []):
	baseline	= objs[0]
	objs_n  	= len(objs)

	# Count how many files each path changes in
	change_counts = defaultdict(int)
	for i in range(1, objs_n):
		diff = DeepDiff(baseline, objs[i], ignore_order=True)
		for path in diff.affected_paths:
			change_counts[path] += 1

	# Sort by number of changes desc, then path name asc
	sorted_fields   	= sorted(change_counts.items(), key=lambda x: (-x[1], x[0]))
	sorted_jsonpaths	= [deepdiff_path_to_jsonpath(path) for path, _ in sorted_fields]

	top_jsonpaths = [jsonpath for jsonpath in sorted_jsonpaths if jsonpath not in ignore_jsonpaths][:top_n]

	# Extract values using jsonpath-ng
	value_lists = []
	for jsonpath in top_jsonpaths:
		expr           	= parse(jsonpath)
		values_per_path	= []
		for obj in objs:
			matches = expr.find(obj)
			# jsonpath-ng returns a list of Match objects
			# If multiple matches, just take the first; else None
			if matches:
				value = matches[0].value
				if isinstance(value, list) or isinstance(value, dict):
					values_per_path.append(dumps(value, indent=4))
				else:
					values_per_path.append(value)
		value_lists.append(values_per_path)

	# Ensure always at least top_n lists
	while len(value_lists) < top_n:
		value_lists.append([])
		top_jsonpaths.append("")

	return (*value_lists, top_jsonpaths)

# jsons = [
#     '{ "id": 1, "value": 100, "price": 123, "tax": 10, "discount": 0, "height": 5 }',
#     '{ "id": 2, "value": 100, "price": 234, "tax": 10, "discount": 0, "height": 5 }',
#     '{ "id": 3, "value": 200, "price": 345, "tax": 10, "discount": 0, "height": 5 }',
#     '{ "id": 4, "value": 100, "price": 456, "tax": 10, "discount": 0, "height": 6 }',
#     '{ "id": 5, "value": 200, "price": 567, "tax": 10, "discount": 10, "height": 6 }',
# ]

# ret = extract_top_changes(jsons)

# print(json.dumps(ret))
