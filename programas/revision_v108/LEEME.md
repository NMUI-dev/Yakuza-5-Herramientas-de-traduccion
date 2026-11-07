# v1.0.8: velocidad de lectura y términos únicos (06-11-2026)

Las tres comprobaciones de la lista común que faltaban en el Y5 (las había pasado claude1 en el Y6). 166 textos
(`correcciones_0711.json`):
- `velocidad_y5.py`: letras por segundo de los 4.785 subtítulos de escena (fotogramas de auth/subtitle.par, 30 por
  segundo) contra el inglés. 28 pedían más de 20 letras/s y más de 1,25 veces el inglés: 26 subtítulos acortados de forma
  natural (con su copia «extra-sub»); de paso, «Suselegantes» y «the force» = la policía.
- `terminos_y5.py`: variantes de los términos de juego. «health» = «salud» (como la saga oficial: 571 contra 4; antes
  también «vida», 106 frases) y «hostess club» = «club de anfitrionas» (un globo conserva «club de cabaré»: no cabe).
  Excluidas las frases con «life»/«live» en inglés («lifestyle» = vida).
- `largo_menus_y5.py`: textos de menú más largos que el inglés más largo de su columna (170, sobre todo nombres de
  habilidades). Solo se puede decidir mirándolo en el juego: queda listado, sin cambios.
- `cambios_v108.py` -> `juntar_v108.py` (base = texto v1.0.7; 10 renglones más partidos por sentido) -> `datos_v108.py`,
  `version_v108.py`, `v108_armar.sh`, `comprobar_v108.sh`: 166 de 166 dentro de los archivos armados.
- `ideas_ia2_y5.py` (ideas del 2.º ciclo de preguntas): ORDEN de variables distinto del inglés. Halló el aviso de
  pesca de string_tbl.bin («¡Atrapaste un %s de %d cm!»): en una cadena de formato el número caía donde va el nombre.
  Ahora con el orden del inglés. También: plurales «(s)», caracteres rotos y botones con varias traducciones (0).
- `falsos_amigos_y5.py` (2.º ciclo): «eventualmente» por eventually, «asumir» por assume, «simpatía» por sympathy
  (10 corregidos, con la copia del subtítulo si la hay) y una ficha de personaje a la que le faltaba una frase.
- `pregunta_cadena_base.md`: la pregunta del segundo ciclo de preguntas a las IA (regla del usuario: al terminar cada trabajo); respuestas en `ideas_de_las_IA_2.md`
  (17 ideas: Kilo y Xing; OpenRouter saturado y Gemini sin cuota ese día).
