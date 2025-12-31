## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow dahil)

JSON nesnelerinden dizileri veya sözlükleri ayıklayarak bir OutputList oluşturur.
Değerleri ayıklamak için JSONPath sözdizimini kullanır, bkz. [JSONPath Wikipedia'da](https://en.wikipedia.org/wiki/JSONPath) .
Eşleşen tüm değerler tek uzun bir listeye düzleştirilir.
Ayrıca `[1, 2, 3]` gibi literal dizgilerden nesneler oluşturmak için bu düğümü de kullanabilirsiniz.
`key`, `value`, `int` ve `float`, `is_output_list=True` kullanır (simge `𝌠` ile belirtilir) ve karşılık gelen düğümler tarafından sıralı olarak işlenir.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `jsonpath` | `STRING` | Değerleri ayıklamak için kullanılan JSONPath. |
| `json` | `STRING` | Bir nesneye çevrilen JSON dizgesi. |
| `obj` | `*` | (isteğe bağlı) JSON dizgesini değiştirecek herhangi bir türde nesne |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Sözlükler için anahtar veya diziler için indeks (dizge olarak). Teknik olarak, tüm anahtar olmayanlar için düzleştirilmiş listenin küresel indeksidir. |
| `value` | `STRING 𝌠` | Değer dizge olarak. |
| `int` | `INT 𝌠` | Değer tamsayı olarak (sayı ayrıştırılamazsa, öntanımlı 0 olur). |
| `float` | `FLOAT 𝌠` | Değer ondalık sayı olarak (sayı ayrıştırılamazsa, öntanımlı 0 olur). |
| `count` | `INT` | Düzleştirilmiş listedeki toplam madde sayısı |
| `debug` | `STRING` | Eşleşen tüm nesnelerin biçimlendirilmiş JSON dizgesi olarak hata ayıklama çıktısı |

