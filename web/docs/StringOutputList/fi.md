## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI-työnkulku mukana)

Luo OutputListin jakamalla merkkijono tekstikentässä erottimella.
`value` ja `index` käyttävät `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `separator` | `STRING` | Merkkijono, jolla jaetaan tekstikentän arvot. |
| `values` | `STRING` | Teksti, jonka haluat jakaa listaksi. Huomaa, että merkkijono leikataan pois lopuista uusista rivinä ennen jakamista, ja jokainen kohde leikataan pois välilyönnistä uudelleen. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `value` | `* 𝌠` | Arvot listasta. |
| `index` | `INT 𝌠` | Alue 0..count. Voit käyttää tätä indeksinä. |
| `count` | `INT` | Kohteiden määrä listassa. |
| `inspect_combo` | `COMBO` | Tyhjä tuloste, johon voit yhdistää `COMBO`-solmuun ja esitäyttää sen arvoilla. Yhteys uudelleenlinkitetään automaattisesti `value`-tulosteeseen. |

