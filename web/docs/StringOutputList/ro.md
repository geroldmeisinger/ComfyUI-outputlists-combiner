## Listă de Ieșire Șir

![Listă de Ieșire Șir](StringOutputList/StringOutputList.png)

(Flux de lucru ComfyUI inclus)

Creează o Listă de Ieșire prin împărțirea șirului de caractere din câmpul text cu un separator.
`value` și `index` folosesc `is_output_list=True` (indicat de simbolul `𝌠`) și vor fi procesate secvențial de nodurile corespunzătoare.

### Intrări

| Nume | Tip | Descriere |
| --- | --- | --- |
| `separator` | `STRING` | Șirul de caractere folosit pentru a împărți valorile din câmpul text. |
| `values` | `STRING` | Textul pe care doriți să-l împărțiți într-o listă. Rețineți că șirul este îndepărtat de caracterele de linie nouă de la final înainte de împărțire, iar fiecare element este din nou îndepărtat de spații albe. |

### Ieșiri

| Nume | Tip | Descriere |
| --- | --- | --- |
| `value` | `* 𝌠` | Valorile din listă. |
| `index` | `INT 𝌠` | Interval de 0..count. Poți folosi acesta ca index. |
| `count` | `INT` | Numărul de elemente din listă. |
| `inspect_combo` | `COMBO` | O ieșire fictivă pe care o poți folosi pentru a o conecta la un `COMBO` și pentru a o preumple cu valorile acestuia. Conectarea va fi apoi automat redeschisă către ieșirea `value`. |

