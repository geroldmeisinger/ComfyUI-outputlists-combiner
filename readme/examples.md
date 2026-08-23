# Examples

## Simple OutputList

![Simple OutputList example](/workflows/Example_00_Simple_OutputList.png)

(ComfyUI workflow included)

Just uses a `String OutputList` to separate a string and produce 4 images in one run.

## Combine prompts

![Combine prompts example](/workflows/Example_01_Combine_Prompts.png)

(ComfyUI workflow included)

Combines two `String OutputList` with a `OutputList Combinations` and merges them into the prompt with `Formatted String`. It iterates over all combinations of `[cat, dog, rat] x [red, green, blue] = 3 x 3 = 9`)

To debug strings it's recommended to use comfyui-custom-scripts `Show Text` as it outputs a new line for each emitted item.

## Combine numbers

![Combine numbers example](/workflows/Example_02_Combine_Numbers.png)

(ComfyUI workflow included)

Makes use of `Number OutputList` to generate the number ranges `[256, 512, 768] x [768, 512, 256]` and connects them to the image width and height to produce image variants in portrait, square and landscape.

Notice that images within a batch always have to be same width and height, wheras here each image has a different image size. This is only possible because it is a list of images.

## Combine samplers and schedulers

![Combine samplers and schedulers example](/workflows/Example_03_Combine_Samplers_Schedulers.png)

(ComfyUI workflow included)

https://github.com/user-attachments/assets/d8da27b9-99d2-4ac5-a6ed-d368d2ae1a38

Makes use of `inspect_combo` to populate the `String OutputList` (unneeded entries were deleted) and connects to the COMBO inputs `samplers` and `schedulers`. It iterates over all combinations of `[euler, dpmpp_2m, uni_pc_bh2] x [simple, karras, beta] = 3 x 3 = 9`)

## Combine row/column for filename

![Combine row/column for filename example](/workflows/Example_04_Combine_RowCol_Filename.png)

(ComfyUI workflow included)

Makes use of the `index` combined the same way as the prompts, which gives as the rows and columns. `Formatted String` produces the filename prefix `img_{c:02d}_row_{ad}_col_{b}`.

## Compare LoRA-model and LoRA-strength

![Combine LoRA-model and LoRA-strength example](/workflows/Example_05_Compare_LoRAModel_LoRAStrength.png)

(ComfyUI workflow included)

https://github.com/user-attachments/assets/64e118c1-15f3-463b-b439-37e1a1f5b62b

