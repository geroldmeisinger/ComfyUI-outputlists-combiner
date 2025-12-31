## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow qo‘shimli)

Spreadsheendlardan (`.csv .tsv .ods .xlsx .xls`) bir nechta OutputList yaratadi.
`Load any File` node dan faylni base64-kodlashda yuklash uchun foydalanishingiz mumkin.
Ichki sifatda *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) va [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) spredsheendlar fayllarini yuklash uchun foydalanadi.
Barcha ro‘yxatlar `is_output_list=True` (belgi `𝌠` bilan ko‘rsatilgan) dan foydalanadi va mos keladigan nodlar tomonidan ketma-ket ishlanadi.

### Kirishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Spreadsheendlardagi qatorlar va ustunlar indekslari va nomlari. Spreadsheendlarda qatorlar 1 dan boshlanadi, ustunlar A dan boshlanadi, lekin OutputListlar 0-qiymatli (u `select-nth` da) bo‘ladi. |
| `header_rows` | `INT` | Ro‘yxatdagi birinchi x qatorlarni e'tiborsiz qoldiring. Faqat `rows_and_cols` da ustunni belgilagan holatda foydalaniladi. |
| `header_cols` | `INT` | Ro‘yxatdagi birinchi x ustunlarni e'tiborsiz qoldiring. Faqat `rows_and_cols` da qatorni belgilagan holatda foydalaniladi. |
| `select_nth` | `INT` | Faqat n-th kirishni tanlang (0-qiymatli). `PrimitiveInt+control_after_generate=increment` pattern bilan foydali. |
| `string_or_base64` | `STRING` | CSV/TSV satr yoki base64 da spredsheendlar fayli (`.ods .xlsx .xls` uchun). Faylni base64 sifatida yuklash uchun `Load Any File` node dan foydalaning. |

### Chiqishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Eng uzun ro‘yxatdagi elementlar soni. |

