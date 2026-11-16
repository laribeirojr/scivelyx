# Análises de materiais

As análises de cristais, líquidos, vidros e defeitos seguem as definições dos computes do LAMMPS e do OVITO, e os
testes as comparam com os dois em simulações reais. Elas vêm de três formas:

- **propriedades por átomo** de cada frame, como novas colunas da tabela de átomos (Analysis ▸ Per-atom
  properties);
- **análises ao longo dos frames**, com uma aba de resultado (RDF, MSD, estrutura no tempo, ângulos, perfis);
- **modificadores** do pipeline, que se combinam com seleções e remoções (Analysis ▸ Materials, ou Pipeline ▸ Add
  modifier; veja [O pipeline de modificadores]({{ROOT}}md/docs/pipeline/)).

## Propriedades por átomo

**Analysis ▸ Per-atom properties** (Ctrl+P) acrescenta colunas a cada frame que você vê:

![A janela das propriedades por átomo]({{AROOT}}assets/md/peratom-dialog.webp)

| Propriedade | Coluna | Como no LAMMPS |
|---|---|---|
| Número de coordenação (todos os vizinhos ou tipos escolhidos) | `coord` | `compute coord/atom` |
| Análise de vizinhos comuns: 1 FCC, 2 HCP, 3 BCC, 4 ICO, 5 outro | `cna` | `compute cna/atom` |
| Centrossimetria (12 ou 8 vizinhos) | `centro` | `compute centro/atom` |
| Q4, Q6 … de Steinhardt | `Q4`, `Q6` | `compute orientorder/atom` |
| Volume e faces de Voronoi | `voro_volume`, `voro_faces` | `compute voronoi/atom` |
| Clusters por raio de corte (id = menor id de átomo) | `cluster` | `compute cluster/atom` |

Os raios de corte partem do espaçamento médio dos átomos; colore a vista por uma coluna nova, selecione com ela
(`cna == 1`) ou abra **Analysis ▸ Histograms of per-atom properties**.

![Um cristal de Lennard-Jones crescendo no seu líquido, colorido pela CNA: os átomos FCC em vermelho]({{AROOT}}assets/md/cna.webp)

## Análises ao longo dos frames

| Análise | Menu | O que dá |
|---|---|---|
| Função de distribuição radial | Analysis ▸ Radial distribution function | g(r) e n(r) por par de tipos, com os pares ligados excluídos se você quiser |
| Estrutura no tempo | Analysis ▸ Structure over time | contagens e frações da CNA, Q4 e Q6 médios, coordenação por frame |
| Deslocamento quadrático médio | Analysis ▸ Mean-squared displacement and diffusion | MSD por tipo (todas as origens de tempo, ou uma), com coordenadas desdobradas, a deriva do centro de massa removida se você pedir, e o coeficiente de difusão de um ajuste linear com seu erro |
| Autocorrelação de velocidades | Analysis ▸ Velocity autocorrelation | a VACF e o coeficiente de difusão de Green–Kubo |
| Distribuição de ângulos de ligação | Analysis ▸ Bond-angle distribution | como o `compute adf` |
| Perfil de densidade | Analysis ▸ Density profile | densidade numérica e mássica e a média de qualquer coluna em fatias ao longo de um vetor da célula |
| Histograma no tempo | Analysis ▸ Histogram over time | o histograma de uma coluna em cada frame, como mapa de calor |
| Mapa de densidade 3D | Analysis ▸ 3D density map (volmap) | veja [Representações]({{ROOT}}md/docs/representations/) |

![O deslocamento quadrático médio de um líquido de Lennard-Jones, com o ajuste linear e o coeficiente de difusão]({{AROOT}}assets/md/msd.webp)

![A fração de átomos FCC, HCP, BCC e outros, frame a frame]({{AROOT}}assets/md/structure.webp)

## Identificação de estruturas e defeitos (modificadores)

**Analysis ▸ Materials** acrescenta estes modificadores ao pipeline:

| Modificador | O que faz |
|---|---|
| Common neighbour analysis (adaptive) | a a-CNA do OVITO: FCC, HCP, BCC, ICO, outro, sem raio de corte |
| Polyhedral template matching | FCC, HCP, BCC, ICO, cúbica simples, diamante cúbico e hexagonal, grafeno; RMSD, orientação, distância interatômica, gradiente de deformação elástica |
| Ackland–Jones analysis | as regras do artigo (como o OVITO) ou as atuais do LAMMPS |
| Identify diamond structure | diamante cúbico e hexagonal e seus vizinhos |
| Chill+ | gelo hexagonal, cúbico e interfacial, hidratos |
| VoroTop | o código de Weinberg de cada célula de Voronoi, e os tipos de um filtro do VoroTop |
| Displacement vectors | a partir de um frame ou arquivo de referência, desdobrados, com mapeamento afim |
| Atomic strain | Falk–Langer: deformação de cisalhamento de von Mises e volumétrica, D²min, rotação e estiramento |
| Elastic strain | a partir da rede do PTM e de um parâmetro de rede |
| Wigner–Seitz defect analysis | vacâncias e intersticiais em relação a uma referência |
| Grain segmentation | grãos a partir das orientações do PTM |
| Cluster analysis | clusters por raio de corte, com tamanho, centro de massa e raio de giro |
| Voronoi analysis | volume, faces, área, índices (também células radicais), poliedros na vista |
| Spatial correlation function | de duas colunas por átomo, direta ou por FFT |
| Dislocation analysis (DXA) | o algoritmo do próprio OVITO, quando o módulo Python do OVITO está instalado |

![PTM e segmentação de grãos de um bicristal de ferro]({{AROOT}}assets/md/ptm-grains.webp)

![Deformação de cisalhamento atômica do bicristal sob tração, com a contagem de Wigner–Seitz de vacâncias e intersticiais]({{AROOT}}assets/md/strain.webp)

As tabelas desses modificadores (histogramas, clusters, grãos, índices de Voronoi, discordâncias) abrem com
**Pipeline ▸ Data tables of the current frame** e vão para o SciVelyx Graphs como qualquer resultado; seus valores
únicos (contagens, áreas, volumes) são atributos do frame, mostrados no painel Properties e nos rótulos de texto.

## Como foram conferidas

Em simulações reais do LAMMPS de um sistema cristal–líquido de Lennard-Jones, de um vapor, de um líquido e de um
bicristal de ferro BCC com defeitos: coordenação, CNA, clusters, faces e volumes de Voronoi, centrossimetria,
Steinhardt, deslocamentos, Ackland–Jones e o MSD são iguais aos próprios computes do LAMMPS; PTM, a-CNA, diamante,
Chill+, VoroTop, deformação atômica e elástica, Wigner–Seitz, clusters, Voronoi e a correlação são iguais ao OVITO
3.17 átomo por átomo. O coeficiente de difusão do líquido de Lennard-Jones fica a 3 % do valor da literatura.
