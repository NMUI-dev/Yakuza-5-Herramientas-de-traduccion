# (claude2, 06-11-2026) Ideas del 2.º ciclo de preguntas (Kilo): ORDEN de variables (%s/%d/{...}/<Sign>) distinto del
# inglés; plurales «(s)»; caracteres de ancho completo/rotos que el inglés no tiene; botones (Back, Cancel, OK, Yes, No...)
# con varias traducciones. Solo marca. Uso: Y5_TEXTOS=... python -I -X utf8 ideas_ia2_y5.py > ideas_ia2.txt
import csv, os, re, collections
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0711/textos_v108_previsto.csv")
VAR = re.compile(r"%[sd]|\$\{[^}]*\}|\{[^}]*\}|<Sign:[^>]*>")
ROTO = re.compile(r"[\uff01-\uff5e\ufffd\u00c3\u00e2\u0080-\u009f]")
BOT = {"Back", "Cancel", "OK", "Yes", "No", "Confirm", "Select", "Exit", "Quit", "Return", "Next", "Close", "Continue", "Retry"}
botones = collections.defaultdict(collections.Counter)
n = collections.Counter()
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if not es:
        continue
    ve, vs = VAR.findall(en), VAR.findall(es)
    if len(ve) >= 2 and sorted(ve) == sorted(vs) and ve != vs and len(set(ve)) > 1:
        n["ORDEN"] += 1; print("ORDEN\t%s\t%s\t%s\t%s" % (r["id"], ve, vs, es[:100].replace("\n", " / ")))
    if re.search(r"\w\((?:s|es|as|os)\)", es):
        n["PLURAL"] += 1; print("PLURAL\t%s\t%s\t%s" % (r["id"], en[:70].replace("\n", " / "), es[:100].replace("\n", " / ")))
    rot = set(ROTO.findall(es)) - set(en)
    if rot:
        n["ROTO"] += 1; print("ROTO\t%s\t%r\t%s" % (r["id"], "".join(rot), es[:100].replace("\n", " / ")))
    if en.strip() in BOT:
        botones[en.strip()][es.strip()] += int(r["veces"] or 1)
for b, c in sorted(botones.items()):
    if len(c) > 1:
        n["BOTON"] += 1; print("BOTON\t%s\t%s" % (b, dict(c.most_common())))
print("total", dict(n))
