<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists kombinatsiyalari

![OutputLists kombinatsiyalari](CombineOutputLists/CombineOutputLists.png)

(ComfyUI vazifasi qo'shildi)

To'rtta OutputListni qabul qilib, ularning barcha kombinatsiyalarini yaratadi.

Misol: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` (belgisi bilan belgilangan `𝌠`) va mos keladigan tugmalar tomonidan ketma-ket bajariladi.

Barcha ro'yxatlar ixtiyoriy bo'lib, bo'sh ro'yxatlar e'tiborga olinmaydi.

Texnik jihatdan u *Kartezian ko'paytmasini* hisoblaydi va har bir kombinatsiyani ularning elementlariga ajratib chiqaradi (`unzip`), bo'sh ro'yxatlar `None` bilan almashtiriladi va mos keladigan chiqishda `None` chiqaradi.

Misol: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Kirishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `list_a` | `*` | (ixtiyoriy) |
| `list_b` | `*` | (ixtiyoriy) |
| `list_c` | `*` | (ixtiyoriy) |
| `list_d` | `*` | (ixtiyoriy) |

### Chiqishlar

| Nomi | Turi | Tavsif |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_b` | `* 𝌠` | `list_b`ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_c` | `* 𝌠` | `list_c`ga mos keladigan kombinatsiyalarning qiymati. |
| `unzip_d` | `* 𝌠` | `list_d`ga mos keladigan kombinatsiyalarning qiymati. |
| `index` | `INT 𝌠` | 0..soni oralig'ida bo'lib, indeks sifatida foydalanish mumkin. |
| `count` | `INT` | Jami kombinatsiyalar soni. |

