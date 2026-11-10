# Editing graphs

A figure is made of **panels** (rows and columns of axes) that hold **series** (curves, bars, maps…), texts,
shapes and a legend. Everything you see is linked to an editable element.

## What a double click opens

| Clicked element | What you can change |
|---|---|
| Titles, axis titles, texts | Text with a symbol palette, 37 Greek letters, sub- and superscripts, partial bold or italic, font, size, colour, rotation, frame and background, with a preview. Invalid math notation is pointed out before it reaches the figure. |
| Axis numbers or axis line | Scale (linear, log, symlog, logit, asinh), limits, inversion; ticks by step, count or explicit positions and labels (Γ, X, M…); number format (scientific ×10ⁿ, fixed, percent, engineering, custom), prefix, suffix, formula, text from a table, weekday and month names, date/time; axis line; grid. |
| Curve, symbols, bars, maps | Type and columns; line (dash, caps, spline, steps, connect across missing data); symbols (filled, half-filled, hollow, every N points); fill under the curve; error bars (plus and/or minus) or an error band; data labels (also from a text column); box and whisker ranges; pie labels and ring; vector heads; colour map, levels and contour labels; 3D styles. |
| Legend | Position (also free), columns, title, font, frame, transparency, order, entries. |
| Colour bar | Title, ticks and format, map, normalization, position, size. |
| Panel background | Projection (2D, 3D, polar, ternary, Smith), background, aspect, grid (also on top of the data), 3D view, zoom and resolution. |
| Outside the panels | The figure: journal, size in mm, DPI, rows and columns of panels, spacing, base font, math font, Matplotlib style sheets, colour cycle, (a)/(b) labels, overall title. |

![The axis dialog]({{AROOT}}assets/img/axis-dialog.webp){: width="835" height="900" loading="lazy" }

## Mouse and keyboard

| Action | Result |
|---|---|
| Single click | Selects the element; the object explorer follows. |
| Right click | Element menu: properties, hide, duplicate, delete, highlight a point, insert text or a line. |
| Drag the legend or a text | Moves it (the position is stored). |
| Drag a 3D panel | Rotates it (elevation and azimuth are stored). |
| Delete / Ctrl+Z / Ctrl+Y | Delete the selected element / undo / redo. **Edit → Undo history** lists every step. |
| Ctrl+Alt+C / Ctrl+Alt+V | Copy and paste the format between series, axes, texts, legends or shapes. |
| Alt+Enter | Properties of the selected element. |

## Panels and layout

The **Layout** tab adds and removes columns and rows of panels, sets the projection, shares x or y between
panels, breaks an axis (`//` marks, the range left out) and adds a **secondary axis** with a unit conversion
(eV↔nm, cm⁻¹↔nm, eV↔cm⁻¹, eV↔THz, K↔°C, rad↔degrees, Hartree and Rydberg→eV, a·x+b, a/x). **Insert → Zoom
(inset)** creates an enlarged inset of a region you drag. **Format → Several curves** offers waterfall, stacked
panels, varying symbols and dashes, a scatter matrix and marginal histograms.

## Drawing and annotation

**Insert**: text (click where it goes), arrow with text, horizontal and vertical lines, reference bands, rectangle,
ellipse, line, arrow, polygon, freehand curve, image, legend, colour bar, panel labels (a)(b) and figure title;
**Graph → Equation…** (LaTeX notation) and **Date and time stamp**. **Insert → Data reader** (Ctrl+Shift+R) shows the coordinates
of the nearest point; a double click annotates it.

## Data tools on the graph

**Graph → Data tools**: move points with the mouse (the sheet changes too), drag a whole curve, remove bad points
with a click (the row is masked), select the range used by fits and operations, and read free coordinates. All of
them can be undone.

## Themes and templates

**Format → Save theme…** stores the look of a figure (fonts, sizes, colours, ticks, grid); **Apply theme…** and the
**Theme organizer** (with a preview of the current graph) reuse it. **Save as template** keeps a whole graph,
including its curve types; **Graph from template** builds a new one with other columns.

## 3D

3D line, scatter, surface, mesh, triangulated surface, contour, bars, ribbons and the SciDAVis/QtiPlot styles
(surface with mesh, hidden lines, polygons, points, crosses, cones). Surfaces come from matrices, from x, y, z
columns, from a function z = f(x, y) or from a parametric definition x(u,v), y(u,v), z(u,v). **Graph → 3D rotation
animation…** writes a GIF (or MP4 with ffmpeg).
