## Formatted String

![Formatted String](/media/FormattedString.png)

(ComfyUI workflow included)

Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`.
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `fstring`	| `STRING`	| Uses python `str.format()` internally, see [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) . * Use `{a:.2f}` to round off a float to 2 decimals. * Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`. * If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`.	|
| `a`	| `*`	| (optional) value that will be as a string at the `{a}` placeholder.	|
| `b`	| `*`	| (optional) value that will be as a string at the `{b}` placeholder.	|
| `c`	| `*`	| (optional) value that will be as a string at the `{c}` placeholder.	|
| `d`	| `*`	| (optional) value that will be as a string at the `{d}` placeholder.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `string`	| `STRING`	| The formatted string with all placeholders replaced with their respective values.	|
