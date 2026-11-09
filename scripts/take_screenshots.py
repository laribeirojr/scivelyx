"""Take the SciPlot-Graphs screenshots of the website (WebP, English interface).

    python scripts/take_screenshots.py /path/to/sciplot-studio-backup

Needs SciPlot-Graphs installed (pip install -e <source>) and runs offscreen.  The SciDAVis project of the
migration pictures is made from one of the program's examples with ``sciplot export-project``."""
import os, tempfile, sys
os.environ["QT_QPA_PLATFORM"] = "offscreen"; os.environ["HOME"] = tempfile.mkdtemp()
os.environ["SCIPLOT_CONFIG_DIR"] = tempfile.mkdtemp()
import numpy as np, pandas as pd
from pathlib import Path
from PIL import Image
from PySide6.QtWidgets import QApplication
app = QApplication.instance() or QApplication([])
from sciplot.gui.main_window import MainWindow
from sciplot.core.data import from_frame
from sciplot.core.spec import SeriesSpec
from sciplot.examples import gallery
SOURCE = Path(sys.argv[1] if len(sys.argv) > 1 else "../sciplot-studio-backup").resolve()
OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img"; OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
def save(widget, name, q=86):
    p = TMP / f"{name}.png"; widget.grab().save(str(p))
    im = Image.open(p).convert("RGB"); im.save(OUT / f"{name}.webp", "WEBP", quality=q, method=6)
    print(name, im.size)
w = MainWindow(); w.settings.clear(); w.resize(1600, 1000); w.show(); app.processEvents()
def flush(tab="Graphs"):
    for _ in range(4): app.processEvents(); w._render_timer.timeout.emit(); app.processEvents()
    r = w.ribbon
    for k in range(r.count()):
        if r.tabText(k).replace("&", "") == tab: r.setCurrentIndex(k)
    app.processEvents()
app.processEvents()
names = list(gallery())
w.load_example(next(n for n in names if n.lower().startswith("tight")) ); flush()
save(w, "main-window")
# property dialog of an axis
from sciplot.gui.dialogs import PropertyDialog
d = PropertyDialog(w, ("axis", 0, "x"), "Tick labels"); d.resize(835, 900); d.show(); app.processEvents(); save(d, "axis-dialog"); d.reject()
# peak analyzer
rng = np.random.default_rng(5)
x = np.linspace(10, 80, 1401)
G = lambda x, c, f, A: A*np.exp(-4*np.log(2)*(x-c)**2/f**2)
y = 5 + 0.05*x + G(x, 26.6, .4, 100) + G(x, 33.2, .6, 40) + G(x, 45.1, .5, 70) + G(x, 54.3, .7, 25) + rng.normal(0, .5, x.size)
dd = from_frame("XRD", pd.DataFrame({"2theta": x, "I": y})); dd.set_meta("2theta", designation="X", long_name="2θ", units="°"); dd.set_meta("I", long_name="Intensity", units="a.u.")
w.add_dataset(dd); w.new_graph(name="XRD")
a = w.spec.axes[0]; a.series = [SeriesSpec(kind="line", dataset="XRD", x="2theta", y="I", label="XRD", color="#15243A", linewidth=0.8)]
a.xlabel, a.ylabel = "2θ (°)", "Intensity (a.u.)"; w._structure_changed(); w.redraw(); flush()
from sciplot.gui.advanced_dialogs import PeakAnalyzerDialog
pa = PeakAnalyzerDialog(w, 0, 0); pa.nmax.setValue(4); pa.run(); pa.resize(1240, 760); pa.show(); app.processEvents()
save(pa, "peak-analyzer"); pa.out_res.setChecked(True); pa.accept(); flush()
# fit wizard
from sciplot.gui.analysis_dialogs import FitDialog
xx = np.linspace(0, 10, 60)
w.add_dataset(from_frame("decay", pd.DataFrame({"t": xx, "signal": 3*np.exp(-xx/2) + 0.5 + rng.normal(0, 0.04, xx.size)})))
w.new_graph(name="Fit"); w.spec.axes[0].series = [SeriesSpec(kind="scatter", dataset="decay", x="t", y="signal", label="signal", markersize=4)]
w._structure_changed(); w.redraw(); flush()
f = FitDialog(w, 0, 0); f.model.setCurrentIndex(f.model.findData("expdec")); f._model_changed()
f.add_conf.setChecked(True); f.add_pred.setChecked(True); f.run(); f.resize(1260, 820); f.show(); app.processEvents(); save(f, "fit-wizard"); f.accept(); flush()
flush("Analysis"); save(w, "fit-result")
# dark theme with the 2D + 3D energy surface example
w.toggle_ui_theme(True); w.load_example(next(n for n in names if "energy surface" in n.lower())); flush(); save(w, "dark-theme")
w.toggle_ui_theme(False)
# scripts
w.show_scripts(); sw = w.dock_scripts
w.scripts.editor().setPlainText('''# Fit the strongest XRD peak and keep the result in a table
r = fit("XRD", "2theta", "I", "gauss", xrange=(25, 28.5))
print(r.report())

summary = new_table("peak_summary", parameter=list(r.names),
                    value=list(r.values), error=list(r.errors))
plot("XRD", "2theta", "I", kind="line", new=True)
export("xrd_peak.pdf")
''')
os.chdir(TMP); w.scripts.run_all(); app.processEvents()
sw.resize(1000, 640); app.processEvents(); save(sw, "script-window")
sw.hide()
# migration report
import subprocess
sci = TMP / "md_thermo.sciprj"
subprocess.run([sys.executable, "-m", "sciplot.cli", "export-project",
                str(SOURCE / "examples" / "04_md_thermodynamics_dual_axis_synthetic.splot.json"), "-o", str(sci)], check=True)
w._open_project_path(str(sci), show_report=True); flush()
dlg = getattr(w, "last_dialog", None)
if dlg is not None:
    dlg.only_issues.setChecked(False); dlg.resize(980, 260); app.processEvents(); save(dlg, "migration-report"); dlg.close()
save(w, "scidavis-project")
print("done")
