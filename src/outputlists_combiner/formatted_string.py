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
			],
			outputs=[
				io.String.Output("string", display_name="string", is_output_list=False, tooltip="The formatted string with all placeholders replaced with their respective values."),
			],
		)
		return ret

	@classmethod
	def execute(self, fstring: str, a: any = "", b: any = "", c: any = "", d: any = "") -> io.NodeOutput:
		ret = io.NodeOutput(fstring.format(a=a, b=b, c=c, d=d))
		return ret
