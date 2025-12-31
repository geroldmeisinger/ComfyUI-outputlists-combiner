## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow ingesluit)

Skep 'n OutputList deur die string in die teksveld te verdeel met 'n separator.
`value` en `index` gebruik(s) `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `separator` | `STRING` | Die string wat gebruik word om die teksveld waardes te verdeel. |
| `values` | `STRING` | Die teks wat jy wil verdeel in 'n lys. Merk op dat die string afgesny word van afsluitende nuwe lyne voor verdeel, en elke item weer afgesny word van spasies. |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `value` | `* 𝌠` | Die waardes van die lys. |
| `index` | `INT 𝌠` | Reeks van 0..count. Jy kan dit gebruik as 'n index. |
| `count` | `INT` | Die aantal items in die lys. |
| `inspect_combo` | `COMBO` | 'n Dummy-uitvoer wat jy kan gebruik om te koppel aan 'n `COMBO` en voorvul met sy waardes. Die verbindings sal dan outomaties herverbind word na die `value` uitvoer. |

