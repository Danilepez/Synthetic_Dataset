# Léxico de Chulupi Lang (`data/lexicon/`)

Esta carpeta almacena los diccionarios versionados (`CH-309`) y la lista de palabras reales de aymara usada como filtro (`CH-306`).

## Archivos actuales

- `lexico_chulupi.csv`: léxico inicial v1.0 (93 entradas curadas que cubren las 13 clases semánticas de `CH-406` y las 4 categorías verbales), con raíces inventadas generadas mediante semilla fija (`20261119`) y filtro `modo_filtro="guia"`.

## Próximos insumos del equipo (Rol 1)

1. **`lexico_sin_raices.csv`** (~3.130 entradas objetivo, ver `CH-402` y `CH-407` en `docs/especificacion/artificial_lang_spec.md`):
   - Debe conservar exactamente las 21 columnas de `CH-402` en UTF-8 (NFC), dejando `raiz` y `silabas` vacías para que las rellene el generador de raíces (§3).
2. **`palabras_reales.txt`** (`CH-306`):
   - Tokens del lado aymara del conjunto *train* de AmericasNLP (uno por línea), para pasar el generador de raíces de `modo_filtro="guia"` (umbral 1) a `modo_filtro="corpus"` (umbral 5).

> **Importante (`CH-309`):** al cambiar el léxico o pasar a `modo_filtro="corpus"`, se debe subir `VERSION_LEXICO` (p. ej. `"2.0"`) y regenerar todos los datasets en una nueva subcarpeta dentro de `data/synthetic/`.

## Léxico de producción v1.0 (generador v1.1.2, rama `dev/mazen`)

- `lexico_sin_raices.csv`: 2.793 entradas (ids desde `L10001`), con la columna `admite_ben` de la v1.1.2 (22 columnas). Se aceptan 497 verbos en lugar de 800 (desviación de CH-407 anotada en `docs/decisiones/PREGUNTAS.md`).
- `REVISAR_lexico.md`: qué revisar del léxico, por prioridad.
- `palabras_reales.txt`: 43.437 palabras reales (dataset de 18k y guía). Filtro CH-306 en modo **"corpus"** (umbral 5).
- `lexico_con_raices_v1.0.csv` y `.json`: el diccionario con sus raíces, generado por el notebook y fijado para la versión 1.0. El notebook lo reutiliza en cada ejecución; para regenerar las raíces hay que subir `VERSION_LEXICO`.
- `conjugaciones.csv`: conjugaciones del español de los 498 verbos. Es un borrador automático: cada fila tiene `revisado = n` hasta que alguien la revisa y la pone en `s`. El notebook nunca cambia una fila que ya existe.
