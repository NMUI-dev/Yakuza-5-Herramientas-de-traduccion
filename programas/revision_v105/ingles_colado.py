# -*- coding: utf-8 -*-
"""(05-11-2026) Palabras ASCII dentro del español que el diccionario es-MX no conoce y que NO están en la frase inglesa
de esa fila: inglés colado por el traductor automático. python ingles_colado.py Y5|Y6 [correcciones.json]"""
import csv, json, os, re, sys
from spylls.hunspell import Dictionary
J = sys.argv[1]
CSV = {'Y5': 'C:/Mods/yakuza5/entrega_v104/Herramientas para traduccion/trabajo/textos.csv',
       'Y6': 'C:/Mods/yakuza6/entrega_v1.0.3/Herramientas para traduccion/trabajo/textos.csv'}[J]
d = Dictionary.from_files(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diccionario_es', 'es'))
corr = json.load(open(sys.argv[2], encoding='utf-8')) if len(sys.argv) > 2 else {}
filas = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
todo_en = set()
for r in filas: todo_en.update(w.lower() for w in re.findall(r"[A-Za-z]+", r['ingles']))
cache = {}
n = 0
for r in filas:
    es = corr.get(r['id'], {}).get('es', r['espanol'])
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)|"[^"]*"|“[^”]*”', ' ', es)
    en = set(w.lower() for w in re.findall(r"[A-Za-z]+", r['ingles']))
    malas = []
    for w in re.findall(r"(?<![\wáéíóúñü])[A-Za-z]{3,}(?![\wáéíóúñü])", t):
        lw = w.lower()
        if lw in en: continue
        if lw not in cache: cache[lw] = d.lookup(lw) or d.lookup(w)
        if not cache[lw]: malas.append(w)
    if malas:
        n += 1
        print(f"{r['id']}|{' '.join(malas)}| {es[:150]!r}")
print('filas', n, file=sys.stderr)
