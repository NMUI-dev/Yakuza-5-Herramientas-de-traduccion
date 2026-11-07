# (claude2, 06-11-2026) Zips de la v1.0.8 para GitHub/Nexus: traducción (carpeta de paquete_v108) y herramientas
# (= zip de la v1.0.6 con los archivos del repo yakuza5-herramientas al día; ParTool/reARMP/texconv siguen del zip viejo).
import os, zipfile, pathlib
T = pathlib.Path("C:/Mods/yakuza5/trabajo")
P = T / "paquete_v108"; N = "Yakuza 5 - Traduccion al espanol v1.0.8"
with zipfile.ZipFile(P / "Yakuza.5.-.Traduccion.al.espanol.v1.0.8.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted((P / N).rglob("*")):
        z.write(p, p.relative_to(P).as_posix())
viejo = zipfile.ZipFile(T / "paquete_v107" / "Yakuza.5.-.Herramientas.para.traduccion.v1.0.7.zip")
R = pathlib.Path("C:/Mods/github/yakuza5-herramientas")
repo = {p.relative_to(R).as_posix(): p for p in R.rglob("*") if p.is_file() and ".git" not in p.relative_to(R).parts}
PRE = "Herramientas para traduccion/"
hechos = set()
with zipfile.ZipFile(P / "Yakuza.5.-.Herramientas.para.traduccion.v1.0.8.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for i in viejo.infolist():
        rel = i.filename[len(PRE):]
        if i.filename.endswith("/"):
            z.writestr(i, b""); continue
        if rel in repo:
            z.write(repo[rel], i.filename); hechos.add(rel)
        else:
            z.writestr(i, viejo.read(i))
    for rel, p in sorted(repo.items()):
        if rel not in hechos:
            z.write(p, PRE + rel)
for f in ("Yakuza.5.-.Traduccion.al.espanol.v1.0.8.zip", "Yakuza.5.-.Herramientas.para.traduccion.v1.0.8.zip"):
    zz = zipfile.ZipFile(P / f); n = zz.namelist()
    malos = [x for x in n if "respaldo_original" in x or "__pycache__" in x or "/trabajo/" in x]
    print(f, len(n), "archivos", os.path.getsize(P / f) // 1048576, "MB", "| prohibidos:", malos[:3])
