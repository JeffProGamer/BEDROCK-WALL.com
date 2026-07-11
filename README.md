# BEDROCK WALL

BEDROCK WALL is a Windows desktop security workspace with:
- a local heuristic scan for suspicious executable/script files and malware-like names
- a permission-gated whole-PC scan that lists drives before scanning
- threat alerts and optional cloud upload when Firebase credentials are available
- a safer OpenVPN connector for trusted local profiles or validated fetched public relay profiles
- a polished local website under the `pages` folder
- shared BEDROCK styling using `resources/bedrock_texture.png`

BEDROCK WALL is a defensive local tool. It does not claim perfect malware detection,
anonymous browsing, or a custom VPN protocol. VPN launch uses an installed OpenVPN
client and only connects with profiles the user approves.

## Run Locally

```powershell
& 'C:\Users\Faisa\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python.exe' main.py
```

## Open The Site

Open:

```text
pages/index.html
```

The site includes:
- overview dashboard
- security console page
- VPN gateway page with profile safety checks and GitHub reachability controls

## Test

```powershell
& 'C:\Users\Faisa\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python.exe' -m pytest
```

## Build Executable

```powershell
& 'C:\Users\Faisa\AppData\Roaming\uv\python\cpython-3.14-windows-x86_64-none\python.exe' -m PyInstaller --clean --noconfirm --distpath dist-new --workpath build-new BedrockWallApp.spec
```

The rebuilt app is written to:

```text
dist-new/BedrockWallApp.exe
```
