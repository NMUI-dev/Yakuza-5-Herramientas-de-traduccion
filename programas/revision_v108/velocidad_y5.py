# (claude2, 06-11-2026) Velocidad de lectura de los subtítulos de las cinemáticas del Y5 (idea de las IA; Netflix pide
# máx. ~17 letras/s, nosotros 20 porque el juego fija los tiempos). auth/subtitle.par: CSV UTF-16, una fila por subtítulo:
# col 0/1 = fotograma de entrada/salida (30 por segundo), col 2 = texto. Compara el armado (v107_check/x) con el inglés
# original (extraido_en) fila a fila. Marca: más de 20 letras/s Y más de 1,25 veces el inglés. Solo marca.
# Uso: python -I -X utf8 velocidad_y5.py > velocidad.txt
import os, re
EN = "C:/Mods/yakuza5/entrega_v107/Herramientas para traduccion/trabajo/extraido_en/auth_subtitle"
ES = "C:/Mods/yakuza5/trabajo/v107_check/x/auth_subtitle.par"
FPS = 30.0
def filas(p):
    t = open(p, "rb").read().decode("utf-16")
    out, buf = [], ""
    for linea in t.split("\r\n"):         # un salto suelto (\n) dentro del texto no corta la fila
        if not linea.strip():
            continue
        out.append(linea.split("\t"))
    return out
letras = lambda s: len(re.sub(r"<[^>]*>|\s|\"", "", s))
malos, total = [], 0
for f in sorted(os.listdir(EN)):
    if not f.lower().endswith(".csv") or not os.path.exists(os.path.join(ES, f)):
        continue
    a, b = filas(os.path.join(EN, f)), filas(os.path.join(ES, f))
    for x, y in zip(a, b):
        if len(x) < 3 or len(y) < 3 or not x[0].isdigit():
            continue
        seg = (int(x[1]) - int(x[0])) / FPS
        if seg <= 0 or not y[2].strip():
            continue
        total += 1
        ce, cs = letras(x[2]) / seg, letras(y[2]) / seg
        if cs > 20 and cs > ce * 1.25:
            malos.append((cs, ce, seg, f, x[2].replace("\n", " / "), y[2].replace("\n", " / ")))
malos.sort(reverse=True)
for m in malos:
    print("%.1f l/s (inglés %.1f) en %.1f s | %s | %s || %s" % m)
print("subtítulos medidos:", total, "| demasiado rápidos:", len(malos))
