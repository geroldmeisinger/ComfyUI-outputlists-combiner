## Kombinasi OutputLists

![Kombinasi OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow an dikeun)

Ngambil sapaun 4 OutputLists jeung ngahasilkeun sakabéh kombinasi tina kéné.

Conto: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` ngagunakeun `is_output_list=True` (diwatesan ku simbol `𝌠`) jeung bakal diprosés secara urutan ku node nu téntu.

Sadaya list téh opsional jeung list kosong bakal diabaikan.

Secara teknis, ieu ngahitung *produék kartésián* jeung ngahasilkeun sakabéh kombinasi nu dipisahkeun jadi eleménÉ (`unzip`), samentara list kosong bakal digantikeun ku unit `None` jeung bakal ngirim `None` kana output nu téntu.

Conto: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inputs

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `list_a` | `*` | (opsional) |
| `list_b` | `*` | (opsional) |
| `list_c` | `*` | (opsional) |
| `list_d` | `*` | (opsional) |

### Outputs

| Nama | Jenis | Deskripsi |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai tina kombinasi nu téntu kana `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai tina kombinasi nu téntu kana `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai tina kombinasi nu téntu kana `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai tina kombinasi nu téntu kana `list_d`. |
| `index` | `INT 𝌠` | Jangkauan 0..count nu bisa dipaké minangka index. |
| `count` | `INT` | Jumlah total kombinasi. |

