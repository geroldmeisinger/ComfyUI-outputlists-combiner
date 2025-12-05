import itertools

import comfy.samplers
import numpy
import nums_from_string
from comfy_execution.graph_utils import GraphBuilder


class AnyType(str):
	def __ne__(self, __value: object) -> bool:
		return False

any = AnyType("*")

class StringOutputList:
	DESCRIPTION = """Create a OutputList by separating the string in the textfield.

inputs:
* separator: the string to split the textfield values.
* delimiter: only used for delimited_str.
* values: the string which will be separated. note that the string is stripped of whitespace before splitting, and each item is again stripped.

outputs:
* value: the values from the list. uses OUTPUT_IS_LIST=True and will be processed sequentially by corresponding nodes.
* delimited_str: the list joined together by the delimiter, which is often useful for other nodes (like grid annotations).
* count: the number of items in the list
* inspect_combo: a dummy output only used to pre-fill the list with values from a COMBO input and will automatically disconnect again.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required":
			{
				"separator"	: ("STRING", { "default": "\\n" }),
				"delimiter"	: ("STRING", { "default": ";" }),
				"values"	: ("STRING",
					{
						"multiline"	: True,
						"default"	: "",
						"placeholder"	: "String separated with newlines. Or try to connect inspect_combo with a COMBO input."
					}),
			},
		}

	RETURN_NAMES	= ("value" , "delimited_str" , "count" , "inspect_combo" )
	RETURN_TYPES	= (any , "STRING" , "INT" , "COMBO" )
	OUTPUT_IS_LIST	= (True , False , False , False )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, separator, delimiter, values):
		inspect_combo	= None
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value	= [s.strip() for s in values.split(unescaped_separator) if s.strip()]
		delimited_str	= delimiter.join(value)
		count	= len(value)
		ret	= (value, delimited_str, count, inspect_combo)
		return ret

class NumberOutputList:
	DESCRIPTION = """Create a OutputList by generating a numbers of values in a range.
Uses numpy.linspace internally because it works more reliably with floatingpoint values.

inputs:
* start: start value to generate the range from
* stop: end value. if endpoint=True this number will be included in the list.
* num: the number of items in the list (not to be confused with a step).
* endpoint: decides if the stop value should be included or excluded in the items.
* delimiter: only used for delimited_str.

outputs:
All the values from the list use OUTPUT_IS_LIST=True and will be processed sequentially by corresponding nodes.
* int: the value converted to int (rounded down/floored)
* float: the value as a float
* str: the value as a string
* count: the number of items in the list
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"start"	: ("FLOAT"	, { "default"	: 0 }),
				"stop"	: ("FLOAT"	, { "default"	: 10 }),
				"num"	: ("FLOAT"	, { "default"	: 10, "min": 1 }),
				"endpoint"	: ("BOOLEAN"	, { "default"	: False, "label_on"	: "include", "label_off"	: "exclude" }),
				"delimiter"	: ("STRING"	, { "default"	: ";" }),
				}
		}

	RETURN_NAMES	= ("int" , "float" , "string" , "delimited_str" )
	RETURN_TYPES	= ("INT" , "FLOAT" , "STRING" , "STRING" )
	OUTPUT_IS_LIST	= (True , True , True , False )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, start, stop, num, endpoint, delimiter):
		values	= list(numpy.linspace(start, stop, int(num), endpoint))
		ints	= [int (v) for v in values]
		floats	= [float (v) for v in values]
		strs	= [str (v) for v in values]
		delimited_str	= delimiter.join(strs)
		ret	= (ints, floats, strs, delimited_str)
		return ret

