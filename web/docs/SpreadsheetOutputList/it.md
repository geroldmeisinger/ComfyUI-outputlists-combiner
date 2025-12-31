## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow incluso)

Crea più OutputList da un foglio di lavoro (`.csv .tsv .ods .xlsx .xls`).
Puoi usare il nodo `Load any File` per caricare un file in codifica base64.
Internamente utilizza *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) e [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) per caricare file di fogli di lavoro.
Tutte le liste usano `is_output_list=True` (indicato dal simbolo `𝌠`) e saranno elaborate sequenzialmente dai nodi corrispondenti.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `rows_and_cols` | `STRINGA` | Indici e nomi di righe e colonne nel foglio di lavoro. Nota che nei fogli di lavoro le righe iniziano da 1, le colonne da A, mentre gli OutputList sono basati su 0 (in `select-nth`). |
| `header_rows` | `INTERO` | Ignora le prime x righe nella lista. Usato solo se specifichi una colonna in `rows_and_cols`. |
| `header_cols` | `INTERO` | Ignora le prime x colonne nella lista. Usato solo se specifichi una riga in `rows_and_cols`. |
| `select_nth` | `INTERO` | Seleziona solo la voce n-esima (basata su 0). Utile in combinazione con il pattern `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRINGA` | Stringa CSV/TSV o file di foglio di lavoro in base64 (per `.ods .xlsx .xls`). Usa il nodo `Load Any File` per caricare un file come base64. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `list_a` | `STRINGA 𝌠` |  |
| `list_b` | `STRINGA 𝌠` |  |
| `list_c` | `STRINGA 𝌠` |  |
| `list_d` | `STRINGA 𝌠` |  |
| `count` | `INTERO` | Numero di elementi nella lista più lunga. |

