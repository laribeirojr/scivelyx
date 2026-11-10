# Exemplos passo a passo

Cada exemplo vai dos dados ao resultado, passo a passo, com as janelas que você vai ver. Os dados estão no próprio
programa (a galeria **Start from an example**) ou são fáceis de fazer. Os valores nas figuras vêm desses dados; os
seus serão outros.

## 1. Tamanho de cristalito a partir de um difratograma de raios X

**Objetivo:** as distâncias interplanares d, o tamanho de Scherrer de cada pico, o tamanho e a deformação de
Williamson–Hall e o parâmetro de rede de um pó cúbico.

1. Abra o difratograma: **File → Open data** lê `.xrdml` (Panalytical), `.ras` (Rigaku), `.uxd` (Bruker) e arquivos
   simples de duas colunas. O comprimento de onda gravado num arquivo de instrumento fica guardado com a planilha.
2. Faça o gráfico de 2θ contra a intensidade (selecione as duas colunas, **Graphs → Line**).
3. Clique na curva e depois em **Analysis → Spectroscopy and diffraction**:

   ![O menu Spectroscopy and diffraction]({{AROOT}}assets/manual/menu-spectroscopy.png)

4. Escolha **X-ray diffraction analysis…**. No diálogo:
   - **Wavelength** (comprimento de onda): escolha a linha (Cu Kα1 = 1,540562 Å na maioria dos equipamentos de
     laboratório) ou digite um valor em Å;
   - **Scherrer constant K**: 0,9 para cristalitos esféricos;
   - **Instrumental FWHM**: a largura de um padrão (LaB₆, Si) medida com a mesma montagem, em graus de 2θ; deixe 0
     se não tiver;
   - **Instrumental correction**: quadrática para picos gaussianos, linear para lorentzianos, geométrica para Voigt;
   - **Peak shape**, a forma usada no ajuste (pseudo-Voigt é a escolha usual), e **strip Kα2 first** se o dubleto
     aparece nos ângulos altos.
5. **OK** encontra e ajusta os picos. O relatório lista, para cada pico, 2θ, d, a FWHM e o tamanho, e depois o
   resultado de Williamson–Hall e a melhor indexação cúbica:

   ![Relatório da análise de difração de raios X de um pó de silício]({{AROOT}}assets/manual/xrd-report.png)

6. Duas planilhas e um gráfico são acrescentados: `<dados>_xrd` (a tabela dos picos com d, q e tamanho),
   `<dados>_williamson_hall` e o gráfico de Williamson–Hall, β cos θ contra 4 sen θ. O intercepto dá o tamanho, e a
   inclinação, a deformação:

   ![Gráfico de Williamson–Hall feito pela análise]({{AROOT}}assets/manual/xrd-williamson-hall.png)

**Confira o resultado.** A equação de Scherrer é confiável abaixo de uns 100 nm. Acima disso, a largura instrumental
domina. Uma inclinação de Williamson–Hall negativa ou com pontos muito espalhados geralmente significa que a
deformação está abaixo do que os dados conseguem resolver. No exemplo do silício, a indexação encontra a rede do
diamante com a = 5,4309 Å.

**Ferramentas relacionadas no mesmo menu:**

- **Strip Kα2** remove o dubleto do difratograma inteiro.
- **Convert 2θ, d and q** acrescenta as colunas d e q, ou 2θ para outro tubo de raios X.
- **Cubic reflections** desenha as linhas hkl de uma rede no gráfico.
- **Match reference peaks** emparelha seus picos com uma ficha de referência digitada numa planilha.

O exemplo *Stacked XRD after milling* da galeria mostra um conjunto de difratogramas deslocados na vertical.
*Power-law fit with a log–log inset* mostra o tamanho de cristalito contra o tempo de moagem, com os valores da
Tabela 1 do artigo.

## 2. Bandas D e G de um espectro Raman de carbono

**Objetivo:** I_D/I_G, A_D/A_G e o tamanho de cristalito L_a de um carbono desordenado.

