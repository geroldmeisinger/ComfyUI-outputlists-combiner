## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow vključen)

Ustvari OutputList z razponom številskih vrednosti.
Uporablja notranje [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), ker deluje zanesljiveje z vrednostmi v plavajoči vejico.
Če želite definirati sezname številk z poljubnimi koraki, si oglejte JSON OutputList in definirajte matriko, npr. `[1, 42, 123]`.
`int`, `float`, `string` in `index` uporabljajo `is_output_list=True` (označeno z simbolom `𝌠`) in bodo obdelani zaporedno z ustreznimi vozlički.

### Vhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `start` | `FLOAT` | Začetna vrednost za generiranje razpona. |
| `stop` | `FLOAT` | Končna vrednost. Če `endpoint=include`, potem je ta številka vključena v seznam. |
| `num` | `INT` | Število elementov v seznamu (ne zamenjajte z `step`). |
| `endpoint` | `BOOLEAN` | Odloči, ali naj bo vrednost `stop` vključena ali izključena v elemente. |

### Izhodi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `int` | `INT 𝌠` | Vrednost pretvorjena v int (zaokroženo navzdol/odštejena). |
| `float` | `FLOAT 𝌠` | Vrednost kot float. |
| `string` | `STRING 𝌠` | Vrednost kot float pretvorjena v niz. |
| `index` | `INT 𝌠` | Razpon 0..count, ki se lahko uporabi kot kazalec. |
| `count` | `INT` | Enako kot `num`. |

