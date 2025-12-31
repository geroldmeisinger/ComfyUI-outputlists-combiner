## Spreadsheet OutputList

![Spreadsheet OutputList](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow included)

បង្កើត OutputLists ច្រើនពីសេចក្តីសម្រេច (`.csv .tsv .ods .xlsx .xls`)។
អ្នកអាចប្រើ `Load any File` node ដើម្បីផ្ទុយចូលឯកសារដែលមានការកូដ base64។
ដោយផ្ទាល់ប្រើ *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) និង [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) ដើម្បីផ្ទុយចូលឯកសារសេចក្តីសម្រេច។
បញ្ជាក់ទាំងអស់ប្រើ `is_output_list=True` (បានបញ្ជាក់ដោយសញ្ញា `𝌠`) ហើយនឹងត្រូវបានដំណើរការតាមលំដាប់ដោយផ្ទាល់ដោយអ្នកចាប់ផ្តើមនឹងការផ្លាស់ប្ដូរដែលមាន។

### បញ្ចូល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | លេខកូដ និងឈ្មោះនៃជួរ និងជួរឈរនៅក្នុងសេចក្តីសម្រេច។ ចំណាំថានៅក្នុងសេចក្តីសម្រេចជួរចាប់ផ្តើមនៅលេខ 1 ជួរឈរចាប់ផ្តើមនៅ A ដោយសារ OutputLists គឺ 0-based (នៅ `select-nth`)។ |
| `header_rows` | `INT` | មិនចាត់ទុកជួរ x ដំបូងនៅក្នុងបញ្ជាក់។ ត្រូវបានប្រើប្រាស់ប៉ុណ្ណោះប្រសិនបើអ្នកបានបញ្ជាក់ជួរឈរនៅ `rows_and_cols`។ |
| `header_cols` | `INT` | មិនចាត់ទុកជួរឈរ x ដំបូងនៅក្នុងបញ្ជាក់។ ត្រូវបានប្រើប្រាស់ប៉ុណ្ណោះប្រសិនបើអ្នកបានបញ្ជាក់ជួរនៅ `rows_and_cols`។ |
| `select_nth` | `INT` | ត្រូវបានជ្រើសរើសធាតុ nth ប៉ុណ្ណោះ (0-based)។ មានប្រយោជន៍នៅក្នុងការបញ្ជូនជាមួយនឹងល្បឿន `PrimitiveInt+control_after_generate=increment`។ |
| `string_or_base64` | `STRING` | ខ្សែអក្សរ CSV/TSV ឬឯកសារសេចក្តីសម្រេចដែលមានការកូដ base64 (សម្រាប់ `.ods .xlsx .xls`)។ ប្រើ `Load Any File` node ដើម្បីផ្ទុយចូលឯកសារជាកូដ base64។ |

### លទ្ធផល

| ឈ្មោះ | ប្រភេទ | ការពិពណ៌នា |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | ចំនួនធាតុនៅក្នុងបញ្ជាក់ដ៏យូរជាងគេ។ |

