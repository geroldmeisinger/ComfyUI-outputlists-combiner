## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow mellékletként)

Létrehoz egy OutputList-et számsorozatból.
Belsőleg a [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) függvényt használja, mivel megbízhatóbb a lebegőpontos értékekkel.
Ha szükséged van tetszőleges lépésekkel rendelkező számlistákra, nézd meg a JSON OutputList-et és hozz létre egy tömböt, például `[1, 42, 123]`.
Az `int`, `float`, `string` és `index` használja a `is_output_list=True` (a `𝌠` szimbólummal jelölt) és szekvenciálisan feldolgozásra kerülnek a megfelelő csomópontokban.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `start` | `FLOAT` | Kezdőérték a tartomány generálásához. |
| `stop` | `FLOAT` | Végérték. Ha `endpoint=include`, akkor ez a szám beletartozik a listába. |
| `num` | `INT` | A lista elemeinek száma (ne hasonlítsd össze lépéssel). |
| `endpoint` | `BOOLEAN` | Meghatározza, hogy a `stop` érték be legyen-e vonva vagy kizárva az elemekből. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `int` | `INT 𝌠` | Az érték egész számmá alakítva (lefelé kerekítve). |
| `float` | `FLOAT 𝌠` | Az érték lebegőpontos számként. |
| `string` | `STRING 𝌠` | Az érték lebegőpontos számként konvertálva sztringgé. |
| `index` | `INT 𝌠` | 0..count tartomány, amely indexként használható. |
| `count` | `INT` | Ugyanaz, mint `num`. |

