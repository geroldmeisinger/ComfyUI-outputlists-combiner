import base64
import hashlib
import itertools
import re
from io import BytesIO, StringIO
from json import dumps, loads

import chardet
import comfy.samplers
import folder_paths
import node_helpers
import numpy
import numpy as np
import nums_from_string
import pandas as pd
import torch
from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder
from fastnumbers import try_float
from jsonpath_ng import parse as jsonpath_parse
from PIL import Image, ImageOps, ImageSequence, UnidentifiedImageError

from .util import INPUTLIST_NOTE, OUTPUTLIST_NOTE


class StringOutputList(io.ComfyNode):
	@classmethod
	def define_schema(self) -> io.Schema:
		ret = io.Schema(
			description=f"""Create a OutputList by separating the string in the textfield.
`value` and `index` {OUTPUTLIST_NOTE}
""",
			node_id     	= "StringOutputList",
			display_name	= "String OutputList",
			category    	= "Utility",
			inputs      	= [
				io.String.Input("separator", display_name="separator", default="\\n", tooltip="The string to split the textfield values by."),
				io.String.Input("values",
					display_name	= "values",
					multiline   	= True,
					default     	= "",
					placeholder 	= "string separated with newlines. Try to connect inspect_combo with a COMBO input!",
					tooltip     	= "The string which will be separated. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed.",
				)
			],
			outputs	= [
				io.AnyType	.Output("value"        	, display_name="value"        	, is_output_list=True 	, tooltip=f"The values from the list. {OUTPUTLIST_NOTE}"                                                                                  	),
				io.Int    	.Output("index"        	, display_name="index"        	, is_output_list=True 	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"                                                           	),
				io.Int    	.Output("count"        	, display_name="count"        	, is_output_list=False	, tooltip=f"The number of items in the list. {OUTPUTLIST_NOTE}"                                                                           	),
				io.Combo  	.Output("inspect_combo"	, display_name="inspect_combo"	, is_output_list=False	, tooltip=f"A dummy output only used to pre-fill the list with values from an other `COMBO` input and will automatically disconnect again"	),
			])
		return ret

	@classmethod
	def execute(self, separator, values) -> io.NodeOutput:
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value              	= [s.strip() for s in values.rstrip().split(unescaped_separator)]
		count              	= len(value)
		index              	= range(count)
		inspect_combo      	= None
		ret                	= io.NodeOutput(value, index, count, inspect_combo)
		return ret

class NumberOutputList(io.ComfyNode):
	@classmethod
	def define_schema(self) -> io.Schema:
		ret = io.Schema(
			description=f"""Create a OutputList by generating a numbers of values in a range.
Uses `[numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)` internally because it works more reliably with floatingpoint values.
If you want to define number lists with arbitrary steps instead check out the JSON OutputList and define an array like `[1, 42, 123]`.
`int`, `float`, `string` and `index` {OUTPUTLIST_NOTE}
""",
			node_id     	= "NumberOutputList",
			display_name	= "Number OutputList",
			category    	= "Utility",
			inputs      	= [
				io.Float  	.Input("start"   	, display_name="start"   	, default= 	0   	,                                         	tooltip="Start value to generate the range from."                                   	),
				io.Float  	.Input("stop"    	, display_name="stop"    	, default=	10   	,                                         	tooltip="End value. If `endpoint=include` this number will be included in the list."	),
				io.Int    	.Input("num"     	, display_name="num"     	, default=	10   	, min=1                                  ,	tooltip="The number of items in the list (not to be confused with a `step`)."       	),
				io.Boolean	.Input("endpoint"	, display_name="endpoint"	, default=	False	, label_on="include", label_off="exclude",	tooltip="Decides if the `stop` value should be included or excluded in the items."  	),
			],
			outputs	= [
				io.Int   	.Output("int"   	, display_name="int"   	, is_output_list=True 	, tooltip=f"The value converted to int (rounded down/floored). {OUTPUTLIST_NOTE}"),
				io.Float 	.Output("float" 	, display_name="float" 	, is_output_list=True 	, tooltip=f"The value as a float. {OUTPUTLIST_NOTE}"),
				io.String	.Output("string"	, display_name="string"	, is_output_list=True 	, tooltip=f"The value as a float converted to string. {OUTPUTLIST_NOTE}"),
				io.Int   	.Output("index" 	, display_name="index" 	, is_output_list=True 	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"),
				io.Int   	.Output("count" 	, display_name="count" 	, is_output_list=False	, tooltip="Same as `num`."),
				])
		return ret

	@classmethod
	def execute(self, start, stop, num, endpoint):
		values	= list(numpy.linspace(start, stop, num, endpoint))
		ints  	= [int  	(v) for v in values]
		floats	= [float	(v) for v in values]
		strs  	= [str  	(v) for v in values]
		index 	= range(num)
		ret   	= (ints, floats, strs, index, num)
		return ret

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
			node_id     	= "JSONOutputList",
			display_name	= "JSON OutputList",
			category    	= "Utility",
			inputs      	= [
				io.String.Input("jsonpath", display_name="jsonpath", default="$.dict", tooltip="JSONPath used to extract the values."),
				io.String.Input("json",
					display_name	= "json",
					default     	= dumps(loads('{ "dict" : { "a": 0.12, "b": 3.45, "c": 6.78 }, "arr": [0.12, 3.45, 6.78] }'), indent=4),
					multiline   	= True,
					placeholder 	= "Object or JSON string",
					tooltip     	= "A JSON string which will be parsed to an object."
				),
				io.AnyType.Input("obj", display_name="obj", optional=True, tooltip="(optional) object of any type which will replace the JSON string"),
			],
			outputs	= [
				io.String	.Output("key"  	, display_name="key"  	, is_output_list=True 	, tooltip=f"The key for dictionaries or index for arrays (as string). {OUTPUTLIST_NOTE} Technically it's a global index of the flattened list for all non-keys."),
				io.String	.Output("value"	, display_name="value"	, is_output_list=True 	, tooltip=f"The value as a string. {OUTPUTLIST_NOTE}"),
				io.Int   	.Output("int"  	, display_name="int"  	, is_output_list=True 	, tooltip=f"The value as a int (if not parseable number default to 0). {OUTPUTLIST_NOTE}"),
				io.Float 	.Output("float"	, display_name="float"	, is_output_list=True 	, tooltip=f"The value as a float (if not parseable number default to 0). {OUTPUTLIST_NOTE}"),
				io.Int   	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Total number of items in the flattened list"),
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
			expr   	= jsonpath_parse(jsonpath)
			matches	= expr.find(data)
		except Exception:
			return io.NodeOutput([], [], [], [], 0, "[]", ui={ "obj": [dumps(obj, indent=4)] })

		if not matches:
			return io.NodeOutput([], [], [], [], 0, "[]", ui={ "obj": [dumps(obj, indent=4)] })

		# outputs
		keys  	= []
		values	= []
		ints  	= []
		floats	= []
		count 	= 0
		debug 	= [m.value for m in matches]

		def append(key, value):
			f = try_float(value, allow_underscores=True, nan=0.0, inf=0.0, on_fail=0.0, on_type_error=0.0)
			keys  	.append(str(key))
			values	.append(str(value))
			floats	.append(f)
			ints  	.append(int(f))

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

class SpreadsheetOutputList(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Create a OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Use `Load any File` node to load a file as base64.
Internally uses pandas [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
All lists {OUTPUTLIST_NOTE}
""",
			node_id     	= "SpreadsheetOutputList",
			display_name	= "Spreadsheet OutputList",
			category    	= "Utility",
			inputs      	= [
				io.String	.Input("rows_and_cols"	, display_name="rows_and_cols"	, default=	"A B C D"	,             	tooltip="Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`)."),
				io.Int   	.Input("header_rows"  	, display_name="header_rows"  	, default= 	1, min=  	0, max=65535,	tooltip="Ignore the first x rows in the list. Only used if you specify a col in `rows_and_cols`."),
				io.Int   	.Input("header_cols"  	, display_name="header_cols"  	, default= 	1, min=  	0, max=65535,	tooltip="Ignore the first x cols in the list. Only used if you specify a row in `rows_and_cols`."),
				io.Int   	.Input("select_nth"   	, display_name="select_nth"   	, default=	-1, min= 	-1, max=65535,	tooltip="Only select the nth entry (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern."),
				io.String	.Input("string_or_base64",
					display_name	= "string_or_base64",
					multiline   	= True,
					default     	= "",
					placeholder 	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
					tooltip     	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
				)
			],
			outputs=[
				io.String	.Output("list_a"	, display_name="list_a"	, is_output_list=True 	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_b"	, display_name="list_b"	, is_output_list=True 	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_c"	, display_name="list_c"	, is_output_list=True 	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_d"	, display_name="list_d"	, is_output_list=True 	, tooltip=OUTPUTLIST_NOTE),
				io.Int   	.Output("count" 	, display_name="count" 	, is_output_list=False	, tooltip="Number of items in the longest list."),
			]
		)
		return ret

	@staticmethod
	def is_valid_selector(re, sel):
		ret = re.match(sel) is not None
		return ret

	@staticmethod
	def col_to_index(col):
		total = 0
		for c in col.upper():
			total = total * 26 + (ord(c) - 64)
		return total - 1

	@classmethod
	def execute(self, string_or_base64, rows_and_cols, header_rows, header_cols, select_nth):
		limit	= 4
		data 	= string_or_base64.strip()

		# load spreadsheet with pandas
		try:
			decoded	= base64.b64decode(data, validate=True)
			xls    	= pd.read_excel(BytesIO(decoded), sheet_name=None, header=None)
		except Exception:
			try:
				df 	= pd.read_csv(StringIO(data), sep=None, engine="python", header=None)
				xls	= {None: df}
			except Exception:
				return ([[] for _ in range(limit)], 0)

		sheet_names  	= list(xls.keys())
		default_sheet	= sheet_names[0]

		# regex to select rows and columns with optional sheet reference (e.g. A, 1, AB, $MySheet.123, $'My Sheet'.ABC)
		re_sheet_row_and_col = re.compile(r"""
^(?:\$
	(?:
		'([^']+)' |
		"([^"]+)" |
		([^.]+)
	)
	\.
)?
([A-Za-z]+|\d+)
$""", re.VERBOSE)

		raw = re.split(r"[^A-Za-z0-9$.'\"]+", rows_and_cols or "")
		raw = [s for s in raw if s]

		if not raw:
			selectors = ["A", "B", "C", "D"][:limit]
		else:
			selectors = []
			for sel in raw:
				if re_sheet_row_and_col.match(sel) is not None:
					selectors.append(sel)
				if len(selectors) >= limit: break

		results = [[] for _ in range(len(selectors))]

		# select lists from rows and columns
		for i, sel in enumerate(selectors):
			m = re_sheet_row_and_col.match(sel)
			if not m: continue

			sheet	= m.group(1) or m.group(2) or m.group(3) or default_sheet
			key  	= m.group(4)

			if sheet not in xls: continue

			df = xls[sheet]
			if key.isdigit(): # select by row
				row = int(key) - 1 # row selector (1-based)
				if 0 <= row < df.shape[0]:
					results[i] = ["" if (x != x or x is None) else str(x) for x in df.iloc[row, header_cols:].tolist()]
			else: # select by column
				col = SpreadsheetOutputList.col_to_index(key)
				if 0 <= col < df.shape[1]:
					results[i] = ["" if (x != x or x is None) else str(x) for x in df.iloc[header_rows:, col].tolist() ]

		lists = (results + [[]] * limit)[:limit] # pad unused slots with empty lists

		# select nth entry if specified
		if select_nth >= 0: lists = [[lst[select_nth]] if select_nth < len(lst) else [] for lst in lists]

		count = max(map(len, lists), default=0) # longest list

		return (*lists, count)

class CombineOutputLists(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Takes up to 4 OutputLists and generates all combinations between them and emits each combination as separate items.

Example:
```
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
```

`unzip_a` .. `unzip_d` {OUTPUTLIST_NOTE}

All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.

Example:
```
[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]
```
""",
			node_id      	= "CombineOutputLists",
			display_name 	= "OutputLists Combinations",
			category     	= "Utility",
			is_input_list	= True,
			inputs=[
				io.AnyType.Input("list_a", display_name="list_a", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_b", display_name="list_b", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_c", display_name="list_c", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
				io.AnyType.Input("list_d", display_name="list_d", optional=True, tooltip=f"(optional) {INPUTLIST_NOTE}"),
			],
			outputs=[
				io.AnyType	.Output("unzip_a"	, display_name="unzip_a"	, is_output_list=True 	, tooltip=f"Value of the combinations corresponding to `list_a`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_b"	, display_name="unzip_b"	, is_output_list=True 	, tooltip=f"Value of the combinations corresponding to `list_b`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_c"	, display_name="unzip_c"	, is_output_list=True 	, tooltip=f"Value of the combinations corresponding to `list_c`. {OUTPUTLIST_NOTE}"),
				io.AnyType	.Output("unzip_d"	, display_name="unzip_d"	, is_output_list=True 	, tooltip=f"Value of the combinations corresponding to `list_d`. {OUTPUTLIST_NOTE}"),
				io.Int    	.Output("index"  	, display_name="index"  	, is_output_list=True 	, tooltip=f"Range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}"),
				io.Int    	.Output("count"  	, display_name="count"  	, is_output_list=False	, tooltip="Total number of combinations."),
			],
		)
		return ret

	@classmethod
	def execute(self, list_a = [], list_b = [], list_c = [], list_d = []):
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product   	= list(itertools.product(*normalized))
		transposed	= tuple(map(list, zip(*product)))
		count     	= len(product)
		index     	= range(count)
		ret       	= (*transposed, index, count)
		return ret

class FormattedString(io.ComfyNode):
	DESCRIPTION = """Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.
"""

	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description 	= FormattedString.DESCRIPTION,
			node_id     	= "FormattedString",
			display_name	= "Formatted String",
			category    	= "Utility",
			inputs      	= [
				io.String.Input("fstring",
					display_name	= "fstring",
					multiline   	= True,
					default     	= "{a}_{b}_{c}_{d}",
					tooltip     	= FormattedString.DESCRIPTION,
				),
				io.AnyType.Input("a", display_name="a", optional=True, tooltip="(optional) value that will be as a string at the `{a}` placeholder."),
				io.AnyType.Input("b", display_name="b", optional=True, tooltip="(optional) value that will be as a string at the `{b}` placeholder."),
				io.AnyType.Input("c", display_name="c", optional=True, tooltip="(optional) value that will be as a string at the `{c}` placeholder."),
				io.AnyType.Input("d", display_name="d", optional=True, tooltip="(optional) value that will be as a string at the `{d}` placeholder."),
			],
			outputs=[
				io.String.Output("string", display_name="string", is_output_list=False, tooltip="The formatted string with all placeholders replaced with their respective values."),
			],
		)
		return ret

	@classmethod
	def execute(self, fstring, a = "", b = "", c = "", d = ""):
		ret = (fstring.format(a=a, b=b, c=c, d=d),)
		return ret

