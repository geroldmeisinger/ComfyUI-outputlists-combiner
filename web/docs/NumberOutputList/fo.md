## Tal OutputList

![Tal OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow íðgu)

Gerir einn OutputList við eimum talaværdi.
Nýtir [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) innanlandsum, tíðan virkar meira ítrúligt við fleytital. 
Um tú ynskir at skilja talalistir við hvørjum skrefum, tí skoða JSON OutputList og skil einn lista, t.d. `[1, 42, 123]`.
`int`, `float`, `string` og `index` nýtir `is_output_list=True` (merkt við symbolið `𝌠`) og verða handtert í fylgjandi rætta av samsvarandi nodes.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `start` | `FLOAT` | Byrjunartal, ið nýtist til at gerða umráðið frá. |
| `stop` | `FLOAT` | Endital. Um `endpoint=include` så er tað talin inklúderð í lista. |
| `num` | `INT` | Tal av itemum í lista (ikki taka tað við sum `step`). |
| `endpoint` | `BOOLEAN` | Skilur hvussu `stop` talin skal vera inklúderð ella útsløða í itemunum. |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Tað talin umskilt til int (rúnduð niður/floored). |
| `float` | `FLOAT 𝌠` | Tað talin sum fleytital. |
| `string` | `STRING 𝌠` | Tað talin sum fleytital umskilt til streng. |
| `index` | `INT 𝌠` | Umráðið 0..count, ið kann nýtast sum index. |
| `count` | `INT` | Sama sum `num`. |

