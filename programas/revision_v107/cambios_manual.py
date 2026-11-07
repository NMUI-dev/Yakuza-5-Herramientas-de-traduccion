# (claude2, 06-11-2026) Correcciones decididas a mano con la escena delante (av_manual_ctx.txt) + barridos mecánicos
# seguros. Cada cambio = (id, texto viejo, texto nuevo, motivo): el viejo TIENE que estar en el español actual.
# Uso: python -I -X utf8 cambios_manual.py  -> cambios_manual.json
import csv, json, re
csv.field_size_limit(10 ** 9)
T = "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv"
R = {r["id"]: r for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";")}
out = {}
def c(i, viejo, nuevo, motivo):
    es = out.get(i, {}).get("es", R[i]["espanol"])
    assert es.count(viejo) >= 1, (i, viejo, es)
    out[i] = {"es": es.replace(viejo, nuevo), "motivo": (out[i]["motivo"] + "; " if i in out else "") + motivo}
LES = [("4952", "le gustará a los"), ("13106", "le ordenó a Ushijima"), ("14637", "le deja la limpieza"),
       ("17842", "No le des tanta"), ("19115", "No le decimos"), ("22100", "Le dije a todos"), ("24606", "le dio a mis"),
       ("26008", "le echas la culpa"), ("27673", "le demuestra a los"), ("29643", "le pongas a tus"), ("30577", "le ganaré"),
       ("34498", "le cuente a los"), ("36994", "le deja el trabajo"), ("39719", "Le ganaste"), ("39880", "le ganaste"),
       ("40308", "le ganaste"), ("41871", "le mostrará"), ("49473", "le echo un reto"), ("53524", "le pone etiquetas"),
       ("55660", "le pone miso"), ("56847", "le hablan así"), ("57343", "le resulta atractivo"), ("57591", "le da consejos"),
       ("57874", "Le mencioné"), ("58521", "le traerá dolor"), ("58726", "le recomendarías")]
for i, t in LES:
    c(i, t, t.replace("le ", "les ", 1).replace("Le ", "Les ", 1), "gramática: le -> les (complemento plural)")
c("56358", "No le funciona a todos", "No a todos les funciona", "gramática: le -> les")
c("29954", "¡¿Carajo!? ¡¿Quién demonios son ustedes!?", "¡¿Qué carajo?! ¡¿Quiénes demonios son ustedes?!", "quiénes + signos")
c("57620", "¿Quién diablos son", "¿Quiénes diablos son", "gramática: quiénes")
c("3419", "¿Quién demonios son?", "¿Quiénes demonios son?", "gramática: quiénes")
c("16137", "invertir  una", "invertir una", "espacio doble")
c("24357", "Vaya, ese tipo", "¿Conoces a Kiryu-san? Vaya, ese tipo", "sentido: faltaba la primera frase")
c("29937", "¡Ustedes dos solo la están usando por su dinero!", "¡Ustedes dos solo están usando a Miyu-chan por su dinero!", "sentido: faltaba Miyu-chan")
c("37615", "¿Me gustaría hablar con él, si\nno hay problema?", "Se llama Kanai-san. ¿Podría hablar con él, si\nno es molestia?", "sentido: faltaba la primera frase")
c("38124", "Dicen que saltó", "Akiyama-san... Dicen que saltó", "sentido: faltaba Akiyama-san")
c("41563", "Yamada-kun!", "Sato-san!", "nombre equivocado: habla Yamada a Sato")
c("49126", "me estás diciendo que tú estás detrás", "me están diciendo que ustedes están detrás", "sentido: le habla a varios (you all)")
c("58272", "el resto de la aldea lo ha marginado.", "el resto de la aldea margina a Okudera-san.", "sentido: faltaba Okudera-san")
for i in ("26540", "28190", "28246"):
    c(i, "viejo Kaz,", "Viejo Kaz,", "mayúscula inicial")
