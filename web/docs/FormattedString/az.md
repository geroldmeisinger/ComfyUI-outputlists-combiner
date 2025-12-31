## Formatlı Sətir

![Formatlı Sətir](FormattedString/FormattedString.png)

(ComfyUI iş axını daxil olunub)

Yer tutucu dəyişənlər ehtiva edən sətri yaradır və onları müvafiq dəyərlərlə əvəz edir.
Daxili olaraq python `str.format()` istifadə edir, bax [Python - Format Sətiri Sintaksisi](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Sətri 2 rəqəmə yuvarlaqlaşdırmaq üçün `{a:.2f}` istifadə edə bilərsiniz.
* Comfy filename suffix `ComfyUI_00001_.png` ilə uyğunlaşdırmaq üçün 5 ədəd başlanğıc sıfırla doldurmaq üçün `{a:05d}` istifadə edə bilərsiniz.
* Əgər sətirlərin daxilində `{ }` yazmaq istəyirsinizsə (məsələn JSON-lar üçün), onları iki dəfə yazmalısınız: `{{ }}`.

Həmçinin `%date:yyyy-MM-dd hh:mm:ss%` və `%KSampler.seed%` kimi *axtarış və əvəz etmə (AƏ) sintaksisini* tətbiq edir.
Beləliklə, onu `GET-node` kimi də istifadə edə bilərsiniz.
"axtarış və əvəz etmə" əməliyyatı Javascript kontekstində baş verir və node icra edilmədən əvvəl işə salınır.

### Girişlər

| Ad | Növ | İzahat |
| --- | --- | --- |
| `fstring` | `STRING` | Yer tutucu dəyişənlər ehtiva edən sətri yaradır və onları müvafiq dəyərlərlə əvəz edir.<br>Daxili olaraq python `str.format()` istifadə edir, bax [Python - Format Sətiri Sintaksisi](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Sətri 2 rəqəmə yuvarlaqlaşdırmaq üçün `{a:.2f}` istifadə edə bilərsiniz.<br>* Comfy filename suffix `ComfyUI_00001_.png` ilə uyğunlaşdırmaq üçün 5 ədəd başlanğıc sıfırla doldurmaq üçün `{a:05d}` istifadə edə bilərsiniz.<br>* Əgər sətirlərin daxilində `{ }` yazmaq istəyirsinizsə (məsələn JSON-lar üçün), onları iki dəfə yazmalısınız: `{{ }}`.<br><br>Həmçinin `%date:yyyy-MM-dd hh:mm:ss%` və `%KSampler.seed%` kimi *axtarış və əvəz etmə (AƏ) sintaksisini* tətbiq edir.<br>Beləliklə, onu `GET-node` kimi də istifadə edə bilərsiniz.<br>"axtarış və əvəz etmə" əməliyyatı Javascript kontekstində baş verir və node icra edilmədən əvvəl işə salınır. |
| `a` | `*` | (isteğe bağlı) `{a}` yer tutucusunda sətir kimi istifadə olunacaq dəyər. |
| `b` | `*` | (isteğe bağlı) `{b}` yer tutucusunda sətir kimi istifadə olunacaq dəyər. |
| `c` | `*` | (isteğe bağlı) `{c}` yer tutucusunda sətir kimi istifadə olunacaq dəyər. |
| `d` | `*` | (isteğe bağlı) `{d}` yer tutucusunda sətir kimi istifadə olunacaq dəyər. |

### Çıxışlar

| Ad | Növ | İzahat |
| --- | --- | --- |
| `string` | `STRING` | Bütün yer tutucular müvafiq dəyərlərlə əvəz edilmiş formatlı sətir. |

