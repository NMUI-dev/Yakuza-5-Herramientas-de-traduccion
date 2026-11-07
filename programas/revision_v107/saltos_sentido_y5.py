# (claude2, 06-11-2026) Renglón partido por mal sitio (Netflix es-419 / idea 53 de las IA): un renglón de subtítulo o
# globo que TERMINA en artículo, preposición, conjunción, «no», pronombre átono o «que». Solo marca; se arregla a mano.
# Uso: Y5_TEXTOS=... python -I -X utf8 saltos_sentido_y5.py > saltos_sentido.txt
import csv, os, re
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv")
MAL = {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "a", "en", "con", "por", "para", "sin",
       "y", "e", "o", "u", "ni", "que", "no", "me", "te", "se", "le", "les", "lo", "nos", "mi", "tu", "su", "mis", "tus", "sus"}
n = 0
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    es = re.sub(r"<[^>]*>", "", r["espanol"])
    if "\n" not in es or not r["donde"].startswith(("sub", "extra-sub", "msg", "pac")):
        continue
    for ren in es.split("\n")[:-1]:
        pal = re.findall(r"[\wáéíóúñü]+$", ren.strip().lower())
        if pal and pal[0] in MAL and not ren.rstrip().endswith((".", ",", "!", "?", "…", ":", ";")):
            n += 1; print("%s\t%s\t%s" % (r["id"], pal[0], r["espanol"].replace("\n", " / ")[:150])); break
print("total", n)
