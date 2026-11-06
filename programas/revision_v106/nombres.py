# -*- coding: utf-8 -*-
"""(06-11-2026) Nombres propios con dos formas -> una sola en todo el juego.
 - «Empresas Ousaka» (subtítulos, menús y fichas ya lo decían) y «Palacio del Dragón» (criterio v1.0.3, saga oficial): se
   cambian los diálogos que seguían en inglés.
 - «Kamurocho Hills» y «Devil Killers» (la banda): casi todo el juego los deja en inglés (17 y ~100 frases); se cambian
   las pocas tablas que los traducían («Colinas de Kamurocho», «asesinos del diablo»).
Salida: cambios_nombres.json."""
import csv, json, re
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = list(csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';'))
R = [('Ousaka Enterprises', 'Empresas Ousaka'), ('Dragon Palace', 'Palacio del Dragón'),
     ('Colinas de Kamurocho', 'Kamurocho Hills'), ('Los asesinos del diablo', 'Los Devil Killers'),
     ('los asesinos del diablo', 'los Devil Killers'), ('Asesino demoníaco', 'Devil Killer')]
out = []
for r in F:
    es = r['espanol']; n = es
    for a, b in R: n = n.replace(a, b)
    n = n.replace(' de Palacio del Dragón', ' del Palacio del Dragón')
    if n != es: out.append({'id': r['id'], 'es': n, 'motivo': 'nombre propio unificado en todo el juego'})
json.dump({'cambios': out, 'dudas': []}, open('cambios_nombres.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print(len(out))
for c in out: print(c['id'], c['es'][:110].replace('\n', ' / '))
