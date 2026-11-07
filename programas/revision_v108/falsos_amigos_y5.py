# (claude2, 06-11-2026) Falsos amigos (idea del 2.º ciclo de preguntas): el inglés dice X y el español usa el «parecido»
# que significa otra cosa (actually -> actualmente, realize -> realizar, eventually -> eventualmente...). Solo marca.
# Uso: Y5_TEXTOS=... python -I -X utf8 falsos_amigos_y5.py > falsos_amigos.txt
import csv, os, re, collections
csv.field_size_limit(10 ** 9)
T = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/trabajo/revision_0711/textos_v108_previsto.csv")
PARES = [(r"\bactually\b", r"\bactualmente\b"), (r"\breali[sz]e[sd]?\b|\brealizing\b", r"\breali[zc]"),
         (r"\beventually\b", r"\beventualmente\b"), (r"\blibrar(?:y|ies)\b", r"\blibrer[ií]a"),
         (r"\bembarrass", r"\bembaraz"), (r"\bassum(?:e|ed|ing)\b", r"\basum"), (r"\bsensible\b", r"\bsensible\b"),
         (r"\bterrific\b", r"\bterrible|terror[ií]fic"), (r"\bcarpet\b", r"\bcarpeta"), (r"\bcomprehensive\b", r"\bcomprensiv"),
         (r"\bdisgust", r"\bdisgust"), (r"\bexit\b", r"\b[ée]xito\b"), (r"\bfabric\b", r"\bf[áa]brica\b"),
         (r"\bintroduce", r"\bintroduc"), (r"\bpretend", r"\bpretend"), (r"\bsuccess", r"\bsuceso"),
         (r"\bsympath", r"\bsimp[aá]t"), (r"\bargument\b", r"\bargumento\b"), (r"\bconsistent", r"\bconsistent"),
         (r"\bdeception\b", r"\bdecepci[óo]n\b"), (r"\bcollege\b", r"\bcolegio\b"), (r"\bconstipat", r"\bconstipad"),
         (r"\bmolest", r"\bmolest"), (r"\brecord(?:ed|ing)?\b(?! (?:high|score|time))", r"\brecord(?:ar|é|ó|aste)\b")]
n = collections.Counter()
for r in csv.DictReader(open(T, encoding="utf-8-sig", newline=""), delimiter=";"):
    en, es = r["ingles"], r["espanol"]
    if not es:
        continue
    for a, b in PARES:
        if re.search(a, en, re.I) and re.search(b, es, re.I):
            n[a] += 1
            print("%s\t%s\t%s || %s" % (a, r["id"], en[:110].replace("\n", " / "), es[:120].replace("\n", " / ")))
            break
print("total", sum(n.values()), dict(n))
