# Origin Apps

Version 0.21 added the free Apps of Origin (standard edition) for analysis and graphing. They sit in four places:

- **Analysis → Apps** for curve fitting, peaks, mathematics, signal and statistics;
- **Sheet → Apps** for data processing;
- **Graph → Apps** for tools that make or change graphs;
- **Graph → Origin graph types → Apps** for the 23 Apps that draw a new kind of graph (see
  [Origin graph types](../graph-types/)).

Tools that work on columns read the columns you select in the sheet (Ctrl+click the headers). Tools that work on a
curve use the curve you clicked on the graph. Tools that compare curves use every curve of the active panel.
Results go to new sheets, to the Messages dock and, where it helps, to a graph.

![Chromaticity diagram]({{ROOT}}assets/img/chromaticity.webp){: width="1600" height="1000" loading="lazy" }

## Curve fitting

| App | What it does |
|---|---|
| Find a fitting function | Fits every built-in model to the selected curve and ranks them by the corrected Akaike criterion (AICc), with Akaike weights. You can have the best model fitted to the curve at once. |
| Simple fit | A quick fit with a model from a short list or your own expression `y = …`. The fitted curve and a result box go on the graph and are refitted when the data change. |
| 2D smoother | A smoothing surface through scattered x, y, z (radial basis functions). Smoothing 0 passes through the points. You get the surface as a contour map and the residuals at each point. |
| Compare datasets | Are the curves of the panel described by one set of parameters? Each curve is fitted alone and all of them together. The extra-sum-of-squares F test and the AIC decide. |
| Compare linear fit parameters and datasets | Tests whether the straight lines through the curves have equal slopes and, if so, equal intercepts (as in an analysis of covariance). |

## Peaks and mathematics

| App | What it does |
|---|---|
| Align peaks | Shifts the curves of the panel along x so that their peaks line up with the first curve. Alignment can use the maximum, the centroid above half height or the cross-correlation. |
| Convert global to local coordinates | x, y in a frame with a new origin and a rotated x axis. |
| Popular constants | A sheet of CODATA constants with units and uncertainties. |
| Curvature radius | Curvature κ = \|y″\| / (1 + y′²)^3/2 and its radius along the curve. |
| Tangent | The tangent, and on request the normal, at an x, drawn on the graph. |
| Tafel extrapolation | Select a polarisation curve: x is the potential in V and y is the current. Straight lines through log\|i\| in an anodic and a cathodic window give Ecorr, icorr, βa and βc. |
| Distance between two points | Distance, dx, dy, angle and slope, with the segment drawn on the panel. |
| Level crossing | The x values where the curve crosses a level: rising, falling or both. Hysteresis ignores noise around the level. |

![Nyquist plot with Bode panels]({{ROOT}}assets/img/nyquist.webp){: width="1600" height="1000" loading="lazy" }

## Signal and statistics

| App | What it does |
|---|---|
| White noise | A sheet of Gaussian or uniform white noise, with a seed so the result can be repeated. |
| NetCDF data analysis | Choose a variable of a NetCDF or HDF5 file and the one or two dimensions to keep. The others are reduced by mean, sum, minimum, maximum, standard deviation or median. The result is a curve or a map. |
| Mann–Kendall test | Trend test with the tie correction, Kendall's τ and Sen's slope. |
| Asymmetric correlation matrix | Correlation (Pearson, Spearman or Kendall) of every column of group A with every column of group B, with p-values and a heat map. |
| Logistic regression | Binary logistic regression. The dependent column holds 0 and 1. You get coefficients, standard errors, Wald tests, odds ratios with 95 % limits, deviance, AIC, the likelihood-ratio test, McFadden's R², fitted probabilities and the confusion counts. |
| Hurst exponent | Rescaled-range (R/S) analysis with the log–log graph. |
| Hysteresis | For the selected loop: area, coercive fields, remanence, saturation and squareness. |

## Data processing (Sheet → Apps)

| App | What it does |
|---|---|
| Text to columns | Splits a text column by a delimiter into new columns. Numeric parts become numbers. |
| Data slicer | Keeps the rows inside a numeric range or among chosen texts, either as a new sheet or by hiding the other rows. |
| Extract XY data from graph | The x, y of every curve of the panel that lie inside its current axis limits. |
| Periodic report | Re-reads a data file at an interval. Each time the file has changed, a row with the time, the number of rows and the last, mean, minimum and maximum of each column is added to a report sheet. Run the command again to stop. |
| Project manager | Lists the projects of a folder and its subfolders, with their sheets, graphs, notes and dates. |
| Project searcher | Finds the projects whose sheet names, column names, graph names, titles, axis labels or notes contain a text. |

## Graph tools (Graph → Apps)

| App | What it does |
|---|---|
| Graph maker | Click the columns in the order you want and choose any graph type, basic or Origin. |
| Batch plotting | Repeats the active graph for other sheets with the same column names, one new graph per sheet. |
| Common bar width | Gives every bar series of the graph, or of the active panel, the same width. |
| Layer stack manager | Reorders, hides and shows the panels of the graph. Insets stay with their parents. |
| Color editor | Makes your own colour maps from a list of colours (smooth or in flat bands). They are kept between sessions and appear, with their reversed “_r” forms, in every colour-map list. |
| LaTeX equation | Typesets LaTeX math, such as `\frac{a}{b}` or `\int_0^\infty e^{-x^2}dx`, on the panel. |
| Toolbar maker | Builds your own toolbar from any commands. It is kept between sessions. |

![Taylor diagram]({{ROOT}}assets/img/taylor.webp){: width="1600" height="1000" loading="lazy" }

![USDA soil texture triangle]({{ROOT}}assets/img/soil-texture.webp){: width="1600" height="1000" loading="lazy" }

![Isosurface]({{ROOT}}assets/img/isosurface.webp){: width="1600" height="1000" loading="lazy" }
