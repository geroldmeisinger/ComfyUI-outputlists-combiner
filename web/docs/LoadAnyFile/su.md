## Mangiang File Apa Aja

![Mangiang File Apa Aja](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

Mangiang file teks atanapi biner mana énana jeung nyadiakeun énti file dina string atanapi string base64. Sélancar mangiangna dina `IMAGE`. Jeung mangiang metadata.

`filepath` nganggo annotated filepaths ComfyUI `[input]` `[output]` atanapi `[temp]`.
`filepath` ogé nganggo glob-pattern expansions `subdir/**/*.png`.
Di daptar manggunakeun python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` manggil `exiftool`, upamana énana diinstal atanapi available di `PATH`, atanapi manggunakeun `PIL.Image.info` salaku fallback.

Karena alasan keamanan, manghissun diréktori ieu aja nu diidin: `[input] [output] [temp]`.
Karena alasan kinerja, jumlah file di batasin kana: 1024.

### Inputs

| Nama | Tipe | Éksplanasin |
| --- | --- | --- |
| `filepath` | `STRING` | Base directory default kana `[input]` user-directory. Nganggo glob-pattern expansion `subdir/**/*.png`. Manggunakeun suffix ` [input]` ` [output]` atanapi ` [temp]` (ingat spasi di méméng!) pikeun nyepetkeun diréktori ComfyUI énana. |

### Outputs

| Nama | Tipe | Éksplanasin |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Énti file pikeun file teks, base64 pikeun file biner. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Data Exif tina ExifTool. Mérébutkeun `exiftool` command kana available di `PATH`. |

