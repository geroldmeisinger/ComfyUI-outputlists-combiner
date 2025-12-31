## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow được bao gồm)

Tạo một OutputList với một dãy giá trị số.
Sử dụng [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) bên trong, bởi vì nó hoạt động đáng tin cậy hơn với các giá trị dấu chấm động.
Nếu bạn muốn định nghĩa danh sách số với bước tùy ý, hãy kiểm tra JSON OutputList và định nghĩa một mảng, ví dụ `[1, 42, 123]`.
`int`, `float`, `string` và `index` sử dụng `is_output_list=True` (được chỉ thị bởi ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các node tương ứng.

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `start` | `FLOAT` | Giá trị bắt đầu để tạo dãy số. |
| `stop` | `FLOAT` | Giá trị kết thúc. Nếu `endpoint=include` thì số này sẽ được bao gồm trong danh sách. |
| `num` | `INT` | Số lượng phần tử trong danh sách (đừng nhầm lẫn với `step`). |
| `endpoint` | `BOOLEAN` | Quyết định xem giá trị `stop` có nên được bao gồm hay loại bỏ trong các phần tử. |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `int` | `INT 𝌠` | Giá trị được chuyển đổi sang int (làm tròn xuống/được làm tròn). |
| `float` | `FLOAT 𝌠` | Giá trị dưới dạng float. |
| `string` | `STRING 𝌠` | Giá trị dưới dạng float được chuyển đổi sang chuỗi. |
| `index` | `INT 𝌠` | Phạm vi từ 0..count có thể được sử dụng làm chỉ mục. |
| `count` | `INT` | Giống như `num`. |

