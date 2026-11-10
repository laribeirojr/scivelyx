# Spectroscopy and diffraction

Version 1.0.0rc5 added tools for Raman, infrared and UV-Vis spectra and for X-ray diffractograms. They are in
**Analysis → Spectroscopy and diffraction**, next to the Peak Analyzer (**Analysis → Peak Analyzer**), which they
use. Tools that work on a curve use the curve you clicked on the graph; tools that work on columns use the
columns you select in the sheet.

## Instrument files

**File → Open data** reads these files directly, like any table:

| File | Instruments |
|---|---|
| `.xrdml` | Malvern Panalytical diffractometers (Empyrean, X'Pert, Aeris) |
| `.ras` | Rigaku diffractometers (SmartLab, MiniFlex, Ultima) |
| `.uxd` | Bruker DIFFRACplus text export |
| `.jdx`, `.dx`, `.jcamp` | JCAMP-DX spectra (IR, Raman, UV-Vis, 1D NMR), including the compressed forms |
| `.spc` | Galactic/Thermo GRAMS SPC (new format; several spectra with one x become several columns) |

The wavelength, anode, laser line or sample name stored in the file is kept with the sheet. The X-ray tools then
start with that wavelength.

## Peaks with different shapes

In the Peak Analyzer, step 3 has two new fields.

- **Shapes per peak:** one shape key per peak, separated by `;`. For example, `lorentz; bwf` is a Lorentzian D
  band and a Breit–Wigner–Fano G band. The last shape repeats for the remaining peaks; left empty, the shape
  chosen above is used for all of them. The keys are:
  - `gauss`, `lorentz`, `voigt` and `pvoigt` (pseudo-Voigt);
  - `bwf` (Breit–Wigner–Fano);
  - `pearson7` (Pearson VII);
  - `bigauss` (asymmetric Gaussian, with its own width on each side).
- **Baseline fitted with peaks:** none, constant, linear or quadratic. It is fitted at the same time as the
  peaks, on top of the baseline subtracted in step 1. Choose *none* in step 1 to fit only this polynomial.

The table shows the shape of each peak and its shape parameter: η for the pseudo-Voigt, m for Pearson VII, q
for BWF, and the left and right widths of a bi-Gaussian. A BWF tail never reaches zero, so its area is
integrated over the fitted range, and its center is the position of the maximum.

![Peak Analyzer with a shape per peak and a linear baseline fitted with the peaks]({{AROOT}}assets/manual/peak-analyzer.png)

## X-ray diffraction

| Tool | What it does |
|---|---|
| X-ray diffraction analysis | Finds and fits the peaks of the selected diffractogram (x = 2θ in degrees). The new sheet has d, q and the Scherrer size of each peak. The instrumental width (from a standard such as LaB₆ or Si) is removed quadratically (Gaussian peaks), linearly (Lorentzian) or geometrically (Voigt). It also draws a Williamson–Hall graph with size and microstrain, and reports the cubic lattice (sc, bcc, fcc or diamond) and lattice constant that index the peaks best. |
| Strip Kα2 | Removes the Kα2 doublet (Rachinger correction) and adds the Kα1-only curve to the graph. |
| Convert 2θ, d and q | Adds columns d (Å) and q (Å⁻¹) to the sheet, and optionally 2θ for another X-ray line. |
| Cubic reflections | The hkl, multiplicity, d and 2θ of a cubic lattice, drawn as vertical lines on the active panel. |
| Match reference peaks | Pairs observed 2θ values with a reference sheet that has a `d` or `two_theta` column (and optionally `hkl` and `intensity`). |

Wavelengths are built in for the Kα1, Kα2, Kα and Kβ lines of Cu, Mo, Co, Cr, Fe and Ag. You can also type any
value in ångström.

Step-by-step examples: [Worked examples](../tutorials/), sections 1, 2 and 4.

## Raman

| Tool | What it does |
|---|---|
| Remove spikes (cosmic rays) | Finds narrow spikes from the jumps between neighbouring points and replaces them by interpolation. Raman bands rise smoothly, so they are kept. |
| Wavelength ↔ Raman shift | Converts an absolute wavelength column (nm) into the Raman shift (cm⁻¹) for a laser line, or the reverse. |
| Carbon D and G bands | Fits the D band (Lorentzian) and the G band (BWF) with a linear baseline. It reports I_D/I_G (heights), A_D/A_G (areas), the crystallite size L_a = 2.4×10⁻¹⁰ λ⁴ (A_D/A_G)⁻¹ (Cançado et al. 2006) and the defect distance L_D (Cançado et al. 2011, low-defect regime). Optionally it adds the D″ (≈1500 cm⁻¹) and D′ (≈1620 cm⁻¹) bands. |

## Fitting implicit functions

**Fit implicit function** fits a curve f(x, y) = 0 to the selected points. It minimises the distance of each
point to the curve (orthogonal distance regression), not a vertical distance. The presets are:

- a circle;
- an ellipse (centre, semi-axes and angle, with eccentricity and area);
- a general conic;
- a straight line with errors in both x and y.

You can also type your own function, such as `x^2/a^2 + y^2/b^2 = 1`, with initial values `a = 1, b = 1`. The
fitted curve goes on the graph; the parameters and their errors go to a new sheet.
