## Wczytaj Dowolny Plik

![Wczytaj Dowolny Plik](LoadAnyFile/LoadAnyFile.png)

(Dołączony workflow ComfyUI)

Wczytuje dowolny plik tekstowy lub binarny i dostarcza zawartość pliku jako ciąg znaków lub ciąg znaków base64. Dodatkowo próbuje załadować go jako `IMAGE`. Również próbuje załadować metadane.

`filepath` obsługuje adnotowane ścieżki plików ComfyUI `[input]` `[output]` lub `[temp]`.
`filepath` obsługuje również rozszerzenia wzorców glob `subdir/**/*.png`.
Wewnętrznie używa pythonowego [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` wywołuje `exiftool`, jeśli jest zainstalowany i dostępny w `PATH`, w przeciwnym razie używa `PIL.Image.info` jako alternatywy.

Ze względów bezpieczeństwa obsługiwane są tylko następujące katalogi: `[input] [output] [temp]`.
Ze względu na wydajność liczba plików jest ograniczona do: 1024.

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `filepath` | `STRING` | Katalog bazowy domyślnie ustawiony na katalog użytkownika `[input]`. Obsługuje rozszerzenia wzorców glob `subdir/**/*.png`. Użyj sufiksu ` [input]` ` [output]` lub ` [temp]` (zwróć uwagę na wiodący biały znak!) aby określić inny katalog użytkownika ComfyUI. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Zawartość pliku dla plików tekstowych, base64 dla plików binarnych. |
| `image` | `IMAGE 𝌠` | Tensor partii obrazów. |
| `mask` | `MASK 𝌠` | Tensor partii mask. |
| `metadata` | `STRING 𝌠` | Dane Exif z ExifTool. Wymaga dostępnego polecenia `exiftool` w `PATH`. |

