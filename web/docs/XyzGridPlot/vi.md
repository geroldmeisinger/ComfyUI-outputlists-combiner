## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow đi kèm)

Tạo một XYZ-Gridplot từ danh sách các hình ảnh.
Nó lấy một danh sách hình ảnh (bao gồm các batch) và làm phẳng chúng thành một danh sách dài trước tiên (do đó `batch_size=1`).

**Hình dạng lưới**
Xác định hình dạng của lưới bằng:
1. số lượng nhãn hàng
2. số lượng nhãn cột
3. số lượng hình ảnh con còn lại.
Bạn có thể sử dụng `order=inside_out` để đảo ngược việc chọn hình ảnh (hữu ích nếu `batch_size>1` và bạn muốn gắn nhãn cho các batch).

**Căn chỉnh**
* Nếu một nhãn bị ngắt dòng sang dòng tiếp theo thì toàn bộ trục được coi là "đa dòng" và căn chỉnh chúng ở trên với khoảng cách đều.
* Nếu tất cả các nhãn đều là số hoặc kết thúc bằng số (ví dụ: `strength: 1.`) thì toàn bộ trục được coi là "số" và căn chỉnh chúng sang phải.
* Tất cả các văn bản khác được coi là "đơn dòng" và căn chỉnh chúng ở giữa.
* Căn chỉnh nhãn đơn dòng và số cho các cột ở dưới, và cho các hàng căn chỉnh dọc ở giữa.

**Cỡ chữ**
* Chiều cao của khu vực nhãn cột được xác định bởi `font_size` hoặc `nửa chiều cao đóng gói hình ảnh con lớn nhất trong bất kỳ hàng nào` (cái nào lớn hơn).
* Chiều rộng của khu vực nhãn hàng được xác định bởi chiều rộng lớn nhất của việc đóng gói hình ảnh con (với tối thiểu là 256px).
* Văn bản sẽ được thu nhỏ cho đến khi vừa vặn (xuống đến `font_size_min=6`) và sử dụng cùng một cỡ chữ cho toàn bộ trục (nhãn hàng hoặc nhãn cột).
Nếu cỡ chữ đã đạt mức tối thiểu, thì sẽ cắt bỏ văn bản còn lại.

**Đóng gói hình ảnh con**
Hình dạng các hình ảnh con (thường từ các batch) thành khu vực vuông nhất (được gọi là "đóng gói hình ảnh con"), trừ khi `output_is_list=True`, trong trường hợp này chỉ sử dụng một hình ảnh cho mỗi ô và tạo danh sách các lưới hình ảnh toàn bộ thay thế.
Bạn có thể sử dụng danh sách các lưới hình ảnh này để kết nối với một nút XyzGridPlot khác để tạo siêu lưới.
Nếu hình ảnh con gồm các batch có kích thước khác nhau, sẽ điền vào các ô thiếu bằng hình ảnh trống.
Số lượng hình ảnh mỗi ô (bao gồm hình ảnh batch) phải là bội số của `rows * columns`.

### Đầu vào

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `images` | `IMAGE` | Danh sách hình ảnh (bao gồm các batch) |
| `row_labels` | `*` | Văn bản nhãn hàng ở bên trái |
| `col_labels` | `*` | Văn bản nhãn cột ở phía trên |
| `gap` | `INT` | Khoảng cách giữa các đóng gói hình ảnh con. Lưu ý rằng bên trong các hình ảnh con không có khoảng cách. Nếu bạn muốn khoảng cách giữa các hình ảnh con thì kết nối thêm một nút XyzGridPlot khác. |
| `font_size` | `FLOAT` | Cỡ chữ mục tiêu. Văn bản sẽ bị thu nhỏ cho đến khi vừa vặn (xuống đến `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Hướng văn bản của nhãn hàng. Hữu ích nếu bạn muốn tiết kiệm không gian. |
| `order` | `BOOLEAN` | Xác định thứ tự xử lý hình ảnh. Điều này chỉ có ý nghĩa nếu bạn có hình ảnh con. Hữu ích nếu `batch_size>1` và bạn muốn vẽ các batch. |
| `output_is_list` | `BOOLEAN` | Điều này chỉ có ý nghĩa nếu bạn có hình ảnh con hoặc muốn tạo siêu lưới. |

### Đầu ra

| Tên | Kiểu | Mô tả |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Hình ảnh XYZ-GridPlot. Nếu `output_is_list=True` sẽ tạo danh sách hình ảnh mà bạn có thể kết nối với một nút XYZ-GridPlot khác để tạo siêu lưới. |

