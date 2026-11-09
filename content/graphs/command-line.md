# Command line

Every package contains `scitrace`, the command-line side of SciTrace-Graphs: on Windows next to `SciTrace-Graphs.exe`
(or on the PATH, if you chose it when installing), on macOS in `SciTrace-Graphs.app/Contents/MacOS/`, on Linux next
to `SciTrace-Graphs` in the folder or as `SciTrace-Graphs.AppImage scitrace …`.

| Command | What it does |
|---|---|
| `scitrace gui [project]` | Opens the window (with a project or data file). |
| `scitrace render project.scitrace.json -o figure.pdf [--dpi 300]` | Draws a project to PDF, SVG, EPS, PNG or TIFF. |
| `scitrace quick data.csv -x T -y rho -o figure.pdf` | Plots columns of a data file (`--kind`, `--preset`, `--xlabel`, `--ylabel`, `-z` for maps). |
| `scitrace github <url> [-r]` | Lists the tabular files of a GitHub repository or folder (`-r`: subfolders too). |
| `scitrace migrate paths… -o folder` | Converts SciDAVis and QtiPlot projects (and Origin exports) to SciTrace, with reports. |
| `scitrace export-project project.scitrace.json -o out.sciprj` | Writes a project for SciDAVis (`.sciprj`), QtiPlot (`.qti`) or Origin (`.py`). |
| `scitrace origin-script -o export_from_origin.py` | Saves the script that exports `.opj`/`.opju` from inside Origin. |
| `scitrace script file.py [--project p.scitrace.json] [--save out.scitrace.json]` | Runs a Python script with the [scripting API]({{ROOT}}graphs/docs/scripts/). |
| `scitrace --version` | Prints the version. |

`scitrace <command> --help` lists every option of a command.

## Examples

```bash
# Redraw every figure of a thesis after changing the theme in the projects
for p in figures/*.scitrace.json; do scitrace render "$p" -o "pdf/$(basename "$p" .scitrace.json).pdf"; done

# Convert a whole archive of SciDAVis and QtiPlot projects
scitrace migrate ~/old_projects -o ~/scitrace_projects
```
