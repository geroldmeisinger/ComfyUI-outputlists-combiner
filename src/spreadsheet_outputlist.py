import base64
import hashlib
import re
import time
from io import BytesIO, StringIO

import pandas as pd

from comfy_api.latest import io

from .util import *


class SpreadsheetOutputList(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Creates multiple OutputLists from a spreadsheet (`.csv .tsv .md .ods .xlsx .xls`).
You can use the `Load any File` node to load a file in base64-encoding.
Internally uses *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
All lists {OUTPUTLIST_NOTE}

Comments that start with `#` character in textfiles are ignored.
""",
			node_id	= "SpreadsheetOutputList",
			display_name	= "Spreadsheet OutputList",
			category	= CATEGORY,
			inputs	= [
				io.String	.Input("rows_and_cols"	, display_name="selectors"	, default=""	, tooltip=f"A list of selectors separated by `separator` or empty list. The selectors can be names in the headers or column names (`A`, `B`, `C`...`ZZZZ`) or row indices (1...{2**16}). Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`).", placeholder="List of selectors, column names or row indices, or select all if empty."),
				io.String	.Input("separator"	, display_name="separator"	, default=","	, tooltip="Separator character used for selectors and data in text files `(.csv .tsv .md)`. Supports escaping, e.g. `\t` becomes tab character, `\\` becomes backslash."),
				io.Boolean	.Input("is_topdown"	, display_name="direction"	, default=True	, tooltip="Direction of iteration is either row-based (top-down) or column-based (left-to-right)", label_on="top-down", label_off="left-to-right"),
				io.Int	.Input("num_headers"	, display_name="num_headers"	, default= 1, min= 0, max=2**16	, tooltip="Treat the first x rows (or columns) in the spreadsheet as headers and skip them in the list. Uses the header as reference for row (or column) names. If direction=top-down searches the headers in bottom header row first (left-to-right, then iterating up). If direction=left-to-right searches the headers from rightmost header column first (top-down, then iterating left)."),
				io.Int	.Input("select_nth"	, display_name="select_nth"	, default=-1, min=-1, max=2**16	, tooltip="Only select the nth entry (0-based) or ignore if -1. Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern."),
				io.String	.Input("string_or_base64",
					display_name	= "string_or_base64",
					multiline	= True,
					default	= "",
					placeholder	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
					tooltip	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
				)
			],
			outputs=[
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Number of items in the longest list row (or column)."),
				io.Dict	.Output("dict"	, display_name="values_dict"	, is_output_list=True	, tooltip=f"A dictionary using the selectors as keys and the values of the current row (or column). Useful in combination with `Format Text` node. Always includes both the selector and column name (or row index) as alias, if there is a header. {OUTPUTLIST_NOTE}"),
				io.Array	.Output("values"	, display_name="values_list"	, is_output_list=True	, tooltip=f"A list of values of the current row (or column) based on the selectors. Useful in combination with `Format Text` node. {OUTPUTLIST_NOTE}"),
				io.String	.Output("list_a"	, display_name="item_a"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_b"	, display_name="item_b"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_c"	, display_name="item_c"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_d"	, display_name="item_d"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
			]
		)
		return ret

	@classmethod
	def execute(cls, string_or_base64: str, rows_and_cols: str, separator: str, is_topdown: bool, num_headers: int, select_nth: int) -> io.NodeOutput:
		limit = 4
		data = string_or_base64.strip()

		if not data:
			return io.NodeOutput(0, [], [], [], [], [], [])

		xls = load_spreadsheet(data, separator)

		if not xls:
			return io.NodeOutput(0, [], [], [], [], [], [])

		sheet_names = list(xls.keys())
		default_sheet = sheet_names[0]
		df = xls[default_sheet]

		if df.empty:
			return io.NodeOutput(0, [], [], [], [], [], [])

		num_headers = min(num_headers, len(df) if is_topdown else len(df.columns))
		selectors = parse_selectors(rows_and_cols, separator)

		if is_topdown:
			aliases = build_column_aliases(df, num_headers)
		else:
			aliases = build_row_aliases(df, num_headers)

		if not selectors:
			selectors = get_default_selectors(aliases)

		resolved = []

		for selector in selectors:
			index = resolve_alias(selector, aliases)

			if index is None:
				return io.NodeOutput(0, [], [], [], [], [], [])

			resolved.append((selector, index))

		if is_topdown:
			data_df = df.iloc[num_headers:].reset_index(drop=True)
			records = list(data_df.iterrows())
		else:
			data_df = df.iloc[:, num_headers:]
			records = list(data_df.items())

		if select_nth >= 0:
			if select_nth >= len(records):
				return io.NodeOutput(0, [], [], [], [], [], [])

			records = [records[select_nth]]

		values_dict = []
		values_list = []

		for _, record in records:
			current_dict = {}
			current_values = []

			for selector, index in resolved:
				if is_topdown:
					value = normalise_value(record.iloc[index])
					alias_names = aliases[index]
				else:
					value = normalise_value(record.iloc[index])
					alias_names = aliases[index]

				current_values.append(value)

				for alias in alias_names:
					current_dict[alias] = value

			values_dict.append(current_dict)
			values_list.append(current_values)

		count = len(values_dict)
		lists = []

		for index in range(limit):
			lists.append([stringify_value(values[index]) for values in values_list] if index < len(resolved) else [])

		return io.NodeOutput(count, values_dict, values_list, lists[0], lists[1], lists[2], lists[3])

	# @classmethod
	# def fingerprint_inputs(cls, string_or_base64: str, rows_and_cols: str, separator: str, is_topdown: bool, num_headers: int, select_nth: int) -> str:
	#	if not string_or_base64:
	#		return str(time.time())  # https://github.com/comfyanonymous/ComfyUI/issues/11017
	#
	#	m = hashlib.sha256(string_or_base64.encode())
	#	ret = m.digest().hex()
	#	return ret

	@classmethod
	def validate_inputs(cls, string_or_base64: str, rows_and_cols: str, separator: str, is_topdown: bool, num_headers: int, select_nth: int) -> bool | str:
		if not string_or_base64:
			return True  # https://github.com/comfyanonymous/ComfyUI/issues/11017

		return True


def column_to_index(column: str) -> int | None:
	if not re.fullmatch(r"[A-Z]{1,4}", column):
		return None

	index = 0

	for char in column:
		index = index * 26 + ord(char) - ord("A") + 1

	index -= 1

	if index < 0 or index >= 2**16:
		return None

	return index


def column_to_name(index: int) -> str:
	name = ""
	index += 1

	while index:
		index, remainder = divmod(index - 1, 26)
		name = chr(ord("A") + remainder) + name

	return name


def is_column_reference(value: str) -> bool:
	return column_to_index(value) is not None


def is_empty_value(value) -> bool:
	if value is None:
		return True

	try:
		if pd.isna(value):
			return True
	except (TypeError, ValueError):
		pass

	return str(value).strip() == ""


def normalise_value(value):
	if is_empty_value(value):
		return ""

	if hasattr(value, "item"):
		try:
			return value.item()
		except (ValueError, TypeError):
			pass

	return value


def stringify_value(value) -> str:
	value = normalise_value(value)
	return "" if value == "" else str(value)


def load_spreadsheet(data: str, separator: str):
	try:
		decoded = base64.b64decode(data, validate=True)
		xls = pd.read_excel(BytesIO(decoded), sheet_name=None, header=None, keep_default_na=False)

		if isinstance(xls, dict) and xls:
			return xls
	except Exception:
		pass

	try:
		df = pd.read_csv(StringIO(data), sep=separator.encode().decode("unicode_escape"), engine="python", header=None, keep_default_na=False, comment="#")
		return {None: df}
	except Exception:
		return None


def parse_selectors(rows_and_cols: str, separator: str) -> list[str]:
	if not rows_and_cols.strip():
		return []

	ret = [selector.strip() for selector in re.split(rf"(?<!\\){re.escape(separator)}", rows_and_cols) if selector.strip()]
	return ret


def find_header(df: pd.DataFrame, index: int, num_headers: int, is_topdown: bool) -> str:
	if is_topdown:
		for row_index in range(min(num_headers, len(df)) - 1, -1, -1):
			value = str(normalise_value(df.iat[row_index, index])).strip()

			if value and not re.fullmatch(r":?-{3,}:?", value):
				return value
	else:
		for column_index in range(min(num_headers, len(df.columns)) - 1, -1, -1):
			value = str(normalise_value(df.iat[index, column_index])).strip()

			if value and not re.fullmatch(r":?-{3,}:?", value):
				return value

	return ""


def build_column_aliases(df: pd.DataFrame, num_headers: int) -> list[list[str]]:
	aliases = []

	for column_index in range(len(df.columns)):
		header = find_header(df, column_index, num_headers, True)
		column_name = column_to_name(column_index)
		current = [column_name]

		if header and header != column_name:
			current.insert(0, header)

		aliases.append(current)

	return aliases


def build_row_aliases(df: pd.DataFrame, num_headers: int) -> list[list[str]]:
	aliases = []

	for row_index in range(len(df)):
		header = find_header(df, row_index, num_headers, False)
		row_name = str(row_index + 1)
		current = [row_name]

		if header and header != row_name:
			current.insert(0, header)

		aliases.append(current)

	return aliases


def get_default_selectors(aliases: list[list[str]]) -> list[str]:
	return [current[0] for current in aliases]


def resolve_alias(selector: str, aliases: list[list[str]]) -> int | None:
	for index, current in enumerate(aliases):
		if selector in current:
			return index

	return None