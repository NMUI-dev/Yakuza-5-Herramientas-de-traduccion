# -*- coding: utf-8 -*-
"""Cuenta lo que hay que traducir y lo que cambió, para no dar cifras de memoria. Solo lee.

  python contar_datos.py --partool <ParTool.exe> --original <data original> --paquete <archivos/data de la traducción>
                         [--csv trabajo/textos.csv] [--juego <main/data entera>] [--tmp <carpeta temporal>]

Original y paquete: desempaqueta cada .par con «ParTool extract -r» y compara archivo por archivo (SHA-256).
CSV: el que deja «python herramienta_traduccion.py extraer».
Juego: cuenta los archivos y los vídeos de la instalación, sin desempaquetar nada.
Escribe el resultado en pantalla, en formato de tablas Markdown."""
import argparse, collections, csv, hashlib, os, shutil, subprocess, sys, tempfile


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def extraer(partool, par, dest):
    r = subprocess.run([partool, 'extract', '-r', par, dest], stdin=subprocess.DEVNULL, capture_output=True)
    if r.returncode:
        sys.exit(f'ParTool falló con {par}: {r.stdout.decode(errors="replace")[-400:]}{r.stderr.decode(errors="replace")[-400:]}')


def lista(raiz):
    out = {}
    for dp, _, fs in os.walk(raiz):
        for f in fs:
            p = os.path.join(dp, f)
            out[os.path.relpath(p, raiz).replace(os.sep, '/').lower()] = p
    return out


def comparar(a):
    paquete = lista(a.paquete)
    filas, tot = [], collections.Counter()
    base = a.tmp or tempfile.mkdtemp(prefix='contar_')
    os.makedirs(base, exist_ok=True)
    for i, (rel, p) in enumerate(sorted(paquete.items())):
        o = os.path.join(a.original, rel)
        if not os.path.exists(o):
            sys.exit(f'No está en el original: {rel}')
        c = collections.Counter()
        if rel.endswith('.par'):
            d = os.path.join(base, str(i))
            shutil.rmtree(d, ignore_errors=True)
            extraer(a.partool, o, os.path.join(d, 'o'))
            extraer(a.partool, p, os.path.join(d, 'p'))
            lo, lp = lista(os.path.join(d, 'o')), lista(os.path.join(d, 'p'))
            c['faltan'] = len(set(lo) - set(lp))
            c['sobran'] = len(set(lp) - set(lo))
            for k in set(lo) & set(lp):
                es_dds = k.endswith('.dds')
                c['archivos'] += 1
                c['dds'] += es_dds
                if sha(lo[k]) != sha(lp[k]):
                    c['cambiados'] += 1
                    c['dds_cambiados'] += es_dds
            shutil.rmtree(d, ignore_errors=True)
        else:
            c['archivos'] = 1
            c['cambiados'] = int(sha(o) != sha(p))
        filas.append((rel, c))
        tot.update(c)
        print(f'  {i + 1}/{len(paquete)} {rel}', file=sys.stderr, flush=True)
    print('| Archivo | Archivos dentro | Cambiados | Imágenes .dds | Imágenes cambiadas | Faltan/sobran |')
    print('|---|--:|--:|--:|--:|--:|')
    for rel, c in filas:
        print(f"| `{rel}` | {c['archivos']} | {c['cambiados']} | {c['dds']} | {c['dds_cambiados']} | {c['faltan']}/{c['sobran']} |")
    print(f"| **Total ({len(filas)} archivos del juego)** | **{tot['archivos']}** | **{tot['cambiados']}** | **{tot['dds']}** | "
          f"**{tot['dds_cambiados']}** | **{tot['faltan']}/{tot['sobran']}** |\n")


def contar_csv(p):
    filas = list(csv.DictReader(open(p, encoding='utf-8-sig', newline=''), delimiter=';'))
    grupos = collections.defaultdict(collections.Counter)
    for f in filas:
        d = f['donde']
        g = d.split('|')[0].strip().split(':')[0]
        c = grupos[g]
        c['filas'] += 1
        c['veces'] += int(f['veces'] or 0)
        c['letras'] += len(f['ingles'])
        es = f['espanol']
        c['vacias'] += not es
        c['iguales'] += bool(es) and es == f['ingles']
    tot = collections.Counter()
    print('| Origen del texto | Textos distintos | Apariciones | Letras en inglés | Iguales al inglés | Vacíos |')
    print('|---|--:|--:|--:|--:|--:|')
    for g, c in sorted(grupos.items(), key=lambda x: -x[1]['letras']):
        tot.update(c)
        print(f"| `{g}` | {c['filas']} | {c['veces']} | {c['letras']} | {c['iguales']} | {c['vacias']} |")
    print(f"| **Total** | **{tot['filas']}** | **{tot['veces']}** | **{tot['letras']}** | **{tot['iguales']}** | **{tot['vacias']}** |\n")


def contar_juego(d):
    c = collections.Counter()
    for dp, _, fs in os.walk(d):
        for f in fs:
            n = os.path.getsize(os.path.join(dp, f))
            ext = os.path.splitext(f)[1].lower()
            c['archivos'] += 1
            c['bytes'] += n
            c['n' + ext] += 1
            c['b' + ext] += n
    print(f"Juego: {c['archivos']} archivos, {c['bytes'] / 2**30:.1f} GiB; "
          f".par: {c['n.par']} ({c['b.par'] / 2**30:.1f} GiB); .usm: {c['n.usm']} ({c['b.usm'] / 2**30:.1f} GiB)\n")


def main():
    sys.stdout.reconfigure(encoding='utf-8')        # si no, al redirigir a un archivo Windows usa otra codificación
    ap = argparse.ArgumentParser()
    ap.add_argument('--partool')
    ap.add_argument('--original')
    ap.add_argument('--paquete')
    ap.add_argument('--csv')
    ap.add_argument('--juego')
    ap.add_argument('--tmp')
    a = ap.parse_args()
    if a.partool:
        a.partool = os.path.abspath(a.partool)      # Windows no encuentra un .exe con ruta relativa y barras «/»
    if a.juego:
        contar_juego(a.juego)
    if a.csv:
        contar_csv(a.csv)
    if a.paquete:
        comparar(a)


if __name__ == '__main__':
    main()
