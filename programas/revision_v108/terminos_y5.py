# (claude2, 06-11-2026) Un término de juego, UNA traducción (idea de las IA y regla 3 del LEEME común). Para cada término
# inglés cuenta las variantes españolas que aparecen en las frases que lo llevan. Solo marca; se decide a mano.
# Uso: Y5_TEXTOS=... python -I -X utf8 terminos_y5.py > terminos.txt
import csv, os, re, collections
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0611b/textos_v107_previsto.csv")
TERM = {
 r"heat actions?": ["acci[oó]n(?:es)? heat", "acci[oó]n(?:es)? de calor", "heat actions?", "t[eé]cnicas? heat", "ataques? heat"],
 r"heat (?:gauge|meter)": ["barra (?:de )?heat", "medidor (?:de )?heat", "indicador (?:de )?heat", "barra de calor", "medidor de calor", "indicador de calor"],
 r"substor(?:y|ies)": ["subhistorias?", "historias? secundarias?", "subtramas?", "misi[oó]n(?:es)? secundarias?"],
 r"completion list": ["lista de logros", "lista de objetivos", "lista de completado", "lista de compleci[oó]n", "lista de terminaci[oó]n"],
 r"hostess(?:es)?": ["anfitrionas?", "hostess", "acompañantes?", "chicas? de compañ[ií]a"],
 r"hostess clubs?": ["clubs? de anfitrionas", "clubs? de cabar[eé]", "clubs? nocturnos?", "clubes de cabar[eé]", "clubes de anfitrionas"],
 r"locker keys?": ["llaves? de casillero", "llaves? de taquilla", "llaves? de consigna"],
 r"\bskill points?\b|\bability points?\b": ["puntos? de habilidad", "puntos? de destreza"],
 r"\bexperience points?\b|\bEXP\b": ["puntos? de experiencia", "\bEXP\b", "experiencia"],
 r"\bhealth\b": ["salud", "vida", "\bPV\b", "energ[ií]a"],
 r"\bcabaret\b": ["cabar[eé]", "cabaret"],
 r"\bpachinko\b": ["pachinko"],
 r"\bmahjong\b": ["mahjong", "mah-jong"],
 r"\byakuza\b": ["yakuza", "yakuzas"],
 r"\bfamily\b(?= [A-Z]|\b)": ["familia"],
 r"\bpatriarch\b": ["patriarca", "jefe de familia", "cabeza de familia"],
 r"\bchairman\b": ["presidente", "jefe del clan"],
 r"\bcaptain\b": ["capit[aá]n", "teniente"],
 r"\bhunter\b": ["cazador", "cazadora"],
}
cuenta = {k: collections.Counter() for k in TERM}
ejemplo = collections.defaultdict(list)
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"].lower()
    if not es:
        continue
    for k, vs in TERM.items():
        if re.search(k, en, re.I):
            hallado = [v for v in vs if re.search(v, es, re.I)]
            clave = hallado[0] if hallado else "(ninguna)"
            cuenta[k][clave] += 1
            if len(ejemplo[(k, clave)]) < 3:
                ejemplo[(k, clave)].append((r["id"], en[:70].replace("\n", " / "), r["espanol"][:90].replace("\n", " / ")))
for k, c in cuenta.items():
    if not c:
        continue
    print("== %s : %s" % (k, dict(c.most_common())))
    if len([x for x in c if x != "(ninguna)"]) > 1:
        for clave, _ in c.most_common()[1:]:
            for e in ejemplo[(k, clave)]:
                print("     [%s] %s | %s || %s" % (clave, e[0], e[1], e[2]))
