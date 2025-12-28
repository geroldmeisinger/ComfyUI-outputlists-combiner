<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konversi ke Int, Float, String

![Konversi ke Int, Float, String](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(workflow ComfyUI termasuk)

Mengubah segala sesuatu yang mirip angka menjadi `INT`, `FLOAT`, dan `STRING`.
Menggunakan `nums_from_string.get_nums` secara internal yang sangat mengizinkan dalam angka yang diterimanya. Angka dari bilangan bulat, bilangan desimal, bilangan bulat atau desimal dalam bentuk string, string yang mengandung beberapa angka dengan pemisah ribuan.
Gunakan string `123;234;345` untuk dengan cepat menghasilkan daftar angka. Jangan gunakan koma sebagai pemisah karena koma bisa dianggap sebagai pemisah ribuan.
`int`, `float`, dan `string` menggunakan `is_output_list=True` (ditandai dengan simbol `𝌠`) dan akan diproses secara berurutan oleh node yang sesuai.

### Input

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `any` | `*` | Apapun yang dapat diubah secara bermakna menjadi string dengan angka yang dapat dibaca di dalamnya |

### Output

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `int` | `INT 𝌠` | Semua angka yang ditemukan dalam string dengan desimal dibulatkan. |
| `float` | `FLOAT 𝌠` | Semua angka yang ditemukan dalam string dalam bentuk desimal. |
| `string` | `STRING 𝌠` | Semua angka yang ditemukan dalam string dalam bentuk desimal yang dikonversi menjadi string. |
| `count` | `INT` | Jumlah angka yang ditemukan dalam nilai tersebut. |

