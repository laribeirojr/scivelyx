# Regressão, estatística e gadgets

A versão 0.18 trouxe as ferramentas de análise do Origin (edição padrão) que ainda faltavam. Elas ficam no menu
**Analysis**, nos submenus *Fitting (more)*, *Peaks (more)*, *Statistics (more)*, *Signal and mathematics (more)* e
*Gadgets*. As ferramentas que trabalham sobre colunas leem as colunas que você seleciona na planilha (Ctrl+clique nos
cabeçalhos). As que trabalham sobre uma curva usam a curva que você clicou no gráfico. Os resultados vão para
planilhas novas, para o painel Messages e, quando ajuda, para um gráfico.

## Ajuste

**Regressão linear múltipla.** Selecione a coluna dependente e as preditoras, e então escolha qual é a dependente. O
relatório e as planilhas dão:

- cada coeficiente com seu erro padrão, t, p, limites de confiança e fator de inflação da variância (VIF);
- a tabela da ANOVA, R², R² ajustado e RMSE;
- os valores ajustados e os resíduos.

O gráfico mostra os resíduos contra os valores ajustados e um gráfico de *alavancagem parcial* (variável adicionada)
por preditora. A inclinação de cada gráfico de alavancagem parcial é o coeficiente daquela preditora.

![Regressão múltipla com gráficos de alavancagem parcial]({{AROOT}}assets/img/mlr.webp){: width="1600" height="1000" loading="lazy" }

**Elipse de confiança.** Selecione duas colunas. A elipse contém uma nova observação (*population*) ou a média, com a
probabilidade que você escolher. O gráfico também mostra os dados e o ajuste de reta.

No **Fit Wizard**:

- **× N** repete o modelo N vezes com um deslocamento y0 compartilhado, por exemplo três picos gaussianos da mesma
  forma. Os parâmetros viram `xc_1`, `xc_2`, …
- **Derived** recebe expressões dos parâmetros ajustados, como `FWHM = 2*sqrt(2*ln(2))*w; area = A*w*sqrt(2*pi)`. Os
  erros delas vêm da matriz de covariância (método delta). Elas são recalculadas com o ajuste quando os dados mudam.

## Picos

- **Integrate peaks** encontra os picos da curva selecionada e integra cada um entre seus limites, sem ajuste. Dá a
  área, o centro, o centroide, a altura, a FWHM e a área %. A linha de base pode ser nenhuma, uma reta entre as
  pontas, ou automática.
- **Batch peak analysis** roda a mesma análise, integração ou ajuste gaussiano, em cada curva do gráfico e grava uma
  planilha-resumo.

## Estatística

| Ferramenta | O que dá |
|---|---|
| Normality tests | Shapiro–Wilk, Kolmogorov–Smirnov, Lilliefors, Anderson–Darling, D'Agostino K² e Chen–Shapiro, com a decisão no seu nível |
| Probability plot | Os dados ordenados na escala de probabilidade de uma distribuição normal, log-normal, Weibull, exponencial, logística ou Gumbel, com a reta ajustada e uma banda de confiança |
| 2D frequency count | Contagens numa grade de classes de x e y, como matriz e mapa de cores |
| Discrete frequency | Quantas vezes ocorre cada valor ou texto distinto, com porcentagem e valores acumulados |
| QC chart (X-bar R) | Médias e amplitudes de subgrupos (valores consecutivos, ou rótulos numa primeira coluna selecionada) com linhas centrais e limites de controle |
| Outlier tests | Grubbs (uma vez ou repetido) e Q de Dixon; opcionalmente mascara as linhas discrepantes |
| Means comparison | Depois de uma ANOVA de um fator (uma coluna por grupo): Tukey, Bonferroni, Šidák, Fisher LSD, Scheffé, Holm–Bonferroni, Holm–Šidák ou Dunnett contra um controle |

Os valores p de Lilliefors, Chen–Shapiro e Dixon vêm de amostras normais simuladas com semente fixa, e por isso são
sempre os mesmos.

![Um gráfico de probabilidade de Weibull]({{AROOT}}assets/img/probability-plot.webp){: width="1600" height="1000" loading="lazy" }

![Uma carta X-barra R]({{AROOT}}assets/img/qc-chart.webp){: width="1600" height="1000" loading="lazy" }

## Sinal e matemática

- **Percentile filter:** cada ponto é trocado por um percentil dos vizinhos (50 = mediana).
- **FFT filter: parabolic or threshold:** um passa-baixa cujo ganho cai como 1 − (f/f<sub>c</sub>)², ou a remoção de
  toda componente de Fourier mais fraca que uma amplitude.
- **Average multiple curves:** as curvas do painel ativo num x comum, com média, desvio padrão, erro padrão e
  contagem.
- **Trace interpolation:** pontos igualmente espaçados ao longo da curva, na ordem dos dados. **On XYZ**: z é lido ao
  longo de um caminho que você dá sobre dados x, y, z espalhados.
- **3D interpolation:** x, y, z espalhados e um valor viram uma grade regular. Cada nível de z vira uma matriz.
- **Polygon area:** a área, o centroide e o perímetro de uma curva fechada.
- **Intersections:** onde as curvas do painel se cruzam, ou cruzam uma reta horizontal ou vertical.

## Gadgets

**Vertical cursor (all graphs):** clique ou arraste num gráfico. A barra de status mostra o valor de cada curva de
cada gráfico naquele x.

Os outros gadgets trabalham sobre a curva selecionada, dentro do **seletor de faixa** (Analysis → Gadgets → Range
selector, depois arraste ao longo de x):

- ajuste rápido (reta) e ajuste sigmoidal rápido;
- picos, derivada, interpolação e integral;
- FFT e estatística.

O resultado aparece numa caixa no gráfico, e uma curva ou um segundo gráfico é acrescentado quando houver. Mova a
faixa e o gadget é calculado de novo. **Stop the gadget** o encerra.

![O gadget de ajuste sigmoidal]({{AROOT}}assets/img/gadget.webp){: width="1600" height="1000" loading="lazy" }
