## Muunna kokonaisluvuksi, desimaaliluvuksi, merkkijonoksi

![Muunna kokonaisluvuksi, desimaaliluvuksi, merkkijonoksi](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI-työnkulku mukana)

Muuntaa kaiken luvullisen muotoisen `INT` `FLOAT` `STRING`.
Käyttää sisäisesti `nums_from_string.get_nums` -toimintoa, joka on erittäin suvaitsevainen hyväksyessään lukuja. Hyväksyy kaiken: oikeat kokonaisluvut, oikeat desimaaliluvut, kokonais- tai desimaaliluvut merkkijonoina, merkkijonot, jotka sisältävät useita numeroita tuhaterottimilla.
Käytä merkkijonoa `123;234;345` luodaksesi nopeasti listan numeroista. Älä käytä pilkkuja erotinmerkkeinä, koska ne saattavat tulkita tuhaterottimina.
`int`, `float` ja `string` käyttävät `is_output_list=True` (merkitty symbolilla `𝌠`) ja ne käsitellään peräkkäin vastaavien solmujen toimesta.

### Syötteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `any` | `*` | Mikä tahansa, mikä voidaan järkevästi muuttaa merkkijonoksi, jossa on jäsennettäviä lukuja |

### Tulosteet

| Nimi | Tyyppi | Kuvaus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kaikki merkkijonosta löydetyt luvut, desimaalit poistettuna. |
| `float` | `FLOAT 𝌠` | Kaikki merkkijonosta löydetyt luvut desimaalilukuna. |
| `string` | `STRING 𝌠` | Kaikki merkkijonosta löydetyt luvut desimaalilukuna muutettuna merkkijonoksi. |
| `count` | `INT` | Arvosta löydettyjen lukujen määrä. |

