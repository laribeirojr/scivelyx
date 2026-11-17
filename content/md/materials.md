# Materials analyses

The analyses of crystals, liquids, glasses and defects follow the definitions of the LAMMPS computes and of OVITO,
and the tests compare them with both on real runs. They come in three forms:

- **per-atom properties** of every frame, as new columns of the atom table (Analysis ▸ Per-atom properties);
- **analyses over the frames**, with a result tab (RDF, MSD, structure over time, angles, profiles);
- **modifiers** of the pipeline, which can be combined with selections and deletions (Analysis ▸ Materials, or
  Pipeline ▸ Add modifier; see [The modifier pipeline]({{ROOT}}md/docs/pipeline/)).

## Per-atom properties

**Analysis ▸ Per-atom properties** (Ctrl+P) adds columns to every frame you look at:

![The per-atom properties dialog]({{AROOT}}assets/md/peratom-dialog.webp)

| Property | Column | As LAMMPS |
|---|---|---|
| Coordination number (all neighbours or chosen types) | `coord` | `compute coord/atom` |
| Common neighbour analysis: 1 FCC, 2 HCP, 3 BCC, 4 ICO, 5 other | `cna` | `compute cna/atom` |
| Centrosymmetry (12 or 8 neighbours) | `centro` | `compute centro/atom` |
| Steinhardt Q4, Q6 … | `Q4`, `Q6` | `compute orientorder/atom` |
| Voronoi volume and faces | `voro_volume`, `voro_faces` | `compute voronoi/atom` |
| Clusters by a cutoff (id = smallest atom id) | `cluster` | `compute cluster/atom` |

The cutoffs start from the mean spacing of the atoms; colour the view by a new column, select with it
(`cna == 1`), or open **Analysis ▸ Histograms of per-atom properties**.

![A Lennard-Jones crystal growing in its liquid, coloured by CNA: FCC atoms in red]({{AROOT}}assets/md/cna.webp)

## Analyses over the frames

| Analysis | Menu | What it gives |
|---|---|---|
| Radial distribution function | Analysis ▸ Radial distribution function | g(r) and n(r) per pair of types, bonded pairs optionally left out |
| Structure over time | Analysis ▸ Structure over time | CNA counts and fractions, mean Q4 and Q6, coordination per frame |
| Mean-squared displacement | Analysis ▸ Mean-squared displacement and diffusion | MSD per type (every time origin, or one), unwrapped, the centre-of-mass drift removed on request, the diffusion coefficient from a straight-line fit with its error |
| Velocity autocorrelation | Analysis ▸ Velocity autocorrelation | VACF and the Green–Kubo diffusion coefficient |
| Bond-angle distribution | Analysis ▸ Bond-angle distribution | as `compute adf` |
| Density profile | Analysis ▸ Density profile | number and mass density and the mean of any column in slabs along a cell vector |
| Histogram over time | Analysis ▸ Histogram over time | the histogram of a column in every frame, as a heat map |
| 3D density map | Analysis ▸ 3D density map (volmap) | see [Representations]({{ROOT}}md/docs/representations/) |

![The mean-squared displacement of a Lennard-Jones liquid with the straight-line fit and the diffusion coefficient]({{AROOT}}assets/md/msd.webp)

![The fraction of FCC, HCP, BCC and other atoms frame by frame]({{AROOT}}assets/md/structure.webp)

## Structure identification and defects (modifiers)

**Analysis ▸ Materials** adds these modifiers to the pipeline:

