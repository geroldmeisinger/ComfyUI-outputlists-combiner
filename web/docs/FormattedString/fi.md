## Muotoiltu merkkijono

![Muotoiltu merkkijono](FormattedString/FormattedString.png)

(ComfyUI-työnkulku mukana)

Luo merkkijonon, joka sisältää paikkatunnusmuuttujia ja korvaa ne vastaavilla arvoilla.
Käyttää sisäisesti pythonin `str.format()` -toimintoa, katso [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .
* Voit käyttää `{a:.2f}` pyöristääksesi desimaaliluvun kahdeksi desimaaliksi.
* Voit käyttää `{a:05d}` täyttääksesi enintään viisi etunollaa sopiaksesi Comfyn tiedostonimen jälkiliitteeseen `ComfyUI_00001_.png`.
* Jos haluat kirjoittaa `{ }` merkkijonoihin (esim. JSON:eihin), sinun täytyy kaksinkertaistaa ne: `{{ }}`.

Soveltuu myös *haku- ja korvaa (H&K)* -syntaksiin, kuten `%date:yyyy-MM-dd hh:mm:ss%` ja `%KSampler.seed%`.
Voit käyttää sitä myös `GET-solmuna`.
Huomaa, että "haku ja korvaa" tapahtuu Javascript-yhteydessä ja suoritetaan ennen solmun suoritusta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `fstring` | `STRING` | Luo merkkijonon, joka sisältää paikkatunnusmuuttujia ja korvaa ne vastaavilla arvoilla.<br>Käyttää sisäisesti pythonin `str.format()` -toimintoa, katso [Python - Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax) .<br>* Voit käyttää `{a:.2f}` pyöristääksesi desimaaliluvun kahdeksi desimaaliksi.<br>* Voit käyttää `{a:05d}` täyttääksesi enintään viisi etunollaa sopiaksesi Comfyn tiedostonimen jälkiliitteeseen `ComfyUI_00001_.png`.<br>* Jos haluat kirjoittaa `{ }` merkkijonoihin (esim. JSON:eihin), sinun täytyy kaksinkertaistaa ne: `{{ }}`.<br><br>Soveltuu myös *haku- ja korvaa (H&K)* -syntaksiin, kuten `%date:yyyy-MM-dd hh:mm:ss%` ja `%KSampler.seed%`.<br>Voit käyttää sitä myös `GET-solmuna`.<br>Huomaa, että "haku ja korvaa" tapahtuu Javascript-yhteydessä ja suoritetaan ennen solmun suoritusta. |
| `a` | `*` | (valinnainen) arvo, joka muutetaan merkkijonoksi paikkatunnukseen `{a}`. |
| `b` | `*` | (valinnainen) arvo, joka muutetaan merkkijonoksi paikkatunnukseen `{b}`. |
| `c` | `*` | (valinnainen) arvo, joka muutetaan merkkijonoksi paikkatunnukseen `{c}`. |
| `d` | `*` | (valinnainen) arvo, joka muutetaan merkkijonoksi paikkatunnukseen `{d}`. |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `string` | `STRING` | Muotoiltu merkkijono, jossa kaikki paikkatunnukset on korvattu vastaavilla arvoilla. |

