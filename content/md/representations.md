# Representations

The drawing methods of VMD and the visual elements of OVITO are modifiers of the pipeline, so several of them share
one picture: a protein as a cartoon, its ligand as licorice and the water as points. **View ▸ Representations**
lists them.

![Water as licorice, with the hydrogen bonds as dashed lines and the oxygen density over the trajectory as an isosurface]({{AROOT}}assets/md/styles.webp)

## Atom styles

| Style | Drawing |
|---|---|
| default | spheres of the covalent radius × the size factor |
| VDW | spheres of the van der Waals radius (Bondi) |
| CPK | small spheres and thin bonds |
| Licorice | spheres and bonds of the same radius |
| Lines | bonds as lines |
| Points | points |

The style box of the 3D view applies to every atom; the **Atom style** modifier to the selected atoms only, with
its own radius and bond radius.

## Cartoon and ribbons

**Cartoon and ribbons** draws VMD's NewCartoon (helices as ribbons, strands as arrows, coils as tubes),
NewRibbons, Tube and Trace through the CA atoms of proteins, the P atoms of nucleic acids, or the atoms of any
polymer (one chain per molecule). The colours come from the secondary structure (DSSP, VMD's colours), from the
atoms, or one colour. The column `ss` also colours the atoms by secondary structure.

## Surfaces

| Modifier | Surface |
|---|---|
| Molecular surface | VMD's QuickSurf (Gaussian density), the solvent accessible surface (SAS) and the solvent excluded surface (SES), with its area and volume |
| Construct surface mesh | OVITO's alpha shape (surface area, solid volume and fraction, surface atoms) or a Gaussian density |
| Create isosurface | the level surface of a 3D grid: a *Density map* of the pipeline, or an OpenDX or Gaussian cube file |
| Coordination polyhedra | convex hulls of the bonded neighbours or of those within a cutoff |

![OVITO's surface mesh of the droplets of a Lennard-Jones vapour, with ambient occlusion]({{AROOT}}assets/md/surface.webp)

## 3D density maps

**Analysis ▸ 3D density map (volmap)** averages the number, mass or charge density of a selection over the frames
(or the fraction of frames with an atom in each voxel, VMD's occupancy), as a histogram or with Gaussian smoothing,
in any cell. It writes an OpenDX or cube file, opens the map as an isosurface and sends three 2D maps (the means
along the cell vectors) to SciVelyx Graphs. From the terminal:

```bash
scivelyx-md volmap water.lammpstrj --select "type == 1" --spacing 0.5 -o oxygen.dx
```

## Lines

- **Generate trajectory lines**: the path of the selected atoms over the frames, unwrapped or cut at the cell.
- **Hydrogen-bond lines**: dashed lines between donors and acceptors, with the definition of the hydrogen-bond
  analysis (VMD's HBonds).

## Ambient occlusion and ray tracing

- The **AO** box of the 3D view adds screen-space ambient occlusion to the view and the pictures; the **Ambient
  occlusion** modifier darkens buried atoms as OVITO does (column `ao_brightness`).
- **Ray-traced pictures** with shadows and ambient light are drawn by Tachyon (VMD's ray tracer) or POV-Ray,
  when you have installed them: File ▸ Save 3D image ▸ Renderer, or
  `scivelyx-md image … --renderer tachyon`. The camera is the camera of the view; the scene file can be kept.

![A Tachyon picture of adenylate kinase (cartoon and the surface of one domain), drawn from the camera of the view]({{AROOT}}assets/md/raytraced.webp)
