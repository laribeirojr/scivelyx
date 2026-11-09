# Scripts

**Scripts → Script window** (Ctrl+Shift+P) opens a window with several scripts in tabs, line numbers, syntax
highlighting and a console. Scripts are Python and are saved in the project.

| Key | Action |
|---|---|
| Ctrl+J | Run the current line or the selection |
| Ctrl+Shift+J | Run the whole script |
| Ctrl+Enter | Evaluate and write the value below the line (`#> value`) |

The console below runs one command at a time and keeps the history. **Restart** clears the interpreter.

![The script window]({{ROOT}}assets/img/script-window.webp){: width="1000" height="640" loading="lazy" }

## The API

The namespace already holds NumPy (`np`), pandas (`pd`), `math` and these functions:

| Call | What it does |
|---|---|
| `table("name")` | A sheet; `t["col"]` reads a column as a NumPy array, `t["col"] = values` writes one (the table grows if needed). |
| `new_table("name", x=…, y=…)` | Creates a sheet from columns (or from a DataFrame). |
| `matrix("name")`, `new_matrix("name", z=…, x=…, y=…)` | Read or create a matrix; `m.values("sin(x)*cos(y)")` sets values by formula. |
| `fit(data, x, y, model, …)` | Least-squares fit (`model` is a built-in name such as `"gauss"` or a formula such as `"a*exp(-x/t) + c"`); accepts `p0`, `sigma`, `fixed`, `xrange`, `bounds`, `method`, `tol`, `maxfev`, `scale_errors`, `n_curve`, `curve_x`. Returns `values`, `errors`, `r2`, `report()`… |
| `plot(data, x, y, kind="line", new=False)` | Adds a curve to the active graph (or a new one). |
| `export("figure.pdf", dpi=300)` | Exports the active graph. |
| `note("text")` | Appends to the project notes. |
| `recalculate()` | Redoes the analyses that depend on changed data. |
| `tables()`, `matrices()`, `datasets()` | Names in the project. |

```python
# Fit every spectrum of a project and collect the peak centers in a table
centers, errors = [], []
names = [n for n in tables() if n.startswith("spectrum_")]
for name in names:
    r = fit(name, "x", "y", "gauss")
    k = list(r.names).index("xc")
    centers.append(r.values[k])
    errors.append(r.errors[k])
new_table("centers", sample=names, xc=centers, xc_err=errors)
plot("centers", "sample", "xc", kind="scatter", new=True)
```

## Without the window

The same API works from the command line, for batch jobs and clusters:

```bash
sciplot script analysis.py                                  # data created by the script itself
sciplot script analysis.py --project project.splot.json     # on an existing project
sciplot script analysis.py --project p.splot.json --save p2.splot.json
```

Scripts run with your own permissions, like any Python program, so run only scripts you trust.
