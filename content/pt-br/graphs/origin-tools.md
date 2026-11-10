# Multivariada, wavelets e o digitalizador

Estas ferramentas chegaram na versão 0.16. Cada uma lê as colunas que você seleciona na planilha ativa (Ctrl+clique
nos cabeçalhos), abre um diálogo curto e grava os resultados como **planilhas novas** (ou matrizes) e um **gráfico**.
Um relatório vai para o painel Messages e abre numa janela de onde você pode copiá-lo.

## Arquivos de arrays: HDF5, NetCDF e MATLAB

**File → HDF5, NetCDF or MATLAB file…**, ou abra ou solte um arquivo `.h5`, `.hdf5`, `.nc` ou `.mat` na janela.

O diálogo lista cada variável numérica com seu tamanho, tipo, unidades e nome longo. Grupos aparecem como
`grupo/nome`.

- **Como planilha:** variáveis unidimensionais do mesmo comprimento viram colunas. As unidades e os nomes longos
  delas viram as unidades e o nome longo da coluna, e os rótulos dos eixos saem certos. A planilha lembra o arquivo
  e as variáveis, e o projeto os recarrega.
- **Como matriz:** uma variável bidimensional vira uma matriz. As variáveis de coordenadas das suas dimensões dão x e
  y: variáveis de coordenadas do NetCDF ou escalas de dimensão do HDF5. Para variáveis com mais dimensões, é tomada
  a primeira fatia.

São lidos arquivos NetCDF no formato clássico e no NetCDF-4, e arquivos MATLAB da versão 4 à 7.3, inclusive campos
de structs. Valores de preenchimento, fatores de escala e deslocamentos são aplicados.

## Componentes principais (PCA)

**Analysis → Multivariate → Principal components.** Selecione duas ou mais colunas numéricas.

| Opção | Escolhas |
|---|---|
| Matriz | **correlação**: cada variável padronizada, como o Origin faz por padrão; ou **covariância**, nas unidades originais |
| Componentes a manter | de 1 até o número de variáveis |

Os resultados são três planilhas:

- **scores** (escores): uma linha por observação;
- **loadings** (pesos): os autovetores;
- **eigenvalues** (autovalores): com a porcentagem e a porcentagem acumulada da variância.

O gráfico mostra o **gráfico de autovalores** (scree plot) e o **biplot**: escores como pontos, pesos como setas com o
nome das variáveis. O relatório também dá o critério de Kaiser, o número de autovalores acima de 1. Linhas com algum
valor faltante ficam de fora.

![PCA: gráfico de autovalores e biplot]({{AROOT}}assets/img/pca.webp){: width="1600" height="1000" loading="lazy" }

## Análise de agrupamentos

**Analysis → Multivariate → Cluster analysis.**

- **k-means:** inícios k-means++; o melhor de dez rodadas é mantido.
- **Hierárquico:** ligação de Ward, média, completa, simples, centroide ou mediana. A árvore é cortada no número de
  grupos que você pedir.

Os grupos são numerados pelo tamanho. A planilha nova traz as colunas escolhidas, o grupo de cada linha e, no
k-means, a distância ao centro. Uma segunda planilha traz os centros. O gráfico colore os pontos por grupo e, no
método hierárquico, desenha o **dendrograma**. O relatório dá a largura média da silhueta, de −1 a 1 (maior significa
grupos mais separados), e, para árvores, a correlação cofenética.

![Agrupamento hierárquico com o dendrograma]({{AROOT}}assets/img/clusters.webp){: width="1600" height="1000" loading="lazy" }

## Curva ROC

**Analysis → Multivariate → ROC curve.**

- Escolha a coluna de pontuação (o resultado de um teste ou de um classificador) e a coluna com a classe verdadeira.
  A coluna de classe precisa ter exatamente dois valores, números ou texto.
- Escolha qual classe é a positiva e se uma pontuação maior significa positivo.

A planilha lista cada limiar com a taxa de falsos positivos, a sensibilidade, a especificidade e o J de Youden. O
relatório dá:

- a **AUC** com seu erro padrão (Hanley–McNeil) e intervalo de 95 %;
- o valor p contra AUC = 0,5;
- o melhor limiar.

## Densidade por kernel

**Analysis → Multivariate → Kernel density.**

