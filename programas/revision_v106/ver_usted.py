# -*- coding: utf-8 -*-
"""Lista cada línea con «usted» con 3 líneas de escena a cada lado (EN || ES) -> usted_ctx.txt"""
import json, re
U = re.compile(r"\busted\b", re.I); vistos = set()
with open('usted_ctx.txt', 'w', encoding='utf-8') as o:
    for l in open('escenas.jsonl', encoding='utf-8'):
        s = json.loads(l); L = s['l']
        for i, x in enumerate(L):
            if x['es'] and U.search(x['es']) and x['id'] not in vistos:
                vistos.add(x['id'])
                o.write(f"### id {x['id']}  {s['a']}\n")
                for k in range(max(0, i-3), min(len(L), i+4)):
                    y = L[k]; o.write(('>> ' if k == i else '   ') + f"[{y['q']}] {y['en']} || {y['es']}".replace('\n', ' / ') + '\n')
print(len(vistos))
