#!/bin/bash
# (claude2, 06-11-2026) Extrae los .par de texto de entrega_v109 y busca cada corrección de la v1.0.9 en los archivos
# armados (trabajo/v109_check/comprobar.py). Uso: bash trabajo/revision_0611b/comprobar_v108.sh
Y=/c/Mods/yakuza5
cd "$Y/trabajo/v109_check"; rm -rf x
for p in wdr_par_en/wdr.par wdr_par_en/common.par bootpar/boot_en.par pausepar/pause_en.par staypar/stay_en.par auth/subtitle.par; do
  "$Y/herramientas/partool/ParTool.exe" extract "C:/Mods/yakuza5/entrega_v109/archivos/data/$p" "x/$(echo $p | tr '/' '_')" -r < /dev/null > /dev/null 2>&1
done
cp -r "$Y/entrega_v109/archivos/data/minigame_en" "$Y/entrega_v109/archivos/data/scenario_en" "$Y/entrega_v109/archivos/data/db.devil" x/
python -I -X utf8 comprobar.py
