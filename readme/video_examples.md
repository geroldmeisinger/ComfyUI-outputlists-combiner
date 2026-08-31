# Examples for Video workflows

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

Accompanying [reddit discussion](https://www.reddit.com/r/comfyui/s/WEUYDmVxlH)

Custom nodes:
- [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling) for `save STRING to file` and `load STRING from file`
- [Crystools](https://github.com/crystian/ComfyUI-Crystools) for `Pipe to` `Pipe from`
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) for `Timer`

Make sure you understand the simpler examples above, how `Iterate Begin/End` works and also how execution order works in ComfyUI (see [explanation from rgthree](https://github.com/rgthree/rgthree-comfy#a-powerful-combination-using-context-context-switch--fast-muter)). In this example some `Pipe from -> Timer -> Pipe to` patterns were added to the MinimaxH3 default template before the `KSampler` and `VAE Decode` nodes to measure their execution time. It's important that all dependent nodes are finished before `Timer=start` (otherwise, if we only used the noise seed for example, the timer might start before all the models are loaded). It's also important that the output passes through the `Timer=stop` and that this is the only source for any downstreams node (otherwise, if we made `KSampler.samples` go to `VAE Decode` independently it might run the decoder before stopping the timer). The comma-separated lines for the CSV files are built with a `Format Text` and written using `save STRING to file` (in the  subgraph `append STRING to file`). There are additional notes in the workflow to explain specific parts.

Example output for duration:

```csv
index,duration,sampler,decode_video,decode_audio,total,unit
0,2000,48571,11047,330,59948,ms
1,3000,61037,14469,370,75876,ms
2,4000,90756,20683,434,111873,ms
3,5000,99017,24955,530,124502,ms
```

![plot duration](/media/Duration_Timer_CSV_plot_duration.png)

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


## Generate multiple videos from spreadsheet

https://github.com/user-attachments/assets/f6705477-ad88-4f23-9178-0ea24362948f

Accompanying [reddit discussion](https://www.reddit.com/r/StableDiffusion/s/pYj9KWc8MT)

![Generate multiple videos from spreadsheet](/workflows/video/Spreadsheet_Videos.png)

(ComfyUI workflow included)

Makes use of `Load Any File` node to load a `.csv` spreadsheet file and feeds the text content into a `Spreadsheet OutputList`. The spreadsheet separates the data by `separator=;` and provides each line one-by-one as a data list. `selectors` are empty which means every column is selected. The workflow uses `values_dict` as the data list which contains the row as a dictionary of key-value pairs. The data list is forwarded to a `Iterate Begin -> workflow -> Iterate End` pattern which is required to make the intermediate results of slow workflows (t2v) available on each iteration. Each row is a dictionary and is provided in `Format Text` where we can access the column via `{a[colname]}` to construct the prompt. The prompt is then forwarded to a standard _Text To Video MiniMax H3 template_ for generation. Another `Format Text` + `{a[name]}` is used to construct a readable filename for each video.

`media/example_video.csv`:
```csv
name;description;voice;weapon;killed;enemy;scene;style
Achilles;a muscular ancient Greek warrior in bronze scale armor and a crested helmet;fierce and booming ancient male voice;a long bronze spear with an ash wood shaft;friend;a tall Trojan prince in ornate silver armor and a plumed helmet holding a bloody sword;windy dusty plains outside the massive stone walls of Troy;epic ancient war blockbuster
Beowulf;a towering muscular Norse warrior with long blonde braids and chainmail;deep and boastful Scandinavian male voice;a massive iron broadsword with a golden hilt;king;a terrifying pale female swamp monster with glowing eyes and razor-sharp claws;dark misty cavern filled with glowing treasure and muddy water;dark fantasy epic
King Arthur;a regal middle-aged king in shining silver plate armor and a white tunic;noble and authoritative British male voice;a glowing straight sword with a jeweled crossguard;knight;a young treacherous knight in dark spiked armor with a tattered red cape;foggy muddy battlefield with broken banners and a blood-red sunset;gritty medieval historical drama
Red Riding Hood;a young girl in a bright red wool hooded cloak and a brown peasant dress;innocent but suddenly furious young female voice;a heavy steel woodsman axe with a long wooden handle;grandmother;a large terrifying wolf walking on two legs wearing a tattered nightgown and cap;dark creepy dense forest with twisted thorny trees and heavy fog;dark gothic fairy tale horror
Spartacus;a rugged muscular Thracian gladiator in leather straps and bronze arm guards;gritty and passionate Mediterranean male voice;a curved Thracian sica sword with a wide blade;brother;a wealthy arrogant Roman senator in a white toga with a purple border and a golden laurel;blood-stained sandy gladiator arena with towering stone seats and cheering crowds;epic historical sword-and-sandal
Joan of Arc;a determined teenage girl in custom-fitted silver plate armor and a short black bob haircut;fervent and commanding young French female voice;a steel broadsword with a fleur-de-lis engraved blade;squire;a cruel English bishop in dark flowing ecclesiastical robes and a tall mitre hat;smoky muddy 15th-century battlefield with siege towers and burning wagons;gritty medieval war epic
Snow White;a beautiful young woman in a yellow skirt blue bodice and a red ribbon with pale skin;soft but suddenly vengeful young female voice;a sharp iron dwarven pickaxe with a leather grip;dwarf;an old wicked queen in a black hooded cloak with a tall spiked collar holding a glowing red apple;snowy pine forest with a small rustic cottage and glowing woodland animals;dark fantasy fairy tale
Odysseus;a weathered middle-aged Greek king with a curly beard a tattered tunic and a tired expression;cunning and weary ancient male voice;a large wooden recurve bow with a thick animal gut string;dog;a massive one-eyed cyclops with dirty matted hair holding a giant wooden club;cavernous dark limestone cave filled with giant sheep and a massive boulder door;ancient mythological adventure
Ragnar Lothbrok;a charismatic Viking jarl with long braided blonde hair blue face paint and a fur mantle;intense and raspy Scandinavian male voice;a broad iron Danish axe with a long wooden haft;shieldmaiden;a cruel Northumbrian king in a golden tunic and a heavy iron crown holding a venomous snake;muddy snowy Viking village with longhouses and burning ships;gritty Viking historical drama
Robin Hood;a cheerful outlaw in Lincoln green tights a brown tunic and a feathered cap;witty and charismatic British male voice;a tall yew longbow with a linen string;peasant;a corrupt wealthy sheriff in a heavy velvet robe a fur collar and a gold chain;lush green Sherwood forest with massive ancient oak trees and dappled sunlight;classic swashbuckling adventure
```

Either copy to `ComfyUI/input` or copy-paste directly into the `Spreadsheet OutputList`.


## Load multiple video files from disk

![Load multiple video files](/workflows/video/LoadMultipleVideos.png)

(ComfyUI workflow included)

Makes use of the `Path OutputList` to generate a data list of filepaths in the output directory. For each iteration the filepath is used in `Load Any Video` to load the video file and forwarded to the default _Minimax H3 reference2video_ workflow to put the fennec fox girl in the reference video.

Notes:
* The only reason the `Load Any Video` exists is because the official node [doesn't support dynamic inputs](https://github.com/comfyanonymous/ComfyUI/issues/11017). * If you want to iterate over ALL videos in a directory (instead of a glob) you can use the Comfy Core `Load Video (from Folder)` instead.
* The `Iterate Begin -> workflow -> Iterate End` pattern is only required to make the intermediate results of slow workflows (ref2v) available on each iteration.

## Iterate resolutions, iterate durations, measure time, write CSV

The following workflow is a extension of "Iterate durations, measure time, write CSV", it generations multiple videos for each combination of resolution x durations, measures the time and writes it to a CSV file.

![Iterate durations, measure time, write CSV](/workflows/video/Resolution_Duration_Timer_CSV.png)

(ComfyUI workflow included)

Accompanying [reddit discussion](https://www.reddit.com/r/comfyui/s/WEUYDmVxlH)

Custom nodes:
- [Basic Data Handling](https://github.com/StableLlama/ComfyUI-basic_data_handling) for `save STRING to file` and `load STRING from file`
- [Crystools](https://github.com/crystian/ComfyUI-Crystools) for `Pipe to` `Pipe from`
- [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) for `Timer`

Make sure you understand the simpler examples above, how `Iterate Begin/End` works and also how execution order works in ComfyUI (see [explanation from rgthree](https://github.com/rgthree/rgthree-comfy#a-powerful-combination-using-context-context-switch--fast-muter)). In this example some `Pipe from -> Timer -> Pipe to` patterns were added to the MinimaxH3 default template to measure the total execution time (in contrast to the individual times of the sampler and decoder as in the previous example). Note that this also includes the model loading time and will produce wrong results on the first generation. To mitigate this a zero duration run was added. It's also important that the output passes through the `Timer=stop` and that this is the only source for any downstreams node. The comma-separated lines for the CSV files are built with a `Format Text` and written using `save STRING to file` (in the  subgraph `append STRING to file`). There are additional notes in the workflow to explain specific parts.

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

## XYZ-GridPlots with Videos

![XYZ-GridPlots with Videos example](/workflows/video/XYZGridPlotVideos.png)

(ComfyUI workflow included)

You can ignore the subgraph on the left, it's just used  to create 9 ad-hoc videos of animals with colorful hats rotating. Makes use of `Get Video Components` to split a video into individual frames. The `XYZ-GridPlot` is set to `output_is_list` so we get individual frames of whole grid images. These need to be collected with `Image List to Image Batch` first before creating the video in the `Create Video` node (otherwise it would grid n videos with 1 frame).

https://github.com/user-attachments/assets/efc43311-1052-4832-8486-66b938a5d5f3
