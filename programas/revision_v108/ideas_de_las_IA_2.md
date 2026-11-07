# Ideas acumuladas (pregunta en cadena, 07-11-2026 01:37)

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
18. **Error de escala numérica larga/corta en sumas de dinero (Billion vs. Mil millones / Trillion vs. Billón)** (gemini:gemini-3.7-flash, prioridad alta)
   - Por qué: En la trama de conspiraciones del Clan Tojo y las deudas de Shinada se manejan cifras astronómicas de yenes. En inglés 'billion' equivale a mil millones y 'trillion' a un billón. Si se traduce literalmente como 'billón', se multiplica la cifra por mil, rompiendo la coherencia del guion y los datos financieros mostrados en gráficos o cinemáticas.
   - Cómo detectarlo: Ejecutar regex en el corpus inglés buscando `\b(\d+|one|two|three|ten|hundred)?\s*(billion|trillion)\b` y comprobar que en la línea en español correspondiente aparezca 'mil millones' o 'billón' según la regla de escala larga del español, alertando si aparece 'billón' para traducir 'billion'.
19. **Desajuste de términos entre las calidades de botín/pieles de la Caza de Saejima y las condiciones de entrega** (gemini:gemini-3.7-flash, prioridad alta)
   - Por qué: En las misiones de cazador de Hokkaido, los contratistas piden calidades específicas de pieles y carne (ej. 'Pristine Pelt', 'Good Meat', 'Damaged Hide'). Si la traducción de los estados de conservación del ítem no es 100 % idéntica entre el diálogo de la misión, el inventario y el menú de venta del comerciante, el jugador no sabrá qué entregar o venderá por error objetos clave.
   - Cómo detectarlo: Filtrar todos los ítems de inventario con origen en el minijuego de caza (`hunting_*.msg`) y extraer sus modificadores de calidad. Cruzar esos nombres con las cadenas de objetivos de misión del contratista y verificar coincidencia exacta de strings.
20. **Confusión mecánica entre 'Heat Action' estándar y 'Climax Heat'** (gemini:gemini-3.7-flash, prioridad alta)
   - Por qué: Yakuza 5 introdujo la barra y mecánicas exclusivas de 'Climax Heat' (que se activa con una entrada de control distinta y consume una barra roja especial). Si en las pantallas de tutorial, contratos de maestros (como Komaki o Sosuke) o descripciones de equipo se traduce indistintamente como 'Acción de calor' o 'Furia', el jugador no sabrá qué comando ejecutar para superar los desafíos.
   - Cómo detectarlo: Buscar en el texto inglés `\bClimax Heat\b` frente a `\bHeat Action\b` / `\bHeat Gauge\b`. Verificar que en español exista un término diferenciado e inmutable para cada concepto (ej. 'Calor Clímax' vs. 'Acción de Calor') y que no haya contaminaciones cruzadas.
21. **Límite visual y desbordamiento en opciones con temporizador del Minijuego de Taxi de Kiryu** (gemini:gemini-3.7-flash, prioridad alta)
   - Por qué: Durante los trayectos de taxi, los clientes formulan preguntas con cuenta regresiva donde las 3 opciones de respuesta aparecen en cajas flotantes estrechas sobre el parabrisas. A diferencia de los diálogos normales, estas cajas no admiten más de una línea ni hacen wrap; si el texto es unos píxeles más largo, invade el HUD del tacómetro o se trunca sin elipsis.
   - Cómo detectarlo: Aislar los archivos de diálogo de taxi (`taxi_*.msg` o etiquetas de branching de pasajeros). Calcular la longitud en caracteres de cada opción de respuesta y comprobar que ninguna supere el ancho máximo del botón gráfico (aprox. 28-32 caracteres en fuente latina del juego).
22. **Discrepancia entre nombres de efectos de comida en restaurantes y parámetros del árbol de habilidades** (gemini:gemini-3.7-flash, prioridad media)
   - Por qué: Cada plato consumido en restaurantes otorga bonificaciones temporales o puntos a atributos (Ataque, Defensa, Evasión, Tasa de Calor, Salud). Si el nombre del atributo que dice aumentar la descripción del menú no calca el nombre exacto de la estadística en el menú de pausa y subida de nivel, el jugador malgasta dinero creyendo mejorar un atributo diferente.
   - Cómo detectarlo: Extraer los modificadores de estadísticas en las descripciones de las cartas de restaurantes (`restaurant_*.msg`) y compararlos contra la lista cerrada de nombres de parámetros del menú de personaje (`status_*.msg`). Generar reporte de discrepancias.
23. **Calco de dialecto campirano estadounidense (Southern/Hillbilly) para simular el dialecto de Kansai y Nagoya** (gemini:gemini-3.7-flash, prioridad media)
   - Por qué: La localización en inglés de Sega suele adaptar el dialecto japonés de Kansai (Osaka) o Nagoya traduciéndolo con jerga rural del sur de EE. UU. (ej. 'y'all', 'ain't', 'reckon', 'howdy', 'partner'). Si se traduce literalmente al español, los personajes urbanos de Sotenbori o Kineicho suenan como vaqueros de película del oeste ('forastero', 'socio', 'ajá'), rompiendo la inmersión neutra.
   - Cómo detectarlo: Buscar en el texto inglés patrones dialectales (`ain't`, `reckon`, `howdy`, `y'all`, `folks`) y revisar manualmente las líneas en español asociadas para cerciorarse de que se adaptaron con un registro coloquial urbano desenfadado y no con clichés de 'western'.
