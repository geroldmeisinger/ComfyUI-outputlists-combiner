## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow disertakan)

Membuat OutputList dengan rentang nilai numerik.
Menggunakan [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) secara internal, karena ini bekerja lebih andal dengan nilai floating-point.
Jika Anda ingin mendefinisikan daftar angka dengan langkah sembarang, lihat JSON OutputList dan definisikan sebuah array, misalnya `[1, 42, 123]`.
`int`, `float`, `string` dan `index` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `start` | `FLOAT` | Nilai awal untuk menghasilkan rentang dari. |
| `stop` | `FLOAT` | Nilai akhir. Jika `endpoint=include` maka angka ini disertakan dalam daftar. |
| `num` | `INT` | Jumlah item dalam daftar (jangan confus dengan `step`). |
| `endpoint` | `BOOLEAN` | Menentukan apakah nilai `stop` harus disertakan atau dikecualikan dalam item. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `int` | `INT 𝌠` | Nilai yang dikonversi ke int (dibulatkan ke bawah/dibawah). |
| `float` | `FLOAT 𝌠` | Nilai sebagai float. |
| `string` | `STRING 𝌠` | Nilai sebagai float dikonversi ke string. |
| `index` | `INT 𝌠` | Rentang 0..count yang dapat digunakan sebagai indeks. |
| `count` | `INT` | Sama dengan `num`. |

