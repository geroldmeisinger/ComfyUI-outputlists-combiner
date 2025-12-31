## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow vključen)

Ustvari OutputList z izvlečenimi nizi ali slovarji iz JSON objektov.
Uporablja sintakso JSONPath za izvlečenje vrednosti, glej [JSONPath na Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Vse ujemajoče se vrednosti so razširjene v eno dolgo seznam.
To vozlišče lahko uporabite tudi za ustvarjanje objektov iz besedilnih nizov, kot je `[1, 2, 3]`.
`key`, `value`, `int` in `float` uporabljajo `is_output_list=True` (označeno z `𝌠`) in bodo obdelani zaporedno z ustreznimi vozlišči.

### Vhodi

| Ime | Tip | Opis |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, ki se uporabi za izvlečenje vrednosti. |
| `json` | `STRING` | JSON niz, ki se pretvori v objekt. |
| `obj` | `*` | (izbirno) objekt katerega koli tipa, ki nadomesti JSON niz |

### Izhodi

| Ime | Tip | Opis |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Ključ za slovarje ali indeks za nize (kot niz). Tehnično je to globalni indeks razširjenega seznama za vse, razen ključev. |
| `value` | `STRING 𝌠` | Vrednost kot niz. |
| `int` | `INT 𝌠` | Vrednost kot celo število (če števila ni mogoče razčleniti, privzeto na 0). |
| `float` | `FLOAT 𝌠` | Vrednost kot decimalno število (če števila ni mogoče razčleniti, privzeto na 0). |
| `count` | `INT` | Skupno število elementov v razširjenem seznamu |
| `debug` | `STRING` | Debug izhod vseh ujemajočih se objektov kot formatiran JSON niz |

