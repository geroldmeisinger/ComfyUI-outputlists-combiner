## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow qo‘shimli)

JSON ob‘ektlardan massivlar yoki lug‘atlarni ajratib olib, OutputList yaratadi.
Qiymatlarni ajratish uchun JSONPath sintaksisidan foydalanadi, [JSONPath Wikipedia'da](https://en.wikipedia.org/wiki/JSONPath) ko‘ring.
Barcha mos kelgan qiymatlar bitta uzun ro‘yxatga tekkan qilinadi.
Siz ushbu nodadan `[1, 2, 3]` kabi literal satrlardan ob‘ekt yaratish uchun ham foydalanishingiz mumkin.
`key`, `value`, `int` va `float` `is_output_list=True` (belgi `𝌠` bilan ko‘rsatilgan) dan foydalanadi va mos keladigan nodalar tomonidan ketma-ket qayta ishlanadi.

### Kirishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `jsonpath` | `STRING` | Qiymatlarni ajratish uchun ishlatiladigan JSONPath. |
| `json` | `STRING` | Ob‘ektga aylantiriladigan JSON satri. |
| `obj` | `*` | (ixtiyoriy) JSON satrini almashtiradigan istalgan turdagi ob‘ekt |

### Chiqishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Lug‘atlar uchun kalit yoki massivlar uchun indeks (satr sifatida). Aniq ravishda bu barcha kalit bo‘lmaganlar uchun tekkan qilingan ro‘yxatning global indeksi. |
| `value` | `STRING 𝌠` | Qiymat satr sifatida. |
| `int` | `INT 𝌠` | Qiymat butun sifatida (agar raqamni tahlil qilib bo‘lmasa, 0 qiymatiga qaytadi). |
| `float` | `FLOAT 𝌠` | Qiymat haqiqiy sifatida (agar raqamni tahlil qilib bo‘lmasa, 0 qiymatiga qaytadi). |
| `count` | `INT` | Tekkan qilingan ro‘yxatdagi elementlar umumiy soni |
| `debug` | `STRING` | Barcha mos kelgan ob‘ektlarning xatoliklarni aniqlash chiqishi formatlangan JSON satri sifatida |

