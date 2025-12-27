import base64
import re
from io import BytesIO, StringIO

import pandas as pd
from comfy_api.latest import io

from .util import OUTPUTLIST_NOTE


class SpreadsheetOutputList(io.ComfyNode):
	@classmethod
	def define_schema(cls) -> io.Schema:
		ret = io.Schema(
			description	= f"""Creates multiple OutputLists from a spreadsheet (`.csv .tsv .ods .xlsx .xls`).
You can use the `Load any File` node to load a file in base64-encoding.
Internally uses *pandas* [read_excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html) and [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) to load spreadsheet files.
All lists {OUTPUTLIST_NOTE}
""",
			node_id	= "SpreadsheetOutputList",
			display_name	= "Spreadsheet OutputList",
			category	= "Utility",
			inputs	= [
				io.String	.Input("rows_and_cols"	, display_name="rows_and_cols"	, default=	"A B C D"	,	tooltip="Indices and names of rows and columns in the spreadsheet. Note that in spreadsheets rows start at 1, columns start at A, whereas OutputLists are 0-based (in `select-nth`)."),
				io.Int	.Input("header_rows"	, display_name="header_rows"	, default=	1, min=	0, max=65535,	tooltip="Ignore the first x rows in the list. Only used if you specify a col in `rows_and_cols`."),
				io.Int	.Input("header_cols"	, display_name="header_cols"	, default=	1, min=	0, max=65535,	tooltip="Ignore the first x cols in the list. Only used if you specify a row in `rows_and_cols`."),
				io.Int	.Input("select_nth"	, display_name="select_nth"	, default=	-1, min=	-1, max=65535,	tooltip="Only select the nth entry (0-based). Useful in combination with the `PrimitiveInt+control_after_generate=increment` pattern."),
				io.String	.Input("string_or_base64",
					display_name	= "string_or_base64",
					multiline	= True,
					default	= "",
					placeholder	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
					tooltip	= "CSV/TSV string or spreadsheet file in base64 (for `.ods .xlsx .xls`). Use `Load Any File` node to load a file as base64.",
				)
			],
			outputs=[
				io.String	.Output("list_a"	, display_name="list_a"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_b"	, display_name="list_b"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_c"	, display_name="list_c"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.String	.Output("list_d"	, display_name="list_d"	, is_output_list=True	, tooltip=OUTPUTLIST_NOTE),
				io.Int	.Output("count"	, display_name="count"	, is_output_list=False	, tooltip="Number of items in the longest list."),
			]
		)
		return ret

	@staticmethod
	def is_valid_selector(re: re.Pattern[str], sel: str):
		ret = re.match(sel) is not None
		return ret

	@staticmethod
	def col_to_index(col: str):
		total = 0
		for c in col.upper():
			total = total * 26 + (ord(c) - 64)
		return total - 1

	@classmethod
	def execute(self, string_or_base64: str, rows_and_cols: str, header_rows: int, header_cols: int, select_nth: int):
		limit	= 4
		data	= string_or_base64.strip()

		# load spreadsheet with pandas
		try:
			decoded	= base64.b64decode(data, validate=True)
			xls	= pd.read_excel(BytesIO(decoded), sheet_name=None, header=None)
		except Exception:
			try:
				df	= pd.read_csv(StringIO(data), sep=None, engine="python", header=None)
				xls	= {None: df}
			except Exception:
				return ([[] for _ in range(limit)], 0)

		sheet_names	= list(xls.keys())
		default_sheet	= sheet_names[0]

		# regex to select rows and columns with optional sheet reference (e.g. A, 1, AB, $MySheet.123, $'My Sheet'.ABC)
		re_sheet_row_and_col = re.compile(r"""
^(?:\$
	(?:
		'([^']+)' |
		"([^"]+)" |
		([^.]+)
	)
	\.
)?
([A-Za-z]+|\d+)
$""", re.VERBOSE)

		raw = re.split(r"[^A-Za-z0-9$.'\"]+", rows_and_cols or "")
		raw = [s for s in raw if s]

		if not raw:
			selectors = ["A", "B", "C", "D"][:limit]
		else:
			selectors = []
			for sel in raw:
				if re_sheet_row_and_col.match(sel) is not None:
					selectors.append(sel)
				if len(selectors) >= limit: break

		results = [[] for _ in range(len(selectors))]

		# select lists from rows and columns
		for i, sel in enumerate(selectors):
			m = re_sheet_row_and_col.match(sel)
			if not m: continue

			sheet	= m.group(1) or m.group(2) or m.group(3) or default_sheet
			key	= m.group(4)

			if sheet not in xls: continue

			df = xls[sheet]
			if key.isdigit(): # select by row
				row = int(key) - 1 # row selector (1-based)
				if 0 <= row < df.shape[0]:
					results[i] = ["" if (x != x or x is None) else str(x) for x in df.iloc[row, header_cols:].tolist()]
			else: # select by column
				col = SpreadsheetOutputList.col_to_index(key)
				if 0 <= col < df.shape[1]:
					results[i] = ["" if (x != x or x is None) else str(x) for x in df.iloc[header_rows:, col].tolist() ]

		lists = (results + [[]] * limit)[:limit] # pad unused slots with empty lists

		# select nth entry if specified
		if select_nth >= 0: lists = [[lst[select_nth]] if select_nth < len(lst) else [] for lst in lists]

		count = max(map(len, lists), default=0) # longest list

		return (*lists, count)
