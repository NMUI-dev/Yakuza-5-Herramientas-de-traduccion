#!/bin/bash
# (05-11-2026) Mete las texturas de imagenes_v105.py (trabajo/imagenes/es_v105/2dpar/ui_en.par_x/surfboard/<pjd>.par/...)
# en 2dpar/ui_en.par del paquete v1.0.5: primero cada .par interior (ParTool add), luego el exterior.
set -e
Y=/c/Mods/yakuza5; PT="$Y/herramientas/partool/ParTool.exe"; W="$Y/trabajo/v105_ui"; NUEVO="$Y/trabajo/imagenes/es_v105/2dpar/ui_en.par_x/surfboard"
UI="$Y/entrega_v105/archivos/data/2dpar/ui_en.par"
[ -f "$W/ui_en_v104.par" ] || { mkdir -p "$W"; cp "$Y/entrega_v104/archivos/data/2dpar/ui_en.par" "$W/ui_en_v104.par"; }
rm -rf "$W/ext" "$W/add" "$W/out"; mkdir -p "$W/add/surfboard" "$W/out"
"$PT" extract "$W/ui_en_v104.par" "$W/ext" < /dev/null > /dev/null
for d in "$NUEVO"/*.par; do
  n=$(basename "$d")
  "$PT" add "$W/ext/surfboard/$n" "$d" "$W/add/surfboard/$n" < /dev/null > "$W/out/$n.log" 2>&1
  echo "$n: $(stat -c %s "$W/ext/surfboard/$n") -> $(stat -c %s "$W/add/surfboard/$n")"
done
"$PT" add "$W/ui_en_v104.par" "$W/add" "$W/out/ui_en.par" < /dev/null > "$W/out/ui_en.log" 2>&1
cp "$W/out/ui_en.par" "$UI"; echo "ui_en.par $(stat -c %s "$W/ui_en_v104.par") -> $(stat -c %s "$UI")"
