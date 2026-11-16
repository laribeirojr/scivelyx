# Pictures, movies and sessions

## Pictures

**File ▸ Save 3D image** (or *Save image…* in the 3D view) draws the current view again at any size, up to 16 384
pixels, with the camera, colours, selection and modifiers of the view:

![The Save image dialog]({{AROOT}}assets/md/save-image-dialog.webp)

- PNG, JPEG or TIFF; a transparent background for PNG and TIFF;
- a label with the timestep and the time;
- the renderer: OpenGL (as the view), or Tachyon and POV-Ray for ray-traced pictures with shadows and ambient light
  (programs you install; see [Representations]({{ROOT}}md/docs/representations/));
- ambient occlusion.

From the terminal, without a window:

```bash
scivelyx-md image dump.lammpstrj --frame -1 --color-by c_pe --cmap coolwarm --size-px 1920x1080 -o last.png
scivelyx-md image md.dcd --topology md.psf -m "cartoon" --renderer tachyon --size-px 1600x1200 -o protein.png
```

## Movies

**File ▸ Save 3D movie** films the chosen frames with the camera of the view:

![The Save movie dialog]({{AROOT}}assets/md/movie-dialog.webp)

| Option | |
|---|---|
| Frames | all, or `start:stop:step` |
| Frames per second | the speed of the movie |
| Width, height | in pixels (even numbers for MP4) |
| Turn the camera per frame | an orbit around the vertical axis of the view, in degrees per frame |
| Label | the timestep and the time in a corner |
| Video quality | fast to write, or the best (slower, smaller file) |

The file type follows the name: **MP4**, MOV, MKV, AVI or WebM through ffmpeg (installed by you), an animated
**GIF**, or a **series of PNG** files. From the terminal:

```bash
scivelyx-md movie dump.lammpstrj --fps 15 --orbit 1 --size-px 1280x720 -o run.mp4
```

## Sessions

**File ▸ Save session** (Ctrl+Shift+S) keeps the open files, the current frame, the pipeline, the view and its
camera, the per-atom properties and every result tab in one `*.scivelyx.json` file, which is also a SciVelyx Graphs
project. **File ▸ Open** of that file brings the session back, also after the folder has been moved with its data.

## Other viewers

**View ▸ Open in an external viewer** sends the chosen frames (after the pipeline) to VMD, UCSF ChimeraX or PyMOL
installed on your computer, as a multi-model PDB with a script that loads it as a trajectory. Set their paths in
**View ▸ Open in an external viewer ▸ Programs** if they are not found.
