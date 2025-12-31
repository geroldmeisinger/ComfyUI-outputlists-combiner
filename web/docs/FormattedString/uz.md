## Formatlangan satr

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow qo'shildi)

Placeholder o'zgaruvchilarni o'z ichiga olgan satr yaratadi va ularni mos qiymatlar bilan almashtiradi.
Python `str.format()` funksiyasidan ichki sifatda foydalanadi, [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) ga qarang.
* Float qiymatni 2 xonaga yaxlitlash uchun `{a:.2f}` dan foydalanishingiz mumkin.
* Comfys fayl nomi suffixi `ComfyUI_00001_.png` bilan moslashish uchun 5 ta boshlanuvchi nol bilan to'ldirish uchun `{a:05d}` dan foydalanishingiz mumkin.
* Agar satrlaringiz ichida `{ }` belgilarni yozmoqchi bo'lsangiz (masalan JSON uchun), ularni ikki marotaba yozishingiz kerak: `{{ }}`.

Shuningdek, `%date:yyyy-MM-dd hh:mm:ss%` va `%KSampler.seed%` kabi *qidiruv va almashtirish (S&R)* sintaksisini qo'llaydi.
Shunday qilib, uni `GET-node` sifatida ham foydalanishingiz mumkin.
"Qidiruv va almashtirish" jarayoni Javascript kontekstida sodir bo'lib, nodeni bajarishdan oldin ishga tushadi.

### Kirishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `fstring` | `STRING` | Placeholder o'zgaruvchilarni o'z ichiga olgan satr yaratadi va ularni mos qiymatlar bilan almashtiradi.<br>Python `str.format()` funksiyasidan ichki sifatda foydalanadi, [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) ga qarang.<br>* Float qiymatni 2 xonaga yaxlitlash uchun `{a:.2f}` dan foydalanishingiz mumkin.<br>* Comfys fayl nomi suffixi `ComfyUI_00001_.png` bilan moslashish uchun 5 ta boshlanuvchi nol bilan to'ldirish uchun `{a:05d}` dan foydalanishingiz mumkin.<br>* Agar satrlaringiz ichida `{ }` belgilarni yozmoqchi bo'lsangiz (masalan JSON uchun), ularni ikki marotaba yozishingiz kerak: `{{ }}`.<br><br>Shuningdek, `%date:yyyy-MM-dd hh:mm:ss%` va `%KSampler.seed%` kabi *qidiruv va almashtirish (S&R)* sintaksisini qo'llaydi.<br>Shunday qilib, uni `GET-node` sifatida ham foydalanishingiz mumkin.<br>"Qidiruv va almashtirish" jarayoni Javascript kontekstida sodir bo'lib, nodeni bajarishdan oldin ishga tushadi. |
| `a` | `*` | (ixtiyoriy) `{a}` placeholderda sifatda satr sifatida bo'ladigan qiymat. |
| `b` | `*` | (ixtiyoriy) `{b}` placeholderda sifatda satr sifatida bo'ladigan qiymat. |
| `c` | `*` | (ixtiyoriy) `{c}` placeholderda sifatda satr sifatida bo'ladigan qiymat. |
| `d` | `*` | (ixtiyoriy) `{d}` placeholderda sifatda satr sifatida bo'ladigan qiymat. |

### Chiqishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `string` | `STRING` | Barcha placeholderlar mos qiymatlar bilan almashtirilgan formatlangan satr. |

