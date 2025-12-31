## Beliebige Datei Laden

![Beliebige Datei Laden](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow inkludiert)

Lädt beliebige Text- oder Binärdateien und stellt den Dateiinhalt als Zeichenkette oder base64-Zeichenkette zur Verfügung. Versucht zusätzlich, sie als `IMAGE` zu laden. Versucht auch, alle Metadaten zu laden.

`filepath` unterstützt ComfyUIs annotierte Dateipfade `[input]` `[output]` oder `[temp]`.
`filepath` unterstützt auch Glob-Muster-Erweiterungen `subdir/**/*.png`.
Verwendet intern python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` ruft `exiftool` auf, falls es installiert und verfügbar unter `PATH` ist, andernfalls verwendet es `PIL.Image.info` als Fallback.

Aus Sicherheitsgründen werden nur folgende Verzeichnisse unterstützt: `[input] [output] [temp]`.
Aus Leistungsgründen ist die Anzahl der Dateien auf: 1024 begrenzt.

### Eingaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `filepath` | `ZEICHENKETTE` | Basisverzeichnis standardmäßig auf `[input]` Benutzerverzeichnis. Unterstützt Glob-Muster-Erweiterung `subdir/**/*.png`. Verwenden Sie den Suffix ` [input]` ` [output]` oder ` [temp]` (achten Sie auf das führende Leerzeichen!), um ein anderes ComfyUI-Benutzerverzeichnis anzugeben. |

### Ausgaben

| Name | Typ | Beschreibung |
| --- | --- | --- |
| `content` | `ZEICHENKETTE 𝌠` | Dateiinhalt für Textdateien, base64 für Binärdateien. |
| `image` | `IMAGE 𝌠` | Bild-Batch-Tensor. |
| `mask` | `MASK 𝌠` | Masken-Batch-Tensor. |
| `metadata` | `ZEICHENKETTE 𝌠` | Exif-Daten von ExifTool. Erfordert, dass der `exiftool`-Befehl unter `PATH` verfügbar ist. |

