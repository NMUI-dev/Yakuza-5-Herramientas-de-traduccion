# -*- coding: utf-8 -*-
"""(06-11-2026) Correcciones a mano de esta revisión (leídas en su escena) + nombre del orfanato unificado.
Orfanato: el Y5 decía «Morning Glory» en ~30 frases y «Campanilla»/«gloria matutina»/«Hogar de huérfanos» en otras; el Y6 dice
«Orfanato Morning Glory» -> todo «Morning Glory». Salida: cambios_manual.json."""
import csv, json, re
CSV = 'C:/Mods/yakuza5/entrega_v105/Herramientas para traduccion/trabajo/textos.csv'
F = {r['id']: r for r in csv.DictReader(open(CSV, encoding='utf-8-sig', newline=''), delimiter=';')}
A = {
 '36408': ('Ahí. ¿Ves a ese hombre? Ese es Christina.', 'género: Christina es hombre'),
 '31757': ('Decía cosas como: "El guiso de venado me está llamando". Además, tenía los ojos inyectados en sangre. Se veía bastante aterradora.', 'género: habla de una mujer'),
 '37583': ('Así que la perseguí... Cuando me di cuenta, ya le estaba\ngolpeando la cabeza contra el suelo del pasillo.', 'gramática: le estaba golpeando la cabeza'),
 '48527': ('Es la mejor hermana del mundo. ¡Así que, por favor, sigue velando por Mieko!', 'sentido: faltaba la primera frase'),
 '49734': ('(Esta es la máquina de tragamonedas King Camel, número 86. ¿Debería probarla?)', 'sentido: el número es 86'),
 '34469': ('Tres años... solo por agresión. Solo hay dos razones por las que alguien cumpliría tanto tiempo por un delito tan menor.', 'sentido: faltaba la segunda frase (la siguiente dice «Uno:...»)'),
 '49501': ('Corta tus lloriqueos, chavo. Reconozco una pelota trucada en cuanto la veo.', 'sentido: faltaba la segunda frase'),
 '55656': ('¿Sabes? Usamos miso en casi todo lo que cocinamos. ¿Será por eso que mi mamá y yo somos tan bonitas?', 'sentido: faltaba la primera frase'),
 '32279': ('¡Hey! ¡Vi esa cara que hiciste! Estás pensando "Vaya, sigue siendo toda una niña", ¿eh?', 'sentido: frase cortada «de lo más» y signos'),
 '33080': ('Estuvo muy divertido, ¿verdad? Creo que la próxima vez pediré a Mayumi-chan.', 'estilo: «a la Mayumi-chan»'),
}
for i, r in F.items():
    es = r['espanol']
    if i in A or not es: continue
    n = es.replace('Hogar de huérfanos Morning Glory', 'Orfanato Morning Glory').replace('Orfanato Campanilla', 'Orfanato Morning Glory') \
          .replace('gloria matutina', 'Morning Glory').replace('Bufanda de campanilla', 'Bufanda de Morning Glory')
    n = re.sub(r'\bCampanilla\b', 'Morning Glory', n)
    if i == '17206': n = 'Obtuviste <Color:8>Faja abdominal de Morning Glory<Color:Default>.'
    if i == '13627': n = 'Morning Glory se emocionaron.'
    if n != es: A[i] = (n, 'nombre del orfanato unificado: Morning Glory (como en el resto del Y5 y en el Y6)')
json.dump({'cambios': [{'id': k, 'es': v[0], 'motivo': v[1]} for k, v in A.items()], 'dudas': []},
          open('cambios_manual.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
for k, v in A.items(): print(k, '|', F[k]['espanol'][:90].replace('\n', ' / '), '=>', v[0][:90].replace('\n', ' / '))
