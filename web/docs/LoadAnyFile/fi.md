## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI-työnkulku mukana)

Lataa minkä tahansa tekstin tai binääritiedoston ja tarjoaa tiedoston sisällön merkkijonona tai base64-merkkijonona. Lisäksi yrittää ladata sen `IMAGE`-tyyppisenä. Yrittää myös ladata kaikki metatiedot.

`filepath` tukee ComfyUI:n merkittyjä tiedostopolkuja `[input]` `[output]` tai `[temp]`.
`filepath` tukee myös glob-mallin laajennuksia `subdir/**/*.png`.
Sisäisesti käyttää pythonin [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` kutsuu `exiftool`, jos se on asennettu ja käytettävissä `PATH`-polussa, muussa tapauksessa käyttää `PIL.Image.info` varavaihtoehtona.

Turvallisuussyistä tuetaan vain seuraavat hakemistot: `[input] [output] [temp]`.
Suorituskykyyn liittyen tiedostojen määrä on rajoitettu: 1024.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `filepath` | `STRING` | Perushakemisto oletuksena `[input]` käyttäjähakemisto. Tukee glob-mallin laajennusta `subdir/**/*.png`. Käytä pääte ` [input]` ` [output]` tai ` [temp]` (huomaa etuliite tyhjä tila!) määrittääksesi eri ComfyUI-käyttäjähakemiston. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Tekstitiedostojen sisältö, base64 binääritiedostoille. |
| `image` | `IMAGE 𝌠` | Kuvien erä tensori. |
| `mask` | `MASK 𝌠` | Maskin erä tensori. |
| `metadata` | `STRING 𝌠` | Exif-tiedot ExifToolistä. Vaatii `exiftool`-komennon olevan käytettävissä `PATH`-polussa. |

