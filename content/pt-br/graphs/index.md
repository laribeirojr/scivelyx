# Manual do usuário do SciVelyx Graphs

*Science in Motion. Data in Focus.*

O SciVelyx Graphs transforma dados medidos ou simulados em figuras de publicação e os analisa. Ele tem:

- planilhas com fórmulas;
- 176 tipos de gráfico, em que todo elemento pode ser editado;
- ajuste de curvas e de picos, e ferramentas de espectroscopia e de difração de raios X;
- estatística, matrizes e scripts Python;
- a migração de projetos do Origin, SciDAVis e QtiPlot.

Nossa missão: oferecer a pesquisadores de todo o mundo ferramentas rápidas, precisas e intuitivas para analisar e
visualizar dados científicos, para que conjuntos de dados complexos virem conclusões claras e o caminho dos dados à
descoberta fique mais curto.

<div class="manual-download">
<a class="btn btn-primary" href="{{AROOT}}downloads/{{MANUAL_PDF}}">Baixar este manual (PDF)</a>
</div>

O PDF tem os mesmos capítulos destas páginas, para ler sem internet ou imprimir.

**Sobre os nomes na tela.** O programa está em inglês. Neste manual, os nomes de menus, botões e campos aparecem
como na tela, em negrito e em inglês — por exemplo, **File → Open data** (Arquivo → Abrir dados) — para que você os
encontre sem precisar adivinhar a tradução.

![O SciVelyx Graphs com uma figura sendo editada]({{AROOT}}assets/manual/workspace.png)

## Por onde começar

| Se você quer… | Leia |
|---|---|
| instalar o programa | [Instalação](install/) |
| conhecer as partes da janela | [A janela](interface/) |
| seguir exemplos completos (DRX, Raman, band gap, ajuste implícito) | [Exemplos passo a passo](tutorials/) |
| fazer uma figura a partir de um arquivo de dados em cinco minutos | [Seu primeiro gráfico](first-graph/) |
| preparar os dados: importação, fórmulas, unidades, máscaras | [Planilhas e dados](sheet/) |
| mudar qualquer coisa numa figura | [Editando gráficos](editing/) |
| ajustar curvas, analisar picos, fazer testes | [Ajuste e análise](analysis/) |
| difração de raios X, Raman, arquivos de instrumentos | [Espectroscopia e difração](spectroscopy/) |
| PCA, agrupamentos, ROC, wavelets, ODR, ler dados de uma figura | [Multivariada, wavelets e o digitalizador](origin-tools/) |
| usar os Apps do Origin (Tafel, regressão logística, diagramas de Taylor e de Venn…) | [Apps do Origin](origin-apps/) |
| trabalhar com grades, imagens e superfícies | [Matrizes e superfícies](matrices/) |
| automatizar com Python | [Scripts](scripts/) |
| trazer seus projetos do Origin, SciDAVis ou QtiPlot | [Vindo do Origin, SciDAVis e QtiPlot](migration/) |
| entregar a figura a uma revista | [Exportação e publicação](export/) |
| desenhar figuras sem a janela | [Linha de comando](command-line/) |

## A janela num relance

- **Faixa de opções** (Home, Sheet, Matrix, Graphs, Analysis, Format, Insert, Layout) e os mesmos comandos nos menus.
- Painel **Project**: planilhas, matrizes, gráficos e pastas. Duplo clique abre; o botão direito cria pastas e move
  itens.
- **Abas de gráficos** no meio, cada gráfico com seu próprio histórico de desfazer.
- Painel **Properties**: o explorador de objetos (todo elemento da figura), o painel ativo e as séries.
- Painéis **Messages** e **Notes** embaixo; as notas são salvas no projeto.

Tecle **F1** no programa para um resumo curto das ações do mouse e do teclado.
