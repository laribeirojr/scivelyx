#!/usr/bin/env python3
"""Assemble the SciTrace-Suite website into ``_site/`` and check it.

The pages are static HTML in ``site/`` with a few shared fragments in ``site/_partials/``; the user guides are
Markdown in ``content/`` and become pages with the same header, navigation and footer.  The build fails on a
broken local link, a missing image, an image whose width/height attributes do not match the file, invalid
JSON-LD, a third-party resource, or a page above the size budget.

    python scripts/build_site.py            # build and check
    python scripts/build_site.py --serve    # … then serve _site/ on http://localhost:8000/

Environment (optional outside CI):
    SITE_ORIGIN     https://ribeirojr-gh.github.io
    SITE_BASE_PATH  /scitrace-studio   (empty for a custom domain)
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


def partial(name: str) -> str:
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


def common_values(rel_root: str, url_path: str, title: str, description: str, nav: str) -> dict:
    graphs = CONFIG["apps"]["graphs"]
    return {
        "ROOT": rel_root, "SITE_URL": SITE_URL, "CANONICAL": SITE_URL + url_path, "TITLE": html.escape(title),
        "DESCRIPTION": html.escape(description), "OG_IMAGE": SITE_URL + "assets/og.png?v=1",
        "YEAR": str(_dt.date.today().year), "NAV": nav,
        "GRAPHS_VERSION": graphs["version"], "GRAPHS_RELEASE_URL": graphs["release_url"],
        "GRAPHS_RELEASES_URL": graphs["releases_url"], "GRAPHS_ISSUES_URL": graphs["issues_url"],
    }


# ------------------------------------------------------------------ navigation
def nav_links(items) -> str:
    return "\n".join(f'          <a href="{href}">{html.escape(label)}</a>' for label, href in items)


NAV_SUITE = [("Applications", "#apps"), ("SciTrace-Graphs", "graphs/"), ("Principles", "#principles"),
             ("FAQ", "#faq"), ("Guides", "graphs/docs/")]
NAV_GRAPHS = [("Editing", "#editing"), ("Analysis", "#analysis"), ("Migration", "#migration"),
              ("Scripts", "#scripts"), ("Gallery", "#gallery"), ("Download", "#download"), ("Guides", "docs/")]


# ------------------------------------------------------------------ guides (Markdown)
def guides() -> list[dict]:
    order = CONFIG["guides"]["graphs"]
    out = []
    for slug in order:
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


def render_guide(g: dict, items: list, k: int) -> tuple[str, str]:
    depth = 2 if g["slug"] == "index" else 3
    rel = "../" * depth
    url = "graphs/docs/" + ("" if g["slug"] == "index" else f"{g['slug']}/")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "attr_list", "sane_lists"],
                           extension_configs={"toc": {"permalink": False}})
    body = md.convert(g["text"].replace("{{ROOT}}", rel))
    first = re.search(r"\n\n([^#\n].+?)\n", g["text"])
    desc = re.sub(r"[*`\[\]]|\(.*?\)", "", first.group(1))[:180] if first else g["title"]
    prev_ = items[k - 1] if k > 0 else None
    next_ = items[k + 1] if k + 1 < len(items) else None

    def link(it, label):
        if it is None:
            return "<span></span>"
        href = f"{rel}graphs/docs/" + ("" if it["slug"] == "index" else f"{it['slug']}/")
        return f'<a class="text-link" href="{href}">{label}: {html.escape(it["title"])}</a>'
    page = fill(partial("doc"), {
        **common_values(rel, url, f"{g['title']} — SciTrace-Graphs guide", desc,
                        nav_links([(lbl, f"{rel}graphs/{h}") for lbl, h in NAV_GRAPHS])),
        "DOC_NAV": doc_nav(items, g["slug"], rel), "DOC_BODY": body,
        "DOC_PAGER": link(prev_, "Previous") + link(next_, "Next")})
    return url + "index.html", page


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
    for item in SITE.iterdir():
        if item.name.startswith("_") or item.suffix == ".html":
            continue
        (shutil.copytree if item.is_dir() else shutil.copy2)(item, OUT / item.name)
    shutil.copy2(ROOT / "LICENSE-MDraft.txt", OUT / "assets" / "LICENSE-MDraft.txt")
    pages: dict[str, str] = {}
    specs = [
        ("index.html", "index.html", "./", "", "SciTrace-Suite — scientific software from the measurement to the paper",
         "SciTrace-Suite: SciTrace-Graphs for publication figures and data analysis, with SciTrace-Math, SciTrace-DFT "
         "and SciTrace-MD to come. Free of telemetry, reproducible, built for research.", NAV_SUITE),
        ("graphs/index.html", "graphs/index.html", "../", "graphs/",
         "SciTrace-Graphs — scientific graphs and data analysis",
         "Publication figures, curve fitting, peak analysis, statistics, matrices and Python scripts, with project "
         "migration from Origin, SciDAVis and QtiPlot. Windows, macOS and Linux.", NAV_GRAPHS),
        ("404.html", "404.html", "{{ABS}}", "404.html", "Page not found — SciTrace-Suite",
         "This page does not exist.", NAV_SUITE),
    ]
    for src, dst, rel, url, title, desc, nav in specs:
        text = (SITE / src).read_text(encoding="utf-8")
        if dst == "404.html":                       # served from any depth: absolute paths under the base
            rel = f"{BASE}/"
            nav = [(label, rel + href) for label, href in nav]
        pages[dst] = fill(text, common_values(rel, url, title, desc, nav_links(nav)))
    items = guides()
    for k, g in enumerate(items):
        dst, text = render_guide(g, items, k)
        pages[dst] = text
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
