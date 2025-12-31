## JSON väljundloend

![JSON väljundloend](JSONOutputList/JSONOutputList.png)

(ComfyUI töövoog on kaasatud)

Loob väljundloendi, ekstraktides massiivid või sõnastikud JSON objektidest.
Kasutab JSONPath süntaksit väärtuste ekstraktimiseks, vaata [JSONPath Wikipedias](https://en.wikipedia.org/wiki/JSONPath) .
Kõik sobivad väärtused lõimitakse üheks pikkaks loendiks.
Saad kasutada ka seda sõlme objektide loomiseks tähtsustest sõnadest nagu `[1, 2, 3]`.
`key`, `value`, `int` ja `float` kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, mida kasutatakse väärtuste ekstraktimiseks. |
| `json` | `STRING` | JSON sõne, mis tõlgendatakse objektiks. |
| `obj` | `*` | (valikuline) objekt igas tüüpis, mis asendab JSON sõne |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Sõnastiku või massiivi indeks (sõnena). Tehniliselt on see globaalne indeks lõimitud loendist kõigi mitte-võtmete jaoks. |
| `value` | `STRING 𝌠` | Väärtus sõnena. |
| `int` | `INT 𝌠` | Väärtus täisarvuna (kui ei saa numbri parsida, siis vaikimisi 0). |
| `float` | `FLOAT 𝌠` | Väärtus ujukomaarvuna (kui ei saa numbri parsida, siis vaikimisi 0). |
| `count` | `INT` | Üldine kogus üksusi lõimitud loendis |
| `debug` | `STRING` | Kõigi sobivate objektide silumise väljund vormindatud JSON sõnena |

