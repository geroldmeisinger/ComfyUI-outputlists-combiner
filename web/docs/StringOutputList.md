## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Creates an OutputList by splitting the string in the textfield with a separator.
`value` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | The string used to split the textfield values by. |
| `values` | `STRING` | The text you want to split into a list. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed of whitespace. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | The values from the list. |
| `index` | `INT 𝌠` | Range of 0..count. You can use this as an index. |
| `count` | `INT` | The number of items in the list. |
| `inspect_combo` | `COMBO` | A dummy-output you can use to link to a `COMBO` and pre-fill with it's values. The connection will then be automatically re-linked to `value` output. |