1. Abra o espectro (deslocamento Raman em cm⁻¹ contra a intensidade). Arquivos JCAMP-DX (`.jdx`) e Galactic SPC
   (`.spc`) abrem diretamente.
2. Se o espectro tiver picos de raios cósmicos, clique na curva e rode **Spectroscopy and diffraction → Remove
   spikes**. Ele acrescenta uma cópia limpa da curva, e a coluna `spike` marca os pontos que foram substituídos.
3. **Carbon D and G bands…** pede o comprimento de onda do laser e ajusta uma banda D lorentziana e uma banda G de
   Breit–Wigner–Fano sobre uma linha de base linear. Marque **also D″ and D′** para carbonos amorfos.
4. O ajuste e as bandas são desenhados no gráfico:

   ![Bandas D e G ajustadas sobre o espectro]({{AROOT}}assets/manual/raman-carbon.png)

5. O relatório dá as posições das bandas, as razões com seus erros, L_a = 2,4×10⁻¹⁰ λ⁴ (A_D/A_G)⁻¹ (Cançado
   et al. 2006) e a distância entre defeitos L_D (Cançado et al. 2011):

   ![Relatório da análise do carbono]({{AROOT}}assets/manual/raman-report.png)

**O mesmo ajuste à mão.** **Analysis → Peak Analyzer** ajusta qualquer combinação de picos. Cada pico pode ter sua
própria forma, e a linha de base pode ser ajustada junto com os picos:

![Peak Analyzer com uma banda D lorentziana, uma banda G BWF e uma linha de base linear ajustadas juntas]({{AROOT}}assets/manual/peak-analyzer.png)

- **Positions**: `1350; 1590` (ou deixe vazio e deixe que ele encontre os picos; *Minimum prominence* controla
  quantos).
- **Shapes per peak**: `lorentz; bwf`. As chaves são gauss, lorentz, voigt, pvoigt, bwf, pearson7 e bigauss.
- **Baseline fitted with peaks**: linear. A etapa 1 ainda pode subtrair antes uma linha de base ALS ou polinomial.
- **Analyze**, olhe os resíduos e depois **Apply to graph**. A tabela de picos vai para uma planilha nova. As colunas
  são centro, altura, FWHM, área e área %, cada uma com seu erro, mais o parâmetro de forma (q para a BWF).

## 3. Band gap óptico por um gráfico de Tauc

**Objetivo:** o E_g de um semicondutor por extrapolação linear de (αhν)² contra hν.

1. Calcule a variável de Tauc na planilha. Acrescente uma coluna com uma fórmula, por exemplo `(2.303 * A * hv)^2`
   para uma transição direta permitida, em que `A` é a absorbância e `hv` a energia do fóton em eV
   (`hv = 1239.84 / wavelength_nm`). Nas fórmulas o separador decimal é o ponto.
2. Faça o gráfico de (αhν)² contra hν. O exemplo *Tauc plot* da galeria tem uma curva assim.
3. Clique na curva e abra **Analysis → Curve fitting**. Escolha o modelo **Linear** e ponha em **x range** a parte
   reta acima da borda de absorção (de 2,6 a 3,0 eV no exemplo).

   ![Diálogo de ajuste de curvas com o modelo linear]({{AROOT}}assets/manual/fit-dialog.png)

4. **Fit** e depois **Apply to graph**. E_g é onde a reta cruza o zero, E_g = −a/b para y = a + b·x. Digite em
   **Derived** (`Eg = -a/b`) e o relatório do ajuste o mostra com seu erro.

![A figura pronta: dados, a reta ajustada e E_g marcado]({{AROOT}}assets/manual/fig-tauc.png)

## 4. Elipse por pontos espalhados (ajuste implícito)

**Objetivo:** o centro, os semieixos e a orientação de uma elipse, ou de qualquer curva dada por f(x, y) = 0.

1. Faça o gráfico dos pontos como dispersão.
2. Clique neles e escolha **Spectroscopy and diffraction → Fit implicit function…**.
3. Escolha **Ellipse** (ou círculo, cônica, reta com erros em x e y, ou digite sua própria função, como
   `x^2/a^2 + y^2/b^2 = 1` com valores iniciais `a = 1, b = 1`).
