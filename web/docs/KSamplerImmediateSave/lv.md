## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow iekļauts)

Mezgla paplašinājums noklusējuma `CheckpointLoader`, `KSampler`, `VAE Decode` un `Save Image`, lai apstrādātu kā vienu.
Šis ir noderīgs, ja vēlaties saglabāt starpniecības attēlus režģos nekavējoties.

*"Pielāgots KSampler, lai saglabātu attēlu? Tagad es esmu kļuvis par tieši to, ko mēs vēlējāmies iznīcināt!"*

### Ievades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ielādējamā pārbaudes punkta (modela) nosaukums. |
| `positive` | `STRING` | Nosacījums, kas apraksta atribūtus, kurus vēlaties iekļaut attēlā. |
| `negative` | `STRING` | Nosacījums, kas apraksta atribūtus, kurus vēlaties izslēgt no attēla. |
| `latent_image` | `LATENT` | Latents attēls, ko atšķīstīt. |
| `seed` | `INT` | Nejaušais sējums, kas tiek izmantots troksņu radīšanai. |
| `steps` | `INT` | Atšķīstīšanas procesā izmantoto solu skaits. |
| `cfg` | `FLOAT` | Klasifikatora brīvais vadības mērogs līdzsvaro radošumu un uzdevuma atbilstību. Lielākas vērtības rezultātā attēli ir tuvāki uzdevumam, tomēr pārāk lielas vērtības negatīvi ietekmē kvalitāti. |
| `sampler_name` | `COMBO` | Algoritms, kas tiek izmantots paraugēšanās laikā, tas var ietekmēt ģenerētā izvades kvalitāti, ātrumu un stilu. |
| `scheduler` | `COMBO` | Plānotājs kontrolē, kā troksnis pa solim tiek noņemts, lai veidotos attēls. |
| `denoise` | `FLOAT` | Lietotās atšķīstīšanas daudzums, mazākas vērtības saglabā sākotnējā attēla struktūru, ļaujot attēlam attēlam paraugēšanās. |
| `filename_prefix` | `STRING` | Saglabājamā faila prefikss. Tas var ietvert formatēšanas informāciju, piemēram, %date:yyyy-MM-dd% vai %Empty Latent Image.width%, lai iekļautu vērtības no mezgliem. |

### Izvades

| Nosaukums | Tips | Apraksts |
| --- | --- | --- |
| `image` | `IMAGE` | Atšifrēts attēls. |

