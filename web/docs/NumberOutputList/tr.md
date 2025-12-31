## Sayı Çıktı Listesi

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI iş akışı dahil)

Sayısal değerlerin bir aralığıyla bir ÇıktıListesi oluşturur.
Nokta değerleriyle daha güvenilir çalıştığı için içsel olarak [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) kullanır.
İsterseniz rastgele adımlarla sayı listeleri tanımlamak için JSON OutputList'e bakın ve bir dizi tanımlayın, örneğin `[1, 42, 123]`.
`int`, `float`, `string` ve `index`, `is_output_list=True` kullanır ( `𝌠` sembolü ile belirtilir) ve karşılık gelen düğümler tarafından sırayla işlenir.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `start` | `FLOAT` | Aralığı oluşturmak için başlangıç değeri. |
| `stop` | `FLOAT` | Bitiş değeri. `endpoint=include` ise bu sayı liste içinde yer alır. |
| `num` | `INT` | Liste içindeki öğe sayısı (`step` ile karıştırmayın). |
| `endpoint` | `BOOLEAN` | `stop` değerinin öğelerde dahil edilip edilmeyeceğine karar verir. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `int` | `INT 𝌠` | Değer int'e dönüştürüldü (aşağı yuvarlandı). |
| `float` | `FLOAT 𝌠` | Değer float olarak. |
| `string` | `STRING 𝌠` | Değer float olarak string'e dönüştürüldü. |
| `index` | `INT 𝌠` | 0..count aralığındaki indeks olarak kullanılabilir. |
| `count` | `INT` | `num` ile aynı. |

