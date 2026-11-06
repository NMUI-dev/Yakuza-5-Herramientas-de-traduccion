# -*- coding: utf-8 -*-
"""(05-11-2026) Y5: incoherencias de género por conversación, sin IA.
En cada .msg se sabe quién habla (Prota = protagonista del capítulo, Otro = la otra persona; del .msg japonés).
Cada adjetivo/participio con «estoy/soy...» vota el género de quien habla; con «estás/eres...» o un vocativo, el de quien
escucha (la otra parte). Se apunta la mayoría por persona y se marcan las frases que van contra ella.
  python genero_y5_votos.py  -> trabajo/revision_steam_0511/votos_y5.txt (para revisar a mano)
"""
import collections, csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genero_lotes as G

P1 = r"(?:estoy|soy|estaba|era|fui|me siento|me veo|parezco|quedé|me quedé|sigo|he sido|seré|estaré|me he vuelto|voy a estar)"
P2 = r"(?:estás|eres|estabas|eras|fuiste|te sientes|te ves|pareces|quedaste|te quedaste|sigues|has sido|serás|estarás|te has vuelto|estés|seas|vas a estar|no seas|no estés)"
MOD = r"\s+(?:muy\s+|tan\s+|bastante\s+|demasiado\s+|un poco\s+|algo\s+|realmente\s+|más\s+|menos\s+|todo\s+|toda\s+|super\s+)?"
ADJ = r"([a-záéíóúñ]+[oa])s?\b"
R1 = re.compile(r"\b" + P1 + MOD + ADJ, re.I)
R2 = re.compile(r"\b" + P2 + MOD + ADJ, re.I)
VOC = re.compile(r"(?:^|[,¡¿!?.] ?)(amig[oa]|querid[oa]|guap[oa]|chic[oa]|muchach[oa]|jovencit[oa]|cariño mí[oa]|hij[oa])\s*[,.!?]", re.I)
NO = G.NO | set('''una uno nada todo toda buena bueno mala malo persona idea cosa ahora misma mismo otra otro yakuza
verdad culpa problema forma manera hora vida broma tipa tipo nueva nuevo cierto cierta posible capaz casa'''.split())


def votos(es):
    e = G.limpio(es)
    ok = lambda w: w.lower() not in NO and len(w) > 3 and not w[0].isupper() and not w.endswith(('ista', 'cida', 'cido'))
    v1 = [w for w in R1.findall(e) if ok(w)]
    v2 = [w for w in R2.findall(e) if ok(w)] + VOC.findall(e)
    g = lambda w: 'F' if w.lower().endswith('a') else 'M'
    return [g(w) for w in v1], [g(w) for w in v2], v1 + v2


def main():
    filas = G.leer_csv('Y5')
    sec = G.secuencias_y5(filas)
    es_de = {G.norm(r['ingles']): r for r in filas}
    out = []
    for a, v in sec.items():
        if '/msg/' not in a: continue
        lin = []
        propios = collections.Counter()   # lo que el protagonista dice de sí mismo
        for i, (q, en) in enumerate(v):
            r = es_de.get(en)
            if not r or q not in ('Prota', 'Otro'): continue
            a1, a2, pal = votos(r['espanol'])
            otro = 'Otro' if q == 'Prota' else 'Prota'
            lin.append((i, q, r, [(q, g) for g in a1] + [(otro, g) for g in a2], pal))
            if q == 'Prota': propios.update(a1)
        cuenta = {p: collections.Counter(g for _, _, _, vs, _ in lin for (pp, g) in vs if pp == p) for p in ('Prota', 'Otro')}
        may = {}
        for p, c in cuenta.items():
            n = sum(c.values())
            if n >= 2:
                g, k = c.most_common(1)[0]
                if k / n >= 0.75: may[p] = g
        # protagonista: hombre salvo que él/ella misma hable en femenino (capítulos de Haruka)
        if 'Prota' not in may or sum(cuenta['Prota'].values()) < 3:
            may['Prota'] = 'F' if propios['F'] > propios['M'] else 'M'
        for i, q, r, vs, pal in lin:
            for p, g in vs:
                m = may.get(p, '')
                if m and m[0] != g:
                    ctx = [f"{'>> ' if k == i else ''}[{v[k][0]}] {v[k][1]} || {es_de[v[k][1]]['espanol'] if v[k][1] in es_de else ''}".replace('\n', ' / ')
                           for k in range(max(0, i - 3), min(len(v), i + 3))]
                    out.append((a, r, p, g, m, cuenta[p], pal, ctx))
                    break
    vistos = set()
    with open(os.path.join(G.SAL['Y5'], 'votos_y5.txt'), 'w', encoding='utf-8') as fh:
        for a, r, p, g, m, c, pal, ctx in out:
            if r['id'] in vistos: continue
            vistos.add(r['id'])
            fh.write(f"### id {r['id']} veces {r['veces']} | {a.split('/')[-1]} | {p} es {m} {dict(c)} y aquí {g} ({', '.join(pal)})\n")
            fh.write('\n'.join(ctx) + '\n\n')
    print('marcadas', len(vistos))


if __name__ == '__main__':
    main()
