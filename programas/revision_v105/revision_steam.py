# -*- coding: utf-8 -*-
"""Revisión pedida por un comentario de Steam (05-11-2026): diálogos de escenas sin traducir y género mal puesto.
Sirve para Y5 y Y6: lee el textos.csv que saca «herramienta_traduccion.py extraer» (separador ;).

  python revision_steam.py ingles  <Y5|Y6>   -> frases en inglés que quedan (vacías, iguales o con trozos en inglés)
  python revision_steam.py genero  <Y5|Y6>   -> candidatos de género (pronombres que no casan, adjetivos con tú/yo)
Salida en <proyecto>/trabajo/revision_steam_0511/.
"""
import csv, json, os, re, sys, collections

RAIZ = r'C:\Mods'
CSV = {'Y5': os.path.join(RAIZ, r'yakuza5\entrega_v104\Herramientas para traduccion\trabajo\textos.csv'),
       'Y6': os.path.join(RAIZ, r'yakuza6\entrega_v1.0.3\Herramientas para traduccion\trabajo\textos.csv')}
SAL = {'Y5': os.path.join(RAIZ, r'yakuza5\trabajo\revision_steam_0511'),
       'Y6': os.path.join(RAIZ, r'yakuza6\trabajo\revision_steam_0511')}


def leer(j):
    with open(CSV[j], encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh, delimiter=';'))


def limpio(t):
    t = re.sub(r'<[^>]*>|\{[^}]*\}|\$\{[^}]*\}|\(改行\)', ' ', t)
    return t.replace('`', 'í').replace('~', 'í').replace('|', 'Í')


# palabras inglesas frecuentes que no existen en español (para encontrar trozos sin traducir dentro del español)
EN = set('''the you your you're i'm it's don't can't won't what's that's there's he's she's we're they're this that with
have has had will would should could just what where when why how who was were been being are is not but and or of to for
from about into because there their them they him her his she he we our us my me yeah okay hey well right sorry thanks
thank please know think want need got get going come here now then never always only still really very much more some
any all one man guy something nothing anything everything someone anyone again time way back down out over'''.split())
ES_TAMBIEN = set('me he has era fue a no son con sin come vas mi tu'.split())
NOMBRES = set()  # se ignoran palabras con mayúscula inicial (nombres) salvo al inicio


def trozos_ingles(es):
    pal = re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)?", limpio(es))
    n = [p for p in pal if p.lower() in EN and p.lower() not in ES_TAMBIEN]
    return n


def cmd_ingles(j):
    rows = leer(j)
    os.makedirs(SAL[j], exist_ok=True)
    sin, igual, mezcla = [], [], []
    for r in rows:
        en, es = r['ingles'], r['espanol']
        palabras_en = re.findall(r"[a-z]{2,}", limpio(en))
        if len(palabras_en) < 2:
            continue
        if not es.strip():
            sin.append(r)
        elif es.strip() == en.strip():
            igual.append(r)
        else:
            t = trozos_ingles(es)
            if len(t) >= 2:
                mezcla.append((r, t))
    with open(os.path.join(SAL[j], 'ingles_quedan.txt'), 'w', encoding='utf-8') as fh:
        for nom, lst in (('VACÍAS (se quedan en inglés)', sin), ('IGUAL AL INGLÉS', igual)):
            fh.write(f'== {nom}: {len(lst)}\n')
            for r in lst:
                fh.write(f"{r['id']}\t{r['donde'][:80]}\t{r['ingles']!r}\n")
        fh.write(f'== ESPAÑOL CON PALABRAS INGLESAS: {len(mezcla)}\n')
        for r, t in mezcla:
            fh.write(f"{r['id']}\t{r['donde'][:80]}\t{' '.join(t)}\n\tEN {r['ingles']!r}\n\tES {r['espanol']!r}\n")
    c = collections.Counter(r['donde'].split(' | ')[0].split('/')[0] for r in sin + igual)
    print(j, 'vacías', len(sin), 'iguales', len(igual), 'mezcla', len(mezcla))
    print(' por sitio:', c.most_common(20))


# --- género ---
FEM_EN = re.compile(r"\b(she|her|hers|herself|woman|girl|lady|miss|ma'am|mother|mom|sister|wife|daughter|madam)\b", re.I)
MAS_EN = re.compile(r"\b(he|him|his|himself|man|guy|boy|sir|father|dad|brother|husband|son|mister|bro|dude)\b", re.I)
FEM_ES = re.compile(r"\b(ella|ellas|señora|señorita|chica|mujer|muchacha|hermana|madre|esposa|hija)\b", re.I)
MAS_ES = re.compile(r"\b(él|ellos|señor|chico|hombre|muchacho|hermano|padre|esposo|hijo|tío|tipo)\b", re.I)
# adjetivo/participio con persona: «estás cansada», «soy nuevo», «te ves preocupado», «gracias, amigo/amiga»
VERBO = r"(?:estás|estas|eres|estoy|soy|estaba|estabas|era|eras|fui|fuiste|has sido|he sido|pareces|parezco|te ves|me veo|te sientes|me siento|quedas|quedé|quedaste|sigues|sigo|vas a estar|estarás|estaré|serás|seré|te has vuelto|me he vuelto|tan|muy|qué|bienvenid)"
ADJ = re.compile(VERBO + r"\s+(?:muy\s+|tan\s+|bastante\s+|demasiado\s+|un poco\s+|algo\s+)?([a-záéíóúñ]+(?:o|a|os|as))\b", re.I)
NO_ADJ = set('''nada algo poco mucho muy otra otro una uno esa eso esta esto toda todo ahora hora casa ropa cosa forma
manera nunca siempre ya nuevo bueno para pero como cuando donde aquí mismo misma solo sola ninguna ninguno ama amo yakuza
cara hacia contra arriba abajo dentro fuera fuerza idea persona gente lo la los las tuyo tuya mío mía suyo suya cuanto
cuanta tanto tanta cierto cierta verdad problema culpa'''.split())


def cmd_genero(j):
    rows = leer(j)
    os.makedirs(SAL[j], exist_ok=True)
    pron, adj = [], []
    for r in rows:
        en, es = limpio(r['ingles']), limpio(r['espanol'])
        if not es.strip() or es == en:
            continue
        fe, me = bool(FEM_EN.search(en)), bool(MAS_EN.search(en))
        fs, ms = bool(FEM_ES.search(es)), bool(MAS_ES.search(es))
        if (fe and not me and ms and not fs) or (me and not fe and fs and not ms):
            pron.append(r)
        m = [x for x in ADJ.findall(es) if x.lower() not in NO_ADJ]
        if m:
            adj.append((r, m))
    with open(os.path.join(SAL[j], 'genero_pronombres.tsv'), 'w', encoding='utf-8') as fh:
        for r in pron:
            fh.write(f"{r['id']}\t{r['donde'][:60]}\t{r['ingles']!r}\t{r['espanol']!r}\n")
    with open(os.path.join(SAL[j], 'genero_adjetivos.jsonl'), 'w', encoding='utf-8') as fh:
        for r, m in adj:
            fh.write(json.dumps({'id': r['id'], 'donde': r['donde'], 'en': r['ingles'], 'es': r['espanol'], 'adj': m},
                                ensure_ascii=False) + '\n')
    print(j, 'pronombres que no casan', len(pron), '| frases con adjetivo de persona', len(adj))


if __name__ == '__main__':
    {'ingles': cmd_ingles, 'genero': cmd_genero}[sys.argv[1]](sys.argv[2])
