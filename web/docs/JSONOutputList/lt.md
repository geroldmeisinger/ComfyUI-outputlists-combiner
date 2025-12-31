## JSON išvesties sąrašas

![JSON išvesties sąrašas](JSONOutputList/JSONOutputList.png)

(ComfyUI darbo eiga įtraukta)

Sukuria išvesties sąrašą ištraukiant masyvus arba žodynus iš JSON objektų.
Naudoja JSONPath sintaksę, kad ištrauktumėte reikšmes, žr. [JSONPath vikipedijoje](https://en.wikipedia.org/wiki/JSONPath) .
Visos sutampiančios reikšmės yra išplėstos į vieną ilgą sąrašą.
Taip pat galite naudoti šį mazgą, kad kurtumėte objektus iš literalių eilučių, pavyzdžiui `[1, 2, 3]`.
`key`, `value`, `int` ir `float` naudoja `is_output_list=True` (pažymėta simboliu `𝌠`) ir bus apdoroti iš eilės atitinkamais mazgais.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `jsonpath` | `EILUTĖ` | JSONPath, naudojamas reikšmėms ištraukti. |
| `json` | `EILUTĖ` | JSON eilutė, kuri yra verčiama į objektą. |
| `obj` | `*` | (neprivaloma) bet kokio tipo objektas, kuris pakeis JSON eilutę |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `raktas` | `EILUTĖ 𝌠` | Raktas žodynams arba indeksas masyvams (kaip eilutė). Techniškai tai yra globalus indeksas išplėstinio sąrašo visiems ne-raktams. |
| `reikšmė` | `EILUTĖ 𝌠` | Reikšmė kaip eilutė. |
| `sveikas` | `SVEIKAS 𝌠` | Reikšmė kaip sveikasis skaičius (jei negali išanalizuoti skaičiaus, naudoja numatytąją reikšmę 0). |
| `dešimtainis` | `DEŠIMTAINIS 𝌠` | Reikšmė kaip dešimtainis skaičius (jei negali išanalizuoti skaičiaus, naudoja numatytąją reikšmę 0). |
| `skaičius` | `SVEIKAS` | Bendras elementų skaičius išplėstame sąraše |
| `derinimas` | `EILUTĖ` | Derinimo išvestis visų sutampančių objektų kaip formatuota JSON eilutė |

