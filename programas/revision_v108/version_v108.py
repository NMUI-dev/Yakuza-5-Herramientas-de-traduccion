# (claude2, 06-11-2026) Copia de version_v107.py para la v1.0.8.
# (claude2, 06-11-2026) Sube a 1.0.8 los textos del paquete entrega_v108 (instalador, .bat, LEEME, guía de la herramienta)
# y pone en el LEEME los cambios de la v1.0.8. Lo llama herramientas/v108_armar.sh al final.
import io
E = "C:/Mods/yakuza5/entrega_v108/"
def cambiar(rel, pares, bom=True):
    p = E + rel; s = open(p, encoding="utf-8-sig", newline="").read()
    for a, b in pares:
        assert a in s, (rel, a); s = s.replace(a, b)
    open(p, "w", encoding="utf-8-sig" if bom else "utf-8", newline="").write(s)
cambiar("instalar.ps1", [('$VERSION = "1.0.7"', '$VERSION = "1.0.8"')])
cambiar("INSTALAR o QUITAR.bat", [("v1.0.7: instalar o quitar", "v1.0.8: instalar o quitar")], bom=False)
cambiar("Herramientas para traduccion/COMO_USAR.txt", [("YAKUZA 5 REMASTERED (v1.0.7)", "YAKUZA 5 REMASTERED (v1.0.8)"),
        ("los mismos textos que el paquete v1.0.7.", "los mismos textos que el paquete v1.0.8.")])
NUEVO = """CAMBIOS EN LA v1.0.8 (velocidad de lectura y términos únicos)
- 26 subtítulos de escena que pedían leer demasiado rápido (más de 20 letras por segundo) acortados sin perder el sentido;
  de paso, «Suselegantes» y «the force» (la policía, no «este juego»).
- Un término, una traducción: «health» es siempre «salud», como en la saga oficial (antes también «vida»), y «hostess
  club» es «club de anfitrionas» (antes también «club de cabaré»; un globo lo conserva porque no cabe).
- Pesca: el aviso «¡Atrapaste...!» tenía el tamaño y el nombre del pez en orden cambiado respecto al juego (%d/%s), lo
  que podía mostrar basura o cerrar el juego al pescar. Arreglado.
- Falsos amigos: «eventualmente» por «eventually» (al final, tarde o temprano), «asumir» por «assume» (suponer, dar por
  hecho), «simpatía» por «sympathy» (compasión); y una ficha de personaje a la que le faltaba una frase.
- Actualizar desde la v1.0.7 o anterior: PRIMERO quita la anterior (su «INSTALAR o QUITAR.bat», opción 2) y luego
  instala esta.

"""
p = E + "LEEME.txt"; s = open(p, encoding="utf-8-sig", newline="").read()
s = s.replace("TRADUCCIÓN AL ESPAÑOL v1.0.7 (06-11-2026)", "TRADUCCIÓN AL ESPAÑOL v1.0.8 (06-11-2026)", 1)
i = s.index("CAMBIOS EN LA v1.0.7"); s = s[:i] + (NUEVO.replace("\n", "\r\n") if "\r\n" in s else NUEVO) + s[i:]
s = s.replace("«Yakuza 5 - Herramientas para traduccion v1.0.7»", "«Yakuza 5 - Herramientas para traduccion v1.0.8»")
open(p, "w", encoding="utf-8-sig", newline="").write(s)
print("versión 1.0.8 puesta")
