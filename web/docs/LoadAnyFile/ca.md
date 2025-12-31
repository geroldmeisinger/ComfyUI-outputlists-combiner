## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inclòs)

Carrega qualsevol fitxer de text o binari i proporciona el contingut del fitxer com a cadena o cadena base64. Addicionalment intenta carregar-lo com a `IMAGE`. I també intenta carregar qualsevol metadada.

`filepath` suporta les rutes de fitxers anotades de ComfyUI `[input]` `[output]` o `[temp]`.
`filepath` també suporta expansions de patrons glob `subdir/**/*.png`.
Internament utilitza [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) de Python.

`metadata` crida `exiftool`, si està instal·lat i disponible a `PATH`, altrament utilitza `PIL.Image.info` com a alternativa.

Per raons de seguretat només s'admeten els següents directoris: `[input] [output] [temp]`.
Per raons de rendiment el nombre de fitxers està limitat a: 1024.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `filepath` | `STRING` | El directori base per defecte és el directori d'usuari `[input]`. Suporta l'expansió de patrons glob `subdir/**/*.png`. Utilitza el sufix ` [input]` ` [output]` o ` [temp]` (tingues en compte l'espai inicial!) per especificar un directori d'usuari ComfyUI diferent. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Contingut del fitxer per fitxers de text, base64 per fitxers binaris. |
| `image` | `IMAGE 𝌠` | Tensor de lot d'imatges. |
| `mask` | `MASK 𝌠` | Tensor de lot de màscares. |
| `metadata` | `STRING 𝌠` | Dades Exif de ExifTool. Requereix que l'ordre `exiftool` estigui disponible a `PATH`. |

