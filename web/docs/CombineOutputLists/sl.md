<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## Kombinacije OutputList-ov

![Kombinacije OutputList-ov](CombineOutputLists/CombineOutputLists.png)

(vključen workflow ComfyUI)

Prijemlja do 4 OutputList in generira vse kombinacije med njimi.

Primer: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` do `unzip_d` uporabljajo `is_output_list=True` (označeno z simbolom `𝌠`) in bodo posredovane po vrsti preko odgovarjajočih vozlišč.

Vse sezname so nepotrebni in prazni seznama bodo zanemarjeni.

Teoretično izračuna *kartezijev produkt* in izpiše vsako kombinacijo razdeljeno na elemente (`unzip`), medtem ko bodo prazni seznama zamenjani z `None` in bodo izpustili `None` na odgovarjajočem izhodu.

Primer: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Vhodni podatki

| Ime | Tip | Opis |
| --- | --- | --- |
| `list_a` | `*` | (neobvezno) |
| `list_b` | `*` | (neobvezno) |
| `list_c` | `*` | (neobvezno) |
| `list_d` | `*` | (neobvezno) |

### Izhodni podatki

| Ime | Tip | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Vrednost kombinacij, ki odgovarjajo `list_a`. |
| `unzip_b` | `* 𝌠` | Vrednost kombinacij, ki odgovarjajo `list_b`. |
| `unzip_c` | `* 𝌠` | Vrednost kombinacij, ki odgovarjajo `list_c`. |
| `unzip_d` | `* 𝌠` | Vrednost kombinacij, ki odgovarjajo `list_d`. |
| `index` | `INT 𝌠` | Rang 0..count, ki ga lahko uporabimo kot indeks. |
| `count` | `INT` | Skupno število kombinacij. |

