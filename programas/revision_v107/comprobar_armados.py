# -*- coding: utf-8 -*-
"""(06-11-2026) Cada corrección de la v1.0.7 (correcciones_0611b.json) se busca en los ARCHIVOS ARMADOS por el trozo que
CAMBIA (lo que no estaba antes), con las letras como las pone la herramienta. Los pac usan su versión corta (datos/cortas.json)."""
import json, os, re, sys, importlib.util, difflib
sys.stdout.reconfigure(encoding='utf-8')
HT = 'C:/Mods/yakuza5/entrega_v107/Herramientas para traduccion/'
spec = importlib.util.spec_from_file_location('h', HT + 'herramienta_traduccion.py'); h = importlib.util.module_from_spec(spec)
sys.argv = ['x']; spec.loader.exec_module(h)
corr = json.load(open('C:/Mods/yakuza5/trabajo/revision_0611b/correcciones_0611b.json', encoding='utf-8'))
C = json.load(open(HT + 'datos/cortas.json', encoding='utf-8'))
blob8, blob16 = bytearray(), bytearray()
for dp, _, fs in os.walk('x'):
    for f in fs:
        b = open(os.path.join(dp, f), 'rb').read()
        (blob16 if f.lower().endswith('.csv') else blob8).extend(b + b'\n')
def trozo(new, old):
    """Trozo de 'new' alrededor del primer cambio, sin etiquetas ni saltos (máx. una línea)."""
    sm = difflib.SequenceMatcher(None, old, new)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op == 'equal': continue
        ini = max(0, b1 - 6); fin = min(len(new), max(b2, b1 + 1) + 6)
        t = new[ini:fin]
        partes = [p for p in re.split(r'<[^>]*>|\n|\r|%s|\{[^}]*\}', t) if p.strip()]
        if partes: return max(partes, key=len)
    return None
ok = falta = 0; malos = []
for i, c in corr.items():
    new = c['es']; k = h.norm(c['en'])
    if k in C and 'pac' in str(c.get('fuente', '')) or k in C: new = C[k] if k in C else new
    t = trozo(new, c['antes']) or new
    t = t.translate(h.LETRAS)
    for cand in {t, t.replace('""', '"')}:
        if cand.encode('utf-8') in blob8 or cand.encode('utf-16-le') in blob16: ok += 1; break
    else: falta += 1; malos.append((i, c['fuente'], t))
print('encontradas', ok, 'NO encontradas', falta)
for m in malos: print('  ', m)
