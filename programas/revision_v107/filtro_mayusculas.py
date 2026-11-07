# (claude2, 06-11-2026) Aviso de claude1 (Y6): el filtro es_texto deja fuera frases cortas. En el Y5 la regla
# «todo MAYÚSCULAS/cifras/._-» (re.fullmatch(r'[A-Z0-9_./\-]+')) puede tirar «OK.», «NO.», «GO!»... Este programa recorre
# todo el inglés extraído y lista lo que esa regla descarta y que parece palabra (2+ letras con vocal) -> filtro_mayusculas.txt
import collections, os, re, sys, importlib.util
H = "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/"
_s = importlib.util.spec_from_file_location("h", H + "herramienta_traduccion.py"); h = importlib.util.module_from_spec(_s)
sys.argv = ["x"]; _s.loader.exec_module(h)
sys.stdout.reconfigure(encoding="utf-8")
orig = h.es_texto
tirados = collections.Counter()
def es_texto(s):
    r = orig(s)
    if not r and (re.fullmatch(r'[A-Z0-9_./\-]+', s) or re.fullmatch(r'[a-z0-9_./\-]+', s)) and re.search(r'[A-Za-z]{2}', s) \
            and re.search(r'[AEIOUYaeiouy]', s) and '_' not in s and '/' not in s:
        tirados[s] += 1
    return r
h.es_texto = es_texto
for dp, _, fs in os.walk(h.EXTRAIDO):
    for f in fs:
        p = os.path.join(dp, f); rel = os.path.relpath(p, h.EXTRAIDO).replace("\\", "/")
        if rel in h.EXCLUIR: continue
        try: h.celdas_de(open(p, "rb").read(), rel)
        except Exception as e: pass
with open("C:/Mods/yakuza5/trabajo/revision_0611b/filtro_mayusculas.txt", "w", encoding="utf-8") as o:
    for s, n in tirados.most_common():
        o.write("%d\t%r\n" % (n, s))
print("distintos", len(tirados), "apariciones", sum(tirados.values()))
