<!-- This file was auto-translated with a local LLM and last updated on 2025-12-27. -->
## OutputLists samsetningar

![OutputLists samsetningar](CombineOutputLists/CombineOutputLists.png)

(ComfyUI virkni innifalið)

Nýtr upp til 4 OutputLists og býr til allar samsetningar þeirra.

Dæmi: `[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`

`unzip_a` .. `unzip_d` notar `is_output_list=True` (táknað með merkinu `𝌠`) og verður að röðuð áfram af samsvarandi hnútum.

Allar listar eru valfrjáls og tómir listar verða hafnir.

Tæknilega reiknar það *samskiptið í Cartesius* og gefur út hverja samsetningu uppdeilt í elementin („unzip“), en tómir listar verða skiptir út fyrir einingar af `None` og munu gefa út `None` á samsvarandi úttaki.

Dæmi: `[1, 2] x [] x ["A", "B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]`

### Inntak

| Heiti | Gerð | Lýsing |
| --- | --- | --- |
| `list_a` | `*` | (valfrjáls) |
| `list_b` | `*` | (valfrjáls) |
| `list_c` | `*` | (valfrjáls) |
| `list_d` | `*` | (valfrjáls) |

### Úttak

| Heiti | Gerð | Lýsing |
| --- | --- | --- |
| `unzip_a` | `* 𝌠` | Gildi samsetninga sem samsvara `list_a`. |
| `unzip_b` | `* 𝌠` | Gildi samsetninga sem samsvara `list_b`. |
| `unzip_c` | `* 𝌠` | Gildi samsetninga sem samsvara `list_c`. |
| `unzip_d` | `* 𝌠` | Gildi samsetninga sem samsvara `list_d`. |
| `index` | `INT 𝌠` | Rúm 0..tala sem getur verið notað sem index. |
| `count` | `INT` | Heildartala samsetninga. |

