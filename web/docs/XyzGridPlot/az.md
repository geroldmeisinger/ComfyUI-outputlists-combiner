<!-- This file was auto-translated with a local LLM and last updated on 2025-12-31. -->
## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow daxil edilib)

Şəkillər siyahısından XYZ-Gridplot yaradır.
Bu, şəkillər siyahısını (partlylər də daxil olmaqla) əvvəlcə uzun siyahıya düzəldir (buna görə də `batch_size=1`).

**Cədvəl forması**
Cədvəlin formasını təyin edir:
1. sətir etiketlərinin sayı
2. sütun etiketlərinin sayı
3. qalan alt şəkillər.
Sənətən `batch_size>1` və partləri etiketləmək istədiyiniz halda `order=inside_out` istifadə edə bilərsiniz.

**Yerləşdirmə**
* Etiket növbəti sətirə qatılsa, bütün ox "çoxsətir" hesab olunur və onları üstə düzə və sətirlər arasında bərabər boşluqla yığırlar.
* Bütün etiketlər rəqəmlərdirsə və ya hər biri rəqəmlə bitirsə (məsələn `strength: 1.`) bütün ox "rəqəmsə" hesab olunur və onları sağa yığırlar.
* Digər bütün mətnlər "tək sətir" hesab olunur və onları mərkəzlə yığırlar.
* Sütunlar üçün tək sətir və rəqəmsə etiketləri alt qəfəsə, sətirlər üçün orta qəfəsə düzəldirlər.

**Şrift ölçüsü**
* Sütun etiketləri sahəsinin hündürlüyü `font_size` və ya hər sətirdə ən böyük alt şəkillərin hündürlüyünün yarısı (ən böyük olanı) təyin edir.
* Sətir etiketləri sahəsinin eni alt şəkillərin ən geniş eninə (minimum 256px) qədər təyin olunur.
* Mətn təxirə salınır və yerə sığdırmaq üçün `font_size_min=6` qədər kiçildir və bütün ox üçün eyni şrift ölçüsünü istifadə edir (sətir etiketləri və ya sütun etiketləri).
Əgər şrift ölçüsü artıq minimumdursa, qalan mətni kəsir.

**Alt şəkillərin yerləşdirməsi**
Alt şəkilləri (əsasən partlərdən) ən kvadrat sahəyə (alt şəkillərin yerləşdirməsi) çevirir, əgər `output_is_list=True` deyilsə, hər bir hüceyrə üçün yalnız bir şəkil istifadə edir və tam şəkillər cədvəlin siyahısını yaradır.
Bu şəkillər cədvəlin siyahısını başqa bir XyzGridPlot düyməsinə qoşmaq üçün istifadə edə bilərsiniz, super-cədvəllər yaratmaq üçün.
Əgər alt şəkillər müxtəlif ölçülərdə partlərdən ibarətdirsə, boş hüceyrələri boş şəkillərlə doldurur.
Hüceyrələrə düşən şəkillərin sayı (partlər də daxil olmaqla) `rows * columns`-in çoxluğu olmalıdır.

### Girişlər

| Ad | Növ | Təsvir |
| --- | --- | --- |
| `images` | `IMAGE` | Şəkillər siyahısı (partlylər də daxil olmaqla) |
| `row_labels` | `*` | Sol tərəfdəki sətir etiketləri |
| `col_labels` | `*` | Yuxarıdakı sütun etiketləri |
| `gap` | `INT` | Alt şəkillər arasında boşluq. Nəzərə alın ki, alt şəkillər öz aralarında boşluq istifadə etmir. Əgər alt şəkillər arasında boşluq istəyirsinizsə başqa bir XyzGridPlot düyməsi qoşun. |
| `font_size` | `FLOAT` | Hədəf şrift ölçüsü. Mətn təxirə salınır və yerə sığdırmaq üçün `font_size_min=6` qədər kiçildir. |
| `row_label_orientation` | `COMBO` | Sətir etiketlərinin mətn yönü. Yer qazanmaq istədiyiniz halda faydalıdır. |
| `order` | `BOOLEAN` | Şəkillərin necə işlənəcəyini təyin edir. Bu yalnız alt şəkilləriniz varsa vacibdir. `batch_size>1` və partləri qrafikə qoymaq istədiyiniz halda faydalıdır. |
| `output_is_list` | `BOOLEAN` | Bu yalnız alt şəkilləriniz varsa və ya super-cədvəllər yaratmaq istədiyiniz halda vacibdir. |

### Çıxışlar
| Ad | Növ | Təsvir |
| --- | --- | --- |
| `output` | `IMAGE` | Nəticə şəkli |
| `image` | `IMAGE 𝌠` | The XYZ-GridPlot image. If `output_is_list=True` creates a list of images which you can connect to another XYZ-GridPlot node to create super-grids. |