- **Uma coluna:** uma estimativa suave da distribuição com kernel gaussiano. A largura do kernel vem da regra de
  Scott ou de Silverman, ou é fixada por você. A curva é desenhada sobre o histograma, e a planilha também traz a
  distribuição acumulada.
- **Duas colunas:** a densidade 2D como matriz e mapa de cores, com os pontos por cima.

## Espectrograma

**Analysis → Time–frequency and wavelets → Spectrogram.** Selecione x e o sinal, ou só o sinal. Os valores de x
precisam ser igualmente espaçados.

As opções são a janela (Hann, Hamming, Blackman, retangular, flat top, Bartlett), o comprimento dela em pontos e a
sobreposição. O resultado é uma matriz de densidade de potência (em dB, como potência ou como amplitude) em função de
x e da frequência, desenhada como mapa de cores. Quando x está em segundos, a frequência sai em hertz.

## Wavelets

**Transformada wavelet contínua:**

- **Wavelets:** Morlet, chapéu mexicano ou Paul.
- **Faixa de frequências:** espaçada logaritmicamente, com uma faixa padrão.
- **Valores:** potência, **potência retificada** (comparável entre frequências), amplitude ou parte real.

O escalograma é desenhado num eixo de frequência logarítmico. O **cone de influência** tracejado marca onde as bordas
do registro o distorcem.

![Transformada wavelet contínua de um chirp]({{AROOT}}assets/img/wavelet.webp){: width="1600" height="1000" loading="lazy" }

**Wavelet decomposition** separa o sinal em uma aproximação e nos detalhes de cada nível. É a análise de
multirresolução, com wavelets de Haar, Daubechies, Symlets, Coiflets ou biortogonais. As partes somadas dão de novo o
sinal, e cada uma ganha seu painel empilhado.

**Wavelet denoise / smooth:**

- **Denoise** (remover ruído): encolhe os coeficientes de detalhe com o limiar universal σ√(2 ln n), suave ou duro,
  em que o σ do ruído vem dos detalhes mais finos. Você também pode digitar seu próprio limiar.
- **Smooth** (suavizar): mantém só a aproximação num nível escolhido.

## Ajuste com erros em x e y (ODR)

No **Fit Wizard**, escolha o algoritmo **Orthogonal distance (ODR, errors in x and y)**. Ele minimiza as distâncias
dos pontos à curva, ponderadas pelas duas barras de erro:

- as **barras de erro em x** da curva;
- os erros em y da opção *Weighting*.

Sem barras de erro em x, x e y contam igualmente. Limites, parâmetros fixos, bandas e recálculo encadeado funcionam
como nos outros algoritmos. Os resultados batem com o ODRPACK, a biblioteca por trás do ODR do Origin e do SciPy. Em
scripts: `fit("data", "T", "rho", "expdec", method="odr", sigma="drho", sigma_x="dT")`.

## Digitalizador

**Analysis → Digitizer…** (também no menu File) abre a imagem de um gráfico: uma digitalização, uma figura de um
artigo, uma captura de tela.

1. **Eixos.** Escolha X1 e clique numa marca rotulada do eixo x, depois digite o valor dela. Faça o mesmo para X2 e
   para Y1 e Y2 no eixo y. Marque *logarithmic* para eixos log. Digitalizações levemente giradas são tratadas.
2. **Pontos.**
    - *Pick points* acrescenta um ponto por clique.
    - *Pick the curve colour* seguido de **Trace line** segue uma linha pela imagem inteira.
    - **Find symbols** encontra marcadores daquela cor.
    - *Region (drag)* limita a busca e deixa a legenda de fora.
    - A tolerância, o passo e o maior espalhamento ajustam o rastreamento.
3. **Planilha.** **Next curve** guarda os pontos e começa outra curva. **Create sheets** faz uma planilha por curva e
   um gráfico com todas.

![O digitalizador rastreando uma curva]({{AROOT}}assets/img/digitizer.webp){: width="1200" height="760" loading="lazy" }

## Em scripts

`pca("data", ["a", "b", "c"])`, `kde("data", "a")`, `roc("data", "score", "class")`,
`cluster("data", ["a", "b"], 3, method="ward")`, `spectrogram("signal", "t", "y")` e
`cwt("signal", "t", "y", wavelet="morlet")` devolvem os mesmos resultados como dicionários de arrays e tabelas.
