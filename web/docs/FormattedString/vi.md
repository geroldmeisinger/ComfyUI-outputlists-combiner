## Chuỗi Định Dạng

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow được bao gồm)

Tạo một chuỗi chứa các biến giữ chỗ và thay thế chúng bằng các giá trị tương ứng.
Sử dụng `str.format()` của Python bên trong, xem [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Bạn có thể sử dụng `{a:.2f}` để làm tròn số float đến 2 chữ số thập phân.
* Bạn có thể sử dụng `{a:05d}` để thêm đến 5 số 0 ở đầu để phù hợp với hậu tố tên file của Comfy `ComfyUI_00001_.png`.
* Nếu bạn muốn viết `{ }` trong chuỗi của mình (ví dụ như JSONs), bạn phải viết đôi: `{{ }}`.

Cũng áp dụng cú pháp *tìm kiếm và thay thế (S&R)* như `%date:yyyy-MM-dd hh:mm:ss%` và `%KSampler.seed%`.
Do đó bạn cũng có thể sử dụng nó như một `GET-node`.
Lưu ý rằng "tìm kiếm và thay thế" diễn ra trong ngữ cảnh Javascript và chạy trước khi thực thi node.

### Đầu Vào

| Tên | Kiểu | Mô Tả |
| --- | --- | --- |
| `fstring` | `STRING` | Tạo một chuỗi chứa các biến giữ chỗ và thay thế chúng bằng các giá trị tương ứng.<br>Sử dụng `str.format()` của Python bên trong, xem [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Bạn có thể sử dụng `{a:.2f}` để làm tròn số float đến 2 chữ số thập phân.<br>* Bạn có thể sử dụng `{a:05d}` để thêm đến 5 số 0 ở đầu để phù hợp với hậu tố tên file của Comfy `ComfyUI_00001_.png`.<br>* Nếu bạn muốn viết `{ }` trong chuỗi của mình (ví dụ như JSONs), bạn phải viết đôi: `{{ }}`.<br><br>Cũng áp dụng cú pháp *tìm kiếm và thay thế (S&R)* như `%date:yyyy-MM-dd hh:mm:ss%` và `%KSampler.seed%`.<br>Do đó bạn cũng có thể sử dụng nó như một `GET-node`.<br>Lưu ý rằng "tìm kiếm và thay thế" diễn ra trong ngữ cảnh Javascript và chạy trước khi thực thi node. |
| `a` | `*` | (tùy chọn) giá trị sẽ được chuyển thành chuỗi tại vị trí `{a}`. |
| `b` | `*` | (tùy chọn) giá trị sẽ được chuyển thành chuỗi tại vị trí `{b}`. |
| `c` | `*` | (tùy chọn) giá trị sẽ được chuyển thành chuỗi tại vị trí `{c}`. |
| `d` | `*` | (tùy chọn) giá trị sẽ được chuyển thành chuỗi tại vị trí `{d}`. |

### Đầu Ra

| Tên | Kiểu | Mô Tả |
| --- | --- | --- |
| `string` | `STRING` | Chuỗi đã được định dạng với tất cả các vị trí giữ chỗ đã được thay thế bằng các giá trị tương ứng. |

