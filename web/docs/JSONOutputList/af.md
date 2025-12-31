## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow ingesluit)

Skep 'n OutputList deur arrays of dictionaries uit JSON-objekte te onttrek.
Gebruik JSONPath sintaks om die waardes te onttrek, sien [JSONPath op Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alle gematchte waardes word geplataf in 'n lang lys.
Jy kan ook hierdie node gebruik om objekte van literale string te skep soos `[1, 2, 3]`.
`key`, `value`, `int` en `float` gebruik `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath wat gebruik word om die waardes te onttrek. |
| `json` | `STRING` | 'n JSON string wat vertaal word na 'n objek. |
| `obj` | `*` | (opsioneel) objek van enige tipe wat die JSON string sal vervang |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Die sleutel vir dictionaries of index vir arrays (as string).  Tegnies is dit 'n globale index van die geplatafde lys vir alle nie-sleutels nie. |
| `value` | `STRING 𝌠` | Die waarde as 'n string. |
| `int` | `INT 𝌠` | Die waarde as 'n int (as dit die getal nie kan ontlees nie, gebruik standaard 0). |
| `float` | `FLOAT 𝌠` | Die waarde as 'n float (as dit die getal nie kan ontlees nie, gebruik standaard 0). |
| `count` | `INT` | Totale aantal items in die geplatafde lys |
| `debug` | `STRING` | Debug uitvoer van alle gematchte objekte as 'n geformateerde JSON string |

