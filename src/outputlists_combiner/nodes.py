import base64
import hashlib
import io
import itertools
import re
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
from comfy_execution.graph_utils import GraphBuilder
from fastnumbers import try_float
from jsonpath_ng import parse as jsonpath_parse
from PIL import Image, ImageOps, ImageSequence, UnidentifiedImageError


class AnyType	(str	)	:
	def __ne__(self, __value: object) -> bool:
		return False

any = AnyType("*")

OUTPUTLIST_NOTE = "uses OUTPUT_IS_LIST=True (indicated by the symbol 𝌠) and will be processed sequentially by corresponding nodes"

class StringOutputList:
	DESCRIPTION = f"""Create a OutputList by separating the string in the textfield.
value and index {OUTPUTLIST_NOTE}
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required":
			{
				"separator"	: ("STRING", { "default": "\\n", "tooltip": "the string to split the textfield values" }),
				"values"	: ("STRING",
					{
						"multiline"	: True,
						"default"	: "",
						"placeholder"	: "string separated with newlines. Try to connect inspect_combo with a COMBO input!",
						"tooltip"	: "the string which will be separated. note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed",
					}),
			},
		}

	RETURN_NAMES	=	("value"	, "index"	, "count"	, "inspect_combo"	)
	RETURN_TYPES	=	(any	, "INT"	, "INT"	, "COMBO"	)
	OUTPUT_IS_LIST	=	(True	, True	, False	, False	)
	OUTPUT_TOOLTIPS	= (
		f"the values from the list. {OUTPUTLIST_NOTE}",
		f"range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}",
		f"the number of items in the list. {OUTPUTLIST_NOTE}",
		"a dummy output only used to pre-fill the list with values from a COMBO input and will automatically disconnect again",
		)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, separator, values):
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value	= [s.strip() for s in values.rstrip().split(unescaped_separator)]
		count	= len(value)
		index	= range(count)
		inspect_combo	= None
		ret	= (value, index, count, inspect_combo)
		return ret

class NumberOutputList:
	DESCRIPTION = f"""Create a OutputList by generating a numbers of values in a range.
Uses numpy.linspace internally because it works more reliably with floatingpoint values.
int, float, string and index {OUTPUTLIST_NOTE}.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"start"	: ("FLOAT"	, { "default"	:	0,	"tooltip": "start value to generate the range from" }),
				"stop"	: ("FLOAT"	, { "default"	:	10,	"tooltip": "end value. if endpoint=include this number will be included in the list" }),
				"num"	: ("INT"	, { "default"	:	10, "min": 1,	"tooltip": "the number of items in the list (not to be confused with a step)" }),
				"endpoint"	: ("BOOLEAN"	, { "default"	:	False, "label_on": "include", "label_off": "exclude",	"tooltip": "decides if the stop value should be included or excluded in the items" }),
				}
		}

	RETURN_NAMES	= ("int"	, "float"	, "string"	, "index"	, "count"	)
	RETURN_TYPES	= ("INT"	, "FLOAT"	, "STRING"	, "INT"	, "INT"	)
	OUTPUT_IS_LIST	= (True	, True	, True	, True	, False	)
	OUTPUT_TOOLTIPS	= (
		f"the value converted to int (rounded down/floored). {OUTPUTLIST_NOTE}",
		f"the value as a float. {OUTPUTLIST_NOTE}",
		f"the value as a string. {OUTPUTLIST_NOTE}",
		f"range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}",
		"same as num",
		)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, start, stop, num, endpoint):
		values	= list(numpy.linspace(start, stop, num, endpoint))
		ints	= [int	(v) for v in values]
		floats	= [float	(v) for v in values]
		strs	= [str	(v) for v in values]
		index	= range(num)
		ret	= (ints, floats, strs, index, num)
		return ret

