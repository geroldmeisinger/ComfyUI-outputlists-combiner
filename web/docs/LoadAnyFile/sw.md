## Pakia Faili Yoyote

![Pakia Faili Yoyote](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow imejengwa)

Hupakia faili yoyote ya maandishi au data mbalimbali na kutoa yaliyomo katika faili kama string au string ya base64. Pia jaribu kupakia kama `IMAGE`. Na pia jaribu kupakia metadata yoyote.

`filepath` hukubali annotated filepaths za ComfyUI `[input]` `[output]` au `[temp]`.
`filepath` pia hukubali glob-pattern expansions `subdir/**/*.png`.
Katika msingi hutumia python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` huitumia `exiftool`, ikiwa imejengwa na kupatikana katika `PATH`, iwapo siyo hutumia `PIL.Image.info` kama fallback.

Kwa sababu za usalama tu viwango vya viwango vifuatavyo vinafanyiwa kufuatwa: `[input] [output] [temp]`.
Kwa sababu za utendaji idadi ya faili imekoma kwenda: 1024.

### Ingizo

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `filepath` | `STRING` | Mwanzo wa directory hupatikana `[input]` user-directory. Inaungana na glob-pattern expansion `subdir/**/*.png`. Tumia suffix ` [input]` ` [output]` au ` [temp]` (kumbuka nafasi ya awali!) ili kubaini directory tofauti ya ComfyUI. |

### Pato

| Jina | Aina | Maelezo |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Yaliyomo katika faili kwa faili za maandishi, base64 kwa faili za data mbalimbali. |
| `image` | `IMAGE 𝌠` | Image batch tensor. |
| `mask` | `MASK 𝌠` | Mask batch tensor. |
| `metadata` | `STRING 𝌠` | Data ya Exif kutoka kwa ExifTool. Inahitaji `exiftool` kuwa ipatikana katika `PATH`. |

