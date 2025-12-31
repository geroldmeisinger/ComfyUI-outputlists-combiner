## Izpisi Seznamov - Kombinacije

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow vključen)

Vzame do 4 sezname izpisa in ustvari vse kombinacije med njimi.

Primer: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` uporablja `is_output_list=True` (označeno z simbolom `𝌠`) in bodo obdelani zaporedno z ustreznimi vozli.

Vsi seznami so izbirni in prazni seznami bodo prezrani.

Tekoče izračuna *Kartezični produkt* in izpise vsako kombinacijo ločeno na svoje elemente (`unzip`), pri čemer bodo prazni seznami zamenjani z enotami `None`, ki bodo izpustile `None` na ustreznem izhodu.

Primer: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `list_a` | `*` | (izbirno) |
| `list_b` | `*` | (izbirno) |
| `list_c` | `*` | (izbirno) |
| `list_d` | `*` | (izbirno) |

### Izpisi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Vrednost kombinacij, ki ustrezajo `list_a`. |
| `unzip_b` | `* 𝌠` | Vrednost kombinacij, ki ustrezajo `list_b`. |
| `unzip_c` | `* 𝌠` | Vrednost kombinacij, ki ustrezajo `list_c`. |
| `unzip_d` | `* 𝌠` | Vrednost kombinacij, ki ustrezajo `list_d`. |
| `index` | `INT 𝌠` | Obseg 0..count, ki se lahko uporabi kot kazalo. |
| `count` | `INT` | Skupno število kombinacij. |

