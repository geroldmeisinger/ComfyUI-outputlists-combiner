<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinasi OutputLists

![Kombinasi OutputLists](CombineOutputLists/CombineOutputLists.png)

(workflow ComfyUI diinclude)

Mengambil hingga 4 OutputLists dan menghasilkan setiap kombinasi dari mereka.

Contoh: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gunaké `is_output_list=True` (ditandai den kíta `𝌠`) dan akan diproses secara berurutan den node yang sesuai.

Semua list optional, dan list kosong akan diabaikan.

Secara teknis, ia menghitung *produk Kartesius* dan menghasilkan setiap kombinasi yang dibagi ke elemen-elemennya (`unzip`), sementara list kosong akan diganti den nilai `None` dan akan menghasilkan `None` di output yang sesuai.

Contoh: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `list_a` | `*` | (opsional) |
| `list_b` | `*` | (opsional) |
| `list_c` | `*` | (opsional) |
| `list_d` | `*` | (opsional) |

### Output

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai kombinasi yang sesuai den `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai kombinasi yang sesuai den `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai kombinasi yang sesuai den `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai kombinasi yang sesuai den `list_d`. |
| `index` | `INT 𝌠` | Rentang 0..count yang bisa digunakan den sebagai indeks. |
| `count` | `INT` | Jumlah total kombinasi. |

