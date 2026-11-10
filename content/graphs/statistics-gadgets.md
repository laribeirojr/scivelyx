# Regression, statistics and gadgets

Version 0.18 added the analysis tools of Origin (standard edition) that were still missing. They are in the
**Analysis** menu, in the submenus *Fitting (more)*, *Peaks (more)*, *Statistics (more)*, *Signal and mathematics
(more)* and *Gadgets*. Tools that work on columns read the columns you select in the sheet (Ctrl+click the
headers). Tools that work on a curve use the curve you clicked on the graph. Results go to new sheets, to the
Messages dock and, where it helps, to a graph.

## Fitting

**Multiple linear regression.** Select the dependent column and the predictors, then choose which column is the
dependent one. The report and the sheets give:

- each coefficient with its standard error, t, p, confidence limits and variance inflation factor (VIF);
- the ANOVA table, R², adjusted R² and RMSE;
- the fitted values and the residuals.

The graph shows the residuals against the fitted values and one *partial leverage* (added-variable) plot per
predictor. The slope of each partial leverage plot is that predictor's coefficient.

![Multiple regression with partial leverage plots]({{AROOT}}assets/img/mlr.webp){: width="1600" height="1000" loading="lazy" }

**Confidence ellipse.** Select two columns. The ellipse holds a new observation (*population*) or the mean with the
probability you choose. The graph also shows the data and the straight-line fit.

In the **Fit Wizard**:

- **× N** repeats the model N times with a shared offset y0, for example three Gaussian peaks of the same shape.
  The parameters become `xc_1`, `xc_2`, …
- **Derived** takes expressions of the fitted parameters, such as `FWHM = 2*sqrt(2*ln(2))*w; area = A*w*sqrt(2*pi)`.
  Their errors come from the covariance matrix (delta method). They are recalculated with the fit when the data
  change.

## Peaks

- **Integrate peaks** finds the peaks of the selected curve and integrates each one between its boundaries, without
  fitting. It reports the area, centre, centroid, height, FWHM and area %. The baseline can be none, a straight line
  between the ends, or automatic.
- **Batch peak analysis** runs the same analysis, integration or a Gaussian fit, on every curve of the graph and
  writes one summary sheet.

## Statistics

| Tool | What it gives |
|---|---|
| Normality tests | Shapiro–Wilk, Kolmogorov–Smirnov, Lilliefors, Anderson–Darling, D'Agostino K² and Chen–Shapiro, with the decision at your level |
| Probability plot | The ordered data on the probability scale of a normal, log-normal, Weibull, exponential, logistic or Gumbel distribution, with the fitted line and a confidence band |
| 2D frequency count | Counts in a grid of x and y bins, as a matrix and a colour map |
| Discrete frequency | How often each distinct value or text occurs, with percent and cumulative values |
| QC chart (X-bar R) | Means and ranges of subgroups (consecutive values, or labels in a first selected column) with centre lines and control limits |
| Outlier tests | Grubbs (once or repeated) and Dixon's Q; optionally masks the outlying rows |
| Means comparison | After a one-way ANOVA (one column per group): Tukey, Bonferroni, Šidák, Fisher LSD, Scheffé, Holm–Bonferroni, Holm–Šidák or Dunnett against a control |

The Lilliefors, Chen–Shapiro and Dixon p-values come from simulated normal samples with a fixed seed, so they are
the same every time.

![A Weibull probability plot]({{AROOT}}assets/img/probability-plot.webp){: width="1600" height="1000" loading="lazy" }

![An X-bar R chart]({{AROOT}}assets/img/qc-chart.webp){: width="1600" height="1000" loading="lazy" }

## Signal and mathematics

- **Percentile filter:** each point is replaced by a percentile of its neighbours (50 = median).
- **FFT filter: parabolic or threshold:** a low pass whose gain falls as 1 − (f/f<sub>c</sub>)², or the removal of
  every Fourier component weaker than an amplitude.
- **Average multiple curves:** the curves of the active panel on a common x, with mean, standard deviation, standard
  error and count.
- **Trace interpolation:** points evenly spaced along the curve in the order of the data. **On XYZ**, z is read along
  a path that you give over scattered x, y, z data.
- **3D interpolation:** scattered x, y, z and a value become a regular grid. Each z level becomes a matrix.
- **Polygon area:** the area, centroid and perimeter of a closed curve.
- **Intersections:** where the curves of the panel cross each other, or a horizontal or vertical line.

## Gadgets

**Vertical cursor (all graphs):** click or drag on a graph. The status bar shows the value of every curve of every
graph at that x.

The other gadgets work on the selected curve, inside the **range selector** (Analysis → Gadgets → Range selector,
then drag along x):

- quick fit (straight line) and quick sigmoidal fit;
- peaks, differentiate, interpolate and integrate;
- FFT and statistics.

The result appears in a box on the graph, and a curve or a second graph is added when there is one. Move the range
and the gadget is computed again. **Stop the gadget** ends it.

![The sigmoidal fit gadget]({{AROOT}}assets/img/gadget.webp){: width="1600" height="1000" loading="lazy" }
