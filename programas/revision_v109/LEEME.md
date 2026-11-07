# v1.0.9: punto y coma fuera de las comillas + ronda final de preguntas (07-11-2026)

- `comillas_y5.py`: punto o coma de cierre DENTRO de las comillas pasa a ir fuera (RAE; idea de claude1 en el Y6):
  151 textos. Solo comillas de cierre, nunca en subtítulos (ahí las comillas de fuera son del formato del archivo) y
  respetando «...». Mismos bytes. `juntar_v109.py` -> `datos_v109.py` -> `v109_armar.sh` -> `comprobar_v109.sh`:
  151 de 151 dentro de los archivos armados.
- Ronda final del ciclo de preguntas (regla del usuario): OpenRouter sin cuota todo el día (429); Gemini 3.7 y 3.5
  dieron 12 ideas (`programas/revision_v108/ideas_de_las_IA_2.md`, 29 en total). `ideas_ia3_y5.py` comprobó las que
  se pueden programar: escala «billion» = mil millones (1 aviso: «un millón de veces», exageración, bien) y códigos de
  casillero iguales al inglés (0). Las demás (nombres de minijuegos y menús) ya las cubrían terminos_color (v1.0.6) y
  terminos_y5 (v1.0.8).
- `preguntar_cadena_y5.py` (revision_v108): arreglado el cliente de Gemini («the client has been closed»: hay que
  guardarlo en una variable); `preguntar_cadena_gemini.py`: la misma pregunta solo a Gemini.
