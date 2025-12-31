## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI radni tok je uključen)

Proširenje čvora zadane `CheckpointLoader`, `KSampler`, `VAE Decode` i `Save Image` za obradu kao jedan cijeli.
Ovo je korisno ako želite odmah sačuvati slike između koraka za mreže.

*"Prilagođeni KSampler samo da sačuva sliku? Sada sam postao ono što sam htio uništiti!"*

### Ulazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Naziv checkpointa (modela) za učitavanje. |
| `positive` | `NIZ ZNAKOVA` | Uslov koji opisuje atribute koje želite uključiti u sliku. |
| `negative` | `NIZ ZNAKOVA` | Uslov koji opisuje atribute koje želite isključiti iz slike. |
| `latent_image` | `LATENT` | Latent slika za dešumiranje. |
| `seed` | `CJELI BROJ` | Slučajni seed korišten za stvaranje šuma. |
| `steps` | `CJELI BROJ` | Broj koraka korišten u procesu dešumiranja. |
| `cfg` | `DECIMALNI BROJ` | Classifier-Free Guidance skala koja ravnoteži kreativnost i pridržavanje prompta. Veće vrijednosti rezultiraju slikama koje se više slažu s promptom, međutim prevelike vrijednosti negativno će utjecati na kvalitetu. |
| `sampler_name` | `COMBO` | Algoritam korišten prilikom uzimanja uzorka, ovo može utjecati na kvalitetu, brzinu i stil generisanog izlaza. |
| `scheduler` | `COMBO` | Scheduler kontrolira kako se šum postepeno uklanja kako bi se formirala slika. |
| `denoise` | `DECIMALNI BROJ` | Količina dešumiranja primijenjena, manje vrijednosti će zadržati strukturu početne slike, omogućavajući sliku u sliku uzimanje uzorka. |
| `filename_prefix` | `NIZ ZNAKOVA` | Prefiks za datoteku za čuvanje. Ovo može uključivati informacije o formatiranju poput %date:yyyy-MM-dd% ili %Empty Latent Image.width% kako bi uključilo vrijednosti iz čvorova. |

### Izlazi

| Naziv | Tip | Opis |
| --- | --- | --- |
| `slika` | `IMAGE` | Dekodirana slika. |

