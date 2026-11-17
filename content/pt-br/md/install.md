# Instalação

O SciVelyx MD roda no Windows 10 e 11 (64 bits), no macOS 11 ou mais novo (Apple silicon e Intel) e no Linux
x86_64. O programa é independente: não precisa de nenhuma outra aplicação SciVelyx. Para editar os resultados como
gráficos, instale também o SciVelyx Graphs (instalador próprio); **File ▸ Send to SciVelyx Graphs** os abre lá. Baixe o arquivo do seu sistema na [página de versões]({{ROOT}}md/#download). Durante a fase de
testes, a página de versões está aberta aos testadores convidados.

| Sistema | Arquivo | Observações |
|---|---|---|
| Windows | `SciVelyx-MD-<versão>-windows-x64-setup.exe` | Instala para o seu usuário sem direitos de administrador (ou para todos). Menu Iniciar, ícone opcional na área de trabalho, `scivelyx-md` opcional no PATH, desinstalador. |
| Windows, sem instalar | `SciVelyx-MD-<versão>-windows-x64-portable.zip` | Descompacte em qualquer pasta e rode `SciVelyx-MD.exe`. |
| macOS, Apple silicon | `SciVelyx-MD-<versão>-macos-arm64.dmg` | M1, M2, M3, M4… |
| macOS, Intel | `SciVelyx-MD-<versão>-macos-x86_64.dmg` | |
| Linux | `SciVelyx-MD-<versão>-linux-x86_64.AppImage` | Um arquivo para a maioria das distribuições. |
| Linux, pasta simples | `SciVelyx-MD-<versão>-linux-x86_64.tar.gz` | Não precisa de FUSE. |

Cada versão publica também `SHA256SUMS.txt`, com as somas de verificação dos arquivos.

## Windows

1. Rode o `…-setup.exe`.
2. As versões de teste ainda não têm assinatura de código. Se o Windows SmartScreen disser “O Windows protegeu o
   computador”, clique em **Mais informações → Executar assim mesmo**.
3. Abra o SciVelyx MD pelo menu Iniciar. Para removê-lo: Configurações → Aplicativos.

## macOS

1. Abra o `.dmg` e arraste o **SciVelyx MD** para **Aplicativos**.
2. As versões de teste ainda não são assinadas com um Apple Developer ID. Na primeira vez, clique com Control (ou
   com o botão direito) no aplicativo em Aplicativos e escolha **Abrir**, e depois **Abrir** de novo. No macOS 15 e
   mais novos, se isso não aparecer: Ajustes do Sistema → **Privacidade e Segurança** → **Abrir Mesmo Assim**.

## Linux

- **AppImage:** `chmod +x SciVelyx-MD-*.AppImage` e rode-o. Distribuições mais antigas precisam do pacote FUSE 2
  (`libfuse2` no Debian e no Ubuntu, `fuse-libs` no Fedora); sem FUSE, use o tar.gz.
- **tar.gz:** descompacte e rode `SciVelyx-MD/SciVelyx-MD`; a linha de comando é `SciVelyx-MD/scivelyx-md`.
- O AppImage também roda a linha de comando: `./SciVelyx-MD-*.AppImage scivelyx-md versions`.

## A partir do código (testadores com acesso)

No Linux, no WSL e no macOS, a partir de um clone do código do SciVelyx MD:

```bash
cd scivelyx-md
./install.sh        # um ambiente Python próprio, os comandos, a entrada no menu
./update.sh         # depois: busca e instala a versão mais nova
```

## Conferir a instalação

```bash
scivelyx-md --version
scivelyx-md versions      # todas as bibliotecas dentro do programa, e se o ffmpeg foi encontrado
```

## Programas que você pode acrescentar

O SciVelyx MD funciona sozinho. Algumas coisas usam programas que você mesmo instala; indique onde eles estão em
**View ▸ Open in an external viewer ▸ Programs** se não forem achados no PATH:

| Programa | Para |
|---|---|
| ffmpeg | filmes MP4, MOV, MKV, AVI e WebM (GIF e séries de PNG funcionam sem ele) |
| Tachyon ou POV-Ray | imagens em ray tracing, com sombras e luz ambiente |
| VMD, UCSF ChimeraX, PyMOL | abrir os frames escolhidos em outro visualizador |
| módulo Python do OVITO (`pip install ovito`) | a análise de discordâncias do próprio OVITO, como opção (o SciVelyx MD tem a sua) |

O programa não se conecta à internet, não envia nada a lugar nenhum e não precisa de conta.
