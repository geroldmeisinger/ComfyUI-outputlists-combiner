<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## 转换为整数 浮点数 字符串

![转换为整数 浮点数 字符串](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(包含 ComfyUI 工作流)

将任何类似数字的内容转换为 `INT` `FLOAT` `STRING`。
内部使用 `nums_from_string.get_nums`，该函数对接受的数字非常宽松。支持实际的整数、实际的浮点数、以字符串形式表示的整数或浮点数，以及包含千位分隔符的多个数字的字符串。
使用字符串 `123;234;345` 可快速生成数字列表。不要使用逗号作为分隔符，因为它们可能被解释为千位分隔符。
`int`、`float` 和 `string` 使用 `is_output_list=True`（由符号 `𝌠` 表示），并将由对应节点依次处理。

### 输入

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `any` | `*` | 任何可以有意义地转换为字符串且包含可解析数字的内容 |

### 输出

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| `int` | `INT 𝌠` | 在字符串中找到的所有数字，小数部分被截断。 |
| `float` | `FLOAT 𝌠` | 在字符串中找到的所有数字，以浮点数形式输出。 |
| `string` | `STRING 𝌠` | 在字符串中找到的所有数字，转换为字符串形式输出。 |
| `count` | `INT` | 在值中找到的数字数量。 |

