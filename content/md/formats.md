# Files and formats

SciVelyx MD recognises a file by its name and, when the name says nothing (`pw.log`, `run.out`), by its first
lines. **File ▸ Open** takes several files at once; open a topology together with its trajectory.

## Trajectories and structures

| Program | Files | Notes |
|---|---|---|
| LAMMPS | dump `atom`/`custom` (text, `.gz`), binary dump (`.bin`), data file, log | any columns: wrapped, scaled, unwrapped, image flags, velocities, forces, charges, per-atom computes; triclinic cells; UNITS and TIME. A dump opened with the data file of the same atoms gets its labels, masses and bonds |
| LAMMPS ReaxFF | `fix reaxff/bonds` (text or `.gz`), `fix reaxff/species` | see [ReaxFF]({{ROOT}}md/docs/reaxff/) |
| GROMACS | `.tpr`, `.gro`, `.xtc`, `.trr`; energies `.edr`, `.xvg` | `.tpr` of GROMACS 4.0 to 2026; `.xtc`/`.trr` with a `.tpr`, `.gro`, `.psf` or `.pdb` |
| CHARMM, NAMD | `.psf`, `.dcd`, `.coor` (NAMD binary); NAMD log | CHARMM 36 and NAMD cells; energies of the NAMD log |
| AMBER | `.prmtop`, `.nc` (NetCDF) | |
| HOOMD-blue | `.gsd` | every frame |
| Tripos | `.mol2` | every molecule of the file as a frame |
| VASP | POSCAR, CONTCAR, XDATCAR | |
| Quantum ESPRESSO | pw.x input (`.pwi`, `.in`) and output (`.pwo`, `.out`) | every ionic step, with its total energy |
| CASTEP | `.castep`, `.cell` | every MD or relaxation step with its energy; `.cell` with unit lines and spins |
| FHI-aims | `geometry.in`, `aims.out` | every step of an MD or relaxation |
| Gaussian cube | `.cube` | the atoms, and the volume data as a grid for isosurfaces |
| Others | PDB, CIF, XYZ and extended XYZ | XYZ with any labels |

The structures of Quantum ESPRESSO, CASTEP and FHI-aims give the positions, the cell and the energy of each step
(the row `energy` of the **Properties** dock); their electronic data (bands, densities of states) belong to
SciVelyx DFT.

![A Quantum ESPRESSO relaxation of Si8 (13 ionic steps) with the isosurface of the charge density written by pp.x]({{AROOT}}assets/md/qe-cube.webp)

## Energies and logs

A LAMMPS log, a GROMACS `.edr` or `.xvg` file and a NAMD log open in the **Thermodynamics** tab: one block per
`run` or `minimize`, every column with its unit. `scivelyx-md thermo FILE` writes them as a SciVelyx Graphs project.

## Units

SciVelyx MD keeps the units of the file: the LAMMPS `units` style (real, metal, lj, si …) of the dump or the log,
Å and ps for the GROMACS, CHARMM, NAMD and AMBER files read through MDAnalysis, Å and eV for the DFT files. The
sheets sent to SciVelyx Graphs carry the units in their column headers.

## Writing frames

**File ▸ Export frames** (Ctrl+E) writes the frames after the modifier pipeline as a LAMMPS dump, a LAMMPS data file
(with bonds and type labels), extended XYZ or PDB. Any cell is written as a LAMMPS restricted triclinic cell.

## Which libraries read them

The LAMMPS, ReaxFF, XYZ and CASTEP `.cell` readers are SciVelyx MD's own. GROMACS, CHARMM/NAMD, AMBER, MOL2 and GSD
files are read through MDAnalysis; PDB, CIF, extended XYZ, VASP, Quantum ESPRESSO, CASTEP outputs, FHI-aims and cube
files through ASE. Every format is checked in the tests against official test files or files written by the program
itself, read again by independent readers.
