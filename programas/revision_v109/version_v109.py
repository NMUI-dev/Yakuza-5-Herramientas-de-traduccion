# (claude2, 07-11-2026) version para la v1.0.9 (copia de version_v108.py).
# (claude2, 06-11-2026) Copia de version_v107.py para la v1.0.8.
# (claude2, 06-11-2026) Sube a 1.0.8 los textos del paquete entrega_v109 (instalador, .bat, LEEME, guía de la herramienta)
# y pone en el LEEME los cambios de la v1.0.8. Lo llama herramientas/v108_armar.sh al final.
import io
E = "C:/Mods/yakuza5/entrega_v109/"
def cambiar(rel, pares, bom=True):
    p = E + rel; s = open(p, encoding="utf-8-sig", newline="").read()
    for a, b in pares:
        assert a in s, (rel, a); s = s.replace(a, b)
    open(p, "w", encoding="utf-8-sig" if bom else "utf-8", newline="").write(s)
cambiar("instalar.ps1", [('$VERSION = "1.0.8"', '$VERSION = "1.0.9"')])
cambiar("INSTALAR o QUITAR.bat", [("v1.0.8: instalar o quitar", "v1.0.9: instalar o quitar")], bom=False)
cambiar("Herramientas para traduccion/COMO_USAR.txt", [("YAKUZA 5 REMASTERED (v1.0.8)", "YAKUZA 5 REMASTERED (v1.0.9)"),
        ("los mismos textos que el paquete v1.0.8.", "los mismos textos que el paquete v1.0.9.")])
NUEVO = """CAMBIOS EN LA v1.0.9 (07-11-2026)
- 151 textos con el punto o la coma de cierre DENTRO de las comillas pasan a ponerlo fuera, como pide la RAE
  (la canción "Machine Gun Kiss". Puede...).
- Ronda final de preguntas a las IA: nada más que corregir (escala de cifras y códigos de casilleros, comprobados).
- Actualizar desde la v1.0.8 o anterior: PRIMERO quita la anterior (su «INSTALAR o QUITAR.bat», opción 2) y luego
  instala esta.

"""
p = E + "LEEME.txt"; s = open(p, encoding="utf-8-sig", newline="").read()
s = s.replace("TRADUCCIÓN AL ESPAÑOL v1.0.8 (06-11-2026)", "TRADUCCIÓN AL ESPAÑOL v1.0.9 (07-11-2026)", 1)
i = s.index("CAMBIOS EN LA v1.0.8"); s = s[:i] + (NUEVO.replace("\n", "\r\n") if "\r\n" in s else NUEVO) + s[i:]
s = s.replace("«Yakuza 5 - Herramientas para traduccion v1.0.8»", "«Yakuza 5 - Herramientas para traduccion v1.0.9»")
open(p, "w", encoding="utf-8-sig", newline="").write(s)
print("versión 1.0.9 puesta")
