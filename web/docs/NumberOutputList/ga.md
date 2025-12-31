## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow san áireamh)

Cruthaíonn OutputList le raon luachanna uimhriúla.
Úsáideann [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) de réir teachtaireachta, toisc go oibríonn sé níosDearbh le luachanna float.
Má tá ag teastáil uait liostaí uimhreacha a shonrú le ceannanna ar bith, seiceáil an JSON OutputList agus sonraigh array, e.g. `[1, 42, 123]`.
Úsáideann `int`, `float`, `string` agus `index` `is_output_list=True` (sonraithe ag an t-síneadh `𝌠`) agus déanfar iad a phróiseáil go sequential trí na nódanna comhfhreagracha.

### Ionchuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `start` | `FLOAT` | Luach tosaigh chun an raon a giniúint. |
| `stop` | `FLOAT` | Luach deiridh. Má tá `endpoint=include` ansin tá an uimhir seo san liosta. |
| `num` | `INT` | An t-uimhir de níomhais sa liosta (ní cheadaigh é le `step`). |
| `endpoint` | `BOOLEAN` | Decidíonn má ba cheart an luach `stop` a chur san áireamh nó a bhaint as na níomhais. |

### Aschuir

| Ainm | Cineál | Cur Síos |
| --- | --- | --- |
| `int` | `INT 𝌠` | An luach a thiontaithe go int (reaptha síos/floored). |
| `float` | `FLOAT 𝌠` | An luach mar float. |
| `string` | `STRING 𝌠` | An luach mar float a thiontaithe go string. |
| `index` | `INT 𝌠` | Raon de 0..count a chlúdaíonn mar index. |
| `count` | `INT` | Caochladh `num`. |

