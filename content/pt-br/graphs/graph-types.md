# Tipos de gráfico do Origin

**Graph → Origin graph types** tem uma entrada para cada tipo de gráfico dos capítulos *Basic 2D*, *Bar, Column*,
*Pie, Doughnut*, *Area*, *Multi-axis, multi-panel* e *Statistical* do Origin, com os nomes do próprio Origin; desde a
0.20, também os capítulos *Specialized*, *Financial*, *3D XYY*, *3D surfaces*, *3D symbol, bar, vector*, *Contour*,
*Waterfall, grouped, image* e *Map*; e desde a 0.21, os *Apps* de gráficos do Origin — 176 tipos ao todo.

Para fazer um:

1. Selecione as colunas na planilha (Ctrl+clique nos cabeçalhos), na ordem dada pela tabela abaixo.
2. Escolha o tipo em **Graph → Origin graph types**.

Alguns tipos precisam de números que não estão na sua planilha, como médias e intervalos de confiança, densidades
por kernel, estatísticas de caixas, porcentagens ou os polígonos de um diagrama de Sankey. Esses números são
calculados e guardados em pequenas planilhas auxiliares com o nome da sua planilha. O gráfico é um gráfico comum:
toda curva, eixo, texto e cor pode ser editado, e as planilhas auxiliares podem ser inspecionadas ou exportadas.

![Violino com caixa]({{AROOT}}assets/img/violin-box.webp){: width="1600" height="1000" loading="lazy" }

## Basic 2D

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Scatter Central | x e y |
| Column Scatter | uma coluna por grupo |
| Error Band | x, y e o erro |
| Scatter + Rug | x e y |
| Line Series | duas ou mais colunas; cada linha vira uma linha atravessando-as |
| Row-wise (each row a curve) | as colunas; os nomes delas são os valores de x, se numéricos |
| Before and After | as colunas 'antes' e 'depois' |
| 2 Point Segment | x e y; as linhas 1–2, 3–4, … são ligadas |
| 3 Point Segment | x e y; as linhas 1–3, 4–6, … são ligadas |
| Spline Connected | x e y |
| Lollipop | categorias (ou x) e valores |
| Density Dots | x e y |
| Color Dots | x, y e opcionalmente a coluna que define a cor |
| Colormapped Line Series | x e duas ou mais colunas y |
| Stacked Lines by Y Offsets | x e duas ou mais colunas y |

## Bar, Column

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Column + Label | categorias (ou x) e valores |
| 100% Stacked Column | categorias e duas ou mais colunas de valores |
| 100% Stacked Bar | categorias e duas ou mais colunas de valores |
| Kite Diagram | posição ao longo do transecto, depois uma coluna por espécie/categoria |

## Pie, Doughnut

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| 3D Color Pie Chart | categorias e valores |
| Pie of Pie | categorias e valores |
| Bar of Pie | categorias e valores |
| Doughnut of Pie | categorias e valores |
| Doughnut with Total | categorias e valores |
| Pie with Different Radius | categorias, valores (ângulo) e raio |
| Doughnut with Different Radius | categorias, valores (ângulo) e raio |

## Area

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| 100% Stacked Area | x e duas ou mais colunas de valores |
| Fill Area with 2 Colors | x, y e opcionalmente um segundo y (senão y = 0) |

## Multi-axis, multi-panel

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Double-Y Column | x (ou categorias), y da esquerda, y da direita |
| 2Ys Column | x (ou categorias), y da esquerda, y da direita |
| Double-Y Column – Line Symbol | x (ou categorias), colunas, linha |
| 2Ys Y-Y (Double Y) | x, y da esquerda, y da direita |
| 3Ys Y-YY | x e três colunas y (uma à esquerda, duas à direita) |
| 3Ys Y-Y-Y | x e três colunas y (duas à esquerda, uma à direita) |
| 4Ys Y-YYY | x e quatro colunas y (uma à esquerda, três à direita) |
| 4Ys YY-YY | x e quatro colunas y (duas à esquerda, duas à direita) |
| Multiple Y Axes | x e de 2 a 7 colunas y, cada uma com seu eixo |
| 9 Panel | x e até nove colunas y |
| Multiple Panels by Label | a coluna de rótulos (grupo), x e y |
| Double X | x1, y1, x2, y2 (o segundo par usa o eixo x de cima) |

