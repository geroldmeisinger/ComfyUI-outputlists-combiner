## Tải Tập Tin Bất Kỳ

![Tải Tập Tin Bất Kỳ](LoadAnyFile/LoadAnyFile.png)

(Workflows ComfyUI đi kèm)

Tải bất kỳ tệp văn bản hay nhị phân nào và cung cấp nội dung tệp dưới dạng chuỗi hoặc chuỗi base64. Ngoài ra còn cố gắng tải tệp dưới dạng `IMAGE`. Cũng cố gắng tải metadata của tệp.

`filepath` hỗ trợ các đường dẫn tệp được chú thích của ComfyUI `[input]` `[output]` hoặc `[temp]`.
`filepath` cũng hỗ trợ mở rộng mẫu glob `subdir/**/*.png`.
Bên trong sử dụng [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) của Python.

`metadata` gọi `exiftool`, nếu nó được cài đặt và có sẵn tại `PATH`, nếu không sẽ sử dụng `PIL.Image.info` như phương án dự phòng.

Do lý do bảo mật, chỉ hỗ trợ các thư mục sau: `[input] [output] [temp]`.
Do lý do hiệu năng, số lượng tệp bị giới hạn ở: 1024.

### Đầu Vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `filepath` | `STRING` | Thư mục gốc mặc định là thư mục người dùng `[input]`. Hỗ trợ mở rộng mẫu glob `subdir/**/*.png`. Sử dụng hậu tố ` [input]` ` [output]` hoặc ` [temp]` (lưu ý khoảng trắng đầu!) để chỉ định thư mục người dùng ComfyUI khác. |

### Đầu Ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Nội dung tệp cho tệp văn bản, base64 cho tệp nhị phân. |
| `image` | `IMAGE 𝌠` | Tensor batch hình ảnh. |
| `mask` | `MASK 𝌠` | Tensor batch mask. |
| `metadata` | `STRING 𝌠` | Dữ liệu Exif từ ExifTool. Yêu cầu lệnh `exiftool` phải có sẵn trong `PATH`. |

