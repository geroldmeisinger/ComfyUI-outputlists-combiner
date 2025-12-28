<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Verwissel Na Int, Vloei, Streng

![Verwissel Na Int, Vloei, Streng](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI werkstroom ingesluit)

Verwissel alles wat getal-lyk is na `INT` `FLOAT` `STRING`.
Gebruik `nums_from_string.get_nums` intern wat baie verskeur is in die getalle wat dit aanvaar. Alles van werklike ints, werklike floats, ints of floats as streng, streng wat meerdere getalle bevat met duisend-skeidinge.
Gebruik 'n streng `123;234;345` om 'n lys van getalle snellik te genereer. Gebruik nie kommas as scheidingsmerke want hulle kan as duisend-skeidinge geïnterpreteer word.
`int`, `float` en `string` gebruik `is_output_list=True` (aangedui deur die simbool `𝌠`) en sal oor die ooreenkomstige nodes seegewys word.

### Ingangsgegevens

| Naam | Tipe | Omschrijving |
| --- | --- | --- |
| `any` | `*` | Elke ding wat betekenisvol kan verander na 'n streng met leesbare getalle binne |

### Uitgangsgegevens

| Naam | Tipe | Omschrijving |
| --- | --- | --- |
| `int` | `INT 𝌠` | Al die getalle wat in die streng gevind is met desimale afgesny. |
| `float` | `FLOAT 𝌠` | Al die getalle wat in die streng gevind is as vloei. |
| `string` | `STRING 𝌠` | Al die getalle wat in die streng gevind is as vloei omgevoer na streng. |
| `count` | `INT` | Aantal getalle wat in die waarde gevind is. |

