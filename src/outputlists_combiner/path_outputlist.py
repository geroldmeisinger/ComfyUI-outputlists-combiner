import hashlib
import time

from comfy_api.latest import io

from .util import *


class PathOutputList(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= """List directory content via glob patterns and split each filepath into it's parts.

`filepath` supports ComfyUI's annotated filepaths `[input]` `[output]` or `[temp]`.
`filepath` also support glob-pattern expansions `subdir/**/*.png`.
Internally uses python's [glob.iglob](https://docs.python.org/3/library/glob.html#glob.iglob).

`bare_strings` is intended for different styles of path recombinations, e.g. "{fulldir}/{basename}.{ext}" vs "{fulldir}{basename}{ext}"

As a design choice the ComfyUI user directory annotation is used in the glob pattern (to allow more flexible patterns) insted of providing a separate variable (in a combo box).
""",
# TODO: For security reason only the following directories are supported: `[input] [output] [temp]`.
			node_id	= "PathOutputList",
			display_name	= "Path OutputList",
			category	= CATEGORY,
			inputs	= [
				io.String	.Input("glob",	display_name="glob"	, tooltip="Glob-pattern expansion `subdir/**/*.png` to list directory content. Base directory defaults to `[input]` user-directory. Use suffix ` [input]` ` [output]` or ` [temp]` (mind the leading whitespace!) to specify a different ComfyUI user-directory."),
				io.Int	.Input("limit",	display_name="limit", min=-1, default=1024, step=1	, tooltip="Limit maximum number of paths to collect (-1.. unlimited)"),
				io.Boolean	.Input("bare_strings",	display_name="bare_strings", default=True	, tooltip="Decides if path-parts only contain the bare strings versus safe OS compliant definitions, e.g. if True `ext` is `png` vs `.png`, `full_dir` is `examples/animals` vs `examples/animals/`, and `parent_dir` may be a empty string vs `./`. Note that `rel_dir` always defaults to `.`")
			],
			outputs	= [
				io.AnyType	.Output("filepath_annotated"	, display_name="filepath+"	, is_output_list=True	, tooltip="Full filepath (relative to a ComfyUI directory) including annotations, e.g. `examples/animals/myfile.png [input]`. Recommended if you want to be specific and adhere to ComfyUI's path notation."),
				io.String	.Output("filepath_rel"	, display_name="filepath"	, is_output_list=True	, tooltip="Full filepath (relative to a ComfyUI directory) without annotations, e.g. `examples/animals/myfile.png`. Recommended if you only load files from input directory anways."),
				io.String	.Output("filename"	, display_name="filename"	, is_output_list=True	, tooltip="Full filename, e.g. `myfile.png`"),
				io.String	.Output("basename"	, display_name="basename"	, is_output_list=True	, tooltip="Basename part of the file without extension, e.g. `myfile`"),
				io.String	.Output("ext"	, display_name="ext"	, is_output_list=True	, tooltip="Extension (e.g. `png` if `bare_strings=True` else `.png'). Note that hidden-files (e.g. `.bashrc`) are considered files without a extension."),
				io.String	.Output("dir_rel"	, display_name="full_dir"	, is_output_list=True	, tooltip="Full directory of the file (relative to a ComfyUI directory), e.g. `examples/animals` if `bare_strings=True` else `examples/animals/` (note the trailing slash)"),
				io.String	.Output("dir_parent"	, display_name="parent_dir"	, is_output_list=True	, tooltip="Immediate parent directory of the file, e.g. `animals` or empty for empty parent if `bare_strings=True` else `./`"),
				io.String	.Output("annotation"	, display_name="annotation"	, is_output_list=True	, tooltip="Annotation to reference the ComfyUI user directory, e.g. `input` if `bare_strings=True` else ` [input]` (note the leading whitespace)"),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Total number of files."),
			],
		)
		return ret

	@classmethod
	def execute(cls, glob: str, limit: int = 1024, bare_strings: bool = True) -> io.NodeOutput:
		# https://github.com/comfyanonymous/ComfyUI/issues/11017
		if not glob:
			ret = io.NodeOutput([], [], [], [], [], [], [], 0)
			return ret

		filepaths = get_files(glob, limit, False)
		if len(filepaths) == 0:
			ret = io.NodeOutput([], [], [], [], [], [], [], 0)
			return ret

		_, annotation	= get_annotation_from_path(glob)
		components	= [split_file_paths(fp, annotation, bare_strings) for fp in filepaths]
		ret	= { key: [value[key] for value in components] for key in components[0] }

		return io.NodeOutput(
			ret["filepath_annotated"],
			ret["filepath_rel"],
			ret["filename"],
			ret["basename"],
			ret["ext"],
			ret["dir_rel"],
			ret["dir_parent"],
			ret["annotation"],
			len(filepaths),
			)

	@classmethod
	def fingerprint_inputs(cls, glob: str, limit: int, bare_strings: bool) -> str:
		if not glob: return str(time.time()) # https://github.com/comfyanonymous/ComfyUI/issues/11017

		m	= hashlib.sha256()
		file_paths = get_files(glob, limit, False)
		for file_path in file_paths:
			with open(file_path, 'rb') as f:
				m.update(f.read())
		ret = m.digest().hex()
		return ret

	@classmethod
	def validate_inputs(cls, glob: str, limit: int, bare_strings: bool) -> bool | str:
		if not glob: return True # https://github.com/comfyanonymous/ComfyUI/issues/11017

		file_paths = get_files(glob, limit, False)
		if len(file_paths) == 0:
			return f"No files found in '{glob}'"

		return True
