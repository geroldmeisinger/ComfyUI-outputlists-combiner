## OutputLists Birliyi

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow daxildir)

4-cü OutputList və onların hər birini əmələ gətirir.

Nümunə: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` (simvol ilə göstərilmiş `𝌠`) istifadə edir və müvafiq düyünlər tərəfindən ardıcıl olaraq işlənir.

Bütün siyahılar istəyə bağlıdır və boş siyahılar gözardı olunur.

Texnik olaraq *Karteziyani hasil* hesablayır və hər bir kombinasiyanı elementlərinə bölünmüş şəkildə çıxarır (`unzip`), bu zaman boş siyahılar `None` ilə əvəz olunur və onlar müvafiq çıxışda `None` çıxarır.

Nümunə: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Girişlər

| Ad | Növ | İzahat |
| --- | --- | --- |
| `list_a` | `*` | (istəyə bağlı) |
| `list_b` | `*` | (istəyə bağlı) |
| `list_c` | `*` | (istəyə bağlı) |
| `list_d` | `*` | (istəyə bağlı) |

### Çıxışlar

| Ad | Növ | İzahat |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`-ya uyğun kombinasiyaların dəyəri. |
| `unzip_b` | `* 𝌠` | `list_b`-ya uyğun kombinasiyaların dəyəri. |
| `unzip_c` | `* 𝌠` | `list_c`-ya uyğun kombinasiyaların dəyəri. |
| `unzip_d` | `* 𝌠` | `list_d`-ya uyğun kombinasiyaların dəyəri. |
| `index` | `INT 𝌠` | 0..count aralığı, indeks kimi istifadə edilə bilər. |
| `count` | `INT` | Ümumi kombinasiya sayı. |

