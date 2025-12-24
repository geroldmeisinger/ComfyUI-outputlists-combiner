from comfy_api.latest import io


class FormattedString(io.ComfyNode):
	DESCRIPTION = """String with variable placeholders which will replaced with their respective values.
Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.

Also applies "search & replace" (S&R) syntax such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.
Thus you can also use it as a getter node.
Note that "search & replace" takes place in Javascript context which runs before node execution.

The final string will be baked into `override` in the workflow JSON, which is useful if you want to restore the very image generated from a list.
"""

	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= FormattedString.DESCRIPTION,
			node_id	= "FormattedString",
			display_name	= "Formatted String",
			category	= "Utility",
			inputs	= [
				io.String.Input("fstring",
					display_name	= "fstring",
					multiline	= True,
					default	= "{a}_{b}_{c}_{d}",
					tooltip	= FormattedString.DESCRIPTION,
				),
				io.AnyType.Input("a", display_name="a", optional=True, tooltip="(optional) value that will be as a string at the `{a}` placeholder."),
				io.AnyType.Input("b", display_name="b", optional=True, tooltip="(optional) value that will be as a string at the `{b}` placeholder."),
				io.AnyType.Input("c", display_name="c", optional=True, tooltip="(optional) value that will be as a string at the `{c}` placeholder."),
				io.AnyType.Input("d", display_name="d", optional=True, tooltip="(optional) value that will be as a string at the `{d}` placeholder."),
				io.String.Input("override",
					display_name	= "override",
					multiline	= False,
					default	= "",
					tooltip	= "If set, will always output this string instead. Used by `Save Image` to bake the value into the workflow JSON.",
				),
			],
			outputs=[
				io.String.Output("string", display_name="string", is_output_list=False, tooltip="The formatted string with all placeholders replaced with their respective values."),
			],
			hidden=[io.Hidden.unique_id, io.Hidden.extra_pnginfo]
		)
		return ret

	@classmethod
	def execute(self, fstring: str, a: any = "", b: any = "", c: any = "", d: any = "", override: str = "") -> io.NodeOutput:
		ret_str = fstring.format(a=a, b=b, c=c, d=d) if override == "" else override

		if self.hidden.extra_pnginfo and self.hidden.unique_id:
			nodes = (self.hidden.extra_pnginfo or {}).get("workflow", {}).get("nodes", []) if self.hidden.extra_pnginfo is not None else []
			for node in nodes:
				if str(node['id']) == str(self.hidden.unique_id):
					node['widgets_values'][1] = ret_str
					break

		ret = io.NodeOutput(ret_str)
		return ret
