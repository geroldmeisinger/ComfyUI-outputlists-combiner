## Rəqəmə Dəyişdir (INT, FLOAT, STR)

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow daxildədir)

Hər nə type nəticəsində `INT` `FLOAT` `STRING` formatına çevirir.
`nums_from_string.get_nums` funksiyasından istifadə edir ki, bu funksiya rəqəmləri qəbul etməkdə çox da dəyərli olur. Hər nə int, float, string formatında rəqəmlər, minlər ayırıcı ilə yazılmış rəqəmlər varsa, hər şey qəbul olunur.
`123;234;345` formatında string istifadə edərək rəqəmlər siyahısı yarada bilərsiniz. Vergüllər minlər ayırıcı kimi qəbul oluna biləcəyi üçün ayırıcı kimi istifadə etməyin.
`int`, `float` və `string` dəyərləri `is_output_list=True` (simvol ilə göstərilmiş `𝌠`) istifadə edərək ardıcıl olaraq təyin ediləcək və uyğun node-lar tərəfindən işlənəcək.

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `any` | `*` | String formatında parse edilə bilən rəqəmlərə malik hər nə |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `int` | `INT 𝌠` | String-də tapılan bütün rəqəmlər ondalıq hissələr kəsilərək |
| `float` | `FLOAT 𝌠` | String-də tapılan bütün rəqəmlər float formatında |
| `string` | `STRING 𝌠` | String-də tapılan bütün rəqəmlər float formatında stringə çevirilmiş |
| `count` | `INT` | Dəyərdə tapılan rəqəmlərin sayı |

