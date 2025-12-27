<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Combinacion de OutputLists

![Combinacion de OutputLists](CombineOutputLists/CombineOutputLists.png)

(Workflow de ComfyUI inclusu)

Toghe a 4 OutputLists e genera cada combinacion de e.

Esempio: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` usan `is_output_list=True` (indicadu cun sìmbolo `𝌠`) e seran processadu sequentzialmente cun nodu corrispondente.

Tutu listas sunt opzionali e listas bìtus sunt ignoradas.

Tècnicamente cunputa *prodotu cartesianu* e emite cada combinacion sìpàrada in e elementus (`unzip`), in canu listas bìtus sunt sostituidas cun unitas de `None` e emeten `None` in sa uscita corrispondente.

Esempio: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inputos

| Isu | Tipu | Descripcione |
| --- | --- | --- |
| `list_a` | `*` | (opzionali) |
| `list_b` | `*` | (opzionali) |
| `list_c` | `*` | (opzionali) |
| `list_d` | `*` | (opzionali) |

### Ouscitas

| Isu | Tipu | Descripcione |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Valore de sa combinacion corrispondente a `list_a`. |
| `unzip_b` | `* 𝌠` | Valore de sa combinacion corrispondente a `list_b`. |
| `unzip_c` | `* 𝌠` | Valore de sa combinacion corrispondente a `list_c`. |
| `unzip_d` | `* 𝌠` | Valore de sa combinacion corrispondente a `list_d`. |
| `index` | `INT 𝌠` | Rangu de 0..count chi podet esse usadu cun indixe. |
| `count` | `INT` | Numeru totale de combinacion. |

