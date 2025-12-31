## Herhangi Bir Dosya Yükle

![Herhangi Bir Dosya Yükle](LoadAnyFile/LoadAnyFile.png)

(ComfyUI iş akışı dahil)

Herhangi bir metin veya ikili dosyayı yükler ve dosya içeriğini string veya base64 string olarak sağlar. Ayrıca dosyayı bir `IMAGE` olarak yüklemeye çalışır. Ayrıca herhangi bir meta veriyi de yüklemeye çalışır.

`filepath`, ComfyUI'nin `[input]` `[output]` veya `[temp]` ekli dosya yollarını destekler.
`filepath`, ayrıca glob-desen genişletmelerini destekler `subdir/**/*.png`.
İçeriksel olarak Python'un [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) kullanır.

`metadata`, eğer `exiftool` kuruluysa ve `PATH`'de mevcutsa çağrılır, aksi takdirde `PIL.Image.info` kullanılır.

Güvenlik nedeniyle yalnızca aşağıdaki dizinlere izin verilir: `[input] [output] [temp]`.
Performans nedeniyle dosya sayısı şu değere sınırlanmıştır: 1024.

### Girişler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `filepath` | `STRING` | Temel dizin `[input]` kullanıcı dizinidir. `subdir/**/*.png` glob-desen genişletmesini destekler. Farklı bir ComfyUI kullanıcı dizini belirtmek için ` [input]` ` [output]` veya ` [temp]` son ekini kullanın (başındaki boşluğu unutmayın!). |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Metin dosyaları için dosya içeriği, ikili dosyalar için base64. |
| `image` | `IMAGE 𝌠` | Resim toplu tensoru. |
| `mask` | `MASK 𝌠` | Maske toplu tensoru. |
| `metadata` | `STRING 𝌠` | ExifTool'dan Exif verileri. `exiftool` komutunun `PATH`'de mevcut olması gerekir. |

