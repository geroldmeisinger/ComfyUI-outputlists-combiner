## Load Any File

![Load Any File](/media/LoadAnyFile.png)

(ComfyUI workflow included)

Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE`.

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `annotated_filepath`	| `STRING`	| Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `string`	| `STRING`	| File content for text files, base64 for binary files.	|
| `image`	| `IMAGE`	| Image batch tensor.	|
| `mask`	| `MASK`	| Mask batch tensor.	|
| `metadata`	| `STRING`	| Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`.	|
