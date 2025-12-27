<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinaciones de OutputLists

![Combinaciones de OutputLists](CombineOutputLists/CombineOutputLists.png)

(Flujo de trabajo de ComfyUI incluido)

Toma hasta 4 OutputLists y genera todas las combinaciones posibles entre ellas.

Ejemplo: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilizan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesados secuencialmente por los nodos correspondientes.

Todos los listados son opcionales y los listados vacíos serán ignorados.

Técnicamente calcula *el producto cartesiano* y entrega cada combinación separada en sus elementos (`unzip`), mientras que los listados vacíos serán reemplazados por unidades de `None` y emitirán `None` en la salida correspondiente.

Ejemplo: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `list_a` | `*` | (opcional) |
| `list_b` | `*` | (opcional) |
| `list_c` | `*` | (opcional) |
| `list_d` | `*` | (opcional) |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor de las combinaciones correspondientes a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor de las combinaciones correspondientes a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor de las combinaciones correspondientes a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor de las combinaciones correspondientes a `list_d`. |
| `index` | `INT 𝌠` | Rango de 0..count que puede usarse como índice. |
| `count` | `INT` | Número total de combinaciones. |

