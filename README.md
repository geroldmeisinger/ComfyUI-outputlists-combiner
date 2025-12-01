# ComfyUI-outputlists-combiner

Did you know that ComfyUI supports so called output lists which tell nodes downstream to execute multiple times within the same run? Notice how this output list emits four strings and causes the KSampler to run four times:

https://github.com/user-attachments/assets/303115d3-7c28-42e8-bb52-d02e7cc1022b

*Wait, what?*

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature seems very underutilized but it allows values to be processed sequentially without weird workarounds (like for-loops, increment counters or external python scripts) which makes them perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally makes XYZ-gridplots easy to use again.

**Features**

![Full Example](/media/FullExample.png)

* **OutputList Combinations:** create all possible combinations of multiple lists, e.g. prompt combinations, image size variants
* **Formatted String:** insert variable placeholders to create custom prompts, e.g. `a {animal} with a {colored} hat`, filename prefixes
* **Inspect Combo:** connect to a COMBO input (like sampler or scheduler) and retrieve all values as a string list, e.g. sampler+scheduler testing, copy+paste model names

## Installation

- [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) search for `ComfyUI-outputlists-combiner`
- `Comfy CLI`: `comfy node install ComfyUI-outputlists-combiner`
- manual: `git clone https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner` into `ComfyUI/custom_nodes`

## Custom nodes

### String OutputList

![Basic String OutputList](/media/StringOutputList.png)
(workflow included)

Create a OutputList by separating the string in the textfield.

