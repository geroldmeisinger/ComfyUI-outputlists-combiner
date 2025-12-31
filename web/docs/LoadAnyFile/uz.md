## Har qanday faylni yuklash

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI ishlash oqimi qo'shildi)

Matn yoki ikkilik faylni yuklab olib, fayl tarkibini matn yoki base64 matn sifatida taqdim etadi. Shuningdek, u faylni `IMAGE` sifatida ham yuklashga harakat qiladi. Metadata larni ham yuklashga harakat qiladi.

`filepath` ComfyUI annotatsiyali fayl yo'llarini qo'llab-quvvatlaydi `[input]` `[output]` yoki `[temp]`.
`filepath` glob-pattern kengaytirishlarni ham qo'llab-quvvatlaydi `subdir/**/*.png`.
Ichki sifatda Python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) dan foydalanadi.

`metadata` agar `exiftool` o'rnatilgan bo'lsa va `PATH` da mavjud bo'lsa, uni chaqiradi, aks holda `PIL.Image.info` ni foydalanadi.

Xavfsizlik nuqtai nazaridan faqat quyidagi kataloglar qo'llab-quvvatlanadi: `[input] [output] [temp]`.
Ish faoliyatiga ko'ra fayllar soni quyidagicha cheklangan: 1024.

### Kirishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `filepath` | `STRING` | Asosiy katalog `[input]` foydalanuvchi katalogi sifatida sozlanadi. Glob-pattern kengaytirishlarni qo'llab-quvvatlaydi `subdir/**/*.png`. Boshqa ComfyUI foydalanuvchi katalogini ko'rsatish uchun ` [input]` ` [output]` yoki ` [temp]` (bosh joy bilan!) sufiksini ishlatib ko'rsating. |

### Chiqishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Matn fayllari uchun fayl tarkibi, ikkilik fayllar uchun base64. |
| `image` | `IMAGE 𝌠` | Rasm to'plami tensori. |
| `mask` | `MASK 𝌠` | Maska to'plami tensori. |
| `metadata` | `STRING 𝌠` | ExifTool dan Exif ma'lumotlari. `exiftool` buyrug'i `PATH` da mavjud bo'lishi kerak. |

