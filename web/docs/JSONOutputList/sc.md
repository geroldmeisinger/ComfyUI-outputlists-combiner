## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Cretz un’OutputList in manera de iscollere arrays o dictionaries dae objectos JSON.
Impreada sa sintassi JSONPath pro iscollere sos balores, si veit a [JSONPath in Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Totu sos balores iscollidos sunt unificados in una lista longa.
Podes impreare custu node pro creare objectos dae cartas literales comente `[1, 2, 3]`.
`key`, `value`, `int` e `float` impreadu s’`is_output_list=True` (indikadu dae su simbolu `𝌠`) e sunt elaborados in manera sequentziale dae sos nodes correispondentes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath impreadu pro iscollere sos balores. |
| `json` | `STRING` | Una carta JSON chi est traduzida a un objectu. |
| `obj` | `*` | (optzionale) objectu de unu de tipos chi sustituit a cartas JSON |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Sa chi de sos dictionaries o s’ìnditze de sos arrays (comente carta).  Tecnicamente est un’ìnditze globale de sa lista unificada pro totu non-chis. |
| `value` | `STRING 𝌠` | Su balore comente carta. |
| `int` | `INT 𝌠` | Su balore comente int (si non si podet analizare su nùmeru, su valor predefinidu est 0). |
| `float` | `FLOAT 𝌠` | Su balore comente float (si non si podet analizare su nùmeru, su valor predefinidu est 0). |
| `count` | `INT` | Nùmeru totale de elementos in sa lista unificada |
| `debug` | `STRING` | Balore de debug de totu sos objectos iscollidos comente una carta JSON formatada |

