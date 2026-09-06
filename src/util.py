import glob
import os

import numpy as np
import PIL
import skia
import torch

import folder_paths

MAX_RESULTS = 2 ** 10

OUTPUTLIST_NOTE	= "use(s) `is_output_list=True` (indicated by the symbol `𝌠`) and will be processed sequentially by corresponding nodes."
INPUTLIST_NOTE	= "ideally connected to a node with `is_output_list=True` indicated by the symbol `𝌠`."
CATEGORY	= "OutputLists Combiner"

def tensor_to_skia_image(img: torch.tensor) -> skia.Image:
	if img.ndim == 4:
		img = img[0]  # Remove batch dim

	np_img	= img.detach().cpu().numpy().astype(np.float32)
	rgb	= np.clip(np_img * 255.0, 0, 255).astype(np.uint8)  # HWC, RGB
	alpha	= np.full((rgb.shape[0], rgb.shape[1], 1), 255, dtype=np.uint8)
	rgba	= np.concatenate([rgb, alpha], axis=2)  # HWC, RGBA
	rgba	= np.ascontiguousarray(rgba)
	ret	= skia.Image.fromarray(rgba, skia.kRGBA_8888_ColorType)
	return ret

def skia_to_tensor(sk_img: skia.Image) -> torch.tensor:
	arr = sk_img.toarray()  # uint8, shape (H, W, 4), premultiplied
	if arr.shape[2] != 4:
		raise ValueError("Expected RGBA image from Skia")

	rgb	= arr[:, :,	:3].astype(np.float32)  # likely BGR
	alpha	= arr[:, :,	3:4].astype(np.float32)
	rgb_unpremul	= np.where(alpha > 0, rgb / (alpha / 255.0), 0.0)
	rgb_unpremul	= np.clip(rgb_unpremul, 0, 255) / 255.0
	rgb_unpremul	= rgb_unpremul[:, :, ::-1].copy() # fix channel order: BGR -> RGB
	ret	= torch.from_numpy(rgb_unpremul).unsqueeze(0)  # BHWC
	return ret

def skia_to_pil(sk_img: skia.Image) -> PIL.Image:
	arr = sk_img.toarray()  # uint8, shape (H, W, 4), premultiplied
	if arr.shape[2] != 4:
		raise ValueError("Expected RGBA image from Skia")

	# Un-premultiply
	rgb	= arr[:, :, :3].astype(np.float32)  # likely BGR
	alpha	= arr[:, :, 3:4].astype(np.float32)
	rgb_unpremul	= np.where(alpha > 0, rgb / (alpha / 255.0), 0.0)
	rgb_unpremul	= np.clip(rgb_unpremul, 0, 255).astype(np.uint8)
	rgb_unpremul	= rgb_unpremul[:, :, ::-1] # fix channel order: BGR -> RGB
	ret	= PIL.Image.fromarray(rgb_unpremul, mode="RGB")
	return ret

def get_files(annotated_filepath: str, limit: int = -1, rel_path: bool = True) -> list[str]:
	pattern, base_dir	= folder_paths.annotated_filepath(annotated_filepath)
	base_real	= os.path.realpath(base_dir or folder_paths.get_input_directory())

	full_pattern	= os.path.join(base_real, pattern)
	has_glob	= any(c in pattern for c in "*?[")
	recursive	= "**" in pattern

	results	= []
	count	= 0

	# Directory listing without glob
	if not has_glob and os.path.isdir(full_pattern):
		with os.scandir(full_pattern) as it:
			for entry in it:
				if not entry.is_file(): continue

				p = entry.path
				if folder_paths.is_within_directory(base_real, entry.path):
					p = os.path.relpath(entry.path, base_real).replace(os.sep, '/') if rel_path else entry.path
					results.append(p)
					count += 1

		ret = sorted(results)[:limit]
		return ret

	# Glob path - streamed
	for match in glob.iglob(full_pattern, recursive=recursive):
		# Skip directories early
		try:
			if not os.path.isfile(match): continue
		except OSError: continue

		if not folder_paths.is_within_directory(base_real, match): continue

		p = os.path.relpath(match, base_real).replace(os.sep, '/') if rel_path else match
		results.append(p)
		count += 1

	ret = sorted(results)[:limit]
	return ret

def get_annotation_from_path(annotated_filepath: str) -> tuple[str, str]:
    if	annotated_filepath.endswith(" [output]"	): return (annotated_filepath[:-len("output"	)], "output")
    elif	annotated_filepath.endswith(" [input]"	): return (annotated_filepath[:-len("input"	)], "input")
    elif	annotated_filepath.endswith(" [temp]"	): return (annotated_filepath[:-len("temp"	)], "temp")
    return (annotated_filepath, "input")

def split_file_paths(filepath: str, annotation: str, bare_strings: bool) -> dict[str, str]:
	filepath_annotated	= filepath + f" [{annotation}]"
	dir_rel, filename	= os.path.split(filepath)
	basename, ext	= os.path.splitext(filename)
	dir_parent	= os.path.basename(dir_rel)

	ret = {
		"filepath_annotated"	: filepath_annotated,
		"filepath_rel"	: filepath,
		"basename"	: basename,
		"filename"	: filename,
		"ext"	: ext.lstrip(".")	if bare_strings else ext,
		"dir_rel"	: ("." if dir_rel == "" else dir_rel)	if bare_strings else ("./" if dir_rel == "" else dir_rel),
		"dir_parent"	: dir_parent	if bare_strings else ("./" if dir_parent == "" else (dir_parent if dir_parent .endswith('/') else dir_parent + '/')),
		"annotation"	: annotation	if bare_strings else f" [{annotation}]"
	}
	return ret

# def unwrap(input_list):
#	if not isinstance(input_list, list)	: return input_list
#	if len(input_list) != 1	: return input_list
#	return input_list[0]
