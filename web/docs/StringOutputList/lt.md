## Eilutės išvesties sąrašas

![Eilutės išvesties sąrašas](StringOutputList/StringOutputList.png)

(ComfyUI darbo eiga įtraukta)

Sukuria išvesties sąrašą, padalijus eilutę tekstinėje laukelyje naudojant skyryklį.
`reikšmė` ir `indeksas` naudoja `is_output_list=True` (žymima simboliu `𝌠`) ir bus apdorojami iš eilės atitinkamais mazgais.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `skyryklis` | `EILUTĖ` | Eilutė, naudojama padalijus tekstinio laukelio reikšmes. |
| `reikšmės` | `EILUTĖ` | Tekstas, kurį norite padalinti į sąrašą. Atminkite, kad eilutė yra apkirptas nuo galinių naujų eilučių prieš padalijimą, o kiekvienas elementas vėl yra apkirptas nuo tarpų. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `reikšmė` | `* 𝌠` | Reikšmės iš sąrašo. |
| `indeksas` | `SANDĖLIS 𝌠` | 0..skaičius diapazonas. Galite naudoti šį kaip indeksą. |
| `skaičius` | `SANDĖLIS` | Elementų skaičius sąraše. |
| `peržiūrėti_combo` | `COMBO` | Apie tai, kad galite naudoti kaip apie „COMBO“ ir iš anksto užpildyti jo reikšmėmis. Prisijungimas bus automatiškai perjungtas į `reikšmės` išvestį. |

