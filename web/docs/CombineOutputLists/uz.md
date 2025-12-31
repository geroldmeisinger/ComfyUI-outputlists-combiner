## OutputLists kombinatsiyalari

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow qo‘shilgan)

4 ta OutputList qabul qiladi va ularning barcha kombinatsiyalarini hosil qiladi.

Misol: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` (belgi `𝌠` bilan ko‘rsatilgan) yordamida ishlaydi va mos keladigan nodelar tomonidan ketma-ket bajariladi.

Barcha ro‘yxatlar ixtiyoriy bo‘lib, bo‘sh ro‘yxatlar e’tiborga olinmaydi.

Texnik jihatdan bu *Karteziy ko‘paytma* hisoblaydi va har bir kombinatsiyani unikal qilib chiqaradi (`unzip`), bo‘sh ro‘yxatlar `None` bilan almashtiriladi va ular mos keladigan chiqishda `None` qaytaradi.

Misol: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Kirish

| Nom | Turi | Tavsif |
| --- | --- | --- |
| `list_a` | `*` | (ixtiyoriy) |
| `list_b` | `*` | (ixtiyoriy) |
| `list_c` | `*` | (ixtiyoriy) |
| `list_d` | `*` | (ixtiyoriy) |

### Chiqish

| Nom | Turi | Tavsif |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a` ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_b` | `* 𝌠` | `list_b` ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_c` | `* 𝌠` | `list_c` ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_d` | `* 𝌠` | `list_d` ga mos keladigan kombinatsiyalarning qiymati. |
| `index` | `INT 𝌠` | 0..count oralig‘i, indeks sifatida foydalanish mumkin. |
| `count` | `INT` | Jami kombinatsiyalar soni. |

