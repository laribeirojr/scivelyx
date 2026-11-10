#!/usr/bin/env python3
"""Assemble the SciVelyx Suite website into ``_site/`` and check it.

The pages are static HTML in ``site/`` with a few shared fragments in ``site/_partials/``; the user guides are
Markdown in ``content/`` and become pages with the same header, navigation and footer.  The build fails on a
broken local link, a missing image, an image whose width/height attributes do not match the file, invalid
JSON-LD, a third-party resource, or a page above the size budget.

    python scripts/build_site.py            # build and check
    python scripts/build_site.py --serve    # … then serve _site/ on http://localhost:8000/

Environment (optional outside CI):
    SITE_ORIGIN     https://laribeirojr.github.io
    SITE_BASE_PATH  /scivelyx   (empty for a custom domain)
"""
from __future__ import annotations

import argparse
import datetime as _dt
import html
import json
import os
import re
import shutil
import sys
import tomllib
from html.parser import HTMLParser
from pathlib import Path

import markdown
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CONTENT = ROOT / "content"
OUT = ROOT / "_site"
CONFIG = tomllib.loads((ROOT / "site.toml").read_text(encoding="utf-8"))

ORIGIN = os.environ.get("SITE_ORIGIN", CONFIG["site"]["origin"]).rstrip("/")
BASE = os.environ.get("SITE_BASE_PATH", CONFIG["site"]["base_path"]).strip()
BASE = "" if BASE in ("", "/") else "/" + BASE.strip("/")
SITE_URL = f"{ORIGIN}{BASE}/"
PAGE_BUDGET = 400_000            # bytes of HTML + CSS + JS + images referenced by one page (lazy images excluded)

failures: list[str] = []


def check(ok: bool, msg: str) -> bool:
    print(("  PASS  " if ok else "  FAIL  ") + msg)
    if not ok:
        failures.append(msg)
    return ok


LANGS = {
    "en": {"prefix": "", "html": "en", "locale": "en_US", "alt": "pt_BR", "pdf": "SciVelyx-Graphs-Manual-en.pdf",
           "T": {"SKIP": "Skip to content", "HOME_LABEL": "SciVelyx Suite home", "SECTIONS": "Sections",
                 "DOWNLOAD": "Download", "LIGHT": "Switch to light theme", "DARK": "Switch to dark theme",
                 "LANGUAGE": "Language", "GUIDE": "SciVelyx Graphs user manual", "DOWNLOADS": "Downloads",
                 "MANUAL_PDF": "User manual (PDF)", "LATEST": "Latest release", "REPORT": "Report a problem",
                 "PAGES": "Manual pages", "PREV": "Previous", "NEXT": "Next", "GUIDE_TITLE": "SciVelyx Graphs manual"}},
    "pt-br": {"prefix": "pt-br/", "html": "pt-BR", "locale": "pt_BR", "alt": "en_US",
              "pdf": "SciVelyx-Graphs-Manual-pt-br.pdf",
              "T": {"SKIP": "Pular para o conteúdo", "HOME_LABEL": "Início da SciVelyx Suite", "SECTIONS": "Seções",
                    "DOWNLOAD": "Baixar", "LIGHT": "Mudar para o tema claro", "DARK": "Mudar para o tema escuro",
                    "LANGUAGE": "Idioma", "GUIDE": "Manual do usuário do SciVelyx Graphs", "DOWNLOADS": "Downloads",
                    "MANUAL_PDF": "Manual do usuário (PDF)", "LATEST": "Versão mais recente",
                    "REPORT": "Relatar um problema", "PAGES": "Páginas do manual", "PREV": "Anterior",
                    "NEXT": "Próxima", "GUIDE_TITLE": "Manual do SciVelyx Graphs"}},
}
LANG = "en"                     # language of the page being filled (partials may have a translated copy)


def partial(name: str) -> str:
    own = SITE / "_partials" / LANG / f"{name}.html"
    if LANG != "en" and own.exists():
        return own.read_text(encoding="utf-8")
    return (SITE / "_partials" / f"{name}.html").read_text(encoding="utf-8")


def fill(text: str, values: dict) -> str:
    """{{> partial}} includes, then {{KEY}} values (repeated until stable, so partials may use values)."""
    for _ in range(4):
        text = re.sub(r"\{\{>\s*([\w-]+)\s*\}\}", lambda m: partial(m.group(1)), text)
        new = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: str(values.get(m.group(1), m.group(0))), text)
        if new == text:
            break
        text = new
    left = sorted(set(re.findall(r"\{\{[^}]+\}\}", text)))
    check(not left, f"no unfilled placeholder {left}" if left else "placeholders filled")
    return text


