## Discriminador de Fluxo de Trabalho

![Discriminador de Fluxo de Trabalho](WorkflowDiscriminator/WorkflowDiscriminator.png)

(Fluxo de trabalho ComfyUI incluído)

Compara fluxos de trabalho e os discrimina para extrair os valores diferentes como Listas de Saída individuais.
Você pode usar este nó para restaurar como cada imagem individual foi criada a partir de uma lista de imagens com o mesmo fluxo de trabalho.
Note que o `IMAGE` do ComfyUI não contém os metadados do fluxo de trabalho e você precisa carregar as imagens com carregadores especializados de imagem+metadados e conectar os metadados a este nó.
Nós personalizados com carregadores de metadados incluem:
* `Load Any File.metadata` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `objs_0` | `*` | (opcional) Um único objeto (ou uma lista de objetos), geralmente de um fluxo de trabalho. `objs_0` e `more_objs` serão concatenados e existem por conveniência, se você quiser comparar apenas dois objetos. |
| `more_objs` | `*` | (opcional) Outro objeto (ou uma lista de objetos), geralmente de um fluxo de trabalho. `objs_0` e `more_objs` serão concatenados e existem por conveniência, se você quiser comparar apenas dois objetos. |
| `ignore_jsonpaths` | `STRING` | (opcional) Uma lista de JSONPaths para ignorar caso você queira encadear múltiplos discriminadores juntos. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `list_a` | `* 𝌠` |  |
| `list_b` | `* 𝌠` |  |
| `list_c` | `* 𝌠` |  |
| `list_d` | `* 𝌠` |  |
| `jsonpaths` | `STRING 𝌠` |  |

