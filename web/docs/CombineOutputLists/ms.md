## Kombinasi OutputLists

![Kombinasi OutputLists](CombineOutputLists/CombineOutputLists.png)

(Aliran kerja ComfyUI disertakan)

Mengambil sehingga 4 OutputLists dan menghasilkan setiap kombinasi daripadanya.

Contoh: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berturut-turut oleh node yang bersesuaian.

Semua senarai adalah pilihan dan senarai kosong akan diabaikan.

Secara teknikal ia mengira *hasil darab Cartesius* dan mengeluarkan setiap kombinasi yang dipisahkan kepada elemen-elemennya (`unzip`), manakala senarai kosong akan digantikan dengan unit `None` dan mereka akan mengeluarkan `None` pada output yang bersesuaian.

Contoh: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `list_a` | `*` | (pilihan) |
| `list_b` | `*` | (pilihan) |
| `list_c` | `*` | (pilihan) |
| `list_d` | `*` | (pilihan) |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai kombinasi yang bersesuaian dengan `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai kombinasi yang bersesuaian dengan `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai kombinasi yang bersesuaian dengan `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai kombinasi yang bersesuaian dengan `list_d`. |
| `index` | `INT 𝌠` | Julat 0..count yang boleh digunakan sebagai indeks. |
| `count` | `INT` | Jumlah total kombinasi. |

