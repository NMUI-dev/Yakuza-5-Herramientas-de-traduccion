#!/bin/bash
# (claude2, 06-11-2026) Arma la v1.0.7 del Y5 con la herramienta pública: copia entrega_v106 -> entrega_v107, pone las
# correcciones (trabajo/revision_0611b/datos_v107.py) y aplica. Luego: trabajo/revision_0611b/comprobar_v107.sh
# Uso: bash herramientas/v107_armar.sh
set -e
Y=/c/Mods/yakuza5; H="$Y/entrega_v107/Herramientas para traduccion"
ORI="C:/Mods/Entregas/Entregas Yakuza 5/Yakuza 5 - Traduccion al espanol v1.0.6/respaldo_original"
rm -rf "$Y/entrega_v107"; cp -r "$Y/entrega_v106" "$Y/entrega_v107"
rm -rf "$H/__pycache__" "$H/salida"
python -I -X utf8 "$Y/trabajo/revision_0611b/datos_v107.py"
cd "$H"
python -I -X utf8 -u herramienta_traduccion.py aplicar --ingles "$ORI" > "$Y/trabajo/v107_aplicar.log" 2>&1
sed -n 3p "$Y/trabajo/v107_aplicar.log"; sed -n 3p "$Y/trabajo/v106_aplicar.log"
cp -r salida/data/. "$Y/entrega_v107/archivos/data/"
python -I -X utf8 "$Y/trabajo/revision_0611b/version_v107.py"
echo "armada v1.0.7"
