from comfy_api.latest import ComfyExtension, io

from .src.outputlists_combiner import *

WEB_DIRECTORY = "./web"

__all__ = ["WEB_DIRECTORY"]

async def comfy_entrypoint() -> ComfyExtension:
	class OutputListsCombiner(ComfyExtension):
		async def get_node_list(self) -> list[type[io.ComfyNode]]:
			return [
				StringOutputList,
				NumberOutputList,
				JSONOutputList,
				SpreadsheetOutputList,
				DynamicPromptsOutputList,
				CombineOutputLists,
				XyzGridPlot,
				WorkflowDiscriminator,
				FormattedString,
				ConvertNumberToIntFloatStr,
				LoadAnyFile,
				KSamplerImmediateSave,
			]

	return OutputListsCombiner()
