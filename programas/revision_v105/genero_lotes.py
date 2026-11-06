# -*- coding: utf-8 -*-
"""(05-11-2026) Lotes para revisar el GÉNERO de los diálogos (queja de Steam: Kiryu tratado de «ella», mujeres de «él»).
Toma las frases candidatas (adjetivos/participios de persona, vocativos) y les pone contexto de su escena: las líneas de
antes y después en el orden del juego, en inglés y español, y quién habla cuando se sabe (Y6: id del personaje).

  python genero_lotes.py Y5|Y6        -> <proyecto>/trabajo/revision_steam_0511/lotes/lote_NNN.json
Cada ítem: {"id": id del textos.csv, "veces": n, "en", "es", "ctx": ["[quién] EN || ES", ... con «>>» en la línea]}
"""
import csv, json, os, re, sys, collections

RAIZ = 'C:/Mods'
CSV = {'Y5': f'{RAIZ}/yakuza5/entrega_v104/Herramientas para traduccion/trabajo/textos.csv',
       'Y6': f'{RAIZ}/yakuza6/entrega_v1.0.3/Herramientas para traduccion/trabajo/textos.csv'}
SAL = {'Y5': f'{RAIZ}/yakuza5/trabajo/revision_steam_0511', 'Y6': f'{RAIZ}/yakuza6/trabajo/revision_steam_0511'}
CTX = 6          # líneas de contexto a cada lado
POR_LOTE = 25    # candidatas por lote
KIRYU_Y6 = 1679  # id de Kiryu en sound_auth_subtitles_speech_list_* (el que más habla)

V = (r"(?:estás|estas|eres|estoy|soy|estaba|estabas|eras|fuiste|has sido|he sido|pareces|parezco|te ves|me veo|"
     r"te sientes|me siento|quedas|quedé|quedaste|sigues|sigo|estarás|estaré|serás|seré|te has vuelto|me he vuelto|"
     r"te has quedado|me he quedado|te veo|me tienes|te tengo|estés|esté|sea|seas|ser|estar|vas a estar|voy a estar)")
ADJ = re.compile(r"\b" + V + r"\s+(?:muy\s+|tan\s+|bastante\s+|demasiado\s+|un poco\s+|algo\s+|todo\s+|toda\s+|"
                 r"realmente\s+|más\s+|menos\s+)?([a-záéíóúñ]+(?:o|a|os|as))\b", re.I)
VOC = re.compile(r"\b(amig[oa]|querid[oa]|guap[oa]|chic[oa]|muchach[oa]|jovencit[oa]|señorit[oa]|herman[oa]|"
                 r"niñ[oa]|cariño|hij[oa] mí[oa]|bienvenid[oa]s?|solit[oa]|sol[oa]|list[oa]s?|segur[oa]|"
                 r"agradecid[oa]|encantad[oa]|preocupad[oa]|cansad[oa]|loc[oa]|tont[oa]|idiota|herid[oa]|"
                 r"enfadad[oa]|enojad[oa]|celos[oa]|orgullos[oa]|nervios[oa]|ocupad[oa]|perdid[oa]|equivocad[oa])\b", re.I)
NO = set('''nada algo poco mucho otra otro una uno esa eso esta esto toda todo ahora hora casa ropa cosa forma manera nunca
siempre ya para pero como cuando donde aquí mismo misma ama amo yakuza cara hacia contra arriba abajo dentro fuera fuerza
idea persona gente tuyo tuya mío mía suyo suya cuanto cuanta tanto tanta cierto cierta verdad problema culpa trabajando
buscando esperando hablando pensando haciendo diciendo yendo tratando intentando mirando'''.split())


def limpio(t):
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)|⑬|⑮', ' ', t)
    return t.replace('`', 'í').replace('~', 'í').replace('|', 'Í')


def candidata(es):
    e = limpio(es)
    return any(x.lower() not in NO for x in ADJ.findall(e)) or bool(VOC.search(e))


def norm(t):
    return t.replace('\r\n', '\n').replace('\r', '\n')


def leer_csv(j):
    with open(CSV[j], encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh, delimiter=';'))


