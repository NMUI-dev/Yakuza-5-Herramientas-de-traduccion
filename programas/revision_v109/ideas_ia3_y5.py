# (claude2, 07-11-2026) Ideas de Gemini en la ronda final del ciclo de preguntas:
#  ESCALA  «billion» = mil millones (NO «billón», que en español es un millón de millones); «trillion» = billón
#  CODIGO  códigos de letra+cifra (casilleros C1, E1...; zonas A-5) iguales en inglés y español
# Uso: Y5_TEXTOS=... python -I -X utf8 ideas_ia3_y5.py > ideas_ia3.txt   (solo marca)
import csv, os, re, collections
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0711/textos_v108_previsto.csv")
COD = re.compile(r"(?<![\w-])[A-Z]-?\d{1,2}(?![\w])")
n = collections.Counter()
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if not es:
        continue
    if re.search(r"\bbillions?\b", en, re.I) and (re.search(r"\bbill[oó]n", es, re.I) or not re.search(r"mil millones", es, re.I)):
        n["ESCALA"] += 1; print("ESCALA\t%s\t%s || %s" % (r["id"], en[:100].replace("\n", " / "), es[:110].replace("\n", " / ")))
    if re.search(r"\btrillions?\b", en, re.I) and not re.search(r"\bbill[oó]n", es, re.I):
        n["ESCALA"] += 1; print("ESCALA\t%s\t%s || %s" % (r["id"], en[:100].replace("\n", " / "), es[:110].replace("\n", " / ")))
    ce, cs = sorted(COD.findall(re.sub(r"<[^>]*>", "", en))), sorted(COD.findall(re.sub(r"<[^>]*>", "", es)))
    if ce != cs and ce:
        n["CODIGO"] += 1; print("CODIGO\t%s\t%s %s\t%s || %s" % (r["id"], ce, cs, en[:80].replace("\n", " / "), es[:90].replace("\n", " / ")))
print("total", dict(n))
