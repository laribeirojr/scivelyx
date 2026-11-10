# Ajuste e análise

Selecione uma curva (clique nela no gráfico) e escolha uma operação na aba ou no menu **Analysis**. Os resultados vão
para o mesmo painel, para o eixo y da direita, para um painel novo abaixo ou para um gráfico novo, e ficam guardados
como planilhas com a receita de como foram feitos.

## Ajuste de curvas

**Analysis → Curve fitting** (Ctrl+Shift+F).

| Opção | Escolhas |
|---|---|
| Modelo | Linear, inclinação (y = a·x), polinômios de grau 2 a 9, gaussiana (também pela área), lorentziana, Voigt, decaimento exponencial (1ª, 2ª e 3ª ordem) e crescimento, logístico, Boltzmann, potência, logarítmico, Arrhenius, saturação exponencial, ExpLin, racionais, Planck, 2 a 6 picos gaussianos ou lorentzianos, sua própria fórmula (`A*exp(-x/t) + c`) ou uma função salva na **biblioteca**. |
| Parâmetros | Valor inicial, **limites inferior e superior**, fixo ou livre; *Estimate initial values* os preenche a partir dos dados. |
| Faixa | Só parte do eixo x (também pelo seletor de faixa no gráfico). |
| Pesos | Nenhum, instrumental (1/σ² de uma coluna de erro), estatístico (1/y), um conjunto de dados qualquer, pesos diretos. |
| Algoritmo | Levenberg–Marquardt (região de confiança quando há limites), Simplex (Nelder–Mead) ou **regressão por distância ortogonal** (ODR: erros em x e y); iterações e tolerância. |
| Saída | Curva ajustada (com N pontos ou nos x dos dados), caixa com os parâmetros e R², painel de resíduos, **bandas de confiança e de previsão** no nível que você escolher, erros escalados por √(χ²/gl), algarismos significativos, **matriz de covariância**, relatório gravado nas notas. |

O relatório dá cada parâmetro com seu erro padrão, R², R² ajustado, χ² reduzido e RMSE. Tudo o que o ajuste criou —
curva, bandas, tabela de parâmetros, caixa — é **recalculado em cadeia** quando os dados mudam.

**Analysis → Global fit** ajusta um modelo a várias curvas de uma vez e deixa você escolher quais parâmetros são
compartilhados (a mesma largura em todos os espectros, por exemplo).

Para curvas dadas na forma f(x, y) = 0 — círculos, elipses, cônicas — use **Analysis → Spectroscopy and diffraction →
Fit implicit function…** ([Exemplos passo a passo](../tutorials/), seção 4).

## Picos

**Analysis → Peak Analyzer** (Ctrl+Shift+K) passa por quatro etapas: linha de base (mínimos quadrados assimétricos ou
um polinômio pelas pontas), detecção (proeminência, número máximo, ou posições digitadas à mão), o ajuste de picos
gaussianos, lorentzianos, Voigt, pseudo-Voigt, Breit–Wigner–Fano, Pearson VII ou bi-gaussianos (uma forma para todos
ou uma por pico, com uma linha de base opcional ajustada junto), e uma tabela com centro, altura, FWHM, área e área % —
tudo com incertezas. **Find peaks** é a versão rápida (posições e FWHM). As ferramentas de Raman e de difração de
raios X estão em [Espectroscopia e difração](../spectroscopy/).

![O Peak Analyzer]({{AROOT}}assets/img/peak-analyzer.webp){: width="1240" height="760" loading="lazy" }

## Sinal

Suavização (Savitzky–Golay, média de vizinhos, passa-baixa por FFT, LOWESS), linha de base, FFT (amplitude, potência,
fase; janelas de Hann, Hamming, Blackman), interpolação (spline, Akima, PCHIP, linear), filtros de Butterworth
passa-baixa, passa-alta, passa-banda e rejeita-banda e o filtro de mediana, correlação e autocorrelação, convolução e
deconvolução (Richardson–Lucy, Wiener), envoltória de Hilbert, derivada, integral (área líquida e absoluta), integral
de uma função de a até b, normalização, translação de uma curva, subtração de uma reta ou de uma curva de referência.

## Estatística

- **Statistics** de colunas (N, média, desvio e erro padrão, quartis, mediana, assimetria, curtose) e de linhas;
  **Curve statistics**.
- **Distribution fit**: normal, lognormal, Weibull, gama, exponencial, logística e Cauchy, ordenadas por AIC e BIC com
  o teste de Kolmogorov–Smirnov, desenhadas sobre o histograma.
- **Hypothesis tests**: t (uma amostra, duas amostras, pareado), ANOVA, Shapiro–Wilk, Kolmogorov–Smirnov,
  Mann–Whitney, Wilcoxon, Kruskal–Wallis, Levene, qui-quadrado de independência e da variância — com a decisão no
  seu nível α. **ANOVA de dois fatores** com interação.

Componentes principais, análise de agrupamentos, curvas ROC, densidade por kernel, o espectrograma, as wavelets e o
digitalizador têm sua própria página: [Multivariada, wavelets e o digitalizador](../origin-tools/).

## Recálculo e lotes

**Analysis → Automatic recalculation** vem ligado. Desligue-o para trabalhar com dados grandes e aperte **Recalculate
now** (Ctrl+F5) quando quiser os resultados atualizados; resultados desatualizados ficam marcados.

**Analysis → Batch processing** roda o mesmo ajuste, Peak Analyzer, estatísticas, integral ou extremos sobre uma
pasta de arquivos ou uma lista de conjuntos de dados e reúne uma tabela-resumo — com o número no nome de cada arquivo
(uma temperatura, por exemplo) como eixo x — e o gráfico dela.
