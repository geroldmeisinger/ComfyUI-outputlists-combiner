## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(Aliran kerja ComfyUI disertakan)

Menghasilkan XYZ-Gridplot dari senarai imej.
Ia mengambil senarai imej (termasuk kumpulan) dan melandas mereka ke dalam senarai panjang terlebih dahulu (oleh itu `batch_size=1`).

**Bentuk Grid**
Menentukan bentuk grid dengan:
1. bilangan label baris
2. bilangan label lajur
3. imej sub yang tinggal.
Anda boleh menggunakan `order=inside_out` untuk membalikkan pemilihan imej (berguna jika `batch_size>1` dan anda mahu mengetik kumpulan).

**Penjajaran**
* Jika label dibungkus ke baris seterusnya keseluruhan paksi dipertimbangkan "multiline" dan menyelaraskannya di atas dengan jarak yang diselaraskan.
* Jika semua label adalah nombor atau semua berakhir dengan nombor (cth. `strength: 1.`) keseluruhan paksi dipertimbangkan "numeric" dan menyelaraskannya ke kanan.
* Teks lain dipertimbangkan "singleline" dan menyelaraskannya di tengah.
* Menyelaraskan label singleline dan numeric untuk lajur di bawah, dan untuk baris menyelaraskannya secara vertikal di tengah.

**Saiz Fon**
* Ketinggian kawasan label lajur ditentukan oleh `font_size` atau `setengah ketinggian pengemasan imej sub terbesar dalam mana-mana baris` (mana-mana yang lebih besar).
* Lebar kawasan label baris ditentukan oleh lebar terluas pengemasan imej sub (dengan minimum 256px).
* Teks dikurangkan sehingga muat (hingga `font_size_min=6`) dan menggunakan saiz fon yang sama untuk keseluruhan paksi (label baris atau label lajur).
Jika saiz fon sudah pada minimum, memotong sebarang teks yang tinggal.

**Pengemasan Imej Sub**
Membentuk imej sub (biasanya dari kumpulan) ke dalam kawasan paling segi empat sama (pembungkusan "imej sub"), kecuali `output_is_list=True`, dalam hal ini hanya menggunakan satu imej untuk setiap sel dan mencipta senarai grid imej keseluruhan.
Anda boleh menggunakan senarai grid imej ini untuk menyambungkan nod XyzGridPlot lain untuk mencipta super-grids.
Jika imej sub terdiri daripada kumpulan dengan saiz berbeza, mengisi sel yang hilang dengan imej kosong.
Bilangan imej per sel (termasuk imej kumpulan) mesti merupakan gandaan daripada `rows * columns`.

### Input

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `images` | `IMAGE` | Senarai imej (termasuk kumpulan) |
| `row_labels` | `*` | Teks label baris di sebelah kiri |
| `col_labels` | `*` | Teks label lajur di bahagian atas |
| `gap` | `INT` | Jarak antara pengemasan imej sub. Perhatikan bahawa di dalam imej sub itu sendiri tidak menggunakan jarak. Jika anda mahu jarak antara imej sub sambungkan nod XyzGridPlot lain. |
| `font_size` | `FLOAT` | Saiz fon sasaran. Teks akan dikurangkan sehingga muat (hingga `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientasi teks label baris. Berguna jika anda mahu menjimatkan ruang. |
| `order` | `BOOLEAN` | Menentukan dalam urutan apa imej harus diproses. Ini hanya relevan jika anda mempunyai imej sub. Berguna jika `batch_size>1` dan anda mahu memplot kumpulan. |
| `output_is_list` | `BOOLEAN` | Ini hanya relevan jika anda mempunyai imej sub atau mahu mencipta super-grids. |

### Output

| Nama | Jenis | Keterangan |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | Imej XYZ-GridPlot. Jika `output_is_list=True` mencipta senarai imej yang boleh anda sambungkan ke nod XYZ-GridPlot lain untuk mencipta super-grids. |