def common_values(rel_root: str, url_path: str, title: str, description: str, nav: str, lang: str = "en",
                  aroot: str | None = None) -> dict:
    """``rel_root``: from the page to the root of its language; ``aroot``: to the site root (assets)."""
    graphs = CONFIG["apps"]["graphs"]
    L = LANGS[lang]
    aroot = rel_root if aroot is None else aroot
    tvals = {f"T_{k}": v for k, v in L["T"].items()}
    return {
        **tvals, "AROOT": aroot, "HTML_LANG": L["html"], "OG_LOCALE": L["locale"], "OG_LOCALE_ALT": L["alt"],
        "MANUAL_PDF": L["pdf"],
        "URL_EN": aroot + url_path or "./", "URL_PT": aroot + "pt-br/" + url_path,
        "CUR_EN": str(lang == "en").lower(), "CUR_PT": str(lang == "pt-br").lower(),
        "ABS_EN": SITE_URL + url_path, "ABS_PT": SITE_URL + "pt-br/" + url_path,
        "ROOT": rel_root, "SITE_URL": SITE_URL, "CANONICAL": SITE_URL + L["prefix"] + url_path,
        "TITLE": html.escape(title),
        "DESCRIPTION": html.escape(description), "OG_IMAGE": SITE_URL + "assets/og.png?v=1",
        "YEAR": str(_dt.date.today().year), "NAV": nav,
        "GRAPHS_VERSION": graphs["version"], "GRAPHS_RELEASE_URL": graphs["release_url"],
        "GRAPHS_RELEASES_URL": graphs["releases_url"], "GRAPHS_ISSUES_URL": graphs["issues_url"],
    }


# ------------------------------------------------------------------ navigation
def nav_links(items) -> str:
    return "\n".join(f'          <a href="{href}">{html.escape(label)}</a>' for label, href in items)


NAV_SUITE = {"en": [("Applications", "#apps"), ("SciVelyx Graphs", "graphs/"), ("Principles", "#principles"),
                     ("FAQ", "#faq"), ("Manual", "graphs/docs/")],
             "pt-br": [("Aplicativos", "#apps"), ("SciVelyx Graphs", "graphs/"), ("Princípios", "#principles"),
                       ("Perguntas", "#faq"), ("Manual", "graphs/docs/")]}
NAV_GRAPHS = {"en": [("Editing", "#editing"), ("Analysis", "#analysis"), ("Migration", "#migration"),
                     ("Scripts", "#scripts"), ("Gallery", "#gallery"), ("Download", "#download"), ("Manual", "docs/")],
              "pt-br": [("Edição", "#editing"), ("Análise", "#analysis"), ("Migração", "#migration"),
                        ("Scripts", "#scripts"), ("Galeria", "#gallery"), ("Baixar", "#download"),
                        ("Manual", "docs/")]}


# ------------------------------------------------------------------ guides (Markdown)
def guides(lang: str = "en") -> list[dict]:
    order = CONFIG["guides"]["graphs"]
    out = []
    base = CONTENT / "graphs" if lang == "en" else CONTENT / lang / "graphs"
    for slug in order:
        src = base / f"{slug}.md"
        if not check(src.exists(), f"{lang}: manual page {slug}.md exists"):
            src = CONTENT / "graphs" / f"{slug}.md"
        text = src.read_text(encoding="utf-8")
        m = re.match(r"^# (.+)$", text, re.M)
        out.append({"slug": slug, "title": m.group(1).strip() if m else slug, "text": text})
    return out


def doc_nav(items, current: str, rel_root: str) -> str:
    li = []
    for g in items:
        cur = ' aria-current="page"' if g["slug"] == current else ""
        href = f"{rel_root}graphs/docs/" + ("" if g["slug"] == "index" else f"{g['slug']}/")
        li.append(f'<li><a href="{href}"{cur}>{html.escape(g["title"])}</a></li>')
    return "\n".join(li)


def figures(body: str, aroot: str) -> str:
    """Markdown pictures: true width/height, lazy loading, and a picture alone in a paragraph becomes a
    <figure> whose caption is its alt text."""
    def img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag).group(1)
        if "width=" not in tag and src.startswith(aroot):
            f = SITE / src[len(aroot):]
            if f.exists():
                with Image.open(f) as pic:
                    w, h = pic.size
                tag = tag.replace("<img ", f'<img width="{w}" height="{h}" loading="lazy" ', 1)
        return tag
    body = re.sub(r"<img [^>]+>", img, body)
    return re.sub(r'<p>(<img [^>]*alt="([^"]*)"[^>]*>)</p>',
                  lambda m: f'<figure class="manual-figure">{m.group(1)}<figcaption>{m.group(2)}</figcaption></figure>',
                  body)


