## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan OutputList dengan mengekstrak array atau kamus daripada objek JSON.
Menggunakan sintaks JSONPath untuk mengekstrak nilai, lihat [JSONPath di Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Semua nilai yang sepadan akan dijalurkan menjadi satu senarai panjang.
Anda juga boleh gunakan nod ini untuk mencipta objek daripada rentetan harfiah seperti `[1, 2, 3]`.
`key`, `value`, `int` dan `float` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh nod yang bersesuaian.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath digunakan untuk mengekstrak nilai. |
| `json` | `STRING` | Rentetan JSON yang diterjemahkan kepada objek. |
| `obj` | `*` | (pilihan) objek mana-mana jenis yang akan menggantikan rentetan JSON |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kunci untuk kamus atau indeks untuk array (sebagai rentetan). Secara teknikal ia adalah indeks global senarai yang dijalurkan untuk semua bukan kunci. |
| `value` | `STRING 𝌠` | Nilai sebagai rentetan. |
| `int` | `INT 𝌠` | Nilai sebagai int (jika tidak dapat menghuraikan nombor, lalai kepada 0). |
| `float` | `FLOAT 𝌠` | Nilai sebagai float (jika tidak dapat menghuraikan nombor, lalai kepada 0). |
| `count` | `INT` | Jumlah item dalam senarai yang dijalurkan |
| `debug` | `STRING` | Output debug semua objek yang sepadan sebagai rentetan JSON yang berformat |

