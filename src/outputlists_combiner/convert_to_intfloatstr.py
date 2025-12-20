import nums_from_string
from comfy_api.latest import io

from .util import OUTPUTLIST_NOTE


class ConvertNumberToIntFloatStr(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description=f"""Convert anything number-like to `INT` `FLOAT` `STRING`.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
Use a string `123;234;345` to quickly generate a list of numbers. Don't use commas as separators as they may be interpreted as thousand-separators.
`int`, `float` and `string` {OUTPUTLIST_NOTE}
""",
			node_id	= "ConvertNumberToIntFloatStr",
			display_name	= "Convert To Int Float Str",
			category	= "Utility",
			is_input_list=True,
			inputs=[
				io.AnyType.Input("number", display_name="any", tooltip="Anything that can be meaningfully converted to a string with parseable numbers inside"),
			],
			outputs=[
				io.Int	.Output("int"	, display_name="int"	, is_output_list=True	, tooltip=f"All the numbers found in the string with the decimals truncated. {OUTPUTLIST_NOTE}"),
				io.Float	.Output("float"	, display_name="float"	, is_output_list=True	, tooltip=f"All the numbers found in the string as floats. {OUTPUTLIST_NOTE}"),
				io.String	.Output("string"	, display_name="string"	, is_output_list=True	, tooltip=f"All the numbers found in the string as floats converted to string. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Amount of numbers found in the value."),
			],
		)
		return ret

	@classmethod
	def execute(self, number: any) -> io.NodeOutput:
		number_str	= str(number)
		floats	= nums_from_string.get_nums(number_str)
		ints	= [int(f) for f in floats]
		strs	= [str(f) for f in floats]
		count	= len(floats)
		ret	= io.NodeOutput(ints, floats, strs, count)
		return ret
