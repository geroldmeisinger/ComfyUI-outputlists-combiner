## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan OutputList dengan memisahkan rentetan dalam medan teks dengan pemisah.
`value` dan `index` menggunakan `is_output_list=True` (ditunjukkan oleh simbol `𝌠`) dan akan diproses secara berurutan oleh nod yang bersesuaian.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `separator` | `STRING` | Rentetan yang digunakan untuk memisahkan nilai medan teks. |
| `values` | `STRING` | Teks yang anda ingin pisahkan ke dalam senarai. Perhatikan bahawa rentetan dipotong daripada baris baru berakhir sebelum dipisahkan, dan setiap item juga dipotong daripada ruang putih. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `value` | `* 𝌠` | Nilai dari senarai. |
| `index` | `INT 𝌠` | Julat 0..count. Anda boleh menggunakan ini sebagai indeks. |
| `count` | `INT` | Bilangan item dalam senarai. |
| `inspect_combo` | `COMBO` | Output palsu yang boleh anda gunakan untuk menyambung ke `COMBO` dan mengisi dengan nilai-nilainya. Sambungan akan kemudian disambungkan secara automatik ke output `value`. |

