## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow disertakan)

Memuat file teks atau biner apa pun dan menyediakan konten file sebagai string atau string base64. Selain itu mencoba memuatnya sebagai `IMAGE`. Dan juga mencoba memuat metadata apa pun.

`filepath` mendukung annotated filepaths ComfyUI `[input]` `[output]` atau `[temp]`.
`filepath` juga mendukung ekspansi pola glob `subdir/**/*.png`.
Secara internal menggunakan [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) dari python.

`metadata` memanggil `exiftool`, jika terinstal dan tersedia di `PATH`, jika tidak menggunakan `PIL.Image.info` sebagai fallback.

Untuk alasan keamanan hanya direktori berikut yang didukung: `[input] [output] [temp]`.
Untuk alasan kinerja jumlah file dibatasi hingga: 1024.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `filepath` | `STRING` | Direktori dasar default ke direktori pengguna `[input]`. Mendukung ekspansi pola glob `subdir/**/*.png`. Gunakan suffix ` [input]` ` [output]` atau ` [temp]` (perhatikan spasi awal!) untuk menentukan direktori pengguna ComfyUI yang berbeda. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Konten file untuk file teks, base64 untuk file biner. |
| `image` | `IMAGE 𝌠` | Tensor batch gambar. |
| `mask` | `MASK 𝌠` | Tensor batch mask. |
| `metadata` | `STRING 𝌠` | Data Exif dari ExifTool. Memerlukan perintah `exiftool` untuk tersedia di `PATH`. |

