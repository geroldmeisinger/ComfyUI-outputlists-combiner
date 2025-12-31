## KSampler Simpan Cepat

![KSampler Simpan Cepat](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow anu kalebet)

Ekspansi node tina default `CheckpointLoader`, `KSampler`, `VAE Decode` jeung `Save Image` pikeun ngolah sacara sahiji.
Ieu mangpaatkeun upami anjeun hoyong nyimpen gambar hartina pikeun kaca grid langsung.

*"A custom KSampler pikeun nyimpen gambar? Ayeuna kuring jadi hiji hal nu kuring ngajalankeun pikeun mampuskeun!"*

### Input

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Nama tina checkpoint (model) nu kudu dimuat. |
| `positive` | `STRING` | Conditioning anu ngagambarkeun atribut anu rék dimasukeun dina gambar. |
| `negative` | `STRING` | Conditioning anu ngagambarkeun atribut anu rék ditangkeleman tina gambar. |
| `latent_image` | `LATENT` | Gambar latent nu kudu di-de noise. |
| `seed` | `INT` | Seed acak anu dipaké pikeun nyiptakeun noise. |
| `steps` | `INT` | Jumlah langkah anu dipaké dina prosés de-noising. |
| `cfg` | `FLOAT` | Skala Classifier-Free Guidance ngabalakeun antara kreativitas jeung patuh ka prompt. Nilai anu luhur bakal ngahasilkeun gambar anu leuwih patuh ka prompt, tapi nilai anu luhur salawasna bakal mangarupeun kualitas. |
| `sampler_name` | `COMBO` | Algoritma anu dipaké dina ngambil sampel, ieu bisa mangarupeun kualitas, kecepatan, jeung gaya tina hasil anu dihasilkeun. |
| `scheduler` | `COMBO` | Scheduler ngamungkinakeun noise diangkep sacara bertahap pikeun ngahasilkeun gambar. |
| `denoise` | `FLOAT` | Jumlah de-noising anu dipaké, nilai anu luhur bakal nahan struktur gambar awal anu mangidin pikeun sampling gambar ka gambar. |
| `filename_prefix` | `STRING` | Prefiks pikeun file anu kudu disimpen. Ieu bisa ngandung informasi formatting sapertos %date:yyyy-MM-dd% atanapi %Empty Latent Image.width% pikeun masukeun nilai tina node. |

### Output

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `image` | `IMAGE` | Gambar anu di-decode. |

