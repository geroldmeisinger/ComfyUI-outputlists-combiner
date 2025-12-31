## Carregar Qualquer Arquivo

![Carregar Qualquer Arquivo](LoadAnyFile/LoadAnyFile.png)

(Workflow ComfyUI incluído)

Carrega qualquer arquivo de texto ou binário e fornece o conteúdo do arquivo como string ou string base64. Além disso, tenta carregá-lo como `IMAGE`. E também tenta carregar qualquer metadado.

`filepath` suporta os caminhos de arquivo anotados do ComfyUI `[input]` `[output]` ou `[temp]`.
`filepath` também suporta expansões de padrões glob `subdir/**/*.png`.
Internamente usa a função [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) do Python.

`metadata` chama `exiftool`, se estiver instalado e disponível no `PATH`, caso contrário usa `PIL.Image.info` como fallback.

Por razões de segurança, apenas os seguintes diretórios são suportados: `[input] [output] [temp]`.
Por razões de desempenho, o número de arquivos é limitado a: 1024.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `filepath` | `STRING` | Diretório base padrão é o diretório do usuário `[input]`. Suporta expansão de padrões glob `subdir/**/*.png`. Use o sufixo ` [input]` ` [output]` ou ` [temp]` (observe o espaço inicial!) para especificar um diretório de usuário ComfyUI diferente. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `content` | `STRING 𝌠` | Conteúdo do arquivo para arquivos de texto, base64 para arquivos binários. |
| `image` | `IMAGE 𝌠` | Tensor de lote de imagem. |
| `mask` | `MASK 𝌠` | Tensor de lote de máscara. |
| `metadata` | `STRING 𝌠` | Dados Exif da ExifTool. Requer que o comando `exiftool` esteja disponível no `PATH`. |