class JSONOutputList:
	DESCRIPTION = f"""Create a OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see https://en.wikipedia.org/wiki/JSONPath .
All matched values will be flattend into one list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
key, value, int, float {OUTPUTLIST_NOTE}.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required":
			{
				"jsonpath"	: ("STRING", { "default": "$.dict", "tooltip": "JSONPath used to extract the values" }),
				"json"	: ("STRING",
					{
						"multiline"	: True,
						"default"	: dumps(loads('{ "dict": { "a": 0.12, "b": 3.45, "c": 6.78 }, "arr": [0.12, 3.45, 6.78] }'), indent=4),
						"placeholder"	: "object or JSON string",
						"tooltip"	: "a string which will be parsed as JSON",
					}),
			},
			"optional": {
				"obj": (any, { "tooltip": "(optional) object of any type which will replace the JSON string" }),
			}
		}

	RETURN_NAMES	= ("key"	, "value"	, "int"	, "float"	, "count"	, "debug"	)
	RETURN_TYPES	= ("STRING"	, "STRING"	, "INT"	, "FLOAT"	, "INT"	, "STRING"	)
	OUTPUT_IS_LIST	= (True	, True	, True	, True	, False	, False	)
	OUTPUT_TOOLTIPS	= (
		f"the key for dictionaries or index for arrays (as string). {OUTPUTLIST_NOTE}. Technically it's a global index of the flattened list for all non-keys",
		f"the value as a string. {OUTPUTLIST_NOTE}",
		f"the value as a int (if not parseable number default to 0). {OUTPUTLIST_NOTE}",
		f"the value as a float (if not parseable number default to 0). {OUTPUTLIST_NOTE}",
		"total number of items in the flattened list",
		"debug output of all matched objects as a formatted JSON string",
		)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, jsonpath, json, obj = None):
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
			return { "ui": { "obj": [dumps(obj, indent=4)] }, "result": ([], [], [], [], 0, "[]") }

		if not matches:
			return { "ui": { "obj": [dumps(obj, indent=4)] }, "result": ([], [], [], [], 0, "[]") }

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

		result	= (keys, values, ints, floats, count, debug_json)
		ret	=  { "ui": { "obj": [dumps(data, indent=4)] }, "result": result }
		return ret

class SpreadsheetOutputList:
	DESCRIPTION = f"""Create a OutputLists from a spreadsheet (CSV, TSV, ODS, XLSX and XLS).
Use `Load any File` node to load a file as base64.
Internally uses pandas to load spreadsheet files.
Lists {OUTPUTLIST_NOTE}.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required":
			{
				"rows_and_cols"	: ("STRING"	, { "default": "A B C D"			, "tooltip": "Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based." }),
				"header_rows"	: ("INT"	, { "default":	1, "min":	0, "max": 65535	, "tooltip": "Ignore the first x rows in the list. Only used if you specify a col in rows_and_cols." }),
				"header_cols"	: ("INT"	, { "default":	1, "min":	0, "max": 65535	, "tooltip": "Ignore the first x cols in the list. Only used if you specify a row in rows_and_cols." }),
				"select_nth"	: ("INT"	, { "default":	-1, "min":	-1, "max": 65535	, "tooltip": "Only select the nth entry. Useful in combination with the PrimitiveInt+control_after_generate=increment pattern." }),
				"string_or_base64"	: ("STRING"	, {
						"multiline"	: True,
						"default"	: "",
						"placeholder"	: "CSV/TSV string or spreadsheet file in base64 (ODS, XLSX, XLS). Use `Load any File` node to load a file as base64.",
						"tooltip"	: "CSV/TSV string or spreadsheet file in base64 (ODS, XLSX, XLS). Use `Load any File` node to load a file as base64.",
					}
				),
			},
		}

	RETURN_NAMES	= ("list_a"	, "list_b"	, "list_c"	, "list_d"	, "count"	)
	RETURN_TYPES	= ("STRING"	, "STRING"	, "STRING"	, "STRING"	, "INT"	)
	OUTPUT_IS_LIST	= (True	, True	, True	, True	, False	)
	OUTPUT_TOOLTIPS	= (
		f"{OUTPUTLIST_NOTE}",
		f"{OUTPUTLIST_NOTE}",
		f"{OUTPUTLIST_NOTE}",
		f"{OUTPUTLIST_NOTE}",
		"number of items in the longest list",
		)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

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

	def execute(self, string_or_base64, rows_and_cols, header_rows, header_cols, select_nth):
		limit	= 4
		data	= string_or_base64.strip()

		# load spreadsheet with pandas
		try:
			decoded	= base64.b64decode(data, validate=True)
			xls	= pd.read_excel(io.BytesIO(decoded), sheet_name=None, header=None)
		except Exception:
			try:
				df	= pd.read_csv(io.StringIO(data), sep=None, engine="python", header=None)
				xls	= {None: df}
			except Exception:
				return ([[] for _ in range(limit)], 0)

		sheet_names	= list(xls.keys())
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
			key	= m.group(4)

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

