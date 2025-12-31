## KSampler Salvare Immediată

![KSampler Salvare Immediată](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Workflow ComfyUI inclus)

Extensia nodului implicit `CheckpointLoader`, `KSampler`, `VAE Decode` și `Save Image` pentru a procesa ca unul singur.
Aceasta este utilă dacă dorești să salvezi imaginile intermediare pentru grile imediat.

*"Un KSampler personalizat doar pentru a salva o imagine? Acum mă fiu transformat în ceea ce am căutat să-l distrug!"*

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Numele punctului de control (modelului) de încărcat. |
| `positive` | `STRING` | Condiționarea care descrie atributele pe care vrei să le incluzi în imagine. |
| `negative` | `STRING` | Condiționarea care descrie atributele pe care vrei să le excludi din imagine. |
| `latent_image` | `LATENT` | Imaginea latentă de dezbrătat. |
| `seed` | `INT` | Seed-ul aleatoriu folosit pentru crearea zgomotului. |
| `steps` | `INT` | Numărul de pași folosiți în procesul de dezbrătare. |
| `cfg` | `FLOAT` | Scala de Ghidare Fără Clasificator echilibrează creativitatea și respectarea promptului. Valori mai mari rezultă în imagini care se potrivesc mai stricte promptului, însă valori prea mari vor afecta negativ calitatea. |
| `sampler_name` | `COMBO` | Algoritmul folosit la eșantionare, acesta poate afecta calitatea, viteza și stilul rezultatului generat. |
| `scheduler` | `COMBO` | Planificatorul controlează cum este îndepărtat treptat zgomotul pentru a forma imaginea. |
| `denoise` | `FLOAT` | Cantitatea de dezbrătare aplicată, valori mai mici vor păstra structura imaginii inițiale permițând eșantionarea imagine de imagine. |
| `filename_prefix` | `STRING` | Prefixul fișierului de salvat. Acesta poate include informații de formatare precum %date:yyyy-MM-dd% sau %Empty Latent Image.width% pentru a include valori din noduri. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `image` | `IMAGE` | Imaginea decodată. |

