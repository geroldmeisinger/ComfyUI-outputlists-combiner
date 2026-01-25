from comfy_api.latest import io

from .util import INPUTLIST_NOTE


# Define ITEM_LIST type to match inspire-pack's ForeachListBegin input
ItemList = io.Custom("ITEM_LIST")


class OutputListsCompress(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description=f"""Takes up to 4 OutputLists and compresses them into a single ITEM_LIST of tuples.

This node is designed to work with inspire-pack's ForeachListBegin/End nodes. It takes multiple synchronized OutputLists (e.g., from OutputLists Combinations) and packs them into tuples that can be iterated over.

Example:
- `list_a = [7.0, 7.5, 8.0]` (CFG values)
- `list_b = ["euler", "dpm++", "euler"]` (sampler names)
- Result: `[(7.0, "euler"), (7.5, "dpm++"), (8.0, "euler")]`

Connect the `item_list` output **directly** to ForeachListBegin's `item_list` input.
Use **OutputLists Unpack** inside the ForeachList loop to extract individual values from the `item` output.

**Note:** All input lists should have the same length (which is guaranteed when using OutputLists Combinations).

**Important:** Do NOT use WorklistToItemList between this node and ForeachListBegin - connect directly!
""",
			node_id="OutputListsCompress",
			display_name="OutputLists Compress",
			category="Utility",
			is_input_list=True,
			inputs=[
				io.AnyType.Input("list_a", display_name="list_a", tooltip=f"First list (required). {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_b", display_name="list_b", optional=True, tooltip=f"(optional) Second list. {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_c", display_name="list_c", optional=True, tooltip=f"(optional) Third list. {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_d", display_name="list_d", optional=True, tooltip=f"(optional) Fourth list. {INPUTLIST_NOTE}"),
			],
			outputs=[
				ItemList.Output("item_list", display_name="item_list", tooltip="ITEM_LIST of tuples for inspire-pack's ForeachListBegin. Connect directly - do NOT use WorklistToItemList!"),
				io.Int.Output("count", display_name="count", tooltip="Number of items in the compressed list."),
			],
		)
		return ret

	@classmethod
	def execute(cls, list_a: list, list_b: list = None, list_c: list = None, list_d: list = None) -> io.NodeOutput:
		# Collect all provided lists
		lists = [list_a]
		
		if list_b is not None and len(list_b) > 0:
			lists.append(list_b)
		if list_c is not None and len(list_c) > 0:
			lists.append(list_c)
		if list_d is not None and len(list_d) > 0:
			lists.append(list_d)
		
		# Zip the lists into tuples
		# zip() stops at the shortest list, but for synchronized outputs
		# from CombineOutputLists they should all be the same length
		zipped = list(zip(*lists))
		count = len(zipped)
		
		return io.NodeOutput(zipped, count)

