## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow disertakan)

Ekspansi node dari default `CheckpointLoader`, `KSampler`, `VAE Decode` dan `Save Image` untuk diproses sebagai satu.
Ini berguna jika Anda ingin menyimpan gambar intermediate untuk grid segera.

*"Sebuah KSampler kustom hanya untuk menyimpan gambar? Sekarang aku telah menjadi hal yang telah kutuju untuk hancurkan!"*

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Nama dari checkpoint (model) yang akan dimuat. |
| `positive` | `STRING` | Kondisi yang menjelaskan atribut yang ingin Anda sertakan dalam gambar. |
| `negative` | `STRING` | Kondisi yang menjelaskan atribut yang ingin Anda kecualikan dari gambar. |
| `latent_image` | `LATENT` | Gambar laten untuk dide-noise. |
| `seed` | `INT` | Benih acak yang digunakan untuk membuat kebisingan. |
| `steps` | `INT` | Jumlah langkah yang digunakan dalam proses de-noising. |
| `cfg` | `FLOAT` | Skala Classifier-Free Guidance menyeimbangkan kreativitas dan kepatuhan terhadap prompt. Nilai yang lebih tinggi menghasilkan gambar yang lebih sesuai dengan prompt namun nilai yang terlalu tinggi akan memengaruhi kualitas secara negatif. |
| `sampler_name` | `COMBO` | Algoritma yang digunakan saat sampling, ini dapat memengaruhi kualitas, kecepatan, dan gaya dari output yang dihasilkan. |
| `scheduler` | `COMBO` | Penjadwal mengontrol bagaimana kebisingan secara bertahap dihapus untuk membentuk gambar. |
| `denoise` | `FLOAT` | Jumlah de-noising yang diterapkan, nilai yang lebih rendah akan mempertahankan struktur dari gambar awal memungkinkan sampling gambar ke gambar. |
| `filename_prefix` | `STRING` | Awalan untuk file yang akan disimpan. Ini mungkin mencakup informasi pemformatan seperti %date:yyyy-MM-dd% atau %Empty Latent Image.width% untuk menyertakan nilai dari node. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `image` | `IMAGE` | Gambar yang didekodekan. |

