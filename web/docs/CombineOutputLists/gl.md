<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinacións de OutputLists

![Combinacións de OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow de ComfyUI incluído)

Toma ata 4 OutputLists e genera todas as súas combinacións.

Exemplo: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesados secuencialmente por nosas nodos.

All lists are optional and empty lists will be ignored.

Técnicamente calcula *o produto cartesiano* e emite cada combinación dividida en seus elementos (`unzip`), mentres que listas vazas serán substituídas por unidades de `None` e emitirán `None` no seu output respectivo.

Exemplo: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `list_a` | `*` | (opcional) |
| `list_b` | `*` | (opcional) |
| `list_c` | `*` | (opcional) |
| `list_d` | `*` | (opcional) |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor das combinacións correspondentes a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor das combinacións correspondentes a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor das combinacións correspondentes a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor das combinacións correspondentes a `list_d`. |
| `index` | `INT 𝌠` | Rango de 0..count que pode usarse como índice. |
| `count` | `INT` | Número total de combinacións. |

