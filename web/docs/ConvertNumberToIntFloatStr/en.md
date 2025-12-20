## Convert To Int Float Str

![Convert To Int Float Str](/media/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Convert anything number-like to `INT` `FLOAT` `STRING`.
Uses `nums_from_string.get_nums` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.
Use a string `123;234;345` to quickly generate a list of numbers. Don't use commas as separators as they may be interpreted as thousand-separators.
`int`, `float` and `string` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `any`	| `*`	| Anything that can be meaningfully converted to a string with parseable numbers inside	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `int`	| `INT 𝌠`	| All the numbers found in the string with the decimals truncated.	|
| `float`	| `FLOAT 𝌠`	| All the numbers found in the string as floats.	|
| `string`	| `STRING 𝌠`	| All the numbers found in the string as floats converted to string.	|
| `count`	| `INT`	| Amount of numbers found in the value.	|
