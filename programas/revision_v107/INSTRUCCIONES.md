# Revisión Y5 v1.0.7 (claude2, 06-11-2026) — instrucciones para ayudantes

Traducción de fans de Yakuza 5 Remastered al ESPAÑOL NEUTRO LATINOAMERICANO, desde el inglés oficial.
Cada bloque «### id N [TIPO]» trae la escena: «[hablante] inglés || español» por línea; «>>» marca la línea a revisar.
« / » dentro de una línea = salto de renglón real del juego.

REGLAS (del usuario, obligatorias):
1. Entender la escena entera antes de tocar una frase (quién habla, a quién, tono, qué se dijo antes y después).
2. NUNCA CENSURAR: groserías con la MISMA fuerza que el inglés (fuck/shit/bitch/bastard -> mierda, carajo, cabrón,
   hijo de puta, maldito, jodido, pendejo NO (México), etc.). «Cuidado con lo que dices» por «Watch your fuckin' mouth» está
   MAL: «Cuida tu maldita boca». Pero tampoco poner groserías donde el inglés no las tiene.
3. Español neutro: nada de España (vosotros, vale, tío, chaval, memeces, coger, ni de coña, a por, ¡Joder!) ni de un solo
   país (mamadas, chido, güey, órale, pendejo, boludo). «jodido», «no me jodas», «que se joda» sí valen.
4. Fiel al original; solo se localiza lo que en español no se entendería (frases hechas, chistes), con la misma intención.
5. Signos: ¿? y ¡! con pareja dentro de la MISMA línea; «!?» del inglés -> «¡¿...?!». OJO: algunas líneas son TROZOS de
   una frase que sigue en la línea siguiente (el inglés tampoco termina): no les pongas el signo de cierre/apertura que
   está en la otra línea. Títulos de canciones o nombres en inglés entre comillas («"So Much More!"») NO se tocan.
6. Si el inglés acaba en ! o ? y el español no: decide por la escena. Si el tono es exclamativo, ponlo; si el español
   está bien así, NO lo cambies (no hace falta cambiar todo).
7. NO cambiar: etiquetas <...>, %s, ⑬, (改行), saltos « / » (mismo número y en sitio razonable), nombres propios.
8. Si ves en la línea marcada OTRO fallo claro (sentido cambiado, género, tú/usted, nombre equivocado, frase cortada),
   corrígelo también y dilo en el motivo. No toques las líneas sin «>>».

SALIDA: solo un archivo JSON (UTF-8) con lo que CAMBIA (lo que esté bien no se pone):
{"<id>": {"es": "<español completo nuevo, con \n donde había « / »>", "motivo": "<tipo: breve>"}}
Tipos de motivo: grosería suavizada, signos, final, sentido, género, España, regional, nombre, tú/usted, errata.
No ejecutes programas que escriban en otros archivos; no toques nada más que tu archivo de salida.
