# -*- coding: utf-8 -*-
"""(06-11-2026) Regla del usuario: entender la conversación entera. Monta TODAS las escenas del Y5 en orden del juego con
quién habla (Prota/Otro, del .msg japonés), inglés y español de la v1.0.5 -> escenas.jsonl (una escena por línea)."""
import sys, json, csv
sys.path.insert(0, 'C:/Mods/yakuza5/herramientas')
import genero_lotes as g
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
filas = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
es_de = {g.norm(r['ingles']): r for r in filas}
sec = g.secuencias_y5(filas)
n = 0
with open('escenas.jsonl', 'w', encoding='utf-8') as o:
    for a, v in sec.items():
        lin = []
        for q, en in v:
            r = es_de.get(en)
            lin.append({'q': q, 'id': r['id'] if r else None, 'en': en, 'es': r['espanol'] if r else None})
        o.write(json.dumps({'a': a, 'l': lin}, ensure_ascii=False) + '\n'); n += 1
print('escenas', n, 'lineas', sum(len(v) for v in sec.values()), 'sin_es', sum(1 for v in sec.values() for q, en in v if en not in es_de))
