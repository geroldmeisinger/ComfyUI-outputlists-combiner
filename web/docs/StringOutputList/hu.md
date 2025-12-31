## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow mellékletként)

Létrehoz egy OutputList-et a szövegmezőben lévő szöveg szétvágásával egy elválasztó karakterrel.
A `value` és `index` használja a `is_output_list=True` (a `𝌠` szimbólummal jelölt) és szekvenciálisan feldolgozásra kerülnek a megfelelő csomópontokban.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `separator` | `STRING` | A szövegmező értékeinek szétvágásához használt karakterlánc. |
| `values` | `STRING` | A lista szétvágásához kívánt szöveg. Megjegyzés: a karakterlánc végén lévő új sorok levágásra kerülnek a szétvágás előtt, és minden elem után is eltávolítja a fehér karaktereket. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `value` | `* 𝌠` | A lista értékei. |
| `index` | `INT 𝌠` | 0..count tartomány. Ezt indexként használhatod. |
| `count` | `INT` | A lista elemeinek száma. |
| `inspect_combo` | `COMBO` | Egy dummy-kimenet, amelyet használhatsz egy `COMBO` csatlakoztatásához, és előre töltse fel annak értékeivel. A kapcsolat automatikusan át lesz irányítva a `value` kimenetre. |

