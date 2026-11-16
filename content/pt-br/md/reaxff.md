# ReaxFF

Uma simulação ReaxFF do LAMMPS grava as ordens de ligação de cada átomo com `fix reaxff/bonds` e, se você quiser,
as moléculas com `fix reaxff/species`. O SciVelyx MD lê os dois, normais ou compactados com gzip, e monta
moléculas, espécies e reações a partir das ordens de ligação, com o corte que você escolher para cada par de
elementos.

## Abrir uma simulação

Abra juntos o dump, o log e o arquivo de ligações. O arquivo de ligações é ligado ao dump dos mesmos átomos: a vista
3D desenha suas ligações, e a tabela ganha as colunas `abo` (soma das ordens de ligação), `nlp` (pares isolados),
`nbonds`, `molecule` e `species`. Os elementos vêm da linha `pair_coeff * * ffield C H O` do log, ou da coluna de
elementos do dump.

![Uma simulação ReaxFF de CH4 + O2 no meio da combustão, colorida pela carga]({{AROOT}}assets/md/reaxff-3d.webp)

## Análises (Analysis ▸ ReaxFF)

| Análise | O que dá |
|---|---|
| Elements, bond-order cutoff and timestep | os ajustes: um corte para todos os pares ou um por par de elementos (`C-H=0.4,O-O=0.65,default=0.3`), o passo de tempo para o eixo do tempo |
| Species from bond orders | o número de cada molécula no tempo (com os nomes que o LAMMPS dá), as mais frequentes no gráfico |
| Bonds by element pair and bond-order distribution | contagens de ligações por par no tempo, histogramas das ordens de ligação |
| Charges by element | a carga média e sua dispersão por elemento no tempo |
| Reaction events | quem reage com quem e quando (moléculas antigas e novas que compartilham átomos), com as contagens e a variação líquida de cada espécie |

Um arquivo do `fix reaxff/species` abre como tabela e gráfico próprios.

![Espécies no tempo, a partir das ordens de ligação da simulação de CH4 + O2]({{AROOT}}assets/md/reaxff.webp)

## Linha de comando

```bash
scivelyx-md species bonds.reaxff --elements "C H O" --cutoff "C-H=0.4,default=0.3"
scivelyx-md reactions bonds.reaxff --elements "C H O"
scivelyx-md bonds bonds.reaxff
scivelyx-md charges dump.lammpstrj
```

## Uma observação sobre o passo das espécies

As espécies que o `fix reaxff/species` do LAMMPS grava para o passo N são as moléculas das ordens de ligação do
passo N − 1. As espécies do SciVelyx MD pertencem ao passo do seu bloco no arquivo de ligações, então as duas
séries ficam deslocadas de um passo de saída. Os testes conferem que, levado em conta esse deslocamento, nossas
espécies são idênticas às do LAMMPS em cada um de 200 passos consecutivos.
