## OutputLists kombinációk

![OutputLists Kombinációk](CombineOutputLists/CombineOutputLists.png)

(ComfyUI munkafolyamat beépítve)

Legfeljebb 4 OutputList fogadása és minden kombinációjuk generálása.

Példa: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` használja a `is_output_list=True` (jelezve a `𝌠` szimbólummal) és sorban feldolgozásra kerülnek a megfelelő csomópontok által.

Minden lista nem kötelező és az üres listák figyelmen kívül lesznek hagyva.

Technikailag a *Descartes-szorzatot* számítja ki és minden kombinációt szétválasztja az elemekre (`unzip`), míg az üres listák `None` egységekkel lesznek helyettesítve és azok `None` értéket adnak ki a megfelelő kimeneten.

Példa: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `list_a` | `*` | (nem kötelező) |
| `list_b` | `*` | (nem kötelező) |
| `list_c` | `*` | (nem kötelező) |
| `list_d` | `*` | (nem kötelező) |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | A kombinációk értéke, amelyek megfelelnek a `list_a` listának. |
| `unzip_b` | `* 𝌠` | A kombinációk értéke, amelyek megfelelnek a `list_b` listának. |
| `unzip_c` | `* 𝌠` | A kombinációk értéke, amelyek megfelelnek a `list_c` listának. |
| `unzip_d` | `* 𝌠` | A kombinációk értéke, amelyek megfelelnek a `list_d` listának. |
| `index` | `INT 𝌠` | 0..count tartomány, amely indexként használható. |
| `count` | `INT` | A kombinációk összes száma. |

