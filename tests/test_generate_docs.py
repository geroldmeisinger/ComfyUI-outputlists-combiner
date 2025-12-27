# #!/usr/bin/env python

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

repo_dir	= os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
readme_dir	= Path(f"{repo_dir}/readme")
sys.path.insert(0, repo_dir)

from src.outputlists_combiner import *
from src.outputlists_combiner.util import INPUTLIST_NOTE, OUTPUTLIST_NOTE

iso_set2	= [
	("en"	, "English"),
	("zh_hans"	, "Chinese (Simplified)"	, "zh"),
	("zh_hant"	, "Chinese (Traditional)")	, "zh-hant",
	("fr"	, "French"),
	("pt"	, "Portuguese", "pt-pt"),
	("de"	, "German"),
	("ro"	, "Romanian"),
	("sv"	, "Swedish"),
	("da"	, "Danish"),
	("bg"	, "Bulgarian"),
	("ru"	, "Russian"),
	("cs"	, "Czech"),
	("el"	, "Greek"),
	("uk"	, "Ukrainian"),
	("es"	, "Spanish"),
	("nl"	, "Dutch"),
	("sk"	, "Slovak"),
	("hr"	, "Croatian"),
	("pl"	, "Polish"),
	("lt"	, "Lithuanian"),
	("nb"	, "Norwegian Bokmål"),
	("nn"	, "Norwegian Nynorsk"),
	("fa"	, "Persian"),
	("sl"	, "Slovenian"),
	("gu"	, "Gujarati"),
	("lv"	, "Latvian"),
	("it"	, "Italian"),
	("oc"	, "Occitan"),
	("ne"	, "Nepali"),
	("mr"	, "Marathi"),
	("be"	, "Belarusian"),
	("sr"	, "Serbian"),
	("lb"	, "Luxembourgish"),
	("as"	, "Assamese"),
	("cy"	, "Welsh"),
	("sd"	, "Sindhi"),
	("ga"	, "Irish"),
	("fo"	, "Faroese"),
	("hi"	, "Hindi"),
	("pa"	, "Punjabi"),
	("bn"	, "Bengali"),
	("or"	, "Oriya"),
	("tg"	, "Tajik"),
	("yi"	, "Eastern Yiddish"),
	("sc"	, "Sardinian"),
	("gl"	, "Galician"),
	("ca"	, "Catalan"),
	("is"	, "Icelandic"),
	("li"	, "Limburgish"),
	("af"	, "Afrikaans"),
	("mk"	, "Macedonian"),
	("si"	, "Sinhala"),
	("ur"	, "Urdu"),
	("bs"	, "Bosnian"),
	("hy"	, "Armenian"),
	("my"	, "Burmese"),
	("ar"	, "Arabic"),
	("he"	, "Hebrew"),
	("mt"	, "Maltese"),
	("id"	, "Indonesian"),
	("ms"	, "Malay"),
	("tl"	, "Tagalog"),
	("jv"	, "Javanese"),
	("su"	, "Sundanese"),
	("ta"	, "Tamil"),
	("te"	, "Telugu"),
	("kn"	, "Kannada"),
	("ml"	, "Malayalam"),
	("tr"	, "Turkish"),
	("az"	, "North Azerbaijani"),
	("uz"	, "Northern Uzbek"),
	("kk"	, "Kazakh"),
	("ba"	, "Bashkir"),
	("tt"	, "Tatar"),
	("th"	, "Thai"),
	("lo"	, "Lao"),
	("fi"	, "Finnish"),
	("et"	, "Estonian"),
	("hu"	, "Hungarian"),
	("vi"	, "Vietnamese"),
	("km"	, "Khmer"),
	("ja"	, "Japanese"),
	("ko"	, "Korean"),
	("ka"	, "Georgian"),
	("eu"	, "Basque"),
	("ht"	, "Haitian"),
	("sw"	, "Swahili"),
]

comfy_iso2 = [
	("en"	, "English"),
	("zh_hans"	, "中文"),
	("zh_hant"	, "繁體中文"),
	("ru"	, "Русский"),
	("ja"	, "日本語"),
	("ko"	, "한국어"),
	("fr"	, "Français"),
	("es"	, "Español"),
	("ar"	, "عربي"),
	("tr"	, "Türkçe"),
	("pt"	, "Português (BR)")
]

nodes = [
	StringOutputList(),
	NumberOutputList(),
	JSONOutputList(),
	SpreadsheetOutputList(),
	CombineOutputLists(),
	XyzGridPlot(),
	WorkflowDiscriminator(),
	FormattedString(),
	ConvertNumberToIntFloatStr(),
	LoadAnyFile(),
	KSamplerImmediateSave(),
]

chapters = [
	"overview",
	"toc",
	"installation",
	"changelog",
	"background",
	"nodes",
	"examples",
	"advanced_examples",
	"credits",
]

def test_generate_badges(active_iso = "en"):
	lang_default = iso_set2.pop(0)
	iso_set2.sort(key=lambda x: x[0])
	iso_set2.insert(0, lang_default)

	lines = []
	for iso, _ in iso_set2:
		extra = "lang-"	if iso == lang_default	else ""
		color = "green"	if iso == active_iso	else ("blue" if iso == lang_default else "gray")
		img = f"[![{iso}](https://img.shields.io/badge/{extra}{iso}-{color})](/docs/README.{iso}.md) "
		lines.append(img)

	text	= "\n".join(lines)
	docs_dir	= Path(f"{repo_dir}/.local/")
	badges_path	= docs_dir / "badges.md"
	badges_path.write_text(text, encoding="utf-8")
	print(text)