Custom LoRAs:
* [MoXinV1.safetensors](https://civitai.com/models/12597)
* [animeoutlineV4_16.safetensors](https://civitai.com/models/16014)
* [blindbox_v1_mix.safetensors](https://civitai.com/models/25995)

Makes use of `inspect_combo` to populate the `String OutputList` with the model names (unneeded entries were deleted), and a corresponding `String OutputList` with the trigger words. Both OutputLists are combined with a `Number OutputList` each to iterate over all combinations of `[modelA, modelB, modelC] x [0.4, 0.7, 1.0] = 3 x 3 = 9` and `[triggerA, triggerB, triggerC] x [0.4, 0.7, 1.0] = 3 x 3 = 9`, so they are in-sync. The `LoRA filename` and `LoRA strength` are connected with the `LoRA Model Loader`, and the `trigger word` is used to construct a prompt in `Formatted String`.

**If you don't need separate trigger words, just delete the second combination altogether, it's much simpler this way!**

It might be a little confusing why we need two combinations here, but it is important that the lists are synchronized. Ideally we would only construct a single combination with pairs of `[(modelA, triggerA), (modelB, triggerB), (modelC, triggerC)] x lora-strengths` but then we would need to deconstruct the `(modelX, triggerX)` pairs later.

## XYZ-GridPlot Simple

![XYZ-GridPlot Simple example](/workflows/Example_06_XYZ-GridPlot.png)

(ComfyUI workflow included)

Uses `String OutputLists + OutputLists Combinations + Formatted String` to generate multiple prompts for an image grid. The values of the `String OutputLists` are directly used as labels for the `XYZ-GridPlot` and they also define how the grid should be shaped.

Note that `batch_size=1` and `output_is_list=False`. If you set `batch_size=4` you get a image grid with the batch as sub-grids. If you also set `output_is_list=True` the sub-images will not be arranged together but you will get 4 separate images instead.

https://github.com/user-attachments/assets/a649b701-58a5-47a8-b697-e2a34a39c999

## Load multiple files with different formats

![Load multiple files example](/workflows/Example_07_LoadMultipleFiles.png)

(ComfyUI workflow included)

Uses `String OutputList` to emit multiple glob patterns that expand, 1. on the directory `tests`, 2. on any sub-directory `**` (in this case: `imgs`), 3. on all files with a certain file ending (`*.png`), 4. starting at ComfyUI's `[output]` directory as the base. This calls `Load Any File` 3 times, each time with a different format, which again emits multiple files each time, resulting in a list of many files.

## Repeat OutputLists

![Repeat OutputLists example](/workflows/Example_08a_RepeatOutputLists.png)

## Cycle OutputLists

![Cycle OuputLists example](/workflows/Example_08b_CycleOutputLists.png)

## The execution stalling problem

One thing you may have noticed when you make a large image grid is that you have to wait for ALL intermediate images to be processed before anything is saved and the grid created. Thus you could loose a lot of processed images when something happens or you cancel the job (though ComfyUI keeps them in cache and should pick up immediately). Another problem that occurs with loader nodes is that the load ALL resources at once before passing on execution which will eventually lead to OOM.

The reason is that ComfyUI process the data list in node-major mode (one node processes all items before proceeding to the next node) instead of list-major mode (one item is processed by a group of nodes before proceeding to the next item). I have filled a [RFC](https://github.com/Comfy-Org/rfcs/discussions/43) specifically for this problem and proposed changes to the execution scheme of ComfyUI. In the meantime there are multiple workarounds:
* Ignore it and just wait it out (I recommend to start ComfyUI with `--cache-ram` though, so you can pick up were you left off anytime)
* Use[Iterate loop nodes]](#iterate loop nodes) with passthrough output nodes (recommended!)
* Use the [PrimitiveInt control\_after\_generate=increment pattern](#the-primitiveint-control_after_generateincrement-pattern) but it requires some manual work.

### Iterate loop nodes

![Iterate loop nodes](/workflows/Example_09_IterateLoopNodes.png)

(ComfyUI workflow included)

Makes use of `Iterate Begin` and `Iterate End` to mark the nodes between the `flow_control` as a "sequential group". This works similar to other loop nodes except that they work with output lists. It's important to use a output node with passthrough to see the intermediate results, otherwise they will only act upon the first item. Newer ComfyUI versions already have them.

(if you want to understand how this works internally see the section [for-loops](#for-loops))

### The PrimitiveInt control_after_generate=increment pattern

You probably noticed the `control_after_generate` widget before in the `KSampler` for `seed` where it's often set to `random`. This feature can also be created manually with the `Primitive Int` node. If you set it to `control_after_generate=increment` you basically get a counter that increases everytime you run a prompt. When you hook it up as a index in a list selector node, it iterates over entries across multiple prompts. In the `Run` toolbox you can set the amount of prompts to the number of items in your list to iterate the whole list. This pattern essentially cancels out the effect of OutputLists and will only ever process one item at a time. That's especially useful if you want to test something out. Remember to reset the counter to 0 afterwards!

![The PrimitiveInt control_after_generate=increment pattern](/media/PrimitiveIntControlAfterGenerateIncrement.png)

And because it is very tedious to add a selector for every single list, the `Spreadsheet OutputList` includes a `select_nth` widget which applies the index to all lists at once, and makes everything simpler for complex workflows that use multiple lists.

![The PrimitiveInt control_after_generate=increment pattern and Spreadsheet OutputList](/media/PrimitiveIntControlAfterGenerateIncrementSpreadsheet.png)

### Node expansion in code

Another solution is node expansion in code but you literally have to rebuild a pattern in code, see [Node expansion in code](https://github.com/geroldmeisinger/rfcs/blob/main/rfcs/0000-execution_mode_in_sequential_processing.md#alternatives).

**Deprecated**: If you want to save the intermediate images after each step you can use the `KSampler immediate Save Image` beta-node. For this node to be visible in the node searchbox you need to activate `Settings -> Comfy -> Show experimental nodes in search`.
