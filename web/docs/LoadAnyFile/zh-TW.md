## 載入任意檔案

![載入任意檔案](LoadAnyFile/LoadAnyFile.png)

(包含 ComfyUI 工作流程)

載入任何文字或二進位檔案，並提供檔案內容為字串或 base64 字串。此外也會嘗試將其載入為 `IMAGE`。並嘗試載入任何元資料。

`filepath` 支援 ComfyUI 的註解路徑 `[input]` `[output]` 或 `[temp]`。
`filepath` 也支援 glob 模式擴展 `subdir/**/*.png`。
內部使用 Python 的 [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob)。

`metadata` 呼叫 `exiftool`，如果它已安裝且在 `PATH` 中可用，否則使用 `PIL.Image.info` 作為備用方案。

出於安全考量，僅支援以下目錄：`[input] [output] [temp]`。
出於效能考量，檔案數量限制為：1024。

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `filepath` | `STRING` | 基本目錄預設為 `[input]` 使用者目錄。支援 glob 模式擴展 `subdir/**/*.png`。使用副檔名 ` [input]` ` [output]` 或 ` [temp]`（注意前導空白！）來指定不同的 ComfyUI 使用者目錄。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `content` | `STRING 𝌠` | 文字檔案的內容，二進位檔案為 base64。 |
| `image` | `IMAGE 𝌠` | 圖片批次張量。 |
| `mask` | `MASK 𝌠` | 遮罩批次張量。 |
| `metadata` | `STRING 𝌠` | ExifTool 的 Exif 資料。需要 `exiftool` 命令在 `PATH` 中可用。 |

