# Matrizes e superfícies

Uma **matriz** é uma grade de valores z(x, y) com coordenadas para suas linhas e colunas — um mapa, uma imagem, um
espectro 2D ou uma superfície de energia potencial. As matrizes ficam no projeto ao lado das planilhas e têm sua
própria aba e menu **Matrix**.

## Criar uma matriz

- **Matrix → New matrix**: dimensões e o primeiro e o último x e y.
- **Matrix → Set values**: uma fórmula de `i`, `j`, `x`, `y`, do valor da célula e de outras matrizes, por exemplo
  `exp(-(x^2 + y^2))` ou `M1 - M2`.
- **Matrix → Import image**: uma imagem vira uma matriz de intensidades.
- **Sheet → Convert to matrix**: colunas x, y, z numa grade regular viram uma matriz; **Matrix → XYZ** faz o caminho
  de volta.
- **Matrix → 2D binning**: conta duas colunas num histograma 2D em forma de matriz.

## Operações

Dimensões e coordenadas, transpor, inverter, determinante, girar ±90°, espelhar na horizontal e na vertical, ampliar
(bilinear) e reduzir (média por blocos), suavizar, FFT 2D, um **perfil de linha** ao longo de uma reta que você
escolhe, **Show as image** com uma paleta (cinza, arco-íris, personalizada) e **Export image**. As saídas são
recalculadas quando a matriz muda. **Convert to table** grava a matriz como tabela, como XYZ ou como YXZ.

## Pontos espalhados → superfície

**Sheet → Surface from XYZ** transforma medidas x, y, z espalhadas numa superfície, por interpolação numa grade
(linear, cúbica, vizinho mais próximo, spline de placa fina) ou ajustando z = f(x, y) (plano, quadrática, gaussiana 2D
ou sua própria fórmula, com erros padrão e R²). Desenha um contorno, um mapa ou uma superfície 3D com os pontos medidos
por cima.

## Gráficos de matrizes

Contorno (linhas ou preenchido), mapa de calor (também com os valores nas células), superfície 3D, malha e os outros
estilos 3D, contornos projetados no chão e nas paredes de uma caixa 3D, e contornos polares. Matrizes do SciDAVis e do
QtiPlot abrem como matrizes e são gravadas de volta como matrizes.
