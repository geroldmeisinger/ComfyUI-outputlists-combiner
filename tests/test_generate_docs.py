# #!/usr/bin/env python

import os
import sys
from pathlib import Path

repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, repo_dir)

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

		md_lines.append(f"## {schema.display_name or schema.node_id}\n")
		#md_lines.append("### Description\n")
		md_lines.append(f"![{schema.display_name or schema.node_id}](/media/{schema.node_id}.png)\n\n(workflow included)\n")
		md_lines.append((schema.description or "").strip() + "\n")

		# Inputs
		md_lines.append("### Inputs\n")
		input_rows = []
		for input in schema.inputs or []:
			type	= "COMBO" if isinstance(input.io_type, list) else str(input.io_type)
			tooltip	= getattr(input, "tooltip", "").replace(INPUTLIST_NOTE, "").strip()
			input_rows.append((input.display_name or input.id, type, tooltip))
		md_lines.extend(generate_table(input_rows))

		# Outputs
		md_lines.append("### Outputs\n")
		output_rows = []
		for out in schema.outputs or []:
			type	= "COMBO" if isinstance(out.io_type, list) else str(out.io_type)
			tooltip	= getattr(out, "tooltip", "").replace(OUTPUTLIST_NOTE, "").strip()
			output_rows.append((out.display_name or out.id, type, tooltip))
		md_lines.extend(generate_table(output_rows))

	# Ensure output directory exists
	#output_path.parent.mkdir(parents=True, exist_ok=True)

	# Write markdown file
	text = "\n".join(md_lines)
	print(text)
	readme_src	= Path(f"{repo_dir}/src_README.md").read_text()
	readme	= readme_src.replace('{NODES}', text)
	Path(f"{repo_dir}/README.md").write_text(readme, encoding="utf-8")
