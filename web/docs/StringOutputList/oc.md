## String OutputList

![String OutputList](StringOutputList/StringOutputList.png)

(ComfyUI workflow inclòcha)

Crea una lista de sortida en dividissent lo tèxte del camp de tèxte amb un separador.
`value` e `index` utiliza(n) `is_output_list=True` (indicat per lo simbòl `𝌠`) e seràn tractats sequencialament per los nòds corresponents.

### Entradas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `separator` | `STRING` | La cadena de caractèrs utilizada per dividir las valors del camp de tèxte. |
| `values` | `STRING` | Lo tèxte que volètz dividir en una lista. Notatz que la cadena es trima de las linhas novèlas a la fin abans la division, e cada element es tornat trimat de l'espaci. |

### Sortidas

| Nom | Tipe |Descripcion |
| --- | --- | --- |
| `value` | `* 𝌠` | Las valors de la lista. |
| `index` | `INT 𝌠` | Interval de 0..count. Pòdètz l'utilizar coma un indèx. |
| `count` | `INT` | Lo nombre d'elements de la lista. |
| `inspect_combo` | `COMBO` | Una sortida fictiva que podètz utilizar per ligar a un `COMBO` e lo pre-emplir amb sas valors. La connexion serà automaticament re-connectada a la sortida `value`. |

