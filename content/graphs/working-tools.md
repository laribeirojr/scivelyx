# Plot wizard, windows and presentations

Version 0.17 added the last tools of SciDAVis and QtiPlot that SciVelyx Graphs did not have yet. They speed up
everyday work with many sheets and graphs.

## Plot wizard

**Graph → Plot wizard…** builds a graph curve by curve, without selecting columns in the sheet first.

1. Choose the **sheet** and the **type** (line, line + symbol, scatter, error bars, steps, columns, area, stems).
2. Click a column, then **↔ X**. Do the same for **↔ Y**, and for **↔ x error** or **↔ y error** if the curve has
   error bars.
3. Click **New curve →**. X stays chosen, so the next curve only needs a new Y.
4. Choose *in a new graph* or *in the active panel* and click **Plot**.

Curves with an error column are drawn with error bars.

![The plot wizard with two curves]({{AROOT}}assets/img/plot-wizard.webp){: width="720" height="460" loading="lazy" }

## Curves and drawing order

- **Hide other curves** and **Show all curves** are in the right-click menu of a curve and in the Graph menu.
- **Edit → Bring to front** (Ctrl+Shift+]) and **Send to back** (Ctrl+Shift+[) change the drawing order of the
  selected text, shape, image or curve. They are also in the right-click menu.
- **Series → Data → Rows (first; last)** draws a curve from part of its sheet only, for example `11; 60`.

## New graph options

- **Axis break with another scale after it.** In the panel's *Axis break* section, choose *Scale after the x break* (or y) = logarithmic for a linear start followed by decades. You can also set the major steps on each side
  (`before; after`) and the position of the break along the axis.
- **Anti-aliasing:** Figure → *Anti-aliasing*, or Panel → *Anti-aliasing* for one panel.
- **Picture as the symbol:** Series → Symbol → *Picture as the symbol* (a PNG, JPEG…). The height of the picture
  follows the symbol size.
- **Error bars over the symbols:** Series → Error bars → *Through the symbol*.
- **3D pie:** Series → Pie → *3D pie*, with tilt and thickness.
- **Speed mode:** Series → Line → *Speed mode*. Curves longer than the number of points you give are simplified
  with the Douglas–Peucker algorithm. The tolerance is a fraction of the data range, and gaps are kept.
- **Logarithmic 3D axes:** in a 3D panel, *Logarithmic axes* = x, y, z or any combination.

![Logarithmic scale after an axis break, and a 3D pie]({{AROOT}}assets/img/break-pie.webp){: width="1600" height="1000" loading="lazy" }

## Zoom and drag along one axis

**View → Zoom and drag** has *Zoom horizontally*, *Zoom vertically*, *Drag canvas horizontally* and *Drag canvas
vertically*: the other axis stays as it is. *Normal pointer* ends the mode. To keep the result as the axis limits,
use **Lock zoom/pan as limits**.

## Projects and windows

- **File → Append project…** adds the sheets, graphs, notes, folders and scripts of another project to the open one.
  The project can come from SciVelyx, SciDAVis, QtiPlot or the Origin exporter. Sheets whose names are already in
  use are renamed, and the graphs follow the new names.
- **File → Save window as project…** saves the active graph with only the data it uses, including the sheets its
  analyses were computed from, as a project of its own.
- **File → All graphs as a presentation (.odp)…** writes one slide per graph, titled with the graph's name. The file
  opens in LibreOffice Impress and in PowerPoint.
- The **Window** menu lists every graph, sheet and matrix. **Next window** (Ctrl+PgDown) and **Previous window**
  (Ctrl+PgUp) cycle through the graphs. **Open graph in a separate window** shows the active graph in a window of its
  own, which is redrawn after every change; *Tile separate windows* arranges them side by side.

![A graph in a separate window]({{AROOT}}assets/img/separate-window.webp){: width="700" height="340" loading="lazy" }

## Your own menu actions and forms

- **Scripts → Add custom script action…** puts one of your Python files in **Scripts → Custom actions** and on a
  toolbar, with an optional keyboard shortcut. The actions are kept between sessions.
- **Scripts → Open custom interface (.ui)…** shows a form made with Qt Designer. To make it do something, load it
  from a script:

```python
w = load_ui("normalize.ui")
w.runButton.clicked.connect(lambda: print(table(w.sheetEdit.text())["y"].max()))
w.show()
```

The widgets of the form are available by their object names.

## Stem-and-leaf plot

Select a numeric column and choose **Analysis → Stem-and-leaf plot**. The display goes to the project notes and the
Messages dock, and a text graph is created. The leaf unit is chosen so there are about √n stems. In scripts,
`scivelyx.core.extras17.stem_leaf(values, leaf_unit=1, split=2)` splits each stem in two lines.

## Small things

- **Edit → Copy status bar text**, or right-click the status bar.
- **Help → Search for updates…** reads a small file on this website with the latest version number. Nothing about
  you or your computer is sent.