def secuencias_y5(filas):
    """Escenas del Y5 en orden del juego: textos_en.jsonl (f, a=archivo, k=orden, t=inglés)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import struct, msg_y5
    quien = {}   # (archivo, offset del registro) -> Prota/Otro: función (2,7,v) del .msg, v=210 protagonista, 255 otro
    def hablante(a, k):
        if a not in quien:
            quien[a] = {}
            try:
                # el .msg inglés tiene siempre 255; el japonés conserva quién habla, con los mismos registros
                ben = open(f'{RAIZ}/yakuza5/trabajo/extraido/{a}', 'rb').read()
                b = open(f"{RAIZ}/yakuza5/trabajo/extraido/{a.replace('wdr_par_en_wdr/wdr_en', 'wdr_ja/wdr_ja')}", 'rb').read()
                ren, rja = msg_y5.leer(ben)[1], msg_y5.leer(b)[1]
                if [r['reg'] for r in ren] != [r['reg'] for r in rja]: raise ValueError('registros distintos')
                for r in rja:
                    for _, x in r['funcs']:
                        if x[0] == 2 and x[1] == 7:
                            v = struct.unpack('>H', x[2:4])[0]
                            quien[a][r['reg']] = 'Prota' if v == 210 else 'Otro' if v == 255 else f'S{v}'
            except Exception:
                pass
        return quien[a].get(k, '')
    sec = collections.defaultdict(list)
    for l in open(f'{RAIZ}/yakuza5/trabajo/textos_en.jsonl', encoding='utf-8'):
        d = json.loads(l)
        if d['f'] in ('msg', 'sub', 'pac'):
            k = d['k'] if isinstance(d['k'], int) else 0
            q = hablante(d['a'], k) if d['f'] == 'msg' else ''
            sec[d['a']].append((k, q, norm(d['t'])))
    for a in sec: sec[a].sort(key=lambda x: x[0])
    print('líneas con hablante:', sum(1 for v in sec.values() for _, q, _ in v if q), file=sys.stderr)
    return {a: [(q, t) for _, q, t in v] for a, v in sec.items()}


def secuencias_y6(filas):
    """Y6: listas de habla de las escenas (con id de quien habla) + el resto en el orden del textos.csv."""
    sec = {}
    d = f'{RAIZ}/yakuza6/trabajo/armp_json'
    for f in sorted(os.listdir(d)):
        if f.startswith('sound_auth_subtitles_speech_list_') and f.endswith('.json'):
            t = json.load(open(os.path.join(d, f), encoding='utf-8'))
            v = []
            for i in range(t['ROW_COUNT']):
                r = t.get(str(i), {}).get('', {})
                if isinstance(r.get('4'), str):
                    q = 'Kiryu' if r.get('1') == KIRYU_Y6 else f"P{r.get('1')}"
                    v.append((q, norm(r['4'])))
            sec[f[len('sound_auth_subtitles_speech_list_'):-9]] = v
    resto = collections.defaultdict(list)
    for r in filas:
        g = r['donde'].split(' | ')[0]
        if g != 'sound_auth':
            resto[r['donde'] if g == 'talk' else g].append(('', norm(r['ingles'])))
    sec.update(resto)
    return sec


def main(j):
    filas = leer_csv(j)
    es_de = {norm(r['ingles']): r for r in filas}
    sec = (secuencias_y5 if j == 'Y5' else secuencias_y6)(filas)
    vistos, items = set(), []
    for nombre, v in sec.items():
        for i, (q, en) in enumerate(v):
            r = es_de.get(en)
            if not r or r['id'] in vistos or not r['espanol'].strip() or not candidata(r['espanol']):
                continue
            vistos.add(r['id'])
            ctx = []
            for k in range(max(0, i - CTX), min(len(v), i + CTX + 1)):
                q2, en2 = v[k]
                r2 = es_de.get(en2)
                es2 = r2['espanol'] if r2 else ''
                ctx.append(('>> ' if k == i else '') + (f'[{q2}] ' if q2 else '') + f'{en2} || {es2}'.replace('\n', ' / '))
            items.append({'id': r['id'], 'escena': nombre, 'veces': int(r['veces'] or 1), 'en': r['ingles'],
                          'es': r['espanol'], 'ctx': ctx})
    # candidatas sin escena conocida (tablas, correos...): contexto vacío
    for r in filas:
        if r['id'] not in vistos and r['espanol'].strip() and candidata(r['espanol']) and r['donde'].split(' | ')[0] in (
                'msg', 'sub', 'extra-sub', 'extra-nom', 'pac', 'talk', 'auth', 'pause_mail', 'pause_sns',
                'minigame_live_chat_chat_messages'):
            items.append({'id': r['id'], 'escena': r['donde'], 'veces': int(r['veces'] or 1), 'en': r['ingles'],
                          'es': r['espanol'], 'ctx': []})
            vistos.add(r['id'])
    out = os.path.join(SAL[j], 'lotes')
    os.makedirs(out, exist_ok=True)
    for n in range(0, len(items), POR_LOTE):
        json.dump(items[n:n + POR_LOTE], open(os.path.join(out, f'lote_{n // POR_LOTE:03d}.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=0)
    print(j, 'candidatas', len(items), 'lotes', (len(items) + POR_LOTE - 1) // POR_LOTE)


if __name__ == '__main__':
    main(sys.argv[1])
