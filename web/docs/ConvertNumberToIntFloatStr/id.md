## Konversi Menjadi Int Float Str

![Convert To Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow disertakan)

Mengonversi apapun yang mirip angka menjadi `INT` `FLOAT` `STRING`.
Menggunakan `nums_from_string.get_nums` secara internal yang sangat permissive dalam angka-angka yang diterimanya. Apa pun dari integer sebenarnya, float sebenarnya, integer atau float sebagai string, string yang mengandung beberapa angka dengan pemisah ribuan.
Gunakan string `123;234;345` untuk dengan cepat menghasilkan daftar angka. Jangan gunakan koma sebagai pemisah karena mereka mungkin diinterpretasikan sebagai pemisah ribuan.
`int`, `float` dan `string` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh node-node yang sesuai.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `any` | `*` | Apapun yang dapat dikonversi secara bermakna menjadi string dengan angka-angka yang dapat diuraikan |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `int` | `INT 𝌠` | Semua angka yang ditemukan dalam string dengan desimal dipotong. |
| `float` | `FLOAT 𝌠` | Semua angka yang ditemukan dalam string sebagai float. |
| `string` | `STRING 𝌠` | Semua angka yang ditemukan dalam string sebagai float dikonversi ke string. |
| `count` | `INT` | Jumlah angka yang ditemukan dalam nilai tersebut. |

