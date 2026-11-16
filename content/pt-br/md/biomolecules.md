# Biomoléculas

**Analysis ▸ Biomolecules** reúne as análises de proteínas e ácidos nucleicos. Elas precisam dos nomes, dos
resíduos e (algumas) das ligações de uma topologia: abra um `.tpr` do GROMACS, um `.psf` do CHARMM/NAMD, um
`.prmtop` do AMBER ou um PDB junto com a trajetória. As moléculas são refeitas inteiras através da fronteira
periódica, ao longo das ligações, antes do ajuste.

| Análise | O que dá | Como |
|---|---|---|
| RMSD | depois do ajuste por mínimos quadrados de um grupo (a cadeia principal, por padrão), para o grupo do ajuste e outros grupos, ponderado pela massa se você pedir | `gmx rms`, a ferramenta de RMSD do VMD |
| RMS fluctuation | por átomo e por resíduo | `gmx rmsf` |
| Radius of gyration | com as componentes x, y e z | `gmx gyrate`, `measure rgyr` |
| Hydrogen bonds | por frame e a ocupação de cada trio doador–hidrogênio–aceitador, periódico | MDAnalysis |
| Secondary structure (DSSP) | hélice, folha ou alça por resíduo e frame, como frações e como linha do tempo | DSSP |
| Solvent accessible area | Shrake–Rupley, por átomo, resíduo e frame | `gmx sasa` |
| Principal component analysis | autovalores, autovetores, projeções das posições ajustadas | `gmx covar` |
| Salt bridges | oxigênios de ASP/GLU a até 3,2 Å de nitrogênios de LYS/ARG (HIS opcional), ocupação e distâncias no tempo | Salt Bridges do VMD |
| Contact map | distância e fração em contato de cada par de resíduos (átomos pesados mais próximos, átomos mais próximos ou CA), contatos no tempo | os contatos do MDTraj |
| Per-residue timeline | mapas de calor resíduo × tempo de estrutura secundária, RMSD, SASA, contatos, ligações de hidrogênio ou pontes salinas | Timeline do VMD |

![RMSD da cadeia principal da adenilato quinase depois do ajuste ao primeiro frame]({{AROOT}}assets/md/rmsd.webp)

![Pontes salinas da adenilato quinase: a ocupação de cada par ao longo da trajetória]({{AROOT}}assets/md/salt-bridges.webp)

![O mapa de contatos entre resíduos: a fração dos frames em que dois resíduos estão a menos de 4,5 Å]({{AROOT}}assets/md/contact-map.webp)

![A linha do tempo da estrutura secundária por resíduo: hélice, folha e alça de cada resíduo em cada frame]({{AROOT}}assets/md/timeline.webp)

## Seleções

As janelas aceitam seleções na linguagem da vista 3D, com as macros `protein`, `backbone`, `sidechain`, `water`,
`ions`, `hydrogen` e `heavy` (os mesmos átomos do MDAnalysis), e colunas como `resname`, `resid`, `segid`, `name`:
`protein and name == "CA"`, `resid >= 122 and resid <= 159`.

## Pelo terminal e em Python

```bash
scivelyx-md rmsd md.xtc --topology topol.tpr --fit backbone
scivelyx-md dssp md.xtc --topology topol.tpr --strings dssp.txt
scivelyx-md saltbridges md.xtc --topology topol.tpr --table pontes.csv
scivelyx-md contacts md.xtc --topology topol.tpr --cutoff 4.5 --scheme closest-heavy
scivelyx-md timeline md.xtc --topology topol.tpr --quantity rmsd
```

```python
t = load("md.xtc", topology="topol.tpr")
sb = salt_bridges(t)
print(sb.pairs.head())          # ácido, base, ocupação, distância O–N média e mínima
send(timeline(t, "ss"))
```

## Como foram conferidas

Nos arquivos de teste oficiais do MDAnalysis (adenilato quinase como PSF + DCD do CHARMM e como TPR + XTC do
GROMACS em água): RMSD, RMSF, raio de giro, ligações de hidrogênio, DSSP e PCA iguais aos do MDAnalysis; RMSD, RMSF,
SASA (a 0,3 %) e DSSP (97 % dos estados) comparados com o MDTraj; pontes salinas comparadas par a par com o
MDAnalysis; distâncias entre resíduos iguais ao `compute_contacts` do MDTraj nos seus três esquemas.
