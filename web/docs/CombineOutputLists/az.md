<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists Combinations

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

4 OutputLists-dan istifadə edər və onlara əsaslanan hər bir kombinasiyasını yaradır.

Məsələ: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` (𝌠 simvolu ilə göstərilir) və mənfi nöqtələr tərəfindən mənfi nöqtələrə təsir edir.

Bütün listlər mütləq deyil və boş listlər qeyd olunmur.

Təsirli olaraq, *Kartezian hasil* hesablanır və hər bir kombinasiya elementləri ilə (unzip) çıxarılır, boş listlər `None` ilə əvəz olunur və onların mənfi nöqtələri `None` olur.

Məsələ: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `list_a` | `*` | (optional) |
| `list_b` | `*` | (optional) |
| `list_c` | `*` | (optional) |
| `list_d` | `*` | (optional) |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`-ya uyğun kombinasiyanın qiyməti. |
| `unzip_b` | `* 𝌠` | `list_b`-ya uyğun kombinasiyanın qiyməti. |
| `unzip_c` | `* 𝌠` | `list_c`-ya uyğun kombinasiyanın qiyməti. |
| `unzip_d` | `* 𝌠` | `list_d`-ya uyğun kombinasiyanın qiyməti. |
| `index` | `INT 𝌠` | 0..count aralığında olan və index kimi istifadə edilə bilən qiymət. |
| `count` | `INT` | Kombinasiyanın əsas sayının qiyməti. |

