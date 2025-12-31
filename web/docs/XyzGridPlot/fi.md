## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(ComfyUI-työnkulku mukana)

Luo XYZ-Gridplotin kuvien listasta.
Se ottaa kuvien listan (mukaan lukien erätyöt) ja litistää ne ensin pitkäksi listaksi (joten `batch_size=1`).

**Ruudukon muoto**
Määrittää ruudukon muodon seuraavasti:
1. rivien nimikkeiden määrä
2. sarakkeiden nimikkeiden määrä
3. jäljellä olevat alakuvat.
Voit käyttää `order=inside_out` kääntääksesi kuvan valinnan (hyödyllinen, jos `batch_size>1` ja haluat nimetä erätyöt).

**Tasaus**
* Jos nimike menee seuraavalle riville, koko akseli kohdellaan "moniriviseksi" ja ne tasataan ylös oikein-tyylisellä välistä.
* Jos kaikki nimikkeet ovat numeroita tai kaikki päättyvät numeroihin (esim. `strength: 1.`), koko akseli kohdellaan "numeeriseksi" ja ne tasataan oikealle.
* Kaikki muut tekstit kohdellaan "yksiriviseksi" ja ne tasataan keskelle.
* Tasaa yksiriviset ja numeeriset nimikkeet sarakkeisiin alhaalla ja riveihin keskelle pystysuunnassa.

**Fonttikoko**
* Sarakkeen nimikkeen alueen korkeus määräytyy `font_size` tai `puolet suurimmasta alakuvien pakkauskorkeudesta jossain rivissä` (molemmat suuremmat).
* Rivin nimikkeen alueen leveys määräytyy suurimman alakuvien pakkausleveyden mukaan (vähimmäinen 256px).
* Teksti pienenee kunnes se mahtuu (alaspäin `font_size_min=6`) ja käyttää samaa fonttikokoa koko akselille (rivin nimikkeet tai sarakkeen nimikkeet).
Jos fonttikoko on jo minimissä, leikkaa jäljelle jäävän tekstin.

**Alakuvien pakkaus**
Muotoilee alakuvat (yleensä erätyöistä) eniten neliöksi alueeksi ("alakuvien pakkaus"), ellei `output_is_list=True`, jolloin käyttää vain yhden kuvan jokaisessa solussa ja luo koko kuvien ruudukkojen listan.
Voit käyttää tätä kuvien ruudukkojen listaa yhdistääksesi toisen XyzGridPlot-solmun luodaksesi yliruudukkoja.
Jos alakuvat koostuvat eri kokoisista erätyöistä, täyttää puuttuvat solut tyhjillä kuville.
Kuvia solussa (mukaan lukien erätyöt) täytyy olla moninkertaista `rows * columns`.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `images` | `IMAGE` | Kuvien lista (mukaan lukien erätyöt) |
| `row_labels` | `*` | Rivin nimikkeiden tekstit vasemmalla puolella |
| `col_labels` | `*` | Sarakkeen nimikkeiden tekstit ylhäällä |
| `gap` | `INT` | Etäisyys alakuvien pakkausten välillä. Huomaa, että alakuvien sisällä ei ole väliä. Jos haluat välin alakuvien välillä, yhdistä toinen XyzGridPlot-solmu. |
| `font_size` | `FLOAT` | Kohde fonttikoko. Teksti pienenee kunnes se mahtuu (alaspäin `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Rivin nimikkeiden tekstin suunta. Hyödyllinen, jos haluat säästää tilaa. |
| `order` | `BOOLEAN` | Määrittää kuvien käsittelyjärjestyksen. Tämä on vain relevantti, jos sinulla on alakuvia. Hyödyllinen, jos `batch_size>1` ja haluat piirtää erätyöt. |
| `output_is_list` | `BOOLEAN` | Tämä on vain relevantti, jos sinulla on alakuvia tai haluat luoda yliruudukkoja. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | XYZ-GridPlot kuva. Jos `output_is_list=True`, luo kuvien listan, johon voit yhdistää toisen XYZ-GridPlot-solmun luodaksesi yliruudukkoja. |

