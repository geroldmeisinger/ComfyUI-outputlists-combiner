## Muat Sebarang Fail

![Muat Sebarang Fail](LoadAnyFile/LoadAnyFile.png)

(Aliran kerja ComfyUI disertakan)

Memuat sebarang fail teks atau binari dan menyediakan kandungan fail sebagai rentetan atau rentetan base64. Tambahan pula cuba memuatnya sebagai `IMAGE`. Dan juga cuba memuat sebarang metadata.

`filepath` menyokong laluan fail yang diberi anotasi oleh ComfyUI `[input]` `[output]` atau `[temp]`.
`filepath` juga menyokong pengembangan corak glob `subdir/**/*.png`.
Secara dalaman menggunakan [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) daripada python.

`metadata` memanggil `exiftool`, jika ia dipasang dan tersedia di `PATH`, jika tidak menggunakan `PIL.Image.info` sebagai fallback.

Untuk alasan keselamatan hanya direktori berikut yang disokong: `[input] [output] [temp]`.
Untuk alasan prestasi bilangan fail dibataskan kepada: 1024.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `filepath` | `STRING` | Direktori asas lalai kepada direktori pengguna `[input]`. Menyokong pengembangan corak glob `subdir/**/*.png`. Gunakan akhiran ` [input]` ` [output]` atau ` [temp]` (perhatikan ruang pemimpin!) untuk menentukan direktori pengguna ComfyUI yang berbeza. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Kandungan fail untuk fail teks, base64 untuk fail binari. |
| `image` | `IMAGE 𝌠` | Tensor batch imej. |
| `mask` | `MASK 𝌠` | Tensor batch topeng. |
| `metadata` | `STRING 𝌠` | Data Exif daripada ExifTool. Memerlukan perintah `exiftool` untuk tersedia di `PATH`. |

