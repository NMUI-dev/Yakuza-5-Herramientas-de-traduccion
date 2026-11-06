# v1.0.6: revisión por escenas (06-11-2026)

Regla del usuario: **antes de traducir o tocar una sola frase, entender toda la conversación** (quién habla, a quién,
género, trato tú/usted, qué se dijo antes y después).

1.153 frases corregidas (`correcciones_0611.json`: id, inglés, antes, ahora, motivo y de qué revisión salió):

| Tipo | Frases |
|---|---|
| signos ¿? ¡! mal abiertos o cerrados | 388 |
| nombre de objeto/técnica/plato igual que en el menú | 295 |
| trato tú/usted mezclado en la misma conversación | 219 |
| sentido (trozos que faltaban, negaciones, números, preguntas) | 99 |
| nombres propios unificados (Morning Glory, Empresas Ousaka, Pequeña Asia, Tienda M, viejo Kaz...) | 83 |
| erratas, gramática e inglés colado | 30 |
| expresiones de España -> español latino | 22 |
| género | 17 |

## Programas (en el orden en que se usan)
- `escenas.py`: monta las 3.311 escenas del juego en orden, con quién habla ([Prota]/[Otro], sacado del .msg japonés).
- `tratamiento.py`, `ver_usted.py`, `mezcla.py`: cuentan tú/usted y sacan los tramos donde la misma voz cambia de trato.
- `genero_tercera.py`: género en tercera persona (correos, fichas, objetos) contra she/he del inglés.
- `sentido.py`: avisos de sentido (falta un trozo, número distinto, pregunta o negación perdida, signos rotos).
- `terminos.py`, `terminos_color.py`: nombres del menú citados con otra traducción en los diálogos (los de
  `<Color:8>`/`<Color:9>` se igualan solos).
- `nombres.py`, `espana.py`, `manual.py`: nombres propios unificados, formas de España y arreglos a mano.
- `INSTRUCCIONES_*.md`: lo que se les dio a los ayudantes (cada caso con su escena) para tú/usted, signos y sentido.
- `juntar.py`: junta todo, comprueba etiquetas, saltos de línea y comillas de subtítulo, y avisa de choques.
- `poner_en_csv.py` + `herramienta_traduccion.py aplicar`; `comprobar_armados.py`: busca cada corrección dentro de
  los archivos armados del juego (1.151 de 1.153; las 2 que faltan son variantes de subtítulo que el juego no usa).
- Las frases de largo fijo (pac) que no cabían tienen su versión corta en `datos/cortas.json`.
