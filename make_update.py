"""Erzeugt update.json für eine neue Version des Skin Studios.
Ablauf: VoidlineSkinStudio.exe + update.json ins öffentliche GitHub-Repo (main-Branch) legen –
alle installierten Apps finden das Update automatisch, laden es im Hintergrund und installieren es beim nächsten Start.
python make_update.py VoidlineSkinStudio.exe 1.2.0 "Neu: ..."
"""
import hashlib, json, os, sys
exe, ver = sys.argv[1], sys.argv[2]
notes = sys.argv[3] if len(sys.argv) > 3 else ""
h = hashlib.sha256(open(exe, "rb").read()).hexdigest()
json.dump({"version": ver, "url": os.path.basename(exe), "sha256": h, "size": os.path.getsize(exe), "notes": notes},
          open(os.path.join(os.path.dirname(os.path.abspath(exe)), "update.json"), "w"), indent=2)
print("update.json geschrieben:", ver, h)
