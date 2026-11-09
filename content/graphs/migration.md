# Coming from Origin, SciDAVis and QtiPlot

SciPlot-Graphs opens and saves the projects of the programs you already use, so years of finished work come along.
Every import and export produces a **report** with three lists: what came across exactly (✓), what came across
approximately (≈, with the reason) and what did not come across (✗, with the reason). Nothing disappears without a
warning.

| Program | Open in SciPlot-Graphs | Save from SciPlot-Graphs |
|---|---|---|
| **SciDAVis** (`.sciprj`, `.sciprj.gz`, every version) | directly | `.sciprj` in the SciDAVis 2.9 format |
| **QtiPlot** (`.qti`, `.qti.gz`, 0.7 to 0.9.8) | directly | `.qti` in the 0.9.8 format |
| **Origin** (`.opj`, `.opju`) | through Origin itself (below) | a Python script that rebuilds the project inside Origin and saves `.opju` |

QtiPlot 0.9.8 projects, which SciDAVis does not open, reach SciDAVis through SciPlot-Graphs: open the `.qti` and
export it as `.sciprj`.

![A migration report]({{ROOT}}assets/img/migration-report.webp){: width="980" height="260" loading="lazy" }

## One project

**File → Open project** (Ctrl+Shift+O) and choose the `.sciprj`, `.qti` or `.sciplot-origin.json`. The original is
never overwritten: the project opens untitled and is saved as `.splot.json`.

## A whole folder

**File → Migration → Migrate a folder of projects…** converts every project in a folder and its subfolders into
`.splot.json`, each with its `.migration.txt` report. From the command line:

```bash
sciplot migrate old_projects/ -o converted/
```

## Origin projects

**File → Migration → Script to export from Origin…** (or `sciplot origin-script`) saves a small Python script. Open
the project in Origin 2021 or later and run the script in Origin's Python window (Connectivity → Python). It only
reads the project and writes a `.sciplot-origin.json` next to it; open that file in SciPlot-Graphs. The other way
round, **File → Migration → Export project to…** with the `.py` type writes a script that rebuilds sheets, graphs
and notes in Origin.

## What is converted

- **Sheets:** values, text and date columns, designations, long names and units, comments, masks and formulas. A
  formula stays live only if it reproduces the saved values; otherwise the values stay and the formula goes to the
  column comment, and the report says why.
- **Matrices:** they arrive as matrices with their coordinates and go back as matrices.
- **2D graphs:** lines, symbols, bars, areas, stems, steps, histograms, boxes, pies, vectors, colour and contour
  maps, function and fit curves (with their parameters), error bars, right and top axes, log scales, limits,
  grids, titles with sub- and superscripts, fonts, legends, texts, arrows and several layers.
- **3D graphs:** surfaces of matrices, of functions and of x, y, z columns.
- **Notes, results log and folders.**

## Known limitations

- Graph types that SciDAVis and QtiPlot do not have (polar, ternary, Smith, violin…) are exported to them as an
  image of the graph, with the PNG next to the project.
- Nested folders become one level in the project explorer.
- The Origin scripts use the official `originpro` API of Origin 2021 or later; reading `.opj` files without Origin
  is not offered yet.
