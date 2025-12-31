## Kombinazzjonijiet tal-Listen tal-Uscita

![Kombinazzjonijiet tal-Listen tal-Uscita](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inkluddat)

Jibbaq 4 OutputLists fil-massimu u jibbni koll kombinazzjonijiet tagħhom.

Eżempju: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` jibbażaw fuq `is_output_list=True` (indikat bil-simbolu `𝌠`) u jipperċessaw sekwenzjalment minn nodi korrispondenti.

Koll il-listen huma opzjonali u el-listi vojti jinżlu.

Teknikament jikkomputa *il-prodott kartiżjan* u jibbni kull kombinazzjoni mbżonnita f’elementi tagħha (`unzip`), wħall-listi vojti jinbidlu bil-unità ta’ `None` u jibbini `None` fuq l-uscita rispettiva.

Eżempju: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Input

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `list_a` | `*` | (opzjonali) |
| `list_b` | `*` | (opzjonali) |
| `list_c` | `*` | (opzjonali) |
| `list_d` | `*` | (opzjonali) |

### Output

| Isem | Tip | Deskrizzjoni |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valur tal-kombinazzjonijiet korrispondenti għall-`list_a`. |
| `unzip_b` | `* 𝌠` | Valur tal-kombinazzjonijiet korrispondenti għall-`list_b`. |
| `unzip_c` | `* 𝌠` | Valur tal-kombinazzjonijiet korrispondenti għall-`list_c`. |
| `unzip_d` | `* 𝌠` | Valur tal-kombinazzjonijiet korrispondenti għall-`list_d`. |
| `index` | `INT 𝌠` | Gamma ta’ 0..count li tista’ tintużax bħala indeks. |
| `count` | `INT` | Numru totali tal-kombinazzjonijiet. |

