# Your first analysis

This example uses a real LAMMPS run that comes with the source of SciVelyx MD (`tests/data`): 27 water molecules
in a periodic box, written as a data file (`water.data`), a dump of 5 frames (`water.lammpstrj`) and the log
(`water.log`). Any LAMMPS run of your own works the same way.

## 1. Open the run

**File ▸ Open**, choose the three files together (or drop them on the window). The dump takes the type labels,
masses and bonds of the data file of the same atoms; the log goes to the **Thermodynamics** tab.

![The water run in the 3D view, with the bonds of the data file and the table of the atoms]({{AROOT}}assets/md/atoms-3d.webp)

- Move through the frames with the slider or the play button.
- Tick **bonds** to draw the O–H bonds of the data file.
- Choose a column in **Colour** (for example `q`, the charge) to colour the atoms by it.
- Type `type == 1` in **Select** to highlight the oxygens.

## 2. Look at the thermodynamics

The **Thermodynamics** tab plots the columns of the log against the step or the time, one curve per run of the
input script; choose the quantities on the left.

![Temperature of the three runs of the log, with the table of the thermodynamic output]({{AROOT}}assets/md/thermo.webp)

## 3. Compute the O–H radial distribution function

**Analysis ▸ Radial distribution function** (Ctrl+R) asks for the two groups of atoms, the cutoff, the number of
bins, the frames and whether bonded pairs count:

![The RDF dialog]({{AROOT}}assets/md/rdf-dialog.webp)

Choose type 1 (O) and type 2 (H), r max = 6 Å, 120 bins, and in *Bonded pairs* **exclude 1-2 and 1-3 pairs**, with
the bonds of the data file — as LAMMPS does with `special_bonds 0 0`. The O–H peak that is left is the hydrogen
bond between molecules. The result opens in a new tab with g(r) and the running
coordination n(r):

![g(r) and n(r) of the O–H pairs, averaged over the five frames]({{AROOT}}assets/md/rdf.webp)

The normalisation is the one of LAMMPS `compute rdf`; the tests of SciVelyx MD compare both on the same frames to
the six digits LAMMPS prints.

## 4. Send it to SciVelyx Graphs

**File ▸ Send to SciVelyx Graphs** (Ctrl+G) saves the result as a project and opens it in SciVelyx Graphs (when it
is installed; otherwise the status bar says where the file is), with the sheet (r, g, n with names and units) and the
two graphs. Everything there is editable: axes, curves, fits, export at the size of the journal.

![The RDF opened in SciVelyx Graphs]({{AROOT}}assets/md/graphs.webp)

**File ▸ Save as SciVelyx project** (Ctrl+S) writes the same thing to a `*.scivelyx.json` file.

## The same from the command line

```bash
scivelyx-md info water.lammpstrj
scivelyx-md thermo water.log -o thermo.scivelyx.json
scivelyx-md rdf water.lammpstrj --topology water.data --pair 1 2 --rmax 6 --bins 120 \
    --exclude-bonded 2 -o rdf.scivelyx.json --csv rdf.csv --png rdf.png
```

And from Python (View ▸ Python console and scripts, or `scivelyx-md shell`):

```python
t = load("water.lammpstrj", topology="water.data")
g = rdf(t, 6, "1", "2", exclude_bonded=2)
print(g.r[g.g.argmax()])      # 1.53 Å: the hydrogen-bond peak (bonded pairs left out)
send(g)                       # to SciVelyx Graphs
```
