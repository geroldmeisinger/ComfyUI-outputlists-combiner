## OutputLists Kombinasyonları

![OutputLists Kombinasyonları](CombineOutputLists/CombineOutputLists.png)

(ComfyUI iş akışı dahil)

En fazla 4 OutputList alır ve bunların tüm kombinasyonlarını oluşturur.

Örnek: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` kullanır `is_output_list=True` (sembol `𝌠` ile gösterilir) ve karşılık gelen düğümler tarafından sıralı olarak işlenir.

Tüm listeler isteğe bağlıdır ve boş listeler yok sayılır.

Teknik olarak *Kartezyen çarpımı* hesaplar ve her kombinasyonu elemanlarına ayrılarak (`unzip`) çıktı verir. Boş listeler `None` birimleriyle değiştirilir ve ilgili çıkışlarda `None` yayarlar.

Örnek: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Girişler

| İsim | Tür | Açıklama |
| --- | --- | --- |
| `list_a` | `*` | (isteğe bağlı) |
| `list_b` | `*` | (isteğe bağlı) |
| `list_c` | `*` | (isteğe bağlı) |
| `list_d` | `*` | (isteğe bağlı) |

### Çıkışlar

| İsim | Tür | Açıklama |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | `list_a`'ya karşılık gelen kombinasyonların değeri. |
| `unzip_b` | `* 𝌠` | `list_b`'ye karşılık gelen kombinasyonların değeri. |
| `unzip_c` | `* 𝌠` | `list_c`'ye karşılık gelen kombinasyonların değeri. |
| `unzip_d` | `* 𝌠` | `list_d`'ye karşılık gelen kombinasyonların değeri. |
| `index` | `INT 𝌠` | Bir dizin olarak kullanılabilen 0..count aralığı. |
| `count` | `INT` | Toplam kombinasyon sayısı. |

