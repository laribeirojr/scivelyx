# Fitting and analysis

Select a curve (click it on the graph) and choose an operation in the **Analysis** tab or menu. Results go to the
same panel, the right y axis, a new panel below or a new graph, and they are stored as sheets with their recipe.

## Curve fitting

**Analysis → Curve fitting** (Ctrl+Shift+F).

| Option | Choices |
|---|---|
| Model | Linear, slope (y = a·x), polynomials of degree 2–9, Gaussian (also by area), Lorentzian, Voigt, exponential decay (1st, 2nd and 3rd order) and growth, logistic, Boltzmann, power, logarithmic, Arrhenius, exponential saturation, ExpLin, rationals, Planck, 2–6 Gaussian or Lorentzian peaks, your own formula (`A*exp(-x/t) + c`) or a function saved in the **library**. |
| Parameters | Initial value, **lower and upper bounds**, fixed or free; *Estimate initial values* fills them from the data. |
| Range | Only part of the x axis (also from the range selector on the graph). |
| Weighting | None, instrumental (1/σ² from an error column), statistical (1/y), arbitrary dataset, direct weights. |
| Algorithm | Levenberg–Marquardt (trust region when there are bounds) or Simplex (Nelder–Mead); iterations and tolerance. |
| Output | Fitted curve (with N points or at the x of the data), box with the parameters and R², residuals panel, **confidence and prediction bands** at the level you choose, errors scaled with √(χ²/dof), significant digits, **covariance matrix**, report written to the notes. |

The report gives each parameter with its standard error, R², adjusted R², reduced χ² and RMSE. Everything the
fit created — curve, bands, parameter table, box — is **recalculated in a chain** when the data change.

**Analysis → Global fit** fits one model to several curves at once and lets you choose which parameters are shared
(the same width in every spectrum, for example).

## Peaks

**Analysis → Peak Analyzer** (Ctrl+Shift+K) goes through four steps: baseline (asymmetric least squares or a
polynomial through the ends), detection (prominence, maximum number, or positions typed by hand), the fit of
Gauss, Lorentz, Voigt or pseudo-Voigt peaks, and a table with center, height, FWHM, area and area % — all with
uncertainties. **Find peaks** is the quick version (positions and FWHM).

![The Peak Analyzer]({{ROOT}}assets/img/peak-analyzer.webp){: width="1240" height="760" loading="lazy" }

## Signal

Smoothing (Savitzky–Golay, adjacent averaging, FFT low-pass, LOWESS), baseline, FFT (amplitude, power, phase; Hann,
Hamming, Blackman windows), interpolation (spline, Akima, PCHIP, linear), Butterworth low-, high-, band-pass and
band-stop filters and the median filter, correlation and autocorrelation, convolution and deconvolution
(Richardson–Lucy, Wiener), Hilbert envelope, derivative, integral (net and absolute area), integrate a function from
a to b, normalize, translate a curve, subtract a line or a reference curve.

## Statistics

- **Statistics** of columns (N, mean, standard deviation and error, quartiles, median, skewness, kurtosis) and of
  rows; **Curve statistics**.
- **Distribution fit**: normal, lognormal, Weibull, gamma, exponential, logistic and Cauchy, ranked by AIC and BIC
  with the Kolmogorov–Smirnov test, drawn over the histogram.
- **Hypothesis tests**: t (one sample, two samples, paired), ANOVA, Shapiro–Wilk, Kolmogorov–Smirnov, Mann–Whitney,
  Wilcoxon, Kruskal–Wallis, Levene, chi-square for independence and for the variance — with the decision at your
  level α. **Two-way ANOVA** with interaction.

## Recalculation and batches

**Analysis → Automatic recalculation** is on by default. Turn it off to work on large data, and press
**Recalculate now** (Ctrl+F5) when you want the results updated; out-of-date results are marked.

**Analysis → Batch processing** runs the same fit, Peak Analyzer, statistics, integral or extremes over a folder of
files or a list of datasets and collects a summary table — with the number in each file name (a temperature, for
example) as the x axis — and its graph.
