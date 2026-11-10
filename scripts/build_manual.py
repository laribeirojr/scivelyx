#!/usr/bin/env python3
"""Build the PDF user manual of SciVelyx Graphs from the same Markdown pages as the website.

    python scripts/build_manual.py            # both languages → site/downloads/SciVelyx-Graphs-Manual-<lang>.pdf
    python scripts/build_manual.py pt-br      # one language

Needs pandoc (≥ 2.19) and LuaLaTeX with the KOMA-Script classes, TeX Gyre Pagella and DejaVu fonts.  The chapters
follow the order of site.toml; links between pages become links inside the PDF."""
from __future__ import annotations

import datetime as dt
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CONTENT = ROOT / "content"
CONFIG = tomllib.loads((ROOT / "site.toml").read_text(encoding="utf-8"))
OUT = SITE / "downloads"

TEXT = {
    "en": {"lang": "en-GB", "title": "SciVelyx Graphs", "subtitle": "User manual",
           "slogan": "Science in Motion. Data in Focus.", "version": "Version",
           "mission": "To empower researchers worldwide with fast, precise and intuitive tools for scientific data "
                      "analysis and visualization, transforming complex datasets into clear insights and "
                      "accelerating the path from data to discovery.",
           "site": "This manual is also on the web, where it is updated with each version:",
           "contents": "Contents", "file": "SciVelyx-Graphs-Manual-en.pdf", "web": ""},
    "pt-br": {"lang": "pt-BR", "title": "SciVelyx Graphs", "subtitle": "Manual do usuário",
              "slogan": "Science in Motion. Data in Focus.", "version": "Versão",
              "mission": "Oferecer a pesquisadores de todo o mundo ferramentas rápidas, precisas e intuitivas para "
                         "a análise e a visualização de dados científicos, transformando conjuntos de dados "
                         "complexos em conclusões claras e encurtando o caminho dos dados à descoberta.",
              "site": "Este manual também está na internet, onde é atualizado a cada versão:",
              "contents": "Sumário", "file": "SciVelyx-Graphs-Manual-pt-br.pdf", "web": "pt-br/"},
}


def site_url() -> str:
    base = CONFIG["site"]["base_path"].strip("/")
    return CONFIG["site"]["origin"].rstrip("/") + "/" + (base + "/" if base else "")


def chapter(slug: str, text: str, tmp: Path, slugs: list) -> str:
    """One page of the website → one chapter of the PDF."""
    text = re.sub(r"\{:[^}]*\}", "", text)                                 # attr_list
    text = re.sub(r'<div class="manual-download">.*?</div>\s*', "", text, flags=re.S)
    text = re.sub(r"^The PDF has the same chapters.*?\n\n", "", text, flags=re.M)
    text = re.sub(r"^O PDF tem os mesmos capítulos.*?\n\n", "", text, flags=re.M)

    def image(m):
        alt, src = m.group(1), m.group(2)
        src = src.replace("{{AROOT}}", "")
        f = SITE / src
        if not f.exists():
            return alt
        jpg = tmp / (f.parent.name + "-" + f.stem + ".jpg")          # smaller PDF; screenshots stay sharp at q 90
        if not jpg.exists():
            im = Image.open(f).convert("RGB")
            if im.width > 1600:
                im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
            im.save(jpg, quality=90, optimize=True)
        f = jpg
        return f"![{alt}]({f.as_posix()})"
    text = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", image, text)

    def link(m):
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        h = href.replace("{{ROOT}}", "").replace("{{AROOT}}", "")
        if h.startswith("downloads/") or h.startswith("assets/"):
            return label
        h = h.split("#")[0].strip("/")
        h = h.removeprefix("graphs/docs").strip("/").removeprefix("../").strip("/")
        target = h.split("/")[-1] if h else "index"
        if target in slugs:
            return f"[{label}](#ch-{target})"
        if h in ("graphs", "") or "download" in href:
            return label
        return label
    text = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    lines = text.split("\n")
    lines[0] = re.sub(r"^# (.+)$", lambda m: f"# {m.group(1)} {{#ch-{slug}}}", lines[0])
    return "\n".join(lines)


PREAMBLE = r"""
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{DejaVu Sans}[Scale=0.9]
\setmonofont{DejaVu Sans Mono}[Scale=0.82]
\newfontfamily\fallbackfont{DejaVu Serif}[Scale=0.92]
\usepackage{newunicodechar}
FALLBACKS
\usepackage{xcolor}
\definecolor{svnavy}{HTML}{002050}
\definecolor{svcyan}{HTML}{0BBAF4}
\addtokomafont{disposition}{\color{svnavy}}
\addtokomafont{chapter}{\sffamily\bfseries}
\usepackage{graphicx}
\setkeys{Gin}{width=\linewidth,height=0.42\textheight,keepaspectratio}
\usepackage{float}
\floatplacement{figure}{H}
\usepackage[font=small,labelformat=empty]{caption}
\usepackage{scrlayer-scrpage}
\pagestyle{scrheadings}
\clearpairofpagestyles
\ohead{\small\sffamily SciVelyx Graphs}
\ihead{\small\sffamily\leftmark}
\ofoot*{\small\sffamily\pagemark}
\setlength{\emergencystretch}{3em}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
"""

