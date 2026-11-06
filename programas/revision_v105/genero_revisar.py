# -*- coding: utf-8 -*-
"""(05-11-2026) Revisor de GÉNERO con ayudantes gratuitos (Gemini 3.5 flash -> OpenRouter :free).
Lee los lotes de genero_lotes.py y deja <lote>_rev.json = {"cambios": [{"id", "es", "motivo"}], "modelo": ...}.
Reparto entre hilos con mkdir atómico (lotes/reclamados/NNN). Retoma solo lo que falta.
  python genero_revisar.py Y5|Y6 NOMBRE_HILO
Claves: GEMINI_API_KEY y OPENROUTER_API_KEY en el entorno (nunca en archivos).
"""
import difflib, json, os, re, sys, time, urllib.request, urllib.error

J, QUIEN = sys.argv[1], sys.argv[2]
SAL = {'Y5': 'C:/Mods/yakuza5/trabajo/revision_steam_0511', 'Y6': 'C:/Mods/yakuza6/trabajo/revision_steam_0511'}[J]
L = f'{SAL}/lotes'
MODELOS = os.environ.get('MODELOS', 'gemini-3.5-flash or:nvidia/nemotron-3-ultra-550b-a55b:free '
                         'or:google/gemma-4-31b-it:free or:nvidia/nemotron-3.5-lightning:free').split()

PERSONAJES = {
    'Y5': '''Yakuza 5. HOMBRES: Kazuma Kiryu (alias «Suzuki», taxista en Fukuoka/Nagasugai; le dicen Kiryu-san, Kiryu-han,
Kiryu-chan, tío Kaz/Uncle Kaz, Dragón de Dojima), Taiga Saejima, Shun Akiyama, Tatsuo Shinada, Daigo Dojima, Goro Majima,
Kanai, Morinaga, Aizawa, Watase, Baba, Kitakata, Hamazaki, Madarame, Aoyama, Kurosawa, Aoki, Kamiyama, Ogita, Kosaka,
Takasugi, Kubota, Manabe, Oshima, Daidoji, Yamaura, Okudera, Nishina, Leo-kun. MUJERES: Haruka Sawamura, Mirei Park,
Mai, Azusa, Hana, Yui, Mayumi, Asuka, Nanako, Airi, Misa, Yoko, Milky-chan, Ayaka, las idols, anfitrionas y mamas.''',
    'Y6': '''Yakuza 6. HOMBRES: Kazuma Kiryu (le dicen Kiryu-san, Kiryu-chan, tío Kaz/Uncle Kaz, aniki, Dragón de Dojima),
Haruto (bebé, niño), Yuta Usami, Tsuyoshi Nagumo, Toru Hirose, Hirose, Joji Kazama, Someya, Iwami (Tsuneaki y Yoshiaki),
Takeru Kurusu? (no), Daigo Dojima, Goro Majima, Saejima, Akiyama, Date, Nishiki, Kazama, Big Tiger, Kurosawa, Munan,
Ono Michio (el mono). MUJERES: Haruka Sawamura, Kiyomi Matsunaga (mama del snack), Yumi, Mayumi, Rina, Hikaru, Erina,
Sora, Riona, Saki (anfitrionas del cabaret), Yuka, la mama del bar, Takako, la abuela.'''}[J]

GUIA = f'''Eres corrector de una traducción al español de {PERSONAJES[:9]} (de inglés a español latino neutro).
{PERSONAJES}
PROBLEMA A CORREGIR: la traducción se hizo sin saber quién habla ni a quién. Hay frases con el GÉNERO gramatical equivocado:
por ejemplo Kiryu (hombre) dice «estoy cansada» o una mujer le dice a Kiryu «eres muy amable, chica» / «estás loca»; o Kiryu
le habla a una mujer en masculino («estás preocupado», «gracias, amigo»), o una mujer habla de sí misma en masculino
(«estoy seguro»), o alguien habla de una tercera persona con el género cambiado.
Te doy ítems. Cada uno trae la frase a revisar (en, es) y su CONTEXTO: las líneas de la escena en orden, «inglés || español»,
la marcada con «>>» es la del ítem. Quién habla, si se sabe: [Prota] = el protagonista que maneja el jugador en ese
capítulo (Kiryu, Saejima, Akiyama o Shinada = HOMBRES; Haruka = MUJER, en sus capítulos de idol); [Otro] = la otra persona
de la conversación; [P123] = número del personaje (mismo número = misma persona). Sin marca = no se sabe.
Deduce por el contexto quién habla y a quién. Si NO está claro, NO cambies la frase (un cambio equivocado es peor).
REGLAS:
1. Corrige SOLO errores de género (adjetivos, participios, artículos, pronombres, vocativos). No cambies estilo, vocabulario
   ni nada más. Si la frase está bien o no se puede saber con seguridad, NO la pongas.
2. Si "veces" > 1 la misma frase sale en varias escenas con distintas personas: si el género cambia según la escena, propón
   una versión NEUTRA que valga para todos (p. ej. «¿Estás bien?» en vez de «¿Estás herida?» -> «¿Te hiciste daño?»).
3. Conserva exactamente las etiquetas <...>, {{...}}, los saltos de línea (\\n) y su número, y una longitud parecida (no más larga).
4. Español latino neutro, el mismo tono de la traducción.
Responde SOLO JSON: {{"cambios": [{{"id": "<id>", "es": "<frase corregida completa>", "motivo": "<quién es quién, breve>"}}]}}
Si no hay nada que corregir: {{"cambios": []}}
ÍTEMS:
'''


