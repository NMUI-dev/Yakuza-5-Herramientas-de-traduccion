# (claude2, 06-11-2026) Y5: cada letra del español debe tener dibujo en la fuente del paquete (sd_hankaku.dds, casillas
# de 16x32, código-0x20), o sale en blanco. Idea del Y6 (claude1: º ª « » à salían en blanco).
# Uso: python -I letras_fuente_y5.py   (sale 1 si falta alguna)
import csv, json, sys
import numpy as np
from PIL import Image
csv.field_size_limit(10 ** 9)
sys.stdout.reconfigure(encoding="utf-8")
H = r"C:\Mods\yakuza5\entrega_v106\Herramientas para traduccion"
DDS = r"C:\Mods\yakuza5\trabajo\fuente\add\font_hd_en\gothic_en\sd_hankaku.dds"
LETRAS = {'¡': '½', 'í': '`', 'Í': '|'}   # casillas cambiadas por la herramienta
a = np.asarray(Image.open(DDS).convert('RGBA'))[..., 3]
dibujo = set()
for i in range(256):
    x, y = (i % 16) * 16, (i // 16) * 32
    if a[y:y + 32, x:x + 16].max() > 60:
        dibujo.add(i + 0x20)
def tiene(ch):
    ch = LETRAS.get(ch, ch)
    return ch in ' \n\r\t' or ord(ch) in dibujo
def sin_etq(s):
    out, dentro = [], False
    for c in s:
        if c == '<': dentro = True
        elif c == '>' and dentro: dentro = False
        elif not dentro: out.append(c)
    return ''.join(out)
textos = []   # (id, es, en)
claves = []   # claves de los .json = texto original (inglés o japonés): sus letras ya las dibuja el juego
for r in csv.DictReader(open(H + r"\trabajo\textos.csv", encoding='utf-8-sig', newline=''), delimiter=';'):
    textos.append((r['id'], r['espanol'], r['ingles']))
def recorrer(o, ruta):
    if isinstance(o, dict):
        for k, v in o.items():
            claves.append(str(k)); recorrer(v, ruta + '/' + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o): recorrer(v, ruta + '/' + str(i))
    elif isinstance(o, str):
        textos.append((ruta, o, ''))
for f in ('cortas', 'textos_extra', 'traducciones', 'devil'):
    recorrer(json.load(open(H + r"\datos\%s.json" % f, encoding='utf-8')), f)
ingles = set(''.join(t[2] for t in textos)) | set(''.join(claves))
faltan = {}
for i, es, en in textos:
    for ch in set(sin_etq(es)):
        if not tiene(ch) and ch not in ingles and not ('\u3040' <= ch <= '\u9fff'):
            faltan.setdefault(ch, []).append((i, es))
for ch, l in sorted(faltan.items(), key=lambda kv: -len(kv[1])):
    print('FALTA %r U+%04X en %d textos' % (ch, ord(ch), len(l)))
    for i, es in l[:4]: print('    ', i, '|', es[:110].replace('\n', ' / '))
print('casillas con dibujo:', len(dibujo), '| letras que faltan:', len(faltan))
sys.exit(1 if faltan else 0)
