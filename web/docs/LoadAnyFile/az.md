## Hər hansı bir faylı Yüklə

![Hər hansı bir faylı Yüklə](LoadAnyFile/LoadAnyFile.png)

(ComfyUI iş axını daxil olunub)

Hər hansı mətn və ya ikili faylı yükləyir və fayl məzmununu sətir və ya base64 sətiri kimi təqdim edir.Əlavə olaraq, onu `IMAGE` kimi yükləməyə çalışır və həmçinin hər hansı meta-məlumatları yükləməyə çalışır.

`filepath` ComfyUI-nin anotasiyalı fayl yollarını `[input]` `[output]` və ya `[temp]` dəstəkləyir.
`filepath` həmçinin glob-pattern genişlənmələrini dəstəkləyir `subdir/**/*.png`.
Daxili olaraq pythonun [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) istifadə edir.

`metadata` komandası `exiftool` quraşdırılıb və `PATH`-da mövcuddursa ona çağırır, əks halda `PIL.Image.info` fallback olaraq istifadə edir.

Təhlükəsizlik səbəbiylə yalnız aşağıdakı qovluqlar dəstəklənir: `[input] [output] [temp]`.
Sürət səbəbiylə fayl sayı aşağıdakı qədər ilə məhdudlaşdırılır: 1024.

### Girişlər

| Ad | Növ | İzahat |
| --- | --- | --- |
| `filepath` | `STRING` | Əsas qovluq `[input]` istifadəçi qovluğuna defolt olaraq təyin olunur. Glob-pattern genişlənməsini dəstəkləyir `subdir/**/*.png`. Fərqli bir ComfyUI istifadəçi qovluğunu müəyyən etmək üçün ` [input]` ` [output]` və ya ` [temp]` (başlanğıc boşluğu unutmayın!) suffixindən istifadə edin. |

### Çıxışlar

| Ad | Növ | İzahat |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Mətn faylları üçün fayl məzmunu, ikili fayllar üçün base64. |
| `image` | `IMAGE 𝌠` | Şəkil partiyası tensoru. |
| `mask` | `MASK 𝌠` | Maska partiyası tensoru. |
| `metadata` | `STRING 𝌠` | ExifTool-dən Exif məlumatları. `exiftool` komandasının `PATH`-da mövcud olması tələb olunur. |

