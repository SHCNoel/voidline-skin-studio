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

## Neu in 1.4
- **Animierte Skins**: Video (MP4/WebM, max. 10 s) hinzufügen – daraus werden 4–16 Einzelbilder, die auf dem Schiff abgespielt werden. Der Export enthält alle Bilder und einen `Frames`-Ordner in der `.rbxmx`.
- **Bilder-Browser**: „Bilder im Internet suchen“ öffnet ein Browser-Fenster (Pixabay, ambientCG, Poly Haven …). Über ein Bild fahren → „In Skin übernehmen“. Bilder lassen sich auch aus Chrome/Edge direkt ins Studio ziehen.
- **Community-Galerie**: freigegebene Skins aus dem Discord-Contest ansehen und als Remix öffnen.
- **Aus Text erstellen**: Skin aus einer Beschreibung wie „roter Drache mit goldenen Streifen“.

