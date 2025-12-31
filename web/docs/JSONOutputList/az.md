## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow daxildədir)

JSON obyektlərindən massivləri və lüğətləri çıxarmaqla OutputList yaradır.
Dəyərləri çıxarmaq üçün JSONPath sintaksisindən istifadə edir, bax [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Bütün uyğun dəyərlər bir uzun siyahıya düzülür.
Həmçinin bu node-la `[1, 2, 3]` kimi literal string-lərdən obyektlər yaratmaq olar.
`key`, `value`, `int` və `float` dəyərləri `is_output_list=True` (simvol ilə göstərilmiş `𝌠`) istifadə edərək ardıcıl olaraq təyin ediləcək və uyğun node-lar tərəfindən işlənəcək.

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `jsonpath` | `STRING` | Dəyərləri çıxarmaq üçün istifadə olunan JSONPath. |
| `json` | `STRING` | Obyektə çevrilən JSON string. |
| `obj` | `*` | (isteğe bağlı) JSON string-ini əvəz edəcək hər hansı tipdə obyekt |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Lüğətlər üçün açar və massivlər üçün indeks (string formatında). Texnik olaraq bu, düzülmiş siyahı üçün ümumi indeksdir, açarlar üçün deyil. |
| `value` | `STRING 𝌠` | Dəyər string formatında. |
| `int` | `INT 𝌠` | Dəyər int formatında (rəqəmi təhlil etmək mümkün deyilsə, 0 ilə qaytarılır). |
| `float` | `FLOAT 𝌠` | Dəyər float formatında (rəqəmi təhlil etmək mümkün deyilsə, 0 ilə qaytarılır). |
| `count` | `INT` | Düzülmiş siyahıda ümumi element sayı |
| `debug` | `STRING` | Bütün uyğun obyektlərin formatlı JSON string kimi debug çıxışı |

