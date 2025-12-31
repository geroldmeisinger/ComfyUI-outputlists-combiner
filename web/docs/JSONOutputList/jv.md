## OutputList JSON

![OutputList JSON](JSONOutputList/JSONOutputList.png)

(Workflow ComfyUI kalebu)

Nggawé OutputList kanthi ngambil array utawa dictionari saka objèk JSON.
Nggunakaké sintak JSONPath supaya ngambil nilai, deleng [JSONPath ing Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Kabèh nilai sing cocok diflatten menyang daptar sing dawa.
Sampeyan bisa nggunakaké node iki supaya nggawé objèk saka string literal kaya `[1, 2, 3]`.
`key`, `value`, `int` lan `float` nggunakaké `is_output_list=True` (indikasi dening simbol `𝌠`) lan bakal diprosés kanthi urutan dening node sing padha.

### Input

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath sing nggunakaké supaya ngambil nilai. |
| `json` | `STRING` | String JSON sing ditranslasikan menyang objèk. |
| `obj` | `*` | (opsional) objèk saka tipe apa waèh sing bakal ngganti string JSON |

### Output

| Jeneng | Tipe | Description |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kunci kanggo dictionari utawa index kanggo array (minangka string).  Secara teknis iki kaya index global saka daptar sing diflatten kanggo kabèh sing ora kunci. |
| `value` | `STRING 𝌠` | Nilai minangka string. |
| `int` | `INT 𝌠` | Nilai minangka int (yen ora bisa ngurai nomor, bakal nggunakaké 0). |
| `float` | `FLOAT 𝌠` | Nilai minangka float (yen ora bisa ngurai nomor, bakal nggunakaké 0). |
| `count` | `INT` | Jumlah total item ing daptar sing diflatten |
| `debug` | `STRING` | Output debug saka kabèh objèk sing cocok minangka string JSON sing diforomat |