4. A curva ajustada é desenhada e os parâmetros com seus erros vão para uma planilha nova. O ajuste minimiza a
   distância de cada ponto à curva, e não a distância vertical; por isso o resultado não depende de qual variável se
   chama y.

![Elipse ajustada a 90 pontos]({{AROOT}}assets/manual/implicit-fit.png)

## 5. Um arquivo com vírgula decimal

**Objetivo:** ler dados gravados por programas configurados em português, alemão ou francês, com `;` entre as colunas
e vírgula nos decimais.

1. **File → Import wizard** (Ctrl+Shift+I) e escolha o arquivo.
2. O assistente mostra o texto bruto e a tabela que vai montar. Ponha **Separator** em automático ou `;` e
   **Decimal** em `comma (1,5)`. Se o arquivo começa com anotações, ajuste **Skip first lines** e a **Header line**.
3. **Import** cria a planilha.

![Assistente de importação lendo um CSV com vírgula decimal]({{AROOT}}assets/manual/import-wizard.png)

## 6. Figuras inspiradas em artigos publicados

Os exemplos da galeria recriam tipos de figura de artigos de 2026. Abra um deles, veja como ele é construído em
**Properties** (séries, eixos, insets, linhas de referência, objetos de desenho) e troque os dados pelos seus: na
lista de séries, mude **Dataset**, **x** e **y**.

| Exemplo | O que ele mostra como fazer |
|------------------------------|------------------------------|
| ![Lei de potência com detalhe log–log]({{AROOT}}assets/manual/fig-power-law.png) | Um detalhe (inset) com eixos logarítmicos próprios (**Insert → Zoom (inset)** e depois as duas escalas em log), uma curva ajustada tracejada e uma equação no painel. |
| ![Curvas de magnetização em dez temperaturas]({{AROOT}}assets/manual/fig-mh-loops.png) | Dois painéis com uma cor por temperatura tirada de um mapa de cores, linhas no zero e uma só legenda para os dois painéis. |
| ![Curvas corrente–tensão com detalhe ampliado]({{AROOT}}assets/manual/fig-iv-inset.png) | Doze curvas com marcadores a cada 20 pontos, uma legenda com título em três colunas, um detalhe ampliado e uma linha de corte. |
| ![Deconvolução de DRX com índices de Miller]({{AROOT}}assets/manual/fig-xrd-deconv.png) | Componentes ajustadas em cores, os dados em cinza e rótulos hkl tirados de uma coluna de texto. |
| ![TGA e DTG]({{AROOT}}assets/manual/fig-tga.png) | Uma faixa de temperatura sombreada (uma banda de referência) e dois painéis com rótulos (a), (b). |
| ![Barras com colchete de significância]({{AROOT}}assets/manual/fig-bars.png) | Barras com barras de erro de desvio padrão, valores dentro das barras e um colchete com ** feito com as ferramentas de desenho. |
| ![Escores de PCA com elipses de 95 %]({{AROOT}}assets/manual/fig-pca.png) | Marcadores vazados por grupo e elipses de confiança de 95 % preenchidas. |
| ![Perfis de profundidade]({{AROOT}}assets/manual/fig-depth.png) | Quatro painéis com a profundidade aumentando para baixo, os títulos dos eixos em cima e linhas pontilhadas nos horizontes do solo. |
| ![Diagrama FORC]({{AROOT}}assets/manual/fig-forc.png) | Um mapa de contornos preenchido de uma distribuição, com barra de cores e suas unidades. |

Fontes dos tipos de figura: Neciosup-Puican et al., *J. Alloys Compd.* 1080 (2026) 190504; de Almeida et al.,
arXiv:2610.36482 (2026); da Silva et al., *Micro Nanostruct.* 221 (2027) 208963; Endres et al., *Clin. Oral Investig.*
30 (2026) 484; do Vale et al., preprint no EarthArXiv (2026).
