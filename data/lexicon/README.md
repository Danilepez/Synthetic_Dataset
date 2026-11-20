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