**inputs**
* `separator`: the string to split the textfield values.
* `delimiter`: only used for `delimited_str` (you probably don't need this).
* `values`: a textfield with the string which will be separated into the OutputList. note that the string is stripped of whitespace before splitting, and each item is again stripped of whitespaces.

**outputs**
* `value`: the values from the list. uses `OUTPUT_IS_LIST=True` internally and will be processed sequentially by corresponding nodes.
* `delimited_str`: the list joined together by the delimiter, which is often useful for other nodes (like grid annotations).
* `count`: the number of items in the list
* `inspect_combo`: a dummy output only used to pre-fill the list with values from a `COMBO` input.

https://github.com/user-attachments/assets/a8aed46e-3d95-4422-a60e-7f62641ef036

### Number OutputList

![Basic Number OutputList](/media/NumberOutputList.png)
(workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses `numpy.linspace` internally because it works more reliably with floating-point values.

**inputs**
* `start`: start value to generate the range from
* `stop`: end value. if `endpoint=True` this number will be included in the list.
* `num`: the number of items in the list (not to be confused with a step).
* `endpoint`: decides if the stop value should be included or excluded in the items.
* `delimiter`: only used for `delimited_str` (you probably don't need this).

**outputs**
All the values from the list use `OUTPUT_IS_LIST=True` and will be processed sequentially by corresponding nodes.
* `int`: the value converted to int (rounded down/floored)
* `float`: the value as a float
* `str`: the value as a string
* `count`: the number of items in the list

### OutputList Combinations

![Two OutputLists combined](/media/OutputListCombinations.png)
(workflow included)

Takes up to 4 OutputLists, computes the Cartesian product and outputs each combination splitted up into their elements (unzip).
Empty lists are replaced with units of None and unused inputs will always emit None on the respective output.

**Examples**
```
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
[1, 2] x [] x ["A", B"] = [(1, None, "A"), (1, None, "B"), (2, None, "A"), (2, None, "B")]
```

**outputs**
* count: the total number of combinations

### Formatted String

![Using OutputList combinations two create a formatted string](/media/FormattedString.png)
(workflow included)

Create string with variable placeholders. Uses python's `str.format()` internally, see https://docs.python.org/3/library/string.html#format-string-syntax .

* Use `{a:.2f}` to round off a float to 2 decimals.
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`

**outputs**
* `string`: the formatted string with all placeholders replaced with their respective values.

### Convert any number to Int Float String

![Convert any number to Int Float String](/media/ConvertNumberToIntFloatStr.png)
(workflow included)

Convert anything number-like to int float string. Uses `nums-from-string.get_nums()` internally which is very permissive in the numbers it accepts. Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.

outputs:
* **int:** all the numbers found in the string with the decimals truncated (floored)
* **float:** all the numbers found in the string as floats
* **string:** all the numbers found in the string as floats converted to string

## Examples

### Simple Example

![Simple example](/workflows/Example_00_Simple_OutputList.png)
(workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

### Combine prompts

![Combine prompts example](/workflows/Example_01_Combine_Prompts.png)
(workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue] = 3 x 3 = 9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

### Combine samplers and schedulers

![Combine samplers and schedulers example](/workflows/Example_02_Combine_Samplers_Schedulers.png)
(workflow included)

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, heunpp2, uni_pc_bh2] x [simple, karras, beta] = 3 x 3 = 9`)

### Combine numbers

![Combine numbers example](/workflows/Example_03_Combine_Numbers.png)
(workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

### Combine row/column for filename

![Combine numbers example](/workflows/Example_01b_Combine_RowCol_Filename.png)
(workflow included)

Makes use of two `Number OutputList` combined the same way as the prommpts, and a `Convert any number to Int Float String` connect with the respective list count to synchronize the list size, which gives as the rows and columns. `Formatted String` produces the filename prefix `row_{a:02d}_col_{b:02d}`.

### Integrate [LEv145/images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)

![ImageGrids example](/workflows/Example_04_ImageGrids.png)
(workflow included)

Makes use of `delimited_str` to correctly fit the annotation labels for the grid.

Note that with OutputLists the images from the KSampler are individual items, i.e. `batch_size=1`. But the image-grid node expects batches, that's why we need to rebatch them into `batch_size=9` with the `Rebatch images` core node.

To understand batch_sizes use comfyui_essentials `Debug Tensor Shape` which outputs the tensor shape of the image batch in the console (click the `>_` button in the lower left corner).

Tensor Shape Debug after KSampler output:
```
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
Shapes found: [[1, 512, 512, 3]]
```

Tensor shape required for images-grid:
```
[[9, 512, 512, 3]]
```

## Advanced Examples

### Immediately save intermediate images of image grid

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` node.

![ImageGrids example](/workflows/Example_04b_ImageGridsImmediateSave.png)
(workflow included)

Technically this node is implemented as a [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion) and uses the default `KSampler`, `VAE Decode` and `Save Image`.

- **TODO** I'm not happy that this node exists at all as I wanted to avoid custom KSampler nodes. Unfortunately I haven't found a way to [use subgraphs to force immediate processing](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) yet.

### Rebatching images for subgrids

![Rebatching example](/workflows/Example_05_SubImageGrids.png)
(workflow included)

Makes use of an additional images-grid to convert a image `batch_size=4` into a 2x2 grid and then rebatches them for main-grid.

Tensor Shape Debug after KSampler output:
```
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
Shapes found: [[4, 512, 512, 3]]
```

Tensor Shape Debug after first images-grid:
```
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
Shapes found: [[1, 1024, 1024, 3]]
```

Tensor Shape Debug required for second images-grid:
```
[[9, 1024, 1024, 3]]
```

- **TODO** This is kinda surprising if don't know what's going own. Maybe we should develop a "Rebatch Images: shape=4x9" node.

### Baking Values Into Workflow

You may have noticed when you load the workflow from one of the grid images it contains the workflow for the whole grid, not the individual image, but sometimes you want to know which exact prompt or values resulted in this image. Thus we need store the individual values in the metadata. The following workflow makes use of https://github.com/crystian/ComfyUI-Crystools `Save image with Metadata` and `Load image with Metadata` and https://github.com/ltdrdata/ComfyUI-Impact-Pack `Select Nth Item`.

![Save Index in Metadata](/workflows/Example_06a_IndexInMetadata.png)
(workflow included)

This example uses `Number OutputList` to create a index range corresponding to the prompt list and stores it as a JSON `{ "index": 123 }` in the metadata of the image with `Save image with Metadata`. You can extend it to also include the prompt string, row, column, etc. if you hook them up in the `Formatted String` `{{ "index": {a}, "row": {b}, "column": {c}, "prompt": {d} }}`.

![Load Index from Metadata](/workflows/Example_06b_IndexFromMetadata.png)
(workflow included)

This example reads the index from the metadata with `Load Image with Metadata` and selects the index using `Select Nth Item`.

It's is not perfect because in the end you still have to manually put the image in `Load Image` and hook up the values from `Select Nth Item` to get this one exact image. If you work a lot with image grids you might want to include both of this patterns in one workflow.

- **TODO** This is unsatisfactory and requires a lot of manual work
- **TODO** If someone knows a native way include metadata please let me know (node expansion?, hidden extra pnginfo?)!

### Load all images from grid

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `xy_{c:02d}_{a}_{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of one of these `Load Image by Path` nodes, like https://github.com/WASasquatch/was-node-suite-comfyui , https://github.com/KosinkadinkComfyUI-VideoHelperSuite or https://github.com/1038lab/ComfyUI-RMBG .

![Load Image with Formatted String](/workflows/Example_07_LoadWithFormattedString.png)
(workflow included)

**TODO** Make the combo work with native `Load Image` (but my `string to any` approach always resulted in `NoneType object has no attribute 'endsWith'`)
