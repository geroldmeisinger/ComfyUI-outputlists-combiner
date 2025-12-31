## Comhbailte OutputLists

![Comhbailte OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow san áireamh)

Gabhann le 4 OutputLists agus giniálta gach comhbailt orthu.

Sampla: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

Úsáidtear `unzip_a` .. `unzip_d` `is_output_list=True` (sonraithe ag an t-symbol `𝌠`) agus déanfar iad a phróiseáil go sequential trí na nódanna comhfhreagracha.

Gach liosta gan riachtanach agus ní dhéanfar aithne a dhéanamh ar liostaí folaa.

Go teicneolaíochtach, ríomhar *an iarratas Cartesian* agus amharcann sé gach comhbailt sna heilpí aige (`unzip`), agus mar sin, ní dhéanfar liostaí folaa a chur ina ionadaithe `None` agus seolfar `None` ar an aschur comhfhreagrach.

Sampla: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `list_a` | `*` | (roghnach) |
| `list_b` | `*` | (roghnach) |
| `list_c` | `*` | (roghnach) |
| `list_d` | `*` | (roghnach) |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Luach na comhbailte a fhreagrann le `list_a`. |
| `unzip_b` | `* 𝌠` | Luach na comhbailte a fhreagrann le `list_b`. |
| `unzip_c` | `* 𝌠` | Luach na comhbailte a fhreagrann le `list_c`. |
| `unzip_d` | `* 𝌠` | Luach na comhbailte a fhreagrann le `list_d`. |
| `index` | `INT 𝌠` | Raon de 0..count is féidir a úsáid mar index. |
| `count` | `INT` | Iomlán na comhbailte. |

