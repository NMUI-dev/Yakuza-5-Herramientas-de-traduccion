# (claude2, 06-11-2026) Cuenta las correcciones de la v1.0.7 por tipo (por el «motivo») para el LEEME y el informe.
import json, collections, sys
sys.stdout.reconfigure(encoding="utf-8")
C = json.load(open("correcciones_0611b.json", encoding="utf-8"))
TIPOS = [("grosería suavizada (NUNCA CENSURAR)", ("grosería", "suavizad", "misma fuerza", "Fuuuuck")),
         ("España / regionalismo", ("España", "regional")),
         ("signos ¿? ¡! y final de frase", ("signos", "final", "¡ mal", "¿ sin")),
         ("sentido / frase incompleta / nombre equivocado", ("sentido", "nombre equivocado", "desplazado", "faltaba", "final de correo")),
         ("gramática: le->les, quiénes, género, número, artículo", ("gramática", "género", "número", "concordancia", "artículo")),
         ("tú/usted", ("tú/usted", "usted")),
         ("risas Haha/Hehe -> Jaja/Jeje", ("risa",)),
         ("erratas, espacios, mayúsculas, palabras rotas", ("errata", "espacio", "mayúscula", "palabra rota", "inglés sin traducir", "calco")),
         ("renglón partido por sentido", ("renglón partido",))]
c = collections.Counter(); por = collections.defaultdict(int)
for i, x in C.items():
    m = x["motivo"]; m2 = m.replace("renglón partido por sentido", "")
    for nombre, claves in TIPOS:
        if any(k.lower() in (m if "renglón" in k else m2).lower() for k in claves):
            c[nombre] += 1
print("total frases", len(C))
for nombre, _ in TIPOS:
    print("%5d  %s" % (c[nombre], nombre))
