## Rentetan Berformat

![Rentetan Berformat](FormattedString/FormattedString.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan rentetan yang mengandungi pembolehubah penempatan dan menggantikannya dengan nilai masing-masing.
Menggunakan `str.format()` python secara dalaman, lihat [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Anda boleh gunakan `{a:.2f}` untuk membulatkan float kepada 2 tempat perpuluhan.
* Anda boleh gunakan `{a:05d}` untuk mengisi sehingga 5 sifar utama untuk sepadan dengan akhiran nama fail comfys `ComfyUI_00001_.png`.
* Jika anda ingin menulis `{ }` dalam rentetan anda (cth. untuk JSONs) anda perlu mendoublenya: `{{ }}`.

Juga menerapkan sintaks *cari & ganti (C&G)* seperti `%date:yyyy-MM-dd hh:mm:ss%` dan `%KSampler.seed%`.
Oleh itu anda juga boleh gunakannya sebagai nod `GET`.
Perhatikan bahawa "cari & ganti" berlaku dalam konteks Javascript dan dijalankan sebelum eksekusi nod.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `fstring` | `STRING` | Menghasilkan rentetan yang mengandungi pembolehubah penempatan dan menggantikannya dengan nilai masing-masing.<br>Menggunakan `str.format()` python secara dalaman, lihat [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Anda boleh gunakan `{a:.2f}` untuk membulatkan float kepada 2 tempat perpuluhan.<br>* Anda boleh gunakan `{a:05d}` untuk mengisi sehingga 5 sifar utama untuk sepadan dengan akhiran nama fail comfys `ComfyUI_00001_.png`.<br>* Jika anda ingin menulis `{ }` dalam rentetan anda (cth. untuk JSONs) anda perlu mendoublenya: `{{ }}`.<br><br>Juga menerapkan sintaks *cari & ganti (C&G)* seperti `%date:yyyy-MM-dd hh:mm:ss%` dan `%KSampler.seed%`.<br>Oleh itu anda juga boleh gunakannya sebagai nod `GET`.<br>Perhatikan bahawa "cari & ganti" berlaku dalam konteks Javascript dan dijalankan sebelum eksekusi nod. |
| `a` | `*` | (pilihan) nilai yang akan menjadi rentetan pada penempatan `{a}`. |
| `b` | `*` | (pilihan) nilai yang akan menjadi rentetan pada penempatan `{b}`. |
| `c` | `*` | (pilihan) nilai yang akan menjadi rentetan pada penempatan `{c}`. |
| `d` | `*` | (pilihan) nilai yang akan menjadi rentetan pada penempatan `{d}`. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `string` | `STRING` | Rentetan berformat dengan semua penempatan digantikan dengan nilai masing-masing. |

