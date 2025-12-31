## KSampler Natychmiastowe Zapisywanie

![KSampler Natychmiastowe Zapisywanie](KSamplerImmediateSave/KSamplerImmediateSave.png)

(Dołączony plik ComfyUI workflow)

Rozszerzenie węzła domyślnych `CheckpointLoader`, `KSampler`, `VAE Decode` i `Save Image` do przetwarzania jako jeden.
Jest to przydatne, jeśli chcesz natychmiast zapisać obrazy pośrednie do siatki.

*"Niestandardowy KSampler tylko po to, by zapisać obraz? I teraz zostałem tym, czym chciałem zniszczyć!"*

### Wejścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | Nazwa punktu kontrolnego (modelu) do załadowania. |
| `positive` | `STRING` | Warunkowanie opisujące atrybuty, które chcesz uwzględnić w obrazie. |
| `negative` | `STRING` | Warunkowanie opisujące atrybuty, które chcesz wykluczyć z obrazu. |
| `latent_image` | `LATENT` | Obraz latentny do wygładzenia. |
| `seed` | `INT` | Losowy seed używany do tworzenia szumu. |
| `steps` | `INT` | Liczba kroków używanych w procesie wygładzania. |
| `cfg` | `FLOAT` | Skala Classifier-Free Guidance balansuje kreatywność i przestrzeganie promptu. Wyższe wartości powodują obrazy bardziej pasujące do promptu, jednak zbyt wysokie wartości negatywnie wpłyną na jakość. |
| `sampler_name` | `COMBO` | Algorytm używany podczas próbkowania, może wpływać na jakość, szybkość i styl wygenerowanego wyniku. |
| `scheduler` | `COMBO` | Harmonogram kontroluje sposób stopniowego usuwania szumu w celu utworzenia obrazu. |
| `denoise` | `FLOAT` | Ilość wygładzania stosowanego, niższe wartości zachowają strukturę początkowego obrazu, umożliwiając próbkowanie obrazu do obrazu. |
| `filename_prefix` | `STRING` | Prefiks pliku do zapisania. Może zawierać informacje o formatowaniu, takie jak %date:yyyy-MM-dd% lub %Empty Latent Image.width% aby uwzględnić wartości z węzłów. |

### Wyjścia

| Nazwa | Typ | Opis |
| --- | --- | --- |
| `image` | `IMAGE` | Zdekodowany obraz. |

