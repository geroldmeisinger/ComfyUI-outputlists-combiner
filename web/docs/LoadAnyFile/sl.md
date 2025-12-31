## Naloži katerokoli datoteko

![Naloži katerokoli datoteko](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow vključen)

Naloži katerokoli besedilno ali binarno datoteko in zagotovi vsebino datoteke kot niz ali base64 niz. Prav tako poskuša naložiti kot `IMAGE`. Poskuša tudi naložiti vse metapodatke.

`filepath` podpira ComfyUI-jeve opisane poti do datotek `[input]` `[output]` ali `[temp]`.
`filepath` podpira tudi razširjanje glob-vzorcev `subdir/**/*.png`.
Notranje uporablja pythonov [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kliče `exiftool`, če je nameščen in dostopen v `PATH`, sicer uporabi `PIL.Image.info` kot nadomestno možnost.

Zaradi varnostnih razlogov so podprte le naslednje mape: `[input] [output] [temp]`.
Zaradi učinkovitosti je število datotek omejeno na: 1024.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `filepath` | `STRING` | Osnovna mapa privzeto `[input]` uporabniška mapa. Podpira razširjanje glob-vzorcev `subdir/**/*.png`. Uporabi pripono ` [input]` ` [output]` ali ` [temp]` (pozor na vodilni presledek!) za določitev različne ComfyUI uporabniške mape. |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Vsebina datoteke za besedilne datoteke, base64 za binarne datoteke. |
| `image` | `IMAGE 𝌠` | Tenzor s slikovnim paketom. |
| `mask` | `MASK 𝌠` | Tenzor s paketom mask. |
| `metadata` | `STRING 𝌠` | Exif podatki iz ExifTool. Zahteva, da je ukaz `exiftool` dostopen v `PATH`. |

