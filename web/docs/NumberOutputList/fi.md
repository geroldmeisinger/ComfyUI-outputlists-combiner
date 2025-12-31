## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI-työnkulku mukana)

Luo OutputListin numeeristen arvojen alueella.
Käyttää sisäisesti [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), koska se toimii luotettavammin liukuluvuilla.
Jos haluat määritellä lukuja minkä tahansa vaiheen kanssa, tarkista sijaan JSON OutputList ja määritä taulukko, esimerkiksi `[1, 42, 123]`.
`int`, `float`, `string` ja `index` käyttävät `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `start` | `FLOAT` | Alkuarvo, josta alue generoidaan. |
| `stop` | `FLOAT` | Loppuarvo. Jos `endpoint=include`, niin tämä numero sisällytetään listaan. |
| `num` | `INT` | Listan kohteiden määrä (älä sekoita sen kanssa `step`). |
| `endpoint` | `BOOLEAN` | Päättelee, pitäisikö `stop`-arvo sisällyttää tai poistaa kohteista. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Arvo muunnettuna intiksi (pyöristetty alaspäin/kerrottu). |
| `float` | `FLOAT 𝌠` | Arvo liukulukuna. |
| `string` | `STRING 𝌠` | Arvo liukulukuna muunnettuna merkkijonoksi. |
| `index` | `INT 𝌠` | Alue 0..count, jota voidaan käyttää indeksinä. |
| `count` | `INT` | Sama kuin `num`. |

