## Lista de sortida de fuèlha de calcul

![Lista de sortida de fuèlha de calcul](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow incluch)

Crea multas listas de sortida a partir d'una fuèlha de calcul (`.csv .tsv .ods .xlsx .xls`).
Podètz utilizar lo node `Load any File` per cargar un fichièr en format base64.
A nivèl intern, utiliza *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) e [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) per cargar los fichièrs de fuèlha de calcul.
Totas las listas utilizan `is_output_list=True` (indicat per lo simbòl `𝌠`) e seràn tractadas seqüencialament per los nodes correspondents.

### Entradas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indicis e noms de las linhas e colomnas de la fuèlha de calcul. Notatz que las linhas començan a 1 e las colomnas a A dins las fuèlhas de calcul, e que las listas de sortida son 0-basadas (dins `select-nth`). |
| `header_rows` | `INT` | Omet las primièras x linhas de la lista. Utilizat sol se especificatz una colomna dins `rows_and_cols`. |
| `header_cols` | `INT` | Omet las primièras x colomnas de la lista. Utilizat sol se especificatz una linha dins `rows_and_cols`. |
| `select_nth` | `INT` | Selecciona sol l'entrada n-èna (0-basada). Util a combinacion amb lo patron `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Cadena CSV/TSV o fichièr de fuèlha de calcul en base64 (per `.ods .xlsx .xls`). Utilizatz lo node `Load Any File` per cargar un fichièr coma base64. |

### Sortidas

| Nom | Tipe | Descripcion |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Nombre d'elements de la lista mai longa. |

