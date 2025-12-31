## Muat File Apa Waèh

![Muat File Apa Waèh](LoadAnyFile/LoadAnyFile.png)

(Workflow ComfyUI kalebu)

Nggawé file teks utawa biner apa waèh lan nyedhiyakaké isi file minangka string utawa string base64. Lan uga nyoba nglmuat iki minangka `IMAGE`. Lan uga nyoba nglmuat metadata apa waèh.

`filepath` nggawé ComfyUI's annotated filepaths `[input]` `[output]` utawa `[temp]`.
`filepath` uga nggawé glob-pattern expansions `subdir/**/*.png`.
Ing ngisoré nggunakaké python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` nggunakaké `exiftool`, yen wis diinstal lan kasedhiya ing `PATH`, otherwise nggunakaké `PIL.Image.info` minangka fallback.

Kanthi alasan keselamatan mung direktori ing ngisoré sing didhukung: `[input] [output] [temp]`.
Kanthi alasan kinerja jumlah file dibatesi menyang: 1024.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `filepath` | `STRING` | Direktori dasar nggawé `[input]` direktori pangguna. Nggunakaké glob-pattern expansion `subdir/**/*.png`. Nggunakaké sufiks ` [input]` ` [output]` utawa ` [temp]` (dheweke ngandhaké spasi munggung!) supaya nyebutake direktori pangguna ComfyUI sing beda. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Isi file kanggo file teks, base64 kanggo file biner. |
| `image` | `IMAGE 𝌠` | Tensor batch gambar. |
| `mask` | `MASK 𝌠` | Tensor batch mask. |
| `metadata` | `STRING 𝌠` | Data Exif saka ExifTool. Mbutuhaké command `exiftool` supaya kasedhiya ing `PATH`. |

