# Sheets and data

## Importing

| Source | How |
|---|---|
| CSV, TSV, text in columns | **File → Open data** (Ctrl+O); `#` comments at the top are kept, Fortran `D` exponents are read |
| Unusual text files | **File → Import wizard** (Ctrl+Shift+I): separator, decimal comma, lines to skip, names and comment lines, with a live preview |
| Excel, LibreOffice (.ods), NumPy, JSON, Parquet | **File → Open data** |
| GROMACS `.xvg`, LAMMPS log | **File → Open data** |
| Diffractometers and spectrometers (XRDML, RAS, UXD, JCAMP-DX, SPC) | **File → Open data** — see [Spectroscopy and diffraction](../spectroscopy/) |
| Sound (.wav) | **File → Open data**: one column per channel |
| SQLite database | **File → SQLite database…**: a table or a `SELECT` query (read-only) |
| HDF5, NetCDF, MATLAB (.mat) | **File → HDF5, NetCDF or MATLAB file…** (or open/drop the file): variables as columns or as a matrix — see [Multivariate, wavelets and the digitizer](../origin-tools/) |
| A picture of a graph | **Analysis → Digitizer…** reads the points back |
| Several files into one table | **File → Several files into one table…**: side by side or stacked, with the file name as a column |
| GitHub | **File → GitHub** (Ctrl+G): a repository, folder or file URL; private repositories with a `GITHUB_TOKEN` |
| A matrix (grid of numbers) | **File → Matrix** or **Sheet → Matrix** |

Date columns become a date axis automatically.

## Columns

- **Designation**: X, Y, Z, X error, Y error, Label or none (right click on the header). Graphs follow them.
- **Long name and units**: they become the axis titles.
- **Type**: number, text or date/time; **numeric format**: decimal, scientific or engineering (10k), with decimal
  places; **read-only**; **hidden**. All are kept in the project.
- Move, swap, add, fill (row numbers, uniform or normal random values) and sort columns — also by several keys.

## Formulas — Set values

**Sheet → Set values** (Ctrl+Q) computes a column from a formula, with a preview:

```text
A^2 + i                       # i is the row number (1-based)
col("E (eV)") * 1000          # another column by its name
hc_eVnm / A                   # physical constants: kB, kB_eV, h, hbar, h_eV, c0, qe, NA, me, eps0, R, Ha_eV, Ry_eV, …
x > 0 ? x : 0                 # SciDAVis and QtiPlot (muParser) syntax works: ?:, &&, ||, if(c, a, b)
```

Special functions (erf, gamma, Bessel, Voigt…) and the muParser functions of SciDAVis and QtiPlot (avg, min/max/sum
with several arguments, rint, w0, wm1, chi2cdf, invt, rnd…) are available. The evaluator is safe: a formula cannot
run arbitrary code. Formula columns **recalculate by themselves** when the columns they use change; typing into a
formula column turns it into ordinary data.

In formulas the decimal separator is always the point (`2.303`), as in every programming language, even when
your files use a comma.

## Masks and undo

**Sheet → Mask rows** strikes rows through in red: they stay out of graphs, fits, tests and statistics but remain in
the file. **Unmask** brings them back. With the sheet in focus, **Ctrl+Z** undoes data edits.

## Reorganizing

The **Sheet** menu also has: transpose; stack and unstack columns; filter rows by a condition
(`T > 300 and k < 50`); join sheets (by a key or side by side); pivot table; row statistics; frequency count;
stem-and-leaf; convert to a matrix and back. Each operation creates a new sheet, so the original stays intact.

**Sheet → Export sheet** writes Excel (with long names and units), LibreOffice, CSV or TSV.
