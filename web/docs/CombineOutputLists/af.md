## UitvoerLys Kombinasies

![UitvoerLys Kombinasies](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow ingesluit)

Neem tot 4 UitvoerLise en genereer elke kombinasie van hulle.

Voorbeeld: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` gebruik `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal sekwensieel deur ooreenstemmende nodes verwerk word.

Alle lise is opsioneel en leë lise sal geïgnoreer word.

Teksniek bereken *die Cartesiese produk* en gee elke kombinasie opgesplit in hulle elemente (`unzip`), terwyl leë lise vervang sal word met eenhede van `None` en hulle sal `None` afgee op die ooreenstemmende uitvoer.

Voorbeeld: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Invoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `list_a` | `*` | (opsioneel) |
| `list_b` | `*` | (opsioneel) |
| `list_c` | `*` | (opsioneel) |
| `list_d` | `*` | (opsioneel) |

### Uitvoere

| Naam | Tipe | Beskrywing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Waarde van die kombinasies wat ooreenstem met `list_a`. |
| `unzip_b` | `* 𝌠` | Waarde van die kombinasies wat ooreenstem met `list_b`. |
| `unzip_c` | `* 𝌠` | Waarde van die kombinasies wat ooreenstem met `list_c`. |
| `unzip_d` | `* 𝌠` | Waarde van die kombinasies wat ooreenstem met `list_d`. |
| `index` | `INT 𝌠` | Reeks van 0..aantal wat as 'n indeks gebruik kan word. |
| `count` | `INT` | Totale aantal kombinasies. |

