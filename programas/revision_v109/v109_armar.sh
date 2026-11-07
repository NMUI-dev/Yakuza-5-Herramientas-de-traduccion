#!/bin/bash
# (claude2, 06-11-2026) Arma la v1.0.9 del Y5 con la herramienta pública: copia entrega_v108 -> entrega_v109, pone las
# correcciones (trabajo/revision_0711b/datos_v109.py) y aplica. Luego: trabajo/revision_0711b/comprobar_v109.sh
# Uso: bash herramientas/v109_armar.sh
set -e
Y=/c/Mods/yakuza5; H="$Y/entrega_v109/Herramientas para traduccion"
ORI="C:/Mods/Entregas/Entregas Yakuza 5/Yakuza 5 - Traduccion al espanol v1.0.8/respaldo_original"
[ -d "$Y/entrega_v109/respaldo_original" ] && { echo "ALTO: entrega_v109 está INSTALADA en Steam (tiene respaldo_original). Quítala antes (opción 2) o borrarías los originales."; exit 1; }
rm -rf "$Y/entrega_v109"; cp -r "$Y/entrega_v108" "$Y/entrega_v109"
rm -rf "$H/__pycache__" "$H/salida" "$Y/entrega_v109/respaldo_original"
python -I -X utf8 "$Y/trabajo/revision_0711b/datos_v109.py"
cd "$H"
python -I -X utf8 -u herramienta_traduccion.py aplicar --ingles "$ORI" > "$Y/trabajo/v109_aplicar.log" 2>&1
sed -n 3p "$Y/trabajo/v109_aplicar.log"; sed -n 3p "$Y/trabajo/v108_aplicar.log"
cp -r salida/data/. "$Y/entrega_v109/archivos/data/"
python -I -X utf8 "$Y/trabajo/revision_0711b/version_v109.py"
echo "armada v1.0.9"
