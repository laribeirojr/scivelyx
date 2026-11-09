# Multivariate, wavelets and the digitizer

These tools came with version 0.16. Each one reads the columns you select in the active sheet (Ctrl+click the column
headers), opens a short dialog and writes its results as **new sheets** (or matrices) plus a **graph**. A report goes
to the Messages dock and opens in a window you can copy from.

## Array files: HDF5, NetCDF and MATLAB

**File → HDF5, NetCDF or MATLAB file…**, or open or drop a `.h5`, `.hdf5`, `.nc` or `.mat` file onto the window.

The dialog lists every numeric variable with its size, type, units and long name. Groups appear as `group/name`.

- **As a sheet:** one-dimensional variables of the same length become columns. Their units and long names become the
  column's units and long name, so the axis labels come out right. The sheet remembers the file and the variables, so
  the project reloads them.
- **As a matrix:** one two-dimensional variable becomes a matrix. The coordinate variables of its dimensions supply
  x and y: NetCDF coordinate variables or HDF5 dimension scales. For variables with more dimensions, the first slice
  is taken.

NetCDF files in the classic format and in NetCDF-4 are both read, and so are MATLAB files from version 4 to 7.3,
fields of structs included. Fill values, scale factors and offsets are applied.

## Principal components (PCA)

**Analysis → Multivariate → Principal components.** Select two or more numeric columns.

| Option | Choices |
|---|---|
| Matrix | **correlation**: each variable standardized, as Origin does by default; or **covariance**, in the original units |
| Components to keep | 1 up to the number of variables |

The results are three sheets:

- **scores:** one row per observation;
- **loadings:** the eigenvectors;
- **eigenvalues:** with the percentage and the cumulative percentage of variance.

The graph shows the **scree plot** and the **biplot**: scores as points, loadings as arrows labelled with the
variable names. The report also gives the Kaiser criterion, the number of eigenvalues above 1. Rows with a missing
value are left out.

![PCA: scree plot and biplot]({{ROOT}}assets/img/pca.webp){: width="1600" height="1000" loading="lazy" }

## Cluster analysis

**Analysis → Multivariate → Cluster analysis.**

- **k-means:** k-means++ starts; the best of ten runs is kept.
- **Hierarchical:** Ward, average, complete, single, centroid or median linkage. The tree is cut into the number of
  clusters you ask for.

Clusters are numbered by size. The new sheet holds the chosen columns, the cluster of each row and, for k-means, the
distance to the centre. A second sheet holds the centres. The graph colours the points by cluster and, for the
hierarchical method, draws the **dendrogram**. The report gives the mean silhouette width, from −1 to 1, where
higher means better separated clusters, and for trees the cophenetic correlation.

![Hierarchical clustering with the dendrogram]({{ROOT}}assets/img/clusters.webp){: width="1600" height="1000" loading="lazy" }

## ROC curve

**Analysis → Multivariate → ROC curve.**

- Choose the score column (the result of a test or a classifier) and the column with the true class. The class
  column must have exactly two values, numbers or text.
- Choose which class is positive and whether a higher score means positive.

The sheet lists every threshold with the false-positive rate, the sensitivity, the specificity and Youden's J. The
report gives:

- the **AUC** with its standard error (Hanley–McNeil) and 95 % interval;
- the p-value against AUC = 0.5;
- the best threshold.

## Kernel density

**Analysis → Multivariate → Kernel density.**

- **One column:** a smooth estimate of its distribution with a Gaussian kernel. The kernel width comes from
  Scott's or Silverman's rule, or you fix it. The curve is drawn over the histogram, and the sheet also holds the
  cumulative distribution.
- **Two columns:** the 2-D density as a matrix and a colour map, with the points on top.

## Spectrogram

**Analysis → Time–frequency and wavelets → Spectrogram.** Select x and the signal, or only the signal. The x values
must be evenly spaced.

The settings are the window (Hann, Hamming, Blackman, rectangular, flat top, Bartlett), its length in points and the
overlap. The result is a matrix of power density (in dB, as power or as amplitude) against x and frequency, drawn as
a colour map. When x is in seconds, the frequency is in hertz.

## Wavelets

**Continuous wavelet transform:**

- **Wavelets:** Morlet, Mexican hat or Paul.
- **Frequency range:** logarithmically spaced, with a default range.
- **Values:** power, **rectified power** (comparable across frequencies), amplitude or real part.

The scalogram is drawn on a logarithmic frequency axis. The dashed **cone of influence** marks where the edges of
the record distort it.

![Continuous wavelet transform of a chirp]({{ROOT}}assets/img/wavelet.webp){: width="1600" height="1000" loading="lazy" }

**Wavelet decomposition** splits the signal into an approximation and the details at each level. This is the
multiresolution analysis, with Haar, Daubechies, Symlets, Coiflets or biorthogonal wavelets. The parts add up to the
signal again, and each one gets its own stacked panel.

**Wavelet denoise / smooth:**

- **Denoise:** shrinks the detail coefficients with the universal threshold σ√(2 ln n), soft or hard, where the noise
  σ comes from the finest details. You can also type your own threshold.
- **Smooth:** keeps only the approximation at a chosen level.

## Fitting with errors in x and y (ODR)

In the **Fit Wizard**, choose the algorithm **Orthogonal distance (ODR, errors in x and y)**. It minimises the
distances from the points to the curve, weighted by both error bars:

- the **x error bars** of the curve;
- the y errors from the *Weighting* option.

Without x error bars, x and y count equally. Bounds, fixed parameters, bands and chained recalculation work as with
the other algorithms. The results match ODRPACK, the library behind Origin's and SciPy's ODR. In scripts:
`fit("data", "T", "rho", "expdec", method="odr", sigma="drho", sigma_x="dT")`.

## Digitizer

**Analysis → Digitizer…** (also in the File menu) opens a picture of a graph: a scan, a figure from a paper, a
screenshot.

1. **Axes.** Choose X1 and click a labelled tick on the x axis, then type its value. Do the same for X2 and for Y1
   and Y2 on the y axis. Tick *logarithmic* for log axes. Slightly rotated scans are handled.
2. **Points.**
    - *Pick points* adds a point per click.
    - *Pick the curve colour* followed by **Trace line** follows a line through the whole picture.
    - **Find symbols** finds markers of that colour.
    - *Region (drag)* limits the search and keeps the legend out.
    - The tolerance, the step and the largest spread tune the tracing.
3. **Sheet.** **Next curve** keeps the points and starts another curve. **Create sheets** makes one sheet per curve
   and a graph with all of them.

![The digitizer tracing a curve]({{ROOT}}assets/img/digitizer.webp){: width="1200" height="760" loading="lazy" }

## In scripts

`pca("data", ["a", "b", "c"])`, `kde("data", "a")`, `roc("data", "score", "class")`,
`cluster("data", ["a", "b"], 3, method="ward")`, `spectrogram("signal", "t", "y")` and
`cwt("signal", "t", "y", wavelet="morlet")` return the same results as dictionaries of arrays and tables.
