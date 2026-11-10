# Exportação e publicação

## Primeiro o tamanho

Uma figura é definida em milímetros e pontos, e por isso o que você vê é o que a revista imprime. **Format → Journal**
define a largura para as revistas e apresentações mais comuns:

| Padrão | Largura |
|---|---|
| Nature — 1 / 2 colunas | 89 mm / 183 mm |
| APS (PRB, PRL) — 1 / 2 colunas | 3 3/8 pol / 7 pol |
| ACS — 1 / 2 colunas | 3,25 pol / 7 pol |
| Elsevier — 1 / 1,5 / 2 colunas | 90 / 140 / 190 mm |
| RSC — 1 / 2 colunas | 83 mm / 171 mm |
| Apresentação 16:9 | 254 mm |

O diálogo da figura (duplo clique fora dos painéis) define o tamanho exato, o DPI, a fonte base, a fonte matemática
(Computer Modern como no LaTeX, STIX…), as folhas de estilo do Matplotlib e o ciclo de cores.

## Formatos

**File → Export** (Ctrl+E):

| Formato | Uso |
|---|---|
| PDF, SVG, EPS | Arquivos vetoriais no tamanho exato, com fontes TrueType embutidas e o texto editável. |
| PNG, TIFF (LZW), JPEG | Imagens na resolução que você escolher. |
| Copy figure (Ctrl+Shift+C) | Cola em documentos e apresentações. |
| Export Python script… | Um script que redesenha a figura de forma idêntica, pixel a pixel, a partir dos dados do projeto. |

**File → Print…**, **Print preview** e **Print all graphs…** mandam os gráficos para uma impressora ou um PDF.

## Vários gráficos numa página

**Layout → Layout page** (Ctrl+Shift+L) compõe gráficos de abas diferentes e textos numa página em milímetros: mova e
redimensione, arrume numa grade, alinhe, acrescente letras dos painéis e exporte PDF vetorial, PNG ou TIFF. As páginas
são salvas no projeto.

## O arquivo de projeto

**File → Save** grava um único `.scivelyx.json` com os gráficos, as notas, os scripts, as páginas de layout, as
fórmulas e designações das colunas e os dados — embutidos, ou por referência com uma soma de verificação SHA-256.
Projetos salvos por versões anteriores sempre abrem nas posteriores, inclusive os `.scitrace.json` e `.splot.json`
dos nomes anteriores do programa.
