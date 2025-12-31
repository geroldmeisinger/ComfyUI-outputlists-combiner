## KSampler 即時儲存

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(包含 ComfyUI workflow)

對預設的 `CheckpointLoader`、`KSampler`、`VAE Decode` 和 `Save Image` 節點進行擴展，使其作為一個整體處理。
如果您想要立即儲存網格的中間圖像，這會很有用。

*"一個自定義的 KSampler 只是為了儲存圖像？現在我成了我所尋求摧毀的事物！"*

### 輸入

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | 要載入的檢查點（模型）名稱。 |
| `positive` | `STRING` | 描述您希望包含在圖像中的屬性的條件。 |
| `negative` | `STRING` | 描述您希望從圖像中排除的屬性的條件。 |
| `latent_image` | `LATENT` | 要去噪的潛在圖像。 |
| `seed` | `INT` | 用於創建噪音的隨機種子。 |
| `steps` | `INT` | 去噪過程中使用的步數。 |
| `cfg` | `FLOAT` | 無分類指導尺度（Classifier-Free Guidance scale）平衡創意與提示的遵循程度。數值越高，圖像越貼近提示，但過高會對品質產生負面影響。 |
| `sampler_name` | `COMBO` | 用於採樣的演算法，這會影響生成輸出的品質、速度和風格。 |
| `scheduler` | `COMBO` | 排程器控制噪音如何逐步被移除以形成圖像。 |
| `denoise` | `FLOAT` | 應用的去噪量，較低的值將保持初始圖像的結構，允許進行圖像到圖像的採樣。 |
| `filename_prefix` | `STRING` | 儲存檔案的前綴。這可能包含格式化資訊，例如 %date:yyyy-MM-dd% 或 %Empty Latent Image.width% 以包含來自節點的值。 |

### 輸出

| 名稱 | 類型 | 描述 |
| --- | --- | --- |
| `image` | `IMAGE` | 解碼後的圖像。 |

