# Ideas acumuladas (pregunta en cadena, 06-11-2026 20:42)

1. **Homónimos traducidos sin contexto (bank, charge, right, set, match)** (kilo:kilo/kilo-auto/free, prioridad alta)
   - Por qué: Palabras inglesas polisémicas cambian de sentido según la escena; un jugador nota cuando un menú dice 'banco' en vez de 'orilla' o 'carga' en vez de 'tiro'
   - Cómo detectarlo: Filtrar strings con una sola palabra inglesa común y cruzar con el archivo de contexto/escena; revisión manual por grupos de contexto
2. **Orden de variables %s/%d distinto al inglés por gramática española** (kilo:kilo/kilo-auto/free, prioridad alta)
   - Por qué: Frases como 'You defeated %d enemies' requieren '%d enemigos derrotados' o reordenar; dejar el orden inglés suena antinatural
   - Cómo detectarlo: Grep de líneas con %s/%d y comparar posición con el inglés; programa que detecta mismatches de orden de placeholders
3. **Plurales dinámicos con contador (%d objeto(s))** (kilo:kilo/kilo-auto/free, prioridad alta)
   - Por qué: Textos como '1 item(s) found' quedan mal; en español hay que usar forma plural o reescribir
   - Cómo detectarlo: Buscar '(s)' o 'item(s)' y strings con %d seguido de sustantivo singular; revisar todos los contadores
4. **Consistencia de botones de interfaz (Aceptar/Cancelar/Volver/OK) en todos los menús** (kilo:kilo/kilo-auto/free, prioridad media)
   - Por qué: Un jugador nota si un menú dice 'OK' y otro 'Aceptar', o 'Back' sin traducir
   - Cómo detectarlo: Extraer valores únicos de botones y comparar contra glosario; listar variantes por columna
5. **Logros/trofeos y sus descripciones coherentes con la acción real** (kilo:kilo/kilo-auto/free, prioridad media)
   - Por qué: Los logros de Steam se leen fuera del juego; una descripción que no coincide con lo que se hace confunde
   - Cómo detectarlo: Cruzar nombres de logros con textos de tutorial y verificar que el verbo y el objeto coincidan
6. **Romanización y orden de nombres japoneses (apellido primero vs nombre primero)** (kilo:kilo/kilo-auto/free, prioridad media)
   - Por qué: Yakuza mezcla nombres japoneses e ingleses; inconsistencia rompe inmersión
   - Cómo detectarlo: Lista de personajes fijos y búsqueda de variantes; comprobar que siempre se use la forma elegida
7. **Prompts de botones de mando según plataforma (Xbox A/B vs PS ○/×)** (kilo:kilo/kilo-auto/free, prioridad media)
   - Por qué: En PC/Steam los prompts deben coincidir con el control configurado; textos como 'Press X' pueden ser incorrectos
   - Cómo detectarlo: Buscar 'Press', 'pulsa', 'botón' y verificar iconos/teclas en archivos de input
8. **Términos de mahjong, shogi, dardos, béisbol y karaoke** (kilo:kilo/kilo-auto/free, prioridad media)
   - Por qué: Minijuegos técnicos tienen jerga propia; una traducción literal suena mal a quien los juega
   - Cómo detectarlo: Filtrar strings por minijuego y revisar con glosarios específicos; probar cada minijuego
9. **Mojibake o caracteres mal codificados (fullwidth, katakana residual)** (kilo:kilo/kilo-auto/free, prioridad alta)
   - Por qué: Aparecen símbolos extraños o letras japonesas sueltas en textos en español
   - Cómo detectarlo: Grep de rangos Unicode fuera de Latin-1 y caracteres de ancho completo en strings españoles
10. **Ordenación alfabética de listas e inventarios con acentos** (kilo:kilo/kilo-auto/free, prioridad baja)
   - Por qué: Si el juego ordena por código, 'Árbol' queda al final; el jugador busca y no encuentra
   - Cómo detectarlo: Revisar menús de inventario/objetos y comprobar que el orden siga reglas del español (RAE)
11. **Formalidad de correos electrónicos vs diálogo hablado** (kilo:kilo/kilo-auto/free, prioridad baja)
   - Por qué: Los emails del juego suelen ser más formales; mezclar tú/usted dentro del mismo correo rompe coherencia
   - Cómo detectarlo: Filtrar strings de mail y verificar registro consistente dentro de cada mensaje
