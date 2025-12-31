## Gabungan OutputLists

![Gabungan OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow ComfyUI kalebu)

Nglumpukaké kaping 4 OutputLists lan ngasilaké kabeh kombinasié.

Conto: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` nggunakaké `is_output_list=True` (diwenehi dening simbol `𝌠`) lan bakal diproses secara urut déngan node sing padha.

Kabeh daptar bisa diisi lan daptar kosong bakal diabaikan.

Secara teknis nglumpukaké *produksian Cartesius* lan nampilaké kabeh kombinasi sing wis dipisah-pisah menurut eleméné (`unzip`), sedangkan daptar kosong bakal diganti karo unit `None` lan bakal mbusak `None` ing output sing padha.

Conto: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Jeneng | Tipe | Deskripsi |
| --- | --- | --- |
| `list_a` | `*` | (opsional) |
| `list_b` | `*` | (opsional) |
| `list_c` | `*` | (opsional) |
| `list_d` | `*` | (opsional) |

### Output

| Jeneng | Tipe | Deskripsi |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Nilai saka kombinasi sing padha karo `list_a`. |
| `unzip_b` | `* 𝌠` | Nilai saka kombinasi sing padha karo `list_b`. |
| `unzip_c` | `* 𝌠` | Nilai saka kombinasi sing padha karo `list_c`. |
| `unzip_d` | `* 𝌠` | Nilai saka kombinasi sing padha karo `list_d`. |
| `index` | `INT 𝌠` | Cakupan 0..count sing bisa digunakaké minangka index. |
| `count` | `INT` | Jumlah total kombinasi. |

