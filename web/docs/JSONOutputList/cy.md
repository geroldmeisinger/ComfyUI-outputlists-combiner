## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(Cyflun ComfyUI wedi'i gynnwys)

Creu OutputList trwy echdynnu araeau neu geirfa o wrthrychau JSON.
Mae'n defnyddio syntax JSONPath i echdynnu'r gwerthoedd, gweler [JSONPath ar Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Pob gwerth a gydwgir yn cael ei lflatennu i un rhestr hir.
Gallwch hefyd ddefnyddio'r nod hwn i greu gwrthrychau o linynnau llythyr fel `[1, 2, 3]`.
Mae `key`, `value`, `int` a `float` yn defnyddio `is_output_list=True` (a nodir gan y symbol `𝌠`) ac byddent yn cael eu prosesu'n dilynol gan nodau cyfatebol.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath a ddefnyddir i echdynnu'r gwerthoedd. |
| `json` | `STRING` | Llinyn JSON sy'n cael ei gyfieithu i wrthrych. |
| `obj` | `*` | (dewisol) wrthrych o unrhyw fath a fydd yn amnewid y llinyn JSON |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Y allwedd ar gyfer geirfa neu indecs ar gyfer araeu (fel llinyn).  Yn technegol mae'n indecs byd-eang y rhestr a lflatennwyd ar gyfer pob un heblaw'r allweddi. |
| `value` | `STRING 𝌠` | Y gwerth fel llinyn. |
| `int` | `INT 𝌠` | Y gwerth fel int (os na all ei parse'r rhif, yn ddiofyn i 0). |
| `float` | `FLOAT 𝌠` | Y gwerth fel ffloat (os na all ei parse'r rhif, yn ddiofyn i 0). |
| `count` | `INT` | Nifer gyfanswm o eitemau yn y rhestr a lflatennwyd |
| `debug` | `STRING` | Allbwn debug o'r holl wrthrychau a gydwgir fel llinyn JSON a fformatiwyd |

