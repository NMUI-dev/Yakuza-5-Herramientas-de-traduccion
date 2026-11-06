# -*- coding: utf-8 -*-
"""(06-11-2026) Barrido como el barrido_fijo.py del Y6 (claude1): formas de España en un juego en español latino,
«tío Kaz» (en el Y5 es «viejo Kaz») y nombres del mapa con dos formas (criterio v1.0.3 = saga oficial:
«Pequeña Asia», «Tienda M»). Salida: cambios_espana.json. Se aplica sobre el texto v1.0.5 (antes de las demás)."""
import csv, json, re
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = {r['id']: r for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';')}
A = {
 '68430': ('En serio, ¿no les enseñan\n<Italic>nada</Italic> hoy en día?', 'España: os -> les'),
 '68437': ('Y aquí estamos. Akiyama les ganó a todos,\ny seguimos sin la carta.', 'España: os ha vencido -> les ganó'),
 '68438': ('Pero tenían buena intención,\nasí que no los voy a regañar.', 'España: teníais/os -> tenían/los'),
 '68432': ('Sueñen lo que quieran, pero nada de eso\nimporta un carajo cuando te enfrentas a la fuerza real.', 'España: soñad/queráis -> sueñen/quieran'),
 '68801': ('No se trata de si él\nrenunció a su juramento.', 'España: vuestro -> su'),
 '17755': ('¡Hmph! ¡Deberías darte vergüenza, si me preguntas! ¡Una\npapa bailaría mejor que tú!', 'latino: patata -> papa'),
 '17788': ('¡Ja! ¡Perdiste! ¡Como esperaba! ¡Te dije que una papa\nbailaría mejor que tú!', 'latino: patata -> papa'),
 '1647': ('Vamos.', 'España: venga -> vamos'),
 '9746': ('¡Ay, por favor!', 'España: ¡Venga ya!'),
 '61935': ('De acuerdo', '«Me vale» en México es «no me importa»; «Cool by me» = de acuerdo'),
}
for i in ['21178', '22838', '22879', '32332', '35000', '36586', '42857', '52364', '54801', '59000', '59046', '25080']:
    A[i] = (F[i]['espanol'].replace('¡Venga, hijo!', '¡Ándale, hijo!').replace('Venga', 'Vamos'), 'España: «¡Venga!» -> «¡Vamos!»')
for i, r in F.items():
    es = r['espanol']
    if i in A or not es: continue
    n = re.sub(r'\b([Tt])ío Kaz', lambda m: ('V' if m.group(1) == 'T' else 'v') + 'iejo Kaz', es)
    n = n.replace('patata', 'papa').replace('Kyuta el Chaval', 'Kyuta el Chico')
    n = n.replace('Little Asia', 'Pequeña Asia').replace('una M Store', 'una Tienda M').replace('M Store', 'Tienda M')
    if n != es: A[i] = (n, 'tío Kaz -> viejo Kaz / latino / nombres del mapa como en la saga oficial (Pequeña Asia, Tienda M)')
for i, (v, m) in A.items():
    if F[i]['espanol'].endswith(' ') and not v.endswith(' '): A[i] = (v + F[i]['espanol'][len(F[i]['espanol'].rstrip()):], m)
json.dump({'cambios': [{'id': k, 'es': v, 'motivo': m} for k, (v, m) in A.items()], 'dudas': []},
          open('cambios_espana.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
for k, (v, m) in A.items(): print(k, '|', F[k]['espanol'][:70].replace('\n', ' / '), '=>', v[:70].replace('\n', ' / '))
