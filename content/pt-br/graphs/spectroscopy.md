# Espectroscopia e difração

A versão 1.0.0rc5 trouxe ferramentas para espectros Raman, de infravermelho e de UV-Vis e para difratogramas de raios
X. Elas ficam em **Analysis → Spectroscopy and diffraction**, ao lado do Peak Analyzer (**Analysis → Peak Analyzer**),
que elas usam. As ferramentas que trabalham sobre uma curva usam a curva que você clicou no gráfico; as que
trabalham sobre colunas usam as colunas selecionadas na planilha.

## Arquivos de instrumentos

**File → Open data** lê estes arquivos diretamente, como qualquer tabela:

| Arquivo | Instrumentos |
|---|---|
| `.xrdml` | Difratômetros Malvern Panalytical (Empyrean, X'Pert, Aeris) |
| `.ras` | Difratômetros Rigaku (SmartLab, MiniFlex, Ultima) |
| `.uxd` | Exportação em texto do Bruker DIFFRACplus |
| `.jdx`, `.dx`, `.jcamp` | Espectros JCAMP-DX (IV, Raman, UV-Vis, RMN 1D), inclusive as formas comprimidas |
| `.spc` | Galactic/Thermo GRAMS SPC (formato novo; vários espectros com um só x viram várias colunas) |

O comprimento de onda, o anodo, a linha do laser ou o nome da amostra gravados no arquivo ficam guardados com a
planilha. As ferramentas de raios X começam com esse comprimento de onda.

## Picos com formas diferentes

No Peak Analyzer, a etapa 3 tem dois campos novos.

- **Shapes per peak** (formas por pico): uma chave de forma por pico, separadas por `;`. Por exemplo, `lorentz; bwf`
  é uma banda D lorentziana e uma banda G de Breit–Wigner–Fano. A última forma se repete para os picos restantes;
  vazio, vale a forma escolhida acima para todos. As chaves são:
  - `gauss`, `lorentz`, `voigt` e `pvoigt` (pseudo-Voigt);
  - `bwf` (Breit–Wigner–Fano);
  - `pearson7` (Pearson VII);
  - `bigauss` (gaussiana assimétrica, com uma largura própria de cada lado).
- **Baseline fitted with peaks** (linha de base ajustada com os picos): nenhuma, constante, linear ou quadrática. Ela
  é ajustada ao mesmo tempo que os picos, por cima da linha de base subtraída na etapa 1. Escolha *none* na etapa 1
  para ajustar só esse polinômio.

A tabela mostra a forma de cada pico e o seu parâmetro de forma: η para a pseudo-Voigt, m para a Pearson VII, q para
a BWF, e as larguras esquerda e direita da bi-gaussiana. A cauda de uma BWF nunca chega a zero; por isso a área dela é
integrada na faixa ajustada, e o centro é a posição do máximo.

![Peak Analyzer com uma forma por pico e uma linha de base linear ajustada junto com os picos]({{AROOT}}assets/manual/peak-analyzer.png)

## Difração de raios X

| Ferramenta | O que faz |
|---|---|
| X-ray diffraction analysis | Encontra e ajusta os picos do difratograma selecionado (x = 2θ em graus). A planilha nova tem d, q e o tamanho de Scherrer de cada pico. A largura instrumental (de um padrão como LaB₆ ou Si) é removida de forma quadrática (picos gaussianos), linear (lorentzianos) ou geométrica (Voigt). Também desenha um gráfico de Williamson–Hall com tamanho e microdeformação, e informa a rede cúbica (sc, bcc, fcc ou diamante) e o parâmetro de rede que melhor indexam os picos. |
| Strip Kα2 | Remove o dubleto Kα2 (correção de Rachinger) e acrescenta ao gráfico a curva só com Kα1. |
| Convert 2θ, d and q | Acrescenta à planilha as colunas d (Å) e q (Å⁻¹) e, se quiser, 2θ para outra linha de raios X. |
| Cubic reflections | Os hkl, a multiplicidade, d e 2θ de uma rede cúbica, desenhados como linhas verticais no painel ativo. |
| Match reference peaks | Emparelha valores de 2θ observados com uma planilha de referência que tenha uma coluna `d` ou `two_theta` (e, se quiser, `hkl` e `intensity`). |

Há comprimentos de onda prontos para as linhas Kα1, Kα2, Kα e Kβ de Cu, Mo, Co, Cr, Fe e Ag. Você também pode digitar
qualquer valor em ångström.

Exemplos passo a passo: [Exemplos passo a passo](../tutorials/), seções 1, 2 e 4.

## Raman

| Ferramenta | O que faz |
|---|---|
| Remove spikes (cosmic rays) | Encontra picos estreitos de raios cósmicos pelos saltos entre pontos vizinhos e os substitui por interpolação. As bandas Raman sobem suavemente e por isso são mantidas. |
| Wavelength ↔ Raman shift | Converte uma coluna de comprimento de onda absoluto (nm) em deslocamento Raman (cm⁻¹) para uma linha de laser, ou o contrário. |
| Carbon D and G bands | Ajusta a banda D (lorentziana) e a banda G (BWF) com uma linha de base linear. Informa I_D/I_G (alturas), A_D/A_G (áreas), o tamanho de cristalito L_a = 2,4×10⁻¹⁰ λ⁴ (A_D/A_G)⁻¹ (Cançado et al. 2006) e a distância entre defeitos L_D (Cançado et al. 2011, regime de poucos defeitos). Opcionalmente acrescenta as bandas D″ (≈1500 cm⁻¹) e D′ (≈1620 cm⁻¹). |

## Ajuste de funções implícitas

**Fit implicit function** ajusta uma curva f(x, y) = 0 aos pontos selecionados. Ele minimiza a distância de cada ponto
à curva (regressão por distância ortogonal), e não uma distância vertical. Os modelos prontos são:

- um círculo;
- uma elipse (centro, semieixos e ângulo, com excentricidade e área);
- uma cônica geral;
- uma reta com erros em x e em y.

Você também pode digitar sua própria função, como `x^2/a^2 + y^2/b^2 = 1`, com valores iniciais `a = 1, b = 1`. A
curva ajustada vai para o gráfico; os parâmetros e seus erros vão para uma planilha nova.
