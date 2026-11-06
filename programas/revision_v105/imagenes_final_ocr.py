# -*- coding: utf-8 -*-
"""(05-11-2026) Revisión de las IMÁGENES del paquete FINAL (no de las copias de trabajo): saca todas las .dds de los .par
del paquete y del original, se queda con las que cambian, les pasa OCR (RapidOCR local) y marca palabras inglesas
(diccionario en, no es) que no sean de la lista de lo que se deja a propósito. Retoma si se corta.
  python -u imagenes_final_ocr.py extraer <data paquete> <data original> <salida>
  python -u imagenes_final_ocr.py ocr <salida>        -> <salida>/ocr.json y <salida>/ingles.txt
"""
import hashlib, json, os, re, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
AQUI = os.path.dirname(os.path.abspath(__file__))
PT = os.path.join(AQUI, 'partool', 'ParTool.exe')


def win(p): return subprocess.run(['cygpath', '-w', p], capture_output=True, text=True).stdout.strip() if p.startswith('/') else p


def extraer(paq, ori, sal):
    for raiz, dst in ((paq, 'es'), (ori, 'en')):
        for dp, _, fs in os.walk(raiz):
            for f in fs:
                if not f.endswith('.par'): continue
                rel = os.path.relpath(os.path.join(dp, f), raiz)
                o = os.path.join(sal, dst, rel + '_x')
                if os.path.isdir(o): continue
                r = subprocess.run([PT, 'extract', os.path.join(dp, f), o, '-r'], stdin=subprocess.DEVNULL,
                                   capture_output=True, text=True)
                print(dst, rel, 'FALLO' if r.returncode else 'ok', flush=True)


def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()


def ocr(sal):
    import numpy as np
    from PIL import Image
    from rapidocr_onnxruntime import RapidOCR
    from spylls.hunspell import Dictionary
    D = os.path.join(AQUI, 'diccionario_es')
    es_d, en_d = Dictionary.from_files(D + '/es'), Dictionary.from_files(D + '/en')
    O = os.path.join(sal, 'ocr.json')
    hecho = json.load(open(O, encoding='utf-8')) if os.path.exists(O) else {}
    cambiadas = []
    for dp, _, fs in os.walk(os.path.join(sal, 'es')):
        for f in fs:
            if not f.lower().endswith('.dds'): continue
            p = os.path.join(dp, f); rel = os.path.relpath(p, os.path.join(sal, 'es'))
            q = os.path.join(sal, 'en', rel)
            if os.path.exists(q) and md5(p) != md5(q): cambiadas.append(rel)
    print('texturas cambiadas', len(cambiadas), flush=True)
    eng = RapidOCR()
    for n, rel in enumerate(cambiadas):
        if rel in hecho: continue
        try:
            im = Image.open(os.path.join(sal, 'es', rel)).convert('RGBA')
        except Exception as e:
            hecho[rel] = {'error': str(e)[:80]}; continue
        txt = []
        for fondo in ((0, 0, 0, 255), (255, 255, 255, 255)):
            b = Image.new('RGBA', im.size, fondo); b.alpha_composite(im)
            r, _ = eng(np.array(b.convert('RGB')))
            txt += [x[1] for x in (r or []) if x[2] > 0.6]
        hecho[rel] = {'texto': sorted(set(txt))}
        if n % 25 == 0:
            json.dump(hecho, open(O, 'w', encoding='utf-8'), ensure_ascii=False); print(n, rel, flush=True)
    json.dump(hecho, open(O, 'w', encoding='utf-8'), ensure_ascii=False)
    cache = {}
    with open(os.path.join(sal, 'ingles.txt'), 'w', encoding='utf-8') as fh:
        for rel, v in sorted(hecho.items()):
            malas = []
            for t in v.get('texto', []):
                for w in re.findall(r"[A-Za-z]{3,}", t):
                    lw = w.lower()
                    if lw not in cache: cache[lw] = (not es_d.lookup(lw)) and en_d.lookup(lw)
                    if cache[lw]: malas.append(w)
            if malas or 'error' in v:
                fh.write(f"{rel}\t{' '.join(malas) or v.get('error')}\t{' | '.join(v.get('texto', []))[:200]}\n")
    print('listo', flush=True)


if __name__ == '__main__':
    if sys.argv[1] == 'extraer': extraer(*sys.argv[2:5])
    else: ocr(sys.argv[2])
