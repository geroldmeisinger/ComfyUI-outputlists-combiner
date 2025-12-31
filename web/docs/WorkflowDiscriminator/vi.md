## Bộ Phân Loại Workflows

![Bộ Phân Loại Workflows](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI workflow đi kèm)

So sánh các workflows và phân loại chúng để trích xuất các giá trị khác nhau thành các OutputLists riêng lẻ.
Bạn có thể sử dụng node này để khôi phục cách mỗi hình ảnh được tạo ra từ một danh sách hình ảnh có cùng workflow.
Lưu ý rằng `IMAGE` của ComfyUI không chứa siêu dữ liệu workflow và bạn cần tải hình ảnh bằng các bộ tải hình ảnh+siêu dữ liệu chuyên dụng và kết nối siêu dữ liệu vào node này.
Các node tùy chỉnh có bộ tải siêu dữ liệu bao gồm:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Đầu Vào

| Tên | Kiểu | Mô Tả |
| --- | --- | --- |
| `objs_0` | `*` | (tùy chọn) Một đối tượng đơn (hoặc danh sách đối tượng), thường là một workflow. `objs_0` và `more_objs` sẽ được nối với nhau và tồn tại vì sự tiện lợi, nếu bạn chỉ muốn so sánh hai đối tượng. |
| `more_objs` | `*` | (tùy chọn) Một đối tượng khác (hoặc danh sách đối tượng), thường là một workflow. `objs_0` và `more_objs` sẽ được nối với nhau và tồn tại vì sự tiện lợi, nếu bạn chỉ muốn so sánh hai đối tượng. |
| `ignore_jsonpaths` | `STRING` | (tùy chọn) Danh sách các JSONPaths để bỏ qua trong trường hợp bạn muốn nối nhiều bộ phân loại với nhau. |

### Đầu Ra

| Tên | Kiểu | Mô Tả |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

