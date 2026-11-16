# Linha de comando

Todo instalador traz o comando `scivelyx-md` ao lado da janela. Ele lê os mesmos arquivos, roda as mesmas análises e
grava os mesmos projetos do SciVelyx Graphs, sem janela: para trabalhos em lote, clusters e scripts.
`scivelyx-md COMANDO --help` lista as opções de cada comando.

| Comando | O que faz |
|---|---|
| `info ARQUIVO` | frames, átomos, colunas, unidades e célula de uma trajetória; os blocos de um log |
| `rdf ARQUIVO --rmax R --pair A B` | g(r) e n(r) |
| `thermo LOG` | termodinâmica de um log do LAMMPS, ou energias do GROMACS (.edr, .xvg), como planilhas e gráficos |
| `msd`, `vacf` | deslocamento quadrático médio e difusão; autocorrelação de velocidades |
| `angles`, `profile` | distribuição de ângulos de ligação; perfil de densidade em fatias |
| `structure`, `peratom` | frações da CNA e parâmetros de ordem médios frame a frame; propriedades por átomo de um frame |
| `species`, `reactions`, `bonds`, `charges` | espécies, eventos de reação, ligações por par de elementos e cargas por elemento do ReaxFF |
| `rmsd`, `rmsf`, `gyration`, `hbonds`, `dssp`, `sasa`, `pca` | biomoléculas |
| `saltbridges`, `contacts`, `timeline` | pontes salinas, mapas de contato entre resíduos, linhas do tempo por resíduo |
| `volmap` | mapa de densidade 3D: arquivo OpenDX ou cube e um projeto com mapas 2D |
| `modify` | aplica modificadores e grava os frames (dump ou data do LAMMPS, XYZ estendido, PDB), as tabelas de dados e os atributos |
| `modifiers` | lista os modificadores e seus parâmetros |
| `image`, `movie` | desenha um frame ou um filme em 3D, com quaisquer modificadores e representações |
| `script`, `shell` | roda um script Python; um Python interativo com os comandos |
| `versions` | as bibliotecas dentro do programa e se o ffmpeg foi encontrado |
| `gui ARQUIVOS` | abre a janela com esses arquivos |

## Opções comuns

| Opção | |
|---|---|
| `--topology ARQUIVO` | o `.tpr`, `.gro`, `.psf`, `.prmtop` ou `.pdb` de um arquivo de coordenadas; um arquivo data do LAMMPS para um dump |
| `--frames início:fim:passo` | quais frames |
| `--workers N` | threads para as análises que rodam em paralelo (ou `$SCIVELYX_MD_WORKERS`) |
| `-o ARQUIVO` | o projeto do SciVelyx Graphs a gravar (senão, um nome padrão) |
| `--csv ARQUIVO`, `--png ARQUIVO` | também a primeira tabela como CSV e o primeiro gráfico como imagem |

## Exemplos

```bash
scivelyx-md info dump.lammpstrj
scivelyx-md rdf md.xtc --topology topol.tpr --rmax 10 --pair OW OW --by name
scivelyx-md msd dump.lammpstrj --types 1 --csv msd.csv --png msd.png
scivelyx-md structure dump.lammpstrj --cna 3.0 --workers 4
scivelyx-md rmsd md.xtc --topology topol.tpr --fit backbone
scivelyx-md modify dump.lammpstrj -m "replicate nx=2 ny=2 nz=2" -o grande.data
scivelyx-md image dump.lammpstrj --frame -1 --rep licorice --ao --size-px 1920x1080 -o ultimo.png
scivelyx-md script analise.py runs/*.lammpstrj
```

O código de saída é 0 em caso de sucesso e 1 em caso de erro, com a mensagem na saída de erro.
