# Python scripts

SciVelyx MD runs Python in three places, with the same commands:

| Where | How | For |
|---|---|---|
| The window | **View ▸ Python console and scripts** (Ctrl+Shift+P), or the *Python* button | script tabs (Ctrl+J runs the line or the selection, Ctrl+Shift+J the script), a console with history, the example scripts, and `app`: the window itself |
| A script file | `scivelyx-md script FILE.py [ARGS…]`, `scivelyx-md script -c "CODE"` | batch work: many files, many analyses, pictures and movies; exit code 1 on an error, with the line |
| The terminal | `scivelyx-md shell` | an interactive Python with the commands (`api()` lists them) |

![An example script run in the Python dock of the window; the console below it drives the 3D view]({{AROOT}}assets/md/python.webp)

## The commands

| Group | Commands |
|---|---|
| Files and frames | `load(path, topology=None)`, `frames(t, "start:stop:step")`, `frame(t, i)`, `select(f, expr)`, `atoms(f, expr)` |
| Materials | `rdf`, `msd`, `vacf`, `angles`, `profile`, `structure`, `coordination`, `cna`, `centrosymmetry`, `steinhardt`, `voronoi`, `clusters`, `cna_adaptive`, `ptm`, `ackland_jones`, `identify_diamond`, `chill_plus`, `elastic_strain`, `displacements`, `atomic_strain`, `wigner_seitz`, `grains`, `cluster_table`, `voronoi_cells`, `vorotop`, `spatial_correlation`, `dislocations`, `dislocation_series`, `histogram_time` |
| Biomolecules | `rmsd`, `rmsf`, `gyration`, `hbonds`, `dssp`, `sasa`, `pca`, `salt_bridges`, `contact_map`, `timeline` |
| ReaxFF and energies | `species`, `reactions`, `thermo` |
| Volumes and surfaces | `density_map`, `volmap`, `read_grid`, `write_grid`, `isosurface`, `surface_mesh`, `molecular_surface`, `polyhedra`, `ambient_occlusion` |
| Pipeline | `pipeline`, `modify(t, [Replicate(nx=2), Slice(distance=5)])`, `modifiers()`, `export`, `measure`, `tables` |
| Output | `image`, `movie`, `raytrace`, `table`, `send` (to SciVelyx Graphs), `save` (a project) |
| The window | `open_file`, `current`, `current_frame`, `current_frames`, `goto`, `view`, `snapshot`, `status`, `add_modifier`, `current_pipeline` |

Each analysis returns a result whose numbers are reachable directly (`g.r`, `g.g`, `m.fit.D`), with `.table` (a
pandas DataFrame), `.csv(path)`, `.save(path)` and `.send()`. `np`, `pd` and `math` are ready to use.

## An example

```python
# the diffusion coefficient of every run of a folder, and a picture of each last frame
import glob
for path in sorted(glob.glob("runs/*/dump.lammpstrj")):
    t = load(path)
    m = msd(t, "1")                       # atoms of type 1
    print(f"{path}: D = {m.fit.D:.4g} ± {m.fit.stderr:.2g}")
    m.csv(path.replace("dump.lammpstrj", "msd.csv"))
    image(t, path.replace("dump.lammpstrj", "last.png"), index=-1, color_by="type")
```

Nine example scripts come with the program (Examples button of the Python dock): first steps, batch RDF,
diffusion, structure and a movie, a ReaxFF report, a protein report, the window automated, the modifier pipeline and
a materials analysis. The window runs `~/.scivelyx-md/startup.py` each time it starts, as VMD runs its `.vmdrc`.

Scripts are your own code and run with your permissions. In the installers a script can import the libraries the
program carries: NumPy, SciPy, pandas, Matplotlib, ASE, MDAnalysis, pyedr, VTK/PyVista and PySide6.
