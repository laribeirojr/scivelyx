# Imagens, filmes e sessões

## Imagens

**File ▸ Save 3D image** (ou *Save image…* na vista 3D) desenha a vista atual de novo em qualquer tamanho, até
16 384 pixels, com a câmera, as cores, a seleção e os modificadores da vista:

![A janela Save image]({{AROOT}}assets/md/save-image-dialog.webp)

- PNG, JPEG ou TIFF; fundo transparente para PNG e TIFF;
- um rótulo com o passo e o tempo;
- o renderizador: OpenGL (como a vista), ou Tachyon e POV-Ray para imagens em ray tracing com sombras e luz
  ambiente (programas que você instala; veja [Representações]({{ROOT}}md/docs/representations/));
- oclusão ambiente.

Pelo terminal, sem janela:

```bash
scivelyx-md image dump.lammpstrj --frame -1 --color-by c_pe --cmap coolwarm --size-px 1920x1080 -o ultimo.png
scivelyx-md image md.dcd --topology md.psf -m "cartoon" --renderer tachyon --size-px 1600x1200 -o proteina.png
```

## Filmes

**File ▸ Save 3D movie** filma os frames escolhidos com a câmera da vista:

![A janela Save movie]({{AROOT}}assets/md/movie-dialog.webp)

| Opção | |
|---|---|
| Frames | todos, ou `início:fim:passo` |
| Frames per second | a velocidade do filme |
| Width, height | em pixels (números pares para MP4) |
| Turn the camera per frame | uma órbita em torno do eixo vertical da vista, em graus por frame |
| Label | o passo e o tempo num canto |
| Video quality | rápido de gravar, ou o melhor (mais lento, arquivo menor) |

O tipo de arquivo segue o nome: **MP4**, MOV, MKV, AVI ou WebM pelo ffmpeg (instalado por você), **GIF** animado,
ou uma **série de PNG**. Pelo terminal:

```bash
scivelyx-md movie dump.lammpstrj --fps 15 --orbit 1 --size-px 1280x720 -o simulacao.mp4
```

## Sessões

**File ▸ Save session** (Ctrl+Shift+S) guarda, num único arquivo `*.scivelyx.json`, os arquivos abertos, o frame
atual, o pipeline, a vista e sua câmera, as propriedades por átomo e todas as abas de resultado; o arquivo também é
um projeto do SciVelyx Graphs. **File ▸ Open** desse arquivo traz a sessão de volta, mesmo depois que a pasta foi
movida com os dados.

## Outros visualizadores

**View ▸ Open in an external viewer** manda os frames escolhidos (depois do pipeline) para o VMD, o UCSF ChimeraX ou
o PyMOL instalados no seu computador, como um PDB de vários modelos com um script que o carrega como trajetória.
Indique onde eles estão em **View ▸ Open in an external viewer ▸ Programs** se não forem achados.
