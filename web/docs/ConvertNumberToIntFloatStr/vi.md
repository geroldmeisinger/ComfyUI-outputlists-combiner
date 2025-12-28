<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Chuyển sang số nguyên, số thực, chuỗi

![Chuyển sang số nguyên, số thực, chuỗi](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Bao gồm workflow của ComfyUI)

Chuyển mọi thứ có dạng số thành `INT`, `FLOAT`, `STRING`.
Sử dụng `nums_from_string.get_nums` bên trong, chức năng này rất linh hoạt khi nhận diện các số, chấp nhận cả số nguyên thực, số thực, số nguyên hoặc số thực dưới dạng chuỗi, các chuỗi chứa nhiều số có dấu phân cách ngàn.
Sử dụng chuỗi `123;234;345` để nhanh chóng tạo ra danh sách các số. Không nên dùng dấu phẩy làm dấu phân cách vì chúng có thể bị hiểu là dấu phân cách ngàn.
Các loại `int`, `float` và `string` sử dụng `is_output_list=True` (được chỉ định bằng ký hiệu `𝌠`) và sẽ được xử lý tuần tự bởi các nút tương ứng.

### Đầu vào

| Tên | Loại | Mô tả |
| --- | --- | --- |
| `any` | `*` | Mọi thứ có thể được chuyển thành chuỗi có chứa các số có thể đọc được |

### Đầu ra

| Tên | Loại | Mô tả |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tất cả các số được tìm thấy trong chuỗi, phần thập phân bị loại bỏ. |
| `float` | `FLOAT 𝌠` | Tất cả các số được tìm thấy trong chuỗi dưới dạng số thực. |
| `string` | `STRING 𝌠` | Tất cả các số được tìm thấy trong chuỗi dưới dạng số thực chuyển thành chuỗi. |
| `count` | `INT` | Số lượng số được tìm thấy trong giá trị. |

