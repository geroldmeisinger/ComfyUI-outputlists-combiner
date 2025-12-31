## Tổ hợp OutputLists

![Tổ hợp OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow đi kèm)

Lấy tối đa 4 OutputLists và tạo ra tất cả các tổ hợp của chúng.

Ví dụ: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` sử dụng `is_output_list=True` (được chỉ thị bởi ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các node tương ứng.

Tất cả các danh sách đều là tùy chọn và các danh sách rỗng sẽ bị bỏ qua.

Về mặt kỹ thuật, nó tính *tích Descartes* và đầu ra mỗi tổ hợp được chia nhỏ thành các phần tử của chúng (`unzip`), trong khi các danh sách rỗng sẽ được thay thế bằng đơn vị `None` và chúng sẽ phát ra `None` trên đầu ra tương ứng.

Ví dụ: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `list_a` | `*` | (tùy chọn) |
| `list_b` | `*` | (tùy chọn) |
| `list_c` | `*` | (tùy chọn) |
| `list_d` | `*` | (tùy chọn) |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_a`. |
| `unzip_b` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_b`. |
| `unzip_c` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_c`. |
| `unzip_d` | `* 𝌠` | Giá trị của các tổ hợp tương ứng với `list_d`. |
| `index` | `INT 𝌠` | Phạm vi từ 0..count có thể được sử dụng như một chỉ số. |
| `count` | `INT` | Tổng số tổ hợp. |

