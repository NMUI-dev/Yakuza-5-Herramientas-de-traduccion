# -*- coding: utf-8 -*-
"""Pone correcciones.json en el textos.csv de la herramienta (entrega_v105). Comprueba inglés y «antes»."""
import csv, json, sys
p = sys.argv[1] if len(sys.argv) > 1 else 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
d = json.load(open('C:/Mods/yakuza5/trabajo/revision_steam_0511/correcciones.json', encoding='utf-8'))
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
