## Načítaj ľubovoľný súbor

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow zahrnutý)

Načíta akýkoľvek textový alebo binárny súbor a poskytne obsah súboru ako reťazec alebo base64 reťazec. Okrem toho sa pokúsi načítať súbor ako `IMAGE`. A tiež sa pokúsi načítať akékoľvek metadáta.

`filepath` podporuje anotované cesty k súborom ComfyUI `[input]` `[output]` alebo `[temp]`.
`filepath` tiež podporuje rozšírenie glob-pattern `subdir/**/*.png`.
Interným spôsobom používa python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` volá `exiftool`, ak je nainštalovaný a dostupný v `PATH`, v opačnom prípade použije `PIL.Image.info` ako náhradu.

Z bezpečnostných dôvodov sú podporované len nasledujúce adresáre: `[input] [output] [temp]`.
Z dôvodov výkonu je počet súborov obmedzený na: 1024.

### Vstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `filepath` | `STRING` | Základný adresár predvolene `[input]` používateľský adresár. Podporuje rozšírenie glob-pattern `subdir/**/*.png`. Použite príponu ` [input]` ` [output]` alebo ` [temp]` (nezabudnite medzeru na začiatku!) na určenie iného ComfyUI používateľského adresára. |

### Výstupy

| Názov | Typ | Popis |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Obsah súboru pre textové súbory, base64 pre binárne súbory. |
| `image` | `IMAGE 𝌠` | Tensor batchu obrázkov. |
| `mask` | `MASK 𝌠` | Tensor batchu masky. |
| `metadata` | `STRING 𝌠` | Exif dáta z ExifTool. Vyžaduje prítomnosť príkazu `exiftool` v `PATH`. |

