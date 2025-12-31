## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow qo‘shimli)

Rasm ro‘yxatidan XYZ-Gridplot yaratadi.
U rasm ro‘yxatini (jamlanishlar hamda) avval uzun ro‘yxatga aylantiradi (shu sababli `batch_size=1`).

**Grid shakli**
To‘rtburchak shaklini belgilaydi:
1. qator etiketlar soni
2. ustun etiketlar soni
3. qolgan qismdagi tushlar.
`order=inside_out` dan foydalanish orqali rasm tanlash tartibini o‘zgartirishingiz mumkin (masalan `batch_size>1` bo‘lganda, jamlanishlarni belgilash uchun foydalidir).

**Qatorlash**
* Agar etiket yangi qatorda joylashgan bo‘lsa, butun o‘sish hisoblanadi "multiline" va ularni yuqori qismga qo‘yadi, joylashtirish joyi teng.
* Agar barcha etiketlar sonlar bo‘lsa yoki barchasi son bilan tugasa (masalan `strength: 1.`) butun o‘sish "numeric" hisoblanadi va ularni o‘ng qismga qo‘yadi.
* Boshqa barcha matnlar "singleline" hisoblanadi va ularni markazga qo‘yadi.
* Bitta qator va ustunlar uchun etiketlarni pastga qo‘yadi, qatorlar uchun esa markazda vertikal ravishda joylashtiradi.

**Shrift hajmi**
* Ustun etiketlar maydonining balandligi `font_size` yoki har qatordagi eng katta qismga joylashtirilgan tushlar balandligining yarmi (ularning kattasini tanlab) bo‘ladi.
* Qator etiketlar maydonining kengligi tushlar joylashtirilgan eng katta kenglik (minimum 256px).
* Matn hajmi kamayib boradi (minimum `font_size_min=6`) va butun o‘sish uchun bir xil shrift hajmi ishlatiladi (qator etiketlar yoki ustun etiketlar).
Agar shrift hajmi allaqachon minimum bo‘lsa, qolgan matnlarni kesadi.

**Tushlar joylashtirish**
Tushlarni eng kvadrat shaklga keltiradi (tushlar joylashtirish), `output_is_list=True` bo‘lmasa. Shu bilan birga, har bir katak uchun bitta rasm ishlatadi va butun rasm joylashtirishlar ro‘yxatini yaratadi.
Buni yordamida boshqa XyzGridPlot nodega ulash orqali super-grids yaratishingiz mumkin.
Agar tushlar turli hajmdagi jamlanishlardan iborat bo‘lsa, bo‘sh joylarni to‘ldiradi.
Bir katak uchun rasm soni (jamlanishlardan ham) `rows * columns` ga karrali bo‘lishi kerak.

### Kirish

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `images` | `IMAGE` | Rasm ro‘yxati (jamlanishlar hamda) |
| `row_labels` | `*` | Qator etiketlar matni chap tomondan |
| `col_labels` | `*` | Ustun etiketlar matni yuqori tomondan |
| `gap` | `INT` | Tushlar joylashtirishlari orasidagi bo‘sh joy. Tushlar o‘zaro joylashishida hech qanday bo‘sh joy yo‘q. Agar tushlar orasidagi bo‘sh joy kerak bo‘lsa, boshqa XyzGridPlot nodega ulang. |
| `font_size` | `FLOAT` | Maqsad shrift hajmi. Matn hajmi kamayib boradi (minimum `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Qator etiketlar matnining joylashishi. Joy saqlash uchun foydalidir. |
| `order` | `BOOLEAN` | Tushlarni qanday tartibda qayta ishlash kerakligini aniqlaydi. Bu faqat tushlar mavjud bo‘lganda ahamiyatga ega. Masalan `batch_size>1` bo‘lganda, jamlanishlarni chizish uchun foydalidir. |
| `output_is_list` | `BOOLEAN` | Bu faqat tushlar yoki super-grids yaratish kerak bo‘lganda ahamiyatga ega. |

### Chiqish

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot rasm. Agar `output_is_list=True` bo‘lsa, rasm ro‘yxatini yaratadi, uni boshqa XYZ-GridPlot nodega ulash orqali super-grids yaratishingiz mumkin. |

