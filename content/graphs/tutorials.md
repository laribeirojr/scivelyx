# Worked examples

Each example goes from the data to the result, step by step, with the windows you will see. The data are either in
the program (the **Start from an example** gallery) or easy to make yourself. Values in the pictures come from
those data; yours will differ.

## 1. Crystallite size from an X-ray diffractogram

**Goal:** the d-spacings, the Scherrer size of each peak, the Williamson–Hall size and strain, and the lattice
constant of a cubic powder.

1. Open the diffractogram: **File → Open data** reads `.xrdml` (Panalytical), `.ras` (Rigaku), `.uxd` (Bruker) and
   plain two-column files. The wavelength stored in an instrument file is kept with the sheet.
2. Plot 2θ against the intensity (select both columns, **Graphs → Line**).
3. Click the curve, then **Analysis → Spectroscopy and diffraction**:

   ![The Spectroscopy and diffraction menu]({{AROOT}}assets/manual/menu-spectroscopy.png)

4. Choose **X-ray diffraction analysis…**. In the dialog:
   - **Wavelength**: pick the line (Cu Kα1 = 1.540562 Å for most laboratory instruments) or type a value in Å;
   - **Scherrer constant K**: 0.9 for spherical crystallites;
   - **Instrumental FWHM**: the width of a standard (LaB₆, Si) measured with the same set-up, in degrees of 2θ;
     leave 0 if you do not have one;
   - **Instrumental correction**: quadratic for Gaussian peaks, linear for Lorentzian, geometric for Voigt;
   - **Peak shape** of the fit (pseudo-Voigt is the usual choice), and **strip Kα2 first** if the doublet is
     visible at high angles.
5. **OK** finds and fits the peaks. The report lists, for each peak, 2θ, d, the FWHM and the size, then the
   Williamson–Hall result and the best cubic indexing:

   ![Report of the X-ray diffraction analysis of a silicon powder]({{AROOT}}assets/manual/xrd-report.png)

6. Two sheets and one graph are added: `<data>_xrd` (the peak table with d, q and size), `<data>_williamson_hall`
   and the Williamson–Hall plot, β cos θ against 4 sin θ. Its intercept gives the size and its slope the strain:

   ![Williamson–Hall plot made by the analysis]({{AROOT}}assets/manual/xrd-williamson-hall.png)

**Check the result.** The Scherrer equation is reliable below about 100 nm. Above that, the instrumental width
dominates. A negative or scattered Williamson–Hall slope usually means that the strain is below what the data can
resolve. In the silicon example the indexing finds the diamond lattice with a = 5.4309 Å.

**Related tools in the same menu:**

- **Strip Kα2** removes the doublet from the whole pattern.
- **Convert 2θ, d and q** adds the columns d and q, or 2θ for another X-ray tube.
- **Cubic reflections** draws the hkl lines of a lattice on the graph.
- **Match reference peaks** pairs your peaks with a reference card typed in a sheet.

The example *Stacked XRD after milling* in the gallery shows a set of patterns offset vertically. *Power-law fit with
a log–log inset* plots the crystallite size against the milling time, with the values of the paper's Table 1.

## 2. D and G bands of a carbon Raman spectrum

**Goal:** I_D/I_G, A_D/A_G and the crystallite size L_a of a disordered carbon.

1. Open the spectrum (Raman shift in cm⁻¹ against intensity). JCAMP-DX (`.jdx`) and Galactic SPC (`.spc`) files open
   directly.
2. If the spectrum has cosmic-ray spikes, click the curve and run **Spectroscopy and diffraction → Remove spikes**.
   It adds a clean copy of the curve, and the `spike` column marks the points that were replaced.
3. **Carbon D and G bands…** asks for the laser wavelength and fits a Lorentzian D band and a Breit–Wigner–Fano G band
   on a linear baseline. Tick **also D″ and D′** for amorphous carbons.
4. The fit and the bands are drawn on the graph:

   ![D and G bands fitted on the spectrum]({{AROOT}}assets/manual/raman-carbon.png)

5. The report gives the band positions, the ratios with their errors, L_a = 2.4×10⁻¹⁰ λ⁴ (A_D/A_G)⁻¹ (Cançado et
   al. 2006) and the defect distance L_D (Cançado et al. 2011):

   ![Report of the carbon analysis]({{AROOT}}assets/manual/raman-report.png)

