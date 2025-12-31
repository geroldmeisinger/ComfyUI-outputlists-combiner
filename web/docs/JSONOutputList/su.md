## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow included)

Ngahasilkeun OutputList ku ngaluarakeun array atanapi dictionary tina objék JSON.
Ngagunakeun sintaks JSONPath undeg ngaluarakeun nilai, liat [JSONPath di Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Sadaya nilai anu cocog dilarapkeun jadi hiji list anu panjang.
Anjeun ogé bisa nganggo ieu node undeg ngahasilkeun objék tina string literal sapertos `[1, 2, 3]`.
`key`, `value`, `int` jeung `float` ngagunakeun `is_output_list=True` (indikasi ku simbol `𝌠`) jeung bakal diprosés secara berurutan ku node anu cocog.

### Input

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath anu digunakeun undeg ngaluarakeun nilai. |
| `json` | `STRING` | String JSON anu ditranslasikeun jadi objék. |
| `obj` | `*` | (opsional) objék sarta jenis na anu bakal ngaluarakeun string JSON |

### Output

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Kunci undeg dictionary atanapi index undeg array (sakumaha string). Secara teknis ieu mangrupakeun index global tina list anu dilarapkeun pikeun sadaya anu sanés kunci. |
| `value` | `STRING 𝌠` | Nilai sakumaha string. |
| `int` | `INT 𝌠` | Nilai sakumaha int (upamana henteu bisa nganalisis angka, bakal nganggo nilai 0). |
| `float` | `FLOAT 𝌠` | Nilai sakumaha float (upamana henteu bisa nganalisis angka, bakal nganggo nilai 0). |
| `count` | `INT` | Jumlah total item dina list anu dilarapkeun |
| `debug` | `STRING` | Output debug tina sadaya objék anu cocog sakumaha string JSON anu diformat

