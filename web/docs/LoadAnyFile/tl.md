## Mag-load ng Anumang File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(Include ang ComfyUI workflow)

Nagloload ng anumang text o binary file at nagbibigay ng laman ng file bilang string o base64 string. Karagdagang sinusubukan i-load ito bilang `IMAGE`. At sinusubukan ding i-load ang anumang metadata.

Ang `filepath` ay sumusuporta sa mga annotated filepaths ni ComfyUI `[input]` `[output]` o `[temp]`.
Ang `filepath` ay sumusuporta din sa glob-pattern expansions `subdir/**/*.png`.
Sa loob ng system gamit ang python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

Ang `metadata` ay tumatawag sa `exiftool`, kung ito ay naka-install at magagamit sa `PATH`, kung hindi gagamitin ang `PIL.Image.info` bilang fallback.

Para sa mga kadahilanang pangseguridad, sumusuportahan lamang ang mga sumusunod na direktoryo: `[input] [output] [temp]`.
Para sa mga kadahilanang pang-performance, limitado ang bilang ng mga file sa: 1024.

### Mga Input

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `filepath` | `STRING` | Ang base directory ay default sa `[input]` user-directory. Sumusuporta sa glob-pattern expansion `subdir/**/*.png`. Gamitin ang suffix ` [input]` ` [output]` o ` [temp]` (tandaan ang leading whitespace!) para tukuyin ang ibang ComfyUI user-directory. |

### Mga Output

| Pangalan | Uri | Paglalarawan |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Laman ng file para sa text files, base64 para sa binary files. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Exif data mula sa ExifTool. Kinakailangan ang `exiftool` command na magagamit sa `PATH`. |