class CombineOutputLists:
	DESCRIPTION = f"""Takes up to 4 OutputLists, generates all combinations between them and emits each combination as separate items.
Example: [1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
All the unzip values and index {OUTPUTLIST_NOTE}.
All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.
Example: [1, 2] x [] x ["A", B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
			},
			"optional": {
				"list_a"	: (any, { "tooltip": "(optional) ideally connected to a node with OUTPUT_IS_LIST=True indicated by the symbol 𝌠" }),
				"list_b"	: (any, { "tooltip": "(optional) ideally connected to a node with OUTPUT_IS_LIST=True indicated by the symbol 𝌠" }),
				"list_c"	: (any, { "tooltip": "(optional) ideally connected to a node with OUTPUT_IS_LIST=True indicated by the symbol 𝌠" }),
				"list_d"	: (any, { "tooltip": "(optional) ideally connected to a node with OUTPUT_IS_LIST=True indicated by the symbol 𝌠" }),
			}
		}

	INPUT_IS_LIST	= True
	RETURN_NAMES	= ("unzip_a"	, "unzip_b"	, "unzip_c"	, "unzip_d"	, "index"	, "count"	)
	RETURN_TYPES	= (any	, any	, any	, any	, "INT"	, "INT"	)
	OUTPUT_IS_LIST	= (True	, True	, True	, True	, True	, False	)
	OUTPUT_TOOLTIPS	= (
		f"value of the combinations corresponding to list_a. {OUTPUTLIST_NOTE}",
		f"value of the combinations corresponding to list_b. {OUTPUTLIST_NOTE}",
		f"value of the combinations corresponding to list_c. {OUTPUTLIST_NOTE}",
		f"value of the combinations corresponding to list_d. {OUTPUTLIST_NOTE}",
		f"range of 0..count which can be used as an index. {OUTPUTLIST_NOTE}",
		"total number of combinations",
		)
	FUNCTION	= "compute"
	CATEGORY	= "Utility"

	def compute(self, list_a = [], list_b = [], list_c = [], list_d = []):
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product	= list(itertools.product(*normalized))
		transposed	= tuple(map(list, zip(*product)))
		count	= len(product)
		index	= range(count)
		ret	= (*transposed, index, count)
		return ret

class FormattedString:
	DESCRIPTION = """Uses python `str.format()` internally, see https://docs.python.org/3/library/string.html#format-string-syntax
