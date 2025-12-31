## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow daxildədir)

Rəqəmsal dəyərlər aralığı ilə OutputList yaradır.
Ədədi dəyərlərlə daha etibarlı işləməsi üçün daxili olaraq [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) istifadə edir.
Əgər istəyirsinizsə, təsadüfi addımlarla rəqəm siyahılarını müəyyən etmək üçün JSON OutputList-a baxın və massiv təyin edin, məsələn `[1, 42, 123]`.
`int`, `float`, `string` və `index` istifadə edir `is_output_list=True` (simvol `𝌠` ilə göstərilir) və相应 node-lar tərəfindən ardıcıl olaraq işlənəcək.

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `start` | `FLOAT` | Aralığı yaratmaq üçün başlanğıc dəyəri. |
| `stop` | `FLOAT` | Bitiş dəyəri. Əgər `endpoint=include`olarsa, bu ədəd siyahıya daxil edilir. |
| `num` | `INT` | Siyahıdakı element sayı (`step` ilə qarışdırmayın). |
| `endpoint` | `BOOLEAN` | `stop` dəyərinin elementlərdə daxil ediləcəyini və ya istisna ediləcəyini qərər verir. |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `int` | `INT 𝌠` | Dəyər int-ə çevrildi (aşağı yuvarlaqlaşdırıldı). |
| `float` | `FLOAT 𝌠` | Dəyər kimi float. |
| `string` | `STRING 𝌠` | Dəyər float kimi string-ə çevrildi. |
| `index` | `INT 𝌠` | 0..count aralığı, indeks kimi istifadə edilə bilər. |
| `count` | `INT` | `num` ilə eyni. |

