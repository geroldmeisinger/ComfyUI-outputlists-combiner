from .nodes import *
from .xyzgridplot import *

NODE_CLASS_MAPPINGS = {
	"StringOutputList"          	: StringOutputList,
	"NumberOutputList"          	: NumberOutputList,
	"JSONOutputList"            	: JSONOutputList,
	"SpreadsheetOutputList"     	: SpreadsheetOutputList,
	"CombineOutputLists"        	: CombineOutputLists,
	"XyzGridPlot"               	: XyzGridPlot,
	"FormattedString"           	: FormattedString,
	"ConvertNumberToIntFloatStr"	: ConvertNumberToIntFloatStr,
	"LoadFile"                  	: LoadFile,
	"KSamplerImmediateSave"     	: KSamplerImmediateSave,
}
NODE_DISPLAY_NAME_MAPPINGS = {
	"StringOutputList"          	: "String OutputList",
	"NumberOutputList"          	: "Number OutputList",
	"JSONOutputList"            	: "JSON OutputList",
	"SpreadsheetOutputList"     	: "Spreadsheet OutputList",
	"CombineOutputLists"        	: "OutputList Combinations",
	"XyzGridPlot"               	: "XYZ-Gridplot",
	"FormattedString"           	: "Formatted String",
	"ConvertNumberToIntFloatStr"	: "Convert to Int Float String",
	"LoadFile"                  	: "Load any File",
	"KSamplerImmediateSave"     	: "KSampler Immediate Save Image",
}
