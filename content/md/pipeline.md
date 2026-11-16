# The modifier pipeline

As in OVITO, every frame you see, analyse, draw, film or export passes through a list of **modifiers**, from the
top of the list to the bottom. A modifier selects atoms, deletes them, adds copies, cuts a slab, computes a new
column, identifies the structure or draws something. Change a modifier and the view, the open analyses and the next
picture follow.

![A pipeline on a crystal–liquid run: CNA, select the non-FCC atoms, delete them, replicate along x, a text label]({{AROOT}}assets/md/pipeline.webp)

## The Pipeline dock

- **Add** (or Pipeline ▸ Add modifier) lists the modifiers by group.
- **Edit** (or double-click) opens the parameters of the modifier:

  ![The parameters of Expand selection]({{AROOT}}assets/md/modifier-dialog.webp)

- The check box switches a modifier off without removing it; ▲ ▼ change the order; ✕ removes it.
- **Save…** and **Load…** keep a pipeline in a `.json` file to use on other runs (also Pipeline ▸ Save pipeline).
- The help of the chosen modifier and its errors are shown below the list.

## The 54 modifiers

| Group | Modifiers |
|---|---|
| Selection | Expression selection, Select type, Manual selection (Ctrl+click in the view), Invert, Clear, Expand selection (by cutoff, N nearest or bonds), Select overlapping atoms |
| Modification | Affine transformation, Fix the centre of mass, Combine datasets, Compute property, Delete selected, Edit the cell, Edit types, Freeze property, Load trajectory, Remove property, Replicate, Slice, Smooth trajectory, Unwrap trajectories, Wrap at periodic boundaries |
| Colouring | Assign colour, Ambient occlusion |
| Structure identification | adaptive CNA, Polyhedral template matching, Ackland–Jones, Identify diamond structure, Chill+, VoroTop |
| Analysis | Measure distances and angles, Per-atom properties, Elastic strain, Displacement vectors, Atomic strain, Wigner–Seitz, Grain segmentation, Cluster analysis, Voronoi analysis, Spatial correlation, Histogram, Scatter plot, Dislocation analysis, Density map (3D) |
| Visualisation | Hide selected, Text label, Atom style, Trajectory lines, Hydrogen-bond lines, Cartoon and ribbons, Create isosurface, Construct surface mesh, Molecular surface, Coordination polyhedra |

The selection is a column (`selection`) that the next modifiers use: *Delete selected*, *Assign colour*, *Hide
selected*, *Atom style*, and the analyses that can work on the selected atoms only.

![A slab of water: the oxygens with x < 6 Å are selected, the selection is expanded along the bonds to their hydrogens and coloured]({{AROOT}}assets/md/selection.webp)

## Attributes and text labels

Modifiers also compute single values of the frame — counts of each structure, the number of selected or deleted
atoms, a surface area, a distance. They are the **attributes** of the frame, shown in the Properties dock. A *Text
label* writes them on the view, the pictures and the movies: `timestep [timestep]: [natoms] atoms`,
`[PTM.counts.FCC] FCC`, `O–H = [d_1_2] Å`.

*Measure distances and angles* takes atom ids (`distance 1 2; angle 2 1 3; dihedral 1 2 3 4`), across the periodic
boundary; **Analysis ▸ Distances, angles and dihedrals over time** gives them as a table and a graph.

## Writing the modified frames

**File ▸ Export frames** (Ctrl+E) writes the frames after the pipeline: LAMMPS dump, LAMMPS data file (with bonds
and type labels), extended XYZ or PDB. From the command line:

```bash
scivelyx-md modifiers                                   # every modifier and its parameters
scivelyx-md modify dump.lammpstrj -m "replicate nx=2 ny=2 nz=2" -m "slice normal='0 0 1' distance=5" -o out.data
scivelyx-md modify dump.lammpstrj --pipeline pipeline.json -o out.lammpstrj
scivelyx-md modify dump.lammpstrj -m "ptm" -m "grain_segmentation" --tables tables/ --attributes attrs.csv
```

`--tables` writes the data tables of the modifiers (one CSV each) and `--attributes` the attributes of every frame.
The same pipeline runs in Python with `modify(t, [Replicate(nx=2), Slice(distance=5)])`.

## How the window uses the pipeline

The analyses of the Analysis menu, pictures, movies, the external viewers and the exported files all use the frames
after the pipeline. Modifiers that need other frames (smooth, unwrap without image flags, freeze, fix the centre
of mass, load trajectory) make the analyses run on one thread.
