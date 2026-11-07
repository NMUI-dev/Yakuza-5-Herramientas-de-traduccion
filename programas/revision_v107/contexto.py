# (claude2, 06-11-2026) Para cada aviso (archivo .txt con «TIPO<tab>id<tab>...» por línea) escribe la escena alrededor
# (orden y hablante de escenas.jsonl; texto español ACTUAL de la v1.0.6) -> <nombre>_ctx.txt. Así se decide con la escena.
# Uso: python -I -X utf8 contexto.py avisos.txt [lineas_a_cada_lado=4]
import csv, json, sys
csv.field_size_limit(10 ** 9)
T = "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv"
ESC = "C:/Mods/yakuza5/trabajo/revision_contexto_0611/escenas.jsonl"
R = {r["id"]: r for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";")}
donde = {}
escenas = [json.loads(l) for l in open(ESC, encoding="utf-8")]
for s in escenas:
    for i, x in enumerate(s["l"]):
        donde.setdefault(x["id"], (s, i))
avisos = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8") if "\t" in l]
k = int(sys.argv[2]) if len(sys.argv) > 2 else 4
fuera = sys.argv[1].rsplit(".", 1)[0] + "_ctx.txt"
with open(fuera, "w", encoding="utf-8") as o:
    for a in avisos:
        i = a[1]
        o.write("### id %s  [%s]  %s\n" % (i, a[0], R[i]["donde"] if i in R else "?"))
        if i in donde:
            s, n = donde[i]
            L = s["l"]
            for j in range(max(0, n - k), min(len(L), n + k + 1)):
                y = L[j]; es = R[y["id"]]["espanol"] if y["id"] in R else y["es"]
                o.write((">> " if j == n else "   ") + "[%s] %s || %s\n" % (y["q"], y["en"].replace("\n", " / "), es.replace("\n", " / ")))
        else:
            o.write(">> %s || %s\n" % (R[i]["ingles"].replace("\n", " / "), R[i]["espanol"].replace("\n", " / ")))
        o.write("\n")
print(len(avisos), "->", fuera)
