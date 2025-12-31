## Combinações de Listas de Saída

![Combinações de Listas de Saída](CombineOutputLists/CombineOutputLists.png)

(Workflow do ComfyUI incluído)

Recebe até 4 Listas de Saída e gera todas as combinações possíveis entre elas.

Exemplo: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` usa(m) `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nós correspondentes.

Todas as listas são opcionais e listas vazias serão ignoradas.

Tecnicamente, ele calcula o *produto cartesiano* e gera cada combinação separada em seus elementos (`unzip`), enquanto listas vazias serão substituídas por unidades de `None` e elas emitirão `None` na saída respectiva.

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
| `unzip_a` | `* 𝌠` | Valor das combinações correspondente a `list_a`. |
| `unzip_b` | `* 𝌠` | Valor das combinações correspondente a `list_b`. |
| `unzip_c` | `* 𝌠` | Valor das combinações correspondente a `list_c`. |
| `unzip_d` | `* 𝌠` | Valor das combinações correspondente a `list_d`. |
| `index` | `INT 𝌠` | Intervalo de 0..count que pode ser usado como índice. |
| `count` | `INT` | Número total de combinações. |

