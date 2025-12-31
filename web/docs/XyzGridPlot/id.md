## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI workflow disertakan)

Menghasilkan XYZ-Gridplot dari daftar gambar.
Node ini mengambil daftar gambar (termasuk batch) dan memadatkannya menjadi daftar panjang terlebih dahulu (sehingga `batch_size=1`).

**Bentuk grid**
Menentukan bentuk grid dengan:
1. jumlah label baris
2. jumlah label kolom
3. sisa sub-gambar.
Anda dapat menggunakan `order=inside_out` untuk membalik pemilihan gambar (berguna jika `batch_size>1` dan Anda ingin memberi label pada batch).

**Perataan**
* Jika label terbungkus ke baris berikutnya, seluruh sumbu dianggap "multiline" dan menyelaraskan mereka di atas dengan spacing yang diratakan.
* Jika semua label berupa angka atau semua berakhir dengan angka (misalnya `strength: 1.`), seluruh sumbu dianggap "numeric" dan menyelaraskan mereka ke kanan.
* Teks lainnya dianggap "singleline" dan menyelaraskan mereka di tengah.
* Menyelaraskan label singleline dan numeric untuk kolom di bawah, dan untuk baris menyelaraskan mereka secara vertikal di tengah.

**Ukuran font**
* Tinggi area label kolom ditentukan oleh `font_size` atau `setengah dari tinggi packing sub-gambar terbesar dalam baris mana pun` (mana pun yang lebih besar).
* Lebar area label baris ditentukan oleh lebar terbesar dari packing sub-gambar (dengan minimum 256px).
* Teks dikurangi hingga muat (sampai `font_size_min=6`) dan menggunakan ukuran font yang sama untuk seluruh sumbu (label baris atau label kolom).
Jika ukuran font sudah mencapai minimum, memotong teks yang tersisa.

**Packing sub-gambar**
Membentuk sub-gambar (biasanya dari batch) ke area paling persegi (yang "sub-images packing"), kecuali `output_is_list=True`, dalam hal ini hanya menggunakan satu gambar untuk setiap sel dan membuat daftar grid gambar utuh sebagai gantinya.
Anda dapat menggunakan daftar grid gambar ini untuk menghubungkan node XyzGridPlot lain untuk membuat super-grids.
Jika sub-gambar terdiri dari batch dengan ukuran berbeda, mengisi sel yang hilang dengan gambar kosong.
Jumlah gambar per sel (termasuk gambar batch) harus merupakan kelipatan dari `rows * columns`.

### Masukan

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `images` | `IMAGE` | Daftar gambar (termasuk batch) |
| `row_labels` | `*` | Teks label baris di sisi kiri |
| `col_labels` | `*` | Teks label kolom di atas |
| `gap` | `INT` | Jarak antara packing sub-gambar. Perhatikan bahwa dalam sub-gambar itu sendiri tidak menggunakan jarak. Jika Anda ingin jarak antara sub-gambar, hubungkan node XyzGridPlot lain. |
| `font_size` | `FLOAT` | Ukuran font target. Teks akan dikurangi hingga muat (sampai `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientasi teks dari label baris. Berguna jika Anda ingin menghemat ruang. |
| `order` | `BOOLEAN` | Menentukan urutan pemrosesan gambar. Ini hanya relevan jika Anda memiliki sub-gambar. Berguna jika `batch_size>1` dan Anda ingin memplot batch. |
| `output_is_list` | `BOOLEAN` | Ini hanya relevan jika Anda memiliki sub-gambar atau ingin membuat super-grids. |

### Keluaran

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Gambar XYZ-GridPlot. Jika `output_is_list=True` membuat daftar gambar yang dapat Anda hubungkan ke node XYZ-GridPlot lain untuk membuat super-grids. |

