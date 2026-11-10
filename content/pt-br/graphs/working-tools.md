# Assistente de gráficos, janelas e apresentações

A versão 0.17 trouxe as últimas ferramentas do SciDAVis e do QtiPlot que o SciVelyx Graphs ainda não tinha. Elas
agilizam o trabalho do dia a dia com muitas planilhas e gráficos.

## Assistente de gráficos

**Graph → Plot wizard…** monta um gráfico curva a curva, sem selecionar colunas na planilha antes.

1. Escolha a **planilha** e o **tipo** (linha, linha + símbolo, dispersão, barras de erro, degraus, colunas, área,
   hastes).
2. Clique numa coluna e depois em **↔ X**. Faça o mesmo para **↔ Y**, e para **↔ x error** ou **↔ y error** se a
   curva tiver barras de erro.
3. Clique em **New curve →**. O X continua escolhido, então a próxima curva só precisa de um Y novo.
4. Escolha *in a new graph* (num gráfico novo) ou *in the active panel* (no painel ativo) e clique em **Plot**.

Curvas com coluna de erro são desenhadas com barras de erro.

![O assistente de gráficos com duas curvas]({{AROOT}}assets/img/plot-wizard.webp){: width="720" height="460" loading="lazy" }

## Curvas e ordem de desenho

- **Hide other curves** e **Show all curves** (ocultar as outras curvas, mostrar todas) estão no menu do botão
  direito de uma curva e no menu Graph.
- **Edit → Bring to front** (Ctrl+Shift+]) e **Send to back** (Ctrl+Shift+[) mudam a ordem de desenho do texto,
  forma, imagem ou curva selecionados. Também estão no menu do botão direito.
- **Series → Data → Rows (first; last)** desenha uma curva com só parte da planilha, por exemplo `11; 60`.

## Novas opções de gráfico

- **Quebra de eixo com outra escala depois dela.** Na seção *Axis break* do painel, escolha *Scale after the x
  break* (ou y) = logarítmica para um início linear seguido de décadas. Você também pode definir os passos principais
  de cada lado (`antes; depois`) e a posição da quebra ao longo do eixo.
- **Suavização de serrilhado:** Figure → *Anti-aliasing*, ou Panel → *Anti-aliasing* para um painel.
- **Imagem como símbolo:** Series → Symbol → *Picture as the symbol* (um PNG, JPEG…). A altura da imagem segue o
  tamanho do símbolo.
- **Barras de erro por cima dos símbolos:** Series → Error bars → *Through the symbol*.
- **Pizza 3D:** Series → Pie → *3D pie*, com inclinação e espessura.
- **Modo rápido:** Series → Line → *Speed mode*. Curvas mais longas que o número de pontos dado são simplificadas
  pelo algoritmo de Douglas–Peucker. A tolerância é uma fração da faixa dos dados, e as lacunas são mantidas.
- **Eixos 3D logarítmicos:** num painel 3D, *Logarithmic axes* = x, y, z ou qualquer combinação.

![Escala logarítmica depois de uma quebra de eixo, e uma pizza 3D]({{AROOT}}assets/img/break-pie.webp){: width="1600" height="1000" loading="lazy" }

## Zoom e arrasto ao longo de um eixo

**View → Zoom and drag** tem *Zoom horizontally*, *Zoom vertically*, *Drag canvas horizontally* e *Drag canvas
vertically*: o outro eixo fica como está. *Normal pointer* encerra o modo. Para manter o resultado como limites dos
eixos, use **Lock zoom/pan as limits**.

## Projetos e janelas

- **File → Append project…** acrescenta ao projeto aberto as planilhas, gráficos, notas, pastas e scripts de outro
  projeto. O projeto pode vir do SciVelyx, do SciDAVis, do QtiPlot ou do exportador do Origin. Planilhas cujo nome já
  está em uso são renomeadas, e os gráficos seguem os novos nomes.
- **File → Save window as project…** salva o gráfico ativo só com os dados que ele usa, inclusive as planilhas das
  quais suas análises foram calculadas, como um projeto próprio.
- **File → All graphs as a presentation (.odp)…** grava um slide por gráfico, com o nome do gráfico como título. O
  arquivo abre no LibreOffice Impress e no PowerPoint.
- O menu **Window** lista todos os gráficos, planilhas e matrizes. **Next window** (Ctrl+PgDown) e **Previous window**
  (Ctrl+PgUp) passam pelos gráficos. **Open graph in a separate window** mostra o gráfico ativo numa janela própria,
  redesenhada a cada mudança; *Tile separate windows* as arruma lado a lado.

![Um gráfico numa janela separada]({{AROOT}}assets/img/separate-window.webp){: width="700" height="340" loading="lazy" }

## Suas próprias ações de menu e formulários

- **Scripts → Add custom script action…** coloca um de seus arquivos Python em **Scripts → Custom actions** e numa
  barra de ferramentas, com um atalho de teclado opcional. As ações são mantidas entre as sessões.
- **Scripts → Open custom interface (.ui)…** mostra um formulário feito no Qt Designer. Para que ele faça alguma
  coisa, carregue-o a partir de um script:

```python
w = load_ui("normalize.ui")
w.runButton.clicked.connect(lambda: print(table(w.sheetEdit.text())["y"].max()))
w.show()
```

Os widgets do formulário ficam disponíveis pelos seus nomes de objeto.

## Diagrama de ramo-e-folhas

Selecione uma coluna numérica e escolha **Analysis → Stem-and-leaf plot**. A exibição vai para as notas do projeto e
para o painel Messages, e um gráfico de texto é criado. A unidade das folhas é escolhida para haver cerca de √n ramos.
Em scripts, `scivelyx.core.extras17.stem_leaf(values, leaf_unit=1, split=2)` divide cada ramo em duas linhas.

## Pequenas coisas

- **Edit → Copy status bar text**, ou botão direito na barra de status.
- **Help → Search for updates…** lê um pequeno arquivo neste site com o número da versão mais recente. Nada sobre
  você ou seu computador é enviado.
