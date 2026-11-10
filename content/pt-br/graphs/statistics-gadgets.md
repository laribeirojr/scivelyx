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
- FFT e estatística;
- tempo de subida (tempos de subida e de descida, de 10 % a 90 %, das bordas dentro da faixa);
- aglomerado (*cluster*: número de pontos, médias, desvios padrão e correlação dos pontos dentro da faixa).

O resultado aparece numa caixa no gráfico, e uma curva ou um segundo gráfico é acrescentado quando houver. Mova a
faixa e o gadget é calculado de novo. **Stop the gadget** o encerra.

![O gadget de ajuste sigmoidal]({{AROOT}}assets/img/gadget.webp){: width="1600" height="1000" loading="lazy" }

## Novidades da 1.0.0rc7: mais estatística, processamento de sinais e matemática

Estas são as ferramentas do OriginPro mais usadas em física. Elas ficam nos mesmos submenus.

### Statistics (more)

| Ferramenta | Selecione | Você recebe |
|---|---|---|
| Partial correlation | três ou mais colunas | a correlação de cada par com as outras colunas mantidas constantes (Pearson ou Spearman), t e p |
| Cross tabulation tests | duas colunas de categorias, ou as colunas de uma tabela de contagens | χ², razão de verossimilhança G, teste exato de Fisher (2 × 2), φ, V de Cramér e o coeficiente de contingência; um aviso quando as contagens esperadas ficam abaixo de 5 |
| Two-sample F test for variances | duas colunas | F = s₁²/s₂², p e o intervalo de confiança da razão |
| Proportion tests | nada (digite as contagens) | uma proporção contra p₀ (binomial exato e z, intervalos de Wilson e exato) ou duas proporções (teste z e exato de Fisher) |
| Repeated-measures ANOVA, one way | uma coluna por condição, uma linha por indivíduo | a tabela da ANOVA, η² parcial, o teste de esfericidade de Mauchly e os valores p corrigidos por Greenhouse–Geisser e Huynh–Feldt |
| Repeated-measures ANOVA, two way | as a × b colunas na ordem A1B1, A1B2, …, A2B1, … | cada efeito com seu próprio termo de erro e sua correção de Greenhouse–Geisser, e as médias das células |
| Sign test | uma coluna (contra uma mediana) ou duas (pareadas) | diferenças positivas, negativas e empates, e p |
| Wilcoxon signed-rank, one sample | uma coluna | W e p contra uma mediana hipotética |
| Two-sample Kolmogorov–Smirnov | duas colunas | D e p: as amostras vêm da mesma distribuição? |
| Mood's median test | duas ou mais colunas | χ², p e as contagens acima e não acima da mediana geral |
| Friedman ANOVA | três ou mais colunas (as linhas são os indivíduos) | χ², p, postos médios e o W de Kendall |
| t tests on rows | as colunas do grupo A e depois as do grupo B | um teste t em cada linha (Welch, pareado ou de uma amostra), com os valores q de Benjamini–Hochberg |
| Power and sample size | nada | a curva de poder contra n e o n que atinge o poder desejado, para testes t, ANOVA de um fator e duas proporções |

Os cálculos de poder concordam com o G\*Power: n = 64 por grupo para um teste t de duas amostras com d = 0,5,
α = 0,05 e poder 0,8.

![Poder de um teste t de duas amostras contra o número por grupo]({{AROOT}}assets/manual/power-curve.png)

### Fitting (more)

**F test of nested models** ajusta dois modelos à curva selecionada: um mais simples e outro, com mais parâmetros,
que o contém (linear e quadrático, uma e duas gaussianas). O teste F da soma de quadrados extra e o AICc de cada
modelo dizem se os parâmetros extras valem a pena. As duas curvas ajustadas são desenhadas.

### Signal and mathematics (more)

- **Power spectral density (Welch):** o periodograma médio da curva selecionada, com o comprimento do segmento e a
  janela.
- **Coherence:** a coerência quadrática (de 0 a 1) de duas curvas do painel amostradas no mesmo x.
- **Decimate:** mantém um ponto a cada n, depois de um filtro antialiasing.
- **Rise and fall times:** os níveis de 0 % e 100 % são os dois valores mais frequentes do sinal (IEEE 181). Cada
  borda de subida e de descida é medida entre os níveis que você escolher (10 % e 90 % por padrão). Linhas
  pontilhadas marcam os níveis no gráfico.
- **Hilbert transform:** a transformada, a envoltória, a fase desembrulhada e a frequência instantânea.
- **2D correlation (Noda):** selecione uma coluna por passo de uma perturbação (temperatura, tempo, pressão), com o
  eixo espectral como a coluna x delas. Você recebe o mapa síncrono Φ e o assíncrono Ψ como matrizes e mapas de
  cores. ν₁ é lido no eixo y e ν₂ no eixo x: quando Φ(ν₁, ν₂) e Ψ(ν₁, ν₂) têm o mesmo sinal, a banda em ν₁ muda
  antes da banda em ν₂.
- **Continuous wavelet function:** os valores de uma wavelet de Morlet, chapéu mexicano, derivada de gaussiana ou
  Paul numa escala e num deslocamento, normalizada para energia unitária.
- **2D FFT filter** (também no menu Matrix): filtro passa-baixa, passa-alta, passa-faixa ou rejeita-faixa da matriz
  ativa, com janela ideal, gaussiana ou de Butterworth.
- **2D volume integration e Surface area:** para três colunas x, y, z (uma grade regular ou pontos espalhados, que
  são triangulados) ou para a matriz ativa.
- **Error propagation:** digite a função, como `a*b/c`, e as variáveis como `a = 2 ± 0.1; b = 3 ± 0.2`. Você recebe
  a incerteza de primeira ordem com a contribuição de cada variável, e uma verificação por Monte Carlo.
- **Convex hull and centroid** (também no menu Graph): a envoltória convexa da dispersão selecionada, o centroide e
  as linhas do centroide até cada ponto.

**Matrix → Eigenvalues and eigenvectors** decompõe a matriz quadrada ativa.

O filtro digital (**Analysis → Filter (IIR / median)**) agora oferece, além do Butterworth, os projetos de Chebyshev
I e II, elíptico e de Bessel, com a ondulação na banda de passagem e a atenuação na banda de rejeição.

![Mapa assíncrono de correlação 2D de uma série de aquecimento: a banda em 1600 cm⁻¹ cresce antes da banda em 1700 cm⁻¹]({{AROOT}}assets/manual/corr2d-async.png)
