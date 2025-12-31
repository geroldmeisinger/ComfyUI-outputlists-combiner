## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI-työnkulku mukana)

Luo OutputListin purkamalla taulukot tai sanakirjat JSON-objekteista.
Käyttää JSONPath-syntaksia arvojen purkamiseen, katso [JSONPath Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Kaikki täsmäävät arvot tasoitetaan yhdeksi pitkäksi listaksi.
Voit myös käyttää tätä solmua luodaksesi objekteja literaalimerkkijonoista, kuten `[1, 2, 3]`.
`key`, `value`, `int` ja `float` käyttävät `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, jota käytetään arvojen purkamiseen. |
| `json` | `STRING` | JSON-merkkijono, joka muutetaan objektiksi. |
| `obj` | `*` | (valinnainen) mikä tahansa tyyppi oleva objekti, joka korvaa JSON-merkkijonon |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Avain sanakirjoille tai indeksi taulukoille (merkkijonona). Teknisesti se on globaali indeksi tasoitetusta listasta kaikille ei-avaimille. |
| `value` | `STRING 𝌠` | Arvo merkkijonona. |
| `int` | `INT 𝌠` | Arvo kokonaislukuna (jos ei voi jäsentää lukua, oletusarvona 0). |
| `float` | `FLOAT 𝌠` | Arvo desimaalilukuna (jos ei voi jäsentää lukua, oletusarvona 0). |
| `count` | `INT` | Yhteensä kohteita tasoitetussa listassa |
| `debug` | `STRING` | Virheenkorjausulostus kaikista täsmäävistä objekteista muotoiltuna JSON-merkkijonona |

