## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow incluído)

Crea múltiples OutputLists dende unha folla de cálculo (`.csv .tsv .ods .xlsx .xls`).
Pode usar o nodo `Load any File` para cargar un ficheiro en codificación base64.
Internamente usa *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) e [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) para cargar ficheiros de follas de cálculo.
Todas as listas usan `is_output_list=True` (indicado polo símbolo `𝌠`) e serán procesadas secuencialmente por nodos correspondentes.

### Entradas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Índices e nomes de filas e columnas na folla de cálculo. Teña en conta que nas follas de cálculo as filas comezan en 1, as columnas comezan en A, mentres que OutputLists son base 0 (en `select-nth`). |
| `header_rows` | `INT` | Ignorar as primeiras x filas na lista. Só se usa se especifica unha columna en `rows_and_cols`. |
| `header_cols` | `INT` | Ignorar as primeiras x columnas na lista. Só se usa se especifica unha fila en `rows_and_cols`. |
| `select_nth` | `INT` | Só seleccionar a entrada n-ésima (base 0). Útil en combinación co patrón `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Cadena CSV/TSV ou ficheiro de folla de cálculo en base64 (para `.ods .xlsx .xls`). Use o nodo `Load Any File` para cargar un ficheiro como base64. |

### Saídas

| Nome | Tipo | Descrición |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Número de elementos na lista máis longa. |

