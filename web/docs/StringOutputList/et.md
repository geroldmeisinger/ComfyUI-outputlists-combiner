## Stringi väljundloend

![Stringi väljundloend](StringOutputList/StringOutputList.png)

(ComfyUI töövoog on kaasatud)

Loob väljundloendi, mida jagatakse tekstivälja stringi jaoturiga.
`value` ja `index` kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `separator` | `STRING` | String, mida kasutatakse tekstivälja väärtuste jagamiseks. |
| `values` | `STRING` | Tekst, mida soovid loendisse jagada. Pange tähele, et string lõigatakse enne jagamist lõpust uute ridade eest ja iga üksus lõigatakse uuesti tühikute eest. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `value` | `* 𝌠` | Loendi väärtused. |
| `index` | `INT 𝌠` | Vahemik 0..count. Saad seda kasutada indeksina. |
| `count` | `INT` | Loendi elementide arv. |
| `inspect_combo` | `COMBO` | Dummy-väljund, mida saad kasutada ühendada `COMBO` ja eelseadistada selle väärtustega. Ühendus ühendatakse automaatselt uuesti `value` väljundisse. |

