<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Comhtháthú OutputLists

![Comhtháthú OutputLists](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow ag an leithne)

Ag úsáid do 4 OutputList agus ag cruthaigh gach comhtháthú acu.

Sampla: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

Úsáidtear `unzip_a` .. `unzip_d` `is_output_list=True` (tugtar ar an smíbhéal `𝌠`) agus beidh iad ag feidhmiú go coinnlíneach de réir na nodanna cothrom.

Tá na liostaí uile rialta agus beidh liostaí folamh ag fágáil.

Tá sé i gceart ar an gcomhtháthú *Cartesian* agus tabharfaidh sé gach comhtháthú ar aon chéime a chuirtear i gcomhtháthú (`unzip`), agus beidh liostaí folamh ag fágáil mar chomhtháthú `None` agus beidh siad ag éileamh `None` ar an gcomhtháthú.

Sampla: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Iontrálaí

| Ainm | Cineál | Cur síos |
| --- | --- | --- |
| `list_a` | `*` | (rualta) |
| `list_b` | `*` | (rualta) |
| `list_c` | `*` | (rualta) |
| `list_d` | `*` | (rualta) |

### Iththáthú

| Ainm | Cineál | Cur síos |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Luach na comhtháthú a chuirtear i gcomhtháthú le `list_a`. |
| `unzip_b` | `* 𝌠` | Luach na comhtháthú a chuirtear i gcomhtháthú le `list_b`. |
| `unzip_c` | `* 𝌠` | Luach na comhtháthú a chuirtear i gcomhtháthú le `list_c`. |
| `unzip_d` | `* 𝌠` | Luach na comhtháthú a chuirtear i gcomhtháthú le `list_d`. |
| `index` | `INT 𝌠` | Rang ó 0..count a d’fhéadfadh é a úsáid mar ainmneach. |
| `count` | `INT` | Uimhir iomlán na comhtháthú. |

