## String Berformat

![Formatted String](FormattedString/FormattedString.png)

(ComfyUI workflow disertakan)

Membuat string yang mengandung variabel placeholder dan menggantinya dengan nilai masing-masing.
Menggunakan `str.format()` python secara internal, lihat [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Anda dapat menggunakan `{a:.2f}` untuk membulatkan float menjadi 2 desimal.
* Anda dapat menggunakan `{a:05d}` untuk mengisi hingga 5 nol di depan untuk sesuai dengan sufiks nama file comfys `ComfyUI_00001_.png`.
* Jika Anda ingin menulis `{ }` dalam string Anda (misalnya untuk JSON), Anda harus menggandakannya: `{{ }}`.

Juga menerapkan sintaks *search & replace (S&R)* seperti `%date:yyyy-MM-dd hh:mm:ss%` dan `%KSampler.seed%`.
Dengan demikian Anda juga dapat menggunakannya sebagai node `GET`.
Perhatikan bahwa "search & replace" terjadi dalam konteks Javascript dan dijalankan sebelum eksekusi node.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `fstring` | `STRING` | Membuat string yang mengandung variabel placeholder dan menggantinya dengan nilai masing-masing.<br>Menggunakan `str.format()` python secara internal, lihat [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Anda dapat menggunakan `{a:.2f}` untuk membulatkan float menjadi 2 desimal.<br>* Anda dapat menggunakan `{a:05d}` untuk mengisi hingga 5 nol di depan untuk sesuai dengan sufiks nama file comfys `ComfyUI_00001_.png`.<br>* Jika Anda ingin menulis `{ }` dalam string Anda (misalnya untuk JSON), Anda harus menggandakannya: `{{ }}`.<br><br>Juga menerapkan sintaks *search & replace (S&R)* seperti `%date:yyyy-MM-dd hh:mm:ss%` dan `%KSampler.seed%`.<br>Dengan demikian Anda juga dapat menggunakannya sebagai node `GET`.<br>Perhatikan bahwa "search & replace" terjadi dalam konteks Javascript dan dijalankan sebelum eksekusi node. |
| `a` | `*` | (opsional) nilai yang akan menjadi string pada placeholder `{a}`. |
| `b` | `*` | (opsional) nilai yang akan menjadi string pada placeholder `{b}`. |
| `c` | `*` | (opsional) nilai yang akan menjadi string pada placeholder `{c}`. |
| `d` | `*` | (opsional) nilai yang akan menjadi string pada placeholder `{d}`. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `string` | `STRING` | String yang diformat dengan semua placeholder diganti dengan nilai masing-masing. |

