## KSampler Simpan Segera

![KSampler Simpan Segera](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Aliran kerja ComfyUI disertakan)

Ekspansi nod bagi `CheckpointLoader` lalai, `KSampler`, `VAE Decode` dan `Save Image` untuk diproses sebagai satu.
Ini berguna jika anda ingin menyimpan imej perantaraan untuk grid segera.

*"Nod KSampler khas hanya untuk menyimpan imej? Sekarang saya telah menjadi perkara yang saya cari untuk memusnahkan!"*

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Nama checkpoint (model) untuk dimuatkan. |
| `positive` | `STRING` | Kondisi yang menerangkan atribut yang ingin dimasukkan ke dalam imej. |
| `negative` | `STRING` | Kondisi yang menerangkan atribut yang ingin dikecualikan dari imej. |
| `latent_image` | `LATENT` | Imej laten untuk dikesan. |
| `seed` | `INT` | Benih rawak digunakan untuk mencipta hingar. |
| `steps` | `INT` | Bilangan langkah digunakan dalam proses penyucian. |
| `cfg` | `FLOAT` | Skala Classifier-Free Guidance seimbangkan kreativiti dan kepatuhan kepada prompt. Nilai yang lebih tinggi menghasilkan imej yang lebih dekat dengan prompt namun nilai yang terlalu tinggi akan mempengaruhi kualiti secara negatif. |
| `sampler_name` | `COMBO` | Algoritma digunakan semasa sampling, ini boleh mempengaruhi kualiti, kelajuan, dan gaya output yang dijana. |
| `scheduler` | `COMBO` | Penjadual mengawal bagaimana hingar secara perlahan dibuang untuk membentuk imej. |
| `denoise` | `FLOAT` | Jumlah penyucian digunakan, nilai yang lebih rendah akan mengekalkan struktur imej asal membenarkan sampling imej ke imej. |
| `filename_prefix` | `STRING` | Awalan untuk fail untuk disimpan. Ini mungkin termasuk maklumat pemformatan seperti %date:yyyy-MM-dd% atau %Empty Latent Image.width% untuk memasukkan nilai daripada nod. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `image` | `IMAGE` | Imej yang dinyahkodkan. |

