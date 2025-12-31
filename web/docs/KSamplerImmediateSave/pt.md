## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Workflow ComfyUI incluído)

Expansão do nó padrão `CheckpointLoader`, `KSampler`, `VAE Decode` e `Save Image` para processar como um único bloco.
Isso é útil se você quiser salvar as imagens intermediárias para grids imediatamente.

*"Um KSampler personalizado apenas para salvar uma imagem? Agora me tornei aquilo que buscava destruir!"*

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | O nome do checkpoint (modelo) a ser carregado. |
| `positive` | `STRING` | A condição que descreve os atributos que você deseja incluir na imagem. |
| `negative` | `STRING` | A condição que descreve os atributos que você deseja excluir da imagem. |
| `latent_image` | `LATENT` | A imagem latente a ser descarregada. |
| `seed` | `INT` | A semente aleatória usada para criar o ruído. |
| `steps` | `INT` | O número de etapas usadas no processo de descarregamento. |
| `cfg` | `FLOAT` | A escala de Direção Livre de Classificador balanceia criatividade e aderência ao prompt. Valores mais altos resultam em imagens mais próximas ao prompt, porém valores muito altos prejudicarão a qualidade. |
| `sampler_name` | `COMBO` | O algoritmo usado ao amostrar, isso pode afetar a qualidade, velocidade e estilo da saída gerada. |
| `scheduler` | `COMBO` | O agendador controla como o ruído é removido gradualmente para formar a imagem. |
| `denoise` | `FLOAT` | A quantidade de descarregamento aplicada, valores mais baixos manterão a estrutura da imagem inicial, permitindo amostragem de imagem para imagem. |
| `filename_prefix` | `STRING` | O prefixo do arquivo a ser salvo. Pode incluir informações de formatação como %date:yyyy-MM-dd% ou %Empty Latent Image.width% para incluir valores de nós. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `image` | `IMAGE` | A imagem decodificada. |

