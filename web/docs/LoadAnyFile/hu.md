## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflow mellékletként)

Bármely szöveges vagy bináris fájl betöltése és a fájl tartalmának sztringként vagy base64 sztringként történő biztosítása. Ezenkívül megpróbálja betölteni mint `IMAGE`-t. Ezenkívül megpróbálja betölteni bármely metaadatot is.

A `filepath` támogatja a ComfyUI annotált fájlkönyvtárakat `[input]` `[output]` vagy `[temp]`.
A `filepath` támogatja a glob-minták kiterjesztését `subdir/**/*.png`.
Belsőleg a python [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) függvényt használja.

A `metadata` meghívja az `exiftool`-t, ha telepítve van és elérhető a `PATH`-en, különben a `PIL.Image.info` fallback-et használja.

Biztonsági okokból csak a következő könyvtárak támogatottak: `[input] [output] [temp]`.
Teljesítmény okokból a fájlok száma korlátozva van: 1024.

### Bemenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `filepath` | `STRING` | Az alapértelmezett könyvtár a `[input]` felhasználói könyvtár. Támogatja a glob-minta kiterjesztést `subdir/**/*.png`. Használja a ` [input]` ` [output]` vagy ` [temp]` utótagot (figyelem a vezető szóközzel!) egy másik ComfyUI felhasználói könyvtár megadásához. |

### Kimenetek

| Név | Típus | Leírás |
| --- | --- | --- |
| `content` | `STRING 𝌠` | A fájl tartalma szöveges fájlokhoz, base64 bináris fájlokhoz. |
| `image` | `IMAGE 𝌠` | Kép batch tenzor. |
| `mask` | `MASK 𝌠` | Maszk batch tenzor. |
| `metadata` | `STRING 𝌠` | Exif adatok az ExifTool-ből. Az `exiftool` parancs elérhető kell legyen a `PATH`-en. |

