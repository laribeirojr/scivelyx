# SciVelyx Studio — the SciVelyx Suite website

Source of the website of the **SciVelyx Suite**: one site for every application of the suite —
SciVelyx Graphs and SciVelyx MD today; SciVelyx Math and SciVelyx DFT later — with a page per application,
downloads that point to each application's releases repository, the FAQ and the user guides.

Published with GitHub Pages at **https://laribeirojr.github.io/scivelyx/** (see “Publishing” below). The page is static: plain HTML, one stylesheet, a small script for the theme switch and the
image viewer, no framework and no third-party request.

## Layout

```
site/
  index.html              suite home page
  graphs/index.html       SciVelyx Graphs page
  md/index.html           SciVelyx MD page
  404.html
  _partials/              head, header, footer and the guide-page template (included at build time)
  styles.css, site.js     design adapted from the MDraft site (MIT, see LICENSE-MDraft.txt)
  assets/                 icons, Open Graph image, fonts (SIL OFL) and screenshots (WebP; SciVelyx MD's in assets/md/)
content/
  graphs/*.md             SciVelyx Graphs user guide (one page per file)
  md/*.md                 SciVelyx MD user guide
site.toml                 site address, version and release links of each application, guide order
scripts/build_site.py     builds _site/ and checks it
scripts/take_screenshots.py  screenshots of the program (needs the source repository)
scripts/make_og.py        draws the Open Graph image site/assets/og.png
.github/workflows/pages.yml   builds and publishes on every push to main
```

## Building locally

```bash
python -m pip install -r requirements.txt
python scripts/build_site.py            # builds _site/ and checks it
python scripts/build_site.py --serve    # … and serves it on http://localhost:8000/
```

The build fails on a broken local link, a missing image, an image whose `width`/`height` do not match the
file, invalid JSON-LD, a third-party script or stylesheet, an unfilled placeholder, or a page above the size
budget.

## Everyday changes

- **New release of SciVelyx Graphs or SciVelyx MD:** change `version` under `[apps.graphs]` or `[apps.md]` in
  `site.toml`.
- **Guide pages:** edit `content/graphs/*.md`; the order of the pages is `guides.graphs` in `site.toml`.
  Images in guides use `![alt]({{ROOT}}assets/img/file.webp){: width="W" height="H" loading="lazy" }`.
- **New application:** add an `[apps.<name>]` table, its guide order under `[guides]`, its name in `APPS` of
  `scripts/build_site.py` and `scripts/build_manual.py`, a `NAV_<NAME>` table, a `site/<name>/index.html` page (and
  `site/pt-br/<name>/index.html`) in the `specs` of the build, and its guide folders `content/<name>/` and
  `content/pt-br/<name>/`. Pages of an application get `APP_*` values (version, release, issues) for the header
  button and the side bar of its manual.
- **Screenshots:** WebP in `site/assets/img/`, taken from the program in English.

## Two languages and the PDF manual

- English is at the root and Portuguese under `pt-br/` (`site/pt-br/…` pages, `content/pt-br/graphs/*.md`), as on
  the MDraft site; the EN/PT links in the header and footer switch between the same page in each language. Partials
  can be overridden per language in `site/_partials/pt-br/`; the short interface strings are the `LANGS` table in
  `scripts/build_site.py`, which also checks that every English page has its Portuguese twin.
- `python scripts/build_manual.py [graphs|md] [en|pt-br]` turns the guide pages into PDF manuals in
  `site/downloads/` (`SciVelyx-Graphs-Manual-<lang>.pdf`, `SciVelyx-MD-Manual-<lang>.pdf`; needs pandoc and XeLaTeX
  with TeX Gyre Pagella and DejaVu). Rebuild them when a guide or its screenshots change, and commit the PDFs: the
  Pages workflow publishes them as they are.
- The manual screenshots in `site/assets/manual/` come from `tools/manual_shots.py` in the source repository of
  SciVelyx Graphs; those of SciVelyx MD in `site/assets/md/` from `tools/md_manual_shots.py SHOTS --site ../scivelyx`
  in the source repository of SciVelyx MD.

## Publishing (once)

1. Settings → **Pages** → Build and deployment → Source: **GitHub Actions**.
2. Push to `main` (or Actions → Pages → Run workflow). The address appears in the run and under
   Settings → Pages.

If the page shows this README instead of the site, the source is still “Deploy from a branch” (GitHub then renders the
README with Jekyll): switch it to **GitHub Actions** and run the workflow again.

The repository and the site are public. The downloads it points to stay in
the private `scivelyx-graphs-releases` repository during the testing phase, so only invited testers can
download.

## Credits

Layout, palette and components adapted, with permission, from the
[MDraft website](https://bgeneto.github.io/MDraft/) by bgeneto (MIT License, `LICENSE-MDraft.txt`).
Typefaces EB Garamond and IBM Plex Mono under the SIL Open Font License (`site/assets/fonts/`).
