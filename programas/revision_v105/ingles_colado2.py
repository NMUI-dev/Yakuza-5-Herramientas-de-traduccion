# -*- coding: utf-8 -*-
"""(05-11-2026) Filtra ingles_colado: palabra inglesa de verdad (diccionario en) o palabra con mayúscula en medio
(«queReceiptiera»): python ingles_colado2.py Y5|Y6 [correcciones.json]"""
import csv, json, os, re, sys
from spylls.hunspell import Dictionary
sys.stdout.reconfigure(encoding='utf-8')
J = sys.argv[1]
CSV = {'Y5': 'C:/Mods/yakuza5/entrega_v104/Herramientas para traduccion/trabajo/textos.csv',
       'Y6': 'C:/Mods/yakuza6/entrega_v1.0.3/Herramientas para traduccion/trabajo/textos.csv'}[J]
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diccionario_es')
es_d, en_d = Dictionary.from_files(D + '/es'), Dictionary.from_files(D + '/en')
corr = json.load(open(sys.argv[2], encoding='utf-8')) if len(sys.argv) > 2 else {}
INTERJ = set('hmm ugh ups umm uff hah pff argh agh erm aah aaah ohh ahh yay wow ooh oops hey psst shh tsk eh uh huh hmph mmm grr'.split())
ce, cn = {}, {}
for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'):
    es = corr.get(r['id'], {}).get('es', r['espanol'])
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)|"[^"]*"|“[^”]*”|«[^»]*»', ' ', es)
    en = set(w.lower() for w in re.findall(r"[A-Za-z]+", r['ingles']))
    malas = []
    for w in re.findall(r"(?<![\wáéíóúñü])[A-Za-záéíóúñü]{3,}(?![\wáéíóúñü])", t):
        lw = w.lower()
        if lw in en or lw in INTERJ: continue
        if re.search(r'[a-záéíóúñ][A-Z]', w): malas.append(w); continue
        if not w.isascii(): continue
        if lw not in ce: ce[lw] = es_d.lookup(lw) or es_d.lookup(w)
        if ce[lw]: continue
        if lw not in cn: cn[lw] = en_d.lookup(lw)
        if cn[lw]: malas.append(w)
    if malas: print(f"{r['id']}|{r['donde'][:40]}|{' '.join(malas)}|EN {r['ingles'][:110]!r}|ES {es[:160]!r}")
