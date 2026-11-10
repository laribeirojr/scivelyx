# Instalação

O SciVelyx Graphs roda no Windows 10 e 11 (64 bits), no macOS 11 ou mais recente (Apple silicon e Intel) e no Linux
x86_64. Baixe o arquivo do seu sistema na [versão mais recente]({{ROOT}}graphs/#download). Durante a fase de testes,
a página das versões é aberta a testadores convidados.

| Sistema | Arquivo | Observações |
|---|---|---|
| Windows | `SciVelyx-Graphs-<versão>-windows-x64-setup.exe` | Instala para o seu usuário sem direitos de administrador (ou para todos os usuários). Menu Iniciar, ícone opcional na área de trabalho, `scivelyx` opcional no PATH, desinstalador. |
| Windows, sem instalação | `SciVelyx-Graphs-<versão>-windows-x64-portable.zip` | Descompacte em qualquer lugar e rode `SciVelyx-Graphs.exe`. |
| macOS, Apple silicon | `SciVelyx-Graphs-<versão>-macos-arm64.dmg` | M1, M2, M3, M4… |
| macOS, Intel | `SciVelyx-Graphs-<versão>-macos-x86_64.dmg` | |
| Linux | `SciVelyx-Graphs-<versão>-linux-x86_64.AppImage` | Um arquivo para a maioria das distribuições (glibc 2.35 ou mais recente). |
| Linux, pasta simples | `SciVelyx-Graphs-<versão>-linux-x86_64.tar.gz` | Não precisa de FUSE. |

## Windows

1. Execute o `…-setup.exe`.
2. As versões de teste ainda não têm assinatura de código. Se o SmartScreen do Windows disser “O Windows protegeu
   o computador”, clique em **Mais informações → Executar assim mesmo**.
3. Abra o SciVelyx Graphs pelo menu Iniciar. Para removê-lo: Configurações → Aplicativos.

## macOS

1. Abra o `.dmg` e arraste o **SciVelyx Graphs** para **Aplicativos**.
2. As versões de teste ainda não são assinadas com um Apple Developer ID. Na primeira vez, Control-clique (ou clique
   com o botão direito) no aplicativo em Aplicativos e escolha **Abrir**, e depois **Abrir** de novo. No macOS 15 e
   seguintes, se isso não aparecer: Ajustes do Sistema → **Privacidade e Segurança** → **Abrir Mesmo Assim**.

## Linux

```bash
chmod +x SciVelyx-Graphs-*-linux-x86_64.AppImage
./SciVelyx-Graphs-*-linux-x86_64.AppImage                    # o programa
./SciVelyx-Graphs-*-linux-x86_64.AppImage scivelyx --help     # a linha de comando
```

Se o AppImage pedir FUSE, instale o FUSE 2 ou use o `.tar.gz` (extraia e rode `SciVelyx-Graphs` dentro da pasta):

| Distribuição | Comando |
|---|---|
| Ubuntu 24.04 ou mais novo | `sudo apt install libfuse2t64` |
| Debian, Linux Mint, Ubuntu mais antigo | `sudo apt install libfuse2` |
| Fedora, RHEL, Rocky, Alma | `sudo dnf install fuse-libs` |
| openSUSE | `sudo zypper install libfuse2` |
| Arch, Manjaro | `sudo pacman -S fuse2` |

**Quem testa e tem acesso ao repositório do código** pode instalar com o git. O `./install.sh` reconhece o
gerenciador de pacotes (apt, dnf, zypper ou pacman) e instala as bibliotecas de que o Qt precisa no Ubuntu, Debian,
Linux Mint, Fedora, RHEL e derivados, openSUSE e Arch. Onde o Python do sistema é anterior ao 3.10 (RHEL 8–9,
openSUSE Leap), ele instala o Python 3.11:

```bash
git clone https://github.com/ribeirojr-gh/scitrace-studio-backup.git ~/scivelyx
cd ~/scivelyx && ./install.sh     # depois: ./update.sh
```

## Conferindo um download

Toda versão tem um `SHA256SUMS.txt`. Compare-o com a soma de verificação do seu arquivo:

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing        # Linux
shasum -a 256 -c SHA256SUMS.txt --ignore-missing    # macOS
certutil -hashfile SciVelyx-Graphs-<versão>-windows-x64-setup.exe SHA256    # Windows
```

## Licença

O SciVelyx Graphs é **freeware**:

- é gratuito para qualquer uso, inclusive pesquisa, ensino e trabalho em empresas;
- você pode passar os instaladores sem modificação a outras pessoas, gratuitamente;
- você não pode modificá-lo, descompilá-lo nem vendê-lo;
- as figuras e os dados que você faz com ele são seus.

O instalador mostra a licença completa, que também está em `LICENSE.txt` (inglês) e `LICENSE.pt-BR.txt` (português)
na pasta do programa. As licenças dos componentes de terceiros estão em `THIRD_PARTY_NOTICES.txt`.

## Conferindo a instalação

**Help → Run the self-test…** (Ajuda → Executar o autoteste) confere o que depende do seu computador:

- as bibliotecas numéricas, o desenho das figuras e os formatos de exportação, inclusive o tamanho exato da página de
  um PDF;
- as fontes, os formatos de arquivo e a pasta de configurações;
- na janela real: a tela e sua escala, a área de transferência, a impressão e os temas.

Ele termina com um relatório no navegador e um `selftest.zip`. Anexe o zip a um relato de problema.

Num terminal, a mesma verificação roda com:

```bash
scivelyx selftest --gui            # relatório em ~/SciVelyx-selftest
```

**Help → Report a problem…** (Ajuda → Relatar um problema) abre um relato de problema no GitHub, já preenchido com a
versão e o sistema.
