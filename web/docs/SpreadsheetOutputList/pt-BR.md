## Lista de Saída de Planilha

![Lista de Saída de Planilha](SpreadsheetOutputList/SpreadsheetOutputList.png)

(Workflow do ComfyUI incluído)

Cria múltiplas Listas de Saída a partir de uma planilha (`.csv .tsv .ods .xlsx .xls`).
Você pode usar o nó `Load any File` para carregar um arquivo em codificação base64.
Internamente utiliza o *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) e [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) para carregar arquivos de planilha.
Todas as listas usam(s) `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processadas sequencialmente pelos nós correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Índices e nomes das linhas e colunas na planilha. Note que em planilhas as linhas começam em 1, colunas começam em A, enquanto Listas de Saída são baseadas em 0 (em `select-nth`). |
| `header_rows` | `INT` | Ignorar as primeiras x linhas na lista. Apenas usado se você especificar uma coluna em `rows_and_cols`. |
| `header_cols` | `INT` | Ignorar as primeiras x colunas na lista. Apenas usado se você especificar uma linha em `rows_and_cols`. |
| `select_nth` | `INT` | Apenas selecionar a enésima entrada (baseada em 0). Útil em combinação com o padrão `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | String CSV/TSV ou arquivo de planilha em base64 (para `.ods .xlsx .xls`). Use o nó `Load Any File` para carregar um arquivo como base64. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Número de itens na lista mais longa. |

