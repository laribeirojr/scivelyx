# The window

This chapter shows the parts of the program window and what each one is for. The other chapters refer to them by
the names used here.

## The start screen

SciVelyx Graphs opens on the start screen.

![The start screen: actions on the left, the gallery of examples on the right]({{AROOT}}assets/manual/start-screen.png)

- **New sheet**, **Open data…** and **Open project…** start the usual work. You can also drag data files or
  projects onto the window.
- **Data from GitHub…** reads a file straight from a GitHub repository.
- **Function plot…** draws y = f(x), a parametric curve or a surface without any data.
- **Recent** lists the last projects. A click opens one.
- **Start from an example** opens a ready figure, with its data, as a normal project. Every element can then be
  edited, so the examples are also templates.

The gallery has two groups. The first ten examples use analytic or synthetic data. The next fourteen recreate
figure types from five 2026 papers of colleagues at the University of Brasília:

- X-ray diffraction, magnetization loops and Mössbauer spectra of quasicrystals;
- the phase diagram and the current–voltage curves of a superconductor;
- XRD deconvolution, a Tauc plot and a particle-size histogram of CeO₂ nanoparticles;
- thermogravimetry, bar charts with significance marks and PCA scores of dentin samples;
- depth profiles and a FORC diagram of a tropical soil.

Their data are illustrative: they were made to look like the published figures, and each dataset note says so.
**Help → Start page** (Ctrl+Shift+H) comes back to this screen.

## The working window

![The working window with an example figure]({{AROOT}}assets/manual/workspace.png)

| Part | Where | What it does |
|----------|----------|------------------------------------------------------------|
| Menus | top line | Every command of the program, grouped as in Origin: File, Edit, View, Graph, Matrix, Scripts, Format, Analysis, Insert, Layout, Sheet, Examples, Window, Help. |
| Ribbon | below the menus | The most used commands as buttons, in tabs: Home, Sheet, Matrix, Graphs, Analysis, Format, Insert, Layout. |
| Project | left | Sheets, matrices, graphs and folders of the project. Double-click opens an item; right-click creates folders and moves items. |
| Graph tabs | middle | One tab per graph. Each graph has its own undo history. The **+** tab creates a graph. |
| Graph toolbar | above the figure | Home, back and forward, pan, zoom, subplot settings, axis limits, save. **Zoom** sets the screen scale of the page (it does not change the exported size). |
| Figure | middle | The page as it will be exported. The line below it gives the final size in millimetres, the font size and the raster resolution. |
| Properties | right | The object explorer (every element of the figure), the active panel, and the list of series with their data. |
| Messages and Notes | bottom | Results of analyses and warnings; the notes are saved with the project. |
| Status bar | last line | What is selected and what the mouse can do now. |

Docks can be closed, moved or made floating with the mouse; **View** shows them again.

## Selecting and editing

- **Click** an element of the figure (a curve, an axis, the legend, a text) to select it. The status bar names it
  and the object explorer highlights it.
- **Double-click** opens its properties.
- **Right-click** opens a menu with the actions for that element: properties, copy and paste the format, hide,
  delete, bring to front…
- **Drag** moves texts, legends, insets and drawing objects.
- **Delete** removes the selected element; **Ctrl+Z** undoes.

![Properties of a curve: data, line, symbol, fill, error bars, labels, drop lines and colour map]({{AROOT}}assets/manual/properties-curve.png)

![Properties of an axis: scale, limits, ticks, labels, grid and breaks]({{AROOT}}assets/manual/properties-axis.png)

## Sheets

Data live in sheets. Click a sheet in the **Project** dock, or its name in the **Data** tab, to see it. Columns
have a role (X, Y, Z, error…), a long name and units; formulas fill a column from the others.

![A sheet: the first column is X and the others Y]({{AROOT}}assets/manual/sheet.png)

The chapter [Sheets and data](../sheet/) explains import, formulas, masks and the sheet operations.

## Keyboard

| Key | Action |
|------------------------------|----------------------------------------------|
| F1 | Summary of the mouse and keyboard actions |
| Ctrl+N, Ctrl+O, Ctrl+S | New project, open, save |
| Ctrl+Z, Ctrl+Shift+Z (Ctrl+Y on Windows) | Undo, redo (of the active graph) |
| Ctrl+T | New graph |
| Ctrl+E | Export the figure |
| Ctrl+Shift+C | Copy the figure as a picture |
| Ctrl+Alt+C, Ctrl+Alt+V | Copy and paste the format of an element |
| Ctrl+G | Data from GitHub |
| Delete | Remove the selected element |
| Ctrl+Shift+H | Start page |
| Ctrl+Shift+P | Script window |
