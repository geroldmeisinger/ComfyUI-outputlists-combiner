## Konversi Menjadi Int Float Str

![Konversi Menjadi Int Float Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Workflow ComfyUI kalebu)

Mengonversi apa waèh sing ana nomoré menyang `INT` `FLOAT` `STRING`.
Nggunakaké `nums_from_string.get_nums` ing ngisoré sing cukup luntur ing nomor sing diterimaké. Apa waèh saka int ényata, float ényata, int utawa float minangka string, string sing ngandhaké saka nomor-nomor karo pangaturan ribuan.
Gunakaké string `123;234;345` supaya gampang nggawé daptar nomor. Jangan nggunakaké koma minangka pangaturan karo karo bisa diartikan minangka pangaturan ribuan.
`int`, `float` lan `string` nggunakaké `is_output_list=True` (indikasi dening simbol `𝌠`) lan bakal diprosés kanthi urutan dening node sing padha.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `any` | `*` | Apa waèh sing bisa dikonversi kanthi bermakna menyang string karo nomor sing bisa dibaca |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kabèh nomor sing ditemokaké ing string karo desimal dipotong. |
| `float` | `FLOAT 𝌠` | Kabèh nomor sing ditemokaké ing string kanthi float. |
| `string` | `STRING 𝌠` | Kabèh nomor sing ditemokaké ing string kanthi float dikonversi menyang string. |
| `count` | `INT` | Jumlah nomor sing ditemokaké ing nilai. |

