## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow uključen)

Učitava bilo koju tekstualnu ili binarnu datoteku i pruža sadržaj datoteke kao niz znakova ili base64 niz znakova. Dodatno pokušava učitati kao `IMAGE`. I također pokušava učitati bilo kakve metapodatke.

`filepath` podržava ComfyUI-ove anotirane putanje datoteka `[input]` `[output]` ili `[temp]`.
`filepath` također podržava glob-obrade uzoraka `subdir/**/*.png`.
Unutarnje koristi pythonov [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` poziva `exiftool`, ako je instaliran i dostupan u `PATH`, u suprotnom koristi `PIL.Image.info` kao rezervnu opciju.

Iz sigurnosnih razloga podržani su samo sljedeći direktoriji: `[input] [output] [temp]`.
Iz razloga performansi broj datoteka je ograničen na: 1024.

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `filepath` | `NIZ ZNAKOVA` | Osnovni direktorij prema zadanim postavkama `[input]` korisnički direktorij. Podržava glob-obrade uzoraka `subdir/**/*.png`. Koristite sufiks ` [input]` ` [output]` ili ` [temp]` (imajte na umu vodeni razmak!) za određivanje drugog ComfyUI korisničkog direktorija. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `content` | `NIZ ZNAKOVA 𝌠` | Sadržaj datoteke za tekstualne datoteke, base64 za binarne datoteke. |
| `image` | `IMAGE 𝌠` | Tensor grupe slika. |
| `mask` | `MASK 𝌠` | Tensor grupe maske. |
| `metadata` | `NIZ ZNAKOVA 𝌠` | Exif podaci iz ExifTool-a. Zahtijeva da `exiftool` komanda bude dostupna u `PATH`. |

