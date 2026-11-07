# (claude2, 06-11-2026) Junta los cambios de la v1.0.7 por prioridad (mano > groserías revisadas > signos) ->
# correcciones_0611b.json {id: en, antes, es, motivo, fuente} + textos_v107_previsto.csv. Frena si una corrección rompe
# etiquetas <...>, %s, ⑬, (改行) o cambia el número de saltos. Los choques (mismo id en dos archivos) se listan.
# Uso: python -I -X utf8 juntar.py
import csv, json, re, sys
from pathlib import Path
csv.field_size_limit(10 ** 9)
T = "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv"
FILAS = list(csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"))
R = {r["id"]: r for r in FILAS}
ORDEN = ["cambios_manual.json", "cambios_censura_ok.json", "cambios_signos_1.json", "cambios_signos_2.json"]
MARCAS = re.compile(r"<[^>]*>|%[sd]|\{[^}]*\}|⑬|⑮|\(改行\)|♪")
def marcas(s):
    return sorted(m for m in MARCAS.findall(s) if not m.lower().startswith(("<italic", "</italic")))
import importlib.util
_s = importlib.util.spec_from_file_location("h", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/herramienta_traduccion.py")
h = importlib.util.module_from_spec(_s); _a = sys.argv; sys.argv = ["x"]; _s.loader.exec_module(h); sys.argv = _a
norm, LETRAS = h.norm, h.LETRAS
CORTAS = json.load(open("C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/datos/cortas.json", encoding="utf-8"))
final, choques, malos, largos = {}, [], [], []
for f in ORDEN:
    if not Path(f).exists():
        print("FALTA", f); continue
    for i, x in json.load(open(f, encoding="utf-8")).items():
        if i not in R:
            malos.append((i, f, "id no existe")); continue
        es = x["es"].replace(" / ", "\n") if "\n" not in x["es"] and R[i]["espanol"].count("\n") else x["es"]
        if i in final:
            choques.append((i, final[i]["fuente"], f, final[i]["es"], es)); continue
        r = R[i]
        if marcas(es) != marcas(r["espanol"]):
            malos.append((i, f, "marcas %s -> %s" % (marcas(r["espanol"]), marcas(es)))); continue
        if es.count("\n") != r["espanol"].count("\n"):
            malos.append((i, f, "saltos %d -> %d" % (r["espanol"].count("\n"), es.count("\n")))); continue
        if es == r["espanol"]:
            continue
        # globos (pac): el español no puede ocupar más bytes que el inglés (con ¡ í Í ya cambiados como la herramienta),
        # o la herramienta deja el INGLÉS. Las cortas de datos/cortas.json mandan en los pac (si existe, no se usa esta).
        if r["donde"].startswith("pac") and norm(r["ingles"]) not in CORTAS:
            if len(es.translate(LETRAS).encode("utf-8")) > len(r["ingles"].encode("utf-8")):
                largos.append((i, f, es, len(es.translate(LETRAS).encode("utf-8")), len(r["ingles"].encode("utf-8")))); continue
        final[i] = {"en": r["ingles"], "antes": r["espanol"], "es": es, "motivo": x.get("motivo", ""), "fuente": f}
# --- renglones partidos por sentido (Netflix es-419; idea 53 de las IA): la palabra suelta al final de un renglón
# (artículo, preposición, «que», «no»...) pasa al renglón siguiente si ese renglón no queda más largo que el renglón más
# largo que ya tenía el texto (nada se sale de la caja; mismos bytes). Subtítulos, diálogos y globos.
MAL = {"el", "la", "los", "las", "un", "una", "unos", "unas", "de", "del", "al", "a", "en", "con", "por", "para", "sin",
       "y", "e", "o", "u", "ni", "que", "no", "me", "te", "se", "le", "les", "lo", "nos", "mi", "tu", "su", "mis", "tus", "sus"}
VIS = lambda s: len(re.sub(r"<[^>]*>", "", s))
def resaltar(es):
    ren = es.split("\n"); tope = max(VIS(x) for x in ren); cambio = False
    for k in range(len(ren) - 1):
        a0, b0 = ren[k], ren[k + 1]
        for _ in range(4):   # «de la» / «antes de que»: se mueven las palabras sueltas que haga falta (máx. 4)
            a = ren[k].rstrip(" ")
            m = re.search(r"(?:^|\s)([\wáéíóúñüÁÉÍÓÚÑ]+)$", a)
            if not m or m.group(1).lower() not in MAL or "<" in a[m.start(1):] or not ren[k + 1].strip() or m.start(1) == 0:
                break
            ren[k] = a[:m.start(1)].rstrip(" ") + ren[k][len(a):]
            ren[k + 1] = m.group(1) + " " + ren[k + 1].lstrip(" ")
        a = ren[k].rstrip(" ")
        fin = re.findall(r"[\wáéíóúñü]+$", a.lower())
        if VIS(ren[k + 1]) > tope or not a.strip() or (fin and fin[0] in MAL):
            ren[k], ren[k + 1] = a0, b0      # no cabe o no se pudo dejar bien: se deja como estaba
        elif (ren[k], ren[k + 1]) != (a0, b0):
            cambio = True
    return "\n".join(ren) if cambio else es
n_salto = 0
for r in FILAS:
    i = r["id"]
    if not r["donde"].startswith(("sub", "extra-sub", "msg", "pac")):
        continue
    es = final[i]["es"] if i in final else r["espanol"]
    if "\n" not in es:
        continue
    nuevo = resaltar(es)
    if nuevo != es and marcas(nuevo) == marcas(es) and nuevo.count("\n") == es.count("\n") \
            and len(nuevo.encode("utf-8")) == len(es.encode("utf-8")):
        n_salto += 1
        if i in final:
            final[i]["es"] = nuevo; final[i]["motivo"] += "; renglón partido por sentido"
        else:
            final[i] = {"en": r["ingles"], "antes": r["espanol"], "es": nuevo, "motivo": "renglón partido por sentido", "fuente": "juntar.py"}
print("renglones partidos por sentido:", n_salto)
# --- filas NUEVAS: últimos renglones de correo (mail.bin) que el filtro es_texto tomaba por códigos y quedaban en
# INGLÉS (filtro_mayusculas.py, 06-11). La herramienta v1.0.7 los acepta (CORTAS_SI, ver datos_v107.py).
NUEVAS = {"board.": "Kansai.", "then.": "entonces.", "audition.": "audición.", "name.": "nombre.", "danger.": "peligro.",
          "children.": "hijos.", "though.": "de todos modos.", "themselves.": "deja.", "here.": "aquí.",
          "judge.": "invitado.", "again.": "de nuevo.", "demo.": "demo.", "interested.": "interesado."}
sig = max(int(r["id"]) for r in FILAS) + 1
for en, es in NUEVAS.items():
    FILAS.append({"id": str(sig), "donde": "ptr | scenario_en/mail.bin (final de correo, nuevo v1.0.7)", "veces": "1", "ingles": en, "espanol": es})
    final[str(sig)] = {"en": en, "antes": "", "es": es, "motivo": "final de correo que quedaba en inglés", "fuente": "juntar.py NUEVAS"}
    sig += 1
json.dump(final, open("correcciones_0611b.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for r in FILAS:
    if r["id"] in final:
        r["espanol"] = final[r["id"]]["es"]
with open("textos_v107_previsto.csv", "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(FILAS[0].keys()), delimiter=";", quoting=csv.QUOTE_ALL)
    w.writeheader(); w.writerows(FILAS)
with open("juntar.txt", "w", encoding="utf-8") as o:
    o.write("correcciones %d | choques %d | rechazadas %d\n" % (len(final), len(choques), len(malos)))
    for c in choques:
        o.write("CHOQUE %s gana %s sobre %s\n   gana: %s\n   otra: %s\n" % (c[0], c[1], c[2], c[3].replace("\n", " / "), c[4].replace("\n", " / ")))
    for m in malos:
        o.write("RECHAZADA %s %s %s\n" % m)
    for l in largos:
        o.write("NO CABE (pac) %s %s %r %d>%d bytes\n" % l)
print(open("juntar.txt", encoding="utf-8").readline().strip())
