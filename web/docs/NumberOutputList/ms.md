## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan OutputList dengan julat nilai numerik.
Menggunakan [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) secara dalaman, kerana ia berfungsi lebih boleh dipercayai dengan nilai titik terapung.
Jika anda ingin menentukan senarai nombor dengan langkah arbitrer, sila semak JSON OutputList dan tentukan array, contohnya `[1, 42, 123]`.
`int`, `float`, `string` dan `index` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh nod yang bersesuaian.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `start` | `FLOAT` | Nilai mula untuk menjana julat dari. |
| `stop` | `FLOAT` | Nilai tamat. Jika `endpoint=include` maka nombor ini dimasukkan ke dalam senarai. |
| `num` | `INT` | Bilangan item dalam senarai (jangan kelirukan dengan `step`). |
| `endpoint` | `BOOLEAN` | Menentukan sama ada nilai `stop` harus dimasukkan atau dikecualikan dalam item. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `int` | `INT 𝌠` | Nilai yang ditukar kepada int (dibuang ke bawah/dibulatkan). |
| `float` | `FLOAT 𝌠` | Nilai sebagai float. |
| `string` | `STRING 𝌠` | Nilai sebagai float ditukar kepada rentetan. |
| `index` | `INT 𝌠` | Julat 0..count yang boleh digunakan sebagai indeks. |
| `count` | `INT` | Sama seperti `num`. |

