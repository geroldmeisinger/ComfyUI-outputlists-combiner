<!-- This file was auto-translated with a local LLM and last updated on 2025-12-28. -->
## Konvertuoti į Int, Float, Str

![Konvertuoti į Int, Float, Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI workflow included)

Konvertuoja kiekvieną skaičių panašią reikšmę į `INT`, `FLOAT`, `STRING`.
Vykdo `nums_from_string.get_nums` iš vidaus, kuris labai atleidžia skaičius, kuriuos priima. Visi skaičiai – tikroji int, tikroji float, int arba float kaip string, stringai, kurie turi kelių skaičių su tūkstančių skaitmenimis.
Naudojant stringą `123;234;345`, greitai gauti skaičių listą. Ne naudok komate kaip skaitmenų skirstymo ženklą, nes jie gali būti interpretuojami kaip tūkstančių skaitmenys.
`int`, `float` ir `string` naudoja `is_output_list=True` (pažymėta simboliu `𝌠`) ir bus procesuojami seka į atitinkamus node'us.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `any` | `*` | Ką nors, ką galima pritaikyti į stringą su pritaikomais skaičiais viduje |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `int` | `INT 𝌠` | Visi rastieji skaičiai stringe su dešimtainiais skaitmenimis ištrintais. |
| `float` | `FLOAT 𝌠` | Visi rastieji skaičiai stringe kaip float. |
| `string` | `STRING 𝌠` | Visi rastieji skaičiai stringe kaip float pakeisti į stringą. |
| `count` | `INT` | Skaičius rastų skaičių reikšmėje. |

