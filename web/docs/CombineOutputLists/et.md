<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists kombinatsioonid

![OutputLists kombinatsioonid](CombineOutputLists/CombineOutputLists.png)

(ComfyUI töövoolu sisend)

Võtab kuni 4 OutputLists ja loob iga võimaliku kombinatsiooni nende vahel.

Näide: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` kasutab `is_output_list=True` (märkitud sümboliga `𝌠`) ja on eelkõige käivitatud vastavate node-ide kaudu.

Kõik loendud on valikulised ja tühi loendid tulevad täpselt üle.

Täpselt arvutab *karteesi produktsi* ja väljastab iga kombinatsiooni elementideks (`unzip`), kus tühi loendid asendatakse `None` ja need väljastavad `None` vastavate väljundite kaudu.

Näide: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `list_a` | `*` | (valikuline) |
| `list_b` | `*` | (valikuline) |
| `list_c` | `*` | (valikuline) |
| `list_d` | `*` | (valikuline) |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Kombinatsioonide väärtus, mis vastab `list_a`. |
| `unzip_b` | `* 𝌠` | Kombinatsioonide väärtus, mis vastab `list_b`. |
| `unzip_c` | `* 𝌠` | Kombinatsioonide väärtus, mis vastab `list_c`. |
| `unzip_d` | `* 𝌠` | Kombinatsioonide väärtus, mis vastab `list_d`. |
| `index` | `INT 𝌠` | 0..count vahemik, mis saab kasutada indeksina. |
| `count` | `INT` | Kombinatsioonide kogus. |

