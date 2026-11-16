# Representações

Os métodos de desenho do VMD e os elementos visuais do OVITO são modificadores do pipeline, de modo que vários
deles dividem a mesma imagem: uma proteína como cartoon, seu ligante como licorice e a água como pontos.
**View ▸ Representations** lista todos.

![Água como licorice, com as ligações de hidrogênio como linhas tracejadas e a densidade do oxigênio ao longo da trajetória como isossuperfície]({{AROOT}}assets/md/styles.webp)

## Estilos de átomos

| Estilo | Desenho |
|---|---|
| default | esferas do raio covalente × o fator de tamanho |
| VDW | esferas do raio de van der Waals (Bondi) |
| CPK | esferas pequenas e ligações finas |
| Licorice | esferas e ligações do mesmo raio |
| Lines | ligações como linhas |
| Points | pontos |

A caixa de estilo da vista 3D vale para todos os átomos; o modificador **Atom style** só para os selecionados, com
raio e raio de ligação próprios.

## Cartoon e fitas

**Cartoon and ribbons** desenha o NewCartoon do VMD (hélices como fitas, folhas como setas, alças como tubos), o
NewRibbons, o Tube e o Trace pelos átomos CA das proteínas, pelos átomos P dos ácidos nucleicos, ou pelos átomos de
qualquer polímero (uma cadeia por molécula). As cores vêm da estrutura secundária (DSSP, as cores do VMD), dos
átomos, ou são uma cor só. A coluna `ss` também colore os átomos pela estrutura secundária.

## Superfícies

| Modificador | Superfície |
|---|---|
| Molecular surface | o QuickSurf do VMD (densidade gaussiana), a superfície acessível ao solvente (SAS) e a superfície excluída do solvente (SES), com área e volume |
| Construct surface mesh | o alpha shape do OVITO (área da superfície, volume e fração sólidos, átomos da superfície) ou uma densidade gaussiana |
| Create isosurface | a superfície de nível de uma grade 3D: um *Density map* do pipeline, ou um arquivo OpenDX ou Gaussian cube |
| Coordination polyhedra | envoltórias convexas dos vizinhos ligados ou dos que estão dentro de um raio de corte |

![A malha de superfície do OVITO das gotas de um vapor de Lennard-Jones, com oclusão ambiente]({{AROOT}}assets/md/surface.webp)

## Mapas de densidade 3D

**Analysis ▸ 3D density map (volmap)** faz a média, ao longo dos frames, da densidade numérica, mássica ou de carga
de uma seleção (ou da fração de frames com um átomo em cada voxel, a ocupação do VMD), como histograma ou com
suavização gaussiana, em qualquer célula. Ele grava um arquivo OpenDX ou cube, abre o mapa como isossuperfície e
manda três mapas 2D (as médias ao longo dos vetores da célula) para o SciVelyx Graphs. No terminal:

```bash
scivelyx-md volmap water.lammpstrj --select "type == 1" --spacing 0.5 -o oxigenio.dx
```

## Linhas

- **Generate trajectory lines**: o caminho dos átomos selecionados ao longo dos frames, desdobrado ou cortado na
  célula.
- **Hydrogen-bond lines**: linhas tracejadas entre doadores e aceitadores, com a definição da análise de ligações de
  hidrogênio (o HBonds do VMD).

## Oclusão ambiente e ray tracing

- A caixa **AO** da vista 3D acrescenta oclusão ambiente em espaço de tela à vista e às imagens; o modificador
  **Ambient occlusion** escurece os átomos enterrados como o OVITO faz (coluna `ao_brightness`).
- **Imagens em ray tracing**, com sombras e luz ambiente, são desenhadas pelo Tachyon (o ray tracer do VMD) ou pelo
  POV-Ray, quando você os instalou: File ▸ Save 3D image ▸ Renderer, ou `scivelyx-md image … --renderer tachyon`. A
  câmera é a da vista; o arquivo de cena pode ser guardado.

![Uma imagem do Tachyon da adenilato quinase (cartoon e a superfície de um domínio), desenhada com a câmera da vista]({{AROOT}}assets/md/raytraced.webp)
