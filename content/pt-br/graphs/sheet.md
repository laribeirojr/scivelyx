# Planilhas e dados

## Importação

| Origem | Como |
|---|---|
| CSV, TSV, texto em colunas | **File → Open data** (Ctrl+O); comentários `#` no início são guardados, expoentes `D` do Fortran são lidos |
| Arquivos de texto incomuns | **File → Import wizard** (Ctrl+Shift+I): separador, vírgula decimal, linhas a pular, linhas de nomes e de comentários, com pré-visualização ao vivo |
| Excel, LibreOffice (.ods), NumPy, JSON, Parquet | **File → Open data** |
| `.xvg` do GROMACS, log do LAMMPS | **File → Open data** |
| Difratômetros e espectrômetros (XRDML, RAS, UXD, JCAMP-DX, SPC) | **File → Open data** — veja [Espectroscopia e difração](../spectroscopy/) |
| Som (.wav) | **File → Open data**: uma coluna por canal |
| Banco de dados SQLite | **File → SQLite database…**: uma tabela ou uma consulta `SELECT` (só leitura) |
| HDF5, NetCDF, MATLAB (.mat) | **File → HDF5, NetCDF or MATLAB file…** (ou abra/solte o arquivo): variáveis como colunas ou como matriz — veja [Multivariada, wavelets e o digitalizador](../origin-tools/) |
| A imagem de um gráfico | **Analysis → Digitizer…** lê os pontos de volta |
| Vários arquivos numa só tabela | **File → Several files into one table…**: lado a lado ou empilhados, com o nome do arquivo numa coluna |
| GitHub | **File → GitHub** (Ctrl+G): a URL de um repositório, pasta ou arquivo; repositórios privados com um `GITHUB_TOKEN` |
| Uma matriz (grade de números) | **File → Matrix** ou **Sheet → Matrix** |

Colunas de datas viram um eixo de datas automaticamente.

## Colunas

- **Designação**: X, Y, Z, erro em X, erro em Y, rótulo ou nenhuma (botão direito no cabeçalho). Os gráficos as
  seguem.
- **Nome longo e unidades**: viram os títulos dos eixos.
- **Tipo**: número, texto ou data/hora; **formato numérico**: decimal, científico ou de engenharia (10k), com casas
  decimais; **somente leitura**; **oculta**. Tudo isso é guardado no projeto.
- Mova, troque, adicione, preencha (números de linha, valores aleatórios uniformes ou normais) e ordene colunas —
  também por várias chaves.

## Fórmulas — Set values

**Sheet → Set values** (Ctrl+Q) calcula uma coluna a partir de uma fórmula, com pré-visualização:

```text
A^2 + i                       # i é o número da linha (começa em 1)
col("E (eV)") * 1000          # outra coluna pelo nome
hc_eVnm / A                   # constantes físicas: kB, kB_eV, h, hbar, h_eV, c0, qe, NA, me, eps0, R, Ha_eV, Ry_eV, …
x > 0 ? x : 0                 # a sintaxe do SciDAVis e do QtiPlot (muParser) funciona: ?:, &&, ||, if(c, a, b)
```

Há funções especiais (erf, gamma, Bessel, Voigt…) e as funções do muParser do SciDAVis e do QtiPlot (avg, min/max/sum
com vários argumentos, rint, w0, wm1, chi2cdf, invt, rnd…). O avaliador é seguro: uma fórmula não consegue executar
código arbitrário. Colunas de fórmula **se recalculam sozinhas** quando as colunas que elas usam mudam; digitar numa
coluna de fórmula a transforma em dados comuns.

Atenção: nas fórmulas o separador decimal é sempre o ponto (`2.303`), como em toda linguagem de programação, mesmo
que os seus arquivos usem vírgula.

## Máscaras e desfazer

**Sheet → Mask rows** risca linhas em vermelho: elas ficam fora dos gráficos, ajustes, testes e estatísticas, mas
continuam no arquivo. **Unmask** as traz de volta. Com a planilha em foco, **Ctrl+Z** desfaz edições de dados.

## Reorganizar

O menu **Sheet** também tem: transpor; empilhar e desempilhar colunas; filtrar linhas por uma condição
(`T > 300 and k < 50`); juntar planilhas (por uma chave ou lado a lado); tabela dinâmica; estatísticas por linha;
contagem de frequências; ramo-e-folhas; converter em matriz e de volta. Cada operação cria uma planilha nova, e a
original fica intacta.

**Sheet → Export sheet** grava Excel (com nomes longos e unidades), LibreOffice, CSV ou TSV.
