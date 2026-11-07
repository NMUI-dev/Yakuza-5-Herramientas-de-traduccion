# v1.0.10: menús largos mirados en el juego (07-11-2026)

- `ancho_menus_y5.py`: ancho EN PÍXELES de cada texto de menú con la fuente del juego (sd_hankaku.dds) frente al renglón
  inglés más ancho de su columna: 367 marcados. Se miraron en el juego (laboratorio) los menús a los que se llega al
  empezar: Habilidades, Objetos y Lista de logros.
- Encontrado y arreglado:
  - Objetos: el rótulo «Pistola» (imagen, inglés «Gun») era más ancho que su hueco y el número de «Hoja» le tapaba la
    «P» («Hoja 0istola»). Ahora «Bala» (`imagenes_v110.py`: mismo método que la v1.0.5, fuente Times, mismo alto y línea
    de base que «Hoja»), en las 7 copias de la textura (2d_yk_z_common de los 6 personajes + pjd_omiyage).
    `meter_v110.sh` la mete en 2dpar/ui_en.par y comprueba que solo cambian esas 7 de los 1.011 archivos.
  - Habilidades: la categoría «Entrenamiento/Revelaciones» (294 px) se salía de su caja (~235 px): «Entreno/Revelaciones».
- Los nombres de habilidades y las descripciones tienen sitio de sobra (la descripción se reparte sola en renglones).
- Sin mirar en el juego (salen horas después): idol de Haruka, misiones de la montaña de Saejima, tutoriales, carreras.
