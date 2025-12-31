## Tall OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow inkludert)

Oppretter en OutputList med et område av numeriske verdier.
Bruker [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) internt, fordi det fungerer mer pålitelig med flytende komma-verdier.
Hvis du ønsker å definere talllister med vilkårlige trinn, sjekk ut JSON OutputList og definer en matrise, f.eks. `[1, 42, 123]`.
`int`, `float`, `string` og `index` bruker `is_output_list=True` (indikert av symbolet `𝌠`) og vil bli behandlet sekvensielt av tilsvarende noder.

### Innputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `start` | `FLOAT` | Startverdi for å generere området fra. |
| `stop` | `FLOAT` | Sluttverdi. Hvis `endpoint=include` så er denne verdien inkludert i listen. |
| `num` | `INT` | Antall elementer i listen (ikke forveksle med et `step`). |
| `endpoint` | `BOOLEAN` | Avgjør om `stop`-verdien skal inkluderes eller ekskluderes i elementene. |

### Utputter

| Navn | Type | Beskrivelse |
| --- | --- | --- |
| `int` | `INT 𝌠` | Verdien konvertert til int (rundet ned/floored). |
| `float` | `FLOAT 𝌠` | Verdien som et flyttall. |
| `string` | `STRING 𝌠` | Verdien som et flyttall konvertert til streng. |
| `index` | `INT 𝌠` | Område fra 0..count som kan brukes som en indeks. |
| `count` | `INT` | Samme som `num`. |

