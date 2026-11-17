# Mio, the AI assistant

Mio is the assistant of the SciVelyx Suite. In SciVelyx MD she answers questions about the open files, builds
modifier pipelines from a sentence, writes Python scripts for repetitive work, finds things in this manual, and,
when you allow it, talks to outside services. She understands English, Portuguese and Spanish, and answers in the
language you write in.

Open her with **Mio ▸ Ask Mio** (Ctrl+Alt+M) or the *Mio* button: the panel opens beside the properties, with the
pipeline still in sight below.

![Mio counts the atoms of a type, reads the temperature of the LAMMPS log and proposes a pipeline, which waits for Apply pipeline]({{AROOT}}assets/md/mio.webp)

## What you can ask

| You write | Mio does |
|---|---|
| *What is open?* · *Quantos átomos de tipo 2?* · *how many atoms with z > 10?* | reads the files: frames, atoms, columns, types, the cell; counts atoms of a type or a selection |
| *mean of z of the atoms of type 1* · *maximum of c_pe* | minimum, mean or maximum of a per-atom column of the current frame |
| *average temperature* · *¿cuál es la presión máxima?* | the mean, range or last value of a quantity of the thermodynamic log |
| *compute the RDF between O and H up to 6* · *diffusion coefficient* · *calcule os tipos de estrutura* | runs the RDF, the MSD with the diffusion coefficient, or the structure types (adaptive CNA); the result opens in a tab, as from the Analysis menu |
| *replicate 2x2x2, then delete type 2 and run the DXA for BCC* | proposes a pipeline (see below) |
| *write a script for the RDF of every file of the folder runs* | writes a script (see below) |
| *how do I make a movie?* | answers from this manual and names the pages it used |
| */run-summary* · *check the crystal* | runs a skill: several steps in one request |

## Pipelines from words

Mio reads the request clause by clause (*then*, *depois*, *luego*, commas) and turns each one into a modifier of
the pipeline: replicate, select a type or an expression, delete the selected atoms, invert the selection, slice,
wrap and unwrap, compute a property, create bonds, clusters, Voronoi, CNA, PTM, grains, displacement vectors,
Wigner–Seitz, the DXA with its lattice, colour by type. When a language model is available it also handles the
requests her rules do not understand, choosing among **all** the program's modifiers and their parameters.

Every modifier and every parameter is checked by the program before you see the proposal, and **nothing changes
until you press *Apply pipeline***. The modifiers are then added to the pipeline like any other: edit, switch off,
reorder or remove them in the pipeline panel.

![After Apply pipeline the three modifiers are in the pipeline; a script Mio wrote is open in the Python panel]({{AROOT}}assets/md/mio-pipeline.webp)

## Scripts

Ask for a *script* (or *python*, *rotina*, *automate*) and Mio writes one from her tested recipes: the RDF of a file
or of every file of a folder, the MSD and diffusion coefficient, the thermodynamic quantities of a log, a movie,
a picture of each frame, the modified frames written to another file, the structure types of every frame. She fills
in the file, the pair of types, the distance, the frames and the format from your request and the open files. The
script opens in a new tab of the Python panel; **it never runs by itself**: read it, change it, then run it (F5).

## The language model

Mio works without a language model: her rules answer the requests above, and questions about the program get the
best passages of this manual. With a model she talks naturally, follows up on the previous question (*and of type
1?*), and understands requests in your own words.

The model runs **on your computer**. **Mio ▸ Language model** shows the memory and graphics card found and
recommends a model for them; all have permissive licences (Apache-2.0 or MIT), from 0.4 GB to 5 GB, and are
downloaded once. You can also point Mio to a model file (`.gguf`) or to a local server such as Ollama, LM Studio or
llama-server (an address on another computer is refused unless you allow it, because your questions would leave the
computer). Running a model file inside SciVelyx MD needs `llama-cpp-python`; the installed program uses a local
server.

What the model writes is checked: facts about the program must come from the manual's passages it was given (cited
as [1], [2]), numbers about your files from Mio's tools. A number that appears nowhere in what the model was given is
marked as unverified, and a wrong count or statistic is replaced by the tool's own sentence.

## Connectors

Mio can send a result to, or look something up in, an outside service:

- **built in:** Crossref (find a reference and its DOI), Zotero (your library; an API key), GitHub (report a problem
  as an issue; a token);
- **through their MCP servers**, which you install: Google Workspace (Sheets, Docs, Drive, Calendar, Gmail),
  Microsoft 365, GitHub, Trello, Jira and Confluence.

*find the reference Allen Tildesley on Crossref* · *send the RDF to a Google sheet* · *crie uma tarefa no Trello
para revisar a simulação amanhã às 10h*.

Connectors are **off** until you switch them on in **Mio ▸ Connectors**, where their keys are kept on your computer
only (`~/.scivelyx-md/connectors.json`). Every call is shown before it runs — the service, the tool, the data that
would leave the computer — and runs only when you press *Send*. Files in a folder you mark as **confidential** ask a
second time. Every call is written to `~/.scivelyx-md/mio/audit.jsonl`.

## Skills

A skill is a recipe of several of Mio's steps, called by a phrase or by `/name`. Three come with the program
(`/crystal-check`, `/run-summary`, `/remove-type`); your own are JSON files in **Mio ▸ Skills folder**:

```json
{"name": "water-check", "title": {"en": "Water check"}, "triggers": ["check the water"],
 "steps": [{"tool": "count", "selection": "type == 1"},
           {"tool": "thermo", "column": "Temp", "statistic": "range"},
           {"tool": "analysis", "analysis": "rdf", "question": "rdf between 1 and 1 up to 8"}]}
```

## SciVelyx MD for other AI assistants (MCP)

`scivelyx-md mcp serve [FILES]` makes SciVelyx MD an MCP server, so that another assistant (Claude Desktop, an IDE)
can open your files, ask Mio, run the RDF, MSD and structure analyses, read the modifiers, have pipelines proposed
and scripts written, and read this manual. **Mio ▸ SciVelyx MD as an MCP server** shows the entry to paste in that
assistant's settings. Python scripts run only when you start the server with `--allow-scripts`.

## From the command line and scripts

```sh
scivelyx-md mio ask dump.lammpstrj log.lammps -q "average temperature"
scivelyx-md mio ask dump.lammpstrj -q "replicate 2x2x1 then delete type 2" --apply -o big.xyz
scivelyx-md mio chat dump.lammpstrj            # a conversation in the terminal
scivelyx-md llm setup                          # choose and download a model
scivelyx-md llm use http://127.0.0.1:11434     # or a local server
```

```python
r = ask("how many atoms of type 2?", "dump.lammpstrj")
p = mio_pipeline("replicate 2x2x1 then delete type 2")
export(modify(load("dump.lammpstrj"), p), "big.xyz")
```
