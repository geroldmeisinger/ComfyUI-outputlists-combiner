## Teisenda täisarvuks, ujukomaarvuks ja sõngruks

![Teisenda täisarvuks, ujukomaarvuks ja sõngruks](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI töövoog on kaasatud)

Teisendab kõik arvulised väärtused `INT` `FLOAT` `STRING` tüüpi.
Kasutab sisemiselt `nums_from_string.get_nums` meetodit, mis on väga lubav arvude suhtes, mida see aktsepteerib. Kõik alates tegelike täisarvudest, tegelikest ujukomaarvudest, täisarvudest või ujukomaarvudest sõnena, sõnadest, mis sisaldavad mitmeid arve koos tuhandete eraldajadega.
Kasuta sõne `123;234;345`, et kiiresti genereerida arvude loend. Ära kasuta komme eraldajana, kuna need võivad tõlgendada tuhandete eraldajatena.
`int`, `float` ja `string` kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `any` | `*` | Midagi, mis saab mõistlikult teisendada sõnks, mis sisaldab analüüsida saadavaid arve |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Kõik stringis leitud arvud, kus komakohtade lõikamine on tehtud. |
| `float` | `FLOAT 𝌠` | Kõik stringis leitud arvud ujukomaarvudena. |
| `string` | `STRING 𝌠` | Kõik stringis leitud arvud ujukomaarvudena teisendatuna sõnks. |
| `count` | `INT` | Arvude arv väärtuses leitud. |