c("28190", "quisiera el <Color:8>Barbacoa", "quisiera la <Color:8>Barbacoa", "género")
c("28191", "quiere el <Color:8>Barbacoa", "quiere la <Color:8>Barbacoa", "género")
c("28192", "pedir el <Color:8>Barbacoa", "pedir la <Color:8>Barbacoa", "género")
c("28246", "me gustaría mucho el <Color:8>Camarones", "me gustarían mucho los <Color:8>Camarones", "número")
c("28247", "pedir el <Color:8>Camarones", "pedir los <Color:8>Camarones", "número")
c("28248", "quería el <Color:8>Camarones", "quería los <Color:8>Camarones", "número")
c("67551", "murmuras, tío?", "murmuras, hombre?", "España: tío")
c("67965", "Te envidio, tío.", "Te envidio, hermano.", "España: tío")
c("68421", "ni de coña me voy de aquí con un falso.", "de ninguna puta manera me voy de aquí con una falsa.", "España: ni de coña; misma fuerza (sure as shit)")
c("68422", "me la tendré que llevar a ti conmigo.", "tendré que llevarte conmigo.", "sentido/gramática")
c("68423", "esa debut tuyo", "ese debut tuyo", "género")
c("27963", "desde que te graduarte?", "desde que te graduaste?", "errata")
c("31554", "¡Ven, ustedes dos!", "¡Vamos, ustedes dos!", "concordancia (ustedes)")
c("38926", "menos de veintiún.", "menos de veintiuno.", "gramática")
# barrido de palabras de España / de un país / rotas en todo el juego (06-11, regla: misma fuerza, nunca censurar)
c("110", "¡Alianza igualitaria, mis cojones!", "¿Alianza igualitaria? ¡Y un carajo!", "España: mis cojones; misma fuerza")
c("2369", "¡Mi amistad, mis cojones!", "¿Amigo? ¡Y un carajo!", "España: mis cojones; sentido (Friend)")
c("67908", "¿Qué cojones?", "¿Qué carajo?", "España: qué cojones")
c("48604", "¡Se cree el puto amo!", "¡Se cree la gran mierda!", "España: puto amo")
for i in ("24911", "24915", "24916", "25009", "25015", "25898", "67922", "48604"):
    c(i, "cojones", "huevos", "España: cojones -> huevos (neutro latino, misma fuerza)")
c("20861", "quiero follarme ese pequeño cuerpo desvergonzado.\nAhora, no abras el ano hasta", "quiero cogerme ese cuerpecito pervertido.\nAhora, cierra el hocico hasta", "España: follar; sentido: blow hole = boca")
c("42643", "cobrar y follar", "cobrar y coger", "España: follar")
c("17729", "malparido!", "pervertido!", "regional (Colombia) y sentido: creep")
c("30278", "Hey, mira esto, Ryotaighted. Cayó.", "Oye, mira esto, a Ryota lo agarraron.", "palabra rota")
c("30769", "este pendejo", "este inútil de mierda", "regional (México): pendejo; misma fuerza")
c("68949", "era solo un pendejo.", "era solo un mocoso estúpido.", "regional (México): pendejo")
# correo de logros DESPLAZADO (mail.bin 57378-57587): el español era de otra fila
MAIL = {"14852": "¡Casilleros de Sotenbori completados!", "14853": "casilleros de monedas de Sotenbori!",
        "14854": "¡Recolección de basura completada!", "14855": "completando todas las misiones",
        "14856": "de recolección de basura!", "14857": "¡Boletos de premio completados!", "14858": "completando todos los"}
for i, t in MAIL.items():
    out[i] = {"es": t, "motivo": "desplazado: el español era de otra fila del correo de logros"}
# a por (España) -> por
for i, r in R.items():
    es = out.get(i, {}).get("es", r["espanol"])
    if re.search(r"\b[Aa] por\b", es):
        nuevo = re.sub(r"\ba por ", "por ", re.sub(r"\bA por ", "Por ", es))
        out[i] = {"es": nuevo, "motivo": (out[i]["motivo"] + "; " if i in out else "") + "España: a por"}
