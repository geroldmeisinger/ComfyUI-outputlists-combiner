## Combinacións de Listas de Saída

![Combinacións de Listas de Saída](CombineOutputLists/CombineOutputLists.png)

(Workflow de ComfyUI incluído)

Toma ata 4 Listas de Saída e xera todas as combinacións posibles delas.

Exemplo: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` usa(n) `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesadas secuencialmente por nodos correspondentes.

Todas as listas son opcionais e as listas baleiras serán ignoradas.

Tecnicamente calcula o *produto cartesiano* e devolve cada combinación dividida nos seus elementos (`unzip`), mentres que as listas baleiras serán substituídas por unidades de `None` e emitirán `None` na saída respectiva.

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
| `index` | `INT 𝌠` | Intervalo de 0..count que pode ser usado como índice. |
| `count` | `INT` | Número total de combinacións. |

