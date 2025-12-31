## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(Workflow ComfyUI incluído)

Cria uma OutputList dividindo a string no campo de texto com um separador.
`value` e `index` usam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nós correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `separator` | `STRING` | A string usada para dividir os valores do campo de texto. |
| `values` | `STRING` | O texto que você deseja dividir em uma lista. Note que a string é removida de novas linhas à direita antes de dividir, e cada item é novamente removido de espaços em branco. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `value` | `* 𝌠` | Os valores da lista. |
| `index` | `INT 𝌠` | Faixa de 0..count. Você pode usar isso como um índice. |
| `count` | `INT` | O número de itens na lista. |
| `inspect_combo` | `COMBO` | Uma saída fictícia que você pode usar para vincular a um `COMBO` e preencher com seus valores. A conexão será então automaticamente revinculada à saída `value`. |

