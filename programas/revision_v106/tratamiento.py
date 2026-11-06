# -*- coding: utf-8 -*-
"""(06-11-2026) Tú/usted por escena. Marca cada línea española: U (usted/ustedes no plural...), T (tú, te, ti, contigo, tu, tus).
Escenas donde la MISMA voz (Prota u Otro) usa T y U -> candidatas a incoherencia. Salida: tratamiento.txt + resumen."""
import json, re, collections
T = re.compile(r'\b(tú|te|ti|contigo|tu|tus|tuyo|tuya|tuyos|tuyas)\b', re.I)
U = re.compile(r'\b(usted)\b', re.I)
def marca(es):
    if not es: return ''
    e = re.sub(r'<[^>]*>|\{[^}]*\}', ' ', es)
    return ('T' if T.search(e) else '') + ('U' if U.search(e) else '')
tot = collections.Counter(); mezcla = []
for l in open('escenas.jsonl', encoding='utf-8'):
    s = json.loads(l); voz = collections.defaultdict(collections.Counter)
    for x in s['l']:
        m = marca(x['es'])
        for c in m: voz[x['q'] or '?'][c] += 1; tot[c] += 1
    for q, c in voz.items():
        if c['T'] and c['U']: mezcla.append((s['a'], q, c['T'], c['U']))
print('lineas con T', tot['T'], 'con U', tot['U'], 'escenas/voz con mezcla', len(mezcla))
with open('tratamiento.txt', 'w', encoding='utf-8') as o:
    for m in mezcla: o.write('\t'.join(map(str, m)) + '\n')
