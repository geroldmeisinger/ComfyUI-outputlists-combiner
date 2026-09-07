#from comfy_api.latest import ComfyExtension, io

from .src.bake_string import BakeString
from .src.combine_outputlists import CombineOutputLists
from .src.convert_to_intfloatstr import ConvertNumberToIntFloatStr
from .src.formatted_string import FormattedString
from .src.iterate import IterateBegin, IterateEnd
from .src.json_outputlist import JSONOutputList
from .src.ksampler_immediate_saveimage import KSamplerImmediateSave
from .src.load_any_file import LoadAnyFile
from .src.load_any_video import LoadAnyVideo
from .src.number_outputlist import NumberOutputList
from .src.path_outputlist import PathOutputList
from .src.spreadsheet_outputlist import SpreadsheetOutputList
from .src.string_outputlist import StringOutputList
from .src.workflow_discriminator import WorkflowDiscriminator
from .src.xyzgridplot import XyzGridPlot

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
