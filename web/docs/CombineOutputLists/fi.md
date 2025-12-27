<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists Combinations

![OutputLists Combinations](CombineOutputLists/CombineOutputLists.png)

(ComfyUI workflow included)

Ottaa enintään 4 OutputListsia ja tuottaa niiden kaikki mahdolliset yhdistelmät.

Esimerkki: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` käyttää `is_output_list=True` (merkitty symboleilla `𝌠`) ja käsitellään vastaavien solujen mukaan järjestyksessä.

Kaikki listat ovat valinnaisia ja tyhjät listat voidaan jättää huomioimatta.

Teknisesti se laskee *karteesisen tulon* ja tuottaa jokainen yhdistelmä erikseen osiin (`unzip`), kun taas tyhjät listat korvataan `None`-arvoilla ja ne tuottavat `None` vastaavissa ulostuloksissa.

Esimerkki: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `list_a` | `*` | (valinnainen) |
| `list_b` | `*` | (valinnainen) |
| `list_c` | `*` | (valinnainen) |
| `list_d` | `*` | (valinnainen) |

### Ulostulokset

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Yhdistelmien arvo, jotka vastaavat `list_a`. |
| `unzip_b` | `* 𝌠` | Yhdistelmien arvo, jotka vastaavat `list_b`. |
| `unzip_c` | `* 𝌠` | Yhdistelmien arvo, jotka vastaavat `list_c`. |
| `unzip_d` | `* 𝌠` | Yhdistelmien arvo, jotka vastaavat `list_d`. |
| `index` | `INT 𝌠` | 0..count -alue, jota voidaan käyttää indeksiksi. |
| `count` | `INT` | Yhdistelmien kokonaisluku. |

