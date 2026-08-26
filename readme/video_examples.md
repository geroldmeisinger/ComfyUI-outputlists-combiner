# Examples for Video workflows

## XYZ-GridPlots with Videos

![XYZ-GridPlots with Videos example](/workflows/video/XYZGridPlotVideos.png)

(ComfyUI workflow included)

You can ignore the subgraph on the left, it's just used  to create 9 ad-hoc videos of animals with colorful hats rotating. Makes use of `Get Video Components` to split a video into individual frames. The `XYZ-GridPlot` is set to `output_is_list` so we get individual frames of whole grid images. These need to be collected with `Image List to Image Batch` first before creating the video in the `Create Video` node (otherwise it would grid n videos with 1 frame).

https://github.com/user-attachments/assets/efc43311-1052-4832-8486-66b938a5d5f3

## Iterate durations

![Iterate durations video example](/workflows/video/Duration.png)

(ComfyUI workflow included)

Makes use of `Number OutputList` to generate a range of durations `[1.0, 2.0, 3.0, ...]` as a data list. The data list is connected with `Iterate Begin -> workflow -> Iterate End` to run the sub-workflow sequentially over the list.

## Iterate resolutions

![Iterate resolutions video example](/workflows/video/Resolution.png)

(ComfyUI workflow included)

Makes use of `Spreadsheet OutputList` to convert the resolution table note from the official text2video template into a list of resolutions `[(608,352),(736,416),(864,480), ...]` as a data list. The data list is connected with `Iterate Begin -> workflow -> Iterate End` to run the sub-workflow sequentially over the list.

## Iterate durations, measure time, write CSV

The following workflow is a extension of "Iterate durations", it generations multiple videos, measures the times and writes them to a CSV file.

![Iterate durations, measure time, write CSV](/workflows/video/Duration_Timer_CSV.png)

(ComfyUI workflow included)

Custom nodes:
- [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling) for `save STRING to file` and `load STRING from file`
- [Crystools](https://github.com/crystian/ComfyUI-Crystools) for `Pipe to` `Pipe from`
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) for `Timer`

Make sure you understand the simpler examples above, how `Iterate Begin/End` works and also how execution order works in ComfyUI (see [explanation from rgthree](https://github.com/rgthree/rgthree-comfy#a-powerful-combination-using-context-context-switch--fast-muter)). In this example some `Pipe from -> Timer -> Pipe to` patterns were added to the MinimaxH3 default template before the `KSampler` and `VAE Decode` nodes to measure their execution time. It's important that all dependent nodes are finished before `Timer=start` (otherwise, if we only used the noise seed for example, the timer might start before all the models are loaded). It's also important that the output passes through the `Timer=stop` and that this is the only source for any downstreams node (otherwise, if we made `KSampler.samples` go to `VAE Decode` independently it might run the decoder before stopping the timer). The comma-separated lines for the CSV files are built with a `Formatted String` and written using `save STRING to file` (in the  subgraph `append STRING to file`). There are additional notes in the workflow to explain specific parts.

Example output for duration:

```csv
index,duration,sampler,decode_video,decode_audio,total,unit
0,2000,48571,11047,330,59948,ms
1,3000,61037,14469,370,75876,ms
2,4000,90756,20683,434,111873,ms
3,5000,99017,24955,530,124502,ms
```

![plot duration](/media/Duration_Timer_CSV_plot_duration.png)

```csv
index,duration,sampler,decode_video,decode_audio,total,unit
0,5,56212,26062,824,83098,steps
1,10,109488,24594,505,134587,steps
2,15,170691,21602,511,192804,steps
3,20,193693,24987,520,219200,steps
```

You can easily adopt this workflow for other values:

**step size**

```csv
index,stepsize,sampler,decode_video,decode_audio,total,unit
0,5,56212,26062,824,83098,steps
1,10,109488,24594,505,134587,steps
2,15,170691,21602,511,192804,steps
3,20,193693,24987,520,219200,steps
```

![plot step size](/media/Duration_Timer_CSV_plot_stepsize.png)

**step resolution**

```csv
index,resolution,sampler,decode_video,decode_audio,total,MP
0,608 x 352,209384,20935,411,230730,0.21
1,736 x 416,325715,26882,414,353011,0.31
2,864 x 480,528057,62051,519,590627,0.41
3,960 x 544,705908,50888,559,757355,0.52
4,1056 x 608,959507,60587,519,1020613,0.64
5,1152 x 640,1278660,74005,571,1353236,0.74
```

![plot step resolution](/media/Duration_Timer_CSV_plot_resolution.png)


## Iterate resolutions, iterate durations, measure time, write CSV

The following workflow is a extension of "Iterate durations, measure time, write CSV", it generations multiple videos for each combination of resolution x durations, measures the time and writes it to a CSV file.

![Iterate durations, measure time, write CSV](/workflows/video/Resolution_Duration_Timer_CSV.png)

(ComfyUI workflow included)

Custom nodes:
- [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling) for `save STRING to file` and `load STRING from file`
- [Crystools](https://github.com/crystian/ComfyUI-Crystools) for `Pipe to` `Pipe from`
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) for `Timer`

Make sure you understand the simpler examples above, how `Iterate Begin/End` works and also how execution order works in ComfyUI (see [explanation from rgthree](https://github.com/rgthree/rgthree-comfy#a-powerful-combination-using-context-context-switch--fast-muter)). In this example some `Pipe from -> Timer -> Pipe to` patterns were added to the MinimaxH3 default template to measure the total execution time (in contrast to the individual times of the sampler and decoder as in the previous example). Note that this also includes the model loading time and will produce wrong results on the first generation. To mitigate this a zero duration run was added. It's also important that the output passes through the `Timer=stop` and that this is the only source for any downstreams node. The comma-separated lines for the CSV files are built with a `Formatted String` and written using `save STRING to file` (in the  subgraph `append STRING to file`). There are additional notes in the workflow to explain specific parts.

Example output
```csv
resolution\video length,0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0
608 x 352,34694,46922,57616,78560,114835,134380,150945,183893
736 x 416,29459,49666,84211,109523,168462,202305,223172,261975
864 x 480,34779,70248,119980,161840,259740,314701,359692,445586
960 x 544,36226,79850,147996,203899,315231,383680,491456,603520
1056 x 608,35898,103637,172406,243467,417185,507748,753206,794601
1152 x 640,33885,113704,186834,262586,454986,601821,896350,1212095
1216 x 672,39751,178621,211445,304997,552472,728026,1240525,1390142
1280 x 736,41593,187896,253539,368939,669417,850895,1483785,1791947
```

![heatmap resolution x duration](/media/Resolution_Duration_Timer_CSV_heatmap.png)

![plot resolution x duration](/media/Resolution_Duration_Timer_CSV_plot.png)