def log(*a): print(time.strftime('%H:%M:%S'), QUIEN, *a, flush=True)


_gem = None
def gemini(m, prompt):
    global _gem
    from google import genai
    from google.genai import types
    if _gem is None: _gem = genai.Client(http_options=types.HttpOptions(timeout=240000))
    r = _gem.models.generate_content(model=m, contents=prompt, config=types.GenerateContentConfig(
        response_mime_type='application/json', temperature=0.2))
    return r.text


def openrouter(m, prompt):
    q = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', headers={
        'Authorization': 'Bearer ' + os.environ['OPENROUTER_API_KEY'], 'Content-Type': 'application/json'},
        data=json.dumps({'model': m, 'temperature': 0.2, 'response_format': {'type': 'json_object'},
                         'messages': [{'role': 'user', 'content': prompt}]}).encode())
    try: return json.load(urllib.request.urlopen(q, timeout=300))['choices'][0]['message']['content']
    except urllib.error.HTTPError as e: raise Exception(f'{e.code} {e.read()[:200]}')


agotado = {}
def pedir(prompt):
    for m in MODELOS:
        if agotado.get(m, 0) > time.time(): continue
        for intento in range(3):
            try:
                t = openrouter(m[3:], prompt) if m.startswith('or:') else gemini(m, prompt)
                t = re.sub(r'^```(?:json)?|```$', '', t.strip()).strip()
                return json.loads(t), m
            except Exception as e:
                s = str(e)
                if '429' in s or 'RESOURCE_EXHAUSTED' in s:
                    if 'PerDay' in s or 'per day' in s.lower() or intento == 2:
                        agotado[m] = time.time() + 3600; log(m, 'sin cuota 1 h'); break
                    time.sleep(30); continue
                if '404' in s: agotado[m] = time.time() + 10 ** 9; log(m, 'no existe'); break
                log(m, 'error', s[:120]); time.sleep(8)
    return None, None


def etiquetas(t): return sorted(re.findall(r'<[^>]*>|\{[^}]*\}', t))


def valido(it, nuevo):
    if not isinstance(nuevo, str) or not nuevo.strip() or nuevo == it['es']: return 'igual o vacío'
    if etiquetas(nuevo) != etiquetas(it['es']): return 'etiquetas distintas'
    if nuevo.count('\n') != it['es'].count('\n'): return 'saltos de línea distintos'
    if len(nuevo) > len(it['es']) + 6: return 'más larga'
    if difflib.SequenceMatcher(None, it['es'], nuevo).ratio() < 0.6: return 'cambia demasiado'
    return ''


def revisar(n):
    lote = json.load(open(f'{L}/lote_{n}.json', encoding='utf-8'))
    por_id = {it['id']: it for it in lote}
    txt = '\n'.join(json.dumps({'id': it['id'], 'veces': it['veces'], 'en': it['en'], 'es': it['es'], 'contexto': it['ctx']},
                               ensure_ascii=False) for it in lote)
    r, m = pedir(GUIA + txt)
    if r is None: return False
    ok, malos = [], []
    for c in r.get('cambios', []) if isinstance(r, dict) else []:
        it = por_id.get(str(c.get('id')))
        if not it: continue
        e = valido(it, c.get('es'))
        (malos if e else ok).append(dict(c, id=it['id'], antes=it['es'], en=it['en'], **({'fallo': e} if e else {})))
    json.dump({'modelo': m, 'cambios': ok, 'rechazados': malos}, open(f'{L}/lote_{n}_rev.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    log(f'lote {n}: {len(ok)} cambios, {len(malos)} rechazados ({m})')
    return True


def main():
    os.makedirs(f'{L}/reclamados', exist_ok=True)
    nums = sorted(f[5:8] for f in os.listdir(L) if re.fullmatch(r'lote_\d{3}\.json', f))
    for n in nums:
        if os.path.exists(f'{L}/lote_{n}_rev.json'): continue
        try: os.mkdir(f'{L}/reclamados/{n}')
        except FileExistsError: continue
        while not revisar(n):
            log('todos los modelos sin cuota: espero 20 min'); time.sleep(1200)
    log('fin')


if __name__ == '__main__':
    main()
