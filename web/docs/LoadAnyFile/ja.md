## Load Any File

![Load Any File](LoadAnyFile/LoadAnyFile.png)

(ComfyUI workflowが含まれます)

任意のテキストまたはバイナリファイルをロードし、ファイル内容を文字列またはbase64文字列として提供します。さらに、それを`IMAGE`としてロードしようとします。また、メタデータもロードしようとします。

`filepath` は ComfyUI の注釈付きファイルパス `[input]` `[output]` または `[temp]` をサポートします。
`filepath` はグロブパターン展開 `subdir/**/*.png` もサポートします。
内部的には Python の [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob) を使用します。

`metadata` は、`exiftool` がインストールされており `PATH` で利用可能な場合に呼び出します。そうでない場合は `PIL.Image.info` をフォールバックとして使用します。

セキュリティ上の理由から以下のディレクトリのみがサポートされています：`[input] [output] [temp]`。
パフォーマンス上の理由からファイル数は次の制限があります：1024。

### 入力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `filepath` | `STRING` | ベースディレクトリのデフォルトは `[input]` ユーザーディレクトリです。グロブパターン展開 `subdir/**/*.png` をサポートします。異なる ComfyUI ユーザーディレクトリを指定するには、接尾辞 ` [input]` ` [output]` または ` [temp]` を使用してください（先頭のスペースに注意！）。 |

### 出力

| 名前 | タイプ | 説明 |
| --- | --- | --- |
| `content` | `STRING 𝌠` | テキストファイルのファイル内容、バイナリファイルのbase64。 |
| `image` | `IMAGE 𝌠` | 画像バッチテンソル。 |
| `mask` | `MASK 𝌠` | マスクバッチテンソル。 |
| `metadata` | `STRING 𝌠` | ExifTool からのExifデータ。`exiftool` コマンドが `PATH` で利用可能である必要があります。 |

