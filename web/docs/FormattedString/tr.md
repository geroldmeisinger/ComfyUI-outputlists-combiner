## Formatlı Dize

![Formatlı Dize](FormattedString/FormattedString.png)

(ComfyUI iş akışı dahil)

Yer tutucu değişkenler içeren bir dize oluşturur ve bunları karşılık gelen değerlerle değiştirir.
İçeriksel olarak Python `str.format()` fonksiyonunu kullanır, bkz. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Bir float sayıyı 2 ondalık basamağa yuvarlamak için `{a:.2f}` kullanabilirsiniz.
* Comfy'nin dosya adı son ekine uyum sağlamak için 5 basamaklı başındaki sıfırları doldurmak için `{a:05d}` kullanabilirsiniz `ComfyUI_00001_.png`.
* Dizeleriniz içinde `{ }` karakterleri yazmak istiyorsanız (örneğin JSON'lar için) bunları iki kez yazmalısınız: `{{ }}`.

Ayrıca `%date:yyyy-MM-dd hh:mm:ss%` ve `%KSampler.seed%` gibi *arama ve değiştirme (S&R)* sözdizimini de uygular.
Bu nedenle aynı zamanda bir `GET-node` olarak da kullanılabilir.
"Not: "arama ve değiştirme" işlemi Javascript bağlamında gerçekleşir ve düğüm çalışmadan önce çalıştırılır.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `fstring` | `STRING` | Yer tutucu değişkenler içeren bir dize oluşturur ve bunları karşılık gelen değerlerle değiştirir.<br>İçeriksel olarak Python `str.format()` fonksiyonunu kullanır, bkz. [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Bir float sayıyı 2 ondalık basamağa yuvarlamak için `{a:.2f}` kullanabilirsiniz.<br>* Comfy'nin dosya adı son ekine uyum sağlamak için 5 basamaklı başındaki sıfırları doldurmak için `{a:05d}` kullanabilirsiniz `ComfyUI_00001_.png`.<br>* Dizeleriniz içinde `{ }` karakterleri yazmak istiyorsanız (örneğin JSON'lar için) bunları iki kez yazmalısınız: `{{ }}`.<br><br>Ayrıca `%date:yyyy-MM-dd hh:mm:ss%` ve `%KSampler.seed%` gibi *arama ve değiştirme (S&R)* sözdizimini de uygular.<br>Bu nedenle aynı zamanda bir `GET-node` olarak da kullanılabilir.<br>Not: "arama ve değiştirme" işlemi Javascript bağlamında gerçekleşir ve düğüm çalışmadan önce çalıştırılır. |
| `a` | `*` | (isteğe bağlı) `{a}` yer tutucusunda bir dize olarak kullanılacak değer. |
| `b` | `*` | (isteğe bağlı) `{b}` yer tutucusunda bir dize olarak kullanılacak değer. |
| `c` | `*` | (isteğe bağlı) `{c}` yer tutucusunda bir dize olarak kullanılacak değer. |
| `d` | `*` | (isteğe bağlı) `{d}` yer tutucusunda bir dize olarak kullanılacak değer. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `string` | `STRING` | Tüm yer tutucuların karşılık gelen değerlerle değiştirildiği formatlı dize. |

