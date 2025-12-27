<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinációk OutputList-ből

![Kombinációk OutputList-ből](CombineOutputLists/CombineOutputLists.png)

(ComfyUI munkafolyamat beletartozik)

Maximálisan 4 OutputList-et vesz fel és minden lehetséges kombinációt generál.

Példa: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` használja a `is_output_list=True` (a `𝌠` szimbólum által jelzett) és megfelelő csomópontok által sorban feldolgozva lesz.

Minden lista opcionális, üres listák figyelmen kívül hagyódnak.

Technikailag a *karteszi szorzatot* számítja ki és minden kombinációt az elemekre bontva (a `unzip` segítségével) ad vissza, míg üres listák `None` értékként lesznek cserélve, és az adott kimeneten `None` értéket adnak ki.

Példa: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `list_a` | `*` | (opcionális) |
| `list_b` | `*` | (opcionális) |
| `list_c` | `*` | (opcionális) |
| `list_d` | `*` | (opcionális) |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | A kombinációk értékei, amelyekhez `list_a` tartoznak. |
| `unzip_b` | `* 𝌠` | A kombinációk értékei, amelyekhez `list_b` tartoznak. |
| `unzip_c` | `* 𝌠` | A kombinációk értékei, amelyekhez `list_c` tartoznak. |
| `unzip_d` | `* 𝌠` | A kombinációk értékei, amelyekhez `list_d` tartoznak. |
| `index` | `INT 𝌠` | 0..count tartomány, amely indexként használható. |
| `count` | `INT` | A kombinációk száma. |

