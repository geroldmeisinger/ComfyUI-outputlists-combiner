## Number OutputList

![Number OutputList](/media/NumberOutputList.png)

(ComfyUI workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internally because it works more reliably with floatingpoint values.
If you want to define number lists with arbitrary steps instead check out the JSON OutputList and define an array like `[1, 42, 123]`.
`int`, `float`, `string` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `start`	| `FLOAT`	| Start value to generate the range from.	|
| `stop`	| `FLOAT`	| End value. If `endpoint=include` this number will be included in the list.	|
| `num`	| `INT`	| The number of items in the list (not to be confused with a `step`).	|
| `endpoint`	| `BOOLEAN`	| Decides if the `stop` value should be included or excluded in the items.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `int`	| `INT 𝌠`	| The value converted to int (rounded down/floored).	|
| `float`	| `FLOAT 𝌠`	| The value as a float.	|
| `string`	| `STRING 𝌠`	| The value as a float converted to string.	|
| `index`	| `INT 𝌠`	| Range of 0..count which can be used as an index.	|
| `count`	| `INT`	| Same as `num`.	|
