## Kombinasi OutputLists

![Kombinasi OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow disertakan)

Mengambil hingga 4 OutputLists dan menghasilkan setiap kombinasi dari mereka.

Contoh: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

Semua daftar bersifat opsional dan daftar kosong akan diabaikan.

Secara teknis menghitung *hasil kali kartesian* dan mengeluarkan setiap kombinasi yang dipisahkan menjadi elemen-elemennya (`unzip`), sedangkan daftar kosong akan diganti dengan unit dari `None` dan akan mengeluarkan `None` pada output yang sesuai.

Contoh: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `list_a` | `*` | (opsional) |
| `list_b` | `*` | (opsional) |
| `list_c` | `*` | (opsional) |
| `list_d` | `*` | (opsional) |

### Output

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai dari kombinasi yang sesuai dengan `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai dari kombinasi yang sesuai dengan `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai dari kombinasi yang sesuai dengan `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai dari kombinasi yang sesuai dengan `list_d`. |
| `index` | `INT 𝌠` | Rentang 0..count yang dapat digunakan sebagai indeks. |
| `count` | `INT` | Jumlah total kombinasi. |

