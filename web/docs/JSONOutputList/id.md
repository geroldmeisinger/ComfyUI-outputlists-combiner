## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow disertakan)

Membuat OutputList dengan mengekstrak array atau dictionary dari objek JSON.
Menggunakan sintaks JSONPath untuk mengekstrak nilai-nilai, lihat [JSONPath on Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Semua nilai yang cocok diubah menjadi satu daftar panjang.
Anda juga dapat menggunakan node ini untuk membuat objek dari string literal seperti `[1, 2, 3]`.
`key`, `value`, `int` dan `float` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath yang digunakan untuk mengekstrak nilai-nilai. |
| `json` | `STRING` | String JSON yang diterjemahkan ke objek. |
| `obj` | `*` | (opsional) objek dari tipe apa pun yang akan menggantikan string JSON |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kunci untuk dictionary atau indeks untuk array (sebagai string). Secara teknis ini adalah indeks global dari daftar yang diubah menjadi datar untuk semua yang bukan kunci. |
| `value` | `STRING 𝌠` | Nilai sebagai string. |
| `int` | `INT 𝌠` | Nilai sebagai int (jika tidak dapat mengurai angka, default ke 0). |
| `float` | `FLOAT 𝌠` | Nilai sebagai float (jika tidak dapat mengurai angka, default ke 0). |
| `count` | `INT` | Jumlah total item dalam daftar yang diubah menjadi datar |
| `debug` | `STRING` | Keluaran debug dari semua objek yang cocok sebagai string JSON yang diformat |

