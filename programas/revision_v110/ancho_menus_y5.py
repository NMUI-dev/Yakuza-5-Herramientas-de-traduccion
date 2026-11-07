# (claude2, 07-11-2026) Ancho EN PÍXELES de los textos de menú (tablas) con la fuente del juego (sd_hankaku.dds: casilla
# de 16x32 por letra; ancho = columnas con tinta + 2 de separación). Marca los textos cuyo renglón más ancho supera el
# renglón inglés más ancho de su columna: ahí el juego nunca pintó algo tan ancho. Solo marca.
# Uso: python -I -X utf8 ancho_menus_y5.py > ancho_menus.txt
import csv, os, re, collections
import numpy as np
from PIL import Image
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0711b/textos_v109_previsto.csv")
a = np.asarray(Image.open(r"C:\Mods\yakuza5\trabajo\fuente\add\font_hd_en\gothic_en\sd_hankaku.dds").convert("RGBA"))[..., 3]
ANCHO = {}
for i in range(256):
    x, y = (i % 16) * 16, (i // 16) * 32
    col = np.where(a[y:y + 32, x:x + 16].max(0) > 60)[0]
    ANCHO[i + 0x20] = (col.max() - col.min() + 1 + 2) if len(col) else 6
LET = {"¡": "½", "í": "`", "Í": "|"}
def px(s):
    s = re.sub(r"<[^>]*>", "", s)
    return max(sum(ANCHO.get(ord(LET.get(c, c)), 16) for c in ren) for ren in s.replace("\r\n", "\n").split("\n"))
filas = [r for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";") if r["donde"].startswith("tabla")]
tope = collections.Counter()
for r in filas:
    col = r["donde"].split(":")[0] + ":" + r["donde"].split(":")[-1].split(" ")[0] if ":" in r["donde"] else r["donde"]
    r["_col"] = r["donde"].rsplit(":", 1)[0] + ":" + re.sub(r"\d+$", "", r["donde"].rsplit(":", 1)[-1])
    tope[r["_col"]] = max(tope[r["_col"]], px(r["ingles"]))
n = collections.Counter()
for r in filas:
    if not r["espanol"].strip():
        continue
    pe, pt = px(r["espanol"]), tope[r["_col"]]
    if pe > pt * 1.05 and pe - pt >= 12:
        n[r["_col"]] += 1
        print("%d > %d px\t%s\t%s\t%s\t%s" % (pe, pt, r["id"], r["_col"][:60], r["ingles"][:50].replace("\n", " / "), r["espanol"][:70].replace("\n", " / ")))
print("marcados:", sum(n.values()))
for k, v in n.most_common(30):
    print("  %3d  %s" % (v, k))
