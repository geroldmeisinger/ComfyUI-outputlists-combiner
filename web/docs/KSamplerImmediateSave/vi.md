## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow đi kèm)

Mở rộng node mặc định `CheckpointLoader`, `KSampler`, `VAE Decode` và `Save Image` để xử lý như một quá trình duy nhất.
Điều này hữu ích nếu bạn muốn lưu các hình ảnh trung gian cho lưới ngay lập tức.

*"Một KSampler tùy chỉnh chỉ để lưu một hình ảnh? Giờ tôi đã trở thành thứ mà tôi từng tìm cách tiêu diệt!"*

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Tên của checkpoint (model) để tải. |
| `positive` | `STRING` | Điều kiện mô tả các thuộc tính bạn muốn bao gồm trong hình ảnh. |
| `negative` | `STRING` | Điều kiện mô tả các thuộc tính bạn muốn loại trừ khỏi hình ảnh. |
| `latent_image` | `LATENT` | Hình ảnh latent để khử nhiễu. |
| `seed` | `INT` | Giá trị seed ngẫu nhiên được sử dụng để tạo nhiễu. |
| `steps` | `INT` | Số bước được sử dụng trong quá trình khử nhiễu. |
| `cfg` | `FLOAT` | Tỷ lệ Classifier-Free Guidance cân bằng giữa sự sáng tạo và tuân thủ prompt. Giá trị cao hơn sẽ tạo ra hình ảnh gần với prompt hơn, tuy nhiên giá trị quá cao sẽ ảnh hưởng tiêu cực đến chất lượng. |
| `sampler_name` | `COMBO` | Thuật toán được sử dụng khi lấy mẫu, điều này có thể ảnh hưởng đến chất lượng, tốc độ và phong cách của đầu ra được tạo. |
| `scheduler` | `COMBO` | Bộ lập lịch kiểm soát cách nhiễu được loại bỏ dần dần để tạo hình ảnh. |
| `denoise` | `FLOAT` | Mức độ khử nhiễu được áp dụng, giá trị thấp hơn sẽ giữ cấu trúc của hình ảnh ban đầu, cho phép lấy mẫu từ hình ảnh này sang hình ảnh khác. |
| `filename_prefix` | `STRING` | Tiền tố cho tệp để lưu. Có thể bao gồm thông tin định dạng như %date:yyyy-MM-dd% hoặc %Empty Latent Image.width% để bao gồm các giá trị từ node. |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `image` | `IMAGE` | Hình ảnh đã được giải mã. |

