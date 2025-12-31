## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow anu kalebet)

Manghasilkeun XYZ-Gridplot tina daptar gambar.
Éta mameuli daptar gambar (kalebet batch) jeung ngekspansiana jadi daptar panjang (sareng `batch_size=1`).

**Bentuk grid**
Nentukan bentuk grid ku:
1. jumlah label baris
2. jumlah label kolom
3. sisa sub-gambar.
Nan bisa nganggo `order=inside_out` pikeun mbalikkeun pilihan gambar (gunaan jike `batch_size>1` jeung anjeun pengen nandai batch-nya).

**Pangaturan**
* Upami label kana ngalih ka baris sabanjurénna, sadaya sumbu dianggap "multiline" jeung nangtukeun éta di luhur jeung ngagunakeun jarak anu disetujui.
* Upami sadaya label mangrupa angka atanapi sadaya éta diakhiri ku angka (kécap `strength: 1.`) sadaya sumbu dianggap "numeric" jeung nangtukeun éta di kanan.
* Téks anu sanés dianggap "singleline" jeung nangtukeun éta di tengah.
* Nangtukeun label singleline jeung numeric pikeun kolom di luhur, jeung pikeun baris nangtukeun éta di tengah vertikal.

**Ukuran font**
* Katinggian wilayah label kolom ditentukan ku `font_size` atanapi `setengah katinggian pakegean sub-gambar pangahiji dina sadaya baris` (naon anu leuwih gedé).
* Lebar wilayah label baris ditentukan ku lebar pangahiji sub-gambar (minim 256px).
* Téks dikurangkeun sampeyan ngahubungkeun sasaténgah (sampai `font_size_min=6`) jeung ngagunakeun ukuran font anu samé pikeun sadaya sumbu (label baris atanapi label kolom).
Upami ukuran font geus di minimum, ngatetkeun téks anu sanés.

**Pakegean sub-gambar**
Ngganti bentuk sub-gambar (biasana tina batch) jadi wilayah anu paling kotak (nu "pakegean sub-gambar"), kecuali `output_is_list=True`, dina kasus éta ngagunakeun cihén gambar pikeun sabaréh wéndi jeung ngahasilkeun daptar wilayah gambar anu lengkep.
Nan bisa nganggo daptar wilayah gambar ieu pikeun nyambungkeun node XyzGridPlot anu sanés pikeun ngahasilkeun super-grids.
Upami sub-gambar mangrupa batch anu ukuran éta béda, ngisi wéndi anu mangkak jadi gambar kosong.
Jumlah gambar dina wéndi (kalebet gambar batch) kudu jadi kelipatan `rows * columns`.

### Input

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `images` | `IMAGE` | Daptar gambar (kalebet batch) |
| `row_labels` | `*` | Téks label baris di sisi kénéh |
| `col_labels` | `*` | Téks label kolom di luhur |
| `gap` | `INT` | Jarak antara pakegean sub-gambar. Perhatikeun yén di dalam sub-gambar éta manggunaan jarak. Upami anjeun pengen jarak antara sub-gambar, nyambungkeun node XyzGridPlot anu sanés. |
| `font_size` | `FLOAT` | Ukuran font target. Téks bakal dikurangkeun sampeyan ngahubungkeun sasaténgah (sampai `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientasi téks pikeun label baris. Useful upami anjeun pengen ngahurungkeun ruang. |
| `order` | `BOOLEAN` | Nentukan urutan pikeun diprosés gambar. Ieu mung aya gunana upami anjeun nganana sub-gambar. Useful upami `batch_size>1` jeung anjeun pengen nampilkeun batch-nya. |
| `output_is_list` | `BOOLEAN` | Ieu mung aya gunana upami anjeun nganana sub-gambar atanapi anjeun pengen ngahasilkeun super-grids. |

### Output

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Gambar XYZ-GridPlot. Upami `output_is_list=True` ngahasilkeun daptar gambar anu bisa nyambungkeun ka node XYZ-GridPlot anu sanés pikeun ngahasilkeun super-grids. |

