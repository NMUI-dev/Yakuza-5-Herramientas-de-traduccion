# Revisión tú/usted por conversación (Yakuza 5, español de México/Latinoamérica)

Archivo de entrada: mezcla_N.txt. Cada bloque `### archivo` es un trozo SEGUIDO de una escena del juego, en orden.
Cada línea: `ID [voz] inglés || español`. `[Prota]` = el protagonista que manejas (Kiryu, Saejima, Akiyama, Haruka o Shinada,
según la parte del juego); `[Otro]` = cualquier otro personaje (OJO: varias personas distintas pueden ser «Otro» en un mismo bloque);
`[]` = desconocido. « / » = salto de línea dentro de la frase. Las marcadas con `>>` son las sospechosas.

REGLA DEL USUARIO: antes de tocar una frase, entiende TODA la conversación: quién habla, a quién, qué relación tienen.

Problema a arreglar: la MISMA persona hablando a la MISMA persona en la MISMA conversación cambia entre tú y usted sin motivo.
Cómo decidir el trato correcto:
- Dependientes, recepcionistas, camareros, crupieres, personal de tiendas/casinos/coliseo, taxistas en servicio, desconocidos
  educados («Excuse me, sir», «ma'am») -> USTED con el cliente, en TODAS sus frases (también «Vuelva pronto», «Si gana...»).
- Akiyama, Shinada y Haruka con desconocidos educados o mayores (presidentes, clientes) -> se mantiene el que más use en la escena.
- Kiryu y Saejima con desconocidos: suelen tutear (son bruscos); si en esa conversación usan usted, que sea siempre usted.
- Amigos, familia, yakuza entre ellos, jefes a subordinados, niños -> TÚ.
- El trato puede cambiar SOLO si el inglés lo justifica (p. ej. pasa a llamarle «son», «kid», se hacen amigos).
- «ustedes» (plural) es correcto siempre (español latino): no se toca.
- Al cambiar el trato, ajusta TODO lo que concuerde: verbos (quieres->quiere, ven->venga, mira->mire), pronombres (te->le/lo/la,
  tu->su, ti->usted, contigo->con usted), imperativos y posesivos. Mantén género correcto (lo/la según a quién se habla).
- Si en el camino ves un ERROR DE SENTIDO (el español no dice lo que dice el inglés, p. ej. «Please come again» = «Vuelva pronto»,
  no «Vuelve a intentarlo») o de GÉNERO, corrígelo también y dilo en el motivo.
- No cambies nada más: ni estilo, ni palabras que estén bien. Conserva EXACTAMENTE etiquetas <Color:8>...<Color:Default>, <Italic>,
  {…}, ⑬, ⑮, signos ¡! ¿?, y el mismo número de « / » (saltos de línea) en el mismo sitio aproximado.
- Una ID puede repetirse en varios bloques (frase compartida): decide una sola versión que valga en todos sus usos; si en algún
  uso no encaja, NO la cambies y anótalo en «dudas».
- No inventes: si no está claro a quién se habla, no toques.

Salida: escribe `cambios_N.json` en esta misma carpeta (UTF-8), así:
{"cambios": [{"id": "19508", "es": "texto nuevo completo", "motivo": "usted: dependiente a cliente, coherente con la escena"}],
 "dudas": [{"id": "...", "nota": "..."}]}
Solo las líneas que de verdad cambian. Al terminar, responde con cuántos cambios y dudas hay (no copies el JSON en la respuesta).
