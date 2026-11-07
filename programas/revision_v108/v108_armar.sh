#!/bin/bash
# (claude2, 06-11-2026) Arma la v1.0.8 del Y5 con la herramienta pública: copia entrega_v107 -> entrega_v108, pone las
# correcciones (trabajo/revision_0711/datos_v108.py) y aplica. Luego: trabajo/revision_0711/comprobar_v108.sh
# Uso: bash herramientas/v108_armar.sh
set -e
Y=/c/Mods/yakuza5; H="$Y/entrega_v108/Herramientas para traduccion"
ORI="C:/Mods/Entregas/Entregas Yakuza 5/Yakuza 5 - Traduccion al espanol v1.0.7/respaldo_original"
[ -d "$Y/entrega_v108/respaldo_original" ] && { echo "ALTO: entrega_v108 está INSTALADA en Steam (tiene respaldo_original). Quítala antes (opción 2) o borrarías los originales."; exit 1; }
rm -rf "$Y/entrega_v108"; cp -r "$Y/entrega_v107" "$Y/entrega_v108"
rm -rf "$H/__pycache__" "$H/salida" "$Y/entrega_v108/respaldo_original"
python -I -X utf8 "$Y/trabajo/revision_0711/datos_v108.py"
cd "$H"
python -I -X utf8 -u herramienta_traduccion.py aplicar --ingles "$ORI" > "$Y/trabajo/v108_aplicar.log" 2>&1
sed -n 3p "$Y/trabajo/v108_aplicar.log"; sed -n 3p "$Y/trabajo/v107_aplicar.log"
cp -r salida/data/. "$Y/entrega_v108/archivos/data/"
python -I -X utf8 "$Y/trabajo/revision_0711/version_v108.py"
echo "armada v1.0.8"
