## Arvu väljundloend

![Arvu väljundloend](NumberOutputList/NumberOutputList.png)

(ComfyUI töövoog on kaasatud)

Loob väljundloendi numbrivahemiku numbritega.
Kasutab sisemiselt [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), kuna see toimib usaldusvääsamatult ujukomaarvudega.
Kui soovid määrata suvalise sammuga numbrite loendid, vaata JSON väljundloendit ja määratle massiiv, näiteks `[1, 42, 123]`.
`int`, `float`, `string` ja `index` kasutavad `is_output_list=True` (märgitud sümboliga `𝌠`) ja neid töödeldakse järjestikku vastavate sõlmede poolt.

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `start` | `FLOAT` | Algusväärtus, millest vahemik genereerida. |
| `stop` | `FLOAT` | Lõppväärtus. Kui `endpoint=include`, siis see number on loendis kaasatud. |
| `num` | `INT` | Loendi elementide arv (ära segi ajada sammuga). |
| `endpoint` | `BOOLEAN` | Otsustab, kas `stop` väärtus peaks olema loendis kaasatud või välja jäetud. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `int` | `INT 𝌠` | Väärtus teisendatud täisarvuks (ümardatud alla/algus). |
| `float` | `FLOAT 𝌠` | Väärtus ujukomaarvuna. |
| `string` | `STRING 𝌠` | Väärtus ujukomaarvuna teisendatuna stringiks. |
| `index` | `INT 𝌠` | 0..count vahemik, mida saab kasutada indeksina. |
| `count` | `INT` | Samasugune nagu `num`. |

