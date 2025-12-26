## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow included)

Creates a OutputList by separating the string in the textfield.
`value` and `index` use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `separator` | `STRING` | The string to split the textfield values by. |
| `values` | `STRING` | The string which will be separated. Note that the string is trimmed of trailing newlines before splitting, and each item is again trimmed. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | The values from the list. |
| `index` | `INT 𝌠` | Range of 0..count which can be used as an index. |
| `count` | `INT` | The number of items in the list. |
| `inspect_combo` | `COMBO` | A dummy output only used to pre-fill the list with values from an other `COMBO` input and will automatically disconnect again |
