## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow daxildədir)

Mətn sahəsindəki sətri ayırıcı ilə bölərək OutputList yaradır.
`value` və `index` istifadə edir `is_output_list=True` (simvol `𝌠` ilə göstərilir) və相应 node-lar tərəfindən ardıcıl olaraq işlənəcək.

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `separator` | `STRING` | Mətn sahəsi dəyərlərini bölən sətir. |
| `values` | `STRING` | Siyahıya böləcəyiniz mətn. Qeyd edin ki, sətir bölünmədən əvvəl sondakı yeni sətirlər kəsilir və hər bir element yenidən boşluqlardan təmizlənir. |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `value` | `* 𝌠` | Siyahıdan dəyərlər. |
| `index` | `INT 𝌠` | 0..count aralığı. Bunu indeks kimi istifadə edə bilərsiniz. |
| `count` | `INT` | Siyahıdakı element sayı. |
| `inspect_combo` | `COMBO` | `COMBO`-ya qoşulmaq və onun dəyərlərlə doldurulmaq üçün istifadə edə biləcəyiniz dummy-output.Əlaqə avtomatik olaraq `value` çıxışına yenidən qoşulacaq. |

