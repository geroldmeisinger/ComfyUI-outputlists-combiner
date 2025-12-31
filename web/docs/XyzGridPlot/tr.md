## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow dahil)

Resim listesinden bir XYZ-Gridplot oluşturur.
Resim listesini (toplu işlemler dahil) önce düz bir listeye dönüştürür (bu nedenle `batch_size=1` olur).

**Izgara şekli**
Izgaranın şeklini şu şekilde belirler:
1. Satır etiketlerinin sayısı
2. Sütun etiketlerinin sayısı
3. Kalan alt-görüntüler.
`batch_size>1` ise ve toplu işlemleri etiketlemek istiyorsanız `order=inside_out` kullanabilirsiniz.

**Hizalama**
* Bir etiket bir sonraki satıra kaydırılırsa, tüm eksen "multiline" olarak kabul edilir ve boşluklar justified (hizalı) olarak yukarı hizalanır.
* Tüm etiketler sayıysa veya hepsi sayıyla bitiyorsa (örneğin `strength: 1.`) tüm eksen "numeric" olarak kabul edilir ve sağa hizalanır.
* Diğer tüm metinler "singleline" olarak kabul edilir ve ortalanır.
* Sütunlarda tek satırlı ve sayısal etiketleri altta, satırlarda ortalar şekilde dikey olarak ortalar.

**Yazı Tipi Boyutu**
* Sütun etiketi alanının yüksekliği `font_size` veya her satırdaki en büyük alt-görüntü paketleme yüksekliğinin yarısı (bunlardan hangisi büyükse) ile belirlenir.
* Satır etiketi alanının genişliği alt-görüntü paketleme en geniş genişliği ile belirlenir (minimum 256px).
* Metin, sığacak şekilde küçültülür (en az `font_size_min=6`) ve tüm eksen için aynı yazı tipi boyutu kullanılır (satır etiketleri veya sütun etiketleri).
Yazı tipi boyutu zaten minimumdaysa, kalan metinler kesilir.

**Alt-görüntü paketleme**
Alt-görüntüleri (genellikle toplu işlemlerden gelenleri) en kare alanı oluşturacak şekilde şekillendirir ("alt-görüntü paketleme"), `output_is_list=True` değilse, her hücre için sadece bir görüntü kullanır ve tam görüntü izgaralarının bir listesini oluşturur.
Bu görüntü izgaralarının listesini başka bir XyzGridPlot düğümüne bağlayarak süper-ızgaralar oluşturabilirsiniz.
Eğer alt-görüntüler farklı boyutlarda toplu işlemlerden oluşuyorsa, eksik hücreleri boş görüntülerle doldurur.
Hücre başına düşen görüntü sayısı (toplu görüntüler dahil) `rows * columns`'un katı olmalıdır.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `images` | `IMAGE` | Resim listesi (toplu işlemler dahil) |
| `row_labels` | `*` | Sol tarafta bulunan satır etiket metinleri |
| `col_labels` | `*` | Üst tarafta bulunan sütun etiket metinleri |
| `gap` | `INT` | Alt-görüntü paketleme arasındaki boşluk. Alt-görüntüler arasında boşluk yoktur. Alt-görüntüler arasında boşluk istiyorsanız başka bir XyzGridPlot düğümü bağlayın. |
| `font_size` | `FLOAT` | Hedef yazı tipi boyutu. Metin sığacak şekilde küçültülür (en az `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Satır etiketlerinin metin yönü. Alan tasarrufu için faydalıdır. |
| `order` | `BOOLEAN` | Görüntülerin işleme sırasını tanımlar. Bu yalnızca alt-görüntüleriniz varsa önemlidir. `batch_size>1` ve toplu işlemleri çizmek istiyorsanız faydalıdır. |
| `output_is_list` | `BOOLEAN` | Bu yalnızca alt-görüntüleriniz varsa veya süper-ızgaralar oluşturmak istiyorsanız önemlidir. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot görüntüsü. `output_is_list=True` ise, başka bir XYZ-GridPlot düğümüne bağlayabileceğiniz görüntü listesi oluşturur ve süper-ızgaralar oluşturmanızı sağlar. |

