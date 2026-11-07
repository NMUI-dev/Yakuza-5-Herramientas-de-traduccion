# (claude2, 06-11-2026) Regla del usuario: NUNCA CENSURAR. Marca textos cuyo inglés lleva una grosería fuerte y cuyo
# español no lleva ninguna (posible suavizado). Solo marca: se decide a mano con la escena delante.
# Uso: python -I -X utf8 censura_y5.py > censura.txt
import csv, re
csv.field_size_limit(10 ** 9)
import os
TEXTOS = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv")   # Y5_TEXTOS = otro CSV (p. ej. el previsto de la v1.0.7)
EN = re.compile(r"\b(?:fuck\w*|motherfuck\w*|shit\w*|bullshit|bitch\w*|bastard\w*|asshole\w*|ass\b|dick\w*|prick\w*|"
                r"cunt\w*|whore\w*|son of a bitch|goddamn\w*|damn\w*|piss\w*|crap\w*|hell\b)", re.I)
FUERTE = re.compile(r"\b(?:fuck|motherfuck|shit|bullshit|bitch|bastard|asshole|cunt|whore|son of a bitch|prick|dick)", re.I)
ES = re.compile(r"(?:mierd|carajo|cabr[oó]n|cabrona|puta|put[oa]s?\b|jod|maldit|desgraciad|imb[eé]cil|idiota|pendej|"
                r"culo|perra|zorra|bastard|malnacid|infeliz|maldici[oó]n|demonio|diablo|estúpid|mamarrach|carajos|"
                r"hijo de|sinvergüenza|gusano|basura|rata|cerdo|cretino|tarad|animal|maricón|miserable|condenad|porquería|"
                r"cagar|cag[oóa]|chingad|verga|huev|infierno|rayos|caray|caramba)", re.I)
n = 0
for r in csv.DictReader(open(TEXTOS, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if not es or not EN.search(en) or ES.search(es):
        continue
    nivel = "FUERTE" if FUERTE.search(en) else "suave"
    n += 1
    print("%s\t%s\t%s\t%s\t%s" % (nivel, r["id"], r["donde"][:40], en.replace("\n", " / "), es.replace("\n", " / ")))
print("total", n)
