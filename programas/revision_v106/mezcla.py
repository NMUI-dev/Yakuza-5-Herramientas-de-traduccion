# -*- coding: utf-8 -*-
"""(06-11-2026) Tú/usted: dentro de una conversación (tramo seguido de la escena), la MISMA voz (Prota u Otro) que trata de
usted y de tú. Marcas U/T por palabras y por imperativos de cortesía. Tramos: ventanas de líneas seguidas entre las que no
hay cortes (líneas del sistema «Ganaste/Recibiste» no cortan). Salida: mezcla.txt (para revisar a mano en contexto)."""
import json, re, collections
T = re.compile(r'\b(tú|te|ti|contigo|tu|tus|tuyo|tuya|oye|mira|disculpa|perdona|espera|ven|dime|fíjate|cuídate|quieres|puedes|tienes|eres|estás|sabes|has|vienes|vuelve|dijiste|hiciste|viniste)\b', re.I)
U = re.compile(r'\b(usted|disculpe|perdone|oiga|dígame|mire|espere|venga|cálmese|quiere usted|puede usted|desea|sabe usted|cuídese|vuelva|le agradezco|lo espera|su ayuda)\b', re.I)
VENT = 8
def m(es):
    if not es: return ''
    e = re.sub(r'<[^>]*>|\{[^}]*\}|\([^)]*\)', ' ', es)   # pensamientos entre paréntesis fuera
    return ('T' if T.search(e) else '') + ('U' if U.search(e) else '')
casos = []; vistos = set()
for l in open('escenas.jsonl', encoding='utf-8'):
    s = json.loads(l); L = s['l']; mk = [m(x['es']) for x in L]
    for i, x in enumerate(L):
        if 'U' not in mk[i] or 'T' in mk[i]: continue
        for k in range(max(0, i - VENT), min(len(L), i + VENT + 1)):
            if k != i and L[k]['q'] == x['q'] and 'T' in mk[k] and 'U' not in mk[k]:
                clave = (s['a'], min(i, k))
                if clave in vistos: continue
                vistos.add(clave); casos.append((s['a'], i, k))
with open('mezcla.txt', 'w', encoding='utf-8') as o:
    porescena = collections.defaultdict(set)
    for a, i, k in casos: porescena[a].update([i, k])
    E = {json.loads(l)['a']: json.loads(l)['l'] for l in open('escenas.jsonl', encoding='utf-8') if json.loads(l)['a'] in porescena}
    for a, idx in porescena.items():
        L = E[a]; lo, hi = max(0, min(idx) - 2), min(len(L), max(idx) + 3)
        o.write(f'### {a}\n')
        for k in range(lo, hi):
            y = L[k]; o.write(('>> ' if k in idx else '   ') + f"{y['id']} [{y['q']}] {y['en']} || {y['es']}".replace('\n', ' / ') + '\n')
print('casos', len(casos), 'escenas', len(porescena))
