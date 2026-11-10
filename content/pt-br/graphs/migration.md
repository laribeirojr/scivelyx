# Vindo do Origin, SciDAVis e QtiPlot

O SciVelyx Graphs abre e salva os projetos dos programas que você já usa, para que anos de trabalho pronto venham
junto. Toda importação e exportação produz um **relatório** com três listas: o que veio exatamente (✓), o que veio de
forma aproximada (≈, com o motivo) e o que não veio (✗, com o motivo). Nada desaparece sem aviso.

| Programa | Abrir no SciVelyx Graphs | Salvar a partir do SciVelyx Graphs |
|---|---|---|
| **SciDAVis** (`.sciprj`, `.sciprj.gz`, todas as versões) | diretamente | `.sciprj` no formato do SciDAVis 2.9 |
| **QtiPlot** (`.qti`, `.qti.gz`, 0.7 a 0.9.8) | diretamente | `.qti` no formato 0.9.8 |
| **Origin** (`.opj`, `.opju`) | pelo próprio Origin (abaixo) | um script Python que reconstrói o projeto dentro do Origin e salva `.opju` |

Projetos do QtiPlot 0.9.8, que o SciDAVis não abre, chegam ao SciDAVis pelo SciVelyx Graphs: abra o `.qti` e exporte-o
como `.sciprj`.

![Um relatório de migração]({{AROOT}}assets/img/migration-report.webp){: width="980" height="260" loading="lazy" }

## Um projeto

**File → Open project** (Ctrl+Shift+O) e escolha o `.sciprj`, `.qti` ou `.scivelyx-origin.json`. O original nunca é
sobrescrito: o projeto abre sem título e é salvo como `.scivelyx.json`.

## Uma pasta inteira

![Migrando uma pasta inteira de projetos]({{AROOT}}assets/manual/migration.png)

**File → Migration → Migrate a folder of projects…** converte cada projeto de uma pasta e de suas subpastas em
`.scivelyx.json`, cada um com seu relatório `.migration.txt`. Na linha de comando:

```bash
scivelyx migrate projetos_antigos/ -o convertidos/
```

## Projetos do Origin

**File → Migration → Script to export from Origin…** (ou `scivelyx origin-script`) salva um pequeno script Python.
Abra o projeto no Origin 2021 ou mais recente e rode o script na janela Python do Origin (Connectivity → Python). Ele
só lê o projeto e grava um `.scivelyx-origin.json` ao lado; abra esse arquivo no SciVelyx Graphs. No sentido inverso,
**File → Migration → Export project to…** com o tipo `.py` grava um script que reconstrói planilhas, gráficos e notas
no Origin.

## O que é convertido

- **Planilhas:** valores, colunas de texto e de data, designações, nomes longos e unidades, comentários, máscaras e
  fórmulas. Uma fórmula só continua viva se reproduzir os valores salvos; senão os valores ficam e a fórmula vai
  para o comentário da coluna, e o relatório diz por quê.
- **Matrizes:** chegam como matrizes com suas coordenadas e voltam como matrizes.
- **Gráficos 2D:** linhas, símbolos, barras, áreas, hastes, degraus, histogramas, caixas, pizzas, vetores, mapas de
  cores e de contornos, curvas de função e de ajuste (com seus parâmetros), barras de erro, eixos da direita e de
  cima, escalas log, limites, grades, títulos com subscritos e sobrescritos, fontes, legendas, textos, setas e várias
  camadas.
- **Gráficos 3D:** superfícies de matrizes, de funções e de colunas x, y, z.
- **Notas, registro de resultados e pastas.**

## Limitações conhecidas

- Tipos de gráfico que o SciDAVis e o QtiPlot não têm (polar, ternário, Smith, violino…) são exportados para eles como
  uma imagem do gráfico, com o PNG ao lado do projeto.
- Pastas aninhadas viram um único nível no explorador do projeto.
- Os scripts do Origin usam a API oficial `originpro` do Origin 2021 ou mais recente; ler arquivos `.opj` sem o Origin
  ainda não é oferecido.
- Arquivos `.scitrace-origin.json` e `.sciplot-origin.json`, gravados pelos exportadores dos nomes anteriores do
  programa, continuam abrindo.
