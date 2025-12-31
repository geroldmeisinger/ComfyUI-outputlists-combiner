## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow inkluddat)

Jiġġenera bosta OutputLists minn spreadsheet (`.csv .tsv .ods .xlsx .xls`).
Tista’ tuża l-`Load any File` node biex tiġġ load fajl bbażat fuq base64-encoding.
Bħall-internu jgħandu *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) u [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) biex jiġġeneraw fajls tal-spreadsheet.
Kollha listi jgħandu(s) `is_output_list=True` (indikat bil-simbolu `𝌠`) u jiġġeneraw sekwenzjali minn nodi korrispondenti.

### Inputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Indiċi u ismijiet tar-riwoli u kolonni fis-spreadsheet. Iż-żgħaża li fir-spreadsheet r-riwoli jibdlu minn 1, il-kolonni jibdlu minn A, imma OutputLists jkunu 0-based (fi `select-nth`). |
| `header_rows` | `INT` | Ignorax ir-riwoli ewlenin x fil-lista. Imkun biżżejjed jekk tippreżenta kolonna fi `rows_and_cols`. |
| `header_cols` | `INT` | Ignorax il-kolonni ewlenin x fil-lista. Imkun biżżejjed jekk tippreżenta r-riwol fi `rows_and_cols`. |
| `select_nth` | `INT` | Iżżom il-ħaġar ta’ n-ħaġar (0-based). Utili bil-kombinazzjoni ma’ `PrimitiveInt+control_after_generate=increment` pattern. |
| `string_or_base64` | `STRING` | String CSV/TSV jew fajl spreadsheet bbażat fuq base64 (għal `.ods .xlsx .xls`). Uża l-`Load Any File` node biex tiġġ load fajl bbażat fuq base64. |

### Outputs

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Numru ta’ oġġetti fl-aktar lista. |

