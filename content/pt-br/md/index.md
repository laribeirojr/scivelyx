# Manual do usuário do SciVelyx MD

*Science in Motion. Data in Focus.*

O SciVelyx MD lê trajetórias de dinâmica molecular de materiais e de biomoléculas, mostra-as em 3D, analisa-as e
entrega cada resultado ao SciVelyx Graphs como planilhas e gráficos editáveis. É uma alternativa ao OVITO e ao VMD,
com o mesmo tipo de pipeline de modificadores do OVITO e as representações e ferramentas de biomoléculas do VMD.
Ele tem:

- leitores para o LAMMPS (dumps de texto e binários, arquivos data, logs, arquivos do ReaxFF), GROMACS,
  CHARMM/NAMD, AMBER, HOOMD-blue, MOL2, PDB, CIF, XYZ e arquivos do VASP, e as estruturas do Quantum ESPRESSO, do
  CASTEP e do FHI-aims;
- uma vista 3D com estilos de átomos, cartoons, superfícies, isossuperfícies e imagens em ray tracing;
- 54 modificadores num pipeline: seleção, modificação, identificação de estruturas, análise e visualização;
- análises de materiais (RDF, MSD e difusão, CNA, PTM, Voronoi, deformação, defeitos, grãos, clusters) e de
  biomoléculas (RMSD, RMSF, ligações de hidrogênio, DSSP, SASA, PCA, pontes salinas, mapas de contato, linhas do
  tempo);
- espécies, reações, ligações e cargas do ReaxFF;
- imagens, filmes, sessões, scripts Python e linha de comando.

Nossa missão: oferecer a pesquisadores de todo o mundo ferramentas rápidas, precisas e intuitivas para analisar e
visualizar dados científicos, para que conjuntos de dados complexos virem conclusões claras e o caminho dos dados à
descoberta fique mais curto.

<div class="manual-download">
<a class="btn btn-primary" href="{{AROOT}}downloads/{{MANUAL_PDF}}">Baixar este manual (PDF)</a>
</div>

O PDF tem os mesmos capítulos destas páginas, para ler sem internet ou imprimir. Vídeos curtos, gravados no
programa, estão no [canal SciVelyx no YouTube](https://www.youtube.com/@SciVelyxSuite).

![SciVelyx MD: a adenilato quinase como cartoon colorido pela estrutura secundária, com a superfície excluída do solvente de um domínio]({{AROOT}}assets/md/main-window.webp)

## Por onde começar

| Se você quer… | Leia |
|---|---|
| instalar o programa | [Instalação]({{ROOT}}md/docs/install/) |
| conhecer as partes da janela | [A janela]({{ROOT}}md/docs/interface/) |
| abrir uma simulação, olhar e mandar uma RDF ao SciVelyx Graphs em cinco minutos | [Sua primeira análise]({{ROOT}}md/docs/first-analysis/) |
| saber quais arquivos abrem, e com qual topologia | [Arquivos e formatos]({{ROOT}}md/docs/formats/) |
| analisar cristais, líquidos, defeitos e difusão | [Análises de materiais]({{ROOT}}md/docs/materials/) |
| selecionar, apagar, replicar, fatiar, colorir e rotular átomos | [O pipeline de modificadores]({{ROOT}}md/docs/pipeline/) |
| desenhar licorice, cartoons, superfícies, mapas de densidade | [Representações]({{ROOT}}md/docs/representations/) |
| analisar proteínas | [Biomoléculas]({{ROOT}}md/docs/biomolecules/) |
| acompanhar moléculas e reações numa simulação ReaxFF | [ReaxFF]({{ROOT}}md/docs/reaxff/) |
| gravar imagens, filmes e sessões | [Imagens, filmes e sessões]({{ROOT}}md/docs/pictures-movies/) |
| automatizar com Python | [Scripts Python]({{ROOT}}md/docs/scripts/) |
| trabalhar sem a janela | [Linha de comando]({{ROOT}}md/docs/command-line/) |
| abrir milhões de átomos | [Sistemas grandes]({{ROOT}}md/docs/large-systems/) |
| achar uma resposta rápida | [Perguntas e respostas]({{ROOT}}md/docs/faq/) |

## Como os resultados chegam ao SciVelyx Graphs

Cada análise abre uma aba de resultado com sua tabela e seu gráfico. **File ▸ Send to SciVelyx Graphs** (Ctrl+G)
abre as mesmas planilhas e gráficos no SciVelyx Graphs (instalado à parte), totalmente editáveis: mude os eixos, ajuste
curvas, exporte no tamanho da revista. **File ▸ Save as SciVelyx project** grava tudo num arquivo
`*.scivelyx.json` que o SciVelyx Graphs abre. Cada planilha registra de onde veio: o arquivo, os frames e os
parâmetros da análise.

## Conferido com os programas de referência

Nos testes, cada análise é comparada, em arquivos reais, com o programa que ela imita: os próprios computes do
LAMMPS (RDF, MSD, CNA, Voronoi, centrossimetria, Steinhardt, deslocamentos, Ackland–Jones, espécies do ReaxFF), o
OVITO 3.17 átomo por átomo (PTM, a-CNA, deformação, Wigner–Seitz, Voronoi, clusters, malha de superfície), o
MDAnalysis e o MDTraj (RMSD, RMSF, ligações de hidrogênio, DSSP, SASA, PCA, pontes salinas, mapas de contato) e os
arquivos de teste oficiais de cada formato. A cobertura do OVITO 3 Basic e do VMD está listada item a item no
projeto; na versão 0.17 ela é de 98,7 % do OVITO Basic e 100 % da lista do VMD.
