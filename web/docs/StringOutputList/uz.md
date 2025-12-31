## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow qo‘shilgan)

Matn maydonidagi satrni ajratgich bilan ajratib, OutputList yaratadi.
`value` va `index` `is_output_list=True` (belgi `𝌠` bilan ko‘rsatilgan) dan foydalanadi va mos keladigan nodelar tomonidan ketma-ket qayta ishlanadi.

### Kirishlar

| Ism | Tur | Tavsif |
| --- | --- | --- |
| `separator` | `STRING` | Matn maydonidagi qiymatlarni ajratish uchun ishlatiladigan satr. |
| `values` | `STRING` | Ro‘yxatga ajratmoqchi bo‘lgan matn. Eslatma: satr ajratishdan oldin oxirgi yangi qatorlar olib tashlanadi, har bir element yana bo‘shliqlardan tozalanadi. |

### Chiqishlar

| Ism | Tur | Tavsif |
| --- | --- | --- |
| `value` | `* 𝌠` | Ro‘yxatdagi qiymatlar. |
| `index` | `INT 𝌠` | 0..count oralig‘i. Siz uni indeks sifatida ishlatishingiz mumkin. |
| `count` | `INT` | Ro‘yxatdagi elementlar soni. |
| `inspect_combo` | `COMBO` | `COMBO` ga ulanish uchun foydalanishingiz mumkin bo‘lgan dummy-chiqish va uni qiymatlari bilan to‘ldirish mumkin. Ulash keyin avtomatik ravishda `value` chiqishiga qayta ulanadi. |