12. **Ritmo y densidad silábica de los subtítulos** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad alta)
   - Por qué: El español suele ser más melodioso y tener mayor densidad silábica que el inglés. Un texto traducido que mantiene la longitud del inglés puede parecer lento o pesado, obligando al jugador a leer más rápido de lo normal para no perder el ritmo de la historia. Un ritmo irregular arruina la inmersión en Yakuza 5, donde el diálogo es constante.
   - Cómo detectarlo: Programa que calcule la densidad silábica (leísmo) y caracteres por segundo de reproducción versus el inglés. Si el texto español supera los 20 caracteres/segundo o si la densidad silábica hace que la lectura sea forzada o pausada en exceso, hay problema. Revisión manual contando tiempos de lectura en el juego.
13. **Consistencia terminológica en mecánicas y UI (drift)** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad alta)
   - Por qué: En Yakuza 5, 'salud' se usa para el health bar, pero en alguna misión o diálogo el traductor podría usar 'vida' o 'vitalidad' por error. Esto confunde al jugador sobre qué barra es qué, rompiendo la coherencia del juego y la comprensión del estado del personaje.
   - Cómo detectarlo: Crear un diccionario de términos centrales (salud, dinero, armas, etc.) extraído del inglés. Usar un script (Grep/Python) para escanear los 88.000 textos y flaggear cualquier variante (salud/vida/vitalidad) que no coincida con la lista blanca definida por el glosario oficial.
14. **Manejo de sufijos de cortesía y honoríficos japoneses** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad media)
   - Por qué: Los personajes de Yakuza usan sufijos como -kun, -san, -senpai. En español, traducir 'Kiryu-kun' a 'Kiryu' pierde la cercanía, pero usar 'Kiryu señor' inconsistente en toda la saga rompe la voz del personaje. El jugador notará la falta de personalidad en los diálogos.
   - Cómo detectarlo: Extracción regex de sufijos japoneses en el texto fuente. Comparar con la tabla de traducción asignada (ej. -kun -> diminutivo/tú, -san -> señor/-a). Script que verifique que cada sufijo se tradujo de forma uniforme a lo largo de todas las escenas y personajes.
15. **Equivalencia cultural e idiomática (evitar traducción literal)** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad media)
   - Por qué: Los refranes o chistes japoneses suenan bien en inglés pero mal si se traducen al español de forma directa. Un jugador nativo de español notará que el chiste se ha perdido o sonaba forzado, alterando el tono cómico o melancólico que define a Yakuza 5.
   - Cómo detectarlo: Revisión manual por grupos de contexto, enfocándose en refranes, metáforas y chistes. Buscar frases que suenen como traducción alfabética ('traducir palabra por palabra') en lugar de adaptación cultural que preserve el humor o la esencia del original.
16. **Falsos amigos y cognados** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad media)
   - Por qué: Palabras que se parecen al inglés pero cambian el significado (ej. 'actual' = actualmente vs real; 'library' = biblioteca vs librería; 'disappointed' = decepcionado vs desilusionado). El jugador leerá y pensará otra cosa, generando confusión en el gameplay o en el desarrollo de la trama.
   - Cómo detectarlo: Grep de palabras clave comunes en español que derivan de inglés (ej. 'actual', 'library', 'disappointed', 'sympathy'). Cruzarlas con el contexto de la scène para verificar que el significado coincide con el inglés oficial y no ha sido distorsionado por un false friend.
17. **Alineación visual de texto dinámico en la interfaz** (or:xingchen-agi/xing4.0-29b-a4b:free, prioridad baja)
   - Por qué: Si un texto dinámico (como el nombre de un NPC o la puntuación de un minijuego) aparece en la cuadro de subtítulo, la longitud del texto español puede desbordar la caja o alinear mal comparado con el inglés, rompiendo la estética del juego y causando cortes en la pantalla.
   - Cómo detectarlo: Comparar el ancho de los caracteres (usando métricas de fuentes tipográficas) entre el texto en inglés y el español para las variables dinámicas. Si el español es más ancho y no se reduce el tamaño de fuente o se ajusta el layout, habrá desbordamiento visual.