class ConvertNumberToIntFloatStr(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description=f"""Convert anything number-like to `INT` `FLOAT` `STRING`.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
Use a string `123;234;345` to quickly generate a list of numbers. Don't use commas as separators as they may be interpreted as thousand-separators.
`int`, `float` and `string` {OUTPUTLIST_NOTE}
""",
			node_id     	= "ConvertNumberToIntFloatStr",
			display_name	= "Convert To Int Float Str",
			category    	= "Utility",
			is_input_list=True,
			inputs=[
				io.AnyType.Input("number", display_name="any", tooltip="Anything that can be meaningfully converted to a string"),
			],
			outputs=[
				io.Int   	.Output("int"   	, display_name="int"   	, is_output_list=True 	, tooltip=f"All the numbers found in the string with the decimals truncated. {OUTPUTLIST_NOTE}"),
				io.Float 	.Output("float" 	, display_name="float" 	, is_output_list=True 	, tooltip=f"All the numbers found in the string as floats. {OUTPUTLIST_NOTE}"),
				io.String	.Output("string"	, display_name="string"	, is_output_list=True 	, tooltip=f"All the numbers found in the string as floats converted to string. {OUTPUTLIST_NOTE}"),
				io.Int   	.Output("count" 	, display_name="count" 	, is_output_list=False	, tooltip="Amount of numbers found in the value."),
			],
		)
		return ret

	@classmethod
	def execute(self, number_any):
		number_str	= str(number_any)
		floats    	= nums_from_string.get_nums(number_str)
		ints      	= [int(f) for f in floats]
		strs      	= [str(f) for f in floats]
		count     	= len(floats)
		ret       	= (ints, floats, strs, count)
		return ret

