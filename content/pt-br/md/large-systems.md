# Sistemas grandes

O SciVelyx MD lê as trajetórias frame a frame: abrir um arquivo lê um índice dos seus frames, e um frame só é lido
quando é mostrado ou analisado. Assim a memória fica em torno de um frame, seja qual for o tamanho da simulação.

## Leia o formato mais rápido

| Sistema | Arquivo | Índice | Um frame | Pico de memória |
|---|---|---|---|---|
| 1 000 188 átomos | dump de texto do LAMMPS, 400 MB | 2,2 s | 1,5 s | 0,3 GB |
| 1 000 188 átomos | dump binário do LAMMPS, 305 MB | 0,01 s | 0,2 s | 0,3 GB |
| 4 000 000 de átomos | dump de texto do LAMMPS, 643 MB | 0,5 s | 5,9 s | 0,9 GB |
| 4 000 000 de átomos | dump binário do LAMMPS, 488 MB | 0,00 s | 1,0 s | 1,0 GB |

Medido em 2 núcleos de CPU, sem placa de vídeo. Para simulações grandes, grave dumps binários no LAMMPS
(`dump 1 all custom 100 run.bin id type x y z`); eles são lidos exatamente como os dumps de texto, bit a bit. Dumps
compactados com gzip não permitem pular para um frame: chegar ao frame N descompacta todos os frames antes dele.

## Threads

A RDF, a estrutura no tempo, o raio de giro, a SASA e o DSSP dividem os frames entre threads. **Analysis ▸ Worker
threads** escolhe quantas (0 = todos os núcleos); na linha de comando, `--workers N` ou a variável
`SCIVELYX_MD_WORKERS`. Com 2 núcleos, a RDF de um milhão de átomos leva 6,1 s por frame em vez de 10,7 s, com o
mesmo resultado do LAMMPS.

## O que leva tempo

- A identificação de estruturas e as células de Voronoi andam átomo por átomo: o polyhedral template matching com
  todos os modelos leva cerca de 3 s por 1 000 átomos, as células de Voronoi cerca de 2 s, a CNA adaptativa e o
  Ackland–Jones menos de 1 s. A coordenação de 4 milhões de átomos leva cerca de 18 s.
- A vista 3D desenha um milhão de átomos em poucos segundos com renderização por software; uma placa de vídeo é bem
  mais rápida. Use o estilo rápido (sprites) e esconda o que não precisa (*Hide selected*) em sistemas muito
  grandes.
- MSD, VACF, ligações de hidrogênio, PCA e as análises do ReaxFF rodam numa thread só.
