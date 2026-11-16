# Arquivos e formatos

O SciVelyx MD reconhece um arquivo pelo nome e, quando o nome não diz nada (`pw.log`, `run.out`), pelas primeiras
linhas. **File ▸ Open** aceita vários arquivos de uma vez; abra a topologia junto com a trajetória.

## Trajetórias e estruturas

| Programa | Arquivos | Observações |
|---|---|---|
| LAMMPS | dump `atom`/`custom` (texto, `.gz`), dump binário (`.bin`), arquivo data, log | quaisquer colunas: coordenadas dentro da caixa, escaladas, desdobradas, image flags, velocidades, forças, cargas, computes por átomo; células triclínicas; UNITS e TIME. Um dump aberto com o arquivo data dos mesmos átomos recebe os rótulos, as massas e as ligações |
| LAMMPS ReaxFF | `fix reaxff/bonds` (texto ou `.gz`), `fix reaxff/species` | veja [ReaxFF]({{ROOT}}md/docs/reaxff/) |
| GROMACS | `.tpr`, `.gro`, `.xtc`, `.trr`; energias `.edr`, `.xvg` | `.tpr` do GROMACS 4.0 a 2026; `.xtc`/`.trr` com um `.tpr`, `.gro`, `.psf` ou `.pdb` |
| CHARMM, NAMD | `.psf`, `.dcd`, `.coor` (binário do NAMD); log do NAMD | células do CHARMM 36 e do NAMD; energias do log do NAMD |
| AMBER | `.prmtop`, `.nc` (NetCDF) | |
| HOOMD-blue | `.gsd` | todos os frames |
| Tripos | `.mol2` | cada molécula do arquivo como um frame |
| VASP | POSCAR, CONTCAR, XDATCAR | |
| Quantum ESPRESSO | entrada (`.pwi`, `.in`) e saída (`.pwo`, `.out`) do pw.x | cada passo iônico, com a energia total |
| CASTEP | `.castep`, `.cell` | cada passo de MD ou de relaxação, com a energia; `.cell` com linhas de unidades e spins |
| FHI-aims | `geometry.in`, `aims.out` | cada passo de uma MD ou relaxação |
| Gaussian cube | `.cube` | os átomos, e os dados volumétricos como grade para isossuperfícies |
| Outros | PDB, CIF, XYZ e XYZ estendido | XYZ com quaisquer rótulos |

As estruturas do Quantum ESPRESSO, do CASTEP e do FHI-aims dão as posições, a célula e a energia de cada passo
(painel **Properties**, linha `energy`); os dados eletrônicos (bandas, densidades de estados) ficam com o SciVelyx
DFT.

![Uma relaxação do Si8 no Quantum ESPRESSO (13 passos iônicos) com a isossuperfície da densidade de carga gravada pelo pp.x]({{AROOT}}assets/md/qe-cube.webp)

## Energias e logs

Um log do LAMMPS, um arquivo `.edr` ou `.xvg` do GROMACS e um log do NAMD abrem na aba **Thermodynamics**: um bloco
por `run` ou `minimize`, cada coluna com sua unidade. `scivelyx-md thermo ARQUIVO` grava tudo como projeto do
SciVelyx Graphs.

## Unidades

O SciVelyx MD mantém as unidades do arquivo: o estilo `units` do LAMMPS (real, metal, lj, si …) do dump ou do log,
Å e ps nos arquivos do GROMACS, CHARMM, NAMD e AMBER lidos pelo MDAnalysis, Å e eV nos arquivos de DFT. As
planilhas mandadas ao SciVelyx Graphs levam as unidades no cabeçalho das colunas.

## Gravar frames

**File ▸ Export frames** (Ctrl+E) grava os frames depois do pipeline de modificadores como dump do LAMMPS, arquivo
data do LAMMPS (com ligações e rótulos de tipos), XYZ estendido ou PDB. Qualquer célula é gravada como célula
triclínica restrita do LAMMPS.

## Que bibliotecas os leem

Os leitores do LAMMPS, do ReaxFF, do XYZ e do `.cell` do CASTEP são do próprio SciVelyx MD. Os arquivos do GROMACS,
CHARMM/NAMD, AMBER, MOL2 e GSD são lidos pelo MDAnalysis; PDB, CIF, XYZ estendido, VASP, Quantum ESPRESSO, saídas
do CASTEP, FHI-aims e cube, pelo ASE. Cada formato é conferido nos testes com arquivos de teste oficiais ou
gravados pelo próprio programa, lidos de novo por leitores independentes.
