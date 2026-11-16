# Installation

SciVelyx MD runs on Windows 10 and 11 (64-bit), macOS 11 or later (Apple silicon and Intel) and Linux x86_64. The
program stands alone: it needs no other SciVelyx application. To edit the results as graphs, install SciVelyx
Graphs as well (its own installer); **File ▸ Send to SciVelyx Graphs** then opens them there. Download the file for your system from the [releases page]({{ROOT}}md/#download). During the testing phase the
release page is open to invited testers.

| System | File | Notes |
|---|---|---|
| Windows | `SciVelyx-MD-<version>-windows-x64-setup.exe` | Installs for your user without administrator rights (or for all users). Start menu, optional desktop icon, optional `scivelyx-md` on the PATH, uninstaller. |
| Windows, no installation | `SciVelyx-MD-<version>-windows-x64-portable.zip` | Unzip anywhere and run `SciVelyx-MD.exe`. |
| macOS, Apple silicon | `SciVelyx-MD-<version>-macos-arm64.dmg` | M1, M2, M3, M4… |
| macOS, Intel | `SciVelyx-MD-<version>-macos-x86_64.dmg` | |
| Linux | `SciVelyx-MD-<version>-linux-x86_64.AppImage` | One file for most distributions. |
| Linux, plain folder | `SciVelyx-MD-<version>-linux-x86_64.tar.gz` | No FUSE needed. |

Every release also publishes `SHA256SUMS.txt` with the checksums of its files.

## Windows

1. Run the `…-setup.exe`.
2. The test builds are not code-signed yet. If Windows SmartScreen says “Windows protected your PC”, click
   **More info → Run anyway**.
3. Open SciVelyx MD from the Start menu. To remove it: Settings → Apps.

## macOS

1. Open the `.dmg` and drag **SciVelyx MD** onto **Applications**.
2. The test builds are not signed with an Apple Developer ID yet. The first time, Control-click (or right-click) the
   app in Applications and choose **Open**, then **Open** again. On macOS 15 and later, if that is not offered:
   System Settings → **Privacy & Security** → **Open Anyway**.

## Linux

- **AppImage:** `chmod +x SciVelyx-MD-*.AppImage`, then run it. Older distributions need the FUSE 2 package
  (`libfuse2` on Debian and Ubuntu, `fuse-libs` on Fedora); without FUSE, use the tar.gz.
- **tar.gz:** unpack it and run `SciVelyx-MD/SciVelyx-MD`; the command line is `SciVelyx-MD/scivelyx-md`.
- The AppImage also runs the command line: `./SciVelyx-MD-*.AppImage scivelyx-md versions`.

## From the source (testers with access)

On Linux, WSL and macOS, from a clone of the SciVelyx MD source:

```bash
cd scivelyx-md
./install.sh        # a private Python environment, the commands, the menu entry
./update.sh         # later: fetch and install the newest version
```

## Check the installation

```bash
scivelyx-md --version
scivelyx-md versions      # every library inside the program, and whether ffmpeg was found
```

## Programs you may add

SciVelyx MD works alone. A few things use programs you install yourself; set their paths in
**View ▸ Open in an external viewer ▸ Programs** if they are not found on the PATH:

| Program | For |
|---|---|
| ffmpeg | MP4, MOV, MKV, AVI and WebM movies (GIF and PNG series work without it) |
| Tachyon or POV-Ray | ray-traced pictures with shadows and ambient light |
| VMD, UCSF ChimeraX, PyMOL | opening the chosen frames in another viewer |
| OVITO's Python module (`pip install ovito`) | the dislocation analysis (DXA) |

The program does not connect to the internet, sends nothing anywhere and needs no account.
