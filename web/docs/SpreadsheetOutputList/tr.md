## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow dahildir)

Bir elektronik tablodan (`.csv .tsv .ods .xlsx .xls`) birden fazla OutputList oluşturur.
`Load any File` düğümünü kullanarak bir dosyayı base64 kodlamasıyla yükleyebilirsiniz.
İçeriksel olarak elektronik tablo dosyalarını yüklemek için *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ve [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) fonksiyonlarını kullanır.
Tüm listeler `is_output_list=True` kullanır (sembol `𝌠` ile belirtilir) ve ilgili düğümler tarafından sıralı olarak işlenir.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Elektronik tablodaki satır ve sütun indeksleri ve isimleri. Elektroniktabloların satırlarının 1'den başladığını, sütunların A'dan başladığını ve OutputList'lerin 0 tabanlı olduğunu (örneğin `select-nth` içinde) unutmayın. |
| `header_rows` | `INT` | Liste içindeki ilk x satırı yoksay. Sadece `rows_and_cols` içinde bir sütun belirttiyseniz kullanılır. |
| `header_cols` | `INT` | Liste içindeki ilk x sütunu yoksay. Sadece `rows_and_cols` içinde bir satır belirttiyseniz kullanılır. |
| `select_nth` | `INT` | Sadece nth girdiyi seç (0 tabanlı). `PrimitiveInt+control_after_generate=increment` deseniyle birlikte kullanışlıdır. |
| `string_or_base64` | `STRING` | CSV/TSV dizisi veya base64 formatında elektronik tablo dosyası (`.ods .xlsx .xls` için). Dosyayı base64 olarak yüklemek için `Load Any File` düğümünü kullanın. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | En uzun listedeki öğe sayısı. |

