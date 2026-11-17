# Scripts Python

O SciVelyx MD roda Python em três lugares, com os mesmos comandos:

| Onde | Como | Para |
|---|---|---|
| A janela | **View ▸ Python console and scripts** (Ctrl+Shift+P), ou o botão *Python* | abas de scripts (Ctrl+J roda a linha ou a seleção, Ctrl+Shift+J o script), um console com histórico, os scripts de exemplo, e `app`: a própria janela |
| Um arquivo de script | `scivelyx-md script ARQUIVO.py [ARGS…]`, `scivelyx-md script -c "CÓDIGO"` | trabalho em lote: muitos arquivos, muitas análises, imagens e filmes; código de saída 1 em caso de erro, com a linha |
| O terminal | `scivelyx-md shell` | um Python interativo com os comandos (`api()` lista todos) |

![Um script de exemplo rodando no painel Python da janela; o console abaixo comanda a vista 3D]({{AROOT}}assets/md/python.webp)

## Os comandos

| Grupo | Comandos |
|---|---|
| Arquivos e frames | `load(caminho, topology=None)`, `frames(t, "início:fim:passo")`, `frame(t, i)`, `select(f, expr)`, `atoms(f, expr)` |
| Materiais | `rdf`, `msd`, `vacf`, `angles`, `profile`, `structure`, `coordination`, `cna`, `centrosymmetry`, `steinhardt`, `voronoi`, `clusters`, `cna_adaptive`, `ptm`, `ackland_jones`, `identify_diamond`, `chill_plus`, `elastic_strain`, `displacements`, `atomic_strain`, `wigner_seitz`, `grains`, `cluster_table`, `voronoi_cells`, `vorotop`, `spatial_correlation`, `dislocations`, `dislocation_series`, `histogram_time` |
| Biomoléculas | `rmsd`, `rmsf`, `gyration`, `hbonds`, `dssp`, `sasa`, `pca`, `salt_bridges`, `contact_map`, `timeline` |
| ReaxFF e energias | `species`, `reactions`, `thermo` |
| Volumes e superfícies | `density_map`, `volmap`, `read_grid`, `write_grid`, `isosurface`, `surface_mesh`, `molecular_surface`, `polyhedra`, `ambient_occlusion` |
| Pipeline | `pipeline`, `modify(t, [Replicate(nx=2), Slice(distance=5)])`, `modifiers()`, `export`, `measure`, `tables` |
| Saída | `image`, `movie`, `raytrace`, `table`, `send` (para o SciVelyx Graphs), `save` (um projeto) |
| A janela | `open_file`, `current`, `current_frame`, `current_frames`, `goto`, `view`, `snapshot`, `status`, `add_modifier`, `current_pipeline` |

Cada análise devolve um resultado cujos números se acessam diretamente (`g.r`, `g.g`, `m.fit.D`), com `.table` (um
DataFrame do pandas), `.csv(caminho)`, `.save(caminho)` e `.send()`. `np`, `pd` e `math` já estão prontos.

## Um exemplo

```python
# o coeficiente de difusão de cada simulação de uma pasta, e uma imagem de cada último frame
import glob
for path in sorted(glob.glob("runs/*/dump.lammpstrj")):
    t = load(path)
    m = msd(t, "1")                       # átomos do tipo 1
    print(f"{path}: D = {m.fit.D:.4g} ± {m.fit.stderr:.2g}")
    m.csv(path.replace("dump.lammpstrj", "msd.csv"))
    image(t, path.replace("dump.lammpstrj", "last.png"), index=-1, color_by="type")
```

Nove scripts de exemplo vêm com o programa (botão Examples do painel Python): primeiros passos, RDF em lote,
difusão, estrutura e um filme, um relatório de ReaxFF, um relatório de proteína, a janela automatizada, o pipeline
de modificadores e uma análise de materiais. A janela roda `~/.scivelyx-md/startup.py` sempre que abre, como o VMD
roda o seu `.vmdrc`.

Scripts são código seu e rodam com as suas permissões. Nos instaladores, um script pode importar as bibliotecas que
o programa traz: NumPy, SciPy, pandas, Matplotlib, ASE, MDAnalysis, pyedr, VTK/PyVista e PySide6.