def render_guide(g: dict, items: list, k: int, lang: str = "en") -> tuple[str, str]:
    L = LANGS[lang]
    depth = 2 if g["slug"] == "index" else 3
    rel = "../" * depth
    aroot = rel + ("../" if lang != "en" else "")
    url = "graphs/docs/" + ("" if g["slug"] == "index" else f"{g['slug']}/")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
                           extension_configs={"toc": {"permalink": False}})
    body = md.convert(g["text"].replace("{{AROOT}}", aroot).replace("{{ROOT}}", rel)
                      .replace("{{MANUAL_PDF}}", L["pdf"]))
    body = figures(body, aroot)
    first = re.search(r"\n\n([^#\n].+?)\n", g["text"])
    desc = re.sub(r"[*`\[\]]|\(.*?\)", "", first.group(1))[:180] if first else g["title"]
    prev_ = items[k - 1] if k > 0 else None
    next_ = items[k + 1] if k + 1 < len(items) else None

    def link(it, label):
        if it is None:
            return "<span></span>"
        href = f"{rel}graphs/docs/" + ("" if it["slug"] == "index" else f"{it['slug']}/")
        return f'<a class="text-link" href="{href}">{label}: {html.escape(it["title"])}</a>'
    T = L["T"]
    page = fill(partial("doc"), {
        **common_values(rel, url, f"{g['title']} — {T['GUIDE_TITLE']}", desc,
                        nav_links([(lbl, f"{rel}graphs/{h}") for lbl, h in NAV_GRAPHS[lang]]), lang, aroot),
        "DOC_NAV": doc_nav(items, g["slug"], rel), "DOC_BODY": body,
        "DOC_PAGER": link(prev_, T["PREV"]) + link(next_, T["NEXT"])})
    return L["prefix"] + url + "index.html", page


