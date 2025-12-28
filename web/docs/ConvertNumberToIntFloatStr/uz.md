<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Butun son, haqiqiy son, matnga o'tkazish

![Butun son, haqiqiy son, matnga o'tkazish](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI ish yoki o'zgarishlari bilan birga)

Istalgan sonli ma'lumotni `BUTUN SON` `HAQIQIY SON` `MATN`ga o'tkazadi.
Ichida `nums_from_string.get_nums`dan foydalanadi, bu sonlarni qabul qilishda juda yengil. Haqiqiy butun sonlar, haqiqiy sonlar, matn sifatida butun sonlar yoki haqiqiy sonlar, minglik ajratuvchilari bilan birga bir nechta sonlarni o'z ichiga olgan matnlar.
Tezda sonlar ro'yxatini yaratish uchun `123;234;345` matnidan foydalaning. Virgul ajratuvchilari sifatida ishlatmang, chunki ular minglik ajratuvchilari sifatida talqin qilinishi mumkin.
`butun son`, `haqiqiy son` va `matn` `is_output_list=True` (belgisi `𝌠` bilan belgilangan) ishlatadi va mos keladigan tugmalar tomonidan ketma-ket bajariladi.

### Kirishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `istalgan` | `*` | Matn sifatida o'qiladigan va ichida o'qiladigan sonlarni o'z ichiga oladigan istalgan narsa |

### Chiquvchilar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `butun son` | `BUTUN SON 𝌠` | Matnda topilgan barcha sonlar, o'nlik qismi olib tashlangan. |
| `haqiqiy son` | `HAQIQIY SON 𝌠` | Matnda topilgan barcha sonlar haqiqiy son sifatida. |
| `matn` | `MATN 𝌠` | Matnda topilgan barcha sonlar haqiqiy son sifatida o'qilgan va matnga o'tkazilgan. |
| `soni` | `BUTUN SON` | Qiymatda topilgan sonlar miqdori. |

