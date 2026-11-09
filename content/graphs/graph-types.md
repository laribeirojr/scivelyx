# Origin graph types

Version 0.19 added **Graph → Origin graph types**, with one entry for each graph type of Origin's *Basic 2D*,
*Bar, Column*, *Pie, Doughnut*, *Area*, *Multi-axis, multi-panel* and *Statistical* chapters, under Origin's own
names. (The 3D, contour, specialized and financial chapters come in the next version.)

To make one:

1. Select the columns in the sheet (Ctrl+click the headers), in the order the table below gives.
2. Choose the type in **Graph → Origin graph types**.

Some types need numbers that are not in your sheet, such as means and confidence intervals, kernel densities,
box statistics, percentages or the polygons of a Sankey diagram. Those numbers are calculated and kept in small
helper sheets named after your sheet. The graph is an ordinary graph: every curve, axis, text and colour can be
edited, and the helper sheets can be inspected or exported.

![Violin with box]({{ROOT}}assets/img/violin-box.webp){: width="1600" height="1000" loading="lazy" }

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

## New drawing tools behind them

- **Filled polygons:** a curve kind whose polygons are separated by empty rows, each with its own colour or with
  a colour map. Kites, violins, Sankey links and chords use it.
- **Line segments:** lines broken at empty rows, for rugs, before/after pairs and parallel plots.
- **Colour-mapped line:** a line coloured by a third column.
- **Extra axes:** in the series properties, *Y axis* can be the 2nd to 4th right axis, the 2nd or 3rd left axis
  (offset and coloured like the curve), or the top X axis (Double X).

![Sankey diagram]({{ROOT}}assets/img/sankey.webp){: width="1600" height="1000" loading="lazy" }

![Four Y axes]({{ROOT}}assets/img/four-axes.webp){: width="1600" height="1000" loading="lazy" }

![Ridgeline]({{ROOT}}assets/img/ridgeline.webp){: width="1600" height="1000" loading="lazy" }
