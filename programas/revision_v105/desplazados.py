# -*- coding: utf-8 -*-
"""(05-11-2026) Detecta traducciones DESPLAZADAS (el español de la fila i es la traducción del inglés de la fila i-1 o i+1),
como el bloque 28880-28927 del Y5. Compara rasgos que no dependen del idioma: ¿ ? ¡ !, nombres propios, cifras,
puntos suspensivos, saltos de línea, etiquetas <...> y largo relativo.
  python desplazados.py Y5|Y6 -> trabajo/revision_steam_0511/desplazados.txt (tramos con su desplazamiento)
"""
import csv, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
J = sys.argv[1]
CSV = {'Y5': 'C:/Mods/yakuza5/entrega_v104/Herramientas para traduccion/trabajo/textos.csv',
       'Y6': 'C:/Mods/yakuza6/entrega_v1.0.3/Herramientas para traduccion/trabajo/textos.csv'}[J]
SAL = {'Y5': 'C:/Mods/yakuza5/trabajo/revision_steam_0511', 'Y6': 'C:/Mods/yakuza6/trabajo/revision_steam_0511'}[J]
F = [r for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';')]
COMUNES = set('I The You What Oh Well Yeah Okay Hey But So And Huh No Yes Hmm Ah Uh Then This That It Now Sorry Thank Thanks Wait'.split())


def rasgos(t, en):
    nombres = set(re.findall(r"\b[A-Z][a-z]{2,}(?:-[a-z]+)?\b", t)) - COMUNES if en else set(re.findall(r"\b[A-Z][a-z]{2,}(?:-[a-z]+)?\b", t))
    return {'q': '?' in t, 'x': '!' in t, 'n': nombres, 'd': set(re.findall(r'\d+', t.replace(',', ''))),
            'e': '...' in t or '…' in t, 'l': len(t), 'tag': len(re.findall(r'<[^>]+>', t))}


def parecido(a, b):
    s = (a['q'] == b['q']) + (a['x'] == b['x']) + (a['e'] == b['e']) + (a['tag'] == b['tag'])
    s += 2 * len(a['n'] & b['n']) - 0.5 * len(a['n'] ^ b['n']) + 2 * len(a['d'] & b['d']) - len(a['d'] ^ b['d'])
    r = min(a['l'], b['l']) / max(1, a['l'], b['l'])
    return s + 3 * r


en = [rasgos(r['ingles'], True) for r in F]
es = [rasgos(r['espanol'], False) for r in F]
mismo_archivo = lambda i, k: F[i]['donde'].split(':')[0] == F[k]['donde'].split(':')[0]
marca = []
for i in range(len(F)):
    a = parecido(en[i], es[i])
    m = 0
    for dlt in (-1, 1):
        k = i + dlt
        if 0 <= k < len(F) and mismo_archivo(i, k) and parecido(en[k], es[i]) > a + 1.0:
            m = dlt
    marca.append(m)
# tramos: al menos 4 de 6 filas seguidas con el mismo desplazamiento
tramos, i = [], 0
while i < len(F):
    if marca[i]:
        j, d = i, marca[i]
        while j < len(F) and sum(1 for k in range(j, min(j + 6, len(F))) if marca[k] == d) >= 3: j += 1
        if j - i >= 4: tramos.append((i, j, d)); i = j; continue
    i += 1
with open(os.path.join(SAL, 'desplazados.txt'), 'w', encoding='utf-8') as fh:
    for a, b, d in tramos:
        fh.write(f"### filas {F[a]['id']}-{F[b-1]['id']} ({b-a}) desplazamiento {d:+d} | {F[a]['donde'][:60]}\n")
        for k in range(a, min(b, a + 4)):
            fh.write(f"   {F[k]['id']} EN {F[k]['ingles'][:70]!r}\n      ES {F[k]['espanol'][:70]!r}\n")
print(J, 'tramos', len(tramos), 'filas', sum(b - a for a, b, _ in tramos))
