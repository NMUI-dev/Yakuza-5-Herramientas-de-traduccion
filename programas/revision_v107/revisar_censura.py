# (claude2, 06-11-2026) Mi revisión de cambios_censura.json (ayudante): arreglos encima y descartes -> cambios_censura_ok.json
import json
d = json.load(open("cambios_censura.json", encoding="utf-8"))
ARREGLO = {
 "9448": "Jeh, mierdas que pasan.",
 "9498": "¡No me jodas!",
 "16389": 'Lástima que ese "si" sea tan condenadamente grande.',
 "16776": "Ah, sí. Lo que hizo fue una locura de mierda.",
 "22932": "Por mí, bien. Toda esa mierda me dio aún más ganas de darte una paliza.",
 "31419": "Pura mierda. Le tendiste una trampa, ¿verdad? Te aprovechaste de que no conocía ni lo más básico de esta ciudad.",
 "40163": "¡Eso es pura mierda! ¡De ninguna manera podría perder contra un chofer de poca monta!",
 "62181": "¡Ja! ¿Victory Road? ¡Ni de puta broma!",
 "62249": "¡Tuviste el descaro de venir con ese atuendo! ¡Te voy a dar una puta paliza!",
}
REEMPLAZO = {"20852": [("esa cámara tuya", "esa cámara suya")], "21182": [("los hará estrellas", "las hará estrellas")],
             "68805": [("poner mi mierda en orden", "poner mi puta vida en orden")]}
DESCARTAR = {"22366", "68421"}   # 22366: calco («su mierda en orden»); 68421: va mi versión (cambios_manual)
for i, t in ARREGLO.items():
    d[i]["es"] = t; d[i]["motivo"] += " (revisado claude2)"
for i, l in REEMPLAZO.items():
    for a, b in l:
        assert a in d[i]["es"], (i, a); d[i]["es"] = d[i]["es"].replace(a, b)
    d[i]["motivo"] += " (revisado claude2)"
for i in DESCARTAR:
    d.pop(i)
json.dump(d, open("cambios_censura_ok.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(d))
