import itertools

from comfy_api.latest import io

from .util import INPUTLIST_NOTE, OUTPUTLIST_NOTE


class CombineOutputLists(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Takes up to 4 OutputLists and generates all combinations between them and emits each combination as separate items.

Example: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` {OUTPUTLIST_NOTE}

All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.

Example: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`
""",
			node_id	= "CombineOutputLists",
			display_name	= "OutputLists Combinations",
			category	= "Utility",
			is_input_list	= True,
			inputs=[
				io.AnyType.Input("list_a", display_name="list_a", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_b", display_name="list_b", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_c", display_name="list_c", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_d", display_name="list_d", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
			],
			outputs=[
				io.AnyType	.Output("unzip_a"	, display_name="unzip_a"	, is_output_list=True	, tooltip=f"Value of the combinations corresponding to `list_a`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_b"	, display_name="unzip_b"	, is_output_list=True	, tooltip=f"Value of the combinations corresponding to `list_b`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_c"	, display_name="unzip_c"	, is_output_list=True	, tooltip=f"Value of the combinations corresponding to `list_c`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_d"	, display_name="unzip_d"	, is_output_list=True	, tooltip=f"Value of the combinations corresponding to `list_d`. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("index"	, display_name="index"	, is_output_list=True	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Total number of combinations."),
			],
		)
		return ret

	@classmethod
	def execute(self, list_a: list = [], list_b: list = [], list_c: list = [], list_d: list = []) -> io.NodeOutput:
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product	= list(itertools.product(*normalized))
		transposed	= tuple(map(list, zip(*product)))
		count	= len(product)
		index	= range(count)
		ret	= io.NodeOutput(*transposed, index, count)
		return ret
