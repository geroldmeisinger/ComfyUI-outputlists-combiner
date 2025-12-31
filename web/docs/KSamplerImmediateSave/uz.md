## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow qo‘shimcha)

Standart `CheckpointLoader`, `KSampler`, `VAE Decode` va `Save Image` nodlarini birlashtirish uchun kengaytirish.
Bunday qilish, gridlarga joylashtirish uchun o'rtacha tasvirlarni saqlash kerak bo'lganda foydali bo'ladi.

*"Rasimni saqlash uchun maxsus KSampler? Endi men o'zimni qidirayotgan narsaning o'zi bo'ldim!"*

### Kirishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Yuklanadigan checkpoint (model) nomi. |
| `positive` | `STRING` | Tasvirda qo‘shishni xohlagan xususiyatlarni tavsiflovchi shart. |
| `negative` | `STRING` | Tasvirdan chiqarishni xohlagan xususiyatlarni tavsiflovchi shart. |
| `latent_image` | `LATENT` | Shafof tasvir shuni tozalash uchun. |
| `seed` | `INT` | Shaxsiy shaklga ega bo'lgan shumor yaratish uchun foydalaniladigan tasodifiy qiymat. |
| `steps` | `INT` | Tozalash jarayonida foydalaniladigan qadam soni. |
| `cfg` | `FLOAT` | Classifier-Free Guidance miqdori, ijro va so'rovga moslik o'rtasida muvozanat. Yuqori qiymatlar so'rovga yaqinroq tasvirlarga olib keladi, lekin juda yuqori qiymatlar sifatni negativ ta'sir qiladi. |
| `sampler_name` | `COMBO` | Namoyish jarayonida foydalaniladigan algoritm, bu so'rovga mos keluvchi chiqish sifatini, tezligini va uslubini o'zgartiradi. |
| `scheduler` | `COMBO` | Rejasi shumor biror qanday qilib chiqishga olib keladi. |
| `denoise` | `FLOAT` | Tozalash miqdori, qiymat past bo'lsa, boshlang'ich tasvir tuzilishi saqlanadi, rasmdan rasmga namoyish amalga oshiriladi. |
| `filename_prefix` | `STRING` | Saqlanadigan fayl uchun prefiks. Bu %date :yyyy-MM-dd% yoki %Empty Latent Image.width% kabi formatlash ma'lumotlarini o'z ichiga oladi, bu ma'lumotlar nodlardan olingan qiymatlarni qo'shadi. |

### Chiqishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `image` | `IMAGE` | Dekodlangan tasvir. |

