# Voidline Skin Studio

Windows-App zum Gestalten von Schiffs-Skins für **Voidline Arena** (Roblox).

**Download:** [Neueste Version (Releases)](https://github.com/SHCNoel/voidline-skin-studio/releases/latest) → `VoidlineSkinStudio.exe` unter *Assets* – Doppelklick, dann „Jetzt installieren“.

## Automatische Updates
Die App prüft beim Start und alle 3 Stunden die Datei [`update.json`](update.json) in diesem Repo.
Ist dort eine höhere Version eingetragen, lädt sie die neue `VoidlineSkinStudio.exe` im Hintergrund,
prüft die SHA-256-Prüfsumme und installiert sie beim nächsten Start (oder sofort per „Neu starten“).

### Neue Version veröffentlichen
1. Neue `VoidlineSkinStudio.exe` in dieses Repo legen.
2. `python make_update.py VoidlineSkinStudio.exe 1.2.0 "Was ist neu"` ausführen – schreibt `update.json`.
3. Beide Dateien committen und pushen. GitHub legt automatisch einen Release an, und alle Apps aktualisieren sich selbst.

> Das Repo muss **öffentlich** sein, damit die App die Dateien ohne Login abrufen kann.