class LoadAnyFile(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE`.
""",
			node_id     	= "LoadAnyFile",
			display_name	= "Load Any File",
			category    	= "Utility",
			inputs      	= [
				io.String.Input("annotated_filepath", tooltip="Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory."),
			],
			outputs	= [
				io.String	.Output("string"	, display_name="string"	, is_output_list=False, tooltip="File content for text files, base64 for binary files."),
				io.Image 	.Output("image" 	, display_name="image" 	, is_output_list=False, tooltip="Image batch tensor."),
				io.Mask  	.Output("mask"  	, display_name="mask"  	, is_output_list=False, tooltip="Mask batch tensor."),
			],
		)
		return ret

	@classmethod
	def load_image(self, image_data):
		img = node_helpers.pillow(Image.open, image_data)

		# from ComfyUI/nodes.py LoadImage
		output_images	= []
		output_masks 	= []
		w, h         	= None, None

		excluded_formats = ['MPO']

		for i in ImageSequence.Iterator(img):
			i = node_helpers.pillow(ImageOps.exif_transpose, i)

			if i.mode == 'I':
				i = i.point(lambda i: i * (1 / 255))
			image = i.convert("RGB")

			if len(output_images) == 0:
				w = image.size[0]
				h = image.size[1]

			if image.size[0] != w or image.size[1] != h:
				continue

			image = np.array(image).astype(np.float32) / 255.0
			image = torch.from_numpy(image)[None,]
			if 'A' in i.getbands():
				mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
				mask = 1. - torch.from_numpy(mask)
			elif i.mode == 'P' and 'transparency' in i.info:
				mask = np.array(i.convert('RGBA').getchannel('A')).astype(np.float32) / 255.0
				mask = 1. - torch.from_numpy(mask)
			else:
				mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
			output_images	.append(image)
			output_masks 	.append(mask.unsqueeze(0))

		if len(output_images) > 1 and img.format not in excluded_formats:
			output_image	= torch.cat(output_images	, dim=0)
			output_mask 	= torch.cat(output_masks 	, dim=0)
		else:
			output_image	= output_images[0]
			output_mask 	= output_masks[0]

		return (output_image, output_mask)

	@classmethod
	def execute(self, annotated_filepath):
		file_path = folder_paths.get_annotated_filepath(annotated_filepath)

		with open(file_path, "rb") as f:
			raw_data = f.read()

		# check if binary
		try:
			result  	= chardet.detect(raw_data)
			encoding	= result["encoding"]
			if encoding:
				filecontent = raw_data.decode(encoding)
			else:
				filecontent = None
		except (UnicodeDecodeError, TypeError):
			filecontent = None

		# check if base64
		if filecontent is not None:
			try:
				_ = base64.b64decode(filecontent, validate=True)
				is_binary = False
			except (base64.binascii.Error, ValueError):
				is_binary = True
		else:
			is_binary = True

		# get file content as text or base64
		if is_binary or filecontent is None:
			filecontent = base64.b64encode(raw_data).decode("utf-8")
			image_data = raw_data
		else:
			image_data = filecontent.encode("utf-8")

		# try to load binary or base64 as image
		try:
			image, mask = self.load_image(BytesIO(image_data))
		except (UnidentifiedImageError, OSError, ValueError):
			# fallback to black 64x64 tensors
			image	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")
			mask 	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")

		return (filecontent, image, mask)

	@classmethod
	def IS_CHANGED(s, annotated_filepath):
		path	= folder_paths.get_annotated_filepath(annotated_filepath)
		m   	= hashlib.sha256()
		with open(path, 'rb') as f:
			m.update(f.read())
		ret = m.digest().hex()
		return ret

	@classmethod
	def VALIDATE_INPUTS(s, annotated_filepath):
		path = folder_paths.get_annotated_filepath(annotated_filepath)
		if not folder_paths.exists_annotated_filepath(path):
			return "Invalid file: {}".format(path)

		return True

class KSamplerImmediateSave(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		return io.Schema(
			description	= """Node expansion of default `KSampler`, `VAE Decode` and `Save Image` to process as one.
This is useful if you want to save the intermediate images for grids immediately.

*"A custom KSampler just to save an image? Now I have become the very thing I sought to destroy!"*
""",
			node_id     	= "KSamplerImmediateSave",
			display_name	= "KSampler Immediate Save",
			category    	= "_for_testing",
			inputs      	= [
				# KSampler inputs
				io.Model       	.Input("model"       	, display_name="model"       	,                                                                      	tooltip="The model used for denoising the input latent."),
				io.Conditioning	.Input("positive"    	, display_name="positive"    	,                                                                      	tooltip="The conditioning describing the attributes you want to include in the image."),
				io.Conditioning	.Input("negative"    	, display_name="negative"    	,                                                                      	tooltip="The conditioning describing the attributes you want to exclude from the image."),
				io.Latent      	.Input("latent_image"	, display_name="latent_image"	,                                                                      	tooltip="The latent image to denoise."),
				io.Vae         	.Input("vae"         	, display_name="vae"         	,                                                                      	tooltip="The VAE model used for decoding the latent."),
				io.Int         	.Input("seed"        	, display_name="seed"        	, default=0, min=0, max=0xfffffffffffffff, control_after_generate=True,	tooltip="The random seed used for creating the noise."),
				io.Int         	.Input("steps"       	, display_name="steps"       	, default=20, min=1, max=10000,                                        	tooltip="The number of steps used in the denoising process."),
				io.Float       	.Input("cfg"         	, display_name="cfg"         	, default=8.0, min=0.0, max=100.0, step=0.1, round=0.01,               	tooltip="The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."),
				io.Combo       	.Input("sampler_name"	, display_name="sampler_name"	, options=comfy.samplers.KSampler.SAMPLERS,                            	tooltip="The algorithm used when sampling , this can affect the quality , speed , and style of the generated output."),
				io.Combo       	.Input("scheduler"   	, display_name="scheduler"   	, options=comfy.samplers.KSampler.SCHEDULERS,                          	tooltip="The scheduler controls how noise is gradually removed to form the image."),
				io.Float       	.Input("denoise"     	, display_name="denoise"     	, default=1.0, min=0.0, max=1.0, step=0.01,                            	tooltip="The amount of denoising applied , lower values will maintain the structure of the initial image allowing for image to image sampling."),
				# SaveImage input
				io.String.Input("filename_prefix", default="ComfyUI", tooltip="The prefix for the file to save. This may include formatting information such as %date :yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes."),
			],
			outputs=[
				io.Image.Output("image", is_output_list=False, tooltip="The decoded image."),
			],
			is_output_node=True,
			enable_expand=True,
		)

	@classmethod
	def execute(self, model, positive, negative, latent_image, vae, seed, steps, cfg, sampler_name, scheduler, denoise, filename_prefix):
		graph 	= GraphBuilder()
		latent	= graph.node("KSampler" , model=model, positive=positive, negative=negative, latent_image=latent_image, seed=seed, steps=steps, cfg=cfg, sampler_name=sampler_name, scheduler=scheduler, denoise=denoise)
		images	= graph.node("VAEDecode", samples=latent.out(0), vae=vae)
		save  	= graph.node("SaveImage", images=images.out(0), filename_prefix=filename_prefix)
		return {
			"result" : (images.out(0),),
			"expand" : graph.finalize(),
		}