## Statistical

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Interval Plot | uma coluna por grupo |
| Bar Chart (mean ± SD) | uma coluna por grupo |
| Bar Overlap | uma coluna por grupo |
| Bar Normal | uma coluna por grupo |
| Box Overlap | uma coluna por grupo |
| Box Normal | uma coluna por grupo |
| Half Box | uma coluna por grupo |
| Scatter Interval | uma coluna por grupo |
| Marginal Box Charts | x e y |
| Beeswarm | uma coluna por grupo |
| Histogram + Rug | uma coluna |
| Histogram + Probabilities | uma coluna |
| Multi-Panel Histograms | duas ou mais colunas |
| Distribution (+ Rug) | uma coluna |
| Histogram with Labels | uma coluna |
| Population Pyramid | faixas etárias, valores da esquerda (p. ex. homens), valores da direita |
| Marginal Plots (grouped) | x, y e a coluna de grupos |
| Violin with Box | uma coluna por grupo |
| Violin with Point | uma coluna por grupo |
| Violin with Quartile | uma coluna por grupo |
| Violin with Stick | uma coluna por grupo |
| Split Violin | as duas colunas comparadas (metade esquerda e direita) |
| Half Violin | uma coluna por grupo |
| Ridgeline | duas ou mais colunas (uma crista cada) |
| QC (X-bar R) Chart | uma coluna de medidas |
| Bland–Altman | os dois métodos (A e B) |
| 2Ys Box Chart | duas colunas com escalas diferentes |
| Parallel Plot | colunas numéricas (opcionalmente uma coluna de grupos primeiro) |
| Parallel Index | colunas numéricas numa escala comum (opcionalmente um grupo primeiro) |
| Parallel Sets | colunas categóricas (opcionalmente uma coluna de pesos por último) |
| Alluvial | colunas categóricas (opcionalmente uma coluna de pesos por último) |
| Sankey | origem, destino e valor |
| Network Plot | origem, destino e opcionalmente o peso |
| Chord Diagram | origem, destino e valor |
| Hierarchical Edge Bundling | origem e destino (nomes 'grupo.nó') |
| Probability Plot | uma coluna |
| Stacked Dot Plot | uma ou mais colunas |
| Interaction Plot | resposta, fator A (eixo x), fator B (linhas) |
| Main Effects Plot | resposta e um ou mais fatores |
| Multi-Vari Chart | resposta, fator A (painéis de pontos), fator B |
| Variability Chart | resposta, fator A, fator B |
| Symmetry Plot | uma coluna |
| Run Chart | uma coluna em ordem temporal |
| CDF Plot | uma ou mais colunas |
| Cause-and-Effect (Ishikawa) | categoria e causa (colunas de texto) |
| Frequency Chart | uma coluna (valores ou textos) |
| Grouped Histogram | valor e grupo |
| Grouped Scatter | x, y e grupo |
| Grouped Pareto | grupo, categoria e valor |

## Specialized

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Bullet Chart | categoria, valor, meta, depois de 1 a 3 limites de faixas |
| Polar Contour + Gradient Vector | ângulo (graus), raio e valor |
| Contour Line + Gradient Vector | x, y e z numa grade |
| Piper (Trilinear) Diagram | Ca, Mg, Na+K, Cl, SO4, HCO3+CO3 (meq/L) |
| Durov Diagram | Ca, Mg, Na+K, Cl, SO4, HCO3+CO3 (meq/L) |
| Stiff Diagram | nome da amostra, Na, Ca, Mg, Cl, HCO3, SO4 (opcionalmente Fe, CO3) |
| Polar Vector θrθr | ângulo inicial (°), raio inicial, ângulo final (°), raio final |
| Polar Vector θRAM | ângulo (°), raio, direção (°), módulo |
| Compass Plot | componentes x e y (setas a partir do centro) |
| Radial Bar | categoria e valor |
| Radial Stacked Bar | categoria e dois ou mais valores |
| Right-Triangle Ternary | A, B e C (qualquer escala) |
| Stacked Radial Plot | categoria e dois ou mais valores |
| Ternary Vector | A, B, C iniciais e A, B, C finais |
| Wind Rose (binned data) | direção (°), depois uma coluna de frequências por classe de velocidade |
| Wind Rose (raw data) | direção (°) e velocidade |
| Window-view Browser Graph | x e y |

