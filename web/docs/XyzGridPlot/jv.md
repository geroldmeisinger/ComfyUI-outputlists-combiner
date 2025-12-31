## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(Workflow ComfyUI kalebu)

Nggawé XYZ-Gridplot saka daptar gambar.
Iki nggunakaké daptar gambar (kabeh batch) lan mbentuk iku menyang daptar panjang (kaya `batch_size=1`).

**Bentuk grid**
Nentukan bentuk grid kanthi:
1. jumlah label baris
2. jumlah label kolom
3. sub-gambar sing sisa.
Sampeyan bisa nggunakaké `order=inside_out` supaya mbalikaké pilihan gambar (bisa digunakaké yen `batch_size>1` lan sampeyan pengin mbayar batch).

**Larik**
* Yen label dibungkus menyang baris sing ndhuit, sumuruh sumuruh dianggep "multiline" lan dilarikaké ing ndhuwur karo spacing sing diterbitaké.
* Yen kabeh label kaya angka utawa kabeh ngakhiri karo angka (kaya `strength: 1.`) sumuruh sumuruh dianggep "numeric" lan dilarikaké kanek.
* Teks liya dianggep "singleline" lan dilarikaké tengah.
* Larik label singleline lan numeric kanggo kolom ing ndhuwur, lan kanggo baris dilarikaké vertikal ing tengah.

**Ukuran font**
* Ketinggian wilayah label kolom ditentukan dening `font_size` utawa `setengah ketinggian sub-gambar sing paling gedhe ing baris apa wae` (kabeh sing luwih gedhe).
* Lebar wilayah label baris ditentukan dening lebar paling gede saka sub-gambar sing dibungkus (karo minimum 256px).
* Teks dibesut nganti pas (kaya `font_size_min=6`) lan nggunakaké ukuran font sing padha kanggo sumuruh sumuruh (label baris utawa label kolom).
Yen ukuran font wis nganti minimum, ngirisaké kabeh teks sing sisa.

**Pembungkusan sub-gambar**
Ngganti bentuk sub-gambar (biasane saka batch) menyang wilayah paling kotak (kaya "sub-images packing"), kanthi ora `output_is_list=True`, sing nggunakaké gambar tunggal kanggo setiap sel lan mbentuk daptar grid gambar utuh.
Sampeyan bisa nggunakaké daptar grid gambar iki supaya nyambungaké node XyzGridPlot liya supaya mbentuk super-grids.
Yen sub-gambar kalebu batch karo ukuran sing beda, ngisi sel sing kurang karo gambar kosong.
Jumlah gambar per sel (kabeh gambar batch) kudu kaping `rows * columns`.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `images` | `IMAGE` | Daptar gambar (kabeh batch) |
| `row_labels` | `*` | Teks label baris ing sisi kiwa |
| `col_labels` | `*` | Teks label kolom ing ndhuwur |
| `gap` | `INT` | Celaké antar pembungkusan sub-gambar. Catet yen ing sub-gambar iki ora nggunakaké celaké. Yen sampeyan pengin celaké antar sub-gambar nyambungaké node XyzGridPlot liya. |
| `font_size` | `FLOAT` | Ukuran font target. Teks dibesut nganti pas (kaya `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientasi teks saka label baris. Bisa digunakaké yen sampeyan pengin ngirit ruang. |
| `order` | `BOOLEAN` | Nentukan urutan gambar sing kudu diproses. Iki mung relevan yen sampeyan nggawé sub-gambar. Bisa digunakaké yen `batch_size>1` lan sampeyan pengin mbuat batch. |
| `output_is_list` | `BOOLEAN` | Iki mung relevan yen sampeyan nggawé sub-gambar utawa sampeyan pengin mbentuk super-grids. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Gambar XYZ-GridPlot. Yen `output_is_list=True` mbentuk daptar gambar sing bisa nyambungaké menyang node XYZ-GridPlot liya supaya mbentuk super-grids. |

