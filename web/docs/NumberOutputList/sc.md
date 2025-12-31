## Number OutputList

![Number OutputList](NumberOutputList/NumberOutputList.png)

(ComfyUI workflow included)

Cuntzat un’OutputList cun un’intervalu de balores nùmericos.
Impread internamente [numpy.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), ca funtzionat prus in manera fàtzile cun balores de puntu fritu.
Si boles definire listas de nùmeros cun passos a su tèrmine, controlla su JSON OutputList e definìs un’array, pro esèmpiu `[1, 42, 123]`.
`int`, `float`, `string` e `index` impread (s) `is_output_list=True` (indicadu dae su simbòl `𝌠`) e ant a èssere elaborados in manera secuenziale dae nodos corrisponentes.

### Inputs

| Name | Type | Description |
| --- | --- | --- |
| `start` | `FLOAT` | Balore de incìtziu pro generare s’intervalu. |
| `stop` | `FLOAT` | Balore de fine. Si `endpoint=include` atza custu nùmeru in sa lista. |
| `num` | `INT` | Sa cantidade de elementos in sa lista (non isbillàres cun unu `step`). |
| `endpoint` | `BOOLEAN` | Decide si su balore `stop` ant a èssere inclùidu o esclùidu in s’intervalu. |

### Outputs

| Name | Type | Description |
| --- | --- | --- |
| `int` | `INT 𝌠` | Su balore convertidu a int (arrotonadu a bassu/infiriore). |
| `float` | `FLOAT 𝌠` | Su balore comente a unu float. |
| `string` | `STRING 𝌠` | Su balore comente a unu float convertidu a stringa. |
| `index` | `INT 𝌠` | Intervalu de 0..count chi si podet impreare comente un’ìnditze. |
| `count` | `INT` | Su matessi de `num`. |

