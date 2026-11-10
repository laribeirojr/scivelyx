# Export and publication

## Size first

A figure is defined in millimetres and points, so what you see is what the journal prints. **Format → Journal**
sets the width for common journals and presentations:

| Preset | Width |
|---|---|
| Nature — 1 / 2 columns | 89 mm / 183 mm |
| APS (PRB, PRL) — 1 / 2 columns | 3 3/8 in / 7 in |
| ACS — 1 / 2 columns | 3.25 in / 7 in |
| Elsevier — 1 / 1.5 / 2 columns | 90 / 140 / 190 mm |
| RSC — 1 / 2 columns | 83 mm / 171 mm |
| Presentation 16:9 | 254 mm |

The figure dialog (double-click outside the panels) sets the exact size, the DPI, the base font, the math font
(Computer Modern as in LaTeX, STIX…), Matplotlib style sheets and the colour cycle.

## Formats

**File → Export** (Ctrl+E):

| Format | Use |
|---|---|
| PDF, SVG, EPS | Vector files at the exact size, with TrueType fonts embedded and the text editable. |
| PNG, TIFF (LZW), JPEG | Images at the resolution you choose. |
| Copy figure (Ctrl+Shift+C) | Pastes into documents and presentations. |
| Export Python script… | A script that redraws the figure identically, pixel for pixel, from the project data. |

**File → Print…**, **Print preview** and **Print all graphs…** send graphs to a printer or a PDF.

## Several graphs on one page

**Layout → Layout page** (Ctrl+Shift+L) composes graphs from different tabs and texts on a page in millimetres:
move and resize them, arrange them in a grid, align them, add panel letters, and export vector PDF, PNG or TIFF.
The pages are saved in the project.

## The project file

**File → Save** writes one `.scivelyx.json` with the graphs, the notes, the scripts, the layout pages, the column
formulas and designations and the data — embedded, or by reference with a SHA-256 checksum. Projects saved by
earlier versions always open in later ones, including the `.scitrace.json` and `.splot.json` files of the
program's earlier names.
