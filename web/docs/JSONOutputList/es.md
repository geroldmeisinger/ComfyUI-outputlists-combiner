## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow incluido)

Crea una OutputList extrayendo matrices o diccionarios de objetos JSON.
Utiliza la sintaxis JSONPath para extraer los valores, vea [JSONPath en Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Todos los valores coincidentes se aplanan en una sola lista larga.
También puede usar este nodo para crear objetos a partir de cadenas literales como `[1, 2, 3]`.
`key`, `value`, `int` y `float` usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath utilizado para extraer los valores. |
| `json` | `STRING` | Una cadena JSON que se traduce a un objeto. |
| `obj` | `*` | (opcional) objeto de cualquier tipo que reemplazará la cadena JSON |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `key` | `STRING 𝌠` | La clave para diccionarios o índice para matrices (como cadena). Técnicamente es un índice global de la lista aplanada para todos los no-claves. |
| `value` | `STRING 𝌠` | El valor como cadena. |
| `int` | `INT 𝌠` | El valor como entero (si no puede analizar el número, por defecto es 0). |
| `float` | `FLOAT 𝌠` | El valor como flotante (si no puede analizar el número, por defecto es 0). |
| `count` | `INT` | Número total de elementos en la lista aplanada |
| `debug` | `STRING` | Salida de depuración de todos los objetos coincidentes como una cadena JSON formateada |

