## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

Fà sa creare de s’OutputList mìltiples dae unu de spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Podet impreare su nodu `Load any File` pro ischire unu archìviu in codìfica base64.
A s’impreat in manera interna *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) e [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) pro ischire archìvios de spreadsheet.
Tutus s’elencus impread s’`is_output_list=True` (indikadu dae su sìmbolu `𝌠`) e ant a èssere traballadus in manera secuenziale dae nodos corrisponentes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Inditzi e nàmines de rìngidas e colùmnidas in su spreadsheet. Nota chi in spreadsheet rìngidas cumintzant a 1, colùmnidas a A, mancari s’OutputList sunt a contare dae 0 (in `select-nth`). |
| `header_rows` | `INT` | Ignorare sas primas x rìngidas in s’elencu. Impreada isceti si specificas una colùmna in `rows_and_cols`. |
| `header_cols` | `INT` | Ignorare sas primas x colùmnidas in s’elencu. Impreada isceti si specificas una rìngida in `rows_and_cols`. |
| `select_nth` | `INT` | Seletzionare isceti s’entrada n-ta (a contà dae 0). È beru in combinatzione cun su pattern `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Càrriga CSV/TSV o archìviu de spreadsheet in base64 (pro `.ods .xlsx .xls`). Imprea su nodu `Load Any File` pro ischire unu archìviu comente base64. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Nùmeru de elementos in s’elencu prus longu. |

