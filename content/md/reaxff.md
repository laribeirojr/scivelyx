# ReaxFF

A ReaxFF run of LAMMPS writes the bond orders of every atom with `fix reaxff/bonds` and, optionally, the molecules
with `fix reaxff/species`. SciVelyx MD reads both, plain or gzipped, and builds molecules, species and reactions
from the bond orders, with the cutoff you choose per element pair.

## Opening a run

Open the dump, the log and the bond file together. The bond file is linked to the dump of the same atoms: the 3D
view draws its bonds, and the table gains the columns `abo` (sum of bond orders), `nlp` (lone pairs), `nbonds`,
`molecule` and `species`. The elements come from the `pair_coeff * * ffield C H O` line of the log, or from the
element column of the dump.

![A CH4 + O2 ReaxFF run in the middle of the combustion, coloured by the charge]({{AROOT}}assets/md/reaxff-3d.webp)

## Analyses (Analysis ▸ ReaxFF)

| Analysis | What it gives |
|---|---|
| Elements, bond-order cutoff and timestep | the settings: one cutoff for every pair or one per element pair (`C-H=0.4,O-O=0.65,default=0.3`), the timestep for the time axis |
| Species from bond orders | the number of each molecule over time (named as LAMMPS names them), the most frequent ones in the graph |
| Bonds by element pair and bond-order distribution | bond counts per pair over time, histograms of the bond orders |
| Charges by element | mean charge and its spread per element over time |
| Reaction events | who reacts with whom and when (old and new molecules sharing atoms), with counts and the net change of each species |

A `fix reaxff/species` file opens as a table and a graph of its own.

![Species over time from the bond orders of the CH4 + O2 run]({{AROOT}}assets/md/reaxff.webp)

## Command line

```bash
scivelyx-md species bonds.reaxff --elements "C H O" --cutoff "C-H=0.4,default=0.3"
scivelyx-md reactions bonds.reaxff --elements "C H O"
scivelyx-md bonds bonds.reaxff
scivelyx-md charges dump.lammpstrj
```

## A note on the step of the species

The species that LAMMPS's `fix reaxff/species` writes for step N are the molecules of the bond orders of step
N − 1. SciVelyx MD's species belong to the step of their block of the bond file, so the two series are shifted by
one output step. The tests check that our species are identical to LAMMPS's at every one of 200 consecutive steps
once this shift is taken into account.
