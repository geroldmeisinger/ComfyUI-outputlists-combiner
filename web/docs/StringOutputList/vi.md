## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow đi kèm)

Tạo một OutputList bằng cách chia chuỗi trong ô văn bản bằng một ký tự phân tách.
`value` và `index` sử dụng `is_output_list=True` (được chỉ thị bởi ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các node tương ứng.

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `separator` | `STRING` | Chuỗi được sử dụng để chia các giá trị trong ô văn bản. |
| `values` | `STRING` | Văn bản bạn muốn chia thành một danh sách. Lưu ý rằng chuỗi sẽ bị loại bỏ các ký tự xuống dòng ở cuối trước khi chia, và mỗi phần tử lại bị loại bỏ khoảng trắng ở đầu và cuối. |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `value` | `* 𝌠` | Các giá trị từ danh sách. |
| `index` | `INT 𝌠` | Phạm vi từ 0..count. Bạn có thể sử dụng điều này như một chỉ số. |
| `count` | `INT` | Số lượng phần tử trong danh sách. |
| `inspect_combo` | `COMBO` | Một đầu ra giả bạn có thể sử dụng để kết nối với một `COMBO` và điền sẵn với các giá trị của nó. Kết nối sẽ sau đó được tự động kết nối lại với đầu ra `value`. |

