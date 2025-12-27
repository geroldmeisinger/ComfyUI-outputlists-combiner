<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists kombinásjoner

![OutputLists kombinásjoner](CombineOutputLists/CombineOutputLists.png)

(ComfyUI virkni inkludert)

Teknar upp til 4 OutputLists og ger hver kombinásjon av dei.

Dæmi: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` notar `is_output_list=True` (indikerað av symbolinum `𝌠`) og verður handhøvuduð sekvensið av tilhøyrandi nýtarni.

Allar listur eru frivilligar og tómur listar verða burtið.

Tækniskt reknar det *Cartesian produkt* og gefur hver kombinásjon uppdelta í elementin („unzip“), medan tómur listar verða erstatdur av einingum af `None` og deyra `None` á tilhøyrandi útgang.

Dæmi: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inntak

| Nafn | Týp | Lýsing |
| --- | --- | --- |
| `list_a` | `*` | (frivilligt) |
| `list_b` | `*` | (frivilligt) |
| `list_c` | `*` | (frivilligt) |
| `list_d` | `*` | (frivilligt) |

### Útgangar

| Nafn | Týp | Lýsing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Gildið av kombinásjunum tilhøyrandi `list_a`. |
| `unzip_b` | `* 𝌠` | Gildið av kombinásjunum tilhøyrandi `list_b`. |
| `unzip_c` | `* 𝌠` | Gildið av kombinásjunum tilhøyrandi `list_c`. |
| `unzip_d` | `* 𝌠` | Gildið av kombinásjunum tilhøyrandi `list_d`. |
| `index` | `INT 𝌠` | Rúm 0..tala sem kan verða notuð sem index. |
| `count` | `INT` | Samanlagt tal av kombinásjum. |

