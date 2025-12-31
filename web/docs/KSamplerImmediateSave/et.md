## KSampler koheselt salvestamine

![KSampler koheselt salvestamine](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI töövoog on kaasatud)

Sõlme laiendus vaikimisi `CheckpointLoader`, `KSampler`, `VAE Decode` ja `Save Image` töödeks, et töödelda üheks tervikuna.
See on kasulik, kui soovid koheselt salvestada vahepildid võrgustike jaoks.

*"Kohandatud KSampler ainult pildi salvestamiseks? Nüüd olen muutunud asjaks, mida otsisin hävitada!"*

### Sisendid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Laetava kontrollpunkti (mudeli) nimi. |
| `positive` | `STRING` | Tingimused, mis kirjeldavad atribuute, mida soovid pildile lisada. |
| `negative` | `STRING` | Tingimused, mis kirjeldavad atribuute, mida soovid pildilt eemaldada. |
| `latent_image` | `LATENT` | Peegeldatav pilt, millelt eemaldada müra. |
| `seed` | `INT` | Juhuslik kood, mida kasutatakse müra loomiseks. |
| `steps` | `INT` | Müra eemaldamise protsessis kasutatavate sammude arv. |
| `cfg` | `FLOAT` | Classifier-Free Guidance skaala tasakaalustab loovust ja juhendust käsikirjaga. Suuremad väärtused viivad piltidele, mis paremini sobivad käsikirjaga, kuid liiga suured väärtused mõjutavad negatiivselt kvaliteeti. |
| `sampler_name` | `COMBO` | Näitamine kasutatav algoritm, mis võib mõjutada genereeritud väljundi kvaliteeti, kiirust ja stiili. |
| `scheduler` | `COMBO` | Planeerija kontrollib, kuidas müra järk-järgult eemaldatakse pildi moodustamiseks. |
| `denoise` | `FLOAT` | Müra eemaldamise kogus, väiksemad väärtused säilitavad algse pildi struktuuri, võimaldades pildilt pildile näytetäisust. |
| `filename_prefix` | `STRING` | Faili salvestamise eesliide. See võib sisaldada vormindamise infot, nagu %date:yyyy-MM-dd% või %Empty Latent Image.width%, et sisestada väärtused sõlmedest. |

### Väljundid

| Nimi | Tüüp | Kirjeldus |
| --- | --- | --- |
| `image` | `IMAGE` | Dekodeeritud pilt. |

