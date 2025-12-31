## Fitxategi Edonoiz Kargatu

![Fitxategi Edonoiz Kargatu](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow included)

Testu edo bitarren fitxategi edonoi kargatzen ditu eta fitxategiaren edukia kate edo base64 kate bezala ematen du. Gainera, `IMAGE` bezala kargatzen saiatzen da. Hala ere, metadata edukien kargatzen saiatzen da.

`filepath`-ek ComfyUI-ren fitxategi-bide-izen anotatuak onartzen ditu: `[input]` `[output]` edo `[temp]`.
`filepath`-ek ere glob-patrroi hedapena onartzen du: `subdir/**/*.png`.
Barnean python-en [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) erabiltzen du.

`metadata` `exiftool` deitzen du, instalatuta eta `PATH`-ean erabilgarri badago, bestela `PIL.Image.info` erabiltzen du fallback bezala.

Segurtasun arrazoiengatik onartutako direktorioak hauek dira: `[input] [output] [temp]`.
Errendimendu arrazoiengatik fitxategi kopurua mugatuta dago: 1024.

### Sarrerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `filepath` | `STRING` | Oinarrizko direktorioa `[input]` erabiltzaile-direktorioa da lehentsi bezala. Glob-patrroi hedapena onartzen du: `subdir/**/*.png`. Erabili ` [input]` ` [output]` edo ` [temp]` atzizkia (zuriunea hasieran!) beste ComfyUI erabiltzaile-direktorio bat zehazteko. |

### Irteerak

| Izena | Mota | Deskribapena |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Testu-fitxategientzako edukia, bitarren kate base64. |
| `image` | `IMAGE 𝌠` | Irudi batch tensor. |
| `mask` | `MASK 𝌠` | Maskara batch tensor. |
| `metadata` | `STRING 𝌠` | ExifTool-eko Exif datuak. `exiftool` komandoa `PATH`-ean egon behar da. |

