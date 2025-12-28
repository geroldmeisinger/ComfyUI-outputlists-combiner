<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konversi Menjadi Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(workflow ComfyUI termasuk)

Mengubah apa pun yang mirip dengan angka menjadi `INT` `FLOAT` `STRING`.
Menggunakan `nums_from_string.get_nums` secara internal yang sangat mengizinkan dalam angka yang diterimanya. Apapun dari bilangan bulat sebenarnya, bilangan desimal sebenarnya, bilangan bulat atau desimal sebagai string, string yang mengandung beberapa angka dengan pemisah ribuan.
Gunakan string `123;234;345` untuk dengan cepat menghasilkan daftar angka. Jangan gunakan koma sebagai pemisah karena mereka mungkin dianggap sebagai pemisah ribuan.
`int`, `float` dan `string` menggunakan `is_output_list=True` (ditandai dengan simbol `𝌠`) dan akan diproses secara berurutan oleh node yang sesuai.

### Input

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `any` | `*` | Apa pun yang dapat diubah secara bermakna menjadi string dengan angka yang dapat dibaca di dalamnya |

### Output

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `int` | `INT 𝌠` | Semua angka yang ditemukan dalam string dengan desimal yang dipotong. |
| `float` | `FLOAT 𝌠` | Semua angka yang ditemukan dalam string sebagai bilangan desimal. |
| `string` | `STRING 𝌠` | Semua angka yang ditemukan dalam string sebagai bilangan desimal yang dikonversi ke string. |
| `count` | `INT` | Jumlah angka yang ditemukan dalam nilai tersebut. |

