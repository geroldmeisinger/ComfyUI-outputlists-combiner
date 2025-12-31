## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Jibbnu lista tal-output billi jibdlu l-arrays jew dictionaries mis-JSON objects.
Jibbraw sintassi ta’ JSONPath biex jibdlu l-valuri, ara [JSONPath fuq Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Kollha valuri mibduta jkunu flatten f’lista twil.
Tista’ tuża din il-node biex tibbnu oġġetti mis-string literal bħall-`[1, 2, 3]`.
`key`, `value`, `int` u `float` jibbraw `is_output_list=True` (indikat bil-simbolu `𝌠`) u jkunu pproċessati seqqunzjalment minn nodi korrispondenti.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath li jibdul l-valuri. |
| `json` | `STRING` | Stringi ta’ JSON li jkien jibdul għal oġġett. |
| `obj` | `*` | (opzjonali) oġġett ta’ kwalunkwe tip li jibdul il-stringi ta’ JSON |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Il-key għal dictionaries jew l-indiċi għal arrays (bħala string).  Teknikament hija indekss globali tal-lista flattened għal kollu li m’għandhomx keys. |
| `value` | `STRING 𝌠` | Il-valur bħala string. |
| `int` | `INT 𝌠` | Il-valur bħala int (jekk ma jistgħux jipproċessaw in-numru, jibqgħu bħala 0). |
| `float` | `FLOAT 𝌠` | Il-valur bħala float (jekk ma jistgħux jipproċessaw in-numru, jibqgħu bħala 0). |
| `count` | `INT` | Numru totali ta’ oġġetti fl-lista flattened |
| `debug` | `STRING` | Output ta’ debug ta’ kollu l-oġġetti mibduta bħala stringi ta’ JSON formattati |

