## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(Workflow ComfyUI incluído)

Cria uma OutputList extraíndo arrays ou dicionários de objetos JSON.
Usa a sintaxe JSONPath para extrair os valores, veja [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Todos os valores combinados são achatados em uma única lista longa.
Você também pode usar este node para criar objetos a partir de strings literais como `[1, 2, 3]`.
`key`, `value`, `int` e `float` usam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nodes correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath usado para extrair os valores. |
| `json` | `STRING` | Uma string JSON que é traduzida para um objeto. |
| `obj` | `*` | (opcional) objeto de qualquer tipo que substituirá a string JSON |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `key` | `STRING 𝌠` | A chave para dicionários ou índice para arrays (como string). Tecnicamente é um índice global da lista achatada para todos os não-chaves. |
| `value` | `STRING 𝌠` | O valor como string. |
| `int` | `INT 𝌠` | O valor como int (se não conseguir interpretar o número, o padrão é 0). |
| `float` | `FLOAT 𝌠` | O valor como float (se não conseguir interpretar o número, o padrão é 0). |
| `count` | `INT` | Número total de itens na lista achatada |
| `debug` | `STRING` | Saída de depuração de todos os objetos combinados como uma string JSON formatada |