## Financial

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Bridge (Waterfall) Chart | categoria e variação |
| Horizontal Bridge Chart | categoria e variação |
| Stacked Bridge Chart | categoria e duas ou mais variações |
| Stacked Bridge Chart with Total | categoria e duas ou mais variações |
| High-Low-Close | data/x, máxima, mínima, fechamento |
| OHLC-Volume | data/x, abertura, máxima, mínima, fechamento, volume |
| Line (stock) | data/x, fechamento e opcionalmente volume |

## 3D XYY

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| XYY 3D Bars | x (ou categorias) e uma ou mais colunas y |
| 3D Side by Side Bars | x (ou categorias) e duas ou mais colunas y |
| 3D Stacked Bars | x (ou categorias) e duas ou mais colunas y |
| 3D 100% Stacked Bars | x (ou categorias) e duas ou mais colunas y |
| 3D Bars with Error Bar | x, depois pares de y e seu erro |
| 3D Wall | x e uma ou mais colunas y |
| Stacked Wall | x e duas ou mais colunas y |
| 100% Stacked Wall | x e duas ou mais colunas y |

## 3D surfaces

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Color Fill Surface | x, y e z numa grade |
| X and Y Constant with Base | x, y e z numa grade |
| 3D Ternary Colormap Surface | A, B, C (frações) e z |
| Surface with Error Bar (color fill) | x, y, z e o erro de z numa grade |
| Surface with Error Bar (colormap) | x, y, z e o erro de z numa grade |
| Multiple Surfaces | x, y e duas ou mais colunas z numa grade |
| 3D Stacked Surfaces | x, y e duas ou mais colunas z numa grade |
| 3D Stacked Heatmaps | x, y e uma ou mais colunas de valores numa grade |

## 3D symbol, bar, vector

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| 3D Scatter with Z Error | x, y, z e o erro de z |
| 3D Bars with Categorical XY | x (texto ou números), y (texto ou números), z |
| 3D Stacked Bars (XYZ) | x, y e duas ou mais colunas z |
| 3D 100% Stacked Bars (XYZ) | x, y e duas ou mais colunas z |
| 3D Floating Bars | x, y, z inicial e z final |
| 3D Vector XYZ XYZ | x, y, z iniciais e x, y, z finais |
| 3D Vector XYZ dXdYdZ | x, y, z e as componentes dx, dy, dz |

## Contour

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Contour – Categorical Z | x, y e uma coluna de texto (categoria) |
| Polar Heatmap | ângulo (°), raio e valor numa grade |
| Split Heatmap | x, y (números ou textos), valor 1 (triângulo superior), valor 2 |
| Heatmap with Split Tiles | x, y (números ou textos) e de 2 a 4 valores |
| Ternary Contour | A, B, C (frações) e valor |
| Overlaid Contour | x, y e duas colunas z numa grade |
| Ternary Overlaid Contour | A, B, C (frações) e dois valores |

## Waterfall, grouped, image

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Waterfall Color Mapped by Y | x e duas ou mais colunas y |
| Waterfall Color Mapped by Z | x e duas ou mais colunas y (nomes numéricos = z) |
| 3D Waterfall | x e duas ou mais colunas y |
| Grouped Column (by two factors) | fator A (grupos), fator B (barras), valor |
| Grouped Box (by two factors) | fator A (grupos), fator B (caixas), valor |
| Grouped Line + Symbol | x (ou fator A), grupo, valor |
| Grouped Scatter (index by two factors) | fator A, fator B, valor |
| Image + Profiles | x, y e z numa grade |

## Map

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Pie Map | x, y, depois dois ou mais valores (uma pizza por linha) |
| Bar Map | x, y, depois um ou mais valores (um grupo de barras por linha) |

## Apps (0.21)

Os Apps de gráficos do Origin que desenham um tipo novo de gráfico. Os outros Apps (Graph Maker, Batch Plotting,
Common Bar Width, Layer Stack Manager, Color Editor, LaTeX) são ferramentas em **Graph → Apps**; veja
[Apps do Origin](../origin-apps/).

