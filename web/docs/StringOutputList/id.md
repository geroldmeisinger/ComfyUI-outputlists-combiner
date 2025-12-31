## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow disertakan)

Membuat OutputList dengan membagi string dalam textfield dengan pemisah.
`value` dan `index` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `separator` | `STRING` | String yang digunakan untuk membagi nilai textfield. |
| `values` | `STRING` | Teks yang ingin Anda bagi menjadi daftar. Perhatikan bahwa string dipotong dari baris baru trailing sebelum membagi, dan setiap item juga dipotong dari whitespace. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `value` | `* 𝌠` | Nilai dari daftar. |
| `index` | `INT 𝌠` | Rentang 0..count. Anda dapat menggunakan ini sebagai indeks. |
| `count` | `INT` | Jumlah item dalam daftar. |
| `inspect_combo` | `COMBO` | Output dummy yang dapat Anda gunakan untuk menghubungkan ke `COMBO` dan mengisi dengan nilainya. Koneksi kemudian akan secara otomatis dihubungkan ulang ke output `value`. |

