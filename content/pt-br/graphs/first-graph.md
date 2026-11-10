# Seu primeiro gráfico

Esta página leva um arquivo de dados até uma figura pronta, ajustada e exportada. Ela usa só a janela; os mesmos
passos podem depois virar um script ([Scripts]({{ROOT}}graphs/docs/scripts/)).

## 1. Abra os dados

**File → Open data** (Ctrl+O) lê CSV, TSV e texto em colunas (com comentários `#` e expoentes `D` do Fortran), Excel,
LibreOffice (.ods), NumPy, JSON, Parquet, `.xvg` do GROMACS, logs do LAMMPS, WAV e SQLite, além dos arquivos de
difratômetros e espectrômetros ([Espectroscopia e difração]({{ROOT}}graphs/docs/spectroscopy/)). Para arquivos com um
formato incomum — vírgula decimal, linhas de cabeçalho a pular, nomes em outra linha — use **File → Import wizard**
(Ctrl+Shift+I), que mostra a tabela enquanto você ajusta as opções.

Os dados abrem como uma **planilha**. Cada coluna tem uma *designação* (X, Y, Z, erro em X, erro em Y, rótulo), um
*nome longo* e *unidades*; nome longo e unidades viram os títulos dos eixos, por exemplo “Energy (eV)”. Mude-os com o
botão direito no cabeçalho da coluna (**Set as X**, **Set as Y**, **Column properties**).

## 2. Faça o gráfico

Selecione as colunas (Ctrl+clique nos cabeçalhos) e clique num botão da aba **Graphs** da faixa de opções — *Line*,
*Scatter*, *Error bars*, *Columns*… O gráfico segue as designações: cada Y usa o X mais próximo à sua esquerda, e uma
coluna de erro em Y selecionada vira barras de erro. Sem seleção, o botão abre uma pequena configuração em que você
escolhe as colunas e o painel de destino.

## 3. Edite

Todo elemento da figura é editável:

- **duplo clique** num título, num eixo, numa curva, na legenda ou no fundo do painel abre as propriedades;
- um clique seleciona (contorno azul), e a barra **Font** das abas Home e Format muda o texto selecionado;
- arraste a legenda e os textos; arraste um painel 3D para girá-lo;
- **Delete** apaga o elemento selecionado, **Ctrl+Z** desfaz.

[Editando gráficos]({{ROOT}}graphs/docs/editing/) lista o que contém cada diálogo.

## 4. Ajuste

Clique na curva e depois em **Analysis → Curve fitting** (Ctrl+Shift+F). Escolha um modelo (linear, gaussiano,
decaimento exponencial, Voigt, vários picos, sua própria fórmula…), aperte **Fit**, olhe os parâmetros, os resíduos e
as bandas, e clique em **Apply to graph**. A curva ajustada, a banda de confiança e uma caixa com os parâmetros
aparecem no gráfico e são recalculadas sempre que os dados mudam.

![O assistente de ajuste]({{AROOT}}assets/img/fit-wizard.webp){: width="1260" height="820" loading="lazy" }

## 5. Exporte

Escolha o tamanho da revista em **Format → Journal** (por exemplo *Nature — 1 column (89 mm)*, *APS — 1 column*) e
depois **File → Export** (Ctrl+E). PDF, SVG e EPS mantêm o texto editável no tamanho físico exato; PNG e TIFF usam a
resolução que você definir. **File → Save** guarda tudo — dados, gráficos, notas e scripts — num único projeto
`.scivelyx.json`.

## Experimente os exemplos

O menu **Examples** e a tela inicial abrem figuras prontas (estrutura de bandas com marcas Γ–X–M, espectro com
densidade de estados, superfície de energia em 2D e 3D, termodinâmica de dinâmica molecular em dois eixos y, cartas
ternária e de Smith, e as figuras inspiradas em artigos de 2026…). Cada uma é totalmente editável e mostra uma
técnica que você pode reaproveitar.
