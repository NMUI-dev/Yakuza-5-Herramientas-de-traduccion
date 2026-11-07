# (claude1, 06-11-2026) Comprobaciones fijas sobre TODO el español del Y6 (textos.csv v1.0.4): palabras repetidas
# («poco poco»), modismos de España (la guía pide español neutro latinoamericano) y vosotros. Solo marca: se decide a mano.
# Uso: python barrido_fijo.py > barrido_fijo.txt
import csv
import re

csv.field_size_limit(10 ** 9)
import os
TEXTOS = os.environ.get("Y5_TEXTOS", "C:/Mods/yakuza5/entrega_v106/Herramientas para traduccion/trabajo/textos.csv")   # (claude2) Y5 v1.0.6   # Y5_TEXTOS = otro CSV (p. ej. el previsto de la v1.0.7)

# palabras que se repiten a propósito (tartamudeo, énfasis): no se marcan
REPETIR_OK = {"no", "sí", "si", "ja", "je", "ji", "jo", "ah", "eh", "oh", "uh", "mm", "hmm", "ay", "oye", "vamos", "muy",
              "rápido", "más", "ya", "bien", "espera", "corre", "otra", "otro", "hola", "adiós", "gracias", "perdón",
              "ven", "anda", "toc", "tic", "tac", "bla", "pum", "bum", "ding", "dong", "ups", "uf", "puaj", "ey", "hey",
              "dale", "venga", "basta", "alto", "fuera", "mira", "aquí", "allá", "jajaja", "ajá", "eso", "así", "nada"}
ESPANA = [r"\bvosotr[oa]s\b", r"\b(?:sois|estáis|tenéis|queréis|podéis|habéis|vais|hacéis|decís|sabéis)\b",
          r"\b(?:mirad|venid|esperad|callad|escuchad|dejad|salid|corred|tomad|dadme|sentaos|marchaos|largaos|id|"
          r"quietos ahí|haced|decidme|contadme|traed|llevad|parad|vamos a ver si os)\b", r"\bos\b",
          r"\by un cuerno\b", r"\bvale\b(?! la pena)(?! más)(?! mucho)(?! nada)(?! poco)", r"\bguay\b", r"\bmola\b",
          r"\bchaval", r"\bgilipollas\b", r"\bcurr(?:o|ar|ando)\b", r"\bordenador\b", r"\bhostia", r"\bcoñ", r"\bcabrear",
          r"\bmogollón\b", r"\bflipa", r"\bpringad", r"\bcutre\b", r"\bmaj[oa]s?\b", r"\btí[oa]s?\b(?! Kaz)", r"\bvaya tela\b",
          r"\bpaso de\b", r"\bcoger\b", r"\bcog(?:e|es|ió|ido)\b", r"\bzumo\b", r"\bcoche\b", r"\bgafas\b",
          r"\b[Jj]oder\b", r"\b(?:qué|mis|tus) cojones\b", r"\bputo amo\b", r"\bfoll(?!et)",r"\bmead[oa]\b",
          r"\bni de coña\b", r"\ba por\b", r"\bmemeces\b", r"\bmalparid", r"\bpendej", r"\bmamadas?\b",
          r"\b[Hh][aei]h[aei]"]
# (claude2 06-11, Y5) REGLA DEL USUARIO: NUNCA CENSURAR. Solo se marca la exclamación ¡Joder! (España);
# «jodido / no me jodas / que se joda» valen en toda Latinoamérica y no se marcan.
ESPANA_RE = re.compile("|".join("(?:%s)" % p for p in ESPANA), re.I)
REP = re.compile(r"\b(\w{2,})\s+\1\b", re.I)

n_rep = n_esp = 0
for r in csv.DictReader(open(TEXTOS, encoding="utf-8-sig", newline=""), delimiter=";"):
    es = r["espanol"].replace("\r\n", " / ").replace("\n", " / ")
    if not es:
        continue
    for m in REP.finditer(es):
        if m.group(1).lower() in REPETIR_OK or m.group(1).isdigit():
            continue
        n_rep += 1
        print("REPETIDA\t%s\t%s\t%s" % (r["id"], m.group(0), es[:160]))
    for m in ESPANA_RE.finditer(es):
        n_esp += 1
        print("ESPAÑA\t%s\t%s\t%s" % (r["id"], m.group(0), es[:160]))
print("total repetidas", n_rep, "| modismos de España", n_esp)
