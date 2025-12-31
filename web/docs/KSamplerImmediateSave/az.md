## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow daxildədir)

Default `CheckpointLoader`, `KSampler`, `VAE Decode` və `Save Image` node-larının genişləndirilməsi, birlikdə işləmək üçün.
Bu, şəkil qələmlərində ara şəkilləri dərhal saxlamaq istədiyiniz zaman faydalıdır.

*"Şəkli saxlamaq üçün xüsusi KSampler? Artıq mən tərəfindən axtarılan şeyin özüm olmuşam!"*

### Girişlər

| Ad | Tip | İzahat |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Yüklənəcək checkpoint (model) adı. |
| `positive` | `STRING` | Şəkildə daxil etmək istədiyiniz xüsusiyyətləri təsvir edən şərt. |
| `negative` | `STRING` | Şəkildə istisna etmək istədiyiniz xüsusiyyətləri təsvir edən şərt. |
| `latent_image` | `LATENT` | Gürültü aradan qaldırılması üçün latent şəkil. |
| `seed` | `INT` | Gürültü yaratmaq üçün istifadə olunan təsadüfi seed. |
| `steps` | `INT` | Gürültü aradan qaldırma prosesində istifadə olunan addım sayı. |
| `cfg` | `FLOAT` | Classifier-Free Guidance miqyası yaradıcılığı və prompt-a uyğunluğu balanslayır. Daha yüksək dəyərlər prompt-a daha yaxın şəkillər yaratır, lakin çox yüksək dəyərlər keyfiyyəti pozaraq təsir edə bilər. |
| `sampler_name` | `COMBO` | Nümunə çıxarma zamanı istifadə olunan alqoritm, bu, yaradılmış çıxışın keyfiyyətini, sürətini və stilini təsir edə bilər. |
| `scheduler` | `COMBO` | Planlayıcı, şəkli yaratmaq üçün gürültünün nəzərdən çıxarılmasını idarə edir. |
| `denoise` | `FLOAT` | Tətbiq olunan gürültü aradan qaldırma miqyası, daha aşağı dəyərlər ilkin şəklin strukturu saxlanır, şəkilə şəkil nümunə çıxarmaq imkanı verir. |
| `filename_prefix` | `STRING` | Saxlanacaq fayl üçün prefix. Bu, %date:yyyy-MM-dd% və ya %Empty Latent Image.width% kimi formatlama məlumatlarını ehtiva edə bilər, node-lardan dəyərləri daxil etmək üçün. |

### Çıxışlar

| Ad | Tip | İzahat |
| --- | --- | --- |
| `image` | `IMAGE` | Kodlaşdırılmış şəkil. |

