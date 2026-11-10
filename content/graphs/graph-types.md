# Origin graph types

**Graph → Origin graph types** has one entry for each graph type of Origin's *Basic 2D*,
*Bar, Column*, *Pie, Doughnut*, *Area*, *Multi-axis, multi-panel* and *Statistical* chapters, under Origin's own
names, and since 0.20 also the *Specialized*, *Financial*, *3D XYY*, *3D surfaces*, *3D symbol, bar, vector*,
*Contour*, *Waterfall, grouped, image* and *Map* chapters, and since 0.21 the graphing *Apps* of Origin — 176 types
in all.

To make one:

1. Select the columns in the sheet (Ctrl+click the headers), in the order the table below gives.
2. Choose the type in **Graph → Origin graph types**.

Some types need numbers that are not in your sheet, such as means and confidence intervals, kernel densities,
box statistics, percentages or the polygons of a Sankey diagram. Those numbers are calculated and kept in small
helper sheets named after your sheet. The graph is an ordinary graph: every curve, axis, text and colour can be
edited, and the helper sheets can be inspected or exported.

![Violin with box]({{AROOT}}assets/img/violin-box.webp){: width="1600" height="1000" loading="lazy" }

## Basic 2D

| Graph type | Columns to select |
|---|---|
| Scatter Central | x and y |
| Column Scatter | one column per group |
| Error Band | x, y and the error |
| Scatter + Rug | x and y |
| Line Series | two or more columns; each row becomes a line across them |
| Row-wise (each row a curve) | the columns; their names are the x values if numeric |
| Before and After | the 'before' and the 'after' columns |
| 2 Point Segment | x and y; rows 1–2, 3–4, … are joined |
| 3 Point Segment | x and y; rows 1–3, 4–6, … are joined |
| Spline Connected | x and y |
| Lollipop | categories (or x) and values |
| Density Dots | x and y |
| Color Dots | x, y and optionally the column that sets the colour |
| Colormapped Line Series | x and two or more y columns |
| Stacked Lines by Y Offsets | x and two or more y columns |

## Bar, Column

| Graph type | Columns to select |
|---|---|
| Column + Label | categories (or x) and values |
| 100% Stacked Column | categories and two or more value columns |
| 100% Stacked Bar | categories and two or more value columns |
| Kite Diagram | position along the transect, then one column per species/category |

## Pie, Doughnut

| Graph type | Columns to select |
|---|---|
| 3D Color Pie Chart | categories and values |
| Pie of Pie | categories and values |
| Bar of Pie | categories and values |
| Doughnut of Pie | categories and values |
| Doughnut with Total | categories and values |
| Pie with Different Radius | categories, values (angle) and radius |
| Doughnut with Different Radius | categories, values (angle) and radius |

## Area

| Graph type | Columns to select |
|---|---|
| 100% Stacked Area | x and two or more value columns |
| Fill Area with 2 Colors | x, y and optionally a second y (else y = 0) |

## Multi-axis, multi-panel

| Graph type | Columns to select |
|---|---|
| Double-Y Column | x (or categories), left y, right y |
| 2Ys Column | x (or categories), left y, right y |
| Double-Y Column – Line Symbol | x (or categories), columns, line |
| 2Ys Y-Y (Double Y) | x, left y, right y |
| 3Ys Y-YY | x and three y columns (one left, two right) |
| 3Ys Y-Y-Y | x and three y columns (two left, one right) |
| 4Ys Y-YYY | x and four y columns (one left, three right) |
| 4Ys YY-YY | x and four y columns (two left, two right) |
| Multiple Y Axes | x and 2 to 7 y columns, each with its own axis |
| 9 Panel | x and up to nine y columns |
| Multiple Panels by Label | the label (group) column, x and y |
| Double X | x1, y1, x2, y2 (the second pair uses the top x axis) |

## Statistical

