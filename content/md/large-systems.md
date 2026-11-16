# Large systems

SciVelyx MD reads trajectories frame by frame: opening a file reads an index of its frames, and a frame is read
only when it is shown or analysed. Memory therefore stays at about one frame, whatever the length of the run.

## Read the fastest format

| System | File | Index | One frame | Peak memory |
|---|---|---|---|---|
| 1 000 188 atoms | LAMMPS text dump, 400 MB | 2.2 s | 1.5 s | 0.3 GB |
| 1 000 188 atoms | LAMMPS binary dump, 305 MB | 0.01 s | 0.2 s | 0.3 GB |
| 4 000 000 atoms | LAMMPS text dump, 643 MB | 0.5 s | 5.9 s | 0.9 GB |
| 4 000 000 atoms | LAMMPS binary dump, 488 MB | 0.00 s | 1.0 s | 1.0 GB |

Measured on 2 CPU cores without a graphics card. For large runs, write binary dumps in LAMMPS
(`dump 1 all custom 100 run.bin id type x y z`); they are read exactly like the text dumps, bit for bit.
Gzipped dumps cannot jump to a frame: reaching frame N decompresses every frame before it.

## Worker threads

The RDF, structure over time, radius of gyration, SASA and DSSP split the frames among threads. **Analysis ▸ Worker
threads** sets how many (0 = every CPU core); on the command line `--workers N`, or the variable
`SCIVELYX_MD_WORKERS`. On 2 cores the RDF of one million atoms takes 6.1 s per frame instead of 10.7 s, with the same
result as LAMMPS.

## What takes time

- Structure identification and Voronoi cells run atom by atom: polyhedral template matching with every template
  takes about 3 s per 1 000 atoms, Voronoi cells about 2 s, adaptive CNA and Ackland–Jones under 1 s. Coordination
  of 4 million atoms takes about 18 s.
- The 3D view draws one million atoms in a few seconds with software rendering; a graphics card is much faster.
  Use the fast style (sprites) and hide what you do not need (*Hide selected*) for very large systems.
- MSD, VACF, hydrogen bonds, PCA and the ReaxFF analyses run on one thread.
