# SciVelyx MD user manual

*Science in Motion. Data in Focus.*

SciVelyx MD reads molecular-dynamics trajectories of materials and of biomolecules, shows them in 3D, analyses them
and hands every result to SciVelyx Graphs as editable sheets and graphs. It is an alternative to OVITO and VMD,
with the same kind of modifier pipeline as OVITO and the representations and biomolecule tools of VMD. It has:

- readers for LAMMPS (text and binary dumps, data files, logs, ReaxFF files), GROMACS, CHARMM/NAMD, AMBER,
  HOOMD-blue, MOL2, PDB, CIF, XYZ and VASP files, and the structures of Quantum ESPRESSO, CASTEP and FHI-aims;
- a 3D view with atom styles, cartoons, surfaces, isosurfaces and ray-traced pictures;
- 54 modifiers in a pipeline: selection, modification, structure identification, analysis and visualisation;
- materials analyses (RDF, MSD and diffusion, CNA, PTM, Voronoi, strain, defects, grains, clusters) and
  biomolecule analyses (RMSD, RMSF, hydrogen bonds, DSSP, SASA, PCA, salt bridges, contact maps, timelines);
- ReaxFF species, reactions, bonds and charges;
- pictures, movies, sessions, Python scripts and a command line.

Our mission: to give researchers everywhere fast, precise and intuitive tools for analysing and visualising
scientific data, so that complex datasets become clear insights and the path from data to discovery is shorter.

<div class="manual-download">
<a class="btn btn-primary" href="{{AROOT}}downloads/{{MANUAL_PDF}}">Download this manual (PDF)</a>
</div>

The PDF has the same chapters as these pages, for reading offline or printing. Short video tutorials, filmed in
the program, are on the [SciVelyx channel on YouTube](https://www.youtube.com/@SciVelyxSuite).

![SciVelyx MD: adenylate kinase as a cartoon coloured by secondary structure, with the solvent-excluded surface of one domain]({{AROOT}}assets/md/main-window.webp)

## Where to start

| If you want to… | Read |
|---|---|
| install the program | [Installation]({{ROOT}}md/docs/install/) |
| know the parts of the window | [The window]({{ROOT}}md/docs/interface/) |
| open a run, look at it and send an RDF to SciVelyx Graphs in five minutes | [Your first analysis]({{ROOT}}md/docs/first-analysis/) |
| know which files open, and with which topology | [Files and formats]({{ROOT}}md/docs/formats/) |
| analyse crystals, liquids, defects and diffusion | [Materials analyses]({{ROOT}}md/docs/materials/) |
| select, delete, replicate, slice, colour and label atoms | [The modifier pipeline]({{ROOT}}md/docs/pipeline/) |
| draw licorice, cartoons, surfaces, density maps | [Representations]({{ROOT}}md/docs/representations/) |
| analyse proteins | [Biomolecules]({{ROOT}}md/docs/biomolecules/) |
| follow molecules and reactions in a ReaxFF run | [ReaxFF]({{ROOT}}md/docs/reaxff/) |
| save pictures, movies and sessions | [Pictures, movies and sessions]({{ROOT}}md/docs/pictures-movies/) |
| automate with Python | [Python scripts]({{ROOT}}md/docs/scripts/) |
| work without the window | [Command line]({{ROOT}}md/docs/command-line/) |
| open millions of atoms | [Large systems]({{ROOT}}md/docs/large-systems/) |
| find a quick answer | [Questions and answers]({{ROOT}}md/docs/faq/) |

## How the results reach SciVelyx Graphs

Every analysis opens a result tab with its table and graph. **File ▸ Send to SciVelyx Graphs** (Ctrl+G) opens the
same sheets and graphs in SciVelyx Graphs (installed separately), fully editable: change the axes, fit, export at the size of the
journal. **File ▸ Save as SciVelyx project** writes them to a `*.scivelyx.json` file that SciVelyx Graphs opens.
Each sheet records where it came from: the file, the frames and the parameters of the analysis.

## Checked against the reference programs

Every analysis is compared in the tests with the program it imitates, on real files: LAMMPS's own computes (RDF,
MSD, CNA, Voronoi, centrosymmetry, Steinhardt, displacements, Ackland–Jones, ReaxFF species), OVITO 3.17 atom by
atom (PTM, a-CNA, strain, Wigner–Seitz, Voronoi, clusters, surface mesh), MDAnalysis and MDTraj (RMSD, RMSF,
hydrogen bonds, DSSP, SASA, PCA, salt bridges, contact maps) and the official test files of each format. The
coverage of OVITO 3 Basic and of VMD is listed item by item in the project; at version 0.18 it is 99.4 % of OVITO
Basic and 100 % of the VMD list.