def test_move_from_downloads():
	docs_dir	= Path(f"{repo_dir}/web/docs/")
	dls_dir	= Path(f"~/Downloads").expanduser()
	header	= f"<!-- This file was auto-translated with an local LLM and last updated on {datetime.now().strftime('%Y-%m-%d')}. -->\n"

	for iso, _, mdtranslator in iso_set2:
		iso_suffix	= mdtranslator if mdtranslator else iso
		lang_dir = docs_dir / iso
		#lang_dir.mkdir(parents=True, exist_ok=True)

		for chapter in chapters:
			dls_path	= dls_dir  / f"{chapter}_{iso_suffix}.md"
			lang_path	= readme_dir / f"{iso}/{chapter}.md"

			if not dls_path.exists(): continue

			try:
				shutil.move(str(dls_path), str(lang_path))
				text = lang_path.read_text(encoding="utf-8")
				lang_path.write_text(header + text, encoding="utf-8")
			except:
				continue

		for node in nodes:
			schema	= node.define_schema()
			dls_path	= dls_dir  / f"{schema.node_id}_{iso_suffix}.md"
			lang_path	= lang_dir / f"{schema.node_id}/{iso}.md"

			if not dls_path.exists(): continue

			try:
				shutil.move(str(dls_path), str(lang_path))
				text = lang_path.read_text(encoding="utf-8")
				lang_path.write_text(header + text, encoding="utf-8")
			except:
				continue

def test_generate_docs():
	def generate_table(rows):
		if not rows: return []

		lines = [
			"| Name | Type | Description |",
			"| --- | --- | --- |",
		]

		for name, type, tooltip in rows:
			tooltip = tooltip.replace("\n", "<br>").strip() if tooltip else ""
			lines.append(f"| `{name}` | `{type}` | {tooltip} |")

		lines.append("")
		return lines

	nodes_dir	= Path(f"{repo_dir}/web/docs/")
	nodes_dir.mkdir(parents=True, exist_ok=True)

	nodes_lines = ["# Nodes"]
	for node in nodes:
		node_lines	= []
		schema	= node.define_schema()
		node_name	= schema.display_name or schema.node_id

		node_lines.append(f"## {node_name}\n")
		#md_lines.append("### Description\n")
		node_lines_img_idx = len(node_lines)
		node_lines.append(f"![{node_name}]({schema.node_id}/{schema.node_id}.png)\n\n(ComfyUI workflow included)\n")
		node_lines.append((schema.description or "").strip() + "\n")

		# Inputs
		node_lines.append("### Inputs\n")
		input_rows = []
		for input in schema.inputs or []:
			type	= "COMBO" if input.io_type.startswith("[") else input.io_type
			tooltip	= getattr(input, "tooltip", "").replace(INPUTLIST_NOTE, "").strip()
			input_rows.append((input.display_name or input.id, type, tooltip))
		node_lines.extend(generate_table(input_rows))

		# Outputs
		node_lines.append("### Outputs\n")
		output_rows = []
		for out in schema.outputs or []:
			type	= "COMBO" if isinstance(out.io_type, list) else out.io_type
			if out.is_output_list:
				type += " 𝌠" # if you want to use a space here make sure it's non-breaking
			tooltip	= getattr(out, "tooltip", "").replace(OUTPUTLIST_NOTE, "").strip()
			output_rows.append((out.display_name or out.id, type, tooltip))
		node_lines.extend(generate_table(output_rows))

		node_text = "\n".join(node_lines)
		node_path = nodes_dir / f"{schema.node_id}.md"
		node_path.write_text(node_text, encoding="utf-8")

		node_locales_dir	= nodes_dir / schema.node_id
		node_locales_path	= node_locales_dir / "en.md"
		node_locales_dir .mkdir(parents=True, exist_ok=True)
		node_locales_path.write_text(node_text, encoding="utf-8")

		# rewrite image path relative to repo root for readme.md
		node_lines[node_lines_img_idx] = f"![{node_name}](/web/docs/{schema.node_id}/{schema.node_id}.png)\n\n(ComfyUI workflow included)\n"

		nodes_lines.extend(node_lines)

	# Ensure output directory exists
	#output_path.parent.mkdir(parents=True, exist_ok=True)

	# Write markdown file
	readme_lines = ["<!--- Auto-generated from readme/! DON'T EDIT THIS FILE! -->"]

	toc_idx = -1
	for chapter in chapters:
		chapter_path = readme_dir / f"{chapter}.md"

		if chapter == "toc":
			toc_idx = len(readme_lines)
			readme_lines.append("")
		elif	chapter == "nodes":
			nodes_text = "\n".join(nodes_lines) + "\n"
			readme_lines.extend(nodes_text.split("\n"))
		else:
			if not chapter_path.exists(): continue

			chapter_text	= chapter_path.read_text(encoding="utf-8")
			chapter_lines	= (chapter_text.strip() + "\n").split("\n")
			readme_lines.extend(chapter_lines)

	toc_lines = []
	for line in readme_lines:
		if line.startswith("## "):
			subheader	= line[3:]
			subheader_a	= subheader.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("/", "").replace("=", "")
			subheader	= subheader.replace("_", "\\_")
			toc_lines.append(f"\t- [{subheader}](#{subheader_a})")
		elif line.startswith("# "):
			header	= line[2:]
			header_a	= header.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("/", "").replace("=", "")
			header	= header.replace("_", "\\_")
			toc_lines.append(f"- [{header}](#{header_a})")
	toc_text = "\n".join(toc_lines) + "\n"

	readme_lines[toc_idx] = toc_text
	readme_text = "\n".join(readme_lines)
	Path(f"{repo_dir}/README.md").write_text(readme_text, encoding="utf-8")
