# (claude2, 07-11-2026) v1.0.10: lo que se vio en el juego al revisar los menús largos (ancho_menus_y5.py + capturas
# trabajo/capturas/hab2.png): la categoría «Entrenamiento/Revelaciones» se salía de su caja (294 px; cabe ~235).
import json
out = {"3609": {"es": "Entreno/Revelaciones", "motivo": "menú: se salía de la caja de categorías (visto en el juego)"}}
json.dump(out, open("cambios_v110.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
