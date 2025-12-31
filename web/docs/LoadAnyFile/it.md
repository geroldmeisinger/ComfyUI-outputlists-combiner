## Carica Qualsiasi File

![Carica Qualsiasi File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow incluso)

Carica qualsiasi file testo o binario e fornisce il contenuto del file come stringa o stringa base64. Inoltre prova a caricarlo come `IMAGE`. E prova anche a caricare qualsiasi metadato.

`filepath` supporta i percorsi file annotati di ComfyUI `[input]` `[output]` o `[temp]`.
`filepath` supporta anche le espansioni dei pattern glob `subdir/**/*.png`.
Internamente utilizza la [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) di Python.

`metadata` chiama `exiftool`, se è installato e disponibile in `PATH`, altrimenti utilizza `PIL.Image.info` come fallback.

Per motivi di sicurezza sono supportate solo le seguenti directory: `[input] [output] [temp]`.
Per motivi di prestazioni il numero di file è limitato a: 1024.

### Input

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `filepath` | `STRINGA` | La directory base predefinita è la directory utente `[input]`. Supporta l'espansione dei pattern glob `subdir/**/*.png`. Usa il suffisso ` [input]` ` [output]` o ` [temp]` (ricorda lo spazio iniziale!) per specificare una directory utente ComfyUI diversa. |

### Output

| Nome | Tipo | Descrizione |
| --- | --- | --- |
| `content` | `STRINGA 𝌠` | Contenuto del file per file testuali, base64 per file binari. |
| `image` | `IMAGE 𝌠` | Tensor batch di immagini. |
| `mask` | `MASK 𝌠` | Tensor batch di maschere. |
| `metadata` | `STRINGA 𝌠` | Dati Exif da ExifTool. Richiede che il comando `exiftool` sia disponibile in `PATH`. |

