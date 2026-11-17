# Questions and answers

**Does SciVelyx MD run simulations?**
No. It reads the output of LAMMPS, GROMACS, NAMD, AMBER, HOOMD-blue and DFT codes, and analyses it.

**Do I need SciVelyx Graphs?**
No: SciVelyx MD works without it, and every result has its table and graph in SciVelyx MD. To edit the graphs,
install SciVelyx Graphs (its own installer): Ctrl+G saves the result as a `*.scivelyx.json` project and opens it in
SciVelyx Graphs. Without SciVelyx Graphs the project file is kept, and opens there later.

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
Yes, its own (since 0.18): Analysis ▸ Materials ▸ Dislocation analysis (DXA), for FCC, HCP, BCC and diamond
crystals, with the same segments and Burgers vectors as OVITO's DXA on the test runs. OVITO's own algorithm can still
be chosen in the modifier when OVITO's Python module is installed.

**Which language is the interface in?**
English. This manual and the website are in English and Portuguese.

**Does the program send anything over the internet?**
No. It works offline and has no account, telemetry or activation.

**Where do I report a problem?**
In the issues of the releases repository (the link is in the side bar of this manual), with the version
(`scivelyx-md --version`) and, if you can, a small file that shows the problem.
