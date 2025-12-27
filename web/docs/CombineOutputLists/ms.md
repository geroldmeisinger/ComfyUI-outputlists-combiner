<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Gabungan OutputLists

![Gabungan OutputLists](CombineOutputLists/CombineOutputLists.png)

(kerja dalam ComfyUI workflow)

Mengambil hingga 4 OutputLists dan menghasilkan setiap kombinasi darinya.

Contoh: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` hingga `unzip_d` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node yang sesuai.

Semua senarai adalah opsional dan senarai kosong akan diabaikan.

Secara teknis, ia menghitung *hasil kali Cartesius* dan mengeluarkan setiap kombinasi yang dibagi ke dalam elemennya (`unzip`), sementara senarai kosong akan diganti dengan nilai `None` dan akan mengeluarkan `None` pada keluaran yang sesuai.

Contoh: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Nama | Jenis | Perihalan |
| --- | --- | --- |
| `list_a` | `*` | (opsional) |
| `list_b` | `*` | (opsional) |
| `list_c` | `*` | (opsional) |
| `list_d` | `*` | (opsional) |

### Output

| Nama | Jenis | Perihalan |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai kombinasi yang sesuai dengan `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai kombinasi yang sesuai dengan `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai kombinasi yang sesuai dengan `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai kombinasi yang sesuai dengan `list_d`. |
| `index` | `INT 𝌠` | Range 0..count yang boleh digunakan sebagai indeks. |
| `count` | `INT` | Jumlah gabungan keseluruhan. |

