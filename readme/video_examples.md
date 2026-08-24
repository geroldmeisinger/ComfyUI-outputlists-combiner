# Examples for Video workflows

## Iterate durations

![Iterate durations video example](/workflows/ExampleVid_00_MinimaxH3_Durations.png)

(ComfyUI workflow included)

## Iterate resolutions

![Iterate durations video example](/workflows/ExampleVid_01_MinimaxH3_Resolutions.png)

(ComfyUI workflow included)

## Iterate durations, measure time, write CSV

The following workflow is a extension of "Iterate durations", it generations multiple videos, measures the time and writes it to a CSV file.

![Iterate durations, measure time, write CSV](/workflows/ExampleVid_03_MinimaxH3_Durations_Timer_CSV.png)

(ComfyUI workflow included)

Custom nodes:
- [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling) for `save STRING to file` and `load STRING from file`
- [Crystools](https://github.com/crystian/ComfyUI-Crystools) for `Pipe to` `Pipe from`
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) for `Timer`

Make sure you understand how `Iterate Begin/End` works (see simpler examples above) and also how execution order works in ComfyUI (see [explanation from rgthree](https://github.com/rgthree/rgthree-comfy#a-powerful-combination-using-context-context-switch--fast-muter)). In this example some `Pipe from -> Timer -> Pipe to` patterns were added to the MinimaxH3 default template before the `KSampler` and `VAE Decode` nodes to measure there execution time. It's important that all dependent nodes are finished before `Timer=start` (otherwise, if we only used the noise seed for example, the timer might start before all the models are loaded). It's also important that the output passes through the `Timer=stop` and that this is the only source for any downstreams node (otherwise, if we made `KSampler.samples` go to `VAE Decode` independently it might run the decoder before stopping the timer). The comma-separated lines for the CSV files are built with a `Formatted String` and written using `save STRING to file` (in the  subgraph `append STRING to file`). There are additional notes in the workflow to explain specific parts.
