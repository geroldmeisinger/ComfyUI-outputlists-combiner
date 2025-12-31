## KSampler Simpen Cepet

![KSampler Simpen Cepet](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Workflow ComfyUI kalebu)

Ekspansi node saka default `CheckpointLoader`, `KSampler`, `VAE Decode` lan `Save Image` supaya diprosés kanthi siji.
Iki kaya kene yen sampeyan pengin nyimpen gambar saka grid langsung.

*"KSampler khusus mung kanggo nyimpen gambar? Aku wis uga menjadi benda sing kubutuhake supaya dihancuraké!"*

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Jeneng saka checkpoint (model) sing bakal dimuat. |
| `positive` | `STRING` | Conditioning sing nglaraké atribut sing pengin sampeyan masuk menyang gambar. |
| `negative` | `STRING` | Conditioning sing nglaraké atribut sing pengin sampeyan kacaulaké saka gambar. |
| `latent_image` | `LATENT` | Gambar latent sing bakal di-denoise. |
| `seed` | `INT` | Seed acak sing nggunakaké supaya nggawé noise. |
| `steps` | `INT` | Jumlah langkah sing nggunakaké ing prosés denoising. |
| `cfg` | `FLOAT` | Skala Classifier-Free Guidance mbalansi kreativitas lan kepatuhan menyang prompt. Nilai sing luwih dhuwur bakal ngasilaké gambar sing luwih cocok karo prompt, tapi nilai sing luwih dhuwur bakal ngaruh negatip kathing kualitas. |
| `sampler_name` | `COMBO` | Algoritma sing nggunakaké nalika ngambil sampel, iki bisa ngaruh kathing kualitas, kecepatan, lan gaya saka output sing digawé. |
| `scheduler` | `COMBO` | Scheduler ngontrol cara noise dadi dadi dipindhakake supaya nggawé gambar. |
| `denoise` | `FLOAT` | Jumlah denoising sing diaplikasikan, nilai sing luwih cilik bakal nyimpen struktur saka gambar awal, ngidini image to image sampling. |
| `filename_prefix` | `STRING` | Prefiks kanggo file sing bakal disimpen. Iki bisa ngandhaké informasi formatting kaya %date:yyyy-MM-dd% utawa %Empty Latent Image.width% supaya nggawé nilai saka node. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `image` | `IMAGE` | Gambar sing di-decode. |

