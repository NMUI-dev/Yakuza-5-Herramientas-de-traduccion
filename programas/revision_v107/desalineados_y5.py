# (claude2, 06-11-2026) Textos DESPLAZADOS (el español es de otra fila): nombre propio o cifra en el español que el
# inglés no lleva. Halló 14852-14858 de mail.bin (correo de logros con las subhistorias de otra fila). Solo marca.
# Uso: python -I -X utf8 desalineados_y5.py > desalineados.txt
import csv, re
csv.field_size_limit(10 ** 9)
import os
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv")   # Y5_TEXTOS = otro CSV (p. ej. el previsto de la v1.0.7)
NOMBRES = ["Kiryu", "Saejima", "Haruka", "Akiyama", "Shinada", "Majima", "Daigo", "Dojima", "Kaz", "Kazuma", "Taiga",
           "Shun", "Tatsuo", "Sawamura", "Morinaga", "Katsuya", "Hamazaki", "Aizawa", "Watase", "Kurosawa", "Baba",
           "Park", "Mirei", "Kanai", "Tsubasa", "Kamurocho", "Sotenbori", "Nagasugai", "Tsukimino", "Sapporo",
           "Fukuoka", "Osaka", "Nagoya", "Okinawa", "Tokio", "Tojo", "Omi", "Yamagasa", "Amon", "Nakajima"]
NOM = re.compile(r"\b(%s)\b" % "|".join(NOMBRES))
NUM = re.compile(r"\d+")
n = 0
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if not es:
        continue
    malos = [x for x in set(NOM.findall(es)) if x not in en and not (x == "Tokio" and "Tokyo" in en)
             and not (x == "Kaz" and "Kazu" in en)]
    nums = [x for x in set(NUM.findall(re.sub(r"<[^>]*>", "", es))) if x not in en and len(x) <= 6]
    nums = [x for x in nums if x.replace(",", "") not in en.replace(",", "")]
    if malos or nums:
        n += 1
        print("%s\t%s\t%s\t%s\t%s\t%s" % (r["id"], r["donde"][:40], ",".join(malos), ",".join(nums),
                                          en.replace("\n", " / ")[:120], es.replace("\n", " / ")[:120]))
print("total", n)