**The same fit by hand.** **Analysis → Peak Analyzer** fits any combination of peaks. Each peak can have its own
shape, and the baseline can be fitted with the peaks:

![Peak Analyzer with a Lorentzian D band, a BWF G band and a linear baseline fitted together]({{AROOT}}assets/manual/peak-analyzer.png)

- **Positions**: `1350; 1590` (or leave empty and let it find the peaks; *Minimum prominence* controls how many).
- **Shapes per peak**: `lorentz; bwf`. The keys are gauss, lorentz, voigt, pvoigt, bwf, pearson7 and bigauss.
- **Baseline fitted with peaks**: linear. Step 1 can still subtract an ALS or polynomial baseline first.
- **Analyze**, look at the residuals, then **Apply to graph**. The peak table goes to a new sheet. Its columns
  are centre, height, FWHM, area and area %, each with its error, plus the shape parameter (q for BWF).

## 3. Optical band gap from a Tauc plot

**Goal:** E_g of a semiconductor by linear extrapolation of (αhν)² against hν.

1. Compute the Tauc variable in the sheet. Add a column with a formula, for example
   `(2.303 * A * hv)^2` for a direct allowed transition, where `A` is the absorbance and `hv` the photon energy in
   eV (`hv = 1239.84 / wavelength_nm`). In formulas the decimal separator is the point.
2. Plot (αhν)² against hν. The gallery example *Tauc plot* has such a curve.
3. Click the curve and open **Analysis → Curve fitting**. Choose the **Linear** model and set the **x range** to the
   straight part above the absorption edge (2.6 to 3.0 eV in the example).

   ![Curve fitting dialog with the linear model]({{AROOT}}assets/manual/fit-dialog.png)

4. **Fit**, then **Apply to graph**. E_g is where the line crosses zero, E_g = −a/b for y = a + b·x. Type it in
   **Derived** (`Eg = -a/b`) and the fit report shows it with its error.

![The finished figure: data, the fitted line and E_g marked]({{AROOT}}assets/manual/fig-tauc.png)

## 4. Ellipse through scattered points (implicit fit)

**Goal:** the centre, semi-axes and orientation of an ellipse, or of any curve given as f(x, y) = 0.

1. Plot the points as a scatter.
2. Click them and choose **Spectroscopy and diffraction → Fit implicit function…**.
3. Choose **Ellipse** (or circle, conic, straight line with errors in x and y, or type your own function, such as
   `x^2/a^2 + y^2/b^2 = 1` with initial values `a = 1, b = 1`).
4. The fitted curve is drawn and the parameters with their errors go to a new sheet. The fit minimises the
   distance of each point to the curve, not the vertical distance, so the result does not depend on which variable
   is called y.

![Ellipse fitted to 90 points]({{AROOT}}assets/manual/implicit-fit.png)

## 5. A file with a decimal comma

**Goal:** read data written by software set to Portuguese, German or French, with `;` between the columns and a
comma for the decimals.

1. **File → Import wizard** (Ctrl+Shift+I) and choose the file.
2. The wizard shows the raw text and the table it will make. Set **Separator** to automatic or `;` and **Decimal** to
   `comma (1,5)`. If the file starts with notes, set **Skip first lines** and the **Header line**.
3. **Import** creates the sheet.

![Import wizard reading a CSV file with a decimal comma]({{AROOT}}assets/manual/import-wizard.png)

## 6. Figures modelled on published papers

The gallery examples recreate figure types from 2026 papers. Open one, look at how it is built in **Properties**
(series, axes, insets, reference lines, drawing objects), and replace its data with yours: in the series list,
change **Dataset**, **x** and **y**.

