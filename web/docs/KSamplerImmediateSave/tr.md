## KSampler Anında Kaydet

![KSampler Anında Kaydet](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow dahil)

Varsayılan `CheckpointLoader`, `KSampler`, `VAE Decode` ve `Save Image` düğümlerinin birleşimi.
Bu, görüntülerin grid'ler için ara görüntülerini anında kaydetmek istiyorsanız kullanışlıdır.

*"Bir görüntüyü kaydetmek için özel bir KSampler? Artık yok etmeye çalıştığım şeyin kendisi oldum!"*

### Girdiler

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Yüklenecek checkpoint (model) adı. |
| `positive` | `STRING` | Görüntüye dahil etmek istediğiniz özellikleri tanımlayan koşullandırma. |
| `negative` | `STRING` | Görüntüden hariç tutmak istediğiniz özellikleri tanımlayan koşullandırma. |
| `latent_image` | `LATENT` | Gürültü azaltılacak latent görüntü. |
| `seed` | `INT` | Gürültü oluşturmada kullanılan rastgele tohum. |
| `steps` | `INT` | Gürültü azaltma işleminde kullanılan adım sayısı. |
| `cfg` | `FLOAT` | Sınıflandırıcı Serbest Yönlendirme ölçeği, yaratıcılık ve prompta uygunluğu dengelemektedir. Daha yüksek değerler, prompta daha yakın görüntüler üretir ancak çok yüksek değerler kalite üzerinde olumsuz etki yapar. |
| `sampler_name` | `COMBO` | Örnekleme sırasında kullanılan algoritma, bu, üretimin kalitesini, hızını ve tarzını etkileyebilir. |
| `scheduler` | `COMBO` | Zamanlayıcı, görüntünün oluşumunda gürültünün nasıl azaltıldığını kontrol eder. |
| `denoise` | `FLOAT` | Uygulanan gürültü azaltma miktarı, düşük değerler başlangıç görüntüsünün yapısını koruyarak görüntü-görüntü örnekleme yapılmasını sağlar. |
| `filename_prefix` | `STRING` | Kaydedilecek dosya için ön ek. Bu, %date:yyyy-MM-dd% veya %Empty Latent Image.width% gibi biçimlendirme bilgilerini içerebilir; düğümlerden gelen değerleri dahil etmek için. |

### Çıkışlar

| Ad | Tür | Açıklama |
| --- | --- | --- |
| `image` | `IMAGE` | Kod çözülmüş görüntü. |