class CombineOutputLists:
	DESCRIPTION = """Takes up to 4 OutputLists, computes the Cartesian product and outputs each combination splitted up into their elements (unzip).
Empty lists are replaced with units of None and unused inputs will always emit None on the respective output.

Examples:
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
[1, 2] x [] x ["A", B"] = [(1, None, "A"), (1, None, "B"), (2, None, "A"), (2, None, "B")]

outputs:
* count: the total number of combinations
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
			},
			"optional": {
				"list_a"	: (any, ),
				"list_b"	: (any, ),
				"list_c"	: (any, ),
				"list_d"	: (any, ),
			}
		}

	INPUT_IS_LIST	= True
	RETURN_NAMES	= ("unzip_a" , "unzip_b" , "unzip_c" , "unzip_d" , "count" )
	RETURN_TYPES	= (any , any , any , any , "INT" )
	OUTPUT_IS_LIST	= (True , True , True , True , False )
	FUNCTION	= "compute"
	CATEGORY	= "Utility"

	def compute(self, list_a = [], list_b = [], list_c = [], list_d = []):
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product	= list(itertools.product(*normalized))
		transposed	= tuple(map(list, zip(*product)))
		ret	= (*transposed, len(product))
		return ret

class FormattedString:
	DESCRIPTION = """Uses python str.format() internally, see https://docs.python.org/3/library/string.html#format-string-syntax .
A commonly used format syntax is {a:.2f} to round of a float to 2 decimals.

outputs:
* string: the formatted string with all placeholders replaced with their respective values.
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"fstring": ("STRING", {
					"multiline"	: True,
					"default"	: "{a}_{b}_{c}_{d}"
					}),
				},
			"optional": {
				"a"	: (any, ),
				"b"	: (any, ),
				"c"	: (any, ),
				"d"	: (any, ),
				}
		}

	RETURN_NAMES	= ("string", )
	RETURN_TYPES	= ("STRING", )
	OUTPUT_IS_LIST	= (False   , )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, fstring, a = "", b = "", c = "", d = ""):
		ret = (fstring.format(a=a, b=b, c=c, d=d),)
		return ret

class ConvertNumberToIntFloatStr:
	DESCRIPTION = """Convert anything number-like to int float string.
Uses `nums-from-string.get_nums` internally which is very permissive in the numbers it accepts.
Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.

outputs:
* int: all the numbers found in the string with the decimals truncated (floored)
* float: all the numbers found in the string as floats
* string: all the numbers found in the string converted to string
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"number": (any,),
			}
		}

	RETURN_NAMES	= ("int" , "float" , "string" )
	RETURN_TYPES	= ("INT" , "FLOAT" , "STRING" )
	OUTPUT_IS_LIST	= (True , True , True )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, number):
		number_str	= str(number)
		floats	= nums_from_string.get_nums(number_str)
		ints	= [int(f) for f in floats]
		strs	= [str(f) for f in floats]
		ret	= (ints, floats, strs)
		return ret

# class StringToCombo:
# DESCRIPTION = """
# """

# @classmethod
# def INPUT_TYPES(cls):
#  return {
#   "required": {
#    "string": ("STRING",),
#    },
#  }

# RETURN_NAMES = ("combo", "any" )
# RETURN_TYPES = ("COMBO", any )
# OUTPUT_IS_LIST = (True, True )
# FUNCTION = "execute"
# CATEGORY = "Utility"

# def execute(self, string):
#  ret = (str(string))
#  return ([ret], [ret])

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

NODE_CLASS_MAPPINGS = {
	"StringOutputList"	: StringOutputList,
	"NumberOutputList"	: NumberOutputList,
	"CombineOutputLists"	: CombineOutputLists,
	"FormattedString"	: FormattedString,
	"ConvertNumberToIntFloatStr"	: ConvertNumberToIntFloatStr,
	#"StringToCombo"	: StringToCombo,
	"KSamplerImmediateSave"	: KSamplerImmediateSave,
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"StringOutputList"	: "String OutputList",
	"NumberOutputList"	: "Number OutputList",
	"CombineOutputLists"	: "OutputList Combinations",
	"FormattedString"	: "Formatted String",
	"ConvertNumberToIntFloatStr"	: "Convert to Int Float String",
	"KSamplerImmediateSave"	: "KSampler Immediate Save Image",
}
