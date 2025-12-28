<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Tukar kepada Integer, Float, String

![Tukar kepada Integer, Float, String](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI termasuk)

Mengubah apa pun yang berbentuk nombor kepada `INT`, `FLOAT`, `STRING`.
Menggunakan `nums_from_string.get_nums` secara dalaman yang sangat membolehkan dalam menerima nombor. Boleh menerima nombor sebenar, nombor perpuluhan sebenar, nombor atau perpuluhan dalam bentuk string, string yang mengandungi beberapa nombor dengan pemisah ribu.
Gunakan string `123;234;345` untuk dengan cepat menghasilkan senarai nombor. Jangan gunakan tanda koma sebagai pemisah kerana ia mungkin dianggap sebagai pemisah ribu.
`int`, `float` dan `string` menggunakan `is_output_list=True` (ditunjukkan dengan simbol `𝌠`) dan akan diproses secara berurutan oleh node yang sesuai.

### Input

| Nama | Jenis | Perihalan |
| --- | --- | --- |
| `any` | `*` | Apa saja yang boleh diubah kepada string dengan nombor yang boleh dibaca di dalamnya |

### Output

| Nama | Jenis | Perihalan |
| --- | --- | --- |
| `int` | `INT 𝌠` | Semua nombor yang ditemui dalam string dengan perpuluhan dipotong. |
| `float` | `FLOAT 𝌠` | Semua nombor yang ditemui dalam string sebagai perpuluhan. |
| `string` | `STRING 𝌠` | Semua nombor yang ditemui dalam string sebagai perpuluhan yang dikonversi kepada string. |
| `count` | `INT` | Jumlah nombor yang ditemui dalam nilai tersebut. |

