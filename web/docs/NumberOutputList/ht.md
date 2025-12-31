## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow ap gen yon pwogrè)

Kreye yon OutputList avèk yon entèval valè nimerik.
Ap itilize [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) anndan, paske li travay pi fiable ak valè flotan.
Si ou vle defini lis nimewo avèk etap aléatò yo eseye JSON OutputList la ak defini yon tablo, p. `[1, 42, 123]`.
`int`, `float`, `chenn` ak `index` itilize `is_output_list=True` (indike pa simbòl `𝌠`) ak ap pwosese sèkilyèman pa nòd ki koresponn yo.

### Antre yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `start` | `FLOTAN` | Valè kòmanse pou jenere entèval la. |
| `stop` | `FLOTAN` | Valè fin. Si `endpoint=include` ap pèmèt valè sa a nan lis la. |
| `num` | `ENTYE` | Kantite objè nan lis la (pa mèlpe l avèk yon `step`). |
| `endpoint` | `BOLEAN` | Dètèmine si valè `stop` ap pèmèt oswa ekskliziv nan objè yo. |

### Sòti yo

| Non | Tip | Deskrisyon |
| --- | --- | --- |
| `int` | `ENTYE 𝌠` | Valè ki konvèti nan int (arondi anba/ak fèn). |
| `float` | `FLOTAN 𝌠` | Valè kòm yon flotan. |
| `string` | `CHENN 𝌠` | Valè kòm yon flotan ki konvèti nan chenn. |
| `index` | `ENTYE 𝌠` | Entèval 0..count ki pèmèt itilizasyon kòm yon endèks. |
| `count` | `ENTYE` | Mèm jan `num`. |

