from pathlib import Path

import folder_paths
from comfy_api.latest import io
from dynamicprompts.generators import RandomPromptGenerator
from dynamicprompts.wildcards.wildcard_manager import WildcardManager


class DynamicPromptsOutputList(io.ComfyNode):
	@classmethod
	def define_schema(self) -> io.Schema:
		ret = io.Schema(
			description=f"""
""",
			node_id	= "DynamicPromptsOutputList",
			display_name	= "DynamicPrompts OutputList",
			category	= "Utility",
			inputs	= [
				io.String	.Input("directory"	, display_name="wildcards_dir"	, default="wildcards/", placeholder="",	tooltip=""	),
				io.Int	.Input("seed"	, display_name="seed"	, default=1234567890,	tooltip=""	),
				io.Int	.Input("num"	, display_name="num"	, default=10, min=0,	tooltip=""	),
				io.Combo	.Input("engine"	, display_name="engine"	, default="dynamicprompts", options=["dynamicprompts"],	tooltip=""	),
				io.String.Input("template",
					display_name	= "template",
					multiline	= True,
					default	= "",
					placeholder	= "",
					tooltip	= "",
				),
			],
			outputs	= [
				io.String	.Output("prompt"	, display_name="prompt"	, is_output_list=True	, tooltip=f""),
				])
		return ret

	@classmethod
	def execute(self, directory: str, seed: int, num: int, engine: str, template: str, ):
		input_directory	= Path(folder_paths.get_input_directory()).resolve()
		fullpath	= (input_directory / Path(directory.lstrip("/"))).resolve()
		wm	= WildcardManager(fullpath)
		generator	= RandomPromptGenerator(wildcard_manager=wm, seed=seed)
		prompts	= generator.generate(template, num_images=num)
		ret	= io.NodeOutput(prompts)

		return ret

	@classmethod
	def validate_inputs(self, directory: str, seed: int, num: int, engine: str, template: str, ):
		input_directory	= Path(folder_paths.get_input_directory()).resolve()
		fullpath	= (input_directory / Path(directory.lstrip("/"))).resolve()

		if not fullpath.relative_to(input_directory): return f"Invalid path. directory='{directory}'"

		return True
