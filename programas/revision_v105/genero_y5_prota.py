# -*- coding: utf-8 -*-
"""(05-11-2026) Y5, 2.ª pasada: en conversaciones SIN Haruka (protagonista hombre), busca palabras en femenino que
casi siempre se refieren a una persona, dichas POR el protagonista (yo) o AL protagonista (tú, línea pegada a una suya).
  python genero_y5_prota.py -> trabajo/revision_steam_0511/prota_y5.txt (revisar a mano)
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genero_lotes as G

FEM = ('sincera segura cansada preocupada encantada agradecida equivocada lista sola nerviosa contenta emocionada '
       'convencida decepcionada sorprendida experta talentosa embobada loca celosa enamorada ocupada asustada aburrida '
       'confundida avergonzada tranquila feliz? orgullosa honesta tonta despistada perdida obsesionada enojada molesta '
       'dispuesta interesada acostumbrada mareada borracha agotada impresionada halagada distraída callada atenta '
       'satisfecha harta rendida herida muerta segurísima listísima única hija nueva vieja buena mala pobre '
       'rara linda guapa bonita encantadora maravillosa amable valiente fuerte lista').split()
FEM = {w for w in FEM if w.endswith('a')}
P_YO = re.compile(r"\b(?:yo|estoy|soy|estaba|era|me\s+\w+|ser|estar|quedé|sigo|he\s+sido|seré|estaré)\b", re.I)
P_TU = re.compile(r"\b(?:tú|estás|eres|estabas|eras|te\s+\w+|seas|estés|pareces|sigues|has\s+sido|serás|estarás)\b", re.I)


def main():
    filas = G.leer_csv('Y5')
    sec = G.secuencias_y5(filas)
    es_de = {G.norm(r['ingles']): r for r in filas}
    vistos, out = set(), []
    for a, v in sec.items():
        if '/msg/' not in a: continue
        if any('Haruka' in en for _, en in v): continue      # capítulos de Haruka u otras dudas: fuera
        for i, (q, en) in enumerate(v):
            r = es_de.get(en)
            if not r or r['id'] in vistos or q not in ('Prota', 'Otro'): continue
            es = G.limpio(r['espanol'])
            pal = [w for w in re.findall(r"[a-záéíóúñ]+", es.lower()) if w in FEM]
            if not pal: continue
            if q == 'Prota' and P_YO.search(es):
                motivo = 'protagonista (hombre) habla de sí'
            elif q == 'Otro' and P_TU.search(es) and any(v[k][0] == 'Prota' for k in (i - 1, i + 1) if 0 <= k < len(v)):
                motivo = 'le hablan al protagonista (hombre)'
            else:
                continue
            vistos.add(r['id'])
            ctx = [f"{'>> ' if k == i else '   '}[{v[k][0]}] {v[k][1]} || {es_de[v[k][1]]['espanol'] if v[k][1] in es_de else ''}".replace('\n', ' / ')[:200]
                   for k in range(max(0, i - 2), min(len(v), i + 2))]
            out.append(f"id {r['id']} veces {r['veces']} | {a.split('/')[-1]} | {motivo} ({', '.join(pal)})\n" + '\n'.join(ctx))
    open(os.path.join(G.SAL['Y5'], 'prota_y5.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('marcadas', len(out))


if __name__ == '__main__':
    main()
