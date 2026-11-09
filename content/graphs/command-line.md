# Command line

Every package contains `sciplot`, the command-line side of SciPlot-Graphs: on Windows next to `SciPlot-Graphs.exe`
(or on the PATH, if you chose it when installing), on macOS in `SciPlot-Graphs.app/Contents/MacOS/`, on Linux next
to `SciPlot-Graphs` in the folder or as `SciPlot-Graphs.AppImage sciplot …`.

| Command | What it does |
|---|---|
| `sciplot gui [project]` | Opens the window (with a project or data file). |
| `sciplot render project.splot.json -o figure.pdf [--dpi 300]` | Draws a project to PDF, SVG, EPS, PNG or TIFF. |
| `sciplot quick data.csv -x T -y rho -o figure.pdf` | Plots columns of a data file (`--kind`, `--preset`, `--xlabel`, `--ylabel`, `-z` for maps). |
| `sciplot github <url> [-r]` | Lists the tabular files of a GitHub repository or folder (`-r`: subfolders too). |
| `sciplot migrate paths… -o folder` | Converts SciDAVis and QtiPlot projects (and Origin exports) to SciPlot, with reports. |
| `sciplot export-project project.splot.json -o out.sciprj` | Writes a project for SciDAVis (`.sciprj`), QtiPlot (`.qti`) or Origin (`.py`). |
| `sciplot origin-script -o export_from_origin.py` | Saves the script that exports `.opj`/`.opju` from inside Origin. |
| `sciplot script file.py [--project p.splot.json] [--save out.splot.json]` | Runs a Python script with the [scripting API]({{ROOT}}graphs/docs/scripts/). |
| `sciplot --version` | Prints the version. |

`sciplot <command> --help` lists every option of a command.

## Examples

```bash
# Redraw every figure of a thesis after changing the theme in the projects
for p in figures/*.splot.json; do sciplot render "$p" -o "pdf/$(basename "$p" .splot.json).pdf"; done

# Convert a whole archive of SciDAVis and QtiPlot projects
sciplot migrate ~/old_projects -o ~/sciplot_projects
```
