# SciPlot-Studio — the SciPlot-Suite website

Source of the website of the **SciPlot-Suite**: one site for every application of the suite —
SciPlot-Graphs today; SciPlot-Math, SciPlot-DFT and SciPlot-MD later — with a page per application,
downloads that point to each application's releases repository, the FAQ and the user guides.

Published with GitHub Pages at **https://ribeirojr-gh.github.io/SciPlot-Studio/** once Pages is enabled
(see below). The page is static: plain HTML, one stylesheet, a small script for the theme switch and the
image viewer, no framework and no third-party request.

## Layout

```
site/
  index.html              suite home page
  graphs/index.html       SciPlot-Graphs page
  404.html
  _partials/              head, header, footer and the guide-page template (included at build time)
  styles.css, site.js     design adapted from the MDraft site (MIT, see LICENSE-MDraft.txt)
  assets/                 icons, Open Graph image, fonts (SIL OFL) and screenshots (WebP)
content/
  graphs/*.md             SciPlot-Graphs user guide (one page per file)
site.toml                 site address, version and release links of each application, guide order
scripts/build_site.py     builds _site/ and checks it
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

- **New release of SciPlot-Graphs:** change `version` under `[apps.graphs]` in `site.toml`.
- **Guide pages:** edit `content/graphs/*.md`; the order of the pages is `guides.graphs` in `site.toml`.
  Images in guides use `![alt]({{ROOT}}assets/img/file.webp){: width="W" height="H" loading="lazy" }`.
- **New application:** add an `[apps.<name>]` table, a `site/<name>/index.html` page and its guide folder.
- **Screenshots:** WebP in `site/assets/img/`, taken from the program in English.

## Publishing (once)

1. Settings → **Pages** → Build and deployment → Source: **GitHub Actions**.
2. Push to `main` (or Actions → Pages → Run workflow). The address appears in the run and under
   Settings → Pages.

A Pages site is public even when the repository is private (GitHub Pro). The downloads it points to stay in
the private `SciPlot-Graphs-releases` repository during the testing phase, so only invited testers can
download.

## Credits

Layout, palette and components adapted, with permission, from the
[MDraft website](https://bgeneto.github.io/MDraft/) by bgeneto (MIT License, `LICENSE-MDraft.txt`).
Typefaces EB Garamond and IBM Plex Mono under the SIL Open Font License (`site/assets/fonts/`).
