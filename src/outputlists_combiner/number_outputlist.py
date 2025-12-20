import numpy
from comfy_api.latest import io

from .util import OUTPUTLIST_NOTE


class NumberOutputList(io.ComfyNode):
	@classmethod
	def define_schema(self) -> io.Schema:
		ret = io.Schema(
			description=f"""Create a OutputList by generating a numbers of values in a range.
Uses [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internally because it works more reliably with floatingpoint values.
If you want to define number lists with arbitrary steps instead check out the JSON OutputList and define an array like `[1, 42, 123]`.
`int`, `float`, `string` and `index` {OUTPUTLIST_NOTE}
""",
			node_id	= "NumberOutputList",
			display_name	= "Number OutputList",
			category	= "Utility",
			inputs	= [
				io.Float	.Input("start"	, display_name="start"	, default=	0	,	tooltip="Start value to generate the range from."	),
				io.Float	.Input("stop"	, display_name="stop"	, default=	10	,	tooltip="End value. If `endpoint=include` this number will be included in the list."	),
				io.Int	.Input("num"	, display_name="num"	, default=	10	, min=1                                  ,	tooltip="The number of items in the list (not to be confused with a `step`)."	),
				io.Boolean	.Input("endpoint"	, display_name="endpoint"	, default=	False	, label_on="include", label_off="exclude",	tooltip="Decides if the `stop` value should be included or excluded in the items."	),
			],
			outputs	= [
				io.Int	.Output("int"	, display_name="int"	, is_output_list=True	, tooltip=f"The value converted to int (rounded down/floored). {OUTPUTLIST_NOTE}"),
				io.Float	.Output("float"	, display_name="float"	, is_output_list=True	, tooltip=f"The value as a float. {OUTPUTLIST_NOTE}"),
				io.String	.Output("string"	, display_name="string"	, is_output_list=True	, tooltip=f"The value as a float converted to string. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("index"	, display_name="index"	, is_output_list=True	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Same as `num`."),
				])
		return ret

	@classmethod
	def execute(self, start: float, stop: float, num: int, endpoint: bool):
		values	= list(numpy.linspace(start, stop, num, endpoint))
		ints	= [int	(v) for v in values]
		floats	= [float	(v) for v in values]
		strs	= [str	(v) for v in values]
		index	= range(num)
		ret	= (ints, floats, strs, index, num)
		return ret