c("43758", "Todos, ven por mí", "Todos, vengan por mí", "concordancia")
out.pop("30345")   # «una A por el esfuerzo» (nota escolar): no es «a por»
c("51244", "¡Por ello!", "¡Ve por ellos!", "España: a por; sentido (Go get 'em)")
c("61550", "¿Cómo entraste acá? ¡Por ellos!", "¡¿Cómo entraste acá?! ¡Vayan por ellos, muchachos!", "España: a por; signos")
c("67839", "¡Por él!", "¡Vayan por él!", "España: a por")
# risas en inglés -> español
RISA = re.compile(r"\b([Hh])((?:a|e|i)(?:h(?:a|e|i))+)\b|\b([Hh])(a|e)\b(?=[,.!?…\s])")
for i, r in R.items():
    es = out.get(i, {}).get("es", r["espanol"])
    nuevo = re.sub(r"\b([Hh])([aei])((?:h[aei])+)\b", lambda m: ("J" if m.group(1) == "H" else "j") + m.group(2) + m.group(3).replace("h", "j"), es)
    if nuevo != es:
        out[i] = {"es": nuevo, "motivo": (out[i]["motivo"] + "; " if i in out else "") + "risa: Haha/Hehe -> Jaja/Jeje"}
# --- globos (pac) donde la versión del ayudante no cabía: versión corta que cabe (medida en bytes) ---
PAC = {"61550": ("¡¿Cómo entraste?! ¡Por ellos!", "España: a por; signos (cabe en el globo)"),
       "62096": ("¡Hoy traigo dinero!", "sentido: flush = con dinero, no «acalorada»"),
       "62320": ("¡Faltan 10 yen!", "sentido: short by = faltan"),
       "61974": ("¿Eh? Uy.", "inglés sin traducir (Huh? Whoa!)"),
       "62368": ("¡Puta!", "signos; misma fuerza (Fuuuuck!)"),
       "61957": ("Qué hago contigo...", "signos: ¿ sin cierre"),
       "61882": ("¡¿Y mi llave?!", "signos"),
       "61939": ("¡Perdón! ¿Esperaste?", "signos"),
       "62130": ("¿El tuyo igual?", "signos"),
       "61837": ("¡¿Qué <Italic>es</Italic> esto?!", "signos")}
for i, (t, m) in PAC.items():
    out[i] = {"es": t, "motivo": m}
# --- choques con los ayudantes de signos: las dos correcciones juntas ---
out["24952"]["es"] = "¿Oh? Jaja, entiendo. ¡Bueno, sin duda reconozco esa cualidad\nen mí, si se me permite presumir!"
out["52051"] = {"es": "¡Jajajaja! ¡Aunque sería muy ridículo tener un cliente que venga todo el tiempo con arroz pegado en la cara!", "motivo": "risa; signos"}
out["55660"]["es"] = "¡Así es! ¡Ahora le gusta tanto que les pone miso hasta a sus recetas de cocina francesa!"
# --- fallos en líneas vecinas que vieron los ayudantes ---
c("3486", "¿Talent natural?", "¿Talento natural?", "errata")
c("22112", "por primera vez!?", "por primera vez?!", "signos")
c("29768", "¡¿Entonces me engañaste!?", "¡¿Entonces me engañaste?!", "signos")
c("30178", "¡ Aposté todo por poder atrapar a ese malhechor!", "¡Aposté todo por atrapar a ese cabrón!", "espacio; grosería suavizada (bastard)")
out["68219"] = {"es": "Ni lo sueñes. ¡El maldito sol se enfriará antes de que\naverigües cómo enseñar a ese mocoso por tu cuenta!", "motivo": "signos; errata (averiguës); calco (Como si.)"}
c("26230", "¿Quieres follar?", "¿Quieres coger?", "España: follar")
c("21178", "¡Ándale, hijo!", "¡Anda, hijo!", "regional (México): ándale")
for i in ("61126", "61129", "61152", "61258"):
    c(i, "Sotenbori  ", "Sotenbori ", "espacio doble")
