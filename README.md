# ComfyUI-outputlists-combiner

Did you know that ComfyUI supports so called output lists, which tell downstream nodes to execute multiple times and retrieve values sequentially, all within one and the same run?

*Wait, what?*

This feature seems very under-utilized but it allows values to be collected and processed without crazy workaround like for-loops or external API calls from python scripts. This project implements some core custom nodes which makes working with output lists easier, provides prompt-combinations and easier use of XYZ-gridplots.

## Installation

1. Install [ComfyUI](https://docs.comfy.org/get_started).
1. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
1. Look up this extension in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

## Custom nodes

### String OutputList

![Basic String OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/StringOutputList.png)

Create a OutputList by separating the string in the textfield.

**inputs**
* separator: the string to split the textfield values.
* delimiter: only used for delimited_str.
* values: the string which will be separated. note that the string is stripped of whitespace before splitting, and each item is again stripped.

**outputs**
* value: the values from the list. uses OUTPUT_IS_LIST=True and will be processed sequentially by corresponding nodes.
* delimited_str: the list joined together by the delimiter, which is often useful for other nodes (like grid annotations).
* full_list: the whole list without OUTPUT_IS_LIST=False in case some nodes require it.
* count: the number of items in the list
* inspect_combo: a dummy output only used to pre-fill the list with values from a COMBO input and will automatically disconnect again.


### Number OutputList

![Basic Number OutputList](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/NumberOutputList.png)

Create a OutputList by generating a numbers of values in a range.
Uses numpy.linspace internally because it works more reliably with floatingpoint values.

**inputs**
* start: start value to generate the range from
* stop: end value. if endpoint=True this number will be included in the list.
* num: the number of items in the list (not to be confused with a step).
* endpoint: decides if the stop value should be included or excluded in the items.
* delimiter: only used for delimited_str.

**outputs**
All the values from the list use OUTPUT_IS_LIST=True and will be processed sequentially by corresponding nodes.
* int: the value converted to int (rounded down/floored)
* float: the value as a float
* str: the value as a string
* full_list: the whole list without OUTPUT_IS_LIST=False in case some nodes require it.
* count: the number of items in the list

### OutputList Combinations

![Two OutputLists combined](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/OutputListCombinations.png)

Takes up to 4 OutputLists, computes the Cartesian product and outputs each combination splitted up into their elements (unzip).
Empty lists are replaced with units of None and unused inputs will always emit None on the respective output.

**Examples**
`[1, 2, 3] x ["A", "B"] = [(1, "A"), (1, "B"), (2, "A"), (2, "B"), (3, "A"), (3, "B")]`
`[1, 2] x [] x ["A", B"] = [(1, None, "A"), (1, None, "B"), (2, None, "A"), (2, None, "B")]`

**outputs**
* count: the total number of combinations

### Formatted String

![Using OutputList combinations two create a formatted string](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/FormattedString.png)

Uses python's `str.format()` internally, see https://docs.python.org/3/library/string.html#format-string-syntax .
A commonly used format syntax is `{a:.2f}` to round of a float to 2 decimals.

**outputs**
* string: the formatted string with all placeholders replaced with their respective values.

## Examples

### Simple Example

![Simple example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_00_Simple_OutputList.png)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

### Combine prompts

![Combine prompts example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_01_Combine_Prompts.png)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue]` (`3x3=9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

### Combine samplers and schedulers

![Combine samplers and schedulers example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_02_Combine_Samplers_Schedulers.png)

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, heunpp2, uni_pc_bh2] x [simple, karras, beta]` (`3x3=9`)

### Combine numbers

![Combine numbers example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_03_Combine_Numbers.png)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width to produce image variants in portrait, square and landscape.

### Integrating [LEv145/images-grid-comfy-plugin](https://github.com/LEv145/images-grid-comfy-plugin)

![ImageGrids example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_04_ImageGrids.png)

Makes use of `delimited_str` to correctly file the annotation labels for the grid.

Note that with OutputLists the images from the KSampler are individual items, i.e. `batch_size=1`. But the image-grid node expects batches, that's why we need to rebatch them into `batch_size=9` with the `Rebatch images` core node.

To understand batch_sizes use comfyui_essentials `Debug Tensor Shape` which outputs the tensor shape of the image batch in the console (click the `>_` button in the lower left corner).

KSampler output:
![](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/BatchList1.png)

Required for images-grid:
![](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/Batch9.png)

### Rebatching images for subgrids

![Rebatching example](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/workflows/Example_05_Rebatching.png)

Makes use of an additional images-grid to convert a image `batch_size=4` into a 2x2 grid and then rebatches them for main-grid.

KSampler output:
![](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/BatchList4.png)

After first images-grid:
![](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/BatchList1.png)

Required for second images-grid:
![](https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner/blob/main/media/Batch9.png)

## TODO

- StringOutputList
  - from string input
- add rebatcher which supports multiple batch sizes
- add list collector for better integration with other custom nodes
