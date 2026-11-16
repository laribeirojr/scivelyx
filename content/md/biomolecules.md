# Biomolecules

**Analysis ▸ Biomolecules** holds the analyses of proteins and nucleic acids. They need the names, residues and
(for some) the bonds of a topology: open a GROMACS `.tpr`, a CHARMM/NAMD `.psf`, an AMBER `.prmtop` or a PDB with the
trajectory. Molecules are made whole across the periodic boundary along the bonds before fitting.

| Analysis | What it gives | As |
|---|---|---|
| RMSD | after a least-squares fit of a group (backbone by default), for the fit group and other groups, mass-weighted on request | `gmx rms`, VMD's RMSD tool |
| RMS fluctuation | per atom and per residue | `gmx rmsf` |
| Radius of gyration | with its x, y and z components | `gmx gyrate`, `measure rgyr` |
| Hydrogen bonds | per frame and the occupancy of every donor–hydrogen–acceptor triple, periodic | MDAnalysis |
| Secondary structure (DSSP) | helix, strand or loop per residue and frame, as fractions and a timeline | DSSP |
| Solvent accessible area | Shrake–Rupley, per atom, residue and frame | `gmx sasa` |
| Principal component analysis | eigenvalues, eigenvectors, projections of the fitted positions | `gmx covar` |
| Salt bridges | ASP/GLU oxygens within 3.2 Å of LYS/ARG nitrogens (HIS optional), occupancy and distances in time | VMD's Salt Bridges |
| Contact map | distance and fraction in contact of every pair of residues (closest heavy atoms, closest atoms or CA), contacts over time | MDTraj's contacts |
| Per-residue timeline | residue × time heat maps of secondary structure, RMSD, SASA, contacts, hydrogen bonds or salt bridges | VMD's Timeline |

![RMSD of the backbone of adenylate kinase after the fit to the first frame]({{AROOT}}assets/md/rmsd.webp)

![Salt bridges of adenylate kinase: the occupancy of each pair over the trajectory]({{AROOT}}assets/md/salt-bridges.webp)

![The residue contact map: the fraction of the frames in which two residues are within 4.5 Å]({{AROOT}}assets/md/contact-map.webp)

![The per-residue timeline of the secondary structure: helix, strand and loop of every residue in every frame]({{AROOT}}assets/md/timeline.webp)

## Selections

The dialogs take selections in the language of the 3D view, with the macros `protein`, `backbone`, `sidechain`,
`water`, `ions`, `hydrogen` and `heavy` (the same atoms as MDAnalysis), and columns such as `resname`, `resid`,
`segid`, `name`: `protein and name == "CA"`, `resid >= 122 and resid <= 159`.

## From the terminal and from Python

```bash
scivelyx-md rmsd md.xtc --topology topol.tpr --fit backbone
scivelyx-md dssp md.xtc --topology topol.tpr --strings dssp.txt
scivelyx-md saltbridges md.xtc --topology topol.tpr --table saltbridges.csv
scivelyx-md contacts md.xtc --topology topol.tpr --cutoff 4.5 --scheme closest-heavy
scivelyx-md timeline md.xtc --topology topol.tpr --quantity rmsd
```

```python
t = load("md.xtc", topology="topol.tpr")
sb = salt_bridges(t)
print(sb.pairs.head())          # acid, base, occupancy, mean and shortest O–N distance
send(timeline(t, "ss"))
```

## How they were checked

On the official test files of MDAnalysis (adenylate kinase as CHARMM PSF + DCD and as GROMACS TPR + XTC in water):
RMSD, RMSF, radius of gyration, hydrogen bonds, DSSP and PCA equal to MDAnalysis; RMSD, RMSF, SASA (within
0.3 %) and DSSP (97 % of the states) against MDTraj; salt bridges pair by pair against MDAnalysis; residue distances
equal to MDTraj's `compute_contacts` in its three schemes.
