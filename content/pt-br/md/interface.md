# A janela

![A janela com uma simulação do GROMACS: o painel Files, a aba Atoms com a vista 3D e a tabela de átomos, os painéis Properties e Pipeline]({{AROOT}}assets/md/gromacs.webp)

| Parte | O que faz |
|---|---|
| **Menus** | File (abrir, salvar, exportar frames, imagens, filmes, sessões, Send to SciVelyx Graphs), Analysis (RDF, propriedades por átomo, materiais, ReaxFF, biomoléculas, threads), Pipeline (acrescentar, salvar e carregar modificadores, tabelas de dados), View (tema, representações, visualizadores externos), Help |
| **Barra de ferramentas** | Open, Radial distribution function, Send to SciVelyx Graphs, Save as SciVelyx project, Python |
| **Files** (à esquerda) | os arquivos abertos: trajetórias, topologias, logs, arquivos de energia e do ReaxFF. Clique num deles para mostrá-lo. Um arquivo de coordenadas (xtc, dcd, nc) usa a topologia aberta dos mesmos átomos |
| Aba **Atoms** | os controles de frames, a vista 3D e a tabela de átomos do frame atual |
| Aba **Thermodynamics** | as colunas de um log do LAMMPS ou de um arquivo de energias como gráfico e tabela, um bloco por run |
| **Abas de resultado** | uma por análise: um gráfico (escolha em *Graph*), a tabela, a barra de ferramentas do gráfico |
| **Properties** (à direita) | o frame (arquivo, formato, passo, tempo, unidades, átomos, célula, atributos) e as estatísticas de cada coluna |
| **Pipeline** (à direita) | os modificadores aplicados a cada frame, com a ajuda logo abaixo |
| **Barra de status** | a última mensagem: o caminho do arquivo, o resultado de uma análise, um aviso |

## Abrir arquivos

**File ▸ Open** (Ctrl+O) aceita vários arquivos de uma vez; também dá para soltá-los na janela. Abra a topologia
junto com a trajetória: um `.tpr` do GROMACS com o `.xtc`, um `.psf` com o `.dcd`, um `.prmtop` com o `.nc`, um
arquivo data do LAMMPS com o dump. Um dump do LAMMPS aberto com o arquivo data dos mesmos átomos recebe os rótulos
dos tipos, as massas e as ligações. **File ▸ Open recent** lista os últimos arquivos.

## Os controles de frames

O controle deslizante, os botões (primeiro, anterior, tocar, próximo, último) e a caixa do frame percorrem a
trajetória; o rótulo mostra o passo, o tempo e o número de átomos. *table: selected atoms only* limita a tabela à
seleção.

## A vista 3D

| Controle | Efeito |
|---|---|
| Colour | por tipo, elemento, resíduo, segmento ou qualquer coluna por átomo (carga, velocidade, CNA, deformação …) |
| Mapa de cores, faixa | o mapa e seus limites (`auto` usa a faixa do frame) |
| size, estilo | o fator de tamanho e o desenho: `auto`, esferas reais ou sprites rápidos |
| default / vdw / cpk / licorice / lines / points | o método de desenho de todos os átomos (por seleção, com o modificador *Atom style*) |
| AO | oclusão ambiente na vista |
| bonds, cutoff | ligações da topologia, ou por distância (`auto`: raios covalentes) |
| cell, wrap | as arestas da célula, e os átomos trazidos de volta para dentro dela |
| Select | uma expressão de seleção, mostrada como *highlight* ou *only* |
| ⟲ x y z | volta a câmera ao início, ou olha ao longo de um eixo |
| Save image… | uma imagem da vista em qualquer tamanho |

Arraste com o botão esquerdo para girar, a roda dá zoom, o botão direito (ou Shift + esquerdo) desloca.
**Ctrl + clique** num átomo o acrescenta ao (ou retira do) modificador *Manual selection* do pipeline; a barra de
status mostra o id, o tipo e a posição dele.

A linguagem de seleção: nomes de colunas (`type`, `element`, `resname`, `resid`, `mol`, `q`, …), posições
`x y z`, comparações e `and`, `or`, `not`, listas (`type in [1, 2]`), aritmética, `within(3.5, type == "O")` e as
macros `protein`, `backbone`, `sidechain`, `water`, `ions`, `hydrogen`, `heavy`.

## Temas e preferências

**View ▸ Dark theme** troca o tema da janela e dos gráficos. As preferências (arquivos recentes, caminhos dos
programas externos, threads, a última pasta) ficam guardadas entre as sessões; a pasta de configuração é
`~/.scivelyx-md`.
