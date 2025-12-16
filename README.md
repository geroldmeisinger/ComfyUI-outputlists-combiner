<div align="center">
	<img src="/media/promo.jpg" alt="OutputLists Combiner Promo" width="600" />
</div>

<h2 align="center">Supercharge multiprompt and grid control!</h2>

<h3 align="center">
	<a href="#features" target="_blank">Features</a> ·
	<a href="#installation" target="_blank">Installation</a> ·
	<a href="#changelog" target="_blank">Changelog</a> ·
	<a href="#nodes" target="_blank">Nodes</a> ·
	<a href="#examples" target="_blank">Examples</a>
</h3>

# Features

- **XYZ-GridPlots** perfectly integrated into ComfyUI's paradigm. No weird custom samplers required! No node black magic!
- **Inspect combo** to iterate lists of LoRas, samplers, checkpoints, schedulers etc.
- **List combinations** fully customizable with all native features including LoRa strength, image size-variants, prompt combinations etc.
- **Quick lists** from CSV and Excel Spreadsheets, JSON data, multiline texts and number ranges etc.
- **Formatted strings** for flexible and beautiful filenames, labels, additional metadata etc.

If this custom node helps you in your work..
- ⭐ **Star the repo** to make others discover the project and motivate the developer!
- 💰 **[Donate](https://github.com/sponsors/geroldmeisinger)** for further development and greatly appreciate my efforts!

# Table of Content

- [Features](#features)
- [Table of Content](#table-of-content)
- [Installation](#installation)
- [Changelog](#changelog)
- [Background](#background)
- [Nodes](#nodes)
	- [String OutputList](#string-outputlist)
	- [Number OutputList](#number-outputlist)
	- [JSON OutputList](#json-outputlist)
	- [Spreadsheet OutputList](#spreadsheet-outputlist)
	- [Load any File](#load-any-file)
	- [OutputList Combinations](#outputlist-combinations)
	- [Formatted String](#formatted-string)
	- [Convert any number to Int Float String](#convert-any-number-to-int-float-string)
- [Examples](#examples)
	- [Simple Example](#simple-example)
	- [Combine prompts](#combine-prompts)
	- [Combine samplers and schedulers](#combine-samplers-and-schedulers)
	- [Combine numbers](#combine-numbers)
	- [Combine row/column for filename](#combine-rowcolumn-for-filename)
	- [XYZ-GridPlots](#xyz-gridplots)
	- [XYZ-GridPlots with sub-grids](#xyz-gridplots-with-sub-grids)
- [Advanced Examples](#advanced-examples)
	- [Immediately save intermediate images of image grid](#immediately-save-intermediate-images-of-image-grid)
	- [Baking Values Into Workflow](#baking-values-into-workflow)
	- [Load all images from grid](#load-all-images-from-grid)
	- [Iterate prompts from PromptManager](#iterate-prompts-from-promptmanager)

# Installation

- [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager): search for ```OutputLists Combiner```
- [comfy-cli](https://github.com/Comfy-Org/comfy-cli): ```comfy node install ComfyUI-outputlists_combiner```
- manual:
```
cd custom_nodes
git clone https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner
```

# Changelog

- 0.0.6 SpreadsheetOutputList, XYZGridPlot
- 0.0.4 restructured outputs, JsonOutputList,
- 0.0.3 ConvertAnyToIntFloatString, KSamplerImmediateSave
- 0.0.2 restructured outputs
- 0.0.1 StringOutputList, NumberOutputList, CombineOutputLists, FormattedString

# Background

Did you know that ComfyUI supports so called output lists which tell nodes downstream to execute multiple times within the same run? Notice how this output list emits four strings and causes the KSampler to run four times:

https://github.com/user-attachments/assets/303115d3-7c28-42e8-bb52-d02e7cc1022b

*Wait, what?*

Yeah, I didn't know about it either. Apparently everytime you see the symbol `𝌠` it's an [output list](https://docs.comfy.org/custom-nodes/backend/lists). This feature seems very underutilized but it allows values to be processed sequentially without weird workarounds (like for-loops, increment counters or external python scripts) which makes them perfect for prompt combinations and XYZ-gridplots. I always found grids a hazzle in ComfyUI whereas they were straightforward in Automatic1111. Most custom nodes either require a lot of manual work or you have to use some extra-special nodes (like custom KSamplers). This project tries to make good use of output lists, integrate well with the ComfyUI's paradigm and finally makes XYZ-gridplots easy to use again.

# Nodes

## String OutputList

![Basic String OutputList](/media/StringOutputList.png)

(workflow included)

Create a OutputList by separating the string in the textfield.

**inputs**

* `separator`: the string to split the textfield values
* `values`: the string which will be separated. note that the string is trimmed of whitespace before splitting, and each item is again trimmed

**outputs**

* `value`: the values from the list
* `index`: range of 0..count which can be used as an index
* `count`: the number of items in the list
* `inspect_combo`: a dummy output only used to pre-fill the list with values from a COMBO input and will automatically disconnect again

https://github.com/user-attachments/assets/b2bc09f8-6cb2-47af-bcf5-0fa380c2ef7e

## Number OutputList

![Basic Number OutputList](/media/NumberOutputList.png)

(workflow included)

Create a OutputList by generating a numbers of values in a range.
Uses numpy.linspace internally because it works more reliably with floatingpoint values.

**inputs**

* `start`: start value to generate the range from
* `stop`: end value. if `endpoint=include` this number will be included in the list
* `num`: the number of items in the list (not to be confused with a step)
* `endpoint`: decides if the stop value should be included or excluded in the items

**outputs**

All the values from the list use `OUTPUT_IS_LIST=True` and will be processed sequentially by corresponding nodes.
* `int`: the value converted to int (rounded down/floored)
* `float`: the value as a float
* `str`: the value as a string
* `index`: range of 0..count which can be used as an index
* `count`: same as num

## JSON OutputList

![Basic JSON OutputList](/media/JSONOutputList.png)

(workflow included)

Create a OutputList by extracting arrays or dictionaries from JSON objects.
Uses JSONPath syntax to extract the values, see https://en.wikipedia.org/wiki/JSONPath .
All matched values will be flattend into one list.

You can also use this node as a python `literal_eval` to quickly define simple types or arrays like so `[1, 2, 3]`.

**inputs**

* `jsonpath`: JSONPath used to extract the values
* `json`: a string which will be parsed as JSON
* `obj`: (optional) object of any type which will replace the JSON string

**outputs**

All the values from the list use `OUTPUT_IS_LIST=True` and will be processed sequentially by corresponding nodes.
* `key`: the key for dictionaries or index for arrays (as string). Technically it's a global index of the flattened list for all non-keys
* `value`: the value as a string
* `int`: the value as a int (if not parseable number default to 0)
* `float`: the value as a float (if not parseable number default to 0)
* `count`: total number of items in the flattened list
* `debug`: debug output of all matched objects as a formatted JSON string

## Spreadsheet OutputList

![Basic Spreadsheet OutputList](/media/SpreadsheetOutputList.png)

(workflow included)

Create a OutputLists from a spreadsheet (CSV, TSV, ODS, XLSX and XLS).
Use `Load any File` node to load a file as base64.
Internally uses pandas to parse spreadsheet files.

**inputs**

* `rows_and_cols`: Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based.
* `header_rows`: Ignore the first x rows in the list. Only used if you specify a col in rows_and_cols.
* `header_cols`: Ignore the first x cols in the list. Only used if you specify a row in rows_and_cols.
* `select_nth` Only select the nth entry. Useful in combination with the PrimitiveInt+control_after_generate=increment pattern.
* `string_or_base64`: CSV/TSV string or spreadsheet file in base64 (ODS, XLSX, XLS). Use `Load any File` node to load a file as base64

**outputs**

* `list_a` .. `list_d`: values from the selected spreadsheet column or row
* `count`: number of items in the longest list

## Load any File

![Load any File](/media/LoadAnyFile.png)

(workflow included)

Load any text or binary file and provide the file content as string or base64 string and additionally try to load it as a `IMAGE` and `MASK`.

**inputs**

* `annotated_filepath`: Base directory defaults to input directory. Use suffix `[input]` `[output]` or `[temp]` to specify a different ComfyUI user directory.
* `string`:	file content for text files, base64 for binary files.
* `image`: image batch tensor
* `mask`: mask batch tensor

## OutputList Combinations

![Two OutputLists combined](/media/OutputListCombinations.png)

(workflow included)

Takes up to 4 OutputLists, generates all combinations between them and emits each combination as separate items.
Example:
```
[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]
```

All lists are optional and empty lists will be ignored.

Technically it computes the Cartesian product and outputs each combination splitted up into their elements (unzip), whereas empty lists will be replaced with units of None and they will emit None on the respective output.
Example:
```
[1, 2] x [] x ["A", B"] x [] = [(1, None, "A", None), (1, None, "B", None), (2, None, "A", None), (2, None, "B", None)]
```

**inputs**

* `list_a` .. `list_d`: (optional) ideally connected to a node with `OUTPUT_IS_LIST=True` indicated by the symbol `𝌠`

**outputs**

* `unzip_a` .. `unzip_d`: value of the combinations corresponding to `list_a` .. `list_d`
* `index`: range of 0..count which can be used as an index
* `count`: the total number of combinations

## Formatted String

![Using OutputList combinations two create a formatted string](/media/FormattedString.png)

(workflow included)

Uses python `str.format()` internally, see https://docs.python.org/3/library/string.html#format-string-syntax
* Use `{a:.2f}` to round off a float to 2 decimals
* Use `{a:05d}` to pad up to 5 leading zeros to fit with comfys filename suffix `ComfyUI_00001_.png`
* If you want to write `{ }` within your strings (e.g. for JSONs) you have to double them like so: `{{ }}`

**inputs**

* `a` .. `d`: (optional) value that will be converted to string with the `{a}` .. `{d}` placeholder

**outputs**

* `string`: the formatted string with all placeholders replaced with their respective values

## Convert any number to Int Float String

![Convert any number to Int Float String](/media/ConvertNumberToIntFloatStr.png)

(workflow included)

Convert anything number-like to int float string.
Uses `nums-from-string.get_nums` internally which is very permissive in the numbers it accepts.
Anything from actual ints, actual floats, ints or floats as strings, strings that contains multiple numbers with thousand-separators.

outputs:
* `int`: all the numbers found in the string with the decimals truncated (floored)
* `float`: all the numbers found in the string as floats
* `string`: all the numbers found in the string as floats converted to string
* `count`: amount of numbers found in the string, which in most cases will be 1

# Examples

## Simple Example

![Simple example](/workflows/Example_00_Simple_OutputList.png)
(workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

## Combine prompts

![Combine prompts example](/workflows/Example_01a_Combine_Prompts.png)
(workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue] = 3 x 3 = 9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

## Combine samplers and schedulers

![Combine samplers and schedulers example](/workflows/Example_02_Combine_Samplers_Schedulers.png)

(workflow included)

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, dpmpp_2m, uni_pc_bh2] x [simple, karras, beta] = 3 x 3 = 9`)

## Combine numbers

![Combine numbers example](/workflows/Example_03_Combine_Numbers.png)
(workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

Notice that images within a batch always have to be same width and height, wheras here each image has a different image size. This is only possible because it is a list of images.

## Combine row/column for filename

![Combine numbers example](/workflows/Example_01b_Combine_RowCol_Filename.png)

(workflow included)

Makes use of the `index` combined the same way as the prompts, which gives as the rows and columns. `Formatted String` produces the filename prefix `cell_{c:02d}_row_{a:02d}_col_{b:02d}`.

## XYZ-GridPlots

![XYZ-Gridplots](/workflows/Example_04a_XYZ-GridPlots.png)

Uses `String OutputLists + OutputLists Combinations + Fomratted String` to generate multiple prompts for an image grid. The values of the `String OutputLists` are directly used a labels for the `XYZ-GridPlot` and they also define how the grid should be shaped.

Note that `batch_size=1` and `output_is_list=False`. If you set `batch_size=4` you get a image grid with the batch as sub-grids. If you also set `output_is_list=True` the sub-images will not be arranged together but you will get 4 separate images instead.

## XYZ-GridPlots with sub-grids

I recommend to start ComfyUI with `--cache-ram` for this example if you want to experiment with the settings alot!

![XYZ-Gridplots with sub-grids](/workflows/Example_04b_XYZ-GridPlots-Subgrids.png)

Uses two `XYZ-GridPlot` in sequence to put one image grid inside the other. For more complex image grids the question always is: How should the axis be ordered and in which way the images be shuffled, e.g. do we want to show `cat|dog|rat` x `red|blue|green` and then the batch next to each other in a subgrid (`RxCxB`), or four separate images each with a grid of `cat|dog|rat` x `red|blue|green` (`BxCxR`). To achieve this you can play around with the options `order=outside-in|inside-out` and `output_is_list=False|True`, but make sure the `row_labels` and `col_labels` match what you want to achieve, as this info is also used how the grid is shaped.

# Advanced Examples

## Immediately save intermediate images of image grid

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.

Custom nodes:
* [images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) (optional)

![ImageGrids example](/workflows/Example_04b_ImageGridsImmediateSave.png)

(workflow included)

Technically this node is implemented as a [node expansion](https://docs.comfy.org/custom-nodes/backend/expansion) and uses the default `KSampler`, `VAE Decode` and `Save Image`.

- **TODO** Update workflow with new `XYZ-GridPlot` node
- **TODO** I'm not happy that this node exists at all as I wanted to avoid custom KSampler nodes. Unfortunately I haven't found a way to [use subgraphs to force immediate processing](https://github.com/Comfy-Org/docs/discussions/532#discussioncomment-15115385) yet.

## Baking Values Into Workflow

Custom nodes:
* [Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
* [Crystools](https://github.com/crystian/ComfyUI-Crystools)

You may have noticed when you load the workflow from one of the grid images it contains the workflow for the whole grid, not the individual image, but sometimes you want to know which exact prompt or values resulted in this image. Thus we need store the individual values in the metadata. The following workflow makes use of Crystools' `Save image with Metadata` and `Load image with Metadata` and Impact-Pack's `Select Nth Item`.

![Save Index in Metadata](/workflows/Example_06a_IndexInMetadata.png)

(workflow included)

Uses the `index` of the combined list to store it as a JSON. It also uses the `index` of the individual lists combined the same way as the prompts, which gives as the rows and columns, for additional information, including the prompt: `{{ "prompt": "{a}", "index": {b}, "row": {c}, "col": {d} }}`

![Load Index from Metadata](/workflows/Example_06b_IndexFromMetadata.png)

(workflow included)

This example reads the index from the metadata with `Load Image with Metadata` and selects the index using `Select Nth Item`.

It's is not perfect because in the end you still have to manually put the image in `Load Image` and hook up the values from `Select Nth Item` to get this one exact image. If you work a lot with image grids you might want to include both of this patterns in one workflow.

- **TODO** This is unsatisfactory and requires a lot of manual work
- **TODO** If someone knows a native way include metadata please let me know (node expansion?, hidden extra pnginfo?, dynprompt?)!

## Load all images from grid

Custom nodes, one of the following:
* [was-ns](https://github.com/ltdrdata/was-node-suite-comfyui)/[was-node-suite-comfyui (old)](https://github.com/WASasquatch/was-node-suite-comfyui)
* [VideoHelperSuite](https://github.com/KosinkadinkComfyUI-VideoHelperSuite)
* [ComfyUI-RMBG](https://github.com/1038lab/ComfyUI-RMBG)

Let's say you generated a lot of images for your grid and (hopefully) stored them with some clever naming scheme, e.g. `cell_{c:02d}-{a}-{b}` like in the previous example. Now you need to load them from the output folder, without accidentally loading any other images. This uses the same prompt combination as before but uses the string to load the image filename. The following workflow makes use of one of these `Load Image by Path` nodes,

![Load Image with Formatted String](/workflows/Example_07_LoadWithFormattedString.png)

(workflow included)

**TODO** Make the combo work with native `Load Image` (but my `string to any` approach always resulted in `NoneType object has no attribute 'endsWith'`). I filled a bugreport https://github.com/comfyanonymous/ComfyUI/issues/11017

## Iterate prompts from PromptManager

Custom nodes:
* [PromptManager](https://github.com/ComfyAssets/ComfyUI_PromptManager)
* [ComfyUI-HTTP](https://github.com/wawahuy/ComfyUI-HTTP)

PromptManager keeps track of all the prompt you generated in a database which you can annotate with tags and categories. The following workflow allows you to search by text, tags and categories to get selection of the prompts and iterate them.

![Load prompts with GET HTTP and extract JSON with JSON OutputList](/workflows/Example_08_PromptManager.png)

(workflow included)

Makes use of ComfyUI-HTTP's `HTTP GET Request` to call PromptManager's search API route and `JSON OutputList` to extract the `text` field using a JSONPath. The prompts are emitted as an OutputList and will be processed sequentially.
