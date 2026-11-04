# Yakuza 5 Remastered: herramientas y guía para traducir

Todo lo necesario para corregir la traducción al español de Yakuza 5 Remastered, pasarla a otro idioma o traducir otro
juego de la saga. **Incluye los `.exe`**, así que no hay que descargar nada más que Python.

**Para jugar no hace falta nada de esto:** descarga la
[traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish/releases/latest).

## Empieza aquí

**[Guía paso a paso](GUIA_PASO_A_PASO.md)**: cómo usar todo, cuánto hay que traducir, dónde guarda el texto el juego, todos
los errores que tuvimos y qué revisar antes de publicar.

En resumen:

1. Descarga y descomprime la [traducción](https://github.com/NMUI-dev/Yakuza-5-Remastered-Espa-ol-Spanish/releases/latest).
2. Descomprime este repositorio **dentro** de esa carpeta.
3. Instala [Python 3](https://www.python.org) y marca **Add python.exe to PATH**.
4. Doble clic en `EXTRAER textos.bat`.
5. Corrige la columna `espanol` de `trabajo\textos.csv`.
6. Doble clic en `APLICAR textos.bat`.
7. Instala con `INSTALAR o QUITAR.bat`, en la carpeta de la traducción.

## Las cifras

| | |
|---|--:|
| Textos distintos | 71.848 |
| Veces que aparecen en el juego | 154.940 |
| Letras en inglés | 3.950.902 |
| Imágenes `.dds` en los archivos que se tocan | 4.800 |
| Imágenes traducidas | 1.213 |
| Archivos del juego que cambian | 35 |

## Qué hay aquí

| Archivo | Para qué |
|---|---|
| `GUIA_PASO_A_PASO.md` | La guía completa |
| `COMO_USAR.txt` | Resumen del programa de textos |
| `HISTORIAL_DEL_TRABAJO.txt` | Diario de cómo se hizo la traducción |
| `EXTRAER textos.bat`, `APLICAR textos.bat` | Sacan los textos a una hoja y los vuelven a meter |
| `herramienta_traduccion.py` | El programa que usan esos `.bat` |
| `datos/` | La traducción actual |
| `programas/contar_datos.py` | Cuenta textos, imágenes y archivos cambiados |
| `programas/dds_formato.py` | Dice el formato de una imagen `.dds` y cómo guardarla igual |
| `programas/ParTool/` | Abre y rearma los `.par` |
| `programas/texconv/` | Convierte imágenes `.dds` |
| `programas/reARMP/` | Lee tablas ARMP |

Este repositorio no lleva archivos del juego enteros, así que necesitas tu propia copia. Tampoco se suben `trabajo/` ni
`salida/`, las carpetas que se crean al usarlo.

## Programas incluidos

Son de sus autores. Se incluyen sin cambios, con su licencia al lado.

| Programa | Autor | Licencia | SHA-256 |
|---|---|---|---|
| [ParTool 1.3.4](https://github.com/Kaplas80/ParManager/releases/tag/v1.3.4) (ParManager) | Kaplas80 | MIT | `b798027a243229c04741e491abb1f92ae4cc7a379c0cba31b81446f9be4e5b3f` |
| [texconv may2026](https://github.com/microsoft/DirectXTex/releases/tag/may2026) (DirectXTex) | Microsoft | MIT | `dcfdec10244e02cf5037fba089c55fb7e1326b1c8181742d77d15fa5cb5eef06` |
| [reARMP](https://github.com/Ret-HZ/reARMP) | Ret-HZ | GPL-2.0 | |

Si el antivirus avisa, comprueba la SHA-256 con `certutil -hashfile <archivo> SHA256` o descarga el programa de su autor.

## Avisos

- Mod no oficial, gratuito y sin fines de lucro. **Prohibido venderlo.**
- Hecho con IA y supervisado por una persona. No está afiliado a SEGA. Más detalles en [AVISO.txt](AVISO.txt).
- El código propio es MIT ([LICENSE](LICENSE)). Yakuza y sus textos e imágenes son de SEGA.

## English

Tools and a step-by-step guide (in Spanish) to edit the Spanish fan translation of *Yakuza 5 Remastered*, or to translate
it or another game in the series. ParTool and texconv are included. You need your own copy of the game.
