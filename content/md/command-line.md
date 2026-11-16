# Command line

Every installer carries the command `scivelyx-md` beside the window. It reads the same files, runs the same
analyses and writes the same SciVelyx Graphs projects, without a window: for batch jobs, clusters and scripts.
`scivelyx-md COMMAND --help` lists the options of each command.

| Command | What it does |
|---|---|
| `info FILE` | frames, atoms, columns, units and cell of a trajectory; the blocks of a log |
| `rdf FILE --rmax R --pair A B` | g(r) and n(r) |
| `thermo LOG` | thermodynamics of a LAMMPS log, or GROMACS energies (.edr, .xvg), as sheets and graphs |
| `msd`, `vacf` | mean-squared displacement and diffusion; velocity autocorrelation |
| `angles`, `profile` | bond-angle distribution; density profile in slabs |
| `structure`, `peratom` | CNA fractions and mean order parameters frame by frame; per-atom properties of one frame |
| `species`, `reactions`, `bonds`, `charges` | ReaxFF species, reaction events, bonds by element pair, charges by element |
| `rmsd`, `rmsf`, `gyration`, `hbonds`, `dssp`, `sasa`, `pca` | biomolecules |
| `saltbridges`, `contacts`, `timeline` | salt bridges, residue contact maps, per-residue timelines |
| `volmap` | 3D density map: OpenDX or cube file and a project with 2D maps |
| `modify` | apply modifiers and write the frames (LAMMPS dump or data, extended XYZ, PDB), the data tables and the attributes |
| `modifiers` | list the modifiers and their parameters |
| `image`, `movie` | draw a frame or a movie in 3D, with any modifiers and representations |
| `script`, `shell` | run a Python script; an interactive Python with the commands |
| `versions` | the libraries inside the program and whether ffmpeg was found |
| `gui FILES` | open the window with these files |

## Common options

| Option | |
|---|---|
| `--topology FILE` | the `.tpr`, `.gro`, `.psf`, `.prmtop` or `.pdb` of a coordinate file; a LAMMPS data file for a dump |
| `--frames start:stop:step` | which frames |
| `--workers N` | threads for the analyses that run in parallel (or `$SCIVELYX_MD_WORKERS`) |
| `-o FILE` | the SciVelyx Graphs project to write (a default name otherwise) |
| `--csv FILE`, `--png FILE` | also the first table as CSV and the first graph as a picture |

## Examples

```bash
scivelyx-md info dump.lammpstrj
scivelyx-md rdf md.xtc --topology topol.tpr --rmax 10 --pair OW OW --by name
scivelyx-md msd dump.lammpstrj --types 1 --csv msd.csv --png msd.png
scivelyx-md structure dump.lammpstrj --cna 3.0 --workers 4
scivelyx-md rmsd md.xtc --topology topol.tpr --fit backbone
scivelyx-md modify dump.lammpstrj -m "replicate nx=2 ny=2 nz=2" -o big.data
scivelyx-md image dump.lammpstrj --frame -1 --rep licorice --ao --size-px 1920x1080 -o last.png
scivelyx-md script analysis.py runs/*.lammpstrj
```

The exit code is 0 on success and 1 on an error, with the message on the standard error.
