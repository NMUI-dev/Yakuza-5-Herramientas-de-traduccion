# (claude2, 06-11-2026) Pone las correcciones de la v1.0.7 (correcciones_0611b.json) en la herramienta de entrega_v107:
# trabajo/textos.csv (= textos_v107_previsto.csv), datos/traducciones.json y el «es» de datos/textos_extra.json.
# Así «aplicar» sin tocar nada da exactamente el paquete v1.0.7 (lo mismo que se hizo en la v1.0.6).
import json, shutil, sys, importlib.util
H = "C:/Mods/yakuza5/entrega_v107/Herramientas para traduccion/"
_s = importlib.util.spec_from_file_location("h", H + "herramienta_traduccion.py"); h = importlib.util.module_from_spec(_s)
sys.argv = ["x"]; _s.loader.exec_module(h)
corr = json.load(open("C:/Mods/yakuza5/trabajo/revision_0611b/correcciones_0611b.json", encoding="utf-8"))
shutil.copy("C:/Mods/yakuza5/trabajo/revision_0611b/textos_v107_previsto.csv", H + "trabajo/textos.csv")
tr = json.load(open(H + "datos/traducciones.json", encoding="utf-8"))
ex = json.load(open(H + "datos/textos_extra.json", encoding="utf-8"))
por_en = {h.norm(c["en"]): c for c in corr.values()}
n_tr = n_ex = 0
# (06-11) finales de correo que es_texto tomaba por códigos («then.», «board.»...): la herramienta los acepta desde la v1.0.7
NUEVAS = {k for k, c in por_en.items() if c["antes"] == ""}
ht = open(H + "herramienta_traduccion.py", encoding="utf-8").read()
viejo = "CORTAS_SI = {\"I'm...\", 'I...'}"
assert viejo in ht, "no encuentro CORTAS_SI"
ht = ht.replace(viejo, "CORTAS_SI = {\"I'm...\", 'I...',\n    # (v1.0.7) último renglón de correos (mail.bin) que quedaba en inglés\n    "
                + ", ".join(repr(k) for k in sorted(NUEVAS)) + "}")
open(H + "herramienta_traduccion.py", "w", encoding="utf-8").write(ht)
for k in NUEVAS:
    tr[k] = h.norm(por_en[k]["es"])
for k, c in por_en.items():
    if k in tr and k not in NUEVAS:
        if tr[k] != h.norm(c["antes"]) and tr[k] != c["antes"]:
            print("AVISO traducciones.json no tenía el «antes»:", repr(k[:50]), repr(tr[k][:50]))
        tr[k] = h.norm(c["es"]); n_tr += 1
for x in ex:
    c = por_en.get(h.norm(x["t"]))
    if c and x.get("es") is not None:
        x["es"] = h.norm(c["es"]); n_ex += 1
json.dump(tr, open(H + "datos/traducciones.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(ex, open(H + "datos/textos_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("traducciones.json", n_tr, "| textos_extra.json", n_ex, "| correcciones", len(corr))
