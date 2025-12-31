## Konvertuoti į sveikąjį, dešimtainį skaičių, eilutę

![Konvertuoti į sveikąjį, dešimtainį skaičių, eilutę](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(ComfyUI darbo eiga įtraukta)

Konvertuoja bet ką panašų į skaičių į `SVEIKAS` `DEŠIMTAINIS` `EILUTĖ`.
Naudoja viduje `nums_from_string.get_nums`, kuris labai leidžiamas priimti skaičius. Bet ką nuo tikrųjų sveikųjų skaičių, tikrųjų dešimtainių skaičių, sveikųjų ar dešimtainių skaičių kaip eilučių, eilučių, kurios turi kelis skaičius su tūkstantmečių skyrikliukais.
Naudokite eilutę `123;234;345`, kad greitai sugeneruotumėte skaičių sąrašą. Nenaudokite kablelių kaip skyrikliukų, nes jie gali būti interpretuojami kaip tūkstantmečių skyrikliukai.
`int`, `float` ir `string` naudoja `is_output_list=True` (pažymėta simboliu `𝌠`) ir bus apdoroti iš eilės atitinkamais mazgais.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `betkas` | `*` | Bet ką, kas gali būti prasmingai konvertuojama į eilutę su skaitmenimis |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `sveikas` | `SVEIKAS 𝌠` | Visi skaičiai, rasti eilutėje, su iškirptomis dešimtainėmis. |
| `dešimtainis` | `DEŠIMTAINIS 𝌠` | Visi skaičiai, rasti eilutėje, kaip dešimtainiai skaičiai. |
| `eilutė` | `EILUTĖ 𝌠` | Visi skaičiai, rasti eilutėje, kaip dešimtainiai skaičiai, konvertuoti į eilutę. |
| `skaičius` | `SVEIKAS` | Kiek skaičių rasta reikšmėje. |

