# Your first graph

This page takes a data file to a finished, fitted and exported figure. It uses only the window; the same steps can be
scripted later ([Scripts]({{ROOT}}graphs/docs/scripts/)).

## 1. Open the data

**File → Open data** (Ctrl+O) reads CSV, TSV and text in columns (with `#` comments and Fortran `D` exponents), Excel,
LibreOffice (.ods), NumPy, JSON, Parquet, GROMACS `.xvg`, LAMMPS logs, WAV and SQLite. For files with an unusual
layout — a decimal comma, header lines to skip, names on another line — use **File → Import wizard**
(Ctrl+Shift+I), which shows the table while you adjust the options.

The data open as a **sheet**. Each column has a *designation* (X, Y, Z, X error, Y error, Label), a *long name* and
*units*; long name and units become the axis titles, for example “Energy (eV)”. Change them with a right click on the
column header (**Set as X**, **Set as Y**, **Column properties**).

## 2. Plot

Select the columns (Ctrl+click on the headers) and click a button on the **Graphs** tab of the ribbon — *Line*,
*Scatter*, *Error bars*, *Columns*… The graph follows the designations: each Y uses the nearest X to its left, and a
selected Y-error column becomes error bars. Without a selection, the button opens a small setup where you choose the
columns and the target panel.

## 3. Edit

Every element of the figure is editable:

- **double-click** a title, an axis, a curve, the legend or the panel background and its properties open;
- a single click selects (blue outline) and the **Font** bar of the Home and Format tabs changes the selected text;
- drag the legend and texts; drag a 3D panel to rotate it;
- **Delete** removes the selected element, **Ctrl+Z** undoes.

[Editing graphs]({{ROOT}}graphs/docs/editing/) lists what each dialog contains.

## 4. Fit

Click the curve, then **Analysis → Curve fitting** (Ctrl+Shift+F). Choose a model (linear, Gaussian, exponential
decay, Voigt, several peaks, your own formula…), press **Fit**, look at the parameters, the residuals and the
bands, and **Apply to graph**. The fitted curve, the confidence band and a box with the parameters appear on the
graph and are recalculated whenever the data change.

![The fit wizard]({{ROOT}}assets/img/fit-wizard.webp){: width="1260" height="820" loading="lazy" }

## 5. Export

Choose the journal size in **Format → Journal** (e.g. *Nature — 1 column (89 mm)*, *APS — 1 column*), then
**File → Export** (Ctrl+E). PDF, SVG and EPS keep the text editable at the exact physical size; PNG and TIFF use the
resolution you set. **File → Save** keeps everything — data, graphs, notes and scripts — in one `.scitrace.json`
project.

## Try the examples

The **Examples** menu opens ready-made figures (band structure with Γ–X–M ticks, spectrum with density of states,
energy surface in 2D and 3D, molecular-dynamics thermodynamics on two y axes, ternary and Smith charts…). Each one
is fully editable and shows a technique you can reuse.
