# Apps do Origin

A versão 0.21 trouxe os Apps gratuitos do Origin (edição padrão) de análise e de gráficos. Eles ficam em quatro
lugares:

- **Analysis → Apps** para ajuste de curvas, picos, matemática, sinal e estatística;
- **Sheet → Apps** para processamento de dados;
- **Graph → Apps** para ferramentas que fazem ou mudam gráficos;
- **Graph → Origin graph types → Apps** para os 23 Apps que desenham um tipo novo de gráfico (veja
  [Tipos de gráfico do Origin](../graph-types/)).

As ferramentas que trabalham sobre colunas leem as colunas que você seleciona na planilha (Ctrl+clique nos
cabeçalhos). As que trabalham sobre uma curva usam a curva que você clicou no gráfico. As que comparam curvas usam
todas as curvas do painel ativo. Os resultados vão para planilhas novas, para o painel Messages e, quando ajuda, para
um gráfico.

![Diagrama de cromaticidade]({{AROOT}}assets/img/chromaticity.webp){: width="1600" height="1000" loading="lazy" }

## Ajuste de curvas

| App | O que faz |
|---|---|
| Find a fitting function | Ajusta todos os modelos prontos à curva selecionada e os ordena pelo critério de Akaike corrigido (AICc), com os pesos de Akaike. Você pode mandar ajustar o melhor modelo à curva na hora. |
| Simple fit | Um ajuste rápido com um modelo de uma lista curta ou sua própria expressão `y = …`. A curva ajustada e uma caixa de resultados vão para o gráfico e são reajustadas quando os dados mudam. |
| 2D smoother | Uma superfície suave por x, y, z espalhados (funções de base radial). Suavização 0 passa pelos pontos. Você recebe a superfície como mapa de contornos e os resíduos em cada ponto. |
| Compare datasets | As curvas do painel são descritas por um mesmo conjunto de parâmetros? Cada curva é ajustada sozinha e todas juntas. O teste F da soma de quadrados extra e o AIC decidem. |
| Compare linear fit parameters and datasets | Testa se as retas pelas curvas têm inclinações iguais e, nesse caso, interceptos iguais (como numa análise de covariância). |

## Picos e matemática

| App | O que faz |
|---|---|
| Align peaks | Desloca as curvas do painel ao longo de x para que os picos delas se alinhem com os da primeira curva. O alinhamento pode usar o máximo, o centroide acima da meia altura ou a correlação cruzada. |
| Convert global to local coordinates | x, y num referencial com uma origem nova e o eixo x girado. |
| Popular constants | Uma planilha de constantes do CODATA com unidades e incertezas. |
| Curvature radius | A curvatura κ = \|y″\| / (1 + y′²)^3/2 e o raio dela ao longo da curva. |
| Tangent | A tangente e, se pedir, a normal num x, desenhadas no gráfico. |
| Tafel extrapolation | Selecione uma curva de polarização: x é o potencial em V e y é a corrente. Retas por log\|i\| numa janela anódica e numa catódica dão Ecorr, icorr, βa e βc. |
| Distance between two points | Distância, dx, dy, ângulo e inclinação, com o segmento desenhado no painel. |
| Level crossing | Os valores de x em que a curva cruza um nível: subindo, descendo ou os dois. A histerese ignora o ruído em torno do nível. |

![Gráfico de Nyquist com painéis de Bode]({{AROOT}}assets/img/nyquist.webp){: width="1600" height="1000" loading="lazy" }

## Sinal e estatística

| App | O que faz |
|---|---|
| White noise | Uma planilha de ruído branco gaussiano ou uniforme, com semente para que o resultado possa ser repetido. |
| NetCDF data analysis | Escolha uma variável de um arquivo NetCDF ou HDF5 e a uma ou duas dimensões a manter. As outras são reduzidas por média, soma, mínimo, máximo, desvio padrão ou mediana. O resultado é uma curva ou um mapa. |
| Mann–Kendall test | Teste de tendência com correção de empates, o τ de Kendall e a inclinação de Sen. |
| Asymmetric correlation matrix | Correlação (Pearson, Spearman ou Kendall) de cada coluna do grupo A com cada coluna do grupo B, com valores p e um mapa de calor. |
| Logistic regression | Regressão logística binária. A coluna dependente tem 0 e 1. Você recebe coeficientes, erros padrão, testes de Wald, razões de chances com limites de 95 %, deviance, AIC, o teste da razão de verossimilhança, o R² de McFadden, probabilidades ajustadas e a tabela de confusão. |
| Hurst exponent | Análise de faixa reescalada (R/S) com o gráfico log–log. |
| Hysteresis | Para o laço selecionado: área, campos coercivos, remanência, saturação e quadratura. |

## Processamento de dados (Sheet → Apps)

| App | O que faz |
|---|---|
| Text to columns | Divide uma coluna de texto por um delimitador em colunas novas. Partes numéricas viram números. |
| Data slicer | Mantém as linhas dentro de uma faixa numérica ou entre textos escolhidos, numa planilha nova ou ocultando as outras linhas. |
| Extract XY data from graph | Os x, y de cada curva do painel que estão dentro dos limites atuais dos eixos. |
| Periodic report | Relê um arquivo de dados a intervalos. Cada vez que o arquivo muda, uma linha com a hora, o número de linhas e o último valor, a média, o mínimo e o máximo de cada coluna é acrescentada a uma planilha de relatório. Rode o comando de novo para parar. |
| Project manager | Lista os projetos de uma pasta e de suas subpastas, com suas planilhas, gráficos, notas e datas. |
| Project searcher | Encontra os projetos cujos nomes de planilhas, nomes de colunas, nomes de gráficos, títulos, rótulos de eixos ou notas contêm um texto. |

## Ferramentas de gráficos (Graph → Apps)

| App | O que faz |
|---|---|
| Graph maker | Clique nas colunas na ordem desejada e escolha qualquer tipo de gráfico, básico ou do Origin. |
| Batch plotting | Repete o gráfico ativo para outras planilhas com os mesmos nomes de colunas, um gráfico novo por planilha. |
| Common bar width | Dá a mesma largura a todas as séries de barras do gráfico, ou do painel ativo. |
| Layer stack manager | Reordena, oculta e mostra os painéis do gráfico. Os detalhes ampliados (insets) ficam com os painéis-pais. |
| Color editor | Faz seus próprios mapas de cores a partir de uma lista de cores (contínuos ou em faixas). Eles são mantidos entre as sessões e aparecem, com as formas invertidas “_r”, em toda lista de mapas de cores. |
| LaTeX equation | Compõe matemática em LaTeX, como `\frac{a}{b}` ou `\int_0^\infty e^{-x^2}dx`, no painel. |
| Toolbar maker | Monta sua própria barra de ferramentas com quaisquer comandos. Ela é mantida entre as sessões. |

![Diagrama de Taylor]({{AROOT}}assets/img/taylor.webp){: width="1600" height="1000" loading="lazy" }

![Triângulo de textura do solo do USDA]({{AROOT}}assets/img/soil-texture.webp){: width="1600" height="1000" loading="lazy" }

![Isossuperfície]({{AROOT}}assets/img/isosurface.webp){: width="1600" height="1000" loading="lazy" }
