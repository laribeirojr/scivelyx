# Perguntas frequentes e solução de problemas

## Geral

**O SciVelyx Graphs é um fork do SciDAVis ou do QtiPlot?**
Não. Ele foi escrito do zero sobre PySide6, Matplotlib, NumPy, pandas e SciPy, e lê e grava os formatos de arquivo
deles. Nenhum código do QtiPlot, do SciDAVis ou do LabPlot é usado.

**Ele precisa de internet?**
Não. A rede só é usada quando você pede, por exemplo para ler dados do GitHub.

**Em que idioma está a interface?**
Inglês, o único idioma do programa. Este manual está em inglês e em português.

**Eu usava o SciPlot ou o SciTrace. O que muda?**
Só o nome: o programa se chamava SciPlot até a 0.14 e SciTrace da 0.15 à 1.0.0rc5. Projetos antigos (`.splot.json`,
`.scitrace.json`), temas, a biblioteca de funções de ajuste e as preferências são lidos e mantidos, e nas instalações
feitas com `install.sh` os comandos antigos `scitrace` continuam abrindo o programa.

**Ele cobre tudo o que o SciDAVis e o QtiPlot fazem?**
Sim. Os menus dos dois e, desde a versão 0.12, as opções dentro dos diálogos de ajuste, de eixos, de curvas e de 3D. A
versão 0.17 trouxe os últimos 21 itens, como pizzas 3D, eixos 3D logarítmicos, imagens como símbolos, escala log
depois de uma quebra de eixo, o Plot wizard, Append project e ações de script personalizadas. Veja
[Assistente de gráficos, janelas e apresentações](../working-tools/).

## Instalação

**O Windows diz “O Windows protegeu o computador”.** As versões de teste ainda não têm assinatura de código: clique
em **Mais informações → Executar assim mesmo**.

**O macOS diz que o aplicativo não pode ser aberto.** Control-clique no aplicativo em Aplicativos → **Abrir** →
**Abrir**; no macOS 15, Ajustes do Sistema → Privacidade e Segurança → **Abrir Mesmo Assim**.

**O AppImage não abre.** Instale o `libfuse2`, ou use o pacote `.tar.gz`.

**No Linux (Wayland) ou no WSL, o duplo clique na barra de título não maximizava a janela.** Corrigido na 1.0.0rc6:
o programa passou a usar a barra de título “adwaita” do Qt, em que o duplo clique maximiza e restaura. Se você
preferir outra, defina a variável de ambiente `QT_WAYLAND_DECORATION`.

## Trabalhando com o programa

**Uma coluna de fórmula não atualiza.** Se você digitou um valor nela, ela virou uma coluna comum de dados; defina a
fórmula de novo com **Sheet → Set values**.

**O resultado do ajuste não acompanha meus dados.** Confira se **Analysis → Automatic recalculation** está ligado, ou
aperte **Recalculate now** (Ctrl+F5).

**Algum texto mostra um aviso vermelho no diálogo de texto.** A notação matemática entre `$…$` é inválida (por
exemplo, uma chave não fechada); o diálogo deixa a figura como estava até que ela seja corrigida.

**O negrito não afeta a matemática entre `$…$`.** Use o botão **𝐁** do diálogo de texto, que escreve `\mathbf{}`.

**Meus números usam vírgula decimal.** Para ler arquivos assim, use **File → Import wizard** e escolha *Decimal:
comma (1,5)* ([Exemplos passo a passo](../tutorials/), seção 5). Nas fórmulas, o separador decimal é sempre o ponto.

## Relatando um problema

Abra uma issue no [repositório de downloads]({{ROOT}}graphs/#download) com a versão (Help → About), o sistema, o que
você fez e o que aconteceu e — se puder compartilhar — um projeto ou arquivo de dados pequeno que mostre o problema.
Anexe também o `selftest.zip` de **Help → Run the self-test…**.
