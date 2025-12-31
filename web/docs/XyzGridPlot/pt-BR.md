## XYZ-GridPlot

![XYZ-GridPlot](XyzGridPlot/XyzGridPlot.png)

(Workflow ComfyUI incluído)

Gera um XYZ-Gridplot a partir de uma lista de imagens.
Ele recebe uma lista de imagens (incluindo batches) e as transforma em uma única lista longa primeiro (assim `batch_size=1`).

**Forma da grade**
Determina a forma da grade por:
1. o número de rótulos de linha
2. o número de rótulos de coluna
3. as sub-imagens restantes.
Você pode usar `order=inside_out` para inverter a seleção das imagens (útil se `batch_size>1` e você quiser rotular os batches).

**Alinhamento**
* Se um rótulo se estender para a próxima linha, todo o eixo é considerado "multiline" e alinha-os no topo com espaçamento justificado.
* Se todos os rótulos forem números ou terminarem em números (ex: `strength: 1.`), todo o eixo é considerado "numérico" e alinha-os à direita.
* Todos os outros textos são considerados "singleline" e alinham-se ao centro.
* Alinha rótulos singleline e numéricos para colunas no fundo, e para linhas alinha-os verticalmente no meio.

**Tamanho da fonte**
* A altura da área dos rótulos de coluna é determinada por `font_size` ou pela "metade da maior altura de empacotamento das sub-imagens em qualquer linha" (o que for maior).
* A largura da área dos rótulos de linha é determinada pela largura mais larga do empacotamento das sub-imagens (com um mínimo de 256px).
* O texto é reduzido até caber (até `font_size_min=6`) e usa o mesmo tamanho de fonte para todo o eixo (rótulos de linha ou coluna).
Se o tamanho da fonte já estiver no mínimo, corta qualquer texto restante.

**Empacotamento de sub-imagens**
Formata as sub-imagens (geralmente de batches) na área mais quadrada possível (o "empacotamento de sub-imagens"), a menos que `output_is_list=True`, nesse caso usa apenas uma imagem para cada célula e cria uma lista de grades inteiras de imagens.
Você pode usar essa lista de grades de imagens para conectar outro nó XyzGridPlot e criar super-grids.
Se as sub-imagens consistirem em batches de tamanhos diferentes, preenche as células vazias com imagens vazias.
O número de imagens por célula (incluindo imagens em batch) deve ser múltiplo de `rows * columns`.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `images` | `IMAGE` | Uma lista de imagens (incluindo batches) |
| `row_labels` | `*` | Textos dos rótulos de linha no lado esquerdo |
| `col_labels` | `*` | Textos dos rótulos de coluna no topo |
| `gap` | `INT` | Espaçamento entre os empacotamentos das sub-imagens. Note que dentro das próprias sub-imagens não há espaçamento. Se você quiser um espaçamento entre as sub-imagens, conecte outro nó XyzGridPlot. |
| `font_size` | `FLOAT` | Tamanho de fonte desejado. O texto será reduzido até caber (até `font_size_min=6`). |
| `row_label_orientation` | `COMBO` | Orientação do texto dos rótulos de linha. Útil se você quiser economizar espaço. |
| `order` | `BOOLEAN` | Define em qual ordem as imagens devem ser processadas. Isso só é relevante se você tem sub-imagens. Útil se `batch_size>1` e você quiser plotar os batches. |
| `output_is_list` | `BOOLEAN` | Isso só é relevante se você tem sub-imagens ou quer criar super-grids. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `image` | `IMAGE 𝌠` | A imagem XYZ-GridPlot. Se `output_is_list=True`, cria uma lista de imagens que você pode conectar a outro nó XYZ-GridPlot para criar super-grids. |

