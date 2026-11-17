# Mio, a assistente de IA

A Mio é a assistente da SciVelyx Suite. No SciVelyx Graphs ela responde a perguntas sobre o projeto, ajusta colunas,
propõe gráficos a partir de uma frase, escreve scripts Python para trabalhos repetitivos, acha coisas neste guia e,
quando você permite, conversa com serviços externos. Ela entende português, inglês e espanhol, e responde na língua
em que você escreve.

Abra-a em **Mio ▸ Ask Mio** (Ctrl+Alt+M): o painel abre ao lado das propriedades.

![A Mio conta as linhas de uma planilha, dá a média de uma coluna, ajusta uma reta e propõe um gráfico, que espera o Make graph]({{AROOT}}assets/manual/mio.png)

## O que você pode pedir

| Você escreve | A Mio faz |
|---|---|
| *O que tem no projeto?* · *quantas linhas tem a planilha data?* · *quantas linhas com y > 2?* | lista as planilhas com as linhas e colunas (e designações) e os gráficos; conta linhas, também as que atendem a uma condição |
| *média da coluna B* · *desvio padrão de y* · *estatísticas de y e z* | média, desvio padrão, mínimo, máximo, mediana ou soma de colunas (sem as linhas mascaradas) |
| *ajuste gaussiano de y* · *faça um ajuste linear de z contra x* · *ajuste voigt de Intensity* | ajustes com os modelos embutidos (linear, gauss, lorentz, voigt, expdec, boltzmann, power, poly2, poly3 …): os parâmetros com os erros e o R²; o projeto não é mudado |
| *dispersão de y contra x* · *plote y e z como linhas* · *grafique Intensity como barras* | propõe um gráfico (veja abaixo) |
| *escreva um script para um ajuste gaussiano de cada coluna* | escreve um script (veja abaixo) |
| *como exporto um gráfico em PDF?* | responde a partir deste guia e diz as páginas que usou |
| */peak-report* · *resuma a planilha* | roda uma habilidade (skill): vários passos num só pedido |

Quando você não diz a planilha, a Mio usa a planilha do gráfico que você está vendo, ou a planilha que tem as
colunas que você citou.

## Gráficos a partir de palavras

A Mio lê do seu pedido a planilha, as colunas e o tipo de gráfico (linhas, dispersão, barras, histograma, box plot,
área, degraus, barras de erro, pizza, violino, haste) — *y contra x* põe x no eixo horizontal; sem um x ela usa a
coluna designada X. A planilha, as colunas e o tipo são conferidos antes de você ver a proposta, e **nada muda até
você apertar *Make graph***: aí um novo gráfico abre no projeto, com uma curva por coluna, pronto para editar como
qualquer outro.

![Depois do Make graph o novo gráfico está no projeto; um script que a Mio escreveu está aberto na janela de scripts]({{AROOT}}assets/manual/mio-graph.png)

## Scripts

Peça um *script* (ou *python*, *rotina*, *automatize*) e a Mio escreve um a partir das receitas testadas dela: um
ajuste, o mesmo ajuste para cada coluna com uma tabela dos parâmetros, um gráfico exportado no tamanho e na
resolução que você pedir, um gráfico para cada arquivo de uma pasta, as estatísticas de cada coluna, colunas
normalizadas, a derivada e a integral de uma coluna. Ela preenche a planilha, as colunas, o modelo, o tipo e o
formato a partir do seu pedido e do projeto. O script abre numa nova aba da janela de scripts; **ele nunca roda
sozinho**: leia, mude e então execute.

## O modelo de linguagem

A Mio funciona sem modelo de linguagem: as regras dela atendem os pedidos acima, e perguntas sobre o programa recebem
os melhores trechos deste guia. Com um modelo ela conversa com naturalidade, continua a pergunta anterior (*e da
coluna C?*) e entende pedidos nas suas próprias palavras.

O modelo roda **no seu computador**. **Mio ▸ Language model** mostra a memória e a placa de vídeo encontradas e
recomenda um modelo; todos têm licenças permissivas (Apache-2.0 ou MIT), de 0,4 GB a 5 GB, e são baixados uma vez.
Você também pode indicar à Mio um arquivo de modelo (`.gguf`) ou um servidor local como Ollama, LM Studio ou
llama-server (um endereço em outro computador é recusado, a menos que você permita). O que o modelo escreve é
conferido: fatos sobre o programa têm de vir dos trechos do guia que ele recebeu (citados como [1], [2]); números
sobre os seus dados, das ferramentas da Mio; um número que não aparece em nada do que o modelo recebeu é marcado como
não verificado, e uma contagem ou estatística errada é trocada pela frase da própria ferramenta.

## Conectores

A Mio pode mandar uma planilha para um serviço externo, ou procurar algo nele: Crossref, Zotero e GitHub vêm
embutidos; Google Workspace, Microsoft 365, GitHub, Trello, Jira e Confluence funcionam pelos servidores MCP deles,
que você instala. *ache a referência Savitzky Golay no Crossref* · *envie a planilha data para uma planilha do
Google*.

Os conectores ficam **desligados** até você ligá-los em **Mio ▸ Connectors**, onde as chaves ficam só no seu
computador. Cada chamada é mostrada antes de rodar — o serviço, a ferramenta, os dados que sairiam do computador — e
só roda quando você aperta *Send*. Dados numa pasta que você marcar como **confidencial** perguntam uma segunda vez.
Cada chamada fica registrada no arquivo de auditoria da Mio, na pasta de configuração.

## O SciVelyx Graphs para outros assistentes de IA (MCP)

`scivelyx mcp serve [ARQUIVOS]` faz do SciVelyx Graphs um servidor MCP, para que outro assistente (o Claude Desktop,
um IDE) abra os seus projetos e arquivos de dados, leia planilhas, calcule estatísticas e ajustes, desenhe gráficos
em arquivos, peça scripts e leia este guia. **Mio ▸ SciVelyx Graphs as an MCP server** mostra a entrada a colar nas
configurações daquele assistente. Scripts Python só rodam quando você inicia o servidor com `--allow-scripts`.

## Pela linha de comando

```sh
scivelyx mio ask dados.csv -q "ajuste gaussiano de y"
scivelyx mio ask dados.csv -q "dispersão de y contra x" --apply -o fig.pdf
scivelyx mio chat projeto.scivelyx.json      # uma conversa no terminal
scivelyx llm setup                           # escolher e baixar um modelo
scivelyx llm use http://127.0.0.1:11434      # ou um servidor local
```
