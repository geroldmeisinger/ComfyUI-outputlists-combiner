## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inclòs)

Crea una OutputList separant la cadena al camp de text amb un separador.
`value` i `index` utilitzen `is_output_list=True` (indicat pel símbol `𝌠`) i seran processats seqüencialment per nodes corresponents.

### Entrades

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `separator` | `STRING` | La cadena utilitzada per separar els valors del camp de text. |
| `values` | `STRING` | El text que vols separar en una llista. Tingues en compte que la cadena es retalla de salts de línia finals abans de separar, i cada element es retalla de espais en blanc. |

### Sortides

| Nom | Tipus | Descripció |
| --- | --- | --- |
| `value` | `* 𝌠` | Els valors de la llista. |
| `index` | `INT 𝌠` | Rang de 0..count. Pots utilitzar-ho com a índex. |
| `count` | `INT` | El nombre d'elements a la llista. |
| `inspect_combo` | `COMBO` | Una sortida fictícia que pots utilitzar per connectar a un `COMBO` i pre-omplir amb els seus valors. La connexió es tornarà a connectar automàticament a la sortida `value`. |

