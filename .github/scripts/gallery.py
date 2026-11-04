"""Spiegelt die freigegebenen Contest-Skins vom Discord-Bot in den Branch "gallery".
Die Adresse des Bots steht nur im Repository-Secret HUB_URL (nie im Code)."""
import json, os, re, shutil, sys, urllib.request

HUB = os.environ.get("HUB_URL", "").strip().rstrip("/")
OLD, NEW = sys.argv[1], sys.argv[2]
if not HUB:
    print("::notice::Secret HUB_URL fehlt – Galerie wird nicht aktualisiert.")
    sys.exit(0)


def get(path, limit=12 << 20):
    req = urllib.request.Request(HUB + path, headers={"User-Agent": "voidline-gallery"})
    with urllib.request.urlopen(req, timeout=40) as r:
        b = r.read(limit + 1)
        if len(b) > limit:
            raise ValueError("zu gross")
        return b


try:
    idx = json.loads(get("/gallery/index.json"))
except Exception as e:
    print("::warning::Galerie nicht erreichbar:", type(e).__name__)
    sys.exit(0)

items = []
os.makedirs(NEW, exist_ok=True)
for it in idx.get("items", [])[:500]:
    eid, prev = str(it.get("id", "")), str(it.get("preview", ""))
    if not re.fullmatch(r"[a-f0-9]{10}", eid) or not re.fullmatch(r"preview\.(png|jpg|webp)", prev):
        continue
    ok = True
    os.makedirs(os.path.join(NEW, eid), exist_ok=True)
    for fn in (prev, "skin.vskin"):
        src, dst = os.path.join(OLD, eid, fn), os.path.join(NEW, eid, fn)
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            continue
        try:
            with open(dst, "wb") as f:
                f.write(get(f"/gallery/{eid}/{fn}"))
        except Exception as e:
            print("::warning::Datei fehlt für", eid, fn, type(e).__name__)
            ok = False
    if ok:
        items.append({k: it.get(k) for k in ("id", "number", "round", "name", "desc", "ship", "rarity", "colors",
                                              "pattern", "user", "created", "votes", "winner", "preview")})
    else:
        shutil.rmtree(os.path.join(NEW, eid), ignore_errors=True)

out = {"version": 1, "round": idx.get("round"), "items": items}
with open(os.path.join(NEW, "index.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"{len(items)} Skins in der Galerie")
