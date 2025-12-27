<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kết hợp các danh sách đầu ra

![Kết hợp các danh sách đầu ra](CombineOutputLists/CombineOutputLists.png)

(bản đồ luồng làm việc của ComfyUI được bao gồm)

Lấy tối đa 4 danh sách đầu ra và tạo ra mọi tổ hợp của chúng.

Ví dụ: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` sử dụng `is_output_list=True` (được chỉ rõ bằng ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các nút tương ứng.

Tất cả các danh sách đều là tùy chọn và các danh sách rỗng sẽ bị bỏ qua.

Cụ thể, nó tính toán *tích Cartes* và đưa ra từng tổ hợp được tách thành các phần tử (`unzip`), trong khi các danh sách rỗng sẽ được thay thế bằng giá trị `None` và sẽ phát hành `None` ở đầu ra tương ứng.

Ví dụ: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Đầu vào

| Tên | Loại | Mô tả |
| --- | --- | --- |
| `list_a` | `*` | (tùy chọn) |
| `list_b` | `*` | (tùy chọn) |
| `list_c` | `*` | (tùy chọn) |
| `list_d` | `*` | (tùy chọn) |

### Đầu ra

| Tên | Loại | Mô tả |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_a`. |
| `unzip_b` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_b`. |
| `unzip_c` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_c`. |
| `unzip_d` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_d`. |
| `index` | `INT 𝌠` | Phạm vi từ 0 đến count có thể dùng làm chỉ số. |
| `count` | `INT` | Tổng số tổ hợp. |

