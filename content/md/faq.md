# Questions and answers

**Does SciVelyx MD run simulations?**
No. It reads the output of LAMMPS, GROMACS, NAMD, AMBER, HOOMD-blue and DFT codes, and analyses it.

**Do I need SciVelyx Graphs?**
It comes inside the installers. Every result can be sent to it with Ctrl+G as editable sheets and graphs, or saved
as a `*.scivelyx.json` project that SciVelyx Graphs opens.

**My xtc (or dcd, or nc) file does not open.**
These files have positions only. Open the topology together with them: a `.tpr` or `.gro` for an `.xtc`, a `.psf`
for a `.dcd`, a `.prmtop` for a `.nc`.

**The bonds of my LAMMPS dump are missing.**
Open the data file of the same atoms together with the dump, or tick *bonds* to draw them by distance (covalent
radii).

**Why does the RDF differ from the one of my LAMMPS input?**
Check that the bonded pairs are treated alike (*Bonded pairs* in the dialog, `special_bonds` in LAMMPS) and that
the same frames are averaged. With the same choices the two agree to the six digits LAMMPS prints.

**Can it read my OVITO session or my VMD state?**
No. It reads the data files; the pipeline and the representations are set up again in SciVelyx MD, and a pipeline
can be saved and loaded as a `.json` file.

**How do I make a picture for a paper?**
File ▸ Save 3D image at the size you need (for example 3000 × 2000 pixels), with a transparent background or a ray
tracer for shadows. Graphs of the results go through SciVelyx Graphs, which exports PDF, SVG and EPS at the exact
size of the journal column.

**Is there a dislocation analysis?**
Yes, through OVITO's own algorithm: install OVITO's Python module (`pip install ovito`) in a Python of your
computer, and SciVelyx MD runs it there.

**Which language is the interface in?**
English. This manual and the website are in English and Portuguese.

**Does the program send anything over the internet?**
No. It works offline and has no account, telemetry or activation.

**Where do I report a problem?**
In the issues of the releases repository (the link is in the side bar of this manual), with the version
(`scivelyx-md --version`) and, if you can, a small file that shows the problem.
