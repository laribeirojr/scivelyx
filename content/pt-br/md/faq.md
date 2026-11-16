# Perguntas e respostas

**O SciVelyx MD roda simulações?**
Não. Ele lê a saída do LAMMPS, GROMACS, NAMD, AMBER, HOOMD-blue e de códigos de DFT, e a analisa.

**Preciso do SciVelyx Graphs?**
Ele vem dentro dos instaladores. Qualquer resultado pode ser mandado para ele com Ctrl+G, como planilhas e gráficos
editáveis, ou salvo como um projeto `*.scivelyx.json` que o SciVelyx Graphs abre.

**Meu arquivo xtc (ou dcd, ou nc) não abre.**
Esses arquivos só têm posições. Abra a topologia junto com eles: um `.tpr` ou `.gro` para um `.xtc`, um `.psf` para
um `.dcd`, um `.prmtop` para um `.nc`.

**Faltam as ligações do meu dump do LAMMPS.**
Abra o arquivo data dos mesmos átomos junto com o dump, ou marque *bonds* para desenhá-las por distância (raios
covalentes).

**Por que a RDF difere da do meu script do LAMMPS?**
Confira se os pares ligados são tratados igualmente (*Bonded pairs* na janela, `special_bonds` no LAMMPS) e se os
mesmos frames entram na média. Com as mesmas escolhas, as duas concordam até os seis algarismos que o LAMMPS imprime.

**Ele lê minha sessão do OVITO ou meu estado do VMD?**
Não. Ele lê os arquivos de dados; o pipeline e as representações são montados de novo no SciVelyx MD, e um pipeline
pode ser salvo e carregado como arquivo `.json`.

**Como faço uma imagem para um artigo?**
File ▸ Save 3D image no tamanho que você precisa (por exemplo 3000 × 2000 pixels), com fundo transparente ou um ray
tracer para as sombras. Os gráficos dos resultados passam pelo SciVelyx Graphs, que exporta PDF, SVG e EPS no
tamanho exato da coluna da revista.

**Tem análise de discordâncias?**
Tem, pelo algoritmo do próprio OVITO: instale o módulo Python do OVITO (`pip install ovito`) num Python do seu
computador, e o SciVelyx MD o roda lá.

**Em que idioma está a interface?**
Inglês. Este manual e o site estão em inglês e português.

**O programa manda alguma coisa pela internet?**
Não. Ele funciona sem internet e não tem conta, telemetria nem ativação.

**Onde relato um problema?**
Nas issues do repositório de versões (o link está na barra lateral deste manual), com a versão
(`scivelyx-md --version`) e, se puder, um arquivo pequeno que mostre o problema.
