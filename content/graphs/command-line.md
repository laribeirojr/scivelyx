# Command line

Every package contains `scivelyx`, the command-line side of SciVelyx Graphs: on Windows next to `SciVelyx-Graphs.exe`
(or on the PATH, if you chose it when installing), on macOS in `SciVelyx-Graphs.app/Contents/MacOS/`, on Linux next
to `SciVelyx-Graphs` in the folder or as `SciVelyx-Graphs.AppImage scivelyx …`.

| Command | What it does |
|---|---|
| `scivelyx gui [project]` | Opens the window (with a project or data file). |
| `scivelyx render project.scivelyx.json -o figure.pdf [--dpi 300]` | Draws a project to PDF, SVG, EPS, PNG or TIFF. |
| `scivelyx quick data.csv -x T -y rho -o figure.pdf` | Plots columns of a data file (`--kind`, `--preset`, `--xlabel`, `--ylabel`, `-z` for maps). |
| `scivelyx github <url> [-r]` | Lists the tabular files of a GitHub repository or folder (`-r`: subfolders too). |
| `scivelyx migrate paths… -o folder` | Converts SciDAVis and QtiPlot projects (and Origin exports) to SciVelyx, with reports. |
| `scivelyx export-project project.scivelyx.json -o out.sciprj` | Writes a project for SciDAVis (`.sciprj`), QtiPlot (`.qti`) or Origin (`.py`). |
| `scivelyx origin-script -o export_from_origin.py` | Saves the script that exports `.opj`/`.opju` from inside Origin. |
| `scivelyx script file.py [--project p.scivelyx.json] [--save out.scivelyx.json]` | Runs a Python script with the [scripting API]({{ROOT}}graphs/docs/scripts/). |
| `scivelyx selftest [--gui]` | Runs the self-test and writes the report and `selftest.zip`. |
| `scivelyx --version` | Prints the version. |

`scivelyx <command> --help` lists every option of a command. In installations made from the source with `install.sh`,
the old `scitrace` and `scitrace-gui` commands still work and start the same program.

## Examples

```bash
# Redraw every figure of a thesis after changing the theme in the projects
for p in figures/*.scivelyx.json; do scivelyx render "$p" -o "pdf/$(basename "$p" .scivelyx.json).pdf"; done

# Convert a whole archive of SciDAVis and QtiPlot projects
scivelyx migrate ~/old_projects -o ~/scivelyx_projects
```
