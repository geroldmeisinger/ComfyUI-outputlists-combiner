import hashlib
import time

from comfy_api.latest import io

from .util import *


class BakeString(io.ComfyNode):

	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """Works as a simple string passthrough first but 'bakes' the string into the `override` field of the workflow JSON and then uses this value instead.

This node may seem strange but it allows to add additional infos on how a specific image was created in a multi-asset workflow.

* Use-case 1 "per-image paramters": If multiple images are created from an output list, the same workflow is stored for ALL images. This node allows to bake the specific string into the workflow JSON for the very string that was used in a individual image.
* Use-case 2 "include image": img2img and controlnet workflows require an input image. Used together with a base64 string the full image can be baked into the workflow JSON.
""",
			node_id	= "BakeString",
			display_name	= "Bake String",
			category	= CATEGORY,
			inputs	= [
				io.String	.Input("string", display_name="string", default= "", lazy=True, tooltip="The string that will be passed through unless `override` is set (lazy=True which means upstream nodes won't be executed if `override` is set)"),
				io.String	.Input("override",
					display_name	= "override",
					multiline	= True,
					default	= "",
					placeholder	= "<EMPTY STRING>",
					tooltip	= "If set, will always output this string instead. Used by `Save Image` (and other save nodes) to bake the value into the workflow JSON.",
				),
				io.Int	.Input("limit", display_name="limit", default=10240, min=0, max=2**32, tooltip="Limit of characters which will be baked into the field."),
				io.Boolean	.Input("trim", display_name="trim", default=True, tooltip="Trims the `override` string of whitespace characters (like spaces and new lines) before doing the override-check. This prevents triggering the override when a new line was entered by accident. Only disable it if you actually need a whitespace string as an override."),
			],
			outputs=[
				io.String	.Output("string"	, display_name="string"	, is_output_list=False, tooltip="If `override` is set, will use `override`, otherwise it's a passtrough of `string`."),
				io.Boolean	.Output("is_override"	, display_name="is_override"	, is_output_list=False, tooltip="A bool indicating if the override was used. Useful for If/Else Switches and Execution Blockers.")
			],
			hidden=[io.Hidden.unique_id, io.Hidden.extra_pnginfo, io.Hidden.dynprompt],
			is_experimental=True,
		)
		return ret

	@classmethod
	def execute(cls, string: str, limit: int, trim: bool = True, override: str = "") -> io.NodeOutput:
		override = override.strip() if trim else override
		ret_str = string if override == "" else override

		if ret_str and len(ret_str) < limit * 1024 and cls.hidden.extra_pnginfo and cls.hidden.unique_id:
			nodes	= (cls.hidden.extra_pnginfo or {}).get("workflow", {}).get("nodes", []) if cls.hidden.extra_pnginfo is not None else []
			id	= cls.hidden.unique_id
			while id in cls.hidden.dynprompt.ephemeral_display:
				id = cls.hidden.dynprompt.ephemeral_display[id]
			for node in nodes:
				if str(node['id']) == id:
					node['widgets_values'][1] = ret_str
					break

		ret = io.NodeOutput(ret_str, override != "")
		return ret

	@classmethod
	def check_lazy_status(cls, string: str, limit: int, trim: bool = True, override: str = ""):
		override = override.strip() if trim else override
		if override != "": return []
		return ["string", "limit", "trim"]

	@classmethod
	def fingerprint_inputs(cls, string: str, limit: int, trim: bool = True, override: str = "") -> str:
		if not string and not override: return str(time.time()) # https://github.com/comfyanonymous/ComfyUI/issues/11017
		override = override.strip() if trim else override
		ret_str = string if override == "" else override

		m	= hashlib.sha256(ret_str.encode('utf-8'))
		ret = m.digest().hex()
		return ret