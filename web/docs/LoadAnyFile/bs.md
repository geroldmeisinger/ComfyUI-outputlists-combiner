## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI radni tok je uključen)

Učitava bilo koju tekstualnu ili binarnu datoteku i pruža sadržaj datoteke kao niz znakova ili base64 niz znakova. Dodatno pokušava učitati kao `IMAGE`. I takođe pokušava učitati sve metapodatke.

`filepath` podržava ComfyUI anotirane putanje datoteka `[input]` `[output]` ili `[temp]`.
`filepath` takođe podržava glob-obrade uzoraka `subdir/**/*.png`.
Unutrašnje korištenje python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` poziva `exiftool`, ako je instaliran i dostupan u `PATH`, u suprotnom koristi `PIL.Image.info` kao rezervnu opciju.

Iz sigurnosnih razloga podržani su samo slijedeći direktoriji: `[input] [output] [temp]`.
Iz razloga performansi broj datoteka je ograničen na: 1024.

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `filepath` | `NIZ ZNAKOVA` | Osnovni direktorij podrazumijeva `[input]` korisnički direktorij. Podržava glob-obradu uzoraka `subdir/**/*.png`. Koristi sufiks ` [input]` ` [output]` ili ` [temp]` (imajte na umu vodeni razmak!) da odredite drugačiji ComfyUI korisnički direktorij. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `content` | `NIZ ZNAKOVA 𝌠` | Sadržaj datoteke za tekstualne datoteke, base64 za binarne datoteke. |
| `slika` | `IMAGE 𝌠` | Tensor grupe slika. |
| `maska` | `MASK 𝌠` | Tensor grupe maski. |
| `metadata` | `NIZ ZNAKOVA 𝌠` | Exif podaci iz ExifTool-a. Zahtijeva `exiftool` komandu da bude dostupna u `PATH`. |

