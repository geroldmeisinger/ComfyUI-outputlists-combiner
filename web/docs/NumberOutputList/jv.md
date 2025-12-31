## OutputList Angka

![OutputList Angka](NumberOutputList/NumberOutputList.png)

(Workflow ComfyUI kalebu)

Nggawé OutputList kanthi jarak nilai angka.
Nggunakaké [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) ing ngisoré, amarga iki luwih andal karo nilai floating-point.
Yen sampeyan pengin nyebutake daptar angka karo langkah semaing uga deleng JSON OutputList lan nyebutake array, contone `[1, 42, 123]`.
`int`, `float`, `string` lan `index` nggunakaké `is_output_list=True` (indikasi dening simbol `𝌠`) lan bakal diprosés kanthi urutan dening node sing padha.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `start` | `FLOAT` | Nilai mulai kanggo nggawé jarak saka. |
| `stop` | `FLOAT` | Nilai pungkasan. Yen `endpoint=include` masing-masing angka iki dimasukaké ing daptar. |
| `num` | `INT` | Jumlah item ing daptar (jangan sampeyan pusingaké karo `step`). |
| `endpoint` | `BOOLEAN` | Nggawé pilihan yen nilai `stop` kudu dimasukaké utawa dikelupaké ing item. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Nilai sing diowahi menyang int (dibulataké munggung/floored). |
| `float` | `FLOAT 𝌠` | Nilai minangka float. |
| `string` | `STRING 𝌠` | Nilai minangka float sing diowahi menyang string. |
| `index` | `INT 𝌠` | Jarak 0..count sing bisa digunakaké minangka index. |
| `count` | `INT` | Same as `num`. |