| Graph type | Columns to select |
|---|---|
| Interval Plot | one column per group |
| Bar Chart (mean ± SD) | one column per group |
| Bar Overlap | one column per group |
| Bar Normal | one column per group |
| Box Overlap | one column per group |
| Box Normal | one column per group |
| Half Box | one column per group |
| Scatter Interval | one column per group |
| Marginal Box Charts | x and y |
| Beeswarm | one column per group |
| Histogram + Rug | one column |
| Histogram + Probabilities | one column |
| Multi-Panel Histograms | two or more columns |
| Distribution (+ Rug) | one column |
| Histogram with Labels | one column |
| Population Pyramid | age groups, left values (e.g. men), right values |
| Marginal Plots (grouped) | x, y and the group column |
| Violin with Box | one column per group |
| Violin with Point | one column per group |
| Violin with Quartile | one column per group |
| Violin with Stick | one column per group |
| Split Violin | the two columns compared (left and right half) |
| Half Violin | one column per group |
| Ridgeline | two or more columns (one ridge each) |
| QC (X-bar R) Chart | one column of measurements |
| Bland–Altman | the two methods (A and B) |
| 2Ys Box Chart | two columns with different scales |
| Parallel Plot | numeric columns (optionally a group column first) |
| Parallel Index | numeric columns on a common scale (optionally a group first) |
| Parallel Sets | categorical columns (optionally a weight column last) |
| Alluvial | categorical columns (optionally a weight column last) |
| Sankey | source, target and value |
| Network Plot | source, target and optionally the weight |
| Chord Diagram | source, target and value |
| Hierarchical Edge Bundling | source and target (names 'group.node') |
| Probability Plot | one column |
| Stacked Dot Plot | one or more columns |
| Interaction Plot | response, factor A (x axis), factor B (lines) |
| Main Effects Plot | response and one or more factors |
| Multi-Vari Chart | response, factor A (panels of points), factor B |
| Variability Chart | response, factor A, factor B |
| Symmetry Plot | one column |
| Run Chart | one column in time order |
| CDF Plot | one or more columns |
| Cause-and-Effect (Ishikawa) | category and cause (text columns) |
| Frequency Chart | one column (values or texts) |
| Grouped Histogram | value and group |
| Grouped Scatter | x, y and group |
| Grouped Pareto | group, category and value |

## Specialized

| Graph type | Columns to select |
|---|---|
| Bullet Chart | category, value, target, then 1 to 3 range limits |
| Polar Contour + Gradient Vector | angle (degrees), radius and value |
| Contour Line + Gradient Vector | x, y and z on a grid |
| Piper (Trilinear) Diagram | Ca, Mg, Na+K, Cl, SO4, HCO3+CO3 (meq/L) |
| Durov Diagram | Ca, Mg, Na+K, Cl, SO4, HCO3+CO3 (meq/L) |
| Stiff Diagram | sample name, Na, Ca, Mg, Cl, HCO3, SO4 (optionally Fe, CO3) |
| Polar Vector θrθr | start angle (°), start radius, end angle (°), end radius |
| Polar Vector θRAM | angle (°), radius, direction (°), magnitude |
| Compass Plot | x and y components (arrows from the centre) |
| Radial Bar | category and value |
| Radial Stacked Bar | category and two or more values |
| Right-Triangle Ternary | A, B and C (any scale) |
| Stacked Radial Plot | category and two or more values |
| Ternary Vector | start A, B, C and end A, B, C |
| Wind Rose (binned data) | direction (°), then one frequency column per speed class |
| Wind Rose (raw data) | direction (°) and speed |
| Window-view Browser Graph | x and y |

## Financial

| Graph type | Columns to select |
|---|---|
| Bridge (Waterfall) Chart | category and change |
| Horizontal Bridge Chart | category and change |
| Stacked Bridge Chart | category and two or more changes |
| Stacked Bridge Chart with Total | category and two or more changes |
| High-Low-Close | date/x, high, low, close |
| OHLC-Volume | date/x, open, high, low, close, volume |
| Line (stock) | date/x, close and optionally volume |

## 3D XYY

| Graph type | Columns to select |
|---|---|
| XYY 3D Bars | x (or categories) and one or more y columns |
| 3D Side by Side Bars | x (or categories) and two or more y columns |
| 3D Stacked Bars | x (or categories) and two or more y columns |
| 3D 100% Stacked Bars | x (or categories) and two or more y columns |
| 3D Bars with Error Bar | x, then pairs of y and its error |
| 3D Wall | x and one or more y columns |
| Stacked Wall | x and two or more y columns |
| 100% Stacked Wall | x and two or more y columns |

## 3D surfaces

| Graph type | Columns to select |
|---|---|
| Color Fill Surface | x, y and z on a grid |
| X and Y Constant with Base | x, y and z on a grid |
| 3D Ternary Colormap Surface | A, B, C (fractions) and z |
| Surface with Error Bar (color fill) | x, y, z and the error of z on a grid |
| Surface with Error Bar (colormap) | x, y, z and the error of z on a grid |
| Multiple Surfaces | x, y and two or more z columns on a grid |
| 3D Stacked Surfaces | x, y and two or more z columns on a grid |
| 3D Stacked Heatmaps | x, y and one or more value columns on a grid |

## 3D symbol, bar, vector

| Graph type | Columns to select |
|---|---|
| 3D Scatter with Z Error | x, y, z and the error of z |
| 3D Bars with Categorical XY | x (text or numbers), y (text or numbers), z |
| 3D Stacked Bars (XYZ) | x, y and two or more z columns |
| 3D 100% Stacked Bars (XYZ) | x, y and two or more z columns |
| 3D Floating Bars | x, y, z from and z to |
| 3D Vector XYZ XYZ | start x, y, z and end x, y, z |
| 3D Vector XYZ dXdYdZ | x, y, z and the components dx, dy, dz |

## Contour

