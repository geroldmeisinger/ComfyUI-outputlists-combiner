## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkludiert)

Erstellt mehrere OutputLists aus einer Tabelle (`.csv .tsv .ods .xlsx .xls`).
Sie können den `Load any File`-Knoten verwenden, um eine Datei im base64-Format zu laden.
Verwendet intern *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) und [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html), um Tabellendateien zu laden.
Alle Listen verwenden `is_output_list=True` (angezeigt durch das Symbol `𝌠`) und werden sequenziell von den entsprechenden Knoten verarbeitet.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `rows_and_cols` | `ZEICHENKETTE` | Indizes und Namen von Zeilen und Spalten in der Tabelle. Beachten Sie, dass in Tabellen Zeilen bei 1 beginnen, Spalten bei A, während OutputLists 0-basiert sind (in `select-nth`). |
| `header_rows` | `GANZZAHL` | Ignoriert die ersten x Zeilen in der Liste. Nur verwendet, wenn Sie eine Spalte in `rows_and_cols` angeben. |
| `header_cols` | `GANZZAHL` | Ignoriert die ersten x Spalten in der Liste. Nur verwendet, wenn Sie eine Zeile in `rows_and_cols` angeben. |
| `select_nth` | `GANZZAHL` | Nur den nth-Eintrag auswählen (0-basiert). Nützlich in Kombination mit dem Muster `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `ZEICHENKETTE` | CSV/TSV-Zeichenkette oder Tabellendatei im base64-Format (für `.ods .xlsx .xls`). Verwenden Sie den `Load Any File`-Knoten, um eine Datei als base64 zu laden. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `list_a` | `ZEICHENKETTE 𝌠` |  |
| `list_b` | `ZEICHENKETTE 𝌠` |  |
| `list_c` | `ZEICHENKETTE 𝌠` |  |
| `list_d` | `ZEICHENKETTE 𝌠` |  |
| `count` | `GANZZAHL` | Anzahl der Elemente in der längsten Liste. |

