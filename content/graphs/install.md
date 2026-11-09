# Installation

SciPlot-Graphs runs on Windows 10 and 11 (64-bit), macOS 11 or later (Apple silicon and Intel) and Linux x86_64.
Download the file for your system from the [latest release]({{ROOT}}graphs/#download). During the testing phase the
release page is open to invited testers.

| System | File | Notes |
|---|---|---|
| Windows | `SciPlot-Graphs-<version>-windows-x64-setup.exe` | Installs for your user without administrator rights (or for all users). Start menu, optional desktop icon, optional `sciplot` on the PATH, uninstaller. |
| Windows, no installation | `SciPlot-Graphs-<version>-windows-x64-portable.zip` | Unzip anywhere and run `SciPlot-Graphs.exe`. |
| macOS, Apple silicon | `SciPlot-Graphs-<version>-macos-arm64.dmg` | M1, M2, M3, M4… |
| macOS, Intel | `SciPlot-Graphs-<version>-macos-x86_64.dmg` | |
| Linux | `SciPlot-Graphs-<version>-linux-x86_64.AppImage` | One file for most distributions (glibc 2.35 or newer). |
| Linux, plain folder | `SciPlot-Graphs-<version>-linux-x86_64.tar.gz` | No FUSE needed. |

## Windows

1. Run the `…-setup.exe`.
2. The test builds are not code-signed yet. If Windows SmartScreen says “Windows protected your PC”, click
   **More info → Run anyway**.
3. Open SciPlot-Graphs from the Start menu. To remove it: Settings → Apps.

## macOS

1. Open the `.dmg` and drag **SciPlot-Graphs** onto **Applications**.
2. The test builds are not signed with an Apple Developer ID yet. The first time, Control-click (or right-click) the
   app in Applications and choose **Open**, then **Open** again. On macOS 15 and later, if that is not offered:
   System Settings → **Privacy & Security** → **Open Anyway**.

## Linux

```bash
chmod +x SciPlot-Graphs-*-linux-x86_64.AppImage
./SciPlot-Graphs-*-linux-x86_64.AppImage                    # the program
./SciPlot-Graphs-*-linux-x86_64.AppImage sciplot --help     # the command line
```

If the AppImage asks for FUSE, install `libfuse2` (Ubuntu and Debian: `sudo apt install libfuse2`) or use the
`.tar.gz`: extract it and run `SciPlot-Graphs` inside the folder.

## Checking a download

Every release has a `SHA256SUMS.txt`. Compare it with the checksum of your file:

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing        # Linux
shasum -a 256 -c SHA256SUMS.txt --ignore-missing    # macOS
certutil -hashfile SciPlot-Graphs-<version>-windows-x64-setup.exe SHA256    # Windows
```

## From the source code

Developers can also run the program from its Python source (Python 3.10 or newer):
`pip install -e ".[gui,excel]"` and then `sciplot gui`.
