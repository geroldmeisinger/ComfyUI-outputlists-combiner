## 格式化字符串

![格式化字符串](FormattedString/FormattedString.png)

(包含 ComfyUI workflow)

创建一个包含占位符变量的字符串，并将其替换为相应的值。
内部使用 Python 的 `str.format()`，请参见 [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)。
* 你可以使用 `{a:.2f}` 将浮点数四舍五入到小数点后两位。
* 你可以使用 `{a:05d}` 填充到最多 5 个前导零以匹配 ComfyUI 的文件名后缀 `ComfyUI_00001_.png`。
* 如果你想在字符串中写入 `{ }`（例如 JSON），必须将它们加倍：`{{ }}`。

还应用了 *搜索与替换（S&R）语法*，例如 `%date:yyyy-MM-dd hh:mm:ss%` 和 `%KSampler.seed%`。
因此你也可以将其用作 `GET-node`。
注意，“搜索与替换”在 JavaScript 上下文中进行，并在节点执行之前运行。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `fstring` | `STRING` | 创建一个包含占位符变量的字符串，并将其替换为相应的值。<br>内部使用 Python 的 `str.format()`，请参见 [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)。<br>* 你可以使用 `{a:.2f}` 将浮点数四舍五入到小数点后两位。<br>* 你可以使用 `{a:05d}` 填充到最多 5 个前导零以匹配 ComfyUI 的文件名后缀 `ComfyUI_00001_.png`。<br>* 如果你想在字符串中写入 `{ }`（例如 JSON），必须将它们加倍：`{{ }}`。<br><br>还应用了 *搜索与替换（S&R）语法*，例如 `%date:yyyy-MM-dd hh:mm:ss%` 和 `%KSampler.seed%`。<br>因此你也可以将其用作 `GET-node`。<br>注意，“搜索与替换”在 JavaScript 上下文中进行，并在节点执行之前运行。 |
| `a` | `*` | （可选）将作为字符串插入到 `{a}` 占位符处的值。 |
| `b` | `*` | （可选）将作为字符串插入到 `{b}` 占位符处的值。 |
| `c` | `*` | （可选）将作为字符串插入到 `{c}` 占位符处的值。 |
| `d` | `*` | （可选）将作为字符串插入到 `{d}` 占位符处的值。 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `string` | `STRING` | 所有占位符都被替换为相应值后的格式化字符串。 |

