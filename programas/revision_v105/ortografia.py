# -*- coding: utf-8 -*-
"""(05-11-2026) Palabras que no existen en español en las traducciones (Y5/Y6): diccionario hunspell es-MX
(diccionario_es/, de github.com/wooorm/dictionaries) con spylls. Se descartan las palabras que salen en el inglés
(nombres, marcas) y las de más de N apariciones (jerga del juego).
  python ortografia.py Y5|Y6 -> <proyecto>/trabajo/revision_steam_0511/ortografia.tsv  (palabra, veces, id, frase)
"""
import csv, os, re, sys, collections
from spylls.hunspell import Dictionary

J = sys.argv[1]
CSV = {'Y5': 'C:/Mods/yakuza5/entrega_v104/Herramientas para traduccion/trabajo/textos.csv',
       'Y6': 'C:/Mods/yakuza6/entrega_v1.0.3/Herramientas para traduccion/trabajo/textos.csv'}[J]
SAL = {'Y5': 'C:/Mods/yakuza5/trabajo/revision_steam_0511', 'Y6': 'C:/Mods/yakuza6/trabajo/revision_steam_0511'}[J]
d = Dictionary.from_files(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diccionario_es', 'es'))
filas = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
en = set()
for r in filas: en.update(w.lower() for w in re.findall(r"[A-Za-z]+", r['ingles']))
cuenta, ej, cache = collections.Counter(), {}, {}
for r in filas:
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)', ' ', r['espanol']).replace('`', 'í').replace('~', 'í')
    for w in re.findall(r"(?<![\w-])[a-záéíóúñü]{3,}(?![\w-])", t):
        if w in en: continue
        if w not in cache: cache[w] = d.lookup(w)
        if not cache[w]:
            cuenta[w] += 1
            ej.setdefault(w, (r['id'], r['espanol'].replace('\n', ' / ')[:140]))
with open(os.path.join(SAL, 'ortografia.tsv'), 'w', encoding='utf-8') as fh:
    for w, n in sorted(cuenta.items(), key=lambda x: (x[1], x[0])):
        fh.write(f'{w}\t{n}\t{ej[w][0]}\t{ej[w][1]}\n')
print(J, 'palabras desconocidas', len(cuenta), 'con 1-3 apariciones', sum(1 for n in cuenta.values() if n <= 3))