24. **Inconsistencias alfanuméricas entre pistas de Llaves de Taquilla (Coin Lockers) y mapa** (gemini:gemini-3.7-flash, prioridad media)
   - Por qué: En Kamurocho y Sotenbori hay 100 taquillas repartidas en matrices con cuadrícula (ej. A-1 a J-5). Existen conversaciones de transeúntes y pistas en objetos que indican dónde hallar una llave específica. Si en el diálogo se tradujo erróneamente la coordenada o se invirtió la letra y el número respecto al ítem inventariable, el jugador buscará en la taquilla equivocada.
   - Cómo detectarlo: Grep mediante regex `[A-J]-\d` tanto en el texto fuente como en el traducido. Validar que cada código de taquilla presente en el diálogo en inglés coincida exactamente en el texto en español.
25. **Truncamiento de pistas en el Diario de Subhistorias por límite de renglones fijos sin scroll** (gemini:gemini-3.7-flash, prioridad baja)
   - Por qué: El panel de detalles del cuaderno de misiones (Pause > Substories) muestra un resumen del progreso con un número estricto de renglones visibles según la interfaz de cada protagonista. Si el texto en español requiere un salto de línea adicional frente al inglés, la última oración queda debajo del marco del recuadro sin posibilidad de desplazar la barra.
   - Cómo detectarlo: Filtrar las entradas del registro de misiones (`substory_memo_*.msg`). Simular el ajuste de línea con el ancho de caja fijado para la UI de memoria de subhistorias y alertar toda entrada cuya altura total supere el límite de renglones permitido por el marco de la UI.
26. **Discrepancia de nombres de bebidas y platillos entre el diálogo de la anfitriona y el menú de pedidos del Hostess Club** (gemini:gemini-3.5-flash, prioridad alta)
   - Por qué: Durante las citas en los clubes de anfitrionas (Kaguya, Honoka, Rikako, Hinata, Kaguya), la chica pide verbalmente una bebida o platillo específico. Si en el diálogo se traduce libremente (ej. «Champán Dorado») pero la opción en el menú desplegable de pedidos tiene otro nombre (ej. «Champagne Gold» o «Champán de Oro»), el jugador elegirá el ítem equivocado y perderá puntos de afecto.
   - Cómo detectarlo: Extraer con regex las menciones a bebidas/comidas en los archivos `hostess_talk_*.msg` y cruzarlas de forma automatizada contra la lista estricta de nombres de objetos en `hostess_menu.msg` para exigir coincidencia exacta.
27. **Descalce en nombres de rivales y calles entre las pistas del menú de Victory Road y los diálogos de los NPC en el mapa** (gemini:gemini-3.5-flash, prioridad alta)
   - Por qué: Para clasificar al torneo Victory Road en las 5 ciudades, el jugador debe buscar luchadores callejeros específicos guiándose por las pistas de la app del teléfono. Si el menú indica «Derrota a El Devorador en Calle Gion» pero el NPC sobre el mapa aparece como «El Traga-hombres» o está en «Calle Gion Oeste», el jugador no podrá identificar al objetivo para iniciar la pelea.
   - Cómo detectarlo: Script en Python que extraiga el listado de nombres de rivales y zonas desde `victory_road_menu.msg` y busque su coincidencia exacta en los archivos de diálogos de encuentro en mapa (`vr_encounter_*.msg`).
28. **Inconsistencia entre títulos de canciones del minijuego de Haruka y las opciones de respuesta en sus entrevistas de TV** (gemini:gemini-3.5-flash, prioridad media)
   - Por qué: En la sección de Idol de Haruka, aparece en concursos y programas de televisión de Osaka donde le hacen preguntas de trivia sobre sus canciones y trayectoria. Si la opción de respuesta traduce el título o letra de una canción diferente a como aparece en la lista del minijuego de baile/karaoke, el jugador elegirá una respuesta incorrecta a pesar de saber la lección.
   - Cómo detectarlo: Hacer grep de las opciones de respuesta en `haruka_tv_quiz_*.msg` y verificar que los nombres de canciones citados coincidan letra por letra con `idol_song_list.msg`.
29. **Descalce entre las instrucciones tácticas de pitcheo del entrenador Igarashi y las etiquetas del HUD de bateo de Shinada** (gemini:gemini-3.5-flash, prioridad media)
   - Por qué: En la subhistoria y entrenamiento de béisbol de Shinada en Kineicho, el entrenador exige batear tipos de lanzamientos específicos (Fork, Sinker, Shoot, Curve). Si el diálogo de instrucción traduce «Forkball» como «Bola de tenedor» pero el indicador visual (HUD) en pantalla durante el pitcheo muestra «Bola Fork», el jugador dudará sobre qué bola debe golpear.
   - Cómo detectarlo: Comparar la lista cerrada de términos de lanzamientos en `baseball_hud.msg` con el texto instructivo de las misiones en `baseball_training_*.msg` para garantizar coincidencia terminológica.
