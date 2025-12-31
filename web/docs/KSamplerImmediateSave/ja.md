## KSampler Immediate Save

![KSampler Immediate Save](KSamplerImmediateSave/KSamplerImmediateSave.png)

(ComfyUI workflowが含まれます)

デフォルトの `CheckpointLoader`、`KSampler`、`VAE Decode`、`Save Image` のノード拡張で、1つとして処理します。
これは、グリッドのための中間画像をすぐに保存したい場合に便利です。

*"画像を保存するだけのカスタムKSampler？今や私が排除しようとしたものとなってしまった！"*

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `cpkt_name` | `COMBO` | ロードするチェックポイント（モデル）の名前。 |
| `positive` | `STRING` | 画像に含みたい属性を記述する条件。 |
| `negative` | `STRING` | 画像から除外したい属性を記述する条件。 |
| `latent_image` | `LATENT` | ノイズを除去する潜在画像。 |
| `seed` | `INT` | ノイズ作成に使用されるランダムシード。 |
| `steps` | `INT` | 除去プロセスで使用されるステップ数。 |
| `cfg` | `FLOAT` | Classifier-Free Guidanceスケールは創造性とプロンプトへの忠実度のバランスをとります。高い値はプロンプトに近い画像を生成しますが、高すぎると品質に悪影響を与えます。 |
| `sampler_name` | `COMBO` | サンプリング時に使用されるアルゴリズムで、生成された出力の品質、速度、スタイルに影響を与えることがあります。 |
| `scheduler` | `COMBO` | スケジューラはノイズが徐々に除去されて画像が形成されるのを制御します。 |
| `denoise` | `FLOAT` | 適用される除去量で、低い値は初期画像の構造を保持し、画像対画像のサンプリングを可能にします。 |
| `filename_prefix` | `STRING` | 保存するファイルのプレフィックス。%date :yyyy-MM-dd% や %Empty Latent Image.width% のようにノードから値を含むフォーマット情報を含めることができます。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `image` | `IMAGE` | デコードされた画像。 |

