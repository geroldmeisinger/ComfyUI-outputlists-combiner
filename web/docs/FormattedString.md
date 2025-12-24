## Formatted String

![Formatted String](/media/FormattedString.png)

(ComfyUI workflow included)

String with variable placeholders which will replaced with their respective values.
Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.

Also applies "search & replace" (S&R) syntax such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.
Thus you can also use it as a getter node.
Note that "search & replace" takes place in Javascript context which runs before node execution.

The final string will be baked into `override` in the workflow JSON, which is useful if you want to restore the very image generated from a list.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `fstring`	| `STRING`	| String with variable placeholders which will replaced with their respective values.<br>Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Use `{a:.2f}` to round off a float to 2 decimals.<br>* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.<br>* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.<br><br>Also applies "search & replace" (S&R) syntax such as `%date:yyyy-MM-dd hh:mm:ss%` and `%KSampler.seed%`.<br>Thus you can also use it as a getter node.<br>Note that "search & replace" takes place in Javascript context which runs before node execution.<br><br>The final string will be baked into `override` in the workflow JSON, which is useful if you want to restore the very image generated from a list.	|
| `a`	| `*`	| (optional) value that will be as a string at the `{a}` placeholder.	|
| `b`	| `*`	| (optional) value that will be as a string at the `{b}` placeholder.	|
| `c`	| `*`	| (optional) value that will be as a string at the `{c}` placeholder.	|
| `d`	| `*`	| (optional) value that will be as a string at the `{d}` placeholder.	|
| `override`	| `STRING`	| If set, will always output this string instead. Used by `Save Image` to bake the value into the workflow JSON.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `string`	| `STRING`	| The formatted string with all placeholders replaced with their respective values.	|
