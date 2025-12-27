<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasyon ng OutputLists

![Kombinasyon ng OutputLists](CombineOutputLists/CombineOutputLists.png)

(naglalagay ng ComfyUI workflow)

Nagpapakita ng hanggang 4 OutputLists at nagpapagawa ng bawat kombinasyon nito.

Halimbawa: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` ginagamit ang `is_output_list=True` (naipapakita sa simbolo `𝌠`) at ipaproseso nang sekuelensyal sa mga tanging node.

Laan ang lahat ng listahan ay optional at ang mga magulo na listahan ay hindi inilalagay.

Tinatagpuan ito ang Cartesian product at nagpapalit ng bawat kombinasyon sa mga elemento (`unzip`), habang ang mga magulo na listahan ay nasa pagkakasunod ng `None` at nagpapakita ng `None` sa mga output.

Halimbawa: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Output

| Name | Type | Description |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Halaga ng mga kombinasyon na tumutugon sa `list_a`. |
| `unzip_b` | `* 𝌠` | Halaga ng mga kombinasyon na tumutugon sa `list_b`. |
| `unzip_c` | `* 𝌠` | Halaga ng mga kombinasyon na tumutugon sa `list_c`. |
| `unzip_d` | `* 𝌠` | Halaga ng mga kombinasyon na tumutugon sa `list_d`. |
| `index` | `INT 𝌠` | Range ng 0..count na maaari gamitin bilang index. |
| `count` | `INT` | Total na bilang ng mga kombinasyon. |