| Example | What it shows how to do |
|------------------------------|------------------------------|
| ![Power law with a log–log inset]({{AROOT}}assets/manual/fig-power-law.png) | An inset with its own logarithmic axes (**Insert → Zoom (inset)**, then set both scales to log), a dashed fitted curve and an equation in the panel. |
| ![Magnetization loops at ten temperatures]({{AROOT}}assets/manual/fig-mh-loops.png) | Two panels sharing a colour per temperature taken from a colour map, zero lines, one legend for both panels. |
| ![Current–voltage curves with a zoom inset]({{AROOT}}assets/manual/fig-iv-inset.png) | Twelve curves with markers every 20 points, a legend with a title in three columns, a zoom inset and a cut-off line. |
| ![XRD deconvolution with Miller indices]({{AROOT}}assets/manual/fig-xrd-deconv.png) | Fitted components in colour, the data in grey and hkl labels taken from a text column. |
| ![TGA and DTG]({{AROOT}}assets/manual/fig-tga.png) | A shaded temperature range (a reference band) and two panels with labels (a), (b). |
| ![Bars with a significance bracket]({{AROOT}}assets/manual/fig-bars.png) | Bars with standard-deviation error bars, values inside the bars, and a bracket with ** drawn with the drawing tools. |
| ![PCA scores with 95 % ellipses]({{AROOT}}assets/manual/fig-pca.png) | Hollow markers per group and filled 95 % confidence ellipses. |
| ![Depth profiles]({{AROOT}}assets/manual/fig-depth.png) | Four panels with depth increasing downwards, the axis titles on top and dotted lines at the soil horizons. |
| ![FORC diagram]({{AROOT}}assets/manual/fig-forc.png) | A filled contour map of a distribution with a colour bar and its units. |

Sources of the figure types: Neciosup-Puican et al., *J. Alloys Compd.* 1080 (2026) 190504; de Almeida et al.,
arXiv:2610.36482 (2026); da Silva et al., *Micro Nanostruct.* 221 (2027) 208963; Endres et al., *Clin. Oral Investig.*
30 (2026) 484; do Vale et al., EarthArXiv preprint (2026).

## 7. Figures for theoreticians: fat bands with the projected DOS, and ELF maps

Two examples of the Start page show how to build the figures of electronic-structure papers. Both are computed from
textbook models in the program, so they are physically sound but **illustrative**, not DFT results.

**Fat bands and projected DOS of silicon.** Bands of the sp3s* tight-binding model of Vogl, Hjalmarson and Dow
(1983) along L–Γ–X–U|K–Γ, with the weight of the s, px, py and pz orbitals as bubbles, and the total, s and p DOS in a
narrow second panel that shares the energy axis.

![Fat bands and projected DOS of silicon]({{AROOT}}assets/manual/fig-fatbands.png)

How it is built (open the example and look in **Properties**):

1. **Two panels side by side** with *width ratios* 3 : 1 and a shared y axis; the DOS panel hides its y tick
   labels.
2. **The bands** are one line per band (columns `band 1` … `band 10`), thin and grey.
3. **The fat bands** are *bubble* series: x = k, y = energy, size = the weight of one orbital, one series and one
   colour per orbital, without edges and half transparent. Bubble max sets the size of a weight of 1.
4. **The k path:** the x axis has explicit ticks at the high-symmetry points with the labels L, Γ, X, U|K, Γ, and
   dotted vertical reference lines there. A dashed horizontal line marks the valence-band maximum (0 eV).
5. **The gap:** a double-headed arrow (**Insert → Arrow (drawing)**) from the valence-band maximum to the conduction-band
   minimum, and a text with E_g.
6. **The DOS panel** plots the DOS on x and the energy on y.

To use your own calculation, put the bands in a sheet (k in the first column, one column per band) and the
projections in another (k, energy and one weight column per orbital). Then change **Dataset**, **x** and **y** of
each series.

**Electron localization function (ELF).** Two maps of the (001) planes of LiF and NaCl, with a shared 0–1 colour
scale. The ELF is computed from closed-shell ions with Slater-type orbitals (the promolecule), which shows the shell
structure of each ion.

![ELF of the (001) planes of LiF and NaCl]({{AROOT}}assets/manual/fig-elf.png)

Each panel is a *filled contour* of a sheet with x, y and ELF columns (50 levels, colour map *jet*, fixed range 0 to
1, colour bar on the right panel only). The axes have no ticks, the aspect is equal, and the ion names are text
labels. A VASP `ELFCAR`, or a plane exported by Quantum ESPRESSO (`pp.x`) or VESTA as x, y, value, plots the same
way.
