import comfy.samplers
import folder_paths
from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder


class KSamplerImmediateSave(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		return io.Schema(
			description	= """Node expansion of default `CheckpointLoader`, `KSampler`, `VAE Decode` and `Save Image` to process as one.
This is useful if you want to save the intermediate images for grids immediately.

*"A custom KSampler just to save an image? Now I have become the very thing I sought to destroy!"*
""",
			node_id	= "KSamplerImmediateSave",
			display_name	= "KSampler Immediate Save",
			category	= "_for_testing",
			inputs	= [
				# CheckpointLoaderSimple
				io.Combo	.Input("ckpt_name"	, display_name="cpkt_name", options=folder_paths.get_filename_list("checkpoints"),	tooltip="The name of the checkpoint (model) to load."),
				# KSampler inputs
				io.String	.Input("positive"	, display_name="positive"	,	tooltip="The conditioning describing the attributes you want to include in the image."),
				io.String	.Input("negative"	, display_name="negative"	,	tooltip="The conditioning describing the attributes you want to exclude from the image."),
				io.Latent	.Input("latent_image"	, display_name="latent_image"	,	tooltip="The latent image to denoise."),
				io.Int	.Input("seed"	, display_name="seed"	, default=0, min=0, max=0xfffffffffffffff, control_after_generate=True,	tooltip="The random seed used for creating the noise."),
				io.Int	.Input("steps"	, display_name="steps"	, default=20, min=1, max=10000,	tooltip="The number of steps used in the denoising process."),
				io.Float	.Input("cfg"	, display_name="cfg"	, default=8.0, min=0.0, max=100.0, step=0.1, round=0.01,	tooltip="The Classifier-Free Guidance scale balances creativity and adherence to the prompt. Higher values result in images more closely matching the prompt however too high values will negatively impact quality."),
				io.Combo	.Input("sampler_name"	, display_name="sampler_name"	, options=comfy.samplers.KSampler.SAMPLERS,	tooltip="The algorithm used when sampling , this can affect the quality , speed , and style of the generated output."),
				io.Combo	.Input("scheduler"	, display_name="scheduler"	, options=comfy.samplers.KSampler.SCHEDULERS,	tooltip="The scheduler controls how noise is gradually removed to form the image."),
				io.Float	.Input("denoise"	, display_name="denoise"	, default=1.0, min=0.0, max=1.0, step=0.01,	tooltip="The amount of denoising applied , lower values will maintain the structure of the initial image allowing for image to image sampling."),
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
	def execute(self, ckpt_name, positive, negative, latent_image, seed, steps, cfg, sampler_name, scheduler, denoise, filename_prefix):
		graph	= GraphBuilder()
		checkpoint	= graph.node("CheckpointLoaderSimple" , ckpt_name=ckpt_name)
		positive	= graph.node("CLIPTextEncode" , text=positive, clip=checkpoint.out(1))
		negative	= graph.node("CLIPTextEncode" , text=negative, clip=checkpoint.out(1))
		latent	= graph.node("KSampler"	, model=checkpoint.out(0), positive=positive.out(0), negative=negative.out(0), latent_image=latent_image, seed=seed, steps=steps, cfg=cfg, sampler_name=sampler_name, scheduler=scheduler, denoise=denoise)
		images	= graph.node("VAEDecode"	, samples=latent.out(0), vae=checkpoint.out(2))
		save	= graph.node("SaveImage"	, images=images.out(0), filename_prefix=filename_prefix)
		return {
			"result" : (images.out(0),),
			"expand" : graph.finalize(),
		}

# class SaveImagePassthrough(io.ComfyNode):
#	@classmethod
#	def define_schema(cls) -> io.Schema:
#		return io.Schema(
#			description	= """Save Image Passthrough""",
#			node_id	= "SaveImagePassthrough",
#			display_name	= "Save Image Passthrough",
#			category	= "_for_testing",
#			inputs	= [
#				io.Image.Input("images", display_name="images", tooltip="The images to save."),
#				io.String.Input("filename_prefix", default="ComfyUI", tooltip="The prefix for the file to save. This may include formatting information such as %date :yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes."),
#			],
#			outputs=[
#				io.Image.Output("images", display_name="images", tooltip="Images"),
#			],
#             hidden	= [
#				io.Hidden.prompt,
#				io.Hidden.extra_pnginfo,
#             ],
#			enable_expand=True,
#		)

#	@classmethod
#	def execute(self, images, filename_prefix):
#		graph	= GraphBuilder()
#		save	= graph.node("SaveImage", images=images, filename_prefix=filename_prefix, prompt=self.hidden.prompt, extra_pnginfo=self.hidden.extra_pnginfo)
#		return {
#			"result" : (images,),
#			"expand" : graph.finalize(),
#		}