# FAQ and troubleshooting

## General

**Is SciTrace-Graphs a fork of SciDAVis or QtiPlot?**
No. It is written from scratch on PySide6, Matplotlib, NumPy, pandas and SciPy, and reads and writes their file
formats. No code from QtiPlot, SciDAVis or LabPlot is used.

**Does it need an internet connection?**
No. The network is used only when you ask for it, for example to read data from GitHub.

**Which language is the interface in?**
English, the program's only language.

**Does it cover everything SciDAVis and QtiPlot do?**
Yes. The menus of both and, since version 0.12, the options inside their fit, axis, curve and 3D dialogs. Version
0.17 added the last 21 items, such as 3D pies, logarithmic 3D axes, pictures as symbols, a log scale after an axis
break, the Plot wizard, Append project and custom script actions. See
[Plot wizard, windows and presentations](../working-tools/).

## Installation

**Windows says “Windows protected your PC”.** The test builds are not code-signed yet: click **More info → Run
anyway**.

**macOS says the app cannot be opened.** Control-click the app in Applications → **Open** → **Open**; on macOS 15,
System Settings → Privacy & Security → **Open Anyway**.

**The AppImage does not start.** Install `libfuse2`, or use the `.tar.gz` package.

## Working with the program

**A formula column does not update.** If you typed a value into it, it became an ordinary data column; set the
formula again with **Sheet → Set values**.

**The fit result does not follow my data.** Check that **Analysis → Automatic recalculation** is on, or press
**Recalculate now** (Ctrl+F5).

**Some text shows a red warning in the text dialog.** The math notation between `$…$` is invalid (for example an
unclosed brace); the dialog keeps the figure unchanged until it is fixed.

**Bold does not affect `$…$` math.** Use the **𝐁** button of the text dialog, which writes `\mathbf{}`.

## Reporting a problem

Open an issue in the [downloads repository]({{ROOT}}graphs/#download) with the version (Help → About), the
system, what you did and what happened, and — if you can share it — a small project or data file that shows it.
