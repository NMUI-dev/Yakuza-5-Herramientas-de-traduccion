# -*- coding: utf-8 -*-
"""(06-11-2026) Junta todos los cambios_*.json, los comprueba y los deja listos para la herramienta:
 - la ID existe; « / » se vuelve salto de línea si el original tenía saltos (mismo número de saltos, si no -> error)
 - mismas etiquetas <...>, {…}, %s, ⑬, ⑮ que el original; sin «¿¿», sin inglés nuevo evidente
 - una ID cambiada por dos archivos de forma distinta -> conflicto (se aplican en cadena solo si uno parte del otro; si no, error)
Salida: correcciones_0611.json {id: {en, antes, es, motivo}} + revisar_0611.txt (antes/después para leer) + errores."""
import csv, json, glob, re, collections, sys
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = {r['id']: r for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';')}
ORDEN = ['cambios_manual.json', 'cambios_terminos.json', 'cambios_nombres.json', 'cambios_espana.json'] + sorted(glob.glob('cambios_[0-9].json')) + sorted(glob.glob('cambios_sentido_*.json')) + sorted(glob.glob('cambios_signos_*.json')) + ['cambios_zz_resueltos.json']
def marcas(t): return sorted(re.findall(r'<[^>]*>|\{[^}]*\}|%s|%d|⑬|⑮|♪', t))
out, err, conf = {}, [], []
for f in ORDEN:
    try: d = json.load(open(f, encoding='utf-8'))
    except Exception as e: err.append(f'{f}: JSON roto {e}'); continue
    for c in d.get('cambios', []):
        i = str(c['id']).strip(); r = F.get(i)
        if not r: err.append(f'{f} {i}: no existe'); continue
        base = out[i]['es'] if i in out else r['espanol']
        nuevo = c['es']
        n_or = r['espanol'].count('\n')
        if n_or and nuevo.count('\n') != n_or:
            if nuevo.count(' / ') == n_or: nuevo = nuevo.replace(' / ', '\n')
            elif nuevo.replace(' /\n', '\n').count('\n') == n_or: pass
            else: err.append(f'{f} {i}: saltos {n_or} vs {nuevo.count(chr(10))}/{nuevo.count(" / ")}'); continue
        # subtítulos: el valor lleva comillas de CSV alrededor ("...") y las de dentro dobladas (""): se respetan
        a0 = r['espanol']
        if len(a0) > 1 and a0[0] == '"' and a0.rstrip()[-1] == '"' and not (nuevo[:1] == '"' and nuevo.rstrip()[-1:] == '"'):
            nuevo = '"' + nuevo + '"'
        if a0[:1] == '"' and nuevo.count('"') % 2:
            err.append(f'{f} {i}: comillas impares en subtítulo'); continue
        # espacios finales de cada línea como el original
        if r['espanol'].endswith(' ') and not nuevo.endswith(' '): nuevo += ' '
        if marcas(nuevo) != marcas(r['espanol']):
            err.append(f'{f} {i}: etiquetas distintas {marcas(r["espanol"])} -> {marcas(nuevo)}'); continue
        if '¿¿' in nuevo or '¡¡' in nuevo: err.append(f'{f} {i}: signo doble'); continue
        if nuevo == base: continue
        if i in out and out[i]['es'] != r['espanol'] and f.startswith(('cambios_signos', 'cambios_sentido')) is False:
            conf.append(f'{i}: {out[i]["fuente"]} y {f}')
        if i in out:
            conf.append(f'{i}: {out[i]["fuente"]} -> {f} (se queda el último)')
        out[i] = {'en': r['ingles'], 'antes': r['espanol'], 'es': nuevo, 'motivo': c.get('motivo', ''), 'fuente': f}
json.dump(out, open('correcciones_0611.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
with open('revisar_0611.txt', 'w', encoding='utf-8') as o:
    for i, c in out.items():
        o.write(f"{i} [{c['fuente'][8:-5]}] {c['motivo']}\n  EN: {c['en']}\n  -: {c['antes']}\n  +: {c['es']}\n".replace('\n', '\n') )
print('cambios', len(out), collections.Counter(c['fuente'] for c in out.values()))
print('errores', len(err)); [print(' ', e) for e in err[:40]]
print('conflictos', len(conf)); [print(' ', c) for c in conf[:40]]
