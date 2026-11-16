# Sua primeira análise

Este exemplo usa uma simulação real do LAMMPS que vem com o código do SciVelyx MD (`tests/data`): 27 moléculas de
água numa caixa periódica, gravadas num arquivo data (`water.data`), num dump de 5 frames (`water.lammpstrj`) e no
log (`water.log`). Qualquer simulação sua do LAMMPS funciona do mesmo jeito.

## 1. Abra a simulação

**File ▸ Open**, escolha os três arquivos juntos (ou solte-os na janela). O dump recebe os rótulos dos tipos, as
massas e as ligações do arquivo data dos mesmos átomos; o log vai para a aba **Thermodynamics**.

![A simulação de água na vista 3D, com as ligações do arquivo data e a tabela de átomos]({{AROOT}}assets/md/atoms-3d.webp)

- Percorra os frames com o controle deslizante ou o botão de tocar.
- Marque **bonds** para desenhar as ligações O–H do arquivo data.
- Escolha uma coluna em **Colour** (por exemplo `q`, a carga) para colorir os átomos por ela.
- Digite `type == 1` em **Select** para destacar os oxigênios.

## 2. Veja a termodinâmica

A aba **Thermodynamics** mostra as colunas do log em função do passo ou do tempo, uma curva por run do script de
entrada; escolha as grandezas à esquerda.

![A temperatura dos três runs do log, com a tabela da saída termodinâmica]({{AROOT}}assets/md/thermo.webp)

## 3. Calcule a função de distribuição radial O–H

**Analysis ▸ Radial distribution function** (Ctrl+R) pede os dois grupos de átomos, o raio de corte, o número de
intervalos, os frames e se os pares ligados contam:

![A janela da RDF]({{AROOT}}assets/md/rdf-dialog.webp)

Escolha o tipo 1 (O) e o tipo 2 (H), r max = 6 Å, 120 intervalos e, em *Bonded pairs*, **exclude 1-2 and 1-3
pairs**, com as ligações do arquivo data — como o LAMMPS faz com `special_bonds 0 0`. O pico O–H que sobra é a
ligação de hidrogênio entre moléculas. O resultado abre numa nova aba com g(r) e o número de coordenação acumulado
n(r):

![g(r) e n(r) dos pares O–H, na média dos cinco frames]({{AROOT}}assets/md/rdf.webp)

A normalização é a do `compute rdf` do LAMMPS; os testes do SciVelyx MD comparam os dois nos mesmos frames, até os
seis algarismos que o LAMMPS imprime.

## 4. Mande para o SciVelyx Graphs

**File ▸ Send to SciVelyx Graphs** (Ctrl+G) abre uma janela do SciVelyx Graphs com a planilha (r, g, n, com nomes
e unidades) e os dois gráficos. Tudo ali é editável: eixos, curvas, ajustes, exportação no tamanho da revista.

![A RDF aberta no SciVelyx Graphs]({{AROOT}}assets/md/graphs.webp)

**File ▸ Save as SciVelyx project** (Ctrl+S) grava o mesmo conteúdo num arquivo `*.scivelyx.json`.

## O mesmo pela linha de comando

```bash
scivelyx-md info water.lammpstrj
scivelyx-md thermo water.log -o thermo.scivelyx.json
scivelyx-md rdf water.lammpstrj --topology water.data --pair 1 2 --rmax 6 --bins 120 \
    --exclude-bonded 2 -o rdf.scivelyx.json --csv rdf.csv --png rdf.png
```

E em Python (View ▸ Python console and scripts, ou `scivelyx-md shell`):

```python
t = load("water.lammpstrj", topology="water.data")
g = rdf(t, 6, "1", "2", exclude_bonded=2)
print(g.r[g.g.argmax()])      # 1,53 Å: o pico da ligação de hidrogênio (pares ligados excluídos)
send(g)                       # para o SciVelyx Graphs
```
