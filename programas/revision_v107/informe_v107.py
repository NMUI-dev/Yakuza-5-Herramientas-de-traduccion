# (claude2, 06-11-2026) Escribe «Errores corregidos v1.0.7.txt»: todas las frases cambiadas, por tipo, con inglés/antes/ahora/motivo.
import json, collections, sys
C = json.load(open("correcciones_0611b.json", encoding="utf-8"))
TIPOS = [("grosería suavizada (regla del usuario: NUNCA CENSURAR)", ("grosería", "suavizad", "misma fuerza")),
         ("España / regionalismo", ("España", "regional")),
         ("sentido / frase incompleta / nombre equivocado / texto desplazado", ("sentido", "nombre equivocado", "desplazado", "faltaba", "final de correo")),
         ("gramática: le->les, quiénes, género, número, artículo", ("gramática", "género", "número", "concordancia", "artículo")),
         ("tú/usted", ("tú/usted",)),
         ("erratas, espacios, mayúsculas, palabras rotas, calcos", ("errata", "espacio", "mayúscula", "palabra rota", "inglés sin traducir", "calco")),
         ("risas Haha/Hehe -> Jaja/Jeje", ("risa",)),
         ("signos ¿? ¡! y final de frase", ("signos", "final", "pregunta")),
         ("renglón partido por sentido (solo se movió una palabra de renglón)", ("renglón partido",))]
por = collections.defaultdict(list)
for i, c in C.items():
    m = c["motivo"].replace("renglón partido por sentido", "") or "renglón partido"
    for nombre, claves in TIPOS:
        if any(k.lower() in m.lower() for k in claves):
            por[nombre].append((i, c)); break
    else:
        por["otros"].append((i, c))
f = lambda s: s.replace("\r\n", " / ").replace("\n", " / ")
L = ["ERRORES CORREGIDOS EN LA v1.0.7 (06-11-2026)", "",
     "Revisión con las reglas de los traductores profesionales (Netflix español latino, guía de Microsoft, RAE), las",
     "comprobaciones que propusieron las IA consultadas en cadena y la regla del usuario NUNCA CENSURAR: «hay que mantener la",
     "esencia de la obra». Cada caso se decidió con su escena delante.",
     "Total: %d textos. Comprobados dentro de los archivos armados del juego (1.994; los 16 restantes son una copia del" % len(C),
     "subtítulo que el juego no muestra: se corrigió también la que sí sale) y probado en el juego (laboratorio con los mismos 35 archivos que quedaron instalados en Steam).", ""]
orden = [t for t, _ in TIPOS] + (["otros"] if por["otros"] else [])
for k in orden: L.append("  %5d  %s" % (len(por[k]), k))
for k in orden:
    L += ["", "=" * 100, "%s (%d)" % (k.upper(), len(por[k])), "=" * 100]
    for i, c in sorted(por[k], key=lambda x: int(x[0])):
        L += ["[%s] %s" % (i, c["motivo"]), "   EN:    " + f(c["en"]), "   Antes: " + f(c["antes"]), "   Ahora: " + f(c["es"])]
salida = sys.argv[1] if len(sys.argv) > 1 else "Errores corregidos v1.0.7.txt"
open(salida, "w", encoding="utf-8-sig").write("\n".join(L) + "\n")
print("\n".join(L[:20]))
