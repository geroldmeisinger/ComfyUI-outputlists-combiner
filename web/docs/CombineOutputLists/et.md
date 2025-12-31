## OutputLists kombinatsioonid

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI töövoog on kaasas)

Võtab kuni 4 OutputListi ja loob nende kõigi kombinatsioonid.

Näide: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

Kõik loendid on valikulised ja tühjad loendid ignoreeritakse.

Tehniliselt arvutab see *Cartesian product* ja väljastab iga kombinatsiooni elementideks jagatuna (`unzip`), kus tühjad loendid asendatakse ühikutega `None` ja need annavad `None` vastavas väljundis.

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
| `index` | `INT 𝌠` | Vahemik 0..count, mida saab kasutada indeksina. |
| `count` | `INT` | Kogu kombinatsioonide arv. |

