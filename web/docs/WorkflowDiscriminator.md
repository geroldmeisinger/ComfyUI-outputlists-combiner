## Workflow Discriminator

![Workflow Discriminator](/media/WorkflowDiscriminator.png)

(ComfyUI workflow included)

Compare workflows and discriminate differences as JSON paths.
Note that ComfyUI's `IMAGE` doesn't contain the workflow metadata and you need to load the images with specialized image+metadata loaders and connect the metadata to this node.
Custom nodes with metadata loaders include:
* `Load Any File.exif` -> `JSON OutputList(jsonpath=$.["PNG:Prompt"]).value`
* [Crystool](https://github.com/crystian/ComfyUI-Crystools) `🪛 Load image with metadata.Metadata RAW` -> `🪛 Metadata extractor.prompt`
* [Simple_Readable_Metadata](https://github.com/ShammiG/ComfyUI-Simple_Readable_Metadata-SG) `Simple Readable Metadata-SG.metadata_raw`

### Inputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `objs_0`	| `*`	| (optional) A single object (or a list of objects), usually of a workflow. `objs_0` and `more_objs` will be concateneted together and exist for convinience, if you only want to compare two objects.	|
| `more_objs`	| `*`	| (optional) Another object (or a list of objects), usually of a workflow. `objs_0` and `more_objs` will be concateneted together and exist for convinience, if you only want to compare two objects.	|
| `ignore_jsonpaths`	| `*`	| (optional) A list of JSONPaths to ignore in case you want to chain multiple discriminators together.	|

### Outputs

| Name	| Type	| Description	|
| ---	| ---	| ---	|
| `list_a`	| `* 𝌠`	| 	|
| `list_b`	| `* 𝌠`	| 	|
| `list_c`	| `* 𝌠`	| 	|
| `list_d`	| `* 𝌠`	| 	|
| `jsonpaths`	| `STRING 𝌠`	| 	|
