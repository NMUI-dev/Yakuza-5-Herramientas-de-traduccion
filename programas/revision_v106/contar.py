# -*- coding: utf-8 -*-
"""Cuenta las correcciones de la v1.0.6 por tipo (para el LEEME y el informe)."""
import json, re, collections
d = json.load(open('correcciones_0611.json', encoding='utf-8'))
def tipo(c):
    m = c['motivo'].lower(); f = c['fuente']
    if f == 'cambios_terminos.json': return 'nombre de objeto/técnica igual que en el menú'
    if f == 'cambios_nombres.json' or 'orfanato' in m or 'nombre' in m and 'mapa' in m or 'pequeña asia' in m: return 'nombres propios unificados'
    if 'tío kaz' in m: return 'nombres propios unificados'
    if 'españa' in m or 'latino' in m or 'me vale' in m: return 'expresiones de España'
    if re.search(r'g[ée]nero', m): return 'género'
    if re.search(r'\busted\b|\btú\b|^tú|^usted|trato|neutro|tutea|plural', m): return 'trato tú/usted'
    if re.search(r'sentido|faltaba|negaci|pregunta|n[úu]mero|omit|perd[ií]a|cambiaba|significado|invertido|no decía|el inglés', m): return 'sentido'
    if re.search(r'signo|apertura|cierre|puntuaci|doble', m) or f.startswith('cambios_signos'): return 'signos ¿? ¡!'
    return 'erratas, gramática e inglés colado'
c = collections.Counter(tipo(x) for x in d.values())
for k, v in c.most_common(): print(v, k)
print('total', sum(c.values()))
json.dump({i: tipo(x) for i, x in d.items()}, open('tipos_0611.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
