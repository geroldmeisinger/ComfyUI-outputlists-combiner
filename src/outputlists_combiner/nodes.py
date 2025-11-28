import itertools

import numpy


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
* full_list: the whole list without OUTPUT_IS_LIST=False in case some nodes require it.
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
						"multiline" : True,
						"default" : "",
						"placeholder"	: "String separated with newlines. Or try to connect inspect_combo with a COMBO input."
					}),
			},
		}

	RETURN_NAMES	=	("value"	, "delimited_str"	, "full_list"	, "count"	, "inspect_combo"	)
	RETURN_TYPES	=	(any	, "STRING"	, "STRING"	, "INT"	, "COMBO"	)
	OUTPUT_IS_LIST	=	(True	, False	, False	, False	, False	)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, separator, delimiter, values):
		inspect_combo	= None
		unescaped_separator	= separator.encode().decode('unicode_escape')
		value	= [s.strip() for s in values.split(unescaped_separator) if s.strip()]
		delimited_str	= delimiter.join(value)
		count	= len(value)
		ret	= (value, delimited_str, value, count, inspect_combo)
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
* full_list: the whole list without OUTPUT_IS_LIST=False in case some nodes require it.
* count: the number of items in the list
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"start"	:	("FLOAT"	, { "default" :	0	}),
				"stop"	:	("FLOAT"	, { "default" :	10	}),
				"num"	:	("FLOAT"	, { "default" :	10	}),
				"endpoint"	:	("BOOLEAN"	, { "default" :	False, "label_on": "include", "label_off": "exclude"	}),
				"delimiter"	:	("STRING"	, { "default" :	";"	}),
				}
		}

	RETURN_NAMES	=	("int"	, "float"	, "string"	, "full_list"	, "delimited_str"	)
	RETURN_TYPES	=	("INT"	, "FLOAT"	, "STRING"	, "LIST"	, "STRING"	)
	OUTPUT_IS_LIST	=	(True	, True	, True	, False	, False	)
	FUNCTION = "execute"
	CATEGORY = "Utility"

	def execute(self, start, stop, num, endpoint, delimiter):
		values	= list(numpy.linspace(start, stop, int(num), endpoint))
		ints	= [int (v) for v in values]
		floats	= [float (v) for v in values]
		strs	= [str (v) for v in values]
		delimited_str	= delimiter.join(strs)
		ret	= (ints, floats, strs, values, delimited_str)
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

	INPUT_IS_LIST = True
	RETURN_NAMES	=	("unzip_a"	, "unzip_b"	, "unzip_c"	, "unzip_d"	, "count"	, "full_list"	)
	RETURN_TYPES	=	(any	, any	, any	, any	, "INT"	, "LIST"	)
	OUTPUT_IS_LIST	=	(True	, True	, True	, True	, False	, False	)
	FUNCTION = "compute"
	CATEGORY = "Utility"

	def compute(self, list_a = [], list_b = [], list_c = [], list_d = []):
		normalized	= [lst if len(lst) > 0 else [None] for lst in [list_a, list_b, list_c, list_d]]
		product	= list(itertools.product(*normalized))
		transposed	= tuple(map(list, zip(*product)))
		return (*transposed, len(product), transposed)

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

	RETURN_NAMES	= ("string"	, "any"	)
	RETURN_TYPES	= ("STRING"	, any	)
	OUTPUT_IS_LIST	= (False	, False	)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, fstring, a = "", b = "", c = "", d = ""):
		ret = fstring.format(a=a, b=b, c=c, d=d)
		return (ret, ret)

class ConvertNumberToIntFloatStr:
	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"number": ("FLOAT,INT",),
			}
		}

	RETURN_NAMES	=	("int"	, "float"	, "string"	)
	RETURN_TYPES	=	("INT"	, "FLOAT"	, "STRING"	)
	FUNCTION = "execute"
	CATEGORY = "Utility"

	def execute(self, number):
		return (int(number), number, str(number))

class StringToCombo:
	DESCRIPTION = """
"""

	@classmethod
	def INPUT_TYPES(cls):
		return {
			"required": {
				"string": ("STRING",),
				},
		}

	RETURN_NAMES	= ("combo",	"any"	)
	RETURN_TYPES	= ("COMBO",	any	)
	OUTPUT_IS_LIST	= (True, True	)
	FUNCTION	= "execute"
	CATEGORY	= "Utility"

	def execute(self, string):
		ret = (str(string))
		return ([ret], [ret])

NODE_CLASS_MAPPINGS = {
	"StringOutputList"	: StringOutputList,
	"NumberOutputList"	: NumberOutputList,
	"CombineOutputLists"	: CombineOutputLists,
	"FormattedString"	: FormattedString,
	"ConvertNumberToIntFloatStr"	: ConvertNumberToIntFloatStr,
	"StringToCombo"	: StringToCombo,
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"StringOutputList"	: "String OutputList",
	"NumberOutputList"	: "Number OutputList",
	"CombineOutputLists"	: "OutputList Combinations",
	"FormattedString"	: "Formatted String",
	"ConvertNumberToIntFloatStr"	: "Convert any number to Int Float String",
	"StringToCombo"	: "String To Combo",
}
