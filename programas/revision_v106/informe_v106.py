# -*- coding: utf-8 -*-
"""Escribe «Errores corregidos v1.0.6.txt» (todas las frases cambiadas, por tipo, con inglés/antes/ahora/motivo)."""
import json, collections
d = json.load(open('correcciones_0611.json', encoding='utf-8')); t = json.load(open('tipos_0611.json', encoding='utf-8'))
por = collections.defaultdict(list)
for i, c in d.items(): por[t[i]].append((i, c))
orden = ['trato tú/usted', 'sentido', 'género', 'nombre de objeto/técnica igual que en el menú', 'nombres propios unificados',
         'expresiones de España', 'signos ¿? ¡!', 'erratas, gramática e inglés colado']
L = ['ERRORES CORREGIDOS EN LA v1.0.6 (06-11-2026)', '',
     'Revisión POR ESCENAS: programas buscaron en TODO el juego (106.814 líneas en 3.311 escenas) cambios de trato, señales de',
     'error de sentido, signos rotos y nombres distintos; cada caso se leyó con su conversación (quién habla, a quién, trato y género),',
     'como pidió el usuario: «antes de traducir una sola frase hay que entender todo el contexto de la conversación».',
     f'Total: {len(d)} frases. Comprobadas dentro de los archivos armados del juego (1.151; las 2 restantes son variantes',
     'de subtítulo que el juego no usa) y probado en el juego (menú y comienzo de partida).', '']
for k in orden: L.append(f'  {len(por[k]):5d}  {k}')
for k in orden:
    L += ['', '=' * 100, f'{k.upper()} ({len(por[k])})', '=' * 100]
    for i, c in sorted(por[k], key=lambda x: int(x[0])):
        f = lambda s: s.replace('\r\n', ' / ').replace('\n', ' / ')
        L += [f'[{i}] {c["motivo"]}', f'   EN:    {f(c["en"])}', f'   Antes: {f(c["antes"])}', f'   Ahora: {f(c["es"])}']
open('C:/Mods/Entregas/Entregas Yakuza 5/Lo que queda en ingles v1.0.6/4 Errores corregidos/Errores corregidos v1.0.6.txt', 'w',
     encoding='utf-8-sig', newline='\r\n').write('\n'.join(L) + '\n')
print('ok', len(L))
