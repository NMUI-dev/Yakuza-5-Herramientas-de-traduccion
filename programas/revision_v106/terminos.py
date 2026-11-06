# -*- coding: utf-8 -*-
"""(06-11-2026) Términos con dos traducciones: nombres cortos de tablas/menús (objetos, lugares, técnicas, tiendas; 2-4 palabras
con mayúscula, traducidos) -> se buscan en el resto de frases inglesas; si la frase inglesa los nombra y la española no lleva
la misma traducción (sin tildes ni mayúsculas), aviso. Salida: terminos.tsv (término en, término es, id, en, es)."""
import csv, re, unicodedata, collections
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
def n(t): return ''.join(c for c in unicodedata.normalize('NFD', re.sub(r'<[^>]*>', '', t).lower()) if unicodedata.category(c) != 'Mn')
F = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
glos = collections.defaultdict(collections.Counter)
for r in F:
    en, es = r['ingles'].strip(), r['espanol'].strip()
    g = r['donde'].split(' | ')[0]
    if g in ('tabla', 'ptr') and 2 <= len(en.split()) <= 4 and re.fullmatch(r"[A-Z][\w'’-]*( [A-Z0-9][\w'’-]*)+", en) and es and n(es) != n(en):
        glos[en][es] += 1
glos = {k: v.most_common(1)[0][0] for k, v in glos.items() if len(v) == 1}   # solo los de traducción única en las tablas
out = []
for r in F:
    if r['donde'].split(' | ')[0] not in ('msg', 'sub', 'extra-sub', 'pac'): continue
    for en_t, es_t in glos.items():
        if en_t in r['ingles'] and n(es_t) not in n(r['espanol']):
            out.append((en_t, es_t, r['id'], r['ingles'].replace('\n', ' / '), r['espanol'].replace('\n', ' / ')))
with open('terminos.tsv', 'w', encoding='utf-8') as o:
    for x in out: o.write('\t'.join(x) + '\n')
c = collections.Counter(x[0] for x in out)
print('glosario', len(glos), 'avisos', len(out), 'términos', len(c)); print(c.most_common(40))
