## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Creates an OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
All matched values are flatten into one long list.
You can also use this node to create objects from literal strings like `[1, 2, 3]`.
`key`, `value`, `int` and `float` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath used to extract the values. |
| `json` | `STRING` | A JSON string which is translated to an object. |
| `obj` | `*` | (optional) object of any type which will replace the JSON string |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | The key for dictionaries or index for arrays (as string).  Technically it's a global index of the flattened list for all non-keys. |
| `value` | `STRING 𝌠` | The value as a string. |
| `int` | `INT 𝌠` | The value as a int (if it cannot parse the number, defaults to 0). |
| `float` | `FLOAT 𝌠` | The value as a float (if it cannot parse the number, defaults to 0). |
| `count` | `INT` | Total number of items in the flattened list |
| `debug` | `STRING` | Debug output of all matched objects as a formatted JSON string |
