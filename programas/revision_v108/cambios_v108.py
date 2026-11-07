# (claude2, 06-11-2026) v1.0.8: subtítulos que piden leer demasiado rápido (velocidad_y5.py) acortados de forma natural,
# con los mismos renglones. Cada cambio se aplica también a la copia «extra-sub» (mismo inglés sin comillas) si existe.
# Además: término único (terminos_y5.py). Uso: python -I -X utf8 cambios_v108.py -> cambios_v108.json
import csv, json, re
csv.field_size_limit(10 ** 9)
T = "C:/Mods/yakuza5/trabajo/revision_0611b/textos_v107_previsto.csv"
FILAS = list(csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"))
R = {r["id"]: r for r in FILAS}
por_en = {}
for r in FILAS:
    por_en.setdefault(r["ingles"].replace("\r\n", "\n"), []).append(r)
out = {}


def nuevo(i, es, motivo):
    r = R[i]; en = r["ingles"].replace("\r\n", "\n")
    assert es.count("\n") == r["espanol"].count("\n"), (i, "saltos")
    out[i] = {"es": es, "motivo": motivo}
    if en.startswith('"') and en.endswith('"'):            # la gemela extra-sub: sin comillas y con las de dentro simples
        gem = en[1:-1].replace('""', '"')
        for g in por_en.get(gem, []):
            if g["donde"].startswith("extra-sub"):
                out[g["id"]] = {"es": es[1:-1].replace('""', '"') if es.startswith('"') else es, "motivo": motivo + " (copia extra-sub)"}


V = "lectura demasiado rápida: acortado"
nuevo("2153", '"Llenando de esperanza a quien la escucha,\nles presento a la única chica prodigio..."', V)
nuevo("2089", '"Aquí, las participantes\nbailarán una canción rápida..."', V)
nuevo("2079", '"¡Esta revolucionaria tecnología permite que\nlas participantes compitan concierto contra concierto!"', V)
nuevo("3349", '"Saejima-san contactó a Kosaka-san\npoco después de que todo se fuera a la mierda."', V)
nuevo("2428", "¡Aún llegas a la imprenta!", V)
nuevo("1878", '"No eres ni un uno por ciento tan antipático\ncomo el típico ejecutivo del espectáculo."', V)
nuevo("2712", "Sawada, de 197 victorias, traspasado a los Wyverns", V)
nuevo("2946", '"¡Los 300 millones son la indemnización\nque se pagaría a los organizadores!"', V)
nuevo("1695", "Por un tiempo, salió sorprendentemente bien.", V)
nuevo("484", "¡Así no actúa un yakuza!", V)
nuevo("2875", '"Estas huellas coinciden con las\ndel asesinato de Morinaga."', V)
nuevo("67", "Pero hago lo posible por seguir este camino.", V)
nuevo("2162", '"La Princess League tiene el sistema de batalla\nmás emocionante... ¡Quizá el mejor jamás creado!"', V)
nuevo("1240", "Debimos estar listos desde el primer día.", V)
nuevo("1946", "No hay palabras para disculparme.", V)
nuevo("2174", "Las participantes bailarán una canción rápida.", V)
nuevo("87", "Mis tarifas.", V)
nuevo("3552", "A todos los presentes.", V)
nuevo("884", "Pero tras tantos años en la policía...", V + "; sentido: the force = la policía")
nuevo("2126", "Sus elegantes pasos de baile...", V + "; errata (Suselegantes)")
nuevo("1843", "Luego tú y yo hablaremos largo y tendido.", V)
nuevo("360", '"Todos miran a esta ciudad\ncomo si fuera la zona cero."', V + "; ground zero = zona cero")
nuevo("518", '"Tendríamos a la policía\npisándonos los talones."', V)
nuevo("2116", '"Para nuestra idol afortunada,\nla Princess League abrirá puertas."', V)
nuevo("1655", '"Así que le dejo a Horie una nota\ncon lo que debe hacer mientras no esté."', V)
nuevo("2898", '"¿Así que deja su miserable territorio de Sotenbori\nlibre para nosotros?"', V)

# ORDEN de variables (ideas_ia2_y5.py, idea de Kilo en el 2.º ciclo): string_tbl.bin es una cadena de formato; si el
# español pone %s antes que %d, el número cae donde va el nombre del pez (basura o cierre del juego). Mismo orden que el inglés.
out["8651"] = {"es": "¡Atrapaste un ejemplar de %d cm de <Color:8>%s<Color:Default>!", "motivo": "orden de variables %d/%s como el inglés (cadena de formato)"}
out["8652"] = {"es": "¡Atrapaste un ejemplar de %d cm de <Color:8>%s<Color:Default>!\n<Color:5>¡Un nuevo récord!", "motivo": "orden de variables %d/%s como el inglés (cadena de formato)"}

# FALSOS AMIGOS (falsos_amigos_y5.py, idea del 2.º ciclo de preguntas): eventually != eventualmente, assume = suponer,
# sympathy = compasión. Los subtítulos se cambian en sus dos copias (fila «sub» con comillas y «extra-sub»).
def cambiar(i, viejo, nuevo_, motivo):
    r = R[i]; es = out.get(i, {}).get("es", r["espanol"])
    assert viejo in es, (i, viejo)
    out[i] = {"es": es.replace(viejo, nuevo_), "motivo": (out[i]["motivo"] + "; " if i in out else "") + motivo}
    en = r["ingles"].replace("\r\n", "\n")
    if r["donde"].startswith("extra-sub"):                      # su gemela «sub» con comillas
        for g in por_en.get('"' + en.replace('"', '""') + '"', []):
            if viejo in g["espanol"]:
                cambiar_g = g["espanol"].replace(viejo, nuevo_)
                out[g["id"]] = {"es": cambiar_g, "motivo": motivo + " (copia sub)"}
FA = "falso amigo"
cambiar("24406", "eventualmente tenemos que ponernos", "tarde o temprano tenemos que ponernos", FA + ": eventually = tarde o temprano")
cambiar("27453", "Eventualmente.", "Al final, sí.", FA + ": eventually = al final")
cambiar("42679", "Eventualmente.", "Tarde o temprano.", FA + ": eventually = tarde o temprano")
cambiar("67575", "eventualmente aparecieras.", "por fin aparecieras.", FA + ": eventually = por fin")
cambiar("25150", "la gente asumirá automáticamente", "la gente dará por hecho", FA + ": assume = dar por hecho")
cambiar("57101", "van a asumir que", "van a suponer que", FA + ": assume = suponer")
cambiar("68591", "es seguro asumir que", "podemos suponer que", FA + ": assume = suponer")
cambiar("52714", "un poquito de simpatía?", "un poquito de compasión?", FA + ": sympathy = compasión")
cambiar("37399", "los votos de simpatía.", "los votos por lástima.", FA + ": sympathy votes = votos por lástima")
cambiar("51466", "Así que, aunque termine por gustar mucho a alguien, tendré que asumir que no sentiré lo mismo por esa persona.",
        "Así que, aunque alguien me termine gustando mucho, tengo que dar por hecho que no le gustaré.",
        FA + ": assume = dar por hecho; sentido: they won't like me back = no le gustaré")
cambiar("13059", "Un director de prisión severo que castiga", "Un hombre muy estricto con la disciplina que castiga",
        "sentido: el inglés no dice que sea el director (luego atacan al director)")
cambiar("13059", "Sin embargo, después de que Saejima fuera expulsado del Clan Tojo, comienza a mostrarle simpatía poco a poco.",
        "Tenía a Saejima en la mira como posible alborotador, pero después de que lo expulsaran del Clan Tojo, poco a poco empieza a simpatizar con él.",
        "sentido: faltaba la frase «He had his eye on Saejima»")

# término único (terminos_y5.py): «health» = «salud» como en la saga oficial (571 contra 4); «hostess club» = «club de
# anfitrionas» (hostess = anfitriona en 162 frases). Solo en frases cuyo inglés lo dice (y no dice «life» / «cabaret»).
HEALTH, LIFE = re.compile(r"\bhealth\b", re.I), re.compile(r"life|live", re.I)   # «lifestyle» = vida (27745)
HCLUB, CABARET = re.compile(r"hostess club", re.I), re.compile(r"cabaret", re.I)
for r in FILAS:
    i, en = r["id"], r["ingles"]
    es = out.get(i, {}).get("es", r["espanol"])
    n = es
    if HEALTH.search(en) and not LIFE.search(en):
        n = re.sub(r"\bvida\b", "salud", n)
        n = re.sub(r"\bVida\b", "Salud", n)
    if HCLUB.search(en) and not CABARET.search(en):
        n = re.sub(r"\b([Cc]lub)(es)? de cabar[eé]", lambda m: m.group(1) + (m.group(2) or "") + " de anfitrionas", n)
    if n != es:
        out[i] = {"es": n, "motivo": (out[i]["motivo"] + "; " if i in out else "") +
                  "término único (health = salud / hostess club = club de anfitrionas)"}
json.dump(out, open("cambios_v108.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "cambios")
