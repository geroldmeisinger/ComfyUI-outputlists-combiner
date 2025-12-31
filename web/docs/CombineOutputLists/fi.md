## OutputLists-yhdistelmät

![OutputLists-yhdistelmät](CombineOutputLists/CombineOutputLists.png)

(ComfyUI-työnkulku mukana)

Ottaa enintään 4 OutputListiä ja tuottaa niistä kaikki mahdolliset yhdistelmät.

Esimerkki: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` käyttää `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

Kaikki listat ovat valinnaisia ja tyhjät listat ohitetaan.

Teknisesti tämä laskee *Cartesian product* ja tulostaa jokaisen yhdistelmän eri elementteihin jaettuna (`unzip`), kun taas tyhjät listat korvataan yksiköillä `None` ja ne tulostavat `None` vastaavalle tulostusportille.

Esimerkki: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `list_a` | `*` | (valinnainen) |
| `list_b` | `*` | (valinnainen) |
| `list_c` | `*` | (valinnainen) |
| `list_d` | `*` | (valinnainen) |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Yhdistelmien arvo, joka vastaa `list_a`:a. |
| `unzip_b` | `* 𝌠` | Yhdistelmien arvo, joka vastaa `list_b`:a. |
| `unzip_c` | `* 𝌠` | Yhdistelmien arvo, joka vastaa `list_c`:a. |
| `unzip_d` | `* 𝌠` | Yhdistelmien arvo, joka vastaa `list_d`:a. |
| `index` | `INT 𝌠` | Alue 0..count, jota voidaan käyttää indeksinä. |
| `count` | `INT` | Yhdistelmien kokonaismäärä. |

