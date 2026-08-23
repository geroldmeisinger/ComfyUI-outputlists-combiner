# Installation

## ComfyUI-Manager (recommended)

Search for ```OutputLists Combiner```

![Search OutputLists Combiner in ComfyUI-Manager](/media/ComfyUIManager.png)

## Comfy-CLI

```bash
comfy-cli node install ComfyUI-outputlists_combiner
```

## Manual

```bash
cd custom_nodes # in ComfyUI/
git clone https://github.com/geroldmeisinger/ComfyUI-outputlists-combiner
cd ComfyUI-outputlists-combiner
uv pip install -r requirements.txt
```

## Troubleshooting

```ImportError: libEGL.so.1: cannot open shared object file: No such file or directory```

Newer Skia versions requires `libEGL.so` to be present on Linux hosts, see [official Skia-Python](https://github.com/skia-python/skia-python#install).
```apt-get install libfontconfig1 libgl1-mesa-glx libgl1-mesa-egl libegl1 libglvnd0 libgl1-mesa-dri```