| Modifier | What it does |
|---|---|
| Common neighbour analysis (adaptive) | OVITO's a-CNA: FCC, HCP, BCC, ICO, other, without a cutoff |
| Polyhedral template matching | FCC, HCP, BCC, ICO, simple cubic, cubic and hexagonal diamond, graphene; RMSD, orientation, interatomic distance, elastic deformation gradient |
| Ackland–Jones analysis | the rules of the paper (as OVITO) or of LAMMPS today |
| Identify diamond structure | cubic and hexagonal diamond and their neighbours |
| Chill+ | hexagonal, cubic and interfacial ice, hydrates |
| VoroTop | the Weinberg code of every Voronoi cell, and the types of a VoroTop filter |
| Displacement vectors | from a reference frame or file, unwrapped, with affine mapping |
| Atomic strain | Falk–Langer: von Mises shear and volumetric strain, D²min, rotation and stretch |
| Elastic strain | from the PTM lattice and a lattice constant |
| Wigner–Seitz defect analysis | vacancies and interstitials against a reference |
| Grain segmentation | grains from the PTM orientations |
| Cluster analysis | clusters by a cutoff with their size, centre of mass and radius of gyration |
| Voronoi analysis | volume, faces, area, indices (also radical cells), polyhedra in the view |
| Spatial correlation function | of two per-atom columns, direct or by FFT |
| Dislocation analysis (DXA) | dislocation lines, Burgers vectors, junctions and the defect mesh (see below) |

![PTM and grain segmentation of an iron bicrystal]({{AROOT}}assets/md/ptm-grains.webp)

![Atomic shear strain of the bicrystal under tension, with the Wigner–Seitz count of vacancies and interstitials]({{AROOT}}assets/md/strain.webp)

## Dislocations

**Dislocation analysis (DXA)** (Analysis ▸ Materials, or Pipeline ▸ Add modifier) finds the dislocation lines of
FCC, HCP, BCC, cubic and hexagonal diamond crystals with the dislocation extraction algorithm (Stukowski, Bulatov
and Arsenlis): it maps the crystal onto the ideal lattice and walks Burgers circuits around the defects. It gives:

- every segment with its Burgers vector in the lattice (for example 1/6[1-21]) and in the simulation frame, its
  family (1/2<110>, 1/6<112> Shockley, 1/6<110> stair-rod, 1/3<111> Frank …; 1/3<11-20>, <0001> … in HCP) and its
  length, as the table *dislocations*;
- the lines in the 3D view, coloured by family, and the junctions where they meet;
- the column `structure` (other, FCC, HCP, BCC, cubic or hexagonal diamond: stacking faults show as HCP layers) and
  the *defect mesh* around the other defects (surfaces, grain boundaries);
- the line length of every family and the dislocation density as attributes.

To look at the lines alone, add *Expression selection* with `structure == 1` (the perfect FCC atoms) and *Delete
selected* after it. **Analysis ▸ Materials ▸ Dislocation lengths over time** runs it on every frame and draws the
lengths and the density against time in SciVelyx Graphs:

```sh
scivelyx-md dislocations dump.lammpstrj --lattice FCC --segments segments.csv
```

![Dislocation analysis of a vacancy disc relaxed in copper: Shockley partials (green), stair-rods (pink) and Frank partials (cyan) around stacking faults (red atoms)]({{AROOT}}assets/md/dislocations.webp)

![Dislocation lengths by Burgers vector family over time]({{AROOT}}assets/md/dislocation-lengths.webp)

The tables these modifiers make (histograms, clusters, grains, Voronoi indices, dislocations) open with
**Pipeline ▸ Data tables of the current frame** and go to SciVelyx Graphs like any result; their single values
(counts, areas, volumes) are attributes of the frame, shown in the Properties dock and in text labels.

## How they were checked

On real LAMMPS runs of a Lennard-Jones crystal–liquid system, a vapour, a liquid and a BCC iron bicrystal with
defects: coordination, CNA, clusters, Voronoi faces and volumes, centrosymmetry, Steinhardt, displacements,
Ackland–Jones and the MSD are equal to LAMMPS's own computes; PTM, a-CNA, diamond, Chill+, VoroTop, atomic and
elastic strain, Wigner–Seitz, clusters, Voronoi and the correlation are equal to OVITO 3.17 atom by atom. The
diffusion coefficient of the Lennard-Jones liquid is within 3 % of the literature.
