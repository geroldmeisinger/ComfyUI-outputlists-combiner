## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow dahil)

Metin alanındaki string'i bir ayırıcı ile ayırarak bir OutputList oluşturur.
`value` ve `index` kullanımları `is_output_list=True` değerini kullanır (sembol `𝌠` ile gösterilir) ve ilgili düğümler tarafından sıralı olarak işlenir.

### Girişler

| Ad | Tip | Açıklama |
| --- | --- | --- |
| `separator` | `STRING` | Metin alanındaki değerleri bölmek için kullanılan string. |
| `values` | `STRING` | Listeye bölünmesini istediğiniz metin. String, bölmeden önce sondaki yeni satır karakterleri kaldırılır ve her bir öğe tekrar boşluk karakterlerinden arındırılır. |

### Çıkışlar

| Ad | Tip | Açıklama |
| --- | --- | --- |
| `value` | `* 𝌠` | Liste öğelerinden gelen değerler. |
| `index` | `INT 𝌠` | 0..count aralığı. Bir indeks olarak kullanabilirsiniz. |
| `count` | `INT` | Liste içindeki öğe sayısı. |
| `inspect_combo` | `COMBO` | Bir `COMBO` bağlantısı yapmak ve değerleri ile önceden doldurmak için kullanabileceğiniz sahte bir çıkış. Bağlantı otomatik olarak `value` çıkışına yeniden bağlanır. |

