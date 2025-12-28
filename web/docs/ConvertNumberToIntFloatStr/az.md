<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Sətrləri Int Float Str-ə Dəyişdir

![Sətrləri Int Float Str-ə Dəyişdir](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Bir neçə ədəd kimi görünən şeyləri `INT` `FLOAT` `STRING`-ə dəyişdirir.
İçərsiz `nums_from_string.get_nums` işləyir və qəbul eddiyi ədədlər çox məhdud deyil. Həqiqi ədədlər, həqiqi ədədlər kimi, ədədlər kimi, ədədlərə sahib olan sətirlər və 1000-lik bölmələrlə ayrılmış sətirlər də daxil olur.
Sətir `123;234;345` istifadə edərək ədədlərin listini sürətlə yaradın. 1000-lik bölmələr kimi qəbul edilə biləcək komma işarələri istifadə etməyin.
`int`, `float` və `string` `is_output_list=True` (sənəd `𝌠` ilə göstərilir) və mənfi nöqtələrlə əlaqədə olan nöqtələr ilə işləyir.

### Girişi

| Ad | Tip | Təsvir |
| --- | --- | --- |
| `any` | `*` | Sətirə çevrilmək üçün mənfi ədədlər içəridə olmaqla məna qoyulmuş şeylər |

### Çıxışı

| Ad | Tip | Təsvir |
| --- | --- | --- |
| `int` | `INT 𝌠` | Sətirdə tapılan ədədlər, onlara nəzər yetirilən ədədlər. |
| `float` | `FLOAT 𝌠` | Sətirdə tapılan ədədlər, onlara nəzər yetirilən ədədlər. |
| `string` | `STRING 𝌠` | Sətirdə tapılan ədədlər, onlara nəzər yetirilən ədədlər. |
| `count` | `INT` | Məlumatda tapılan ədədlərin sayını göstərir. |

