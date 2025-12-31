## JSON OutputList

![JSON OutputList](JSONOutputList/JSONOutputList.png)

(ComfyUI workflow íðgu)

Gerir einn OutputList við at úrdraga listir ella orðabøkur frá JSON hlutum.
Nýtir JSONPath syntax til at úrdraga víldi, sjá [JSONPath á Wikipedia](https://en.wikipedia.org/wiki/JSONPath) .
Alt samsvarendi víldi er fløtt í einn langan lista.
Tú kanst einnig nýta ta node til at gerða hlutir frá literal strengum sum `[1, 2, 3]`.
`key`, `value`, `int` og `float` nýtir `is_output_list=True` (merkt við symbolið `𝌠`) og verða handtert í fylgjandi rætta av samsvarandi nodes.

### Inntak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `jsonpath` | `STRING` | JSONPath, ið nýtist til at úrdraga víldi. |
| `json` | `STRING` | Ein JSON streng, ið er umreind til einn hlut. |
| `obj` | `*` | (valfrítt) hlut av hvøsnum slag, ið yvirskrivur JSON strengin |

### Úttak

| Navn | Slag | Lýsing |
| --- | --- | --- |
| `key` | `STRING 𝌠` | Keyin fyri orðabøkur ella index fyri listir (sum strengur).  Tæknisk er ta globalt index í fløttu lista fyri alt, ið ikki er key. |
| `value` | `STRING 𝌠` | Víldi sum strengur. |
| `int` | `INT 𝌠` | Víldi sum tal (um ta ikki kannte parse talið, setur sjálvum 0). |
| `float` | `FLOAT 𝌠` | Víldi sum fleyt (um ta ikki kannte parse talið, setur sjálvum 0). |
| `count` | `INT` | Samtals tal av itemum í fløttu lista |
| `debug` | `STRING` | Debug úttak av alt samsvarendi hlutum sum formtstraður JSON strengur |