Use `{a:.2f}` to round off a float to 2 decimals
Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`
If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"fstring": ("STRING", {
					"multiline"	: True,
					"default"	: "{a}_{b}_{c}_{d}",
					"tooltip"	: FormattedString.DESCRIPTION,
					}),
				},
			"optional": {
				"a"	: (any, { "tooltip": "(optional) value that will be converted to string with the {a} placeholder" }),
				"b"	: (any, { "tooltip": "(optional) value that will be converted to string with the {b} placeholder" }),
				"c"	: (any, { "tooltip": "(optional) value that will be converted to string with the {c} placeholder" }),
				"d"	: (any, { "tooltip": "(optional) value that will be converted to string with the {d} placeholder" }),
				}
		}

	RETURN_NAMES	= ("string", )
	RETURN_TYPES	= ("STRING", )
	OUTPUT_IS_LIST	= (False   , )
	OUTPUT_TOOLTIPS	= ("the formatted string with all placeholders replaced with their respective values", )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, fstring, a = "", b = "", c = "", d = ""):
		ret = (fstring.format(a=a, b=b, c=c, d=d),)
		return ret

class ConvertNumberToIntFloatStr:
	DESCRIPTION = f"""Convert anything number-like to int float string.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts.
Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
int, float and string {OUTPUTLIST_NOTE}.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"number": (any, { "tooltip": "anything that can be converted to a string" }),
			}
		}

	INPUT_IS_LIST	= True
	RETURN_NAMES	= ("int"	, "float"	, "string"	, "count"	)
	RETURN_TYPES	= ("INT"	, "FLOAT"	, "STRING"	, "INT"	)
	OUTPUT_IS_LIST	= (True	, True	, True	, False	)
	OUTPUT_TOOLTIPS	= (
		f"all the numbers found in the string with the decimals truncated. {OUTPUTLIST_NOTE}",
		f"all the numbers found in the string as floats. {OUTPUTLIST_NOTE}",
		f"all the numbers found in the string as floats converted to string. {OUTPUTLIST_NOTE}",
		"amount of numbers found in the string, which in most cases will be 1",
		)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, number):
		number_str	= str(number)
		floats	= nums_from_string.get_nums(number_str)
		ints	= [int(f) for f in floats]
		strs	= [str(f) for f in floats]
		count	= len(floats)
		ret	= (ints, floats, strs, count)
		return ret

class LoadFile:
	DESCRIPTION = f"""Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a IMAGE.
"""

	@classmethod
	def INPUT_TYPES(s):
		return {
			"required": {
					"annotated_filepath": ("STRING", { "tooltip": "Base directory defaults to input directory. Use suffix [input] [output] [temp] to specify a different ComfyUI user directory." }),
				},
			}

	CATEGORY = "Utility"

	RETURN_NAMES	= ("string"	, "image"	, "mask"	)
	RETURN_TYPES	= ("STRING"	, "IMAGE"	, "MASK"	)
	OUTPUT_TOOLTIPS	= (
		"file content for text files, base64 for binary files.",
		"image batch tensor",
		"mask batch tensor",
		)
	FUNCTION = "execute"

	def load_image(self, image_data):
		img = node_helpers.pillow(Image.open, image_data)

		# from ComfyUI/nodes.py LoadImage
		output_images	= []
		output_masks	= []
		w, h	= None, None

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
			output_masks	.append(mask.unsqueeze(0))

		if len(output_images) > 1 and img.format not in excluded_formats:
			output_image	= torch.cat(output_images, dim	=0)
			output_mask	= torch.cat(output_masks, dim	=0)
		else:
			output_image	= output_images[0]
			output_mask	= output_masks[0]

		return (output_image, output_mask)

	def execute(self, annotated_filepath):
		file_path = folder_paths.get_annotated_filepath(annotated_filepath)

		with open(file_path, "rb") as f:
			raw_data = f.read()

		# check if binary
		try:
			result	= chardet.detect(raw_data)
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
			image, mask = self.load_image(io.BytesIO(image_data))
		except (UnidentifiedImageError, OSError, ValueError):
			# fallback to black 64x64 tensors
			image	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")
			mask	= torch.zeros((64, 64), dtype=torch.float32, device="cpu")

		return (filecontent, image, mask)

	@classmethod
	def IS_CHANGED(s, annotated_filepath):
		path	= folder_paths.get_annotated_filepath(annotated_filepath)
		m	= hashlib.sha256()
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

class KSamplerImmediateSave:
	DESCRIPTION="""Node Expansion of default KSampler, VAE Decode and Save Image to process as one.
This is useful if you want to save the intermediate images for grids immediately.
'A custom KSampler just to save an image? Now I have become the very thing I sought to destroy!'
"""
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				# from ComfyUI/nodes.py KSampler
				"model"	: ("MODEL"	, { "tooltip" : "The model used for denoising the input latent." } ) ,
				"positive"	: ("CONDITIONING"	, { "tooltip" : "The conditioning describing the attributes you want to include in the image." } ) ,
				"negative"	: ("CONDITIONING"	, { "tooltip" : "The conditioning describing the attributes you want to exclude from the image." } ) ,
				"latent_image"	: ("LATENT"	, { "tooltip" : "The latent image to denoise." } ) ,
				"vae"	: ("VAE"	, { "tooltip" : "The VAE model used for decoding the latent." } ) ,

				"seed"	: ("INT"	, {"default" :	0	, "min" :	0	, "max" :	0xfffffffffffffff	, "control_after_generate" : True,	"tooltip" : "The random seed used for creating the noise." } ) ,
				"steps"	: ("INT"	, {"default" :	20	, "min" :	1	, "max" :	10000	,	"tooltip" : "The number of steps used in the denoising process." } ) ,
				"cfg"	: ("FLOAT"	, {"default" :	8.0	, "min" :	0.0	, "max" :	100.0	, "step" : 0.1, "round" : 0.01,	"tooltip" : "The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality." } ) ,
				"sampler_name"	: (comfy.samplers.KSampler.SAMPLERS	, {"tooltip" : "The algorithm used when sampling , this can affect the quality , speed , and style of the generated output." } ) ,
				"scheduler"	: (comfy.samplers.KSampler.SCHEDULERS	, {"tooltip" : "The scheduler controls how noise is gradually removed to form the image." } ) ,
				"denoise"	: ("FLOAT"	, {"default" :	1.0	, "min" :	0.0	, "max" :	1.0	, "step" : 0.01,	"tooltip" : "The amount of denoising applied , lower values will maintain the structure of the initial image allowing for image to image sampling." } ) ,

				# from ComfyUI/nodes.py SaveImage
				"filename_prefix"	: ("STRING", {"default" : "ComfyUI", "tooltip" : "The prefix for the file to save. This may include formatting information such as %date :yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes."}),
			},
			# "hidden": {
			#	"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO",
			# },
		}

	RETURN_NAMES	= ("image", )
	RETURN_TYPES	= ("IMAGE", )
	OUTPUT_TOOLTIPS	= ("The decoded image.",) # from ComfyUI/nodes.py VAEDecode
	OUTPUT_NODE	= True
	FUNCTION	= "execute"
	CATEGORY	= "_for_testing"

	def execute(self, model, positive, negative, latent_image, vae, seed, steps, cfg, sampler_name, scheduler, denoise, filename_prefix):
		graph	= GraphBuilder()
		latent	= graph.node("KSampler" , model=model, positive=positive, negative=negative, latent_image=latent_image, seed=seed, steps=steps, cfg=cfg, sampler_name=sampler_name, scheduler=scheduler, denoise=denoise)
		images	= graph.node("VAEDecode", samples=latent.out(0), vae=vae)
		save	= graph.node("SaveImage", images=images.out(0), filename_prefix=filename_prefix)
		return {
			"result" : (images.out(0),),
			"expand" : graph.finalize(),
		}
