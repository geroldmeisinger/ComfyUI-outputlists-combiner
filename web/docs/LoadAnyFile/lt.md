## Įkelti bet kokį failą

![Įkelti bet kokį failą](LoadAnyFile/LoadAnyFile.png)

(ComfyUI darbo eiga įtraukta)

Įkelia bet kokį tekstinį arba dvejetainį failą ir pateikia failo turinį kaip eilutę arba base64 eilutę. Be to, bandys įkelti jį kaip `VAIZDAS`. Taip pat bandys įkelti bet kokius metaduomenis.

`filepath` palaiko ComfyUI anotuotas failų keliais `[input]` `[output]` arba `[temp]`.
`filepath` taip pat palaiko glob šablonų išplėtimą `subdir/**/*.png`.
Viduje naudoja python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` iškviečia `exiftool`, jei jis įdiegtas ir prieinamas `PATH`, kitaip naudoja `PIL.Image.info` kaip atsarginį sprendimą.

Saugumo sumetimais palaikomos tik šios direktorijos: `[input] [output] [temp]`.
Našumo sumetimais failų skaičius apribotas iki: 1024.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `filepath` | `EILUTĖ` | Pagrindinė direktorija numatyta `[input]` naudotojo direktorija. Palaiko glob šablonų išplėtimą `subdir/**/*.png`. Naudokite sufiksą ` [input]` ` [output]` arba ` [temp]` (atsiminkite pradžios tarpą!) norėdami nurodyti kitą ComfyUI naudotojo direktoriją. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `turinys` | `EILUTĖ 𝌠` | Failo turinys tekstinio failo atveju, base64 dvejetainių failų atveju. |
| `vaizdas` | `VAIZDAS 𝌠` | Vaizdų paketo tensorius. |
| `kaukė` | `KAUKĖ 𝌠` | Kaukės paketo tensorius. |
| `metaduomenys` | `EILUTĖ 𝌠` | Exif duomenys iš ExifTool. Reikalauja, kad `exiftool` komanda būtų prieinama `PATH`. |

