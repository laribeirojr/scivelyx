# Linha de comando

Todo pacote traz o `scivelyx`, o lado de linha de comando do SciVelyx Graphs: no Windows ao lado do
`SciVelyx-Graphs.exe` (ou no PATH, se você escolheu isso ao instalar), no macOS em
`SciVelyx-Graphs.app/Contents/MacOS/`, no Linux ao lado do `SciVelyx-Graphs` na pasta ou como
`SciVelyx-Graphs.AppImage scivelyx …`.

| Comando | O que faz |
|---|---|
| `scivelyx gui [projeto]` | Abre a janela (com um projeto ou arquivo de dados). |
| `scivelyx render projeto.scivelyx.json -o figura.pdf [--dpi 300]` | Desenha um projeto em PDF, SVG, EPS, PNG ou TIFF. |
| `scivelyx quick dados.csv -x T -y rho -o figura.pdf` | Faz o gráfico de colunas de um arquivo de dados (`--kind`, `--preset`, `--xlabel`, `--ylabel`, `-z` para mapas). |
| `scivelyx github <url> [-r]` | Lista os arquivos de tabelas de um repositório ou pasta do GitHub (`-r`: também as subpastas). |
| `scivelyx migrate caminhos… -o pasta` | Converte projetos do SciDAVis e do QtiPlot (e exportações do Origin) para o SciVelyx, com relatórios. |
| `scivelyx export-project projeto.scivelyx.json -o saida.sciprj` | Grava um projeto para o SciDAVis (`.sciprj`), o QtiPlot (`.qti`) ou o Origin (`.py`). |
| `scivelyx origin-script -o export_from_origin.py` | Salva o script que exporta `.opj`/`.opju` de dentro do Origin. |
| `scivelyx script arquivo.py [--project p.scivelyx.json] [--save saida.scivelyx.json]` | Roda um script Python com a [API de scripts]({{ROOT}}graphs/docs/scripts/). |
| `scivelyx selftest [--gui]` | Roda o autoteste e grava o relatório e o `selftest.zip`. |
| `scivelyx --version` | Mostra a versão. |

`scivelyx <comando> --help` lista todas as opções de um comando. Nas instalações feitas a partir do código com
`install.sh`, os comandos antigos `scitrace` e `scitrace-gui` continuam funcionando e abrem o mesmo programa.

## Exemplos

```bash
# Redesenha todas as figuras de uma tese depois de mudar o tema nos projetos
for p in figuras/*.scivelyx.json; do scivelyx render "$p" -o "pdf/$(basename "$p" .scivelyx.json).pdf"; done

# Converte um arquivo inteiro de projetos do SciDAVis e do QtiPlot
scivelyx migrate ~/projetos_antigos -o ~/projetos_scivelyx
```
