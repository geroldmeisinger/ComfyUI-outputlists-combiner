## OutputLists kombinatiónir

![OutputLists Kombinatiónir](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow viðlægt)

Takur upp til 4 OutputLists og gerir allar kombinatiónir av tær.

Dømi: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` nýtir `is_output_list=True` (merkt við symbolinum `𝌠`) og verður ræst í fylgjandi ræðu av samsvarandi nodes.

Allar listir eru valfrítt og tómar listir verða ignorerðir.

Tæknilega reiknar hon *Cartesian product* og skilar hverri kombinatión upp í einstøkum elementum (`unzip`), meðan tómar listir verða settir í staðin fyri einingar av `None` og verða að senda `None` á samsvarandi útgang.

Dømi: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inntak

| Navn | Slagur | Lýsing |
| --- | --- | --- |
| `list_a` | `*` | (valfrítt) |
| `list_b` | `*` | (valfrítt) |
| `list_c` | `*` | (valfrítt) |
| `list_d` | `*` | (valfrítt) |

### Útgangur

| Navn | Slagur | Lýsing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Virði av kombinatiónirnar samsvarandi `list_a`. |
| `unzip_b` | `* 𝌠` | Virði av kombinatiónirnar samsvarandi `list_b`. |
| `unzip_c` | `* 𝌠` | Virði av kombinatiónirnar samsvarandi `list_c`. |
| `unzip_d` | `* 𝌠` | Virði av kombinatiónirnar samsvarandi `list_d`. |
| `index` | `INT 𝌠` | Ræða frá 0..count sum kann nýtast sum index. |
| `count` | `INT` | Talsmætti kombinatiónir. |

