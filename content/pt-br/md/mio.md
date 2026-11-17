# Mio, a assistente de IA

A Mio é a assistente da SciVelyx Suite. No SciVelyx MD ela responde a perguntas sobre os arquivos abertos, monta
pipelines de modificadores a partir de uma frase, escreve scripts Python para trabalhos repetitivos, acha coisas
neste manual e, quando você permite, conversa com serviços externos. Ela entende português, inglês e espanhol, e
responde na língua em que você escreve.

Abra-a em **Mio ▸ Ask Mio** (Ctrl+Alt+M) ou no botão *Mio*: o painel abre ao lado das propriedades, com o pipeline
ainda à vista logo abaixo.

![A Mio conta os átomos de um tipo, lê a temperatura do log do LAMMPS e propõe um pipeline, que espera o Apply pipeline]({{AROOT}}assets/md/mio.webp)

## O que você pode pedir

| Você escreve | A Mio faz |
|---|---|
| *O que está aberto?* · *Quantos átomos de tipo 2?* · *quantos átomos com z > 10?* | lê os arquivos: quadros, átomos, colunas, tipos, a célula; conta os átomos de um tipo ou de uma seleção |
| *média de z dos átomos de tipo 1* · *máximo de c_pe* | mínimo, média ou máximo de uma coluna por átomo do quadro atual |
| *temperatura média* · *qual a pressão máxima?* | a média, o intervalo ou o último valor de uma grandeza do log termodinâmico |
| *calcule a RDF entre O e H até 6* · *coeficiente de difusão* · *calcule os tipos de estrutura* | roda a RDF, o MSD com o coeficiente de difusão, ou os tipos de estrutura (CNA adaptativa); o resultado abre numa aba, como pelo menu Analysis |
| *replique 2x2x2, depois apague o tipo 2 e rode a DXA para BCC* | propõe um pipeline (veja abaixo) |
| *escreva um script para a RDF de todos os arquivos da pasta runs* | escreve um script (veja abaixo) |
| *como faço um filme?* | responde a partir deste manual e diz as páginas que usou |
| */run-summary* · *verifique o cristal* | roda uma habilidade (skill): vários passos num só pedido |

## Pipelines a partir de palavras

A Mio lê o pedido oração por oração (*depois*, *then*, *luego*, vírgulas) e transforma cada uma num modificador do
pipeline: replicar, selecionar um tipo ou uma expressão, apagar os átomos selecionados, inverter a seleção, fatiar,
reenquadrar e desenrolar, calcular uma propriedade, criar ligações, clusters, Voronoi, CNA, PTM, grãos, vetores de
deslocamento, Wigner–Seitz, a DXA com a sua rede, cor por tipo. Quando há um modelo de linguagem, ele também atende
os pedidos que as regras dela não entendem, escolhendo entre **todos** os modificadores do programa e os seus
parâmetros.

Cada modificador e cada parâmetro é conferido pelo programa antes de você ver a proposta, e **nada muda até você
apertar *Apply pipeline***. Os modificadores entram então no pipeline como quaisquer outros: edite, desligue,
reordene ou remova-os no painel do pipeline.

![Depois do Apply pipeline os três modificadores estão no pipeline; um script que a Mio escreveu está aberto no painel Python]({{AROOT}}assets/md/mio-pipeline.webp)

## Scripts

Peça um *script* (ou *python*, *rotina*, *automatize*) e a Mio escreve um a partir das receitas testadas dela: a RDF
de um arquivo ou de todos os arquivos de uma pasta, o MSD e o coeficiente de difusão, as grandezas termodinâmicas de
um log, um filme, uma imagem de cada quadro, os quadros modificados gravados em outro arquivo, os tipos de estrutura
de cada quadro. Ela preenche o arquivo, o par de tipos, a distância, os quadros e o formato a partir do seu pedido e
dos arquivos abertos. O script abre numa nova aba do painel Python; **ele nunca roda sozinho**: leia, mude e então
execute (F5).

## O modelo de linguagem

A Mio funciona sem modelo de linguagem: as regras dela atendem os pedidos acima, e perguntas sobre o programa
recebem os melhores trechos deste manual. Com um modelo ela conversa com naturalidade, continua a pergunta anterior
(*e do tipo 1?*) e entende pedidos nas suas próprias palavras.

