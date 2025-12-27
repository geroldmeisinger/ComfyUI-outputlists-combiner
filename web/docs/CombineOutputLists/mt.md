<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinazzjoni ta’ OutputLists

![Kombinazzjoni ta’ OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow ta’ ComfyUI inkluż)

Jikkupri 4 OutputLists u jipproduċi kwalunkwe kombinazzjoni tagħhom.

Eżempju: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` jistgħu jikbru `is_output_list=True` (indikat minn `𝌠`) u jinħolqu sekwentjalment mit-tajjeb tal-karigi kien.

Kull lista hija opzjonali u listi vojt jinħolqu.

Tiknikament jikkalkula *l-prodott karteżjanu* u jippubblika kwalunkwe kombinazzjoni miktuba f’elementi (`unzip`), imbagħad listi vojt jinżlu b’unitajiet ta’ `None` u jipproduċu `None` fuq l-outputs kien.

Eżempju: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Isem | Tip | Deskrittjoni |
| --- | --- | --- |
| `list_a` | `*` | (opzjonali) |
| `list_b` | `*` | (opzjonali) |
| `list_c` | `*` | (opzjonali) |
| `list_d` | `*` | (opzjonali) |

### Output

| Isem | Tip | Deskrittjoni |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valuri tal-kombinazzjonijiet li jikkorrispondu mal `list_a`. |
| `unzip_b` | `* 𝌠` | Valuri tal-kombinazzjonijiet li jikkorrispondu mal `list_b`. |
| `unzip_c` | `* 𝌠` | Valuri tal-kombinazzjonijiet li jikkorrispondu mal `list_c`. |
| `unzip_d` | `* 𝌠` | Valuri tal-kombinazzjonijiet li jikkorrispondu mal `list_d`. |
| `index` | `INT 𝌠` | Range ta’ 0..count li jista’ jkun istifed bħal indekss. |
| `count` | `INT` | Numru totali tal-kombinazzjonijiet. |

