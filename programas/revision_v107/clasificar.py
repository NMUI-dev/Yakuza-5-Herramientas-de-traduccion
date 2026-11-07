# (claude2, 06-11-2026) Separa los cambios de un ayudante en «solo signos» (quitando ¡¿?!.,… y espacios queda igual) y
# «texto» (cambia palabras), para revisar todos los de texto y una muestra de los de signos.
# Uso: python -I -X utf8 clasificar.py cambios_X.json > rev_X.txt
import csv, json, re, sys
csv.field_size_limit(10 ** 9)
R = {r["id"]: r for r in csv.DictReader(open("C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv",
                                             encoding="utf-8-sig", newline=""), delimiter=";")}
d = json.load(open(sys.argv[1], encoding="utf-8"))
q = lambda s: re.sub(r"[¡¿?!.,…\s]", "", s).lower()
f = lambda s: s.replace("\n", " / ")
solo, texto = [], []
for i, x in d.items():
    (solo if q(x["es"]) == q(R[i]["espanol"]) else texto).append(i)
print("solo signos", len(solo), "| texto", len(texto))
for i in texto:
    print("T", i, "|", f(R[i]["ingles"])[:160]); print("   -", f(R[i]["espanol"])[:170]); print("   +", f(d[i]["es"])[:170], "  [", d[i].get("motivo", "")[:60], "]")
print("=== SOLO SIGNOS")
for i in solo:
    print("S", i, "|", f(R[i]["espanol"])[:110], "=>", f(d[i]["es"])[:110])