O modelo roda **no seu computador**. **Mio ▸ Language model** mostra a memória e a placa de vídeo encontradas e
recomenda um modelo para elas; todos têm licenças permissivas (Apache-2.0 ou MIT), de 0,4 GB a 5 GB, e são baixados
uma vez. Você também pode indicar à Mio um arquivo de modelo (`.gguf`) ou um servidor local como Ollama, LM Studio
ou llama-server (um endereço em outro computador é recusado, a menos que você permita, porque as suas perguntas
sairiam do computador). Rodar um arquivo de modelo dentro do SciVelyx MD precisa do `llama-cpp-python`; o programa
instalado usa um servidor local.

O que o modelo escreve é conferido: fatos sobre o programa têm de vir dos trechos do manual que ele recebeu
(citados como [1], [2]); números sobre os seus arquivos, das ferramentas da Mio. Um número que não aparece em nada do
que o modelo recebeu é marcado como não verificado, e uma contagem ou estatística errada é trocada pela frase da
própria ferramenta.

## Conectores

A Mio pode mandar um resultado para um serviço externo, ou procurar algo nele:

- **embutidos:** Crossref (achar uma referência e o seu DOI), Zotero (a sua biblioteca; uma chave de API), GitHub
  (relatar um problema como issue; um token);
- **pelos servidores MCP deles**, que você instala: Google Workspace (Sheets, Docs, Drive, Agenda, Gmail),
  Microsoft 365, GitHub, Trello, Jira e Confluence.

*ache a referência Allen Tildesley no Crossref* · *envie a RDF para uma planilha do Google* · *crie uma tarefa no
Trello para revisar a simulação amanhã às 10h*.

Os conectores ficam **desligados** até você ligá-los em **Mio ▸ Connectors**, onde as chaves ficam só no seu
computador (`~/.scivelyx-md/connectors.json`). Cada chamada é mostrada antes de rodar — o serviço, a ferramenta, os
dados que sairiam do computador — e só roda quando você aperta *Send*. Arquivos numa pasta que você marcar como
**confidencial** perguntam uma segunda vez. Cada chamada fica registrada em `~/.scivelyx-md/mio/audit.jsonl`.

## Habilidades (skills)

Uma habilidade é uma receita de vários passos da Mio, chamada por uma frase ou por `/nome`. Três vêm com o programa
(`/crystal-check`, `/run-summary`, `/remove-type`); as suas são arquivos JSON em **Mio ▸ Skills folder**:

```json
{"name": "agua", "title": {"pt": "Verificação da água"}, "triggers": ["verifique a água"],
 "steps": [{"tool": "count", "selection": "type == 1"},
           {"tool": "thermo", "column": "Temp", "statistic": "range"},
           {"tool": "analysis", "analysis": "rdf", "question": "rdf entre 1 e 1 até 8"}]}
```

## O SciVelyx MD para outros assistentes de IA (MCP)

`scivelyx-md mcp serve [ARQUIVOS]` faz do SciVelyx MD um servidor MCP, para que outro assistente (o Claude Desktop,
um IDE) abra os seus arquivos, pergunte à Mio, rode a RDF, o MSD e as análises de estrutura, leia os modificadores,
peça pipelines e scripts e leia este manual. **Mio ▸ SciVelyx MD as an MCP server** mostra a entrada a colar nas
configurações daquele assistente. Scripts Python só rodam quando você inicia o servidor com `--allow-scripts`.

## Pela linha de comando e por scripts

```sh
scivelyx-md mio ask dump.lammpstrj log.lammps -q "temperatura média"
scivelyx-md mio ask dump.lammpstrj -q "replique 2x2x1 e depois apague o tipo 2" --apply -o grande.xyz
scivelyx-md mio chat dump.lammpstrj            # uma conversa no terminal
scivelyx-md llm setup                          # escolher e baixar um modelo
scivelyx-md llm use http://127.0.0.1:11434     # ou um servidor local
```

```python
r = ask("quantos átomos de tipo 2?", "dump.lammpstrj")
p = mio_pipeline("replique 2x2x1 e depois apague o tipo 2")
export(modify(load("dump.lammpstrj"), p), "grande.xyz")
```
