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

## The OVITO Pro environment

Version 0.20 brings what OVITO reserves for its paid edition, around Python and rendering:

- **Your own modifiers, formats, picture layers and tools.** Put Python files in `~/.scivelyx-md/extensions`;
  functions marked `@modifier_function("Title", params={…})` become pipeline modifiers (Pipeline ▸ Add modifier ▸
  Python), `@file_reader(".ext")` and `@file_writer(".ext")` new formats of File ▸ Open and Export frames,
  `@viewport_layer("Name")` drawings on pictures and movies (Tools ▸ Viewport layers), and `@utility("Title")`
  entries of Tools ▸ Utilities. The **Python script** modifier keeps a short `modify(frame, ctx)` function inside
  the pipeline itself.
- **Python code from the pipeline.** Tools ▸ Generate Python code writes a script with the file, the modifiers, the
  drawing and the camera, which exports the frames, draws the picture or films the movie; it runs in the window,
  with `scivelyx-md script` and with plain `python` (also `scivelyx-md codegen`).
- **Several datasets in one scene** (Tools ▸ Add a dataset to the scene), each with its frame, offset and pipeline,
  and **pictures of several views** side by side (Tools ▸ Picture of several views).
- **Files and formats.** glTF scenes for Blender, the web and PowerPoint (Tools ▸ Export the scene as glTF); ASE
  `.traj` and `.db` files; a Python script with `create(index)` or a LAMMPS input script (run by your LAMMPS)
  opened as data; files on another computer opened as `ssh://user@host/path` (Tools ▸ Open a remote file), copied
  by your own `scp`.
- **Rendering elsewhere.** Tools ▸ Render on a remote computer (or `--remote user@host`) makes the picture or the
  movie on a workstation with SciVelyx MD installed and brings it back; OSPRay Studio, if you install it, is one more
  ray tracer (Save 3D image ▸ Renderer).

![A Python script modifier colours the atoms by their height, the first frame of the same run is added beside the last one, and the script generated from the pipeline is open in the Python dock]({{AROOT}}assets/md/pro-python.webp)

![Four views of the iron bicrystal in one picture, coloured by the structure found by PTM]({{AROOT}}assets/md/pro-layout.webp)

```python
# ~/.scivelyx-md/extensions/my_tools.py  (ILLUSTRATIVE)
from scivelyx_md.extensions import modifier_function
from scivelyx_md.modifiers import copy_frame, with_attributes

@modifier_function("Kinetic energy", params={"mass": 1.0})
def kinetic_energy(frame, ctx, mass=1.0):
    d = frame.data.copy()
    d["ke"] = 0.5 * mass * (d.vx ** 2 + d.vy ** 2 + d.vz ** 2)
    return with_attributes(copy_frame(frame, data=d), ke_total=float(d.ke.sum()))
```
