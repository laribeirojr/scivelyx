# The window

![The window with a GROMACS run: the Files dock, the Atoms tab with the 3D view and the atom table, the Properties and Pipeline docks]({{AROOT}}assets/md/gromacs.webp)

| Part | What it does |
|---|---|
| **Menus** | File (open, save, export frames, pictures, movies, sessions, Send to SciVelyx Graphs), Analysis (RDF, per-atom properties, materials, ReaxFF, biomolecules, worker threads), Pipeline (add, save and load modifiers, data tables), View (theme, representations, external viewers), Help |
| **Toolbar** | Open, Radial distribution function, Send to SciVelyx Graphs, Save as SciVelyx project, Python |
| **Files** (left) | the open files: trajectories, topologies, logs, energy and ReaxFF files. Click one to show it. A coordinate file (xtc, dcd, nc) uses the open topology of the same atoms |
| **Atoms** tab | the frame controls, the 3D view and the per-atom table of the current frame |
| **Thermodynamics** tab | the columns of a LAMMPS log or an energy file as a graph and a table, one block per run |
| **Result tabs** | one per analysis: a graph (choose it in *Graph*), the table, the toolbar of the graph |
| **Properties** (right) | the frame (file, format, timestep, time, units, atoms, cell, attributes) and the statistics of every column |
| **Pipeline** (right) | the modifiers applied to every frame, with their help below |
| **Status bar** | the last message: the path of the file, the result of an analysis, a warning |

## Opening files

**File ▸ Open** (Ctrl+O) takes several files at once, or drop them on the window. Open the topology together with
its trajectory: a GROMACS `.tpr` with its `.xtc`, a `.psf` with its `.dcd`, a `.prmtop` with its `.nc`, a LAMMPS
data file with its dump. A LAMMPS dump opened with the data file of the same atoms gets its type labels, masses and
bonds. **File ▸ Open recent** lists the last files.

## The frame controls

The slider, the buttons (first, previous, play, next, last) and the frame box move through the trajectory; the
label shows the timestep, the time and the number of atoms. *table: selected atoms only* limits the table to the
selection.

## The 3D view

| Control | Effect |
|---|---|
| Colour | by type, element, residue, segment or any per-atom column (charge, velocity, CNA, strain …) |
| Colour map, range | the map and its limits (`auto` takes the range of the frame) |
| size, style | the size factor and the drawing: `auto` real spheres or fast sprites |
| default / vdw / cpk / licorice / lines / points | the drawing method of every atom (per selection with the *Atom style* modifier) |
| AO | ambient occlusion in the view |
| bonds, cutoff | bonds from the topology, or by distance (`auto`: covalent radii) |
| cell, wrap | the cell edges, and atoms put back into the cell |
| Select | a selection expression, shown as *highlight* or *only* |
| ⟲ x y z | reset the camera, or look along an axis |
| Save image… | a picture of the view at any size |

Drag with the left button to rotate, the wheel to zoom, the right button (or Shift + left) to pan.
**Ctrl + click** on an atom adds it to (or removes it from) the *Manual selection* modifier of the pipeline; the
status bar shows its id, type and position.

The selection language: column names (`type`, `element`, `resname`, `resid`, `mol`, `q`, …), positions `x y z`,
comparisons and `and`, `or`, `not`, lists (`type in [1, 2]`), arithmetic, `within(3.5, type == "O")`, and the
macros `protein`, `backbone`, `sidechain`, `water`, `ions`, `hydrogen`, `heavy`.

## Themes and settings

**View ▸ Dark theme** switches the window and the graphs. The settings (recent files, paths of external programs,
worker threads, the last folder) are kept between sessions; the configuration folder is `~/.scivelyx-md`.
