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
| Dislocation analysis (DXA) | linhas de discordância, vetores de Burgers, junções e a malha de defeitos (veja abaixo) |

![PTM e segmentação de grãos de um bicristal de ferro]({{AROOT}}assets/md/ptm-grains.webp)

![Deformação de cisalhamento atômica do bicristal sob tração, com a contagem de Wigner–Seitz de vacâncias e intersticiais]({{AROOT}}assets/md/strain.webp)

## Discordâncias

**Dislocation analysis (DXA)** (Analysis ▸ Materials, ou Pipeline ▸ Add modifier) encontra as linhas de discordância
de cristais FCC, HCP, BCC, diamante cúbico e hexagonal com o algoritmo de extração de discordâncias (Stukowski,
Bulatov e Arsenlis): ele mapeia o cristal na rede ideal e percorre circuitos de Burgers em volta dos defeitos. Ele
dá:

- cada segmento com o seu vetor de Burgers na rede (por exemplo 1/6[1-21]) e no referencial da simulação, a sua
  família (1/2<110>, 1/6<112> Shockley, 1/6<110> stair-rod, 1/3<111> Frank …; 1/3<11-20>, <0001> … no HCP) e o seu
  comprimento, na tabela *dislocations*;
- as linhas na vista 3D, coloridas pela família, e as junções onde elas se encontram;
- a coluna `structure` (other, FCC, HCP, BCC, diamante cúbico ou hexagonal: as falhas de empilhamento aparecem como
  camadas HCP) e a *malha de defeitos* em volta dos outros defeitos (superfícies, contornos de grão);
- o comprimento de linha de cada família e a densidade de discordâncias como atributos.

Para ver só as linhas, acrescente *Expression selection* com `structure == 1` (os átomos FCC perfeitos) e *Delete
selected* depois dele. **Analysis ▸ Materials ▸ Dislocation lengths over time** roda a análise em cada frame e
desenha os comprimentos e a densidade contra o tempo no SciVelyx Graphs:

```sh
scivelyx-md dislocations dump.lammpstrj --lattice FCC --segments segmentos.csv
```

![Análise de discordâncias de um disco de vacâncias relaxado no cobre: parciais de Shockley (verde), stair-rods (rosa) e parciais de Frank (ciano) em volta das falhas de empilhamento (átomos vermelhos)]({{AROOT}}assets/md/dislocations.webp)

![Comprimentos de discordância por família de vetor de Burgers ao longo do tempo]({{AROOT}}assets/md/dislocation-lengths.webp)

As tabelas desses modificadores (histogramas, clusters, grãos, índices de Voronoi, discordâncias) abrem com
**Pipeline ▸ Data tables of the current frame** e vão para o SciVelyx Graphs como qualquer resultado; seus valores
únicos (contagens, áreas, volumes) são atributos do frame, mostrados no painel Properties e nos rótulos de texto.

## As análises do OVITO Pro

Desde a versão 0.19 o SciVelyx MD tem também, de graça, as análises que o OVITO reserva à edição paga Pro (Análise ▸
Materials, ou Pipeline ▸ Add modifier):

- **Fator de estrutura** S(k) pela rede recíproca da célula ou a partir de g(r), com os fatores de estrutura parciais
  e de Faber–Ziman e fatores de forma de raios X;
- **Find rings** (anéis de caminho mínimo das ligações, desenhados como polígonos), **distribuições de comprimentos**
  e de **ângulos de ligação**, e **ordens de ligação** com os grupos funcionais de moléculas (amida, aromático,
  carboxilato, nitro, amina) — acrescente antes **Create bonds**, ou use as ligações do arquivo;
- **Integração de cargas de Bader** de uma densidade eletrônica (arquivo cube do Gaussian), por átomo;
- **Regiões volumétricas e poros**: volume e área de cada região cheia e vazia, porosidade e vazios;
- **Identify fcc planar faults**: falhas de empilhamento intrínsecas, contornos de macla e falhas de várias camadas
  com suas áreas, depois de *Polyhedral template matching*;
- **Entropia local** (a entropia de pares de Piaggi e Parrinello, como o compute entropy/atom do LAMMPS);
- **Regiões do LAMMPS** (block, sphere, cylinder, cone, plane, prism, ellipsoid) e os átomos dentro delas;
- **Spatial binning** em 1, 2 ou 3 dimensões, **Reduce property**, **diferença entre quadros**, **média no tempo**,
  **séries temporais**, **coeficiente de difusão** (com o tensor de deslocamentos e por tipo de átomo), **parâmetros
  de Steinhardt** (com pesos de Voronoi, médios), **Color by type**;
- os átomos do núcleo de cada discordância (uma opção de *Dislocation analysis*) e cortes por planos da rede dados por
  índices de Miller (uma opção de *Slice*).

```sh
scivelyx-md modify asi.dump -m "create_bonds mode=cutoff cutoff=2.85" -m "find_rings maximum=10" --tables aneis/
scivelyx-md modify cu.dump -m "ptm" -m "fcc_planar_faults" --tables falhas/
```

![Anéis de caminho mínimo do silício amorfo, desenhados como polígonos coloridos pelo tamanho]({{AROOT}}assets/md/pro-rings.webp)

![Uma falha de empilhamento intrínseca (vermelho), uma falha de várias camadas (roxo) e os dois contornos de uma lamela de macla (azul) no cobre, sem os átomos CFC]({{AROOT}}assets/md/pro-faults.webp)

## Como foram conferidas

Em simulações reais do LAMMPS de um sistema cristal–líquido de Lennard-Jones, de um vapor, de um líquido e de um
bicristal de ferro BCC com defeitos: coordenação, CNA, clusters, faces e volumes de Voronoi, centrossimetria,
Steinhardt, deslocamentos, Ackland–Jones e o MSD são iguais aos próprios computes do LAMMPS; PTM, a-CNA, diamante,
Chill+, VoroTop, deformação atômica e elástica, Wigner–Seitz, clusters, Voronoi e a correlação são iguais ao OVITO
3.17 átomo por átomo. O coeficiente de difusão do líquido de Lennard-Jones fica a 3 % do valor da literatura.
As análises do OVITO Pro são
iguais às do próprio OVITO Pro (fator de estrutura, anéis, cargas de Bader, regiões, falhas planares, binning, difusão,
Steinhardt) ou às do LAMMPS (entropia local, regiões) em rodadas reais do LAMMPS; as ordens de ligação e o fator de
estrutura de Debye ficam próximos dos do OVITO (o arquivo de cobertura do projeto diz onde diferem).
