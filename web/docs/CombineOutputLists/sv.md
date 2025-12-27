<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists kombinationer

![OutputLists kombinationer](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkluderad)

Tar upp till 4 OutputLists och genererar varje kombination av dem.

Exempel: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` använder `is_output_list=True` (indikerat av symbolet `𝌠`) och kommer att bearbetas sekventiellt av motsvarande noder.

Alla listor är valfria och tomma listor kommer att ignoreras.

Tekniskt beräknar det *kartesiska produkten* och utgår varje kombination uppdelad i sina element (`unzip`), medan tomma listor ersätts med `None` och de skickar `None` på den respektive utgången.

Exempel: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inmatningar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `list_a` | `*` | (valfritt) |
| `list_b` | `*` | (valfritt) |
| `list_c` | `*` | (valfritt) |
| `list_d` | `*` | (valfritt) |

### Utgångar

| Namn | Typ | Beskrivning |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Värdet av kombinationerna som motsvarar `list_a`. |
| `unzip_b` | `* 𝌠` | Värdet av kombinationerna som motsvarar `list_b`. |
| `unzip_c` | `* 𝌠` | Värdet av kombinationerna som motsvarar `list_c`. |
| `unzip_d` | `* 𝌠` | Värdet av kombinationerna som motsvarar `list_d`. |
| `index` | `INT 𝌠` | Omfattning 0..count som kan användas som index. |
| `count` | `INT` | Totala antalet kombinationer. |

