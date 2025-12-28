<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Sayıya Dönüştürme: Tam Sayı, Ondalıklı Sayı, Dize

![Sayıya Dönüştürme: Tam Sayı, Ondalıklı Sayı, Dize](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI çalıştırma akışı dahil edilmiştir)

Herhangi bir sayıya benzer şeyi `INT`, `FLOAT`, `STRING` olarak dönüştürür.
İçerisinde `nums_from_string.get_nums` kullanır, bu, kabul edilen sayılar açısından çok esnek bir yapıya sahiptir. Gerçek tam sayılar, gerçek ondalıklı sayılar, tam sayılar ya da ondalıklı sayılar olarak dize, birden fazla sayı içeren dize ile binlik ayırıcıları olan dizeri de dahil eder.
Bir dize `123;234;345` kullanarak sayı listesi oluşturabilirsiniz. Binlik ayırıcıları olarak virgül kullanmayın çünkü bunlar binlik ayırıcıları olarak yorumlanabilir.
`int`, `float` ve `string` çıkışları `is_output_list=True` (sembol `𝌠` ile gösterilir) kullanır ve ilgili düğümler tarafından sırayla işlenir.

### Girdi

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `any` | `*` | Dışarıya çıkarılabilir bir dizeye dönüştürülebilen her şey, içine parse edilebilecek sayılar varsa |

### Çıktılar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `int` | `INT 𝌠` | Dize içinde bulunan tüm sayılar, ondalık kısmı kesilerek elde edilir. |
| `float` | `FLOAT 𝌠` | Dize içinde bulunan tüm sayılar ondalıklı olarak elde edilir. |
| `string` | `STRING 𝌠` | Dize içinde bulunan tüm sayılar ondalıklı olarak elde edilip dizeye dönüştürülür. |
| `count` | `INT` | Değer içinde bulunan sayıların sayısı. |

