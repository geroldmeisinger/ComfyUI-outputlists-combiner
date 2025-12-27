<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinações de OutputLists

![Combinações de OutputLists](CombineOutputLists/CombineOutputLists.png)

(fluxo do ComfyUI incluído)

Toma até 4 OutputLists e gera todas as combinações entre elas.

Exemplo: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` utilizam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nós correspondentes.

Todas as listas são opcionais e listas vazias serão ignoradas.

Tecnicamente calcula o *produto cartesiano* e devolve cada combinação dividida em seus elementos (`unzip`), enquanto listas vazias serão substituídas por unidades de `None` e emitirão `None` na saída correspondente.

Exemplo: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `list_a` | `*` | (opcional) |
| `list_b` | `*` | (opcional) |
| `list_c` | `*` | (opcional) |
| `list_d` | `*` | (opcional) |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valor das combinações correspondentes a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor das combinações correspondentes a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor das combinações correspondentes a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor das combinações correspondentes a `list_d`. |
| `index` | `INT 𝌠` | Intervalo de 0..count que pode ser usado como índice. |
| `count` | `INT` | Número total de combinações. |