# artículo que no concuerda con el nombre del objeto (ideas_ia_y5.py, idea 47 de las IA)
ART = {"22565": ("un <Color:8>Venda", "una <Color:8>Venda"), "22576": ("una <Color:8>Plátano", "un <Color:8>Plátano"),
       "22599": ("un <Color:8>Venda", "una <Color:8>Venda"), "22622": ("una <Color:8>Chicle", "un <Color:8>Chicle"),
       "22623": ("una <Color:8>Yokan", "un <Color:8>Yokan"), "26305": ("un <Color:8>Gallina", "una <Color:8>Gallina"),
       "39326": ("la <Color:8>Plato", "el <Color:8>Plato"), "43344": ("un <Color:8>Navaja", "una <Color:8>Navaja"),
       "47392": ("un <Color:8>Tubería", "una <Color:8>Tubería"), "48273": ("comer un <Color:8>Cola", "tomar una <Color:8>Cola"),
       "48274": ("del <Color:8>Cola", "de la <Color:8>Cola"), "48275": ("un <Color:8>Cola", "una <Color:8>Cola"),
       "58369": ("una <Color:8>Lazo", "un <Color:8>Lazo")}
for i, (a, b) in ART.items():
    c(i, a, b, "género del artículo con el objeto")
for i in ("48304", "48311", "48314", "49457", "49820"):
    c(i, "un <Color:8>Vara", "una <Color:8>Vara", "género del artículo con el objeto")
# subtítulos de dos renglones que USA el juego (fila «sub» con el texto entre comillas; la «extra-sub» gemela no sale)
c("790", "¡No te asustes porque sea", "¡No se asusten porque sea", "tú/ustedes: le habla al grupo (¡Atáquenlo!)")
c("2014", "tendré que llevarte contigo.", "tendré que llevarte conmigo.", "sentido: conmigo")
c("2205", "y no me veo la hora de ver lo que hace después!", "y no veo la hora de ver lo que hace después!", "errata")
# renglones anteriores a los finales de correo que la herramienta dejaba en INGLÉS (filtro_mayusculas.py): el final va
# en su fila nueva (juntar.py, NUEVAS) y aquí se quita lo que ya decía el renglón de antes, para que no salga repetido
c("13643", "la evaluación crediticia de Kansai", "la agencia de crédito de", "final de correo en inglés (board.)")
c("13852", "De verdad espero aprobar el", "De verdad espero aprobar la", "final de correo en inglés (audition.)")
c("14399", "y ladra si hay algo.", "y ladra si hay algún", "final de correo en inglés (danger.)")
c("14635", "aprender a recoger lo que deja.", "aprender a recoger lo que", "final de correo en inglés (themselves.)")
c("14666", "chica desde que empezó.", "chica desde que empezó", "final de correo en inglés (here.)")
c("14751", "MC Mittsu será nuestro invitado.", "MC Mittsu será nuestro juez", "final de correo en inglés (judge.)")
c("14783", "Será un placer atenderte ", "Será un placer atenderte", "final de correo en inglés (again.)")
c("14935", "de zonas en esta demo.", "de zonas en esta", "final de correo en inglés (demo.)")
# «Heheh» / «Hahah» (risa con h final) -> Jeje / Jaja
for i, r in R.items():
    es = out.get(i, {}).get("es", r["espanol"])
    nuevo = re.sub(r"\b([Hh])([ae])h\2h\b", lambda m: ("J" if m.group(1) == "H" else "j") + m.group(2) + "j" + m.group(2), es)
    if nuevo != es:
        out[i] = {"es": nuevo, "motivo": (out[i]["motivo"] + "; " if i in out else "") + "risa: Heheh -> Jeje"}
json.dump(out, open("cambios_manual.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "cambios")
