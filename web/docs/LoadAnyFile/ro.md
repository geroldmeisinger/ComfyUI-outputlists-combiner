## Încarcă orice fișier

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inclus)

Încarcă orice fișier text sau binar și furnizează conținutul fișierului ca șir de caractere sau șir de caractere base64. De asemenea încearcă să îl încarce ca `IMAGE`. Și de asemenea încearcă să încarce orice metadate.

`filepath` suportă căilor de fișiere annotate de ComfyUI `[input]` `[output]` sau `[temp]`.
`filepath` suportă și expansiunile de tip glob-pattern `subdir/**/*.png`.
Folosește intern [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) din Python.

`metadata` apelează `exiftool`, dacă este instalat și disponibil în `PATH`, altfel folosește `PIL.Image.info` ca alternativă.

Din motive de securitate, sunt suportate doar următoarele directoare: `[input] [output] [temp]`.
Din motive de performanță, numărul de fișiere este limitat la: 1024.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `filepath` | `STRING` | Directorul de bază are implicit `[input]` directorul de utilizator. Suportă expansiunea de tip glob-pattern `subdir/**/*.png`. Folosește sufixul ` [input]` ` [output]` sau ` [temp]` (ține cont de spațiul din față!) pentru a specifica un director de utilizator ComfyUI diferit. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Conținutul fișierului pentru fișierele text, base64 pentru fișierele binare. |
| `image` | `IMAGE 𝌠` | Tensor batch de imagini. |
| `mask` | `MASK 𝌠` | Tensor batch de mascuri. |
| `metadata` | `STRING 𝌠` | Date Exif de la ExifTool. Necesită ca comanda `exiftool` să fie disponibilă în `PATH`. |

