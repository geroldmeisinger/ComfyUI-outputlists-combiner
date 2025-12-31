## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow incluido)

Crea múltiples OutputLists a partir de una hoja de cálculo (`.csv .tsv .ods .xlsx .xls`).
Puede usar el nodo `Load any File` para cargar un archivo en codificación base64.
Internamente utiliza *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) y [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) para cargar archivos de hojas de cálculo.
Todas las listas usan `is_output_list=True` (indicado por el símbolo `𝌠`) y serán procesadas secuencialmente por los nodos correspondientes.

### Entradas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Índices y nombres de filas y columnas en la hoja de cálculo. Tenga en cuenta que en las hojas de cálculo las filas comienzan en 1, las columnas comienzan en A, mientras que las OutputLists son basadas en 0 (en `select-nth`). |
| `header_rows` | `INT` | Ignora las primeras x filas en la lista. Solo se usa si especifica una columna en `rows_and_cols`. |
| `header_cols` | `INT` | Ignora las primeras x columnas en la lista. Solo se usa si especifica una fila en `rows_and_cols`. |
| `select_nth` | `INT` | Solo selecciona la entrada nth (basada en 0). Útil en combinación con el patrón `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Cadena CSV/TSV o archivo de hoja de cálculo en base64 (para `.ods .xlsx .xls`). Use el nodo `Load Any File` para cargar un archivo como base64. |

### Salidas

| Nombre | Tipo | Descripción |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Número de elementos en la lista más larga. |

