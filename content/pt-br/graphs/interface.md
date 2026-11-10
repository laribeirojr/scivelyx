# A janela

Este capítulo mostra as partes da janela do programa e para que serve cada uma. Os outros capítulos se referem a elas
pelos nomes usados aqui.

## A tela inicial

O SciVelyx Graphs abre na tela inicial.

![A tela inicial: ações à esquerda, a galeria de exemplos à direita]({{AROOT}}assets/manual/start-screen.png)

- **New sheet**, **Open data…** e **Open project…** (nova planilha, abrir dados, abrir projeto) começam o trabalho
  de sempre. Você também pode arrastar arquivos de dados ou projetos para a janela.
- **Data from GitHub…** lê um arquivo direto de um repositório do GitHub.
- **Function plot…** desenha y = f(x), uma curva paramétrica ou uma superfície sem nenhum dado.
- **Recent** lista os últimos projetos. Um clique abre um deles.
- **Start from an example** (começar de um exemplo) abre uma figura pronta, com seus dados, como um projeto comum.
  Todo elemento pode então ser editado; por isso os exemplos também servem de modelos.

A galeria tem dois grupos. Os dez primeiros exemplos usam dados analíticos ou sintéticos. Os catorze seguintes
recriam tipos de figura de cinco artigos de 2026 de colegas da Universidade de Brasília:

- difração de raios X, curvas de magnetização e espectros Mössbauer de quasicristais;
- o diagrama de fases e as curvas corrente–tensão de um supercondutor;
- deconvolução de DRX, um gráfico de Tauc e um histograma de tamanhos de nanopartículas de CeO₂;
- termogravimetria, gráficos de barras com marcas de significância e escores de PCA de amostras de dentina;
- perfis de profundidade e um diagrama FORC de um solo tropical.

Os dados desses exemplos são ilustrativos: foram feitos para se parecer com as figuras publicadas, e a nota de cada
conjunto de dados diz isso. **Help → Start page** (Ctrl+Shift+H) volta a esta tela.

## A janela de trabalho

![A janela de trabalho com uma figura de exemplo]({{AROOT}}assets/manual/workspace.png)

| Parte | Onde | Para que serve |
|----------|----------|------------------------------------------------------------|
| Menus | linha de cima | Todos os comandos do programa, agrupados como no Origin: File, Edit, View, Graph, Matrix, Scripts, Format, Analysis, Insert, Layout, Sheet, Examples, Window, Help. |
| Faixa de opções | abaixo dos menus | Os comandos mais usados como botões, em abas: Home, Sheet, Matrix, Graphs, Analysis, Format, Insert, Layout. |
| Project | esquerda | Planilhas, matrizes, gráficos e pastas do projeto. Duplo clique abre um item; o botão direito cria pastas e move itens. |
| Abas de gráficos | meio | Uma aba por gráfico. Cada gráfico tem seu próprio histórico de desfazer. A aba **+** cria um gráfico. |
| Barra do gráfico | acima da figura | Início, voltar e avançar, mover, zoom, ajustes dos subgráficos, limites dos eixos, salvar. **Zoom** muda a escala da página na tela (não muda o tamanho exportado). |
| Figura | meio | A página como será exportada. A linha abaixo dela mostra o tamanho final em milímetros, o tamanho da fonte e a resolução das imagens. |
| Properties | direita | O explorador de objetos (todo elemento da figura), o painel ativo e a lista de séries com seus dados. |
| Messages e Notes | embaixo | Resultados das análises e avisos; as notas são salvas com o projeto. |
| Barra de status | última linha | O que está selecionado e o que o mouse pode fazer agora. |

Os painéis podem ser fechados, movidos ou soltos com o mouse; o menu **View** os mostra de novo.

## Selecionar e editar

- **Clique** num elemento da figura (uma curva, um eixo, a legenda, um texto) para selecioná-lo. A barra de status
  diz o nome dele e o explorador de objetos o destaca.
- **Duplo clique** abre as propriedades.
- **Botão direito** abre um menu com as ações daquele elemento: propriedades, copiar e colar o formato, ocultar,
  apagar, trazer para a frente…
- **Arrastar** move textos, legendas, detalhes ampliados (insets) e objetos de desenho.
- **Delete** apaga o elemento selecionado; **Ctrl+Z** desfaz.

![Propriedades de uma curva: dados, linha, símbolo, preenchimento, barras de erro, rótulos, linhas de projeção e mapa de cores]({{AROOT}}assets/manual/properties-curve.png)

![Propriedades de um eixo: escala, limites, marcas, rótulos, grade e quebras]({{AROOT}}assets/manual/properties-axis.png)

## Planilhas

Os dados ficam em planilhas. Clique numa planilha no painel **Project**, ou no nome dela na aba **Data**, para vê-la.
As colunas têm um papel (X, Y, Z, erro…), um nome longo e unidades; fórmulas preenchem uma coluna a partir das
outras.

![Uma planilha: a primeira coluna é X e as outras são Y]({{AROOT}}assets/manual/sheet.png)

O capítulo [Planilhas e dados](../sheet/) explica a importação, as fórmulas, as máscaras e as operações de planilha.

## Teclado

| Tecla | Ação |
|------------------------------|----------------------------------------------|
| F1 | Resumo das ações do mouse e do teclado |
| Ctrl+N, Ctrl+O, Ctrl+S | Novo projeto, abrir, salvar |
| Ctrl+Z, Ctrl+Shift+Z (Ctrl+Y no Windows) | Desfazer, refazer (no gráfico ativo) |
| Ctrl+T | Novo gráfico |
| Ctrl+E | Exportar a figura |
| Ctrl+Shift+C | Copiar a figura como imagem |
| Ctrl+Alt+C, Ctrl+Alt+V | Copiar e colar o formato de um elemento |
| Ctrl+G | Dados do GitHub |
| Delete | Apagar o elemento selecionado |
| Ctrl+Shift+H | Tela inicial |
| Ctrl+Shift+P | Janela de scripts |
