#from comfy_api.latest import ComfyExtension, io

from .src import *

# async def comfy_entrypoint() -> ComfyExtension:
# class OutputListsCombiner(ComfyExtension):
#  async def get_node_list(self) -> list[type[io.ComfyNode]]:
#   return [

#   ]

# return OutputListsCombiner()

WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "StringOutputList"	: StringOutputList,
    "NumberOutputList"	: NumberOutputList,
    "JSONOutputList"	: JSONOutputList,
    "SpreadsheetOutputList"	: SpreadsheetOutputList,
    "CombineOutputLists"	: CombineOutputLists,
    "XyzGridPlot"	: XyzGridPlot,
    "WorkflowDiscriminator"	: WorkflowDiscriminator,
    "FormattedString"	: FormattedString,
    "ConvertNumberToIntFloatStr"	: ConvertNumberToIntFloatStr,
    "LoadAnyFile"	: LoadAnyFile,
    "LoadAnyVideo"	: LoadAnyVideo,
    "PathOutputList"	: PathOutputList,
    "KSamplerImmediateSave"	: KSamplerImmediateSave,
    "IterateBegin"	: IterateBegin,
    "IterateEnd"	: IterateEnd,
    "BakeString"	: BakeString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringOutputList"	: "String OutputList",
    "NumberOutputList"	: "Number OutputList",
    "JSONOutputList"	: "JSON OutputList",
    "SpreadsheetOutputList"	: "Spreadsheet OutputList",
    "CombineOutputLists"	: "Combine OutputLists",
    "XyzGridPlot"	: "Xyz Grid Plot",
    "WorkflowDiscriminator"	: "Workflow Discriminator",
    "FormattedString"	: "Formatted String",
    "ConvertNumberToIntFloatStr"	: "Convert Number to Int/Float/Str",
    "LoadAnyFile"	: "Load Any File",
    "LoadAnyVideo"	: "Load Any Video",
    "PathOutputList"	: "Path OutputList",
    "KSamplerImmediateSave"	: "KSampler Immediate Save",
    "IterateBegin"	: "Iterate Begin",
    "IterateEnd"	: "Iterate End",
    "BakeString"	: "Bake String",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
