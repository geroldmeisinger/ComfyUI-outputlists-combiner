## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow imejengwa)

Inaunda OutputLists nyingi kutoka kwa hifadhi ya data (`.csv .tsv .ods .xlsx .xls`).
Unaweza kutumia kifaa `Load any File` ili kuleta faili kwa njia ya base64-encoding.
Nje inatumia *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) na [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) ili kuleta faili za hifadhi ya data.
Vidhibiti vyote vinatumia `is_output_list=True` (iliyoelezwa kwa alama `𝌠`) na vitatumiwa kwa kufuatana na kifaa kulingana.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Vijiji na majina ya safu na sambamba katika hifadhi ya data. Kumbuka kuwa katika hifadhi za data safu zinaanza kutoka 1, sambamba zinaanza kutoka A, wakati OutputLists zinaanza kutoka 0 (katika `select-nth`). |
| `header_rows` | `INT` | Pasua safu ya kwanza x katika orodha. Inatumika tu ikiwa unakubaliana na sambamba katika `rows_and_cols`. |
| `header_cols` | `INT` | Pasua sambamba ya kwanza x katika orodha. Inatumika tu ikiwa unakubaliana na safu katika `rows_and_cols`. |
| `select_nth` | `INT` | Chagua kwa kufuata kipengele cha nth (0-based). Inapatikana kwa kufuatana na `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | String ya CSV/TSV au faili ya hifadhi ya data kwa base64 (kwa `.ods .xlsx .xls`). Tumia kifaa `Load Any File` ili kuleta faili kama base64. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Idadi ya vitu katika orodha inayozidi. |

