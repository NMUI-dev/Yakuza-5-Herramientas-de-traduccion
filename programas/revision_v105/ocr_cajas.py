# -*- coding: utf-8 -*-
"""Cajas OCR (x0,y0,x1,y1,texto,conf) de una textura .dds sobre fondo negro y blanco. python ocr_cajas.py <dds> [...]"""
import sys, numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
sys.stdout.reconfigure(encoding='utf-8')
eng = RapidOCR()
for p in sys.argv[1:]:
    im = Image.open(p).convert('RGBA'); vistos = set()
    print('##', p.replace(chr(92), '/').split('/')[-1], im.size)
    for fondo in ((0, 0, 0, 255), (255, 255, 255, 255)):
        b = Image.new('RGBA', im.size, fondo); b.alpha_composite(im)
        r, _ = eng(np.array(b.convert('RGB')))
        for box, t, c in r or []:
            xs = [q[0] for q in box]; ys = [q[1] for q in box]
            k = (round(min(xs) / 8), round(min(ys) / 8), t)
            if k in vistos or c < 0.5: continue
            vistos.add(k); print(int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys)), repr(t), round(c, 2))
