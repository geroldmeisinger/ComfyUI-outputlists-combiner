from typing import Iterable

from comfy_api.latest import io

from .util import OUTPUTLIST_NOTE


class StringOutputList(io.ComfyNode):
	@classmethod
	def define_schema(self) -> io.Schema:
		ret = io.Schema(
			description=f"""Create a OutputList by separating the string in the textfield.
`value` and `index` {OUTPUTLIST_NOTE}
""",
			node_id	= "StringOutputList",
			display_name	= "String OutputList",
			category	= "Utility",
			inputs	= [
				io.String.Input("separator", display_name="separator", default="\\n", tooltip="The string to split the textfield values by."),
				io.String.Input("values",
					display_name	= "values",
					multiline	= True,
					default	= "",
					placeholder	= "string separated with newlines. Try to connect inspect_combo with a COMBO input!",
					tooltip	= "The string which will be separated. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed.",
				)
			],
			outputs	= [
				io.AnyType	.Output("value"	, display_name="value"	, is_output_list=True	, tooltip=f"The values from the list. {OUTPUTLIST_NOTE}"	),
				io.Int	.Output("index"	, display_name="index"	, is_output_list=True	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"	),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip=f"The number of items in the list. {OUTPUTLIST_NOTE}"	),
				io.Combo	.Output("inspect_combo"	, display_name="inspect_combo"	, is_output_list=False	, tooltip=f"A dummy output only used to pre-fill the list with values from an other `COMBO` input and will automatically disconnect again"	),
			])
		return ret

	@classmethod
	def execute(self, separator: str, values: Iterable[str]) -> io.NodeOutput:
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value	= [s.strip() for s in values.rstrip().split(unescaped_separator)]
		count	= len(value)
		index	= range(count)
		inspect_combo	= None
		ret	= io.NodeOutput(value, index, count, inspect_combo)
		return ret
