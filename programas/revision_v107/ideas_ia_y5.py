# (claude2, 06-11-2026) Comprobaciones salidas de la pregunta en cadena a las IA (cadena/lista_acumulada.md):
#  JAPONES  kana/kanji en el español que el inglés no tiene (idea 12)
#  ARTICULO artículo delante de un nombre de objeto <Color:...> que no concuerda (idea 47; caso real: «el <Color:8>Barbacoa»)
# Uso: Y5_TEXTOS=... python -I -X utf8 ideas_ia_y5.py > ideas_ia.txt   (solo marca)
import csv, os, re
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv")
JA = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")
ART = re.compile(r"\b(el|un|la|una|los|unos|las|unas|del|al) <Color:[^>]*>([^<]+)<Color", re.I)
FEM_SG = re.compile(r"^(?:[A-ZÁÉÍÓÚ]?\w*(?:a|ión|dad|tad|tud|umbre))(?: |$)")
n = {"JAPONES": 0, "ARTICULO": 0}
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if es and JA.search(es) and not JA.search(en):
        n["JAPONES"] += 1; print("JAPONES\t%s\t%s\t%s" % (r["id"], en[:80].replace("\n", " / "), es[:100].replace("\n", " / ")))
    for m in ART.finditer(es):
        art, nom = m.group(1).lower(), m.group(2).strip()
        pal = nom.split()[0] if nom.split() else ""
        plural = pal.endswith("s") and not pal.endswith(("is", "us"))
        fem = bool(FEM_SG.match(pal)) and not plural and pal.lower() not in ("día", "mapa", "sistema", "tema", "problema", "programa", "planeta", "idioma", "drama", "poema", "clima", "sofá")
        malo = (art in ("el", "un", "del", "al") and (fem or plural)) or (art in ("la", "una") and (plural or not fem)) \
            or (art in ("los", "unos") and not plural) or (art in ("las", "unas") and not plural)
        if malo:
            n["ARTICULO"] += 1; print("ARTICULO\t%s\t%s %s\t%s" % (r["id"], art, nom, es[:120].replace("\n", " / ")))
print("total", n)
