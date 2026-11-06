# Revisión v1.0.5 (05-11-2026)

Programas usados para la revisión que pidió un comentario en Steam («diálogos sin traducir» y «género mal»).
Resultado: 589 frases corregidas (`correcciones.json`, con inglés, antes, ahora y motivo) y 7 imágenes rehechas.

| Programa | Qué hace |
|---|---|
| `revision_steam.py` | Frases en inglés que quedan y candidatos de género |
| `genero_lotes.py` | Lotes con el contexto de cada escena; en el Y5 saca QUIÉN HABLA del `.msg` japonés (210 = protagonista, 255 = el otro) |
| `genero_y5_votos.py`, `genero_y5_prota.py` | Incoherencias de género por conversación, sin IA (luego revisadas a mano) |
| `genero_revisar.py` | Revisor con IA gratuita (Gemini/OpenRouter). Ojo: se equivoca; todo cambio se revisó a mano |
| `ortografia.py`, `ingles_colado.py`, `ingles_colado2.py` | Palabras que no existen e inglés metido en el español (diccionarios hunspell es-MX y en de github.com/wooorm/dictionaries, en `diccionario_es/`) |
| `desplazados.py` | Traducciones corridas una fila |
| `informe_queda_ingles.py` | Informe de lo que queda en inglés por regla y de los errores corregidos |
| `imagenes_final_ocr.py`, `ocr_cajas.py`, `imagenes_v105.py`, `meter_v105.sh` | OCR de las imágenes del paquete final, rehacer las que tienen inglés y meterlas en el `.par` |
| `correcciones_y5.py`, `poner_en_csv.py`, `v105_armar_y_comprobar.sh` | Correcciones, ponerlas en `textos.csv` y armar + comprobar en los archivos armados |

Las rutas `C:/Mods/...` son las del equipo donde se hizo; cámbialas por las tuyas.
