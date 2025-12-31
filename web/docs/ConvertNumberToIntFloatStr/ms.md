## Tukar Ke Int Float Str

![Tukar Ke Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Aliran kerja ComfyUI disertakan)

Menukar apa-apa yang seperti nombor kepada `INT` `FLOAT` `STRING`.
Menggunakan `nums_from_string.get_nums` secara dalaman yang sangat murah untuk nombor yang diterimanya. Apa-apa sahaja dari integer sebenar, float sebenar, integer atau float sebagai rentetan, rentetan yang mengandungi beberapa nombor dengan pemisah ribuan.
Guna rentetan `123;234;345` untuk menjana senarai nombor dengan cepat. Jangan gunakan koma sebagai pemisah kerana ia boleh ditafsirkan sebagai pemisah ribuan.
`int`, `float` dan `string` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh nod yang bersesuaian.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `any` | `*` | Apa-apa sahaja yang boleh ditukar kepada rentetan dengan nombor yang boleh dihuraikan |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `int` | `INT 𝌠` | Semua nombor yang ditemui dalam rentetan dengan perpuluhan dipotong. |
| `float` | `FLOAT 𝌠` | Semua nombor yang ditemui dalam rentetan sebagai float. |
| `string` | `STRING 𝌠` | Semua nombor yang ditemui dalam rentetan sebagai float ditukar kepada rentetan. |
| `count` | `INT` | Jumlah nombor yang ditemui dalam nilai tersebut. |

