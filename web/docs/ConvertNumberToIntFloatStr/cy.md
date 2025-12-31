## Trosi i Int, Ffloat, Str

![Trosi i Int, Ffloat, Str](ConvertNumberToIntFloatStr/ConvertNumberToIntFloatStr.png)

(Cyflun ComfyUI wedi'i gynnwys)

Trosi unrhyw beth yn rhif i `INT` `FLOAT` `STRING`.
Mae'n defnyddio `nums_from_string.get_nums` o fewnol sydd yn rhagorol iawn yn y rhifau sydd yn eu derbyn. Unrhyw beth o intiaid go iawn, ffloatiaid go iawn, intiaid neu ffloatiaid fel llinynnau, llinynnau sydd â llawer o rifau â gwahanyddion mil. 
Defnyddiwch linyn `123;234;345` i greu'r rhestr o rifau yn gyflym. Peidiwch â defnyddio atalnodau fel gwahanyddion mil gan y byddent yn cael eu dehongli fel gwahanyddion mil.
Mae `int`, `float` a `string` yn defnyddio `is_output_list=True` (a nodir gan y symbol `𝌠`) ac byddent yn cael eu prosesu'n dilynol gan nodau cyfatebol.

### Mewnbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `any` | `*` | Unrhyw beth y gellir ei drosi'n llinyn â rifau sydd yn ei gynnwys |

### Allbwn

| Enw | Math | Disgrifiad |
| --- | --- | --- |
| `int` | `INT 𝌠` | Pob rhif a ganfuwyd yn y llinyn â'r degolion yn cael eu torri. |
| `float` | `FLOAT 𝌠` | Pob rhif a ganfuwyd yn y llinyn fel ffloatiaid. |
| `string` | `STRING 𝌠` | Pob rhif a ganfuwyd yn y llinyn fel ffloatiaid wedi'u trosi i linyn. |
| `count` | `INT` | Nifer y rhifau a ganfuwyd yn y gwerth. |