| Graph type | Columns to select |
|---|---|
| Contour – Categorical Z | x, y and a text (category) column |
| Polar Heatmap | angle (°), radius and value on a grid |
| Split Heatmap | x, y (numbers or texts), value 1 (upper triangle), value 2 |
| Heatmap with Split Tiles | x, y (numbers or texts) and 2 to 4 values |
| Ternary Contour | A, B, C (fractions) and value |
| Overlaid Contour | x, y and two z columns on a grid |
| Ternary Overlaid Contour | A, B, C (fractions) and two values |

## Waterfall, grouped, image

| Graph type | Columns to select |
|---|---|
| Waterfall Color Mapped by Y | x and two or more y columns |
| Waterfall Color Mapped by Z | x and two or more y columns (numeric names = z) |
| 3D Waterfall | x and two or more y columns |
| Grouped Column (by two factors) | factor A (groups), factor B (bars), value |
| Grouped Box (by two factors) | factor A (groups), factor B (boxes), value |
| Grouped Line + Symbol | x (or factor A), group, value |
| Grouped Scatter (index by two factors) | factor A, factor B, value |
| Image + Profiles | x, y and z on a grid |

## Map

| Graph type | Columns to select |
|---|---|
| Pie Map | x, y, then two or more values (one pie per row) |
| Bar Map | x, y, then one or more values (one bar group per row) |

## Apps (0.21)

The graphing Apps of Origin that draw a new kind of graph. The other Apps (Graph Maker, Batch Plotting, Common Bar
Width, Layer Stack Manager, Color Editor, LaTeX) are tools in **Graph → Apps**; see [Origin Apps](../origin-apps/).

| Graph type | Columns to select |
|---|---|
| Nyquist Plot (with Bode) | frequency, Z′ (real) and Z″ (imaginary) |
| Polar Contour Profile | angle (°), radius and value |
| Means Plot | one column per group |
| Paired Comparison Plot | the two paired columns (before, after) |
| Volcano Plot | log2 fold change, p-value and optionally a label column |
| Rectangle and Ellipse Profile | x, y and z (a grid or scattered) |
| Plot Sub Matrix | x, y and z on a grid |
| Color Spectrum Plot | wavelength (nm) and intensity |
| Chromaticity Diagram (CIE 1931) | x and y chromaticity, or X, Y, Z tristimulus |
| Hansen Solubility Parameter Plot | δD, δP, δH, good (1) or bad (0), optional solvent name |
| Ternary Contour Profile | A, B, C (fractions) and value |
| Kernel Density (Ternary) | A, B and C |
| Kernel Density (Polar) | angle (°) and radius |
| Soil Texture Triangle (USDA) | sand, silt and clay (%) |
| Sediment Classification (Folk) | sand, silt and clay (%) |
| Taylor Diagram | reference (observations), then one column per model |
| 3D Polar Strain Map | angle (°), radius and strain (a polar grid) |
| 3D Wind Rose | direction (°) and speed |
| Isosurface | x, y, z (a 3D grid) and the value |
| 3D Wall Profile | x, y and z on a grid |
| Zoomed Inset | x and one or more y |
| Zoomed Inset Plus (two or three zooms) | x and one or more y |
| Venn Diagram | two or three columns of items (one item per cell) |

## New drawing tools behind them

- **Filled polygons:** a curve kind whose polygons are separated by empty rows, each with its own colour or with
  a colour map. Kites, violins, Sankey links and chords use it.
- **Line segments:** lines broken at empty rows, for rugs, before/after pairs and parallel plots.
- **Colour-mapped line:** a line coloured by a third column.
- **3D polygons, 3D segments, 3D vectors and flat 3D heat maps** (0.20): 3D bars, walls, error bars, vectors
  with a *w* column, and heat maps stacked at different heights.
- **Lit 3D polygons and new colour maps** (0.21): isosurfaces are shaded by a light; the *visible_spectrum*
  colour map and your own colour maps (Graph → Apps → Color editor) appear in every colour-map list.
- **Extra axes:** in the series properties, *Y axis* can be the 2nd to 4th right axis, the 2nd or 3rd left axis
  (offset and coloured like the curve), or the top X axis (Double X).

![Sankey diagram]({{AROOT}}assets/img/sankey.webp){: width="1600" height="1000" loading="lazy" }

![Four Y axes]({{AROOT}}assets/img/four-axes.webp){: width="1600" height="1000" loading="lazy" }

![Ridgeline]({{AROOT}}assets/img/ridgeline.webp){: width="1600" height="1000" loading="lazy" }

![Piper diagram]({{AROOT}}assets/img/piper.webp){: width="1600" height="1000" loading="lazy" }

![Wind rose]({{AROOT}}assets/img/wind-rose.webp){: width="1600" height="1000" loading="lazy" }

![Bridge chart]({{AROOT}}assets/img/bridge.webp){: width="1600" height="1000" loading="lazy" }

![3D 100 % stacked bars]({{AROOT}}assets/img/bars3d.webp){: width="1600" height="1000" loading="lazy" }

![Ternary contour]({{AROOT}}assets/img/ternary-contour.webp){: width="1600" height="1000" loading="lazy" }
