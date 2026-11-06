# -*- coding: utf-8 -*-
"""(05-11-2026) Informe de lo que queda en inglés A PROPÓSITO en los textos (por regla) y de los errores corregidos.
Lee el textos.csv que saca la herramienta de la versión FINAL y correcciones.json.
  python informe_queda_ingles.py <textos.csv final> <correcciones.json> <carpeta salida>
Salida: 1 Textos que se dejan en ingles (por regla).txt, 2 Errores corregidos v1.0.5.txt
"""
import collections, csv, json, os, re, sys
from spylls.hunspell import Dictionary
sys.stdout.reconfigure(encoding='utf-8')
CSV, CORR, SAL = sys.argv[1:4]
os.makedirs(SAL, exist_ok=True)
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diccionario_es')
es_d, en_d = Dictionary.from_files(D + '/es'), Dictionary.from_files(D + '/en')
filas = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))

TERMINOS = {  # término que se deja en inglés -> por qué
    'home run': 'béisbol: así se dice en Latinoamérica (término fijado por el usuario)',
    'foul': 'béisbol', 'strike': 'béisbol', 'hit': 'béisbol', 'playoffs': 'béisbol', 'lip sync': 'música',
    'idol': 'término de la saga (idols japonesas)', 'fan': 'de uso común en español', 'premium': 'de uso común',
    'freelance': 'de uso común', 'snowboard': 'deporte', 'surf': 'deporte', 'nerd': 'de uso común', 'cool': 'jerga',
    'manager': 'jerga del espectáculo', 'paparazzi': 'de uso común', 'graffiti': 'de uso común', 'puzzle': 'billar',
    'split': 'bolos', 'full': 'póker', 'bust': 'blackjack', 'charlie': 'blackjack (Six Card Charlie)',
    'single malt': 'whisky', 'whiskey': 'whisky', 'kimono': 'japonés', 'maid': 'cafés de maids', 'buffet': 'de uso común',
    'look': 'jerga', 'ring': 'lucha libre', 'cringe': 'jerga', 'sashimi': 'japonés', 'hip': 'hipo (onomatopeya)',
}
grupos = collections.defaultdict(list)
cache = {}
for r in filas:
    en, es = r['ingles'], r['espanol']
    if not es.strip(): grupos['Vacías (el juego muestra el inglés)'].append(r); continue
    if es.strip() == en.strip():
        grupos['Iguales al inglés: nombres de personas, locales, marcas, objetos con nombre propio'].append(r); continue
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)', ' ', es)
    citas = re.findall(r'"([^"]*[A-Za-z][^"]*)"', t)
    if any(re.search(r'\b[A-Za-z]+ [A-Za-z]+\b', c) and c in en for c in citas):
        grupos['Títulos de canciones, programas o frases citadas en inglés (entre comillas)'].append(r); continue
    malas = []
    for w in re.findall(r"(?<![\wáéíóúñü])[A-Za-z]{3,}(?![\wáéíóúñü])", t):
        lw = w.lower()
        if w[0].isupper() and lw in en.lower(): continue          # nombre propio que ya estaba
        if lw not in cache: cache[lw] = (not es_d.lookup(lw)) and bool(en_d.lookup(lw))
        if cache[lw]: malas.append(lw)
    if not malas: continue
    termino = next((k for k in TERMINOS if any(m.startswith(k.split()[0]) for m in malas)), None)
    grupos[f'Términos que se dejan en inglés: {termino} ({TERMINOS[termino]})' if termino else
           'Otras palabras inglesas dentro del español (revisadas: nombres, marcas, juegos de palabras)'].append(r)

with open(os.path.join(SAL, '1 Textos que se dejan en ingles (por regla).txt'), 'w', encoding='utf-8-sig') as fh:
    fh.write('QUÉ SE QUEDA EN INGLÉS EN LOS TEXTOS Y POR QUÉ (Yakuza 5, v1.0.5)\n'
             'Regla: se traduce todo salvo nombres propios (personas, locales, marcas), títulos de canciones y programas,\n'
             'y términos que en Latinoamérica se usan en inglés o que la saga oficial deja así.\n\n')
    for g in sorted(grupos, key=lambda k: -len(grupos[k])):
        fh.write(f'== {g}: {len(grupos[g])}\n')
        for r in grupos[g]:
            fh.write(f"  [{r['id']}] {r['ingles'][:90]!r} -> {r['espanol'][:110]!r}\n".replace('\\n', ' / '))
        fh.write('\n')
corr = json.load(open(CORR, encoding='utf-8'))
cat = collections.defaultdict(list)
for i, c in corr.items():
    m = c['motivo']
    k = ('Género equivocado' if m.startswith('género') else
         'Traducción desplazada una fila (citas de cabaret)' if 'desplazada' in m else
         '«Uncle Kaz» mal puesto («Soberano Kaz», «Kaz-nee»)' if ('Uncle' in m or 'Kaz-nee' in m) else
         'Inglés metido en la frase o texto roto' if any(x in m for x in ('inglés', 'roto', 'portugués', 'cortada', 'otra fila', 'sentido', 'calco')) else
         'Faltas de ortografía y palabras inexistentes')
    cat[k].append((i, c))
with open(os.path.join(SAL, '2 Errores corregidos v1.0.5.txt'), 'w', encoding='utf-8-sig') as fh:
    fh.write(f'ERRORES CORREGIDOS EN LOS TEXTOS (Yakuza 5, v1.0.4 -> v1.0.5): {len(corr)} frases\n\n')
    for k in sorted(cat, key=lambda k: -len(cat[k])):
        fh.write(f'== {k}: {len(cat[k])}\n')
        for i, c in cat[k]:
            fh.write(f"  [{i}] EN {c['en'][:90]!r}\n      antes {c['antes'][:110]!r}\n      ahora {c['es'][:110]!r}  ({c['motivo']})\n".replace('\\n', ' / '))
        fh.write('\n')
print({k: len(v) for k, v in grupos.items()})
print({k: len(v) for k, v in cat.items()})
