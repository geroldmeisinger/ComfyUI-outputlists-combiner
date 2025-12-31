## OutputList String

![OutputList String](StringOutputList/StringOutputList.png)

(Workflow ComfyUI kalebu)

Nggawé OutputList kanthi mbagi string ing textfield karo separator.
`value` lan `index` nggunakaké `is_output_list=True` (indikasi dening simbol `𝌠`) lan bakal diprosés kanthi urutan dening node sing padha.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `separator` | `STRING` | String sing digunakaké supaya mbagi nilai textfield. |
| `values` | `STRING` | Teks sing sampeyan pengin dibagi menyang daptar. Catet yen string iki dipotong saka newline pungkasan sadurunge mbagi, lan saben item uga dipotong saka spasi. |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `value` | `* 𝌠` | Nilai saka daptar. |
| `index` | `INT 𝌠` | Jarak 0..count. Sampeyan bisa nggunakaké iki minangka index. |
| `count` | `INT` | Jumlah item ing daptar. |
| `inspect_combo` | `COMBO` | Output dummy sing bisa digunakaké supaya nyambung menyang `COMBO` lan mbayar iki kanthi nilainya. Sambungan iki bakal otomatis disambung menyang output `value`. |

