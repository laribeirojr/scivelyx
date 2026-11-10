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
- FFT and statistics;
- rise time (10–90 % rise and fall times of the edges in the range);
- cluster (number of points, means, standard deviations and correlation of the points in the range).

The result appears in a box on the graph, and a curve or a second graph is added when there is one. Move the range
and the gadget is computed again. **Stop the gadget** ends it.

![The sigmoidal fit gadget]({{AROOT}}assets/img/gadget.webp){: width="1600" height="1000" loading="lazy" }

## Added in 1.0.0rc7: more statistics, signal processing and mathematics

These are the OriginPro tools most used in physics. They are in the same submenus.

### Statistics (more)

| Tool | Select | You get |
|---|---|---|
| Partial correlation | three or more columns | the correlation of each pair with the other columns held constant (Pearson or Spearman), t and p |
| Cross tabulation tests | two columns of categories, or the columns of a table of counts | χ², likelihood ratio G, Fisher's exact test (2 × 2), φ, Cramér's V and the contingency coefficient; a warning when expected counts are below 5 |
| Two-sample F test for variances | two columns | F = s₁²/s₂², p and the confidence interval of the ratio |
| Proportion tests | nothing (type the counts) | one proportion against p₀ (exact binomial and z, Wilson and exact intervals) or two proportions (z test and Fisher's exact test) |
| Repeated-measures ANOVA, one way | one column per condition, one row per subject | the ANOVA table, partial η², Mauchly's test of sphericity, and the p values corrected by Greenhouse–Geisser and Huynh–Feldt |
| Repeated-measures ANOVA, two way | the a × b columns in the order A1B1, A1B2, …, A2B1, … | each effect with its own error term and Greenhouse–Geisser correction, and the cell means |
| Sign test | one column (against a median) or two (paired) | positive, negative and tied differences, and p |
| Wilcoxon signed-rank, one sample | one column | W and p against a hypothesised median |
| Two-sample Kolmogorov–Smirnov | two columns | D and p: do the samples come from the same distribution? |
| Mood's median test | two or more columns | χ², p and the counts above and not above the grand median |
| Friedman ANOVA | three or more columns (rows are subjects) | χ², p, mean ranks and Kendall's W |
| t tests on rows | the columns of group A, then those of group B | a t test on every row (Welch, paired or one-sample), with the Benjamini–Hochberg q values |
| Power and sample size | nothing | the power curve against n and the n that reaches the target power, for t tests, one-way ANOVA and two proportions |

The power calculations agree with G\*Power: n = 64 per group for a two-sample t test with d = 0.5, α = 0.05 and
power 0.8.

![Power of a two-sample t test against the number per group]({{AROOT}}assets/manual/power-curve.png)

### Fitting (more)

**F test of nested models** fits two models to the selected curve, a simpler one and one with more parameters that
contains it (linear and quadratic, one and two Gaussians). The extra-sum-of-squares F test and the AICc of each
model say whether the extra parameters are worth it. Both fitted curves are drawn.

### Signal and mathematics (more)

- **Power spectral density (Welch):** the averaged periodogram of the selected curve, with segment length and
  window.
- **Coherence:** the magnitude-squared coherence (0 to 1) of two curves of the panel sampled on the same x.
- **Decimate:** keeps one point in n after an anti-aliasing filter.
- **Rise and fall times:** the 0 % and 100 % levels are the two most frequent values of the signal (IEEE 181). Each
  rising and falling edge is timed between the levels you choose (10 % and 90 % by default). Dotted lines mark the
  levels on the graph.
- **Hilbert transform:** the transform, the envelope, the unwrapped phase and the instantaneous frequency.
- **2D correlation (Noda):** select one column per step of a perturbation (temperature, time, pressure), with the
  spectral axis as their x column. You get the synchronous map Φ and the asynchronous map Ψ as matrices and colour
  maps. ν₁ is read on the y axis and ν₂ on the x axis: when Φ(ν₁, ν₂) and Ψ(ν₁, ν₂) have the same sign, the band at ν₁
  changes before the one at ν₂.
- **Continuous wavelet function:** the values of a Morlet, Mexican hat, derivative-of-Gaussian or Paul wavelet at a
  scale and shift, normalised to unit energy.
- **2D FFT filter** (also in the Matrix menu): low-pass, high-pass, band-pass or band-stop filter of the active
  matrix, with an ideal, Gaussian or Butterworth window.
- **2D volume integration and Surface area:** for three columns x, y, z (a regular grid or scattered points, which
  are triangulated) or for the active matrix.
- **Error propagation:** type the function, such as `a*b/c`, and the variables as `a = 2 ± 0.1; b = 3 ± 0.2`. You get
  the first-order uncertainty with the contribution of each variable, and a Monte Carlo check.
- **Convex hull and centroid** (also in the Graph menu): the hull of the selected scatter, its centroid and the lines
  from the centroid to every point.

**Matrix → Eigenvalues and eigenvectors** decomposes the active square matrix.

The digital filter (**Analysis → Filter (IIR / median)**) now offers the Chebyshev I and II, elliptic and Bessel designs
besides Butterworth, with the pass-band ripple and the stop-band attenuation.

![Asynchronous 2D correlation map of a heating series: the band at 1600 cm⁻¹ grows before the one at 1700 cm⁻¹]({{AROOT}}assets/manual/corr2d-async.png)
