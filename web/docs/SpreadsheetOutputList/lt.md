## Išdėstymo lentelės išvesties sąrašas

![Išdėstymo lentelės išvesties sąrašas](SpreadsheetOutputList/SpreadsheetOutputList.png)

(ComfyUI darbo eiga įtraukta)

Sukuria kelis išvesties sąrašus iš išdėstymo lentelės (`.csv .tsv .ods .xlsx .xls`).
Galite naudoti `Įkelti bet kokį failą` mazgą failui įkelti base64 kodavimu.
Viduje naudoja *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) ir [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) išdėstymo lentelės failams įkelti.
Visi sąrašai naudoja `is_output_list=True` (žymima simboliu `𝌠`) ir bus apdorojami iš eilės atitinkamais mazgais.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `eilutės_ir_stulpeliai` | `EILUTĖ` | Eilučių ir stulpelių indeksai ir pavadinimai išdėstymo lentelėje. Atminkite, kad išdėstymo lentelėse eilutės prasideda nuo 1, stulpeliai prasideda nuo A, o išvesties sąrašai yra 0-pagrindiniai (su `pasirinkti-n-tą`). |
| `antraštės_eilutės` | `SANDĖLIS` | Ignoruoti pirmas x eilutes sąraše. Naudojama tik tada, kai nurodote stulpelį su `eilutės_ir_stulpeliai`. |
| `antraštės_stulpeliai` | `SANDĖLIS` | Ignoruoti pirmus x stulpelius sąraše. Naudojama tik tada, kai nurodote eilutę su `eilutės_ir_stulpeliai`. |
| `pasirinkti_n-tą` | `SANDĖLIS` | Pasirinkti tik n-tą įrašą (0-pagrindinis). Naudinga kartu su `PrimitiveInt+control_after_generate=increment` šablonu. |
| `eilutė_arba_base64` | `EILUTĖ` | CSV/TSV eilutė arba išdėstymo lentelės failas base64 (su `.ods .xlsx .xls`). Naudokite `Įkelti bet kokį failą` mazgą failui įkelti base64. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `sąrašas_a` | `EILUTĖ 𝌠` |  |
| `sąrašas_b` | `EILUTĖ 𝌠` |  |
| `sąrašas_c` | `EILUTĖ 𝌠` |  |
| `sąrašas_d` | `EILUTĖ 𝌠` |  |
| `skaičius` | `SANDĖLIS` | Elementų skaičius ilgiausiai sąraše. |

