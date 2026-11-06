# Yakuza 5 (español latino): signos y sentido

Archivos signos_N.txt: `ID<TAB>inglés<TAB>español`. « / » = salto de línea (consérvalo igual).
Arregla SOLO los signos de exclamación/interrogación del español, según la norma:
- Cada pregunta/exclamación se abre y se cierra: «¿...?», «¡...!». Si el inglés hace «!?» -> «¡¿...?!» o «¿¡...!?» (vale cualquiera
  de las dos, pero abre y cierra con las dos).
- Prohibido abrir dos veces seguidas sin cerrar: «¿Piensas mucho, ¿verdad?» -> «Piensas mucho, ¿verdad?»; «¡Ah, ¿sabes qué?» ->
  «Ah, ¿sabes qué?»; «¡No puedo esperar. ¡Esto...» -> «¡No puedo esperar! ¡Esto...» (o quitar el primer «¡» si no es exclamación en inglés).
- Si la frase se corta con «...» o «⑬» dentro de una exclamación, el cierre puede faltar solo si el inglés también corta; si no,
  ciérrala.
- No toques nada más (palabras, etiquetas <...>, %s, ⑬, ⑮, ♪). Si además ves un error de sentido evidente, arréglalo y dilo.
- Si la línea está bien (falso aviso), no la pongas.

Archivos sentido_N.txt: `ID<TAB>avisos<TAB>inglés<TAB>español`. Avisos: preg (el inglés pregunta y el español no, o al revés),
neg (el inglés niega y el español no), corta (al español le falta un trozo), num (número distinto).
Para cada una: ¿el español dice LO MISMO que el inglés? Muchos avisos son falsos (p. ej. «No way!» = «¡Imposible!» está bien,
«You know what?» no es pregunta real). Corrige solo lo que de verdad dice otra cosa, falta un trozo, cambia una negación o un número,
o pierde/inventa una pregunta. Conserva el trato tú/usted, el género, el tono y las etiquetas tal cual.

Salida (UTF-8, JSON válido, con la herramienta Write) en esta carpeta: `cambios_signos_N.json` o `cambios_sentido_N.json`:
{"cambios": [{"id": "...", "es": "texto completo nuevo", "motivo": "..."}], "dudas": [{"id": "...", "nota": "..."}]}
Responde solo con cuántos cambios y dudas.
