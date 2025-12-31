## Spreadsheets OutputList

![Spreadsheets OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow íðgu)

Gerir fleiri OutputLists frá einni spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Tú kanst nýta `Load any File` node til at henda einn fílu í base64-koding.
Innanlandsum nýtir *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) og [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) til at henda spreadsheet fílur.
Allir listir nýtir `is_output_list=True` (merkt við symbolið `𝌠`) og verða handtert í fylgjandi rætta av samsvarandi nodes.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indikar og navn á røðum og dálkum í spreadsheet. Tíðan í spreadsheets røður byrja á 1, dálkar byrja á A, tá er OutputLists 0-baserað (í `select-nth`). |
| `header_rows` | `INT` | Overskrítt fyrstu x røðum í lista. Einans brúkt um tú tilkenda einn dálk í `rows_and_cols`. |
| `header_cols` | `INT` | Overskrítt fyrstu x dálkum í lista. Einans brúkt um tú tilkenda einn røð í `rows_and_cols`. |
| `select_nth` | `INT` | Vel einn nth entry (0-baserað). Nýtist í sambandi við `PrimitiveInt+control_after_generate=increment` mønster. |
| `string_or_base64` | `STRING` | CSV/TSV streng ella spreadsheet fíla í base64 (fyri `.ods .xlsx .xls`). Nýt `Load Any File` node til at henda einn fílu sum base64. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Tal av itemum í lengsta lista. |

