## XYZ-Tinklelio grafikas

![XYZ-Tinklelio grafikas](XyzGridPlot/XyzGridPlot.png)

(ComfyUI darbo eiga įtraukta)

Generuoja XYZ-tinklelio grafiką iš vaizdų sąrašo.
Jis paims vaizdų sąrašą (įskaitant paketus) ir pirmiausia juos išskleidžia į ilgą sąrašą (todėl `batch_size=1`).

**Tinklelio forma**
Nustato tinklelio formą pagal:
1. eilučių etikečių skaičių
2. stulpelių etikečių skaičių
3. likusius sub-paveikslėlius.
Galite naudoti `order=inside_out`, kad pakeistumėte vaizdų pasirinkimą (naudinga, jei `batch_size>1` ir norite etiketę pridėti prie paketų).

**Lygiavimas**
* Jei etiketė yra perkelta į kitą eilutę, visa ašis laikoma "kelių eilučių" ir jos lygiuojamos viršuje su išlygintu tarpais.
* Jei visas etiketės yra skaičiai arba visos baigiasi skaičiais (pvz., `strength: 1.`), visa ašis laikoma "skaitmeninė" ir jos lygiuojamos dešinėje.
* Visi kiti tekstai laikomi "vienos eilutės" ir jie lygiuojami centru.
* Vieno eilutės ir skaitmeninės etiketės stulpeliuose lygiuojamos apačioje, o eilutės lygiuojamos vertikaliai centre.

**Šrifto dydis**
* Stulpelio etiketės srities aukštis nustatomas pagal `font_size` arba `pusė didžiausio sub-paveikslėlių pakavimo aukščio bet kuriame eilutėje` (kuri yra didesnė).
* Eilutės etiketės srities plotis nustatomas pagal plotų sub-paveikslėlių pakavimą (minimalus 256px).
* Tekstas sumažinamas, kol jis tilps (iki `font_size_min=6`) ir naudoja tą patį šrifto dydį visai ašiai (eilutės etiketės arba stulpelių etiketės).
Jei šrifto dydis jau yra minimalus, apkirpti bet kokį likusį tekstą.

**Sub-paveikslėlių pakavimas**
Pakelia sub-paveikslėlius (įprastai iš paketų) į daugiausia kvadratinę sritį („sub-paveikslėlių pakavimas“), nebent `output_is_list=True`, kuriuo atveju naudoja tik vieną paveikslėlį kiekvienam langeliui ir sukuria visų paveikslėlių tinklelių sąrašą.
Galite naudoti šį paveikslėlių tinklelių sąrašą, kad prijungtumėte kitą XyzGridPlot mazgą ir sukurtumėte super-tinklelius.
Jei sub-paveikslėliai yra skirtingo dydžio paketų, užpildo trūkstamas langelius tuščiais paveikslėliais.
Paveikslėlių skaičius kiekvienam langeliui (įskaitant paketus) turi būti daugiklis `eilučių * stulpelių`.

### Įvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `vaizdai` | `IMAGE` | Vaizdų sąrašas (įskaitant paketus) |
| `eilučių_etiketės` | `*` | Eilučių etiketės teksto kairėje |
| `stulpelių_etiketės` | `*` | Stulpelių etiketės teksto viršuje |
| `tarpas` | `INT` | Tarpas tarp sub-paveikslėlių pakavimų. Atminkite, kad sub-paveikslėliuose viduje nenaudojamas tarps. Jei norite tarpo tarp sub-paveikslėlių prijunkite kitą XyzGridPlot mazgą. |
| `šrifto_dydis` | `FLOAT` | Tikslus šrifto dydis. Tekstas bus sumažinamas, kol tilps (iki `font_size_min=6`). |
| `eilučių_etiketės_orientacija` | `COMBO` | Eilučių etiketės teksto orientacija. Naudinga, jei norite taupyti vietą. |
| `tvarka` | `BOOLEAN` | Nustato, kokia tvarka turi būti apdorojami vaizdai. Tai aktualu tik tada, kai turite sub-paveikslėlius. Naudinga, jei `batch_size>1` ir norite nubrėžti paketus. |
| `išvestis_yra_sąrašas` | `BOOLEAN` | Tai aktualu tik tada, kai turite sub-paveikslėlius arba norite sukurti super-tinklelius. |

### Išvestys

| Pavadinimas | Tipas | Aprašymas |
| --- | --- | --- |
| `vaizdas` | `IMAGE 𝌠` | XYZ-tinklelio grafiko vaizdas. Jei `output_is_list=True`, sukuria vaizdų sąrašą, kurį galite prijungti prie kito XYZ-GridPlot mazgo, kad sukurtumėte super-tinklelius. |

