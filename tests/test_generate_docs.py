# #!/usr/bin/env python

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.outputlists_combiner import *


def generate_table(rows):
	if not rows: return []

	lines = [
		"| Name\t| Type\t| Description\t|",
		"| ---\t| ---\t| ---\t|",
	]

	for name, type, tooltip in rows:
		tooltip = tooltip.replace("\n", " ").strip() if tooltip else ""
		lines.append(f"| {name}\t| {type}\t| {tooltip}\t|")

	lines.append("\n")
	return lines

def test_generate_docs():
	nodes = [
		StringOutputList(),
		NumberOutputList(),
		JSONOutputList(),
		SpreadsheetOutputList(),
		CombineOutputLists(),
		XyzGridPlot(),
		FormattedString(),
		ConvertNumberToIntFloatStr(),
		LoadAnyFile(),
		KSamplerImmediateSave(),
	]

	md_lines = []

	for node_cls in nodes:
		schema = node_cls.define_schema()

		md_lines.append(f"## {schema.display_name}\n")
		md_lines.append("### Description\n")
		md_lines.append((schema.description or "").strip() + "\n")

		# Inputs
		md_lines.append("### Inputs\n")
		input_rows = []
		for input in schema.inputs or []:
			input_rows.append((input.display_name or input.id, input.__class__.__name__, getattr(input, "tooltip", "")))
		md_lines.extend(generate_table(input_rows))

		# Outputs
		md_lines.append("### Outputs\n")
		output_rows = []
		for out in schema.outputs or []:
			output_rows.append((out.display_name or out.id, out.__class__.__name__, getattr(out, "tooltip", "")))
		md_lines.extend(generate_table(output_rows))

	# Ensure output directory exists
	#output_path.parent.mkdir(parents=True, exist_ok=True)

	# Write markdown file
	text = "\n".join(md_lines)
	Path("docs.md").write_text(text, encoding="utf-8")
	print(text)