| Tipo de gráfico | Colunas a selecionar |
|---|---|
| Nyquist Plot (with Bode) | frequência, Z′ (real) e Z″ (imaginária) |
| Polar Contour Profile | ângulo (°), raio e valor |
| Means Plot | uma coluna por grupo |
| Paired Comparison Plot | as duas colunas pareadas (antes, depois) |
| Volcano Plot | log2 da razão (fold change), valor p e opcionalmente uma coluna de rótulos |
| Rectangle and Ellipse Profile | x, y e z (numa grade ou espalhados) |
| Plot Sub Matrix | x, y e z numa grade |
| Color Spectrum Plot | comprimento de onda (nm) e intensidade |
| Chromaticity Diagram (CIE 1931) | cromaticidades x e y, ou valores triestímulo X, Y, Z |
| Hansen Solubility Parameter Plot | δD, δP, δH, bom (1) ou ruim (0), nome do solvente opcional |
| Ternary Contour Profile | A, B, C (frações) e valor |
| Kernel Density (Ternary) | A, B e C |
| Kernel Density (Polar) | ângulo (°) e raio |
| Soil Texture Triangle (USDA) | areia, silte e argila (%) |
| Sediment Classification (Folk) | areia, silte e argila (%) |
| Taylor Diagram | referência (observações), depois uma coluna por modelo |
| 3D Polar Strain Map | ângulo (°), raio e deformação (numa grade polar) |
| 3D Wind Rose | direção (°) e velocidade |
| Isosurface | x, y, z (numa grade 3D) e o valor |
| 3D Wall Profile | x, y e z numa grade |
| Zoomed Inset | x e um ou mais y |
| Zoomed Inset Plus (two or three zooms) | x e um ou mais y |
| Venn Diagram | duas ou três colunas de itens (um item por célula) |

## As novas ferramentas de desenho por trás deles

- **Polígonos preenchidos:** um tipo de curva cujos polígonos são separados por linhas vazias, cada um com sua cor
  ou com um mapa de cores. Pipas (kites), violinos, ligações de Sankey e cordas o usam.
- **Segmentos de linha:** linhas interrompidas nas linhas vazias, para tapetes (rugs), pares antes/depois e gráficos
  paralelos.
- **Linha com mapa de cores:** uma linha colorida por uma terceira coluna.
- **Polígonos 3D, segmentos 3D, vetores 3D e mapas de calor 3D planos** (0.20): barras 3D, paredes, barras de erro,
  vetores com uma coluna *w*, e mapas de calor empilhados em alturas diferentes.
- **Polígonos 3D iluminados e novos mapas de cores** (0.21): isossuperfícies são sombreadas por uma luz; o mapa de
  cores *visible_spectrum* e os seus próprios mapas de cores (Graph → Apps → Color editor) aparecem em toda lista de
  mapas de cores.
- **Eixos extras:** nas propriedades da série, *Y axis* pode ser do 2º ao 4º eixo da direita, o 2º ou 3º eixo da
  esquerda (deslocado e com a cor da curva), ou o eixo X de cima (Double X).

![Diagrama de Sankey]({{AROOT}}assets/img/sankey.webp){: width="1600" height="1000" loading="lazy" }

![Quatro eixos Y]({{AROOT}}assets/img/four-axes.webp){: width="1600" height="1000" loading="lazy" }

![Ridgeline]({{AROOT}}assets/img/ridgeline.webp){: width="1600" height="1000" loading="lazy" }

![Diagrama de Piper]({{AROOT}}assets/img/piper.webp){: width="1600" height="1000" loading="lazy" }

![Rosa dos ventos]({{AROOT}}assets/img/wind-rose.webp){: width="1600" height="1000" loading="lazy" }

![Gráfico de ponte]({{AROOT}}assets/img/bridge.webp){: width="1600" height="1000" loading="lazy" }

![Barras 3D empilhadas a 100 %]({{AROOT}}assets/img/bars3d.webp){: width="1600" height="1000" loading="lazy" }

![Contorno ternário]({{AROOT}}assets/img/ternary-contour.webp){: width="1600" height="1000" loading="lazy" }
