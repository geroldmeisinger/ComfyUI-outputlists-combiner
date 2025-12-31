## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI vinnusvæði included)

Býr til OutputList með sviði af tölulegum gildum.
Notar [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) innri, vegna þess að það virkar treystilegra með fleytitalnum.
Ef þú vilt skilgreina tölulista með hérvalda skrefum í staðinn skoðaðu JSON OutputList og skilgreindu fylki, t.d. `[1, 42, 123]`.
`int`, `float`, `string` og `index` notar `is_output_list=True` (sýnt með tákninu `𝌠`) og verður þá meðhöndlað síðan af samsvarandi node.

### Inntök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `start` | `FLOAT` | Byrjunargildi til að búa til sviðið frá. |
| `stop` | `FLOAT` | Endargildi. Ef `endpoint=include` þá er þetta tala innifalin í listanum. |
| `num` | `INT` | Fjöldi atriða í listanum (ekki taka það saman við `step`). |
| `endpoint` | `BOOLEAN` | Ákveður hvort `stop` gildið ætti að vera innifalið eða útilokað í atriðunum. |

### Úttök

| Nafn | Gerð | Lýsing |
| --- | --- | --- |
| `int` | `INT 𝌠` | Gildið breytt í int (rúnduð niður/floored). |
| `float` | `FLOAT 𝌠` | Gildið sem fleytitala. |
| `string` | `STRING 𝌠` | Gildið sem fleytitala breytt í streng. |
| `index` | `INT 𝌠` | Svið 0..count sem hægt er að nota sem index. |
| `count` | `INT` | Sama og `num`. |

