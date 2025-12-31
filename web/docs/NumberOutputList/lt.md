## Skaičius išvesties sąrašas

![Skaičius išvesties sąrašas](NumberOutputList/NumberOutputList.png)

(ComfyUI darbo eiga įtraukta)

Sukuria išvesties sąrašą su skaitmeninėmis reikšmėmis.
Viduje naudoja [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), nes jis veikia patikimesniu būdu su slankaus kablelio reikšmėmis.
Jei norite apibrėžti skaičių sąrašus su bet kokia žingsnio reikšme, žiūrėkite JSON išvesties sąrašą ir apibrėžkite masyvą, pavyzdžiui `[1, 42, 123]`.
`int`, `float`, `string` ir `index` naudoja `is_output_list=True` (žymima simboliu `𝌠`) ir bus apdorojami iš eilės atitinkamais mazgais.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `pradžia` | `DEŠIMTAINIS` | Pradžios reikšmė, iš kurios generuojamas diapazonas. |
| `pabaiga` | `DEŠIMTAINIS` | Pabaigos reikšmė. Jei `endpoint=include`, tada šis skaičius įtraukiamas į sąrašą. |
| `skaičius` | `SANDĖLIS` | Elementų skaičius sąraše (nesuklastokite su `žingsnis`). |
| `pabaiga` | `BOOLEAN` | Nusprendžia, ar `pabaigos` reikšmė turėtų būti įtraukta ar išimta iš elementų. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `sandaus` | `SANDĖLIS 𝌠` | Reikšmė, konvertuota į sandėlį (apvalinta žemyn/pusė). |
| `slankus` | `DEŠIMTAINIS 𝌠` | Reikšmė kaip slankusis kablelis. |
| `eilutė` | `EILUTĖ 𝌠` | Reikšmė kaip slankusis kablelis, konvertuota į eilutę. |
| `indeksas` | `SANDĖLIS 𝌠` | 0..skaičius diapazonas, kuris gali būti naudojamas kaip indeksas. |
| `skaičius` | `SANDĖLIS` | Toks pats kaip `skaičius`. |

