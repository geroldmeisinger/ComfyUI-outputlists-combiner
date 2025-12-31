## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow daxildədir)

Hesab cədvəli (`.csv .tsv .ods .xlsx .xls`) ilə bir neçə OutputList yaradır.
`Load any File` node-ni base64-kodlaşdırma ilə fayl yükləmək üçün istifadə edə bilərsiniz.
Daxili olaraq *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) və [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) hesab cədvəli fayllarını yükləmək üçün istifadə edir.
Bütün siyahılar `is_output_list=True` istifadə edir (simvol `𝌠` ilə göstərilir) və相应 node-lar tərəfindən ardıcıl olaraq işlənəcək.

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Hesab cədvəlinin sətirlər və sütunların indeksləri və adları. Qeyd edin ki, hesab cədvəllərində sətirlər 1-dən başlayır, sütunlar A-dan başlayır, amma OutputList-lər 0-ə əsaslanır (`select-nth`-də). |
| `header_rows` | `INT` | Siyahıda ilk x sətiri nəzərə alma. Yalnız `rows_and_cols`-da sütun təyin etmisinizsə istifadə olunur. |
| `header_cols` | `INT` | Siyahıda ilk x sütununu nəzərə alma. Yalnız `rows_and_cols`-da sətir təyin etmisinizsə istifadə olunur. |
| `select_nth` | `INT` | Yalnız nth daxil etməni seç (0-ə əsaslanır). `PrimitiveInt+control_after_generate=increment` pattern ilə birləşdirmək üçün faydalıdır. |
| `string_or_base64` | `STRING` | CSV/TSV sətri və ya hesab cədvəli faylı base64-də (`.ods .xlsx .xls` üçün). Faylı base64 kimi yükləmək üçün `Load Any File` node-ni istifadə edin. |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Ən uzun siyahıdakı element sayı. |

