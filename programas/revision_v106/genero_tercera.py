# -*- coding: utf-8 -*-
"""(06-11-2026) Género en tercera persona (correos, subhistorias, fichas, objetos y también diálogos): la frase inglesa habla
de UNA sola persona con género claro (she/her vs he/him/his) y el español lleva participios/adjetivos de persona del género
contrario cerca de un verbo ser/estar/fue/quedó. -> genero_tercera.txt para revisar a mano."""
import csv, re
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = re.compile(r"\b(she|her|hers|herself|woman|girl|lady|mother|mom|wife|sister|daughter|hostess|actress|waitress|grandma|miss|ma'am)\b", re.I)
M = re.compile(r"\b(he|him|his|himself|man|guy|boy|father|dad|husband|brother|son|grandpa|mister|sir)\b", re.I)
V = r"(?:es|era|fue|está|estaba|estuvo|queda|quedó|parece|parecía|sigue|seguía|resulta|resultó|ha sido|había sido|ser|estar|se siente|se sentía|se ve|se veía|anda|vive)"
ADJ = re.compile(r"\b" + V + r"\s+(?:muy\s+|tan\s+|bastante\s+|demasiado\s+|un poco\s+|algo\s+|realmente\s+|más\s+|menos\s+|todo\s+|toda\s+)?([a-záéíóúñ]+?(?:ad|id|ad|ich|ios|os)?(?:o|a))\b", re.I)
NO = set('nada algo poco mucho otra otro una uno esa eso esta esto toda todo ahora hora casa ropa cosa forma manera nunca para pero como cuando donde aquí mismo misma cara hacia contra arriba abajo dentro fuera fuerza idea persona gente tuyo tuya mío mía suyo suya cuanto cuanta tanto tanta cierto cierta verdad problema culpa yakuza idol estrella figura buena mala justo'.split())
out = []
for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'):
    en, es = r['ingles'], r['espanol']
    if not es: continue
    f, m = bool(F.search(en)), bool(M.search(en))
    if f == m: continue
    for w in ADJ.findall(es):
        if w.lower() in NO or len(w) < 4: continue
        if (f and w.endswith('o')) or (m and w.endswith('a') and not w.endswith(('ista', 'ida' if False else '¬'))):
            out.append((r['id'], r['donde'].split(':')[0], 'F' if f else 'M', w, en.replace('\n', ' / '), es.replace('\n', ' / '))); break
with open('genero_tercera.txt', 'w', encoding='utf-8') as o:
    for x in out: o.write('\t'.join(x) + '\n')
print(len(out))
import collections; print(collections.Counter(x[1].split(' | ')[0] for x in out).most_common(12))
