## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(Workflow ComfyUI incluído)

Cria uma OutputList com uma sequência de valores numéricos.
Utiliza internamente [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), pois funciona de forma mais confiável com valores de ponto flutuante.
Se você quiser definir listas de números com passos arbitrários, confira o JSON OutputList e defina um array, por exemplo `[1, 42, 123]`.
`int`, `float`, `string` e `index` usam `is_output_list=True` (indicado pelo símbolo `𝌠`) e serão processados sequencialmente por nós correspondentes.

### Entradas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `start` | `FLOAT` | Valor inicial para gerar o intervalo. |
| `stop` | `FLOAT` | Valor final. Se `endpoint=include`, então este número será incluído na lista. |
| `num` | `INT` | O número de itens na lista (não confundir com um `step`). |
| `endpoint` | `BOOLEAN` | Decide se o valor `stop` deve ser incluído ou excluído dos itens. |

### Saídas

| Nome | Tipo | Descrição |
| --- | --- | --- |
| `int` | `INT 𝌠` | O valor convertido para int (arredondado para baixo). |
| `float` | `FLOAT 𝌠` | O valor como um float. |
| `string` | `STRING 𝌠` | O valor como um float convertido para string. |
| `index` | `INT 𝌠` | Intervalo de 0..count que pode ser usado como um índice. |
| `count` | `INT` | O mesmo que `num`.

