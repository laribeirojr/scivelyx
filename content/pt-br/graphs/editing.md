# Editando gráficos

Uma figura é feita de **painéis** (linhas e colunas de eixos) que contêm **séries** (curvas, barras, mapas…), textos,
formas e uma legenda. Tudo o que você vê está ligado a um elemento editável.

## O que um duplo clique abre

| Elemento clicado | O que você pode mudar |
|---|---|
| Títulos, títulos dos eixos, textos | Texto com paleta de símbolos, 37 letras gregas, subscritos e sobrescritos, negrito ou itálico parcial, fonte, tamanho, cor, rotação, moldura e fundo, com pré-visualização. Notação matemática inválida é apontada antes de chegar à figura. |
| Números ou linha do eixo | Escala (linear, log, symlog, logit, asinh), limites, inversão; marcas por passo, por número ou em posições explícitas com rótulos (Γ, X, M…); formato dos números (científico ×10ⁿ, fixo, percentual, engenharia, personalizado), prefixo, sufixo, fórmula, texto de uma tabela, nomes dos dias e dos meses, data/hora; linha do eixo; grade. |
| Curva, símbolos, barras, mapas | Tipo e colunas; linha (tracejado, pontas, spline, degraus, ligar sobre dados faltantes); símbolos (cheios, meio cheios, vazados, a cada N pontos); preenchimento sob a curva; barras de erro (mais e/ou menos) ou uma banda de erro; rótulos de dados (também de uma coluna de texto); faixas de caixa e bigodes; rótulos e anel de pizza; pontas de vetores; mapa de cores, níveis e rótulos de contornos; estilos 3D. |
| Legenda | Posição (também livre), colunas, título, fonte, moldura, transparência, ordem, entradas. |
| Barra de cores | Título, marcas e formato, mapa, normalização, posição, tamanho. |
| Fundo do painel | Projeção (2D, 3D, polar, ternária, Smith), fundo, proporção, grade (também por cima dos dados), vista 3D, zoom e resolução. |
| Fora dos painéis | A figura: revista, tamanho em mm, DPI, linhas e colunas de painéis, espaçamento, fonte base, fonte matemática, folhas de estilo do Matplotlib, ciclo de cores, rótulos (a)/(b), título geral. |

![O diálogo do eixo]({{AROOT}}assets/img/axis-dialog.webp){: width="835" height="900" loading="lazy" }

## Mouse e teclado

| Ação | Resultado |
|---|---|
| Um clique | Seleciona o elemento; o explorador de objetos acompanha. |
| Botão direito | Menu do elemento: propriedades, ocultar, duplicar, apagar, destacar um ponto, inserir texto ou uma linha. |
| Arrastar a legenda ou um texto | Move-o (a posição é guardada). |
| Arrastar um painel 3D | Gira-o (elevação e azimute são guardados). |
| Delete / Ctrl+Z / Ctrl+Y | Apaga o elemento selecionado / desfaz / refaz. **Edit → Undo history** lista cada passo. |
| Ctrl+Alt+C / Ctrl+Alt+V | Copia e cola o formato entre séries, eixos, textos, legendas ou formas. |
| Alt+Enter | Propriedades do elemento selecionado. |

## Painéis e layout

A aba **Layout** adiciona e remove colunas e linhas de painéis, define a projeção, compartilha x ou y entre painéis,
quebra um eixo (marcas `//`, a faixa omitida) e adiciona um **eixo secundário** com conversão de unidades (eV↔nm,
cm⁻¹↔nm, eV↔cm⁻¹, eV↔THz, K↔°C, rad↔graus, Hartree e Rydberg→eV, a·x+b, a/x). **Insert → Zoom (inset)** cria um
detalhe ampliado da região que você arrastar. **Format → Several curves** oferece cascata (waterfall), painéis
empilhados, símbolos e tracejados variados, matriz de dispersão e histogramas marginais.

## Desenho e anotação

**Insert**: texto (clique onde ele vai), seta com texto, linhas horizontais e verticais, faixas de referência,
retângulo, elipse, linha, seta, polígono, curva à mão livre, imagem, legenda, barra de cores, rótulos de painéis
(a)(b) e título da figura; **Graph → Equation…** (notação LaTeX) e **Date and time stamp** (carimbo de data e hora).
**Insert → Data reader** (Ctrl+Shift+R) mostra as coordenadas do ponto mais próximo; um duplo clique o anota.

## Ferramentas de dados no gráfico

**Graph → Data tools**: mover pontos com o mouse (a planilha muda junto), arrastar uma curva inteira, remover pontos
ruins com um clique (a linha é mascarada), selecionar a faixa usada por ajustes e operações, e ler coordenadas livres.
Tudo pode ser desfeito.

## Temas e modelos

**Format → Save theme…** guarda a aparência de uma figura (fontes, tamanhos, cores, marcas, grade); **Apply theme…** e
o **Theme organizer** (com pré-visualização do gráfico atual) a reaproveitam. **Save as template** guarda um gráfico
inteiro, inclusive os tipos das curvas; **Graph from template** monta um novo com outras colunas.

## 3D

Linha, dispersão, superfície, malha, superfície triangulada, contorno, barras e fitas em 3D, e os estilos do
SciDAVis/QtiPlot (superfície com malha, linhas ocultas, polígonos, pontos, cruzes, cones). As superfícies vêm de
matrizes, de colunas x, y, z, de uma função z = f(x, y) ou de uma definição paramétrica x(u,v), y(u,v), z(u,v).
**Graph → 3D rotation animation…** grava um GIF (ou MP4, com o ffmpeg).
