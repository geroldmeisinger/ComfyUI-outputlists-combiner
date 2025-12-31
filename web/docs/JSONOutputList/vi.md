## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow được bao gồm)

Tạo một OutputList bằng cách trích xuất các mảng hoặc từ điển từ các đối tượng JSON.
Sử dụng cú pháp JSONPath để trích xuất các giá trị, xem [JSONPath trên Wikipedia](https://en.wikipedia.org/wiki/JSONPath).
Tất cả các giá trị phù hợp đều được làm phẳng thành một danh sách dài.
Bạn cũng có thể sử dụng node này để tạo các đối tượng từ các chuỗi ký tự như `[1, 2, 3]`.
`key`, `value`, `int` và `float` sử dụng `is_output_list=True` (được chỉ thị bởi ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các node tương ứng.

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath được sử dụng để trích xuất các giá trị. |
| `json` | `STRING` | Chuỗi JSON được chuyển đổi thành một đối tượng. |
| `obj` | `*` | (tùy chọn) đối tượng bất kỳ nào sẽ thay thế chuỗi JSON |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Khóa cho từ điển hoặc chỉ mục cho mảng (dưới dạng chuỗi). Về mặt kỹ thuật, đây là chỉ mục toàn cục của danh sách đã làm phẳng cho tất cả các không phải khóa. |
| `value` | `STRING 𝌠` | Giá trị dưới dạng chuỗi. |
| `int` | `INT 𝌠` | Giá trị dưới dạng số nguyên (nếu không thể phân tích số, mặc định là 0). |
| `float` | `FLOAT 𝌠` | Giá trị dưới dạng số thực (nếu không thể phân tích số, mặc định là 0). |
| `count` | `INT` | Tổng số mục trong danh sách đã làm phẳng |
| `debug` | `STRING` | Đầu ra debug của tất cả các đối tượng phù hợp dưới dạng chuỗi JSON được định dạng |

