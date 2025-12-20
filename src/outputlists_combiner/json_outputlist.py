from json import dumps, loads

from comfy_api.latest import io
from fastnumbers import try_float
from jsonpath_ng import parse as jsonpath_parse

from .util import OUTPUTLIST_NOTE


class JSONOutputList(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Create a OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All matched values will be flattend into one list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
`key`, `value`, `int` and `float` {OUTPUTLIST_NOTE}
""",
			node_id	= "JSONOutputList",
			display_name	= "JSON OutputList",
			category	= "Utility",
			inputs	= [
				io.String.Input("jsonpath", display_name="jsonpath", default="$.dict", tooltip="JSONPath used to extract the values."),
				io.String.Input("json",
					display_name	= "json",
					default	= dumps(loads('{ "dict" : { "a": 0.12, "b": 3.45, "c": 6.78 }, "arr": [0.12, 3.45, 6.78] }'), indent=4),
					multiline	= True,
					placeholder	= "Object or JSON string",
					tooltip	= "A JSON string which will be parsed to an object."
				),
				io.AnyType.Input("obj", display_name="obj", optional=True, tooltip="(optional) object of any type which will replace the JSON string"),
			],
			outputs	= [
				io.String	.Output("key"	, display_name="key"	, is_output_list=True	, tooltip=f"The key for dictionaries or index for arrays (as string). {OUTPUTLIST_NOTE} Technically it's a global index of the flattened list for all non-keys."),
				io.String	.Output("value"	, display_name="value"	, is_output_list=True	, tooltip=f"The value as a string. {OUTPUTLIST_NOTE}"),
				io.Int	.Output("int"	, display_name="int"	, is_output_list=True	, tooltip=f"The value as a int (if not parseable number default to 0). {OUTPUTLIST_NOTE}"),
				io.Float	.Output("float"	, display_name="float"	, is_output_list=True	, tooltip=f"The value as a float (if not parseable number default to 0). {OUTPUTLIST_NOTE}"),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Total number of items in the flattened list"),
				io.String	.Output("debug"	, display_name="debug"	, is_output_list=False	, tooltip="Debug output of all matched objects as a formatted JSON string"),
			]
		)
		return ret

	@classmethod
	def execute(cls, jsonpath, json, obj=None) -> io.NodeOutput:
		# parse JSON
		if obj:
			if isinstance(obj, str):
				try:
					data = loads(obj)
				except Exception:
					data = obj	# treat raw string as value
			else:
				data = obj
		else:
			if isinstance(json, str):
				try:
					data = loads(json)
				except Exception:
					data = json	# treat raw string as value
			else:
				data = json

		# jsonpath
		try:
			expr	= jsonpath_parse(jsonpath)
			matches	= expr.find(data)
		except Exception:
			return io.NodeOutput([], [], [], [], 0, "[]", ui={ "obj": [dumps(obj, indent=4)] })

		if not matches:
			return io.NodeOutput([], [], [], [], 0, "[]", ui={ "obj": [dumps(obj, indent=4)] })

		# outputs
		keys	= []
		values	= []
		ints	= []
		floats	= []
		count	= 0
		debug	= [m.value for m in matches]

		def append(key, value):
			f = try_float(value, allow_underscores=True, nan=0.0, inf=0.0, on_fail=0.0, on_type_error=0.0)
			keys	.append(str(key))
			values	.append(str(value))
			floats	.append(f)
			ints	.append(int(f))

		# iterate and flatten matches
		for m in matches:
			target = m.value

			if isinstance(target, dict):
				for key, value in target.items():
					append(key, value)
					count += 1
			elif isinstance(target, list):
				for value in target:
					append(count, value)
					count += 1
			else: # scalar1
				append(count, target)
				count += 1

		debug_json = dumps(debug, indent=4)

		ret = io.NodeOutput(keys, values, ints, floats, count, debug_json, ui={ "obj": [dumps(data, indent=4)] })
		return ret
