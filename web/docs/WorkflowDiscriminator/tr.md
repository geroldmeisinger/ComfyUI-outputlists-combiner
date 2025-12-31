## İş Akışı Ayırt Edici

![Workflow Discriminator](WorkflowDiscriminator/WorkflowDiscriminator.png)

(ComfyUI iş akışı dahil)

İş akışlarını karşılaştırır ve farklı değerleri ayrı OutputList'ler olarak ayıklamak için ayrıştırır.
Bu düğümü, aynı iş akışından oluşturulmuş görüntüler listesinden her bir görüntünün nasıl oluşturulduğunu geri yüklemek için kullanabilirsiniz.
ComfyUI'nin `IMAGE` öğesinin iş akışı üst veri bilgisini içermediğini ve görüntülerin özel görüntü+üst veri yükleyicileriyle yüklenmesi ve üst verinin bu düğüme bağlanması gerektiğini unutmayın.
Üst veri yükleyicileri içeren özel düğümler şunlardır:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `objs_0` | `*` | (isteğe bağlı) Genellikle bir iş akışının bir nesnesi (veya nesneler listesi). `objs_0` ve `more_objs` birleştirilir ve sadece iki nesneyi karşılaştırmak istiyorsanız kolaylık sağlamak için bulunurlar. |
| `more_objs` | `*` | (isteğe bağlı) Genellikle bir iş akışının başka bir nesnesi (veya nesneler listesi). `objs_0` ve `more_objs` birleştirilir ve sadece iki nesneyi karşılaştırmak istiyorsanız kolaylık sağlamak için bulunurlar. |
| `ignore_jsonpaths` | `STRING` | (isteğe bağlı) Birden fazla ayırt ediciyi zincirlemek istiyorsanız yok saymak istediğiniz JSONYolların listesi. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

