#!/bin/bash
# (05-11-2026) Arma la v1.0.5 del Y5 con la herramienta pública y comprueba en los ARCHIVOS ARMADOS que están todas las
# correcciones (trabajo/revision_steam_0511/correcciones.json) y que no queda ninguna palabra rota conocida.
# Uso: bash herramientas/v105_armar_y_comprobar.sh
set -e
Y=/c/Mods/yakuza5; H="$Y/entrega_v105/Herramientas para traduccion"
ORI="C:/Mods/Entregas/Entregas Yakuza 5/Yakuza 5 - Traduccion al espanol v1.0.4/respaldo_original"
cd "$H"
cp "$Y/trabajo/revision_steam_0511/textos_v105_previsto.csv" trabajo/textos.csv 2>/dev/null || true
python -I "$Y/trabajo/revision_steam_0511/poner_en_csv.py"
rm -rf salida
PYTHONIOENCODING=utf-8 python -u herramienta_traduccion.py aplicar --ingles "$ORI" > "$Y/trabajo/v105_aplicar.log" 2>&1
sed -n 3p "$Y/trabajo/v105_aplicar.log"
rm -rf "$Y/entrega_v105/archivos/data"; cp -r "$Y/entrega_v104/archivos/data" "$Y/entrega_v105/archivos/data"
cp -r salida/data/. "$Y/entrega_v105/archivos/data/"
cd "$Y/trabajo/v105_check"; rm -rf x
for p in wdr_par_en/wdr.par wdr_par_en/common.par bootpar/boot_en.par pausepar/pause_en.par staypar/stay_en.par auth/subtitle.par; do
  "$Y/herramientas/partool/ParTool.exe" extract "C:/Mods/yakuza5/entrega_v105/archivos/data/$p" "x/$(echo $p | tr '/' '_')" -r < /dev/null > /dev/null 2>&1
done
cp -r "$Y/entrega_v105/archivos/data/minigame_en" "$Y/entrega_v105/archivos/data/scenario_en" "$Y/entrega_v105/archivos/data/db.devil" x/
python -I comprobar.py
echo "Kaz-nee en archivos armados (pac/vivos): $(grep -rlac 'Kaz-nee' x/wdr_par_en_wdr.par/wdr_en/pac 2>/dev/null | wc -l) archivos"
