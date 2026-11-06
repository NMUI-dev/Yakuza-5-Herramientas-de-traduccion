# -*- coding: utf-8 -*-
"""Pone correcciones_0611.json en el textos.csv de entrega_v106 (comprueba inglés y «antes»)."""
import csv, json, sys
p = 'C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv'
d = json.load(open('C:/Mods/yakuza5/trabajo/revision_contexto_0611/correcciones_0611.json', encoding='utf-8'))
rows = list(csv.DictReader(open(p, encoding='utf-8-sig', newline=''), delimiter=';'))
campos = list(rows[0].keys()); n = ya = 0
for r in rows:
    c = d.get(r['id'])
    if not c: continue
    assert r['ingles'] == c['en'], r['id']
    if r['espanol'] == c['es']: ya += 1; continue
    assert r['espanol'] == c['antes'], (r['id'], r['espanol'])
    r['espanol'] = c['es']; n += 1
with open(p, 'w', encoding='utf-8-sig', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=campos, delimiter=';', quoting=csv.QUOTE_ALL); w.writeheader(); w.writerows(rows)
print('nuevas', n, 'ya puestas', ya, 'total', len(d))
