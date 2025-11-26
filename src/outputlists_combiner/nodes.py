import itertools

import numpy


class AnyType(str):
	def __ne__(self, __value: object) -> bool:
		return False

any = AnyType("*")

class StringOutputList:
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required":
			{
				"separator"	: ("STRING", { "default": "\\n" }),
				"delimiter"	: ("STRING", { "default": ";" }),
				"values"	: ("STRING",
					{
						"multiline" : True,
						"default" : "String separated with newlines. Or try to inspect_combo with a COMBO input."
					}),
			},
		}

	RETURN_NAMES	= ("value" , "delimited_str" , "full_list" , "inspect_combo" )
	RETURN_TYPES	= (any , "STRING" , "LIST" , "COMBO" )
	OUTPUT_IS_LIST	= (True , False , False , False )
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, separator, delimiter, values):
		inspect_combo	= None
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value	= [s.strip() for s in values.split(unescaped_separator) if s.strip()]
		delimited_str	= delimiter.join(value)
		ret	= (value, delimited_str, value, inspect_combo)
		return ret

class NumberOutputList:
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"start"	:	("FLOAT"	, { "default" :	0	}),
				"stop"	:	("FLOAT"	, { "default" :	10	}),
				"num"	:	("INT"	, { "default" :	10	}),
				"endpoint"	:	("BOOLEAN"	, { "default" :	False	}),
				"delimiter"	:	("STRING"	, { "default" :	";"	}),
				}
		}

	RETURN_NAMES	= ("int", "float", "string", "full_list", "delimited_str")
	RETURN_TYPES	= ("INT", "FLOAT", "STRING", "LIST", "STRING")
	OUTPUT_IS_LIST	= (True, True, True, False, False)
	FUNCTION = "execute"
	CATEGORY = "Utility"

	def execute(self, start, stop, num, endpoint, delimiter):
		values	= list(numpy.linspace(start, stop, num, endpoint))
		ints	= [int (v) for v in values]
		floats	= [float (v) for v in values]
		strs	= [str (v) for v in values]
		delimited_str	= delimiter.join(strs)
		ret	= (ints, floats, strs, values, delimited_str)
		return ret

class CombineOutputLists:
	DESCRIPTION = """
Takes up to 4 lists, computes the Cartesian product and emits each combination splitted up into their elements (unzip).
Empty lists are replaced with units of None.

Examples:
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
[1, 2] x [] x ["A", B"] = [(1, None, "A"), (1, None, "B"), (2, None, "A"), (2, None, "B")]
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

	INPUT_IS_LIST = True
	RETURN_NAMES	= ("unzip_a" , "unzip_b" , "unzip_c" , "unzip_d" )
	RETURN_TYPES	= (any , any , any , any )
	OUTPUT_IS_LIST	= (True , True , True , True )
	FUNCTION = "compute"
	CATEGORY = "Utility"

	def compute(self, list_a = [], list_b = [], list_c = [], list_d = []):
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product	= list(itertools.product	(*normalized))
		transposed	= tuple(map(list, zip	(*product)))
		return transposed

class FormattedString:
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

	RETURN_NAMES	= ("string",)
	RETURN_TYPES	= ("STRING",)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, fstring, a = "", b = "", c = "", d = ""):
		ret = fstring.format(a=str(a), b=str(b), c=str(c), d=str(d))
		return (ret, )

NODE_CLASS_MAPPINGS = {
	"StringOutputList"	: StringOutputList,
	"NumberOutputList"	: NumberOutputList,
	"CombineOutputLists"	: CombineOutputLists,
	"FormattedString"	: FormattedString,
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"StringOutputList"	: "String OutputList",
	"NumberOutputList"	: "Number OutputList",
	"CombineOutputLists"	: "OutputList Combinations",
	"FormattedString"	: "Formatted String",
}
