## Combinatziones de lista de àrtigos

![Combinatziones de lista de àrtigos](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow inclùidu)

Pigat finas a 4 lista de àrtigos e generat cada combinatzione de elas.

Esempiu: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` impreadu `is_output_list=True` (indikadu dae su simbolo `𝌠`) e at a èssere processadu in manera sequentziale dae nodos corrisponentes.

Todas sas listas sunt optzionales e sas listas bòidas ant a èssere ignoradas.

In manera tecnicu, custu at a calculare *su produtu cartesiu* e a impreare cada combinatzione dividida in sòrbitis elementos (`unzip`), mentres sas listas bòidas ant a èssere trocadas cun unidades de `None` e ant a emìtere `None` in s’òrtidu respetivu.

Esempiu: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Ingressos

| Nàmene | Genire | Descritzione |
| --- | --- | --- |
| `list_a` | `*` | (optzionale) |
| `list_b` | `*` | (optzionale) |
| `list_c` | `*` | (optzionale) |
| `list_d` | `*` | (optzionale) |

### Àrtigos

| Nàmene | Genire | Descritzione |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Balore de sas combinatziones corrisponentes a `list_a`. |
| `unzip_b` | `* 𝌠` | Balore de sas combinatziones corrisponentes a `list_b`. |
| `unzip_c` | `* 𝌠` | Balore de sas combinatziones corrisponentes a `list_c`. |
| `unzip_d` | `* 𝌠` | Balore de sas combinatziones corrisponentes a `list_d`. |
| `index` | `INT 𝌠` | Intervalu de 0..count chi si podet impreare comente un’ìnditze. |
| `count` | `INT` | Nùmeru totale de combinatziones. |

