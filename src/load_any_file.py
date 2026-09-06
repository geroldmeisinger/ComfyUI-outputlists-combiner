import base64
import hashlib
import time
from io import BytesIO
from json import dumps

import chardet
import numpy as np
import torch
from exiftool import ExifTool, ExifToolHelper
from PIL import Image, ImageOps, ImageSequence, UnidentifiedImageError

import node_helpers
from comfy_api.latest import io

from .util import *

MAX_RESULTS = 2 ** 10

class LoadAnyFile(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Loads any text or binary file and provides the file content as string or base64 string. Additionally tries to load it as a `IMAGE`. And also tries to load any metadata.

`filepath` supports ComfyUI's annotated filepaths `[input]` `[output]` or `[temp]`.
`filepath` also support glob-pattern expansions `subdir/**/*.png`.
Internally uses python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`metadata` calls `exiftool`, if it's installed and available at `PATH`, otherwise uses `PIL.Image.info` as a fallback.

For security reason only the following directories are supported: `[input] [output] [temp]`.
For performance reasons the number of files are limited to: {MAX_RESULTS}.
""",
			node_id	= "LoadAnyFile",
			display_name	= "Load Any File",
			category	= CATEGORY,
			inputs	= [
				io.String	.Input("annotated_filepath"	, display_name="filepath"	,  tooltip="Base directory defaults to `[input]` user-directory. Supports glob-pattern expansion `subdir/**/*.png`. Use suffix ` [input]` ` [output]` or ` [temp]` (mind the leading whitespace!) to specify a different ComfyUI user-directory."),
				io.String	.Input("extra"	, display_name="_extra", optional=True, default="", force_input=True	, tooltip="(optional) try to load additional file from string (plaintext or base64)")
			],
			outputs	= [
				io.String	.Output("string"	, display_name="content"	, is_output_list=True, tooltip="File content for text files, base64 for binary files."),
				io.Image	.Output("image"	, display_name="image"	, is_output_list=True, tooltip="Image batch tensor."),
				io.Mask	.Output("mask"	, display_name="mask"	, is_output_list=True, tooltip="Mask batch tensor."),
				io.String	.Output("metadata"	, display_name="metadata"	, is_output_list=True, tooltip="Exif data from ExifTool. Requires `exiftool` command to be available in `PATH`."),
			],
		)
		return ret

	@classmethod
	def execute(cls, annotated_filepath: str, extra: str = "") -> io.NodeOutput:
		# https://github.com/comfyanonymous/ComfyUI/issues/11017
		if not annotated_filepath and not extra:
			ret = io.NodeOutput([], [], [], [])
			return ret

		ret_strings	= []
		ret_images	= []
		ret_masks	= []
		ret_metadata	= []
		file_paths	= get_files(annotated_filepath, MAX_RESULTS, False) if annotated_filepath else []
		if extra: file_paths.append("\0")
		for file_path in file_paths:
			if file_path != "\0":
				#try:
					with open(file_path, "rb") as f:
						raw_data = f.read()
				#except: continue
			else:
				raw_data = extra.encode('utf-8')

			is_binary = True
			is_base64 = False

			# check if textfile or binary or base64
			try:
				result	= chardet.detect(raw_data[:1024]) # trunc for performance
				encoding	= result["encoding"]
				if encoding and result["confidence"] > 0.9:
					filecontent	= raw_data.decode(encoding)
					is_binary	= False

					# check if base64
					try:
						_ = base64.b64decode(filecontent, validate=True)
						is_base64 = True
					except (base64.binascii.Error, ValueError): pass
				else:
					filecontent = base64.b64encode(raw_data).decode("utf-8")
			except (UnicodeDecodeError, TypeError):
				filecontent = base64.b64encode(raw_data).decode("utf-8")

			image_data	= raw_data if is_binary else filecontent

			# run exiftool
			metadata = "{}"
			if file_path != "\0":
				try:
					with ExifToolHelper() as et:
						exif	= et.get_metadata(file_path)[0]
						metadata	= dumps(exif, indent=4)
				except FileNotFoundError: pass # exiftool not found in path

			# try to load binary or base64 as image
			pil_img = None
			if is_binary or is_base64:
				try:
					image_data	= raw_data if is_binary else base64.b64decode(filecontent)
					pil_img	= node_helpers.pillow(Image.open, BytesIO(image_data))
					image, mask	= load_image(pil_img)

					if not metadata and pil_img:
						# get info from standard PNG otherwise fall back to exiftool
						if hasattr(pil_img, "info") and pil_img.info and not "exif" in pil_img.info:
							pil_img.info["SourceFile"] = file_path if file_path != "\0" else "\0<input>"
							metadata = dumps(pil_img.info, indent=4, default=to_base64)
				except (UnidentifiedImageError, OSError, ValueError):
					image	= torch.zeros((1,	64, 64, 3	), dtype=torch.float32, device="cpu")
					mask	= torch.zeros((	64, 64	), dtype=torch.float32, device="cpu")
			else:
				image	= torch.zeros((1,	64, 64, 3	), dtype=torch.float32, device="cpu")
				mask	= torch.zeros((	64, 64	), dtype=torch.float32, device="cpu")

			# try to load preview thumbnail PNG
			if not pil_img and "File:PreviewPNG" in metadata:
				if file_path != "\0":
					try:
						with ExifTool(encoding=None, common_args=[]) as et:
							preview_data = et.execute("-b", "-PreviewPNG", file_path, raw_bytes=True)
							pil_img	= node_helpers.pillow(Image.open, BytesIO(preview_data))
							image, mask	= load_image(pil_img)
					except: pass # exiftool not found in path

			ret_strings	.append(filecontent)
			ret_images	.append(image)
			ret_masks	.append(mask)
			ret_metadata	.append(metadata)

		ret = io.NodeOutput(ret_strings, ret_images, ret_masks, ret_metadata)
		return ret

	@classmethod
	def fingerprint_inputs(cls, annotated_filepath: str, extra: str = "") -> str:
		if not annotated_filepath and not extra: return str(time.time()) # https://github.com/comfyanonymous/ComfyUI/issues/11017

		m	= hashlib.sha256()
		file_paths = get_files(annotated_filepath, MAX_RESULTS, False)
		if extra: file_paths.append("\0")
		for file_path in file_paths:
			if file_path != "\0":
				try:
					with open(file_path, 'rb') as f:
						m.update(f.read())
				except: continue # skip non-existing files
			else:
				m.update(extra.encode('utf-8'))
		ret = m.digest().hex()
		return ret

	@classmethod
	def validate_inputs(cls, annotated_filepath: str, extra: str = "") -> bool | str:
		if not annotated_filepath and not extra: return True # https://github.com/comfyanonymous/ComfyUI/issues/11017

		# skip non-existing files check to work together with Bake String
		# file_paths = get_files(annotated_filepath, MAX_RESULTS, False)
		# if len(file_paths) == 0:
		#	return f"No files found in '{annotated_filepath}'"

		return True

def to_base64(data: any) -> str | None:
	if not isinstance(data, bytes): return None
	ret = base64.b64encode(data).decode("utf-8")
	return ret

# from ComfyUI/nodes.py LoadImage
def load_image(img: Image) -> tuple[torch.tensor, torch.tensor]:
	output_images	= []
	output_masks	= []
	w, h	= None, None

	excluded_formats = ['MPO']

	for i in ImageSequence.Iterator(img):
		i = node_helpers.pillow(ImageOps.exif_transpose, i)

		if i.mode == 'I':
			i = i.point(lambda i: i * (1 / 255))
		image = i.convert("RGB")

		if len(output_images) == 0:
			w = image.size[0]
			h = image.size[1]

		if image.size[0] != w or image.size[1] != h:
			continue

		image = np.array(image).astype(np.float32) / 255.0
		image = torch.from_numpy(image)[None,]
		if 'A' in i.getbands():
			mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
			mask = 1. - torch.from_numpy(mask)
		elif i.mode == 'P' and 'transparency' in i.info:
			mask = np.array(i.convert('RGBA').getchannel('A')).astype(np.float32) / 255.0
			mask = 1. - torch.from_numpy(mask)
		else:
			mask = torch.zeros((64,64), dtype=torch.float32, device="cpu")
		output_images	.append(image)
		output_masks	.append(mask.unsqueeze(0))

	if len(output_images) > 1 and img.format not in excluded_formats:
		output_image	= torch.cat(output_images	, dim=0)
		output_mask	= torch.cat(output_masks	, dim=0)
	else:
		output_image	= output_images[0]
		output_mask	= output_masks[0]

	return (output_image, output_mask)
