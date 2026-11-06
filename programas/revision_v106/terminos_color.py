# -*- coding: utf-8 -*-
"""(06-11-2026) Nombres de objetos/técnicas entre etiquetas de color (<Color:8>…, <Color:9>…) en los diálogos: tienen que
llamarse IGUAL que en el menú (tablas). Si el inglés de dentro de la etiqueta es un nombre del menú con traducción única,
el español de dentro se cambia por el del menú. Solo si inglés y español tienen el mismo número de etiquetas, en el mismo orden.
Salida: cambios_terminos.json (mismo formato que los demás)."""
import csv, re, json, collections
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
glos = collections.defaultdict(collections.Counter)
for r in F:
    if r['donde'].split(' | ')[0] in ('tabla', 'ptr') and r['espanol'].strip() and '\n' not in r['ingles'] and len(r['ingles']) < 50:
        glos[r['ingles'].strip()][r['espanol'].strip()] += 1
glos = {k: v.most_common(1)[0][0] for k, v in glos.items() if len(v) == 1}
TAG = re.compile(r'(<Color:(?:8|9)>)(.*?)(<Color:Default>)')
NO_TOCAR = {'17206'}   # el menú dice «Faja abdominal de gloria matutina» (mal: Morning Glory es el orfanato); se arregla el menú
cambios = []
for r in F:
    if r['donde'].split(' | ')[0] not in ('msg', 'sub', 'extra-sub', 'pac'): continue
    te, ts = TAG.findall(r['ingles']), list(TAG.finditer(r['espanol']))
    if not te or len(te) != len(ts): continue
    nuevo = r['espanol']; hubo = []
    for (a, en_in, c), m in reversed(list(zip(te, ts))):
        es_in = m.group(2); ok = glos.get(en_in.strip())
        if ok and ok.strip().lower() == en_in.strip().lower(): ok = None   # en el menú sigue en inglés: no se copia
        if ok and es_in[:1] in '¡¿': ok = es_in[0] + ok
        if ok and ok != es_in.strip() and ok.lower() != es_in.strip().lower() and a == m.group(1):
            nuevo = nuevo[:m.start(2)] + ok + nuevo[m.end(2):]; hubo.append(f'{es_in} -> {ok}')
    if hubo and r['id'] not in NO_TOCAR:
        cambios.append({'id': r['id'], 'es': nuevo, 'motivo': 'nombre como en el menú: ' + '; '.join(hubo)})
json.dump({'cambios': cambios, 'dudas': []}, open('cambios_terminos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('cambios', len(cambios))
for c in cambios[:40]: print(c['id'], c['motivo'])
