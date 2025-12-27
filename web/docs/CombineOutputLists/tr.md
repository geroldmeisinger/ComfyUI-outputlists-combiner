<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Çıktı Listelerinin Kombinasyonları

![Çıktı Listelerinin Kombinasyonları](CombineOutputLists/CombineOutputLists.png)

(ComfyUI çalışma akışı dahildir)

En fazla 4 Çıktı Listesini alır ve bunların her kombinasyonunu üretir.

Örnek: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` `is_output_list=True` kullanır (𝌠 sembolüyle gösterilir) ve karşılık gelen düğümler tarafından sırayla işlenir.

Tüm listeler isteğe bağlıdır ve boş listeler göz ardı edilir.

Teknik olarak *Kartesiyen çarpım* hesaplanır ve her kombinasyonun elemanlarına ayrılmış (unzip) hâline getirilir; boş listeler `None` ile değiştirilir ve bu durumda ilgili çıkışta `None` emit edilir.

Örnek: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Girdiler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `list_a` | `*` | (isteğe bağlı) |
| `list_b` | `*` | (isteğe bağlı) |
| `list_c` | `*` | (isteğe bağlı) |
| `list_d` | `*` | (isteğe bağlı) |

### Çıktılar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`'ya karşılık gelen kombinasyonların değerleri. |
| `unzip_b` | `* 𝌠` | `list_b`'ye karşılık gelen kombinasyonların değerleri. |
| `unzip_c` | `* 𝌠` | `list_c`'ye karşılık gelen kombinasyonların değerleri. |
| `unzip_d` | `* 𝌠` | `list_d`'ye karşılık gelen kombinasyonların değerleri. |
| `index` | `INT 𝌠` | 0..count aralığı ve bu değerler bir indekse kullanılabilir. |
| `count` | `INT` | Toplam kombinasyon sayısı. |

