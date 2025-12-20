import comfy.samplers
from comfy_api.latest import io
from comfy_execution.graph_utils import GraphBuilder


class KSamplerImmediateSave(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		return io.Schema(
			description	= """Node expansion of default `KSampler`, `VAE Decode` and `Save Image` to process as one.
This is useful if you want to save the intermediate images for grids immediately.

*"A custom KSampler just to save an image? Now I have become the very thing I sought to destroy!"*
""",
			node_id	= "KSamplerImmediateSave",
			display_name	= "KSampler Immediate Save",
			category	= "_for_testing",
			inputs	= [
				# KSampler inputs
				io.Model	.Input("model"	, display_name="model"	,	tooltip="The model used for denoising the input latent."),
				io.Conditioning	.Input("positive"	, display_name="positive"	,	tooltip="The conditioning describing the attributes you want to include in the image."),
				io.Conditioning	.Input("negative"	, display_name="negative"	,	tooltip="The conditioning describing the attributes you want to exclude from the image."),
				io.Latent	.Input("latent_image"	, display_name="latent_image"	,	tooltip="The latent image to denoise."),
				io.Vae	.Input("vae"	, display_name="vae"	,	tooltip="The VAE model used for decoding the latent."),
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
	def execute(self, model, positive, negative, latent_image, vae, seed, steps, cfg, sampler_name, scheduler, denoise, filename_prefix):
		graph	= GraphBuilder()
		latent	= graph.node("KSampler" , model=model, positive=positive, negative=negative, latent_image=latent_image, seed=seed, steps=steps, cfg=cfg, sampler_name=sampler_name, scheduler=scheduler, denoise=denoise)
		images	= graph.node("VAEDecode", samples=latent.out(0), vae=vae)
		save	= graph.node("SaveImage", images=images.out(0), filename_prefix=filename_prefix)
		return {
			"result" : (images.out(0),),
			"expand" : graph.finalize(),
		}