# ------------------------------------------------------------------ checks
class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.imgs, self.scripts, self.jsonld, self._json = [], [], [], [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.refs.append(a["href"])
        if tag == "link" and a.get("href") and a.get("rel") not in ("canonical", "alternate"):
            self.refs.append(a["href"])
            if a.get("rel") == "stylesheet" and a["href"].startswith("http"):
                self.scripts.append(a["href"])
        if tag == "img":
            self.imgs.append(a)
            if a.get("src"):
                self.refs.append(a["src"])
        if tag == "script":
            if a.get("src"):
                self.refs.append(a["src"])
                if a["src"].startswith("http"):
                    self.scripts.append(a["src"])
            if a.get("type") == "application/ld+json":
                self._json = []

    def handle_data(self, data):
        if self._json is not None:
            self._json.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._json is not None:
            self.jsonld.append("".join(self._json))
            self._json = None


def validate(pages: dict[str, str]) -> None:
    ids = {}
    for rel, text in pages.items():
        ids[rel] = set(re.findall(r'\sid="([^"]+)"', text))
    for rel, text in pages.items():
        s = Scan()
        s.feed(text)
        here = (OUT / rel).parent
        broken = []
        for ref in s.refs:
            if not ref or ref.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = ref.partition("#")
            path = path.split("?")[0]
            if not path:
                if frag and frag not in ids[rel]:
                    broken.append(ref)
                continue
            target = (here / path).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(ref)
            elif frag:
                key = str(target.relative_to(OUT.resolve()))
                if key in ids and frag not in ids[key]:
                    broken.append(ref)
        check(not broken, f"{rel}: local links resolve" + (f" — broken {broken}" if broken else ""))
        bad = []
        size = len(text.encode())
        for im in s.imgs:
            src = im.get("src", "")
            if not src:                              # the lightbox image gets its source from the script
                continue
            if src.startswith("http"):
                bad.append(f"{src} (remote)")
                continue
            f = (here / src.split("?")[0]).resolve()
            if not f.exists():
                continue
            if im.get("loading") != "lazy":
                size += f.stat().st_size
            if "width" not in im or "height" not in im:
                bad.append(f"{src} without width/height")
                continue
            with Image.open(f) as pic:
                if (int(im["width"]), int(im["height"])) != pic.size:
                    bad.append(f"{src} is {pic.size}, attributes say {im['width']}×{im['height']}")
            if not im.get("alt") and im.get("alt") != "":
                bad.append(f"{src} without alt")
        check(not bad, f"{rel}: images exist with true sizes and alt text" + (f" — {bad}" if bad else ""))
        check(not s.scripts, f"{rel}: no third-party script or stylesheet {s.scripts if s.scripts else ''}")
        for block in s.jsonld:
            try:
                json.loads(block)
                ok = True
            except json.JSONDecodeError:
                ok = False
            check(ok, f"{rel}: JSON-LD is valid JSON")
        for asset in ("styles.css", "site.js"):
            if asset in text:
                size += (OUT / asset).stat().st_size
        check(size <= PAGE_BUDGET, f"{rel}: {size / 1000:.0f} kB within the {PAGE_BUDGET // 1000} kB budget")


# ------------------------------------------------------------------ build
def build() -> int:
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir()
    global LANG
    for item in SITE.iterdir():
        if item.name.startswith("_") or item.suffix == ".html" or item.name in LANGS:
            continue
        (shutil.copytree if item.is_dir() else shutil.copy2)(item, OUT / item.name)
    shutil.copy2(ROOT / "LICENSE-MDraft.txt", OUT / "assets" / "LICENSE-MDraft.txt")
    pages: dict[str, str] = {}
    specs = [
        ("index.html", "index.html", "./", "", {
            "en": ("SciVelyx Suite — scientific software from the measurement to the paper",
                   "SciVelyx Suite: SciVelyx Graphs for publication figures and data analysis, with SciVelyx Math, "
                   "SciVelyx DFT and SciVelyx MD to come. Science in Motion. Data in Focus."),
            "pt-br": ("SciVelyx Suite — software científico da medida ao artigo",
                      "SciVelyx Suite: SciVelyx Graphs para figuras de publicação e análise de dados; SciVelyx Math, "
                      "SciVelyx DFT e SciVelyx MD a caminho. Science in Motion. Data in Focus.")}, NAV_SUITE),
        ("graphs/index.html", "graphs/index.html", "../", "graphs/", {
            "en": ("SciVelyx Graphs — scientific graphs and data analysis",
                   "Publication figures, curve fitting, peak analysis, spectroscopy, statistics, matrices and Python "
                   "scripts, with project migration from Origin, SciDAVis and QtiPlot. Windows, macOS and Linux."),
            "pt-br": ("SciVelyx Graphs — gráficos científicos e análise de dados",
                      "Figuras de publicação, ajuste de curvas, análise de picos, espectroscopia, estatística, matrizes "
                      "e scripts Python, com migração de projetos do Origin, SciDAVis e QtiPlot. Windows, macOS e "
                      "Linux.")}, NAV_GRAPHS),
        ("404.html", "404.html", "{{ABS}}", "404.html", {
            "en": ("Page not found — SciVelyx Suite", "This page does not exist.")}, NAV_SUITE),
    ]
    for src, dst, rel, url, texts, nav in specs:
        for lang, (title, desc) in texts.items():
            LANG = lang
            L = LANGS[lang]
            path = SITE / src if lang == "en" else SITE / lang / src
            if not check(path.exists(), f"{lang}: page {src} exists"):
                path = SITE / src
            text = path.read_text(encoding="utf-8")
            r, aroot = rel, rel + ("../" if lang != "en" else "")
            links = nav[lang]
            if dst == "404.html":                   # served from any depth: absolute paths under the base
                r = aroot = f"{BASE}/"
                links = [(label, r + href) for label, href in links]
            pages[L["prefix"] + dst] = fill(text, common_values(r, url, title, desc, nav_links(links), lang, aroot))
    for lang in LANGS:
        LANG = lang
        items = guides(lang)
        for k, g in enumerate(items):
            dst, text = render_guide(g, items, k, lang)
            pages[dst] = text
    LANG = "en"
    for dst, text in pages.items():
        (OUT / dst).parent.mkdir(parents=True, exist_ok=True)
        (OUT / dst).write_text(text, encoding="utf-8")
    (OUT / ".nojekyll").write_text("")
    # read by Help → Search for updates in each application (a static file: nothing is sent by the program)
    apps = CONFIG["apps"]
    (OUT / "version.json").write_text(json.dumps(
        {name: {"version": a["version"], "download": a["release_url"], "notes": a.get("releases_url", "")}
         for name, a in apps.items()}, indent=1) + "\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n")
    urls = [SITE_URL + d.removesuffix("index.html") for d in pages if d != "404.html"]
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{html.escape(u)}</loc></url>\n" for u in urls) + "</urlset>\n")
    print(f"Built {len(pages)} pages into {OUT.relative_to(ROOT)}/ for {SITE_URL}")
    validate({k: v for k, v in pages.items() if k != "404.html"})
    if failures:
        print(f"\n{len(failures)} check(s) failed")
        return 1
    print("\nall checks passed")
    return 0


def serve() -> None:
    import functools
    import http.server
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    print("Serving _site/ on http://localhost:8000/ (Ctrl+C stops)")
    http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    args = ap.parse_args()
    code = build()
    if args.serve and code == 0:
        serve()
    sys.exit(code)
