# Mio, the AI assistant

Mio is the assistant of the SciVelyx Suite. In SciVelyx Graphs she answers questions about the project, fits
columns, proposes graphs from a sentence, writes Python scripts for repetitive work, finds things in this guide and,
when you allow it, talks to outside services. She understands English, Portuguese and Spanish, and answers in the
language you write in.

Open her with **Mio ▸ Ask Mio** (Ctrl+Alt+M): the panel opens beside the properties.

![Mio counts the rows of a sheet, gives the mean of a column, fits a line and proposes a graph, which waits for Make graph]({{AROOT}}assets/manual/mio.png)

## What you can ask

| You write | Mio does |
|---|---|
| *What is in the project?* · *quantas linhas tem a planilha data?* · *how many rows with y > 2?* | lists the sheets with their rows and columns (and designations) and the graphs; counts rows, also those meeting a condition |
| *mean of column B* · *desvio padrão de y* · *statistics of y and z* | mean, standard deviation, minimum, maximum, median or sum of columns (masked rows left out) |
| *gaussian fit of y* · *faça um ajuste linear de z contra x* · *voigt fit of Intensity* | fits with the built-in models (linear, gauss, lorentz, voigt, expdec, boltzmann, power, poly2, poly3 …): the parameters with their errors and R²; the project is not changed |
| *scatter of y against x* · *plote y e z como linhas* · *grafique Intensity como barras* | proposes a graph (see below) |
| *write a script for a gaussian fit of every column* | writes a script (see below) |
| *how do I export a graph as PDF?* | answers from this guide and names the pages it used |
| */peak-report* · *summarize the sheet* | runs a skill: several steps in one request |

When you do not name the sheet, Mio uses the sheet of the graph you see, or the sheet that has the columns you
named.

## Graphs from words

Mio reads the sheet, the columns and the kind of graph (lines, scatter, bars, histogram, box plot, area, step, error
bars, pie, violin, stem) from your request — *y against x* puts x on the horizontal axis; without an x she uses the
column designated X. The sheet, the columns and the kind are checked before you see the proposal, and **nothing
changes until you press *Make graph***: then a new graph opens in the project, with one curve per column, ready to
edit like any other.

![After Make graph the new graph is in the project; a script Mio wrote is open in the script window]({{AROOT}}assets/manual/mio-graph.png)

## Scripts

Ask for a *script* (or *python*, *rotina*, *automate*) and Mio writes one from her tested recipes: a fit, the same
fit for every column with a table of the parameters, a graph exported at the size and resolution you ask, a graph
for every file of a folder, the statistics of every column, normalised columns, the derivative and integral of a
column. She fills in the sheet, the columns, the model, the kind and the format from your request and the project.
The script opens in a new tab of the script window; **it never runs by itself**: read it, change it, then run it.

## The language model

Mio works without a language model: her rules answer the requests above, and questions about the program get the
best passages of this guide. With a model she talks naturally, follows up on the previous question (*and of column
C?*), and understands requests in your own words.

The model runs **on your computer**. **Mio ▸ Language model** shows the memory and graphics card found and
recommends a model; all have permissive licences (Apache-2.0 or MIT), from 0.4 GB to 5 GB, and are downloaded once.
You can also point Mio to a model file (`.gguf`) or to a local server such as Ollama, LM Studio or llama-server (an
address on another computer is refused unless you allow it). What the model writes is checked: facts about the
program must come from the guide's passages it was given (cited as [1], [2]), numbers about your data from Mio's
tools; a number that appears nowhere in what the model was given is marked as unverified, and a wrong count or
statistic is replaced by the tool's own sentence.

## Connectors

Mio can send a sheet to, or look something up in, an outside service: Crossref, Zotero and GitHub are built in;
Google Workspace, Microsoft 365, GitHub, Trello, Jira and Confluence work through their MCP servers, which you
install. *find the reference Savitzky Golay on Crossref* · *send the sheet data to a Google sheet*.

Connectors are **off** until you switch them on in **Mio ▸ Connectors**, where their keys are kept on your computer
only. Every call is shown before it runs — the service, the tool, the data that would leave the computer — and runs
only when you press *Send*. Data in a folder you mark as **confidential** ask a second time. Every call is written to
Mio's audit file in the configuration folder.

## SciVelyx Graphs for other AI assistants (MCP)

`scivelyx mcp serve [FILES]` makes SciVelyx Graphs an MCP server, so that another assistant (Claude Desktop, an
IDE) can open your projects and data files, read sheets, compute statistics and fits, draw graphs to files, have
scripts written and read this guide. **Mio ▸ SciVelyx Graphs as an MCP server** shows the entry to paste in that
assistant's settings. Python scripts run only when you start the server with `--allow-scripts`.

## From the command line

```sh
scivelyx mio ask data.csv -q "gaussian fit of y"
scivelyx mio ask data.csv -q "scatter of y against x" --apply -o fig.pdf
scivelyx mio chat project.scivelyx.json      # a conversation in the terminal
scivelyx llm setup                           # choose and download a model
scivelyx llm use http://127.0.0.1:11434      # or a local server
```
