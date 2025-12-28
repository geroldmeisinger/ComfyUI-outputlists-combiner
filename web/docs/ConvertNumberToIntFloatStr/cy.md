<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Trosi i Int Gwirioneddol Str

![Trosi i Int Gwirioneddol Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(gweithlun ComfyUI wedi'i ychwanegu)

Trosi unrhyw beth sydd â rhagor o niferoedd i `INT` `GWIRIONEDDOL` `RHYNGOEDD`.
Defnyddir `nums_from_string.get_nums` yn gartref i'w gael, sydd yn gyfrifol yn aml i'r niferoedd sydd yn cael eu cymryd. unrhyw beth o INTiau gwirioneddol, gwirioneddau gwirioneddol, INTiau neu gwirioneddau fel testun, testun sydd â nifer o niferoedd gyda rhagorau chwech.
Defnyddio testun `123;234;345` i greu rhestr o niferoedd yn gynt. Peidiwch â defnyddio cwmni fel rhagorion oherwydd gallant gael eu cyflwyno fel rhagorau chwech.
Mae `int`, `float` a `string` yn defnyddio `is_output_list=True` (a'i ddau ar gyfer y symbol `𝌠`) ac yn cael eu prosesu yn y tro yn y cyd-destun.

### Myneddiadau

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `any` | `*` | unrhyw beth sydd yn gallu cael ei trosi i testun gyda rhagor o niferoedd sydd yn cael eu darllen |

### Allforion

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `int` | `INT 𝌠` | Pob nifer a gafodd ei ddarganfod yn y testun gyda'r degolion wedi'u tynnu. |
| `float` | `FLOAT 𝌠` | Pob nifer a gafodd ei ddarganfod yn y testun fel gwirioneddau. |
| `string` | `STRING 𝌠` | Pob nifer a gafodd ei ddarganfod yn y testun fel gwirioneddau a gafodd eu trosi i testun. |
| `count` | `INT` | Cyfanswm y niferoedd a gafodd eu ddarganfod yn y gwerth. |

