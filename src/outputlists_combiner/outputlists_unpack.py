from comfy_api.latest import io


class OutputListsUnpack(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description="""Unpacks a tuple from OutputLists Compress into separate values.

This node is designed to work inside a ForeachList loop. It takes the `item` output from ForeachListBegin (which contains a tuple created by OutputLists Compress) and unpacks it into up to 4 separate outputs.

Example:
- Input: `(7.0, "euler", 20, "positive prompt")`
- Outputs: 
  - `value_a = 7.0`
  - `value_b = "euler"`
  - `value_c = 20`
  - `value_d = "positive prompt"`

If the tuple has fewer than 4 elements, the remaining outputs will be `None`.

**Typical workflow:**
1. OutputLists Compress → ITEM_LIST
2. ForeachListBegin → item (tuple)
3. **OutputLists Unpack** → separate values
4. Use values in your workflow (e.g., KSampler)
5. ForeachListEnd → loop or finish
""",
			node_id="OutputListsUnpack",
			display_name="OutputLists Unpack",
			category="Utility",
			inputs=[
				io.AnyType.Input("packed_item", display_name="packed_item", tooltip="The tuple from ForeachListBegin's 'item' output. This should be connected to the 'item' output of ForeachListBegin."),
			],
			outputs=[
				io.AnyType.Output("value_a", display_name="value_a", tooltip="First element of the tuple (index 0)."),
				io.AnyType.Output("value_b", display_name="value_b", tooltip="Second element of the tuple (index 1), or None if tuple is shorter."),
				io.AnyType.Output("value_c", display_name="value_c", tooltip="Third element of the tuple (index 2), or None if tuple is shorter."),
				io.AnyType.Output("value_d", display_name="value_d", tooltip="Fourth element of the tuple (index 3), or None if tuple is shorter."),
			],
		)
		return ret

	@classmethod
	def execute(cls, packed_item) -> io.NodeOutput:
		# Handle both tuple and list inputs
		if isinstance(packed_item, (tuple, list)):
			values = list(packed_item)
		else:
			# Single value case - wrap in list
			values = [packed_item]
		
		# Pad to 4 elements with None
		while len(values) < 4:
			values.append(None)
		
		return io.NodeOutput(values[0], values[1], values[2], values[3])

