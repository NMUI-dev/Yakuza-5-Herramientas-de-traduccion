# (claude2, 07-11-2026) Punto y coma de cierre FUERA de las comillas (RAE; Netflix es-419; idea de claude1: 38 en el Y6):
# «...canción "Machine Gun Kiss." Puede» -> «...canción "Machine Gun Kiss". Puede». Solo las comillas de CIERRE (número
# impar de comillas antes) y nunca en subtítulos (sub/extra-sub: ahí las comillas de fuera son del formato del archivo).
# Mismos bytes (se intercambian dos letras). Uso: python -I -X utf8 comillas_y5.py -> cambios_comillas.json
import csv, json, os, re
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0711/textos_v108_previsto.csv")
out = {}
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    es = r["espanol"]
    if r["donde"].startswith(("sub", "extra-sub")) or '"' not in es:
        continue
    b = list(es); n = 0; i = 0
    while i < len(b):
        if b[i] == '"':
            n += 1
            if n % 2 == 0 and i > 0 and b[i - 1] in ".," and not (i > 2 and b[i - 3:i] == list("...")):
                b[i - 1], b[i] = b[i], b[i - 1]
        i += 1
    nuevo = "".join(b)
    if nuevo != es:
        out[r["id"]] = {"es": nuevo, "motivo": "punto/coma fuera de las comillas (RAE)"}
json.dump(out, open("cambios_comillas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "cambios")
for i, x in list(out.items())[:8]:
    print(" ", i, x["es"][:110].replace("\n", " / "))
