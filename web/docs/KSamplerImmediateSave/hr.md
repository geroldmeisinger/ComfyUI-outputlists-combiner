## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflow uključen)

Proširenje čvora zadane `CheckpointLoader`, `KSampler`, `VAE Decode` i `Save Image` za obradu kao jedno.
Ovo je korisno ako želite odmah spremiti slike za mreže.

*"Prilagođeni KSampler samo za spremanje slike? Postao sam stvarno ono što sam htio uništiti!"*

### Ulazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Ime checkpointa (modela) za učitavanje. |
| `positive` | `NIZ ZNAKOVA` | Uslovljavanje koje opisuje atribute koje želite uključiti u sliku. |
| `negative` | `NIZ ZNAKOVA` | Uslovljavanje koje opisuje atribute koje želite isključiti iz slike. |
| `latent_image` | `LATENT` | Latentna slika za dešumiranje. |
| `seed` | `CJELI BROJ` | Slučajni seed korišten za stvaranje šuma. |
| `steps` | `CJELI BROJ` | Broj koraka korišten u procesu dešumiranja. |
| `cfg` | `DECIMALNI BROJ` | Classifier-Free Guidance skala ravnoteži kreativnost i pridržavanje prompta. Veće vrijednosti rezultiraju slikama koje se više slažu s promptom, međutim prevelike vrijednosti negativno će utjecati na kvalitetu. |
| `sampler_name` | `COMBO` | Algoritam korišten pri uzimanju uzoraka, ovo može utjecati na kvalitetu, brzinu i stil generiranog izlaza. |
| `scheduler` | `COMBO` | Scheduler kontroliše kako se šum postepeno uklanja za formiranje slike. |
| `denoise` | `DECIMALNI BROJ` | Količina dešumiranja primijenjena, niže vrijednosti će očuvati strukturu početne slike, omogućavajući sliku u sliku uzimanje uzoraka. |
| `filename_prefix` | `NIZ ZNAKOVA` | Prefiks za datoteku za spremanje. Ovo može uključivati informacije o formatiranju poput %date:yyyy-MM-dd% ili %Empty Latent Image.width% za uključivanje vrijednosti iz čvorova. |

### Izlazi

| Ime | Vrsta | Opis |
| --- | --- | --- |
| `slika` | `IMAGE` | Dekodirana slika. |

