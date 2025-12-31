## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow je zahrnutý)

Vytvorí OutputList rozdelením reťazca v textovom poli oddeľovačom.
`value` a `index` používajú `is_output_list=True` (označené symbolom `𝌠`) a budú spracované postupne príslušnými uzlami.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `separator` | `STRING` | Reťazec použitý na rozdelenie hodnôt z textového poľa. |
| `values` | `STRING` | Text, ktorý chcete rozdeliť na zoznam. Upozorňujeme, že reťazec je pred rozdelením orezaný od koncových nových riadkov a každá položka je opäť orezaná od medzier. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `value` | `* 𝌠` | Hodnoty zo zoznamu. |
| `index` | `INT 𝌠` | Rozsah 0..počet. Môžete ho použiť ako index. |
| `count` | `INT` | Počet položiek v zozname. |
| `inspect_combo` | `COMBO` | Falošný výstup, ktorý môžete použiť na pripojenie k `COMBO` a predvyplnenie jeho hodnotami. Pripojenie sa potom automaticky prepojí na výstup `value`. |

