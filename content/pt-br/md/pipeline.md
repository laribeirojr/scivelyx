# O pipeline de modificadores

Como no OVITO, cada frame que você vê, analisa, desenha, filma ou exporta passa por uma lista de **modificadores**,
do primeiro ao último. Um modificador seleciona átomos, apaga-os, acrescenta cópias, corta uma fatia, calcula uma
coluna nova, identifica a estrutura ou desenha alguma coisa. Mude um modificador e a vista, as análises abertas e a
próxima imagem acompanham.

![Um pipeline numa simulação cristal–líquido: CNA, seleção dos átomos que não são FCC, remoção, replicação em x, um rótulo de texto]({{AROOT}}assets/md/pipeline.webp)

## O painel Pipeline

- **Add** (ou Pipeline ▸ Add modifier) lista os modificadores por grupo.
- **Edit** (ou duplo clique) abre os parâmetros do modificador:

  ![Os parâmetros de Expand selection]({{AROOT}}assets/md/modifier-dialog.webp)

- A caixa de marcação desliga um modificador sem removê-lo; ▲ ▼ mudam a ordem; ✕ o remove.
- **Save…** e **Load…** guardam um pipeline num arquivo `.json`, para usá-lo em outras simulações (também em
  Pipeline ▸ Save pipeline).
- A ajuda do modificador escolhido e seus erros aparecem abaixo da lista.

## Os 54 modificadores

| Grupo | Modificadores |
|---|---|
| Seleção | Expression selection, Select type, Manual selection (Ctrl+clique na vista), Invert, Clear, Expand selection (por raio de corte, N mais próximos ou ligações), Select overlapping atoms |
| Modificação | Affine transformation, Fix the centre of mass, Combine datasets, Compute property, Delete selected, Edit the cell, Edit types, Freeze property, Load trajectory, Remove property, Replicate, Slice, Smooth trajectory, Unwrap trajectories, Wrap at periodic boundaries |
| Cores | Assign colour, Ambient occlusion |
| Identificação de estruturas | adaptive CNA, Polyhedral template matching, Ackland–Jones, Identify diamond structure, Chill+, VoroTop |
| Análise | Measure distances and angles, Per-atom properties, Elastic strain, Displacement vectors, Atomic strain, Wigner–Seitz, Grain segmentation, Cluster analysis, Voronoi analysis, Spatial correlation, Histogram, Scatter plot, Dislocation analysis, Density map (3D) |
| Visualização | Hide selected, Text label, Atom style, Trajectory lines, Hydrogen-bond lines, Cartoon and ribbons, Create isosurface, Construct surface mesh, Molecular surface, Coordination polyhedra |

A seleção é uma coluna (`selection`) que os modificadores seguintes usam: *Delete selected*, *Assign colour*,
*Hide selected*, *Atom style* e as análises que podem trabalhar só com os átomos selecionados.

![Uma fatia de água: os oxigênios com x < 6 Å são selecionados, a seleção é expandida pelas ligações até seus hidrogênios e colorida]({{AROOT}}assets/md/selection.webp)

## Atributos e rótulos de texto

Os modificadores também calculam valores únicos do frame — contagens de cada estrutura, o número de átomos
selecionados ou apagados, uma área de superfície, uma distância. São os **atributos** do frame, mostrados no painel
Properties. Um *Text label* escreve-os na vista, nas imagens e nos filmes: `timestep [timestep]: [natoms] atoms`,
`[PTM.counts.FCC] FCC`, `O–H = [d_1_2] Å`.

*Measure distances and angles* recebe ids de átomos (`distance 1 2; angle 2 1 3; dihedral 1 2 3 4`), atravessando a
fronteira periódica; **Analysis ▸ Distances, angles and dihedrals over time** dá esses valores como tabela e
gráfico.

## Gravar os frames modificados

**File ▸ Export frames** (Ctrl+E) grava os frames depois do pipeline: dump do LAMMPS, arquivo data do LAMMPS (com
ligações e rótulos de tipos), XYZ estendido ou PDB. Pela linha de comando:

```bash
scivelyx-md modifiers                                   # todos os modificadores e seus parâmetros
scivelyx-md modify dump.lammpstrj -m "replicate nx=2 ny=2 nz=2" -m "slice normal='0 0 1' distance=5" -o out.data
scivelyx-md modify dump.lammpstrj --pipeline pipeline.json -o out.lammpstrj
scivelyx-md modify dump.lammpstrj -m "ptm" -m "grain_segmentation" --tables tabelas/ --attributes atributos.csv
```

`--tables` grava as tabelas de dados dos modificadores (um CSV cada) e `--attributes` os atributos de cada frame. O
mesmo pipeline roda em Python com `modify(t, [Replicate(nx=2), Slice(distance=5)])`.

## Como a janela usa o pipeline

As análises do menu Analysis, as imagens, os filmes, os visualizadores externos e os arquivos exportados usam
todos os frames depois do pipeline. Modificadores que precisam de outros frames (suavizar, desdobrar sem image
flags, congelar, fixar o centro de massa, carregar trajetória) fazem as análises rodarem numa thread só.
