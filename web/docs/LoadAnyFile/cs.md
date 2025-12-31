## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow zahrnut)

Načte libovolný textový nebo binární soubor a poskytne obsah souboru jako řetězec nebo base64 řetězec. Navíc se pokusí načíst jako `IMAGE`. A také se pokusí načíst jakékoli metadata.

`filepath` podporuje anotované cesty souborů ComfyUI `[input]` `[output]` nebo `[temp]`.
`filepath` také podporuje rozšíření glob-patterů `subdir/**/*.png`.
Interně používá python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` volá `exiftool`, pokud je nainstalován a dostupný v `PATH`, jinak používá `PIL.Image.info` jako zálohu.

Z bezpečnostních důvodů jsou podporovány pouze následující adresáře: `[input] [output] [temp]`.
Z důvodů výkonu je počet souborů omezen na: 1024.

### Vstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `filepath` | `ŘETĚZEC` | Základní adresář ve výchozím nastavení `[input]` uživatelský adresář. Podporuje rozšíření glob-patterů `subdir/**/*.png`. Použijte příponu ` [input]` ` [output]` nebo ` [temp]` (nezapomeňte na vedoucí mezery!) pro určení jiného uživatelského adresáře ComfyUI. |

### Výstupy

| Název | Typ | Popis |
| --- | --- | --- |
| `content` | `ŘETĚZEC 𝌠` | Obsah souboru pro textové soubory, base64 pro binární soubory. |
| `image` | `OBRÁZEK 𝌠` | Tensor batch obrázků. |
| `mask` | `MASKA 𝌠` | Tensor batch mask. |
| `metadata` | `ŘETĚZEC 𝌠` | Exif data z ExifToolu. Vyžaduje, aby příkaz `exiftool` byl dostupný v `PATH`. |

