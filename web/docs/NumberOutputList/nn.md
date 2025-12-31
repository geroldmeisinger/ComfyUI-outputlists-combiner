## Tall utdata liste

![Tall utdata liste](NumberOutputList/NumberOutputList.png)

(ComfyUI arbeidsflyt inkludert)

Lagar ein utdata liste med eit område med numeriske verdiar.
Brukar [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internt, fordi det fungerer påliteliger med flytende punktverdiar.
Viss du vil definere talistor med vilkårlege steg, sjekk JSON utdata liste og definér ein matrise, til dømes `[1, 42, 123]`.
`int`, `float`, `string` og `index` bruker `is_output_list=True` (indikert med symbolet `𝌠`) og vil bli handsama sekvensielt av tilhøyrande noder.

### Inndata

| Namn | Type | Skildring |
| --- | --- | --- |
| `start` | `FLOAT` | Startverdi for å generere området frå. |
| `stop` | `FLOAT` | Sluttverdi. Viss `endpoint=include` så er denne verdien inkludert i lista. |
| `num` | `INT` | Talet på element i lista (ikkje forveksl med `step`). |
| `endpoint` | `BOOLEAN` | Avgjer om `stop`-verdien skal inkluderes eller ekskluderes i elementa. |

### Utdata

| Namn | Type | Skildring |
| --- | --- | --- |
| `int` | `INT 𝌠` | Verdien konvertert til int (rundet ned/floora). |
| `float` | `FLOAT 𝌠` | Verdien som ein float. |
| `string` | `STRING 𝌠` | Verdien som ein float konvertert til streng. |
| `index` | `INT 𝌠` | Område frå 0..count som kan brukast som ein index. |
| `count` | `INT` | Same som `num`. |

