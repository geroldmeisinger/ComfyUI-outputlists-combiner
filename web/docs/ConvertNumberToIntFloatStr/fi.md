<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Muuta kokonaisluku, desimaaliluku ja merkkijonoksi

![Muuta kokonaisluku, desimaaliluku ja merkkijonoksi](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI -työkalu sisältyy)

Muuttaa mitä tahansa lukuun liittyvää muotoa kokonaisluvuksi, desimaaliluvuksi tai merkkijonoksi.
Käyttää sisäisesti `nums_from_string.get_nums`, joka on erittäin laajassa numeron hyväksennyksessä. Tarkoittaa todellisia kokonaislukuja, todellisia desimaalilukuja, kokonaislukuja tai desimaalilukuja merkkijonoina, merkkijonoja, joissa on useita lukuja tuhannen-erotuksilla.
Käytä merkkijonoa `123;234;345` saadaksesi nopeasti luvun listan. Älä käytä pilkkuja erotuksina, koska ne voidaan tulkita tuhannen-erotuksina.
`int`, `float` ja `string` käyttävät `is_output_list=True` (merkityksellä `𝌠`) ja käsitellään vastaavasti vastaavilla solmuilla.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `any` | `*` | Mitä tahansa, joka voidaan merkityksellisesti muuttaa merkkijonoon, jossa on tulkittavat numerot sisällä |

### Tulokset

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kaikki löydetty luvut merkkijonosta desimaalien poistettuna. |
| `float` | `FLOAT 𝌠` | Kaikki löydetty luvut merkkijonosta desimaalilukuna. |
| `string` | `STRING 𝌠` | Kaikki löydetty luvut merkkijonosta desimaalilukuna muunnettuna merkkijonoksi. |
| `count` | `INT` | Luku, joka löydetty arvosta. |

