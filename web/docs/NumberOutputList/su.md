## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow anu kalebet)

Nggawé OutputList nu nganggo kumpulan nilai numerik.
Nganggo [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) di dalamna, sabab éta beKERJA leuwih andal pikeun nilai floating-point.
Upami anjeun pengen mameutkeun daptar angka nu mawa langkah anu acak, cek JSON OutputList jeung mameutkeun array, conto: `[1, 42, 123]`.
`int`, `float`, `string` jeung `index` nganggo `is_output_list=True` (diwatesan ku simbol `𝌠`) jeung bakal diprosés secara urutan ku node nu cocog.

### Input

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `start` | `FLOAT` | Nilai mimiti pikeun ngahasilkeun rentang éta. |
| `stop` | `FLOAT` | Nilai akhir. Upami `endpoint=include` makan angka ieu bakal kalebet dina daptar. |
| `num` | `INT` | Jumlah item dina daptar (jangan pikeun ngeconfuse ku `step`). |
| `endpoint` | `BOOLEAN` | Ngadetéminasi apakah nilai `stop` kudu kalebet atanapi dilarang dina item. |

### Output

| Nama | Tipe | Deskripsi |
| --- | --- | --- |
| `int` | `INT 𝌠` | Nilai nu dijadikeun ka int (dibulatkeun sarta di floor). |
| `float` | `FLOAT 𝌠` | Nilai salaku float. |
| `string` | `STRING 𝌠` | Nilai salaku float dijadikeun ka string. |
| `index` | `INT 𝌠` | Rentang 0..count nu bisa dipaké salaku index. |
| `count` | `INT` | Sama keur `num`. |

