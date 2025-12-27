<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combiniadau OutputLists

![Combiniadau OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

Gwnewch i 4 OutputLists a gweithredu pob combi'n i ddynod.

Gwnewch: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` defnyddir `is_output_list=True` (yn ymddangos gan y symble `𝌠`) ac mae'n cael ei wneud yn ymddangos yn ymddangos gan nodau'r gweithredu.

Mae pob list yn optional a mae listau holl yma yn cael eu ddod yma.

Gwnewch yn gyflwr yw *y product cyflwr* ac yn gweithredu pob combi'n yn ymddangos yn ymddangos gan y gweithredu (`unzip`), yn ymddangos yn ymddangos gan y symble `None` ac mae'n cyflwr `None` ar y gweithredu.

Gwnewch: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Adroddwyr

| Adrodd | Rhif | Gwnewch |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Adroddwyr

| Adrodd | Rhif | Gwnewch |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Gwnewch y combi'n ar gyfer `list_a`. |
| `unzip_b` | `* 𝌠` | Gwnewch y combi'n ar gyfer `list_b`. |
| `unzip_c` | `* 𝌠` | Gwnewch y combi'n ar gyfer `list_c`. |
| `unzip_d` | `* 𝌠` | Gwnewch y combi'n ar gyfer `list_d`. |
| `index` | `INT 𝌠` | Gwnewch o 0..count sydd yn cael ei wneud yn index. |
| `count` | `INT` | Rhif o combi'n. |

