# v1.0.7: reglas profesionales + NUNCA CENSURAR (06-11-2026)

Reglas del usuario: **nunca censurar** («hay que mantener la esencia de la obra»: una grosería se traduce con la misma
fuerza), **preguntar a las IA en cadena qué falta** y **seguir las reglas reales de los traductores profesionales**
(Netflix español latino, guía de Microsoft para español neutro, RAE). Cada caso se decidió con su escena delante.

2.010 textos corregidos (`correcciones_0611b.json`: id, inglés, antes, ahora, motivo y de qué revisión salió):

| Tipo | Textos |
|---|---|
| renglón partido por mal sitio («de la / Familia»): solo se movió una palabra, sin alargar | 1.015 |
| signos ¿? ¡! sin pareja o perdidos (el inglés exclamaba o preguntaba) | 666 |
| groserías SUAVIZADAS subidas a la fuerza del original | 113 |
| sentido: trozos perdidos, nombre cambiado, 7 textos desplazados en mail.bin, 13 finales de correo en inglés | 64 |
| gramática: le->les, quiénes, género y número de los objetos | 60 |
| España o un solo país -> neutro con la misma fuerza | 36 |
| risas Haha/Hehe -> Jaja/Jeje | 36 |
| erratas, espacios, palabras rotas | 16 |
| tú/usted | 4 |

## Programas
Todos leen el CSV de la variable `Y5_TEXTOS` (si no, el `trabajo/textos.csv` de la entrega). Solo marcan: se decide a mano.
- `censura_y5.py`: inglés con fuck/shit/bitch/bastard... y español sin grosería (posible suavizado).
- `barrido_fijo_y5.py`, `barrido_ias_y5.py`, `barrido_extra_y5.py`: España y regionalismos, palabras repetidas,
  honoríficos perdidos (frases que perdieron el trozo con -san), le/les, quién/quiénes, signos, mayúsculas, espacios.
- `desalineados_y5.py`: nombre propio o cifra en el español que el inglés no tiene (encontró el bloque desplazado de mail.bin).
- `ideas_ia_y5.py`: japonés olvidado y artículo que no concuerda con el objeto («el <Color:8>Barbacoa»).
- `saltos_sentido_y5.py`: renglones que terminan en artículo, preposición, «que», «no»...
- `letras_fuente_y5.py`: cada letra del español tiene dibujo en la fuente (sale 0: la fuente tiene todo Latin-1; no tiene «…»).
- `filtro_mayusculas.py`: lo que el filtro `es_texto` tomaba por código. Halló 13 finales de correo («then.», «danger.»)
  que quedaban en inglés: la herramienta los acepta ahora (`CORTAS_SI`).
- `preguntar_cadena_y5.py` + `pregunta_cadena_base.md`: pregunta a las IA gratuitas, una detrás de otra, qué falta;
  respuestas en `ideas_de_las_IA.md` (53 ideas).
- `contexto.py`: la escena alrededor de cada aviso; `INSTRUCCIONES.md`: lo que se les dio a los ayudantes.
- `cambios_manual.py` (decisiones a mano), `revisar_censura.py` (revisión de lo que propuso el ayudante), `clasificar.py`
  (separa cambios de solo signos y de texto para revisarlos), `juntar.py` (junta por prioridad; frena etiquetas o saltos
  rotos y frases de globo (pac) que ya no caben: ahí la herramienta dejaría el INGLÉS; reparte los renglones).
- `datos_v107.py`, `version_v107.py`, `v107_armar.sh`, `comprobar_v107.sh` + `comprobar_armados.py`: arman el paquete con
  esta herramienta y buscan cada corrección dentro de los archivos armados (1.994 de 2.010; las 16 restantes son la copia
  «extra-sub» de un subtítulo de dos renglones que el juego no muestra: se corrigió también la fila «sub» que sí sale).

## Lecciones
- En los globos (pac) el español no puede ocupar más bytes que el inglés: si no cabe, la herramienta deja el inglés.
- Cada subtítulo de dos renglones sale dos veces en el CSV («sub» con comillas y «extra-sub»): corregir los dos.
- Lo que se cambia por ser de España va por otra palabra igual de fuerte; «jodido» o «no me jodas» valen en Latinoamérica.
