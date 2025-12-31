## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI vinnusvæði included)

Býr til mörg OutputList úr töflureikningi (`.csv .tsv .ods .xlsx .xls`).
Þú getur notað `Load any File` node til að hlaða inn skrá sem base64-kóðuð.
Innri notar *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) og [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) til að hlaða inn töflureikningaskránum.
Allir listarnir notar `is_output_list=True` (sýnt með tákninu `𝌠`) og verður þá meðhöndlað síðan af samsvarandi node.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Tölvur og nöfn fyrir raðir og dálka í töflureikningnum. Athugaðu að í töflureikningum byrja raðir á 1, dálkar byrja á A, en OutputList eru 0-baðir (í `select-nth`). |
| `header_rows` | `INT` | Hunsa fyrstu x raðir í listanum. Aðeins notast við ef þú tilgreinir dálk í `rows_and_cols`. |
| `header_cols` | `INT` | Hunsa fyrstu x dálka í listanum. Aðeins notast við ef þú tilgreinir rað í `rows_and_cols`. |
| `select_nth` | `INT` | Velur aðeins nth atriði (0-baði). Gagnlegt í samsetningu með `PrimitiveInt+control_after_generate=increment` mynstri. |
| `string_or_base64` | `STRING` | CSV/TSV strengur eða töflureikningsskrá sem base64 (fyrir `.ods .xlsx .xls`). Nota `Load Any File` node til að hlaða inn skrá sem base64. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Fjöldi atriða í lengsta listanum. |

