## OutputList Bảng tính

![OutputList Bảng tính](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI workflow đi kèm)

Tạo nhiều OutputLists từ một bảng tính (`.csv .tsv .ods .xlsx .xls`).
Bạn có thể sử dụng node `Load any File` để tải tệp dưới dạng base64-encoding.
Bên trong sử dụng *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) và [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) để tải tệp bảng tính.
Tất cả các danh sách đều sử dụng `is_output_list=True` (được chỉ thị bởi ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các node tương ứng.

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `rows_and_cols` | `STRING` | Chỉ số và tên của hàng và cột trong bảng tính. Lưu ý rằng trong bảng tính hàng bắt đầu từ 1, cột bắt đầu từ A, trong khi OutputLists là 0-based (trong `select-nth`). |
| `header_rows` | `INT` | Bỏ qua x hàng đầu tiên trong danh sách. Chỉ được sử dụng nếu bạn chỉ định một cột trong `rows_and_cols`. |
| `header_cols` | `INT` | Bỏ qua x cột đầu tiên trong danh sách. Chỉ được sử dụng nếu bạn chỉ định một hàng trong `rows_and_cols`. |
| `select_nth` | `INT` | Chỉ chọn mục thứ n (dựa trên 0). Hữu ích khi kết hợp với mẫu `PrimitiveInt+control_after_generate=increment`. |
| `string_or_base64` | `STRING` | Chuỗi CSV/TSV hoặc tệp bảng tính ở dạng base64 (cho `.ods .xlsx .xls`). Sử dụng node `Load Any File` để tải tệp dưới dạng base64. |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `list_a` | `STRING 𝌠` |  |
| `list_b` | `STRING 𝌠` |  |
| `list_c` | `STRING 𝌠` |  |
| `list_d` | `STRING 𝌠` |  |
| `count` | `INT` | Số lượng mục trong danh sách dài nhất. |

