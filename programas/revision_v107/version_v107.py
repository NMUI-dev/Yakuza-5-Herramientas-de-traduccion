# (claude2, 06-11-2026) Sube a 1.0.7 los textos del paquete entrega_v107 (instalador, .bat, LEEME, guía de la herramienta)
# y pone en el LEEME los cambios de la v1.0.7. Lo llama herramientas/v107_armar.sh al final.
import io
E = "C:/Mods/yakuza5/entrega_v107/"
def cambiar(rel, pares, bom=True):
    p = E + rel; s = open(p, encoding="utf-8-sig", newline="").read()
    for a, b in pares:
        assert a in s, (rel, a); s = s.replace(a, b)
    open(p, "w", encoding="utf-8-sig" if bom else "utf-8", newline="").write(s)
cambiar("instalar.ps1", [('$VERSION = "1.0.6"', '$VERSION = "1.0.7"')])
cambiar("INSTALAR o QUITAR.bat", [("v1.0.6: instalar o quitar", "v1.0.7: instalar o quitar")], bom=False)
cambiar("Herramientas para traduccion/COMO_USAR.txt", [("YAKUZA 5 REMASTERED (v1.0.6)", "YAKUZA 5 REMASTERED (v1.0.7)"),
        ("los mismos textos que el paquete v1.0.6.", "los mismos textos que el paquete v1.0.7.")])
NUEVO = """CAMBIOS EN LA v1.0.7 (revisión con las reglas de los traductores profesionales y la regla NUNCA CENSURAR)
- 2.010 textos corregidos:
  · 113 groserías que estaban SUAVIZADAS: ahora con la misma fuerza que el original («Watch your fuckin' mouth»
    ya no es «Cuidado con lo que dices» sino «Cuida tu maldita boca»). La obra se respeta tal cual es.
  · 36 expresiones de España o de un solo país cambiadas a español neutro con la misma fuerza («ni de coña», «a por»,
    «mis cojones», «follar», «tío», «pendejo», «malparido», «mamadas», «ándale»).
  · 64 de SENTIDO: frases que perdían un trozo («Se llama Kanai-san», «¿Conoces a Kiryu-san?»), un nombre cambiado
    (Sato-san por Yamada-kun), 7 renglones DESPLAZADOS en el correo de logros y 13 finales de correo que salían en inglés
    («then.», «danger.», «interested.»...).
  · 60 de gramática: «le» por «les» («les ganaste a los Devil Killers»), «quiénes son», género y número de los objetos
    («la Barbacoa de cordero», «una Vara de nébeda», «los Camarones»).
  · 666 signos de pregunta y exclamación sin pareja o perdidos (el inglés exclamaba o preguntaba y el español no).
  · 1.015 subtítulos y diálogos con el renglón partido por mal sitio («...de la / Familia Yamagasa»): ahora la palabra
    va con la que acompaña, sin que el texto ocupe más.
  · 36 risas en inglés («Haha», «Hehe») a «Jaja», «Jeje»; 16 erratas, espacios dobles y palabras rotas («Ryotaighted»).
- Actualizar desde la v1.0.6 o anterior: PRIMERO quita la anterior (su «INSTALAR o QUITAR.bat», opción 2) y luego
  instala esta.

"""
p = E + "LEEME.txt"; s = open(p, encoding="utf-8-sig", newline="").read()
s = s.replace("TRADUCCIÓN AL ESPAÑOL v1.0.6 (06-11-2026)", "TRADUCCIÓN AL ESPAÑOL v1.0.7 (06-11-2026)", 1)
i = s.index("CAMBIOS EN LA v1.0.6"); s = s[:i] + (NUEVO.replace("\n", "\r\n") if "\r\n" in s else NUEVO) + s[i:]
s = s.replace("«Yakuza 5 - Herramientas para traduccion v1.0.6»", "«Yakuza 5 - Herramientas para traduccion v1.0.7»")
open(p, "w", encoding="utf-8-sig", newline="").write(s)
print("versión 1.0.7 puesta")
