# -*- coding: utf-8 -*-
"""(06-11-2026) Señales de ERROR DE SENTIDO (frase inglesa vs española), para revisar a mano en contexto:
 corta  = el español es mucho más corto que el inglés (falta un trozo; p. ej. «She's the best sister...» se perdió)
 num    = un número del inglés no está en el español
 preg   = el inglés pregunta y el español no (o al revés)
 neg    = el inglés niega y el español no tiene ninguna negación
 signos = «¿...¿eh?» con dos aperturas, «¿» sin «?» o «¡» sin «!»
Salida: sentido.tsv (tipo, id, donde, en, es)."""
import csv, re, collections
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
def limpio(t): return re.sub(r'<[^>]*>|\{[^}]*\}|⑬|⑮', ' ', t)
def frases(t): return len([x for x in re.split(r'[.!?…]+', t) if len(x.strip()) > 2])
NEG_EN = re.compile(r"\b(not|n't|never|no|nobody|nothing|none|nowhere|neither|nor|without|can't|won't|ain't)\b|n't\b", re.I)
NEG_ES = re.compile(r"\b(no|nunca|jamás|nadie|nada|ninguno|ninguna|ningún|ni|tampoco|sin|apenas)\b", re.I)
out = []
for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'):
    en, es = limpio(r['ingles']), limpio(r['espanol'])
    if not es.strip() or es.strip() == en.strip(): continue
    t = []
    if len(en) > 40 and len(es) < 0.55 * len(en) and frases(en) > frases(es): t.append('corta')
    ne = set(re.findall(r'\d[\d,.]*\d|\d', en)); ns = set(re.findall(r'\d[\d,.]*\d|\d', es))
    if {x.replace(',', '').replace('.', '') for x in ne} - {x.replace(',', '').replace('.', '') for x in ns}: t.append('num')
    if en.rstrip().endswith('?') != ('?' in es[-3:]) and len(en) < 120: t.append('preg')
    if NEG_EN.search(en) and not NEG_ES.search(es) and len(en) < 150: t.append('neg')
    e1 = es.replace('\n', ' ')
    if re.search(r'¿[^?]*¿', e1) or re.search(r'¡[^!]*¡', e1) or e1.count('¿') != e1.count('?') or e1.count('¡') > e1.count('!'): t.append('signos')
    for x in t: out.append((x, r['id'], r['donde'].split(':')[0], r['ingles'].replace('\n', ' / '), r['espanol'].replace('\n', ' / ')))
with open('sentido.tsv', 'w', encoding='utf-8') as o:
    for x in out: o.write('\t'.join(x) + '\n')
print(collections.Counter(x[0] for x in out))