COVER = r"""
\begin{titlepage}
\centering
\vspace*{2.2cm}
\includegraphics[width=3.2cm]{@@LOGO@@}\par
\vspace{1.2cm}
{\fontsize{40}{46}\selectfont\color{svnavy} @@TITLE@@\par}
\vspace{0.35cm}
{\Large\sffamily @@SUBTITLE@@\par}
\vspace{0.8cm}
{\large\itshape @@SLOGAN@@\par}
\vspace{0.4cm}
{\color{svcyan}\rule{6cm}{1.2pt}\par}
\vspace{1.4cm}
\begin{minipage}{0.78\textwidth}\centering\normalsize @@MISSION@@\end{minipage}
\vfill
{\sffamily @@VERSIONLABEL@@ @@VERSION@@ \textbullet{} @@DATE@@\par}
\vspace{0.3cm}
{\small @@SITETEXT@@\par\url{@@SITEURL@@}\par}
\end{titlepage}
"""


def fallbacks(text: str) -> str:
    """Characters that TeX Gyre Pagella lacks are printed with DejaVu Serif (XeLaTeX has no automatic fallback)."""
    from fontTools.ttLib import TTFont
    pag = subprocess.run(["kpsewhich", "texgyrepagella-regular.otf"], capture_output=True, text=True).stdout.strip()
    cmap = TTFont(pag).getBestCmap()
    skip = set("\\{}$&#^_%~")
    chars = sorted({c for c in text if ord(c) > 127 and ord(c) not in cmap and c not in skip})
    return "\n".join(f'\\newunicodechar{{{c}}}{{{{\\fallbackfont\\char"{ord(c):04X}\\relax}}}}' for c in chars)


def build(lang: str) -> Path:
    T = TEXT[lang]
    base = CONTENT / "graphs" if lang == "en" else CONTENT / lang / "graphs"
    slugs = CONFIG["guides"]["graphs"]
    version = CONFIG["apps"]["graphs"]["version"]
    tmp = Path(tempfile.mkdtemp(prefix="manual-"))
    parts = []
    for slug in slugs:
        text = (base / f"{slug}.md").read_text(encoding="utf-8")
        parts.append(chapter(slug, text, tmp, slugs))
    md = "\n\n".join(parts)
    (tmp / "manual.md").write_text(md, encoding="utf-8")
    logo = SITE / "assets" / "apple-touch-icon.png"
    values = {"LOGO": logo.as_posix(), "TITLE": T["title"], "SUBTITLE": T["subtitle"], "SLOGAN": T["slogan"],
              "MISSION": T["mission"], "VERSIONLABEL": T["version"], "VERSION": version,
              "DATE": dt.date.today().isoformat(), "SITETEXT": T["site"],
              "SITEURL": site_url() + T["web"] + "graphs/docs/"}
    cover = re.sub(r"@@([A-Z]+)@@", lambda m: values[m.group(1)], COVER)
    pre = PREAMBLE.replace("FALLBACKS", fallbacks(md))
    (tmp / "preamble.tex").write_text(pre + "\\AtBeginDocument{\\hypersetup{pdftitle={" + T["title"] + " — "
                                      + T["subtitle"] + "}, pdfauthor={SciVelyx Suite}}}\n", encoding="utf-8")
    (tmp / "cover.tex").write_text(cover, encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    pdf = OUT / T["file"]
    cmd = ["pandoc", str(tmp / "manual.md"), "-o", str(pdf), "--pdf-engine=xelatex",
           "--top-level-division=chapter", "--toc", "--toc-depth=2", "-V", "documentclass=scrreprt",
           "-V", "classoption=oneside", "-V", "papersize=a4", "-V", "fontsize=11pt",
           "-V", "geometry:margin=2.3cm", "-V", f"lang={T['lang']}", "-V", f"toc-title={T['contents']}",
           "-V", "colorlinks=true", "-V", "linkcolor=svnavy", "-V", "urlcolor=svnavy", "-V", "toccolor=black",
           "-M", f"pagetitle={T['title']}",
           "--include-in-header", str(tmp / "preamble.tex"), "--include-before-body", str(tmp / "cover.tex"),
           "--highlight-style=tango", "-V", "microtypeoptions=protrusion=false", "--resource-path", str(SITE)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit(f"pandoc failed for {lang}")
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{pdf.relative_to(ROOT)}  {pdf.stat().st_size // 1024} kB")
    return pdf


if __name__ == "__main__":
    langs = sys.argv[1:] or list(TEXT)
    for lg in langs:
        build(lg)
