## Raqam Chiqish Ro'yxati

![Raqam Chiqish Ro'yxati](NumberOutputList/NumberOutputList.png)

(ComfyUI ishlash oqimi qo'shib berilgan)

Raqamli qiymatlardan iborat ChiqishRo'yxat yaratadi.
U [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) dan ichki sifatida foydalanadi, chunki u o'nlik sonlarda ishlashi kafolatlanadi.
Agar siz ixtiyoriy qadam bilan raqamlar ro'yxatini aniqlamoqchi bo'lsangiz, JSON ChiqishRo'yxatini ko'rib chiqing va massivni aniqlang, masalan `[1, 42, 123]`.
`int`, `float`, `string` va `index` `is_output_list=True` (belgi `𝌠` bilan ko'rsatilgan) dan foydalanadi va mos uzunlikdagi tugunlar tomonidan ketma-ket ishlanadi.

### Kirishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `start` | `FLOAT` | Qiymat diapazonini yaratish uchun boshlang'ich qiymat. |
| `stop` | `FLOAT` | Oxirgi qiymat. Agar `endpoint=include` bo'lsa, bu raqam ro'yxatga kiritiladi. |
| `num` | `INT` | Ro'yxatdagi elementlar soni (`step` bilan xato tushunmaslik kerak). |
| `endpoint` | `BOOLEAN` | `stop` qiymat ro'yxatga kiritsin yoki kiritilmasin. |

### Chiqishlar

| Ism | Turi | Tavsif |
| --- | --- | --- |
| `int` | `INT 𝌠` | Qiymat butun qismga aylantirilgan (pastga qarab yaxlitlangan). |
| `float` | `FLOAT 𝌠` | Qiymat o'nlik sifatida. |
| `string` | `STRING 𝌠` | Qiymat o'nlik sifatida satrga aylantirilgan. |
| `index` | `INT 𝌠` | 0..count oralig'i, indeks sifatida foydalanish mumkin. |
| `count` | `INT` | `num` ga teng. |

