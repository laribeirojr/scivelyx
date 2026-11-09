# Matrices and surfaces

A **matrix** is a grid of values z(x, y) with coordinates for its rows and columns — a map, an image, a 2D
spectrum or a potential-energy surface. Matrices live in the project next to the sheets and have their own
**Matrix** tab and menu.

## Creating a matrix

- **Matrix → New matrix**: dimensions and the first and last x and y.
- **Matrix → Set values**: a formula of `i`, `j`, `x`, `y`, the cell value and other matrices, e.g.
  `exp(-(x^2 + y^2))` or `M1 - M2`.
- **Matrix → Import image**: an image becomes a matrix of intensities.
- **Sheet → Convert to matrix**: x, y, z columns on a regular grid become a matrix; **Matrix → XYZ** goes back.
- **Matrix → 2D binning**: counts two columns into a 2D histogram matrix.

## Operations

Dimensions and coordinates, transpose, invert, determinant, rotate ±90°, mirror horizontally and vertically, expand
(bilinear) and shrink (block mean), smooth, 2D FFT, a **line profile** along a line you choose, **Show as image**
with a palette (grey, rainbow, custom) and **Export image**. Outputs are recalculated when the matrix changes.
**Convert to table** writes the matrix as a table, as XYZ or as YXZ.

## Scattered points → surface

**Sheet → Surface from XYZ** turns scattered x, y, z measurements into a surface, either by interpolation onto a grid
(linear, cubic, nearest, thin-plate spline) or by fitting z = f(x, y) (plane, quadratic, 2D Gaussian or your own
formula, with standard errors and R²). It draws a contour, a map or a 3D surface with the measured points on top.

## Graphs of matrices

Contour (lines or filled), heat map (also with the values in the cells), 3D surface, mesh and the other 3D styles,
contours projected on the floor and walls of a 3D box, and polar contours. SciDAVis and QtiPlot matrices open as
matrices and are written back as matrices.
