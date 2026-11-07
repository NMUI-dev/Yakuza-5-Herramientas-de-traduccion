# Guía para traducir Yakuza 5 Remastered

Todo lo que necesitas para corregir nuestra traducción, pasarla a otro idioma o traducir otro Yakuza. Los comandos y las
cifras de esta guía se probaron el 03-11-2026 con la traducción v1.0.4 (de la v1.0.5 a la v1.0.8 solo cambian textos y 7 imágenes).

**Probado solo en:** Yakuza 5 Remastered de Steam (appid 1105510, build 6407471), con el juego en inglés, en Windows 11.

## Índice

1. [Elige tu camino](#1-elige-tu-camino)
2. [Cuánto hay que traducir](#2-cuánto-hay-que-traducir)
3. [Preparar todo](#3-preparar-todo)
4. [Camino 1: traducir los textos](#4-camino-1-traducir-los-textos)
5. [Camino 2: traducir las imágenes](#5-camino-2-traducir-las-imágenes)
6. [Camino 3: traducir otro Yakuza o empezar de cero](#6-camino-3-traducir-otro-yakuza-o-empezar-de-cero)
7. [Dónde guarda el texto el juego](#7-dónde-guarda-el-texto-el-juego)
8. [Todos los errores que tuvimos](#8-todos-los-errores-que-tuvimos)
9. [Decisiones de traducción](#9-decisiones-de-traducción)
10. [Antes de publicar](#10-antes-de-publicar)
11. [Si algo falla](#11-si-algo-falla)

## 1. Elige tu camino

| Quiero... | Camino | Necesitas |
|---|---|---|
| Corregir frases o pasar los textos a otro idioma | [1](#4-camino-1-traducir-los-textos) | Python y una hoja de cálculo |
| Cambiar palabras dibujadas en menús, carteles o capítulos | [2](#5-camino-2-traducir-las-imágenes) | Lo anterior y un editor de imágenes |
| Traducir otro Yakuza o rehacer todo desde el código | [3](#6-camino-3-traducir-otro-yakuza-o-empezar-de-cero) | Lo anterior y programar en Python |

## 2. Cuánto hay que traducir

Cifras medidas con `programas/contar_datos.py`, no estimadas.

### Textos

| Dónde sale | Textos distintos | Veces que aparecen | Letras en inglés |
|---|--:|--:|--:|
| `msg`: diálogos | 45.049 | 70.021 | 2.974.463 |
| `tabla`: objetos, misiones, habilidades | 7.007 | 11.866 | 407.248 |
| `ptr`: menús, correos, tiendas (`.bin` con punteros) | 6.123 | 27.021 | 178.636 |
| `sub`: subtítulos de escenas | 3.602 | 6.024 | 125.640 |
| `extra-sub`: subtítulos de dos renglones | 1.539 | 1.624 | 98.236 |
| `extra-nom`: quien habla, opciones, preguntas del concurso | 4.057 | 7.191 | 80.270 |
| `extra-rep`: carteles de zona, objetos, enemigos | 2.769 | 3.046 | 48.738 |
| `pac`: frases de acompañantes dentro de los guiones | 1.284 | 27.693 | 29.880 |
| `devil`: mensajes del sistema | 418 | 454 | 7.791 |
| **Total** | **71.848** | **154.940** | **3.950.902** |

- 1.941 textos son iguales al inglés a propósito: nombres, marcas y términos.
- Se dividieron en 372 lotes con 74.373 entradas. Un mismo texto puede estar en más de un lote, por eso la cifra es mayor
  que los 71.848 de la hoja.

### Imágenes

| | Cantidad |
|---|--:|
| Imágenes `.dds` en los archivos que toca la traducción | 4.800 |
| Imágenes cambiadas | 1.213 |

Las que más cambian:

| Archivo | Cambiadas | Total | Qué lleva |
|---|--:|--:|---|
| `pausepar/pause_en.par` | 747 | 3.200 | Pausa, reglas, capítulos, objetos, tarjetas de habilidad |
| `minigame_en/karaoke_e.par` | 199 | 218 | Letras del karaoke |
| `2dpar/ui_en.par` | 189 | 587 | Menús, celular, minijuegos |
| `2dpar/sprite_en.par` | 30 | 158 | Avisos de acción |
| `pausepar/tougijyo_en.par` | 19 | 34 | Coliseo |

### Archivos y vídeos

| | Cantidad |
|---|--:|
| Archivos del juego que cambia la traducción | 35 |
| Archivos dentro de ellos, ya desempaquetados | 11.312 |
| De esos, cambiados | 4.671 |
| Instalación completa de `main/data` | 8.077 archivos, 31,3 GiB |
| Vídeos `.usm` en `data/mvstm` | 89 archivos, 6,6 GiB |

Los vídeos no se tocan. Lo dibujado dentro se queda en inglés; sus subtítulos sí se traducen.

### Cuánto nos costó

- **Traducción automática:** 326 lotes en unas 19 horas (20 y 21-10-2026), con 3 traductores gratuitos en paralelo.
- **Imágenes:** fue lo más largo. Tras la primera versión, una revisión a ojo de 905 imágenes encontró 234 malas.
- **Versiones:** salieron ocho correcciones (v1.0.1 a v1.0.8) por cosas que se escaparon; la v1.0.5 (589 frases: género, inglés metido, faltas, una tanda corrida una fila) está en programas/revision_v105/LEEME.md y la v1.0.6 (1.153 frases revisadas por escenas: tú/usted, sentido, nombres iguales en menú y diálogos, signos) en programas/revision_v106/LEEME.md; la v1.0.7 (2.010 textos: groserías suavizadas, renglones partidos por sentido, signos, finales de correo que quedaban en inglés) en programas/revision_v107/LEEME.md; la v1.0.8 (velocidad de lectura de subtítulos y un término, una traducción) en programas/revision_v108/LEEME.md. La sección 8 explica cada una.

## 3. Preparar todo

### Lo que necesitas

- Windows 10 u 11.
- Yakuza 5 Remastered de Steam, con el idioma del juego en inglés.
- [Python 3](https://www.python.org). Al instalarlo, marca **Add python.exe to PATH**.
- Excel, LibreOffice Calc o un editor de texto.
- Unos 2 GB libres.

`ParTool.exe` y `texconv.exe` ya vienen en `programas/`.

### Instalación

1. Descarga el zip de la [última versión de la traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish/releases/latest)
   y descomprímelo.
2. Descarga este repositorio con **Code > Download ZIP** o desde Releases.
3. Descomprímelo **dentro** de la carpeta de la traducción. Debe quedar así:

   ```text
   Yakuza 5 - Traduccion al espanol v1.0.8\
       archivos\                        lo que se instala en el juego
       INSTALAR o QUITAR.bat
       Yakuza-5-Herramientas-de-traduccion-main\
           EXTRAER textos.bat
           APLICAR textos.bat
           programas\
           datos\
   ```

La carpeta tiene que estar ahí porque el programa busca `..\archivos` y `..\respaldo_original`.

### El inglés original

El programa necesita los archivos originales. Los busca en este orden:

1. La carpeta que le indiques con `--ingles "<carpeta>"`.
2. `..\respaldo_original`, que crea el instalador al instalar la traducción.
3. El juego de Steam, si no tiene la traducción puesta.

Si el juego tiene la traducción y no hay respaldo, el programa se niega a seguir. Quita la traducción con
`INSTALAR o QUITAR.bat`, opción 2, o usa en Steam **Propiedades > Archivos instalados > Verificar integridad**.

## 4. Camino 1: traducir los textos

1. **Saca los textos.** Doble clic en `EXTRAER textos.bat`. Tarda unos minutos y crea `trabajo\textos.csv`.
   Debe terminar con `Español rellenado: 71848 (sin traducción: 0)`.

2. **Edita la hoja.** Abre `trabajo\textos.csv`. Usa `;` como separador y está en UTF-8. Si Excel lo muestra todo en una
   columna, ábrelo con **Datos > Desde texto/CSV** y elige UTF-8 y punto y coma.

   | Columna | Qué es | ¿Se cambia? |
   |---|---|---|
   | `id` | Número de fila | No |
   | `donde` | De dónde sale el texto | No, sirve de contexto |
   | `veces` | En cuántos sitios aparece; se cambia en todos a la vez | No |
   | `ingles` | Original; el programa lo usa para encontrar el texto | **Nunca** |
   | `espanol` | La traducción | **Sí** |

   Si vacías una celda de `espanol`, ese texto queda en inglés.

3. **Guarda** con el mismo nombre, en formato **CSV UTF-8**.

4. **Mete los textos.** Doble clic en `APLICAR textos.bat`. Deja el resultado en `salida\data` y lo copia encima de
   `..\archivos\data`.

5. **Pruébalo.** Cierra el juego, abre `INSTALAR o QUITAR.bat` y elige la opción 1. Si ya tenías una versión instalada,
   quítala antes con la opción 2. Si instalas encima, el respaldo guarda la versión vieja en lugar de los originales.

> **Las pruebas en Steam suman horas y pueden dar logros.** Si no quieres eso, usa una copia del juego, pero lee antes
> el error de las uniones en la [sección 8](#proceso-y-herramientas).

### Reglas al escribir

- **Respeta las marcas:** `<Color...>`, `<Action...>`, `<Sign...>`, `{player_name}`, `${...}` y los saltos de línea.
- **Preguntas del concurso:** `(改行)` es un salto de renglón. Deja el mismo número, con 46 letras como mucho por renglón.
- **Escribe normal `¡`, `í` e `Í`.** El programa las cambia solo a las casillas `½`, `` ` `` y `|` de la letra del juego.
  Por eso esos tres símbolos no se pueden usar como texto.
- **Signos partidos:** si una frase está cortada en trozos, el `¿` o `¡` va en el trozo donde empieza la frase.
- **Otros idiomas:** la letra del juego es una rejilla Latin-1 de 16x32. Otros alfabetos obligan a rehacer la letra, y eso
  no lo hemos probado.
- **Letras nuevas:** si dibujas una letra en la casilla de otra, hereda su ancho. Pruébala en una frase dentro del juego.

## 5. Camino 2: traducir las imágenes

Las palabras dibujadas no están en la hoja. Las imágenes son `.dds` dentro de archivos `.par`, y a veces hay un `.par`
dentro de otro.

Abre una consola en la carpeta de las herramientas y sigue estos pasos.

**1. Saca el `.par` y copia su formato:**

```bat
mkdir png nuevo
programas\ParTool\ParTool.exe extract "<juego>\auth_telop\auth_telop_en.par" tel
python programas\dds_formato.py tel\2d30.dds
```

`<juego>` es la carpeta con los originales: `..\respaldo_original` o el `main\data` de Steam sin la traducción.

`dds_formato.py` dice el tamaño, los mipmaps, la compresión y la orden exacta para guardar la imagen. Ejemplo:

```text
2d30.dds: 1024x128, 1 mipmaps, BC3_UNORM
```

**2. Pásala a PNG:**

```bat
programas\texconv\texconv.exe -nologo -y -ft png -m 1 -o png tel\2d30.dds
```

**3. Edita `png\2d30.png`** sin cambiar su tamaño.

**4. Vuelve a `.dds` con el mismo formato:**

```bat
programas\texconv\texconv.exe -nologo -y -f BC3_UNORM -m 1 -o nuevo png\2d30.png
```

**5. Métela en el `.par`.** La carpeta `nuevo` lleva solo lo que cambia, con la misma ruta y las mismas mayúsculas:

```bat
programas\ParTool\ParTool.exe add "<juego>\auth_telop\auth_telop_en.par" nuevo auth_telop_en.par
```

**6. Compruébalo:** extrae el `.par` nuevo y compara. Solo debe cambiar tu imagen.

### Un `.par` dentro de otro

Se rearman **de dentro hacia fuera**. Ejemplo con `2dpar\ui_en.par`, que contiene `surfboard\pjd_titlemenu.par`:

```bat
programas\ParTool\ParTool.exe extract "<juego>\2dpar\ui_en.par" ui
programas\ParTool\ParTool.exe extract ui\surfboard\pjd_titlemenu.par tm

mkdir add2\Texlist_0001 add3\surfboard
rem copia la imagen nueva a add2\Texlist_0001\<nombre>.dds
programas\ParTool\ParTool.exe add ui\surfboard\pjd_titlemenu.par add2 add3\surfboard\pjd_titlemenu.par
programas\ParTool\ParTool.exe add "<juego>\2dpar\ui_en.par" add3 ui_en.par
```

`Texlist_0001` tiene que ir exactamente así, con mayúscula: es uno de los errores de la [sección 8](#imágenes).

Para sacar todo de una vez, usa `ParTool extract -r`.

### Para instalar tu imagen

Copia el `.par` nuevo a `..\archivos\data\<su ruta>` y usa el instalador. Si editas textos e imágenes, **aplica primero los
textos**. Para los archivos que llevan las dos cosas, como `pausepar\pause_en.par`, el programa de textos parte de
`..\archivos\data`, así que conserva tus imágenes.

### Consejos

- **Rehaz desde el ORIGINAL**, nunca encima de una versión traducida.
- **Letra normal sobre fondo:** borra el inglés y escribe encima con la misma letra, tamaño y color.
- **Una línea sobre fondo transparente** (rótulos, karaoke): rehaz la textura entera. Borrar a trozos deja restos.
- **Borra también el color**, no solo el alfa. Si no, el blanco viejo asoma bajo el halo y se lee el inglés.
- **Letra estilizada** (pincel, brillo, pegatinas): hazla a mano con una letra parecida.
- **Atlas de menús:** son palabras pegadas que el juego recorta. Los rectángulos exactos están en el `.sbb` del mismo `.par`.
- **Piezas combinadas** («GOOD» + «CHOICE»): tienen un hueco fijo. A veces es mejor no traducirlas.
- **Mira cada imagen a ojo**, en hojas de «original | traducción» y con una segunda revisión.

Nuestro kit de imágenes está en el [repositorio de la traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish):
`herramientas/atlas_*.py`, `paginas_*.py`, `imagenes_*.py` y `trabajo/imagenes/GUIA_ATLAS.md`.

## 6. Camino 3: traducir otro Yakuza o empezar de cero

El método que nos funcionó, en orden:

1. **Haz una copia de prueba** y confirma que un cambio llega al juego. Cambia un subtítulo antes de programar nada más.
2. **Busca todo el texto:** escanea todos los archivos del juego en busca de inglés (`escanear_ingles.py`).
3. **Descifra cada formato** y escribe un lector y un escritor. Comprueba que, sin cambios, el archivo sale igual byte a byte.
4. **Prueba con una marca:** pon `ñ-` delante de todos los textos (`aplicar.py --prueba`). Lo que salga sin marca en el juego
   viene de otro sitio.
5. **Divide en lotes** de unas 12.000 letras (`preparar_lotes.py`), con guía de estilo, glosario y validador (`validar_lote.py`).
6. **Traduce por lotes.** Nosotros usamos modelos gratuitos (`traductor_gemini.py`) y revisamos después (`buscar_fallos.py`,
   `corregir_fallos.py`). Vigila que sigan trabajando: los nuestros estuvieron parados casi dos horas sin avisar.
7. **Arregla la letra:** prueba cada letra con tilde en una frase real.
8. **Pasa OCR a TODAS las imágenes en inglés**, no solo a las que parecen distintas.
9. **Compara con el original** y haz un barrido de lo armado ([sección 10](#10-antes-de-publicar)).

Todo el código está en el [repositorio de la traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish),
con [COMPILAR.md](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish/blob/main/COMPILAR.md) para rehacerla.
El diario de cada paso está en [HISTORIAL_DEL_TRABAJO.txt](HISTORIAL_DEL_TRABAJO.txt). Para Yakuza 6, mira también sus
[lecciones](https://github.com/NMUI-dev/Yakuza-6-The-Song-of-Life-Espa-ol-Spanish/blob/main/LECCIONES_PARA_TRADUCTORES.md).

### Español oficial de la saga

Para ser coherente con la saga, saca los términos de los juegos con español latino oficial, solo leyendo:

| Juego | Dónde están los idiomas |
|---|---|
| Kiwami R, Yakuza 0 Director's Cut | `wdr_par_<letra>` (c = inglés, l = latino, s = España); tablas en `db.nex/en\|ls\|es` (Yakuza 0: `db.gld`) |
| Kiwami 2 R | `db.par/<idioma>/` (en, esl = latino, ese = España) |
| Kiwami 3 & Dark Ties | `db.bis.en.par`, `db.bis.esl.par` |

Like a Dragon, Infinite Wealth, Lost Judgment y Pirate Yakuza solo traen español de España. Sacamos 191.057 parejas
inglés-español con `glosario_saga.py`.

Algunos términos oficiales: «UFO catcher» es «máquina de regalos» y «Hostess/Host» es «Acompañante». Los modos de dardos
(«Cricket», «Count-Up») y las marcas se dejan en inglés. Lo oficial traduce «Heat» como «adrenalina», pero nosotros lo
dejamos como «Heat» a propósito ([sección 9](#9-decisiones-de-traducción)).

## 7. Dónde guarda el texto el juego

Los textos en inglés están en archivos con sufijo `_en`, dentro de `main\data`.

| Dónde | Qué hay | Formato |
|---|---|---|
| `wdr_par_en\wdr.par` (`.msg`, 5.214 archivos) | Diálogos y, al final, **tabla de nombres**: quien habla, opciones, preguntas del concurso | Big endian. Registro de 12 bytes: largo u16, n.º de funciones u8, 0, offset de texto u32, offset de funciones u32. Tabla de nombres: número u16 en `0x0E`, punteros en `0x10` |
| `wdr_par_en\common.par` | Tiendas | `.bin` con punteros |
| `auth\subtitle.par` | Subtítulos de escenas y vídeos | 207 CSV en UTF-16, con saltos de línea dentro de comillas |
| `db.devil\en\msg.bin` | Mensajes del sistema | ARMP v2, con puntero u32 little endian por cadena |
| `db.devil\en\msg_replacer.bin` | Carteles de zona, objetos, enemigos, comentarios de dardos | ARMP v2 |
| `bootpar\boot_en.par` | Objetos, habilidades, menús, misiones | Tablas con cabecera `20 07 03 19`, columnas con nombre |
| `pausepar\*_en.par`, `staypar\stay_en.par` | Menús, enemigos, premios | Tablas e imágenes |
| `scenario_en\mail.bin` | Correos | `.bin` con punteros absolutos big endian |
| Guiones `pac_*.bin` | Frases de acompañantes | Texto en línea, con **límite de bytes** |
| `minigame_en\` | Reglas y textos de minijuegos | Sueltos y `.par` |
| `fontpar\font_hd_en.par` | Letra del juego | Rejilla Latin-1 de 16x32 en `sd_hankaku.dds`, con **tabla de anchos fija** |
| `auth_telop\`, `2dpar\`, `pausepar\`, `minigame_en\karaoke_e.par` | Imágenes con texto | `.dds` (BC1, BC2, BC3, BC7), a veces en `.par` anidados |
| `data\mvstm\*.usm` | Texto dibujado dentro de los vídeos | Reeditar el vídeo; no lo hicimos |
| `Yakuza5.exe` | «PRESS ANY BUTTON» | No se toca, por riesgo con la protección de Steam |

**Cómo se mete un texto más largo:**

- `.msg`: el texto nuevo va al final del archivo y se recalculan las posiciones de pausas y colores, que cuentan letras
  visibles sin etiquetas.
- `.bin` con punteros: el texto nuevo va al final y se redirige el puntero. La cadena inglesa vieja sigue en el archivo,
  aunque ya no se use.
- Tablas: se reescriben completas.
- `.par`: se rearman con `ParTool add`.
- **Texto en Yakuza 6 (`cmn.bin`):** cada texto tiene un hueco fijo. Una tilde ocupa 2 bytes.

## 8. Todos los errores que tuvimos

### El juego se cierra

| Error | Causa | Qué hacer |
|---|---|---|
| Se cierra en el primer diálogo | La columna `CATEGORY` de `drive_parts.bin` («Wheel», «Default») es una clave interna y la traducimos | No traduzcas columnas internas: expresiones, IDs, nombres de animación (`COL_INTERNAS` en `aplicar.py`) |
| Se cierra al arrancar | Buscamos un puntero por su valor, y un dato de cabecera valía igual que la posición del texto «Po» | No toques lo que no cambia. Exige que el u32 de al lado también apunte a una cadena |
| No sabes qué texto lo rompe | Son miles de cambios | Parte la lista por la mitad: con 3.672 cadenas bastaron 12 arranques |
| `Yakuza5.exe` se cerraba incluso con los originales | No era la traducción: pasaba igual sin ella | Antes de culpar a tu trabajo, prueba con los archivos originales |

### Textos que se quedaron en inglés

| Error | Cuánto | Qué hacer |
|---|---|---|
| No leíamos la tabla de nombres de los `.msg` | Quien habla, opciones y preguntas del concurso; parte de los 8.492 textos de la v1.0.2 | Lee también el final de cada `.msg` |
| Subtítulos con salto de línea dentro de las comillas | Se partían en dos filas y no se traducían | Usa un lector CSV real, no línea a línea |
| Dimos por interno `msg_replacer.bin` | Tenía carteles de zona, objetos y enemigos | Mira el contenido antes de descartar un archivo |
| El filtro `isprintable()` tiraba frases con `\n` | Comentarios de los dardos | No filtres por eso |
| Un filtro de «¿es texto o código?» tiraba frases cortas | 2 frases en Y5 («I...», «I'm...»), que obligaron a la v1.0.4; 830 subtítulos en Y6 | Busca lo que siga igual al inglés con `^[.…]*[A-Z][a-z']+[.!?…]+$` |
| Textos iguales al inglés sin revisar | 1.453, entre ellos «Hard» | Decide uno a uno si es nombre propio |
| Buscamos el inglés en el original y no en lo armado | Quedaban restos | Haz el barrido sobre lo armado; en `.bin`, cuenta solo cadenas con puntero |
| Filtro de inglés demasiado amplio | Las claves internas (`Talk_Yes`, `adv1_020/...`) colaron 5.000 entradas | Descarta lo que no tiene espacios o es una ruta |

### Textos que salieron mal

| Error | Causa | Qué hacer |
|---|---|---|
| Etiquetas o espacios de más | Búsqueda «parecida» sin etiquetas ni espacios | Busca primero por la frase exacta |
| Signos de apertura mal puestos | En frases partidas, el corrector añadía `¿` o `¡` al trozo final | El signo va en el trozo donde empieza la frase; no toques los `?` y `!` de cierre |
| Inglés suelto dentro de una frase traducida | «... Even chicken or horse.» | Se puede cambiar en su sitio, con los mismos bytes |
| Tablas oficiales mal emparejadas: «Baseball» salía «Salero» | El orden de las cadenas cambia entre idiomas | Empareja por fila y columna con reARMP |
| Palabras de España y restos de inglés | Traducción automática | Pasa `buscar_fallos.py` y guarda un registro de cada corrección |

### La letra

| Error | Causa | Qué hacer |
|---|---|---|
| `¿` salía como `/` | La casilla del juego está mal | Redibújala: usamos el `?` del juego girado |
| `¡` corrida una casilla | Igual | Redibújala |
| Huecos: «paí s», «Í ñigo», «¡ Hola» | El juego usa una **tabla de anchos fija por casilla** | Dibuja la letra en una casilla estrecha casi sin uso: í en `` ` ``, Í en `\|`, ¡ en `½` |
| Primero creímos que medía por la tinta | Probamos varias casillas | Prueba cada letra nueva en una frase real, como «país, día, Íñigo, ¡Hola!» |

### Imágenes

| Error | Cuánto | Qué hacer |
|---|---|---|
| Carpeta interna con otra mayúscula: `Texlist_0001` | 55 imágenes seguían en inglés; ParTool la añadía aparte | Copia la ruta exacta y comprueba extrayendo el `.par` nuevo |
| El compresor DXT de Pillow estropeaba el texto fino | Fantasmas y letras rotas | Guarda con texconv y, fuera de lo editado, conserva los bloques originales |
| Buscar solo «texturas distintas de la versión japonesa» | Se saltó `auth_telop_en`; en Y6, 13 títulos de capítulo | Pasa OCR a TODAS las texturas en inglés |
| Filtrar por prefijo de nombre | El karaoke es `2d_jm_ok_*` **y** `2d_yk_ok_*`; se escapó «Kamurocho Lullaby» | Filtra por carpeta |
| Un filtro de basura tiraba textos con «LVE», «DART», «PART» | «THE WAY OF RESOLVE» no se dibujaba | Revisa lo que descartan tus filtros |
| El OCR parte las líneas | Quedaban restos del inglés | Rehaz la textura entera |
| Atlas de menús automáticos | 193 descartados: tamaños dispares, letras cortadas | Hazlos con los rectángulos del `.sbb` y la letra elegida a ojo |
| Una pasada automática pisó 4 imágenes hechas a mano | Hubo que rehacerlas | Lleva una lista de manuales y exclúyelas |
| Texto traducido que no cabe | 221 avisos; 145 textos acortados | Acorta el texto en lugar de encoger la letra |
| Sin revisión a ojo | 234 de 905 estaban mal | Revisión completa, y que cada uno mire lo del otro |
| Inicios de capítulo a medias | 32 títulos solo traducían «CAPÍTULO N» | Revisa todos en una hoja de contacto |
| Rehacer sobre la versión traducida | Se acumulan defectos | Parte siempre del original |

### Proceso y herramientas

| Error | Consecuencia | Qué hacer |
|---|---|---|
| Copiar a una carpeta de prueba enlazada a Steam | Un `cp` escribió en `pause_en.par` de Steam; se recuperó verificando integridad | Comprueba que no sea unión ni enlace duro antes de copiar |
| Instalar encima de otra versión | El respaldo guarda la versión vieja | Quita la anterior primero |
| Herramientas que no reproducían el paquete | Quien las usara desharía la versión | Sin cambios, deben dar el mismo texto: nuestro resultado es 0 diferencias en 187.531 textos |
| Sacar versiones tras subir | Dos frases obligaron a una versión aparte | Corre todos los barridos antes de publicar |
| Traductores parados sin avisar | Casi dos horas perdidas | Revisa el avance cada cierto tiempo |
| Se acabó la cuota gratuita | Parón de la traducción | Ten otro modelo de reserva |
| `reARMP` no lee bien las tablas ARMP v2 de `db.devil` | Hizo falta un lector propio (`devil.py`) | Y ojo: guarda el `.json` en la carpeta desde la que se ejecuta |
| `git clone` falla por rutas largas | Sobre todo en el repositorio de la traducción | Usa `git -c core.longpaths=true clone` y una carpeta corta |
| Git Bash estropea `\\`, `\r\n` y `\x00` en los heredoc | Archivos dañados | Escribe el código con un editor |
| `open(p, 'w')` en Windows cambia los saltos a CRLF | Archivos distintos sin querer | Usa `newline=` |
| Zip publicado con `__pycache__\*.pyc` | Nexus revisa los paquetes | Revisa el contenido del zip |
| Nexus pidió el código fuente | Revisión de moderación | Publica el código, declara el uso de IA y no incluyas ejecutables en el mod |

## 9. Decisiones de traducción

**Idioma:** español neutro latinoamericano, coherente con el español oficial de la saga.

**Se dejó en inglés a propósito:**

- Créditos finales y contrato de SEGA.
- Nombres propios, títulos de canciones y mangas.
- Marcas y premios.
- Términos de juego: Heat, BULL, DEALER, HOME RUN, Cricket, Count-Up.
- El `.exe` y lo dibujado dentro de los vídeos.

**Regla práctica:** si la traducción queda demasiado larga o suena peor, se deja el término en inglés. Es lo que hicimos con
«Heat», aunque lo oficial diga «adrenalina».

Cambia solo los **términos** para que coincidan con lo oficial. El estilo de los diálogos es de cada traducción.

## 10. Antes de publicar

- [ ] **Barrido** de todo el inglés en lo ARMADO (`barrido.py`, `barrido_msg.py`).
- [ ] **Frases cortas:** busca las de una palabra y las de una letra que sigan en inglés.
- [ ] **Comparación con el original** (`comparar_original.py`): misma lista dentro de cada `.par`, mismas imágenes y tamaños,
      mismos nombres en cada `.msg`, mismas filas de subtítulos. Nuestro resultado: 0 fallos en 35 archivos.
- [ ] **Cifras** con `contar_datos.py`.
- [ ] **Inicios de capítulo** a ojo.
- [ ] **El juego arranca** tras cada cambio de textos.
- [ ] **Lista de lo que queda en inglés** y por qué, por formato: imágenes, textos, vídeos.
- [ ] **Si publicas herramientas:** sin cambios, deben reproducir tu paquete (`comparar_textos.py`).
- [ ] **El zip:** sin archivos del juego enteros que no hagan falta, sin `.pyc` ni `.exe`, y con LEEME.
- [ ] **Avisos:** es un mod no oficial y gratuito, necesita el juego original y declara el uso de IA ([AVISO.txt](AVISO.txt)).

### Comandos útiles

```bat
rem Cifras: textos de la hoja y comparación con los originales
python programas\contar_datos.py --csv trabajo\textos.csv
python programas\contar_datos.py --partool programas\ParTool\ParTool.exe --original "<originales>" --paquete "..\archivos\data"

rem Cifras de la instalación del juego
python programas\contar_datos.py --juego "<juego>\main\data"
```

`comparar_original.py`, `comparar_textos.py` y `barrido.py` están en `herramientas/` del
[repositorio de la traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish).

## 11. Si algo falla

| Problema | Solución |
|---|---|
| `Falta Python 3` | Instálalo y marca **Add python.exe to PATH** |
| `El juego de Steam ya tiene la traducción puesta` | Quítala con la opción 2 del instalador o verifica la integridad en Steam |
| `No encontré el juego` | Usa `python herramienta_traduccion.py extraer --ingles "<juego>\main\data"` |
| No encuentra `..\archivos` | Las herramientas no están dentro de la carpeta de la traducción ([sección 3](#3-preparar-todo)) |
| Excel muestra todo en una columna | Ábrelo con **Datos > Desde texto/CSV**, en UTF-8 y con `;` |
| Letras raras en el juego | Guarda la hoja como **CSV UTF-8**; revisa también las letras que la rejilla no tiene |
| El juego se cierra | Quita la traducción con la opción 2. Prueba con los originales y luego parte tus cambios por la mitad |
| Sale en inglés | Pon el juego en inglés: es el idioma que se reemplaza |
| Steam actualizó el juego | Vuelve a instalar. Si la versión cambió, borra `trabajo` y extrae de nuevo |
| Quiero empezar de cero | Borra la carpeta `trabajo` |
| El antivirus avisa de `ParTool.exe` | Compara su SHA-256 con la del [README](README.md) o descárgalo de su autor |
