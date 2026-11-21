# Traductor Aymara Boliviano → Español (Preentrenamiento con Lengua Aglutinante Artificial — Chulupi Lang)

Repositorio de investigación para evaluar si el entrenamiento previo con una lengua aglutinante sintética controlada (**Chulupi Lang**, modelada sobre la morfología y sintaxis del aymara boliviano normalizado) mejora la traducción automática **aymara boliviano → español** en escenarios de bajos recursos.

---

## Generador v1.1.2 (rama `dev/mazen`)

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Danilepez/Synthetic_Dataset/blob/dev/mazen/notebooks/chulupi_generador.ipynb)

Notebook ejecutable que genera el dataset sintético a partir de la **especificación v1.1.2** y del léxico de producción (2.793 entradas). Antes de generar, comprueba que todo cumple la especificación (124 pruebas) y, después, revisa cada par con la lista V01–V31 (§13).

### Cómo ejecutarlo en Google Colab

1. Pulsa el botón **Abrir en Colab** de arriba.
2. *Entorno de ejecución → Ejecutar todo*. El notebook descarga este repositorio (rama `dev/mazen`) y usa sus archivos: no hay que subir nada.
3. Tarda unos minutos (en local, unos 3). Cada sección termina con "✔ … pruebas en verde" y la sección 11 con "Sin errores E".
4. Los resultados quedan en `/content/Synthetic_Dataset/salida/pares/` (panel de archivos de Colab). Se borran al cerrar la sesión: descárgalos si los necesitas.

Para solo estudiar el código y correr las pruebas sin generar, pon `GENERAR = False` en la celda de parámetros (0.2): tarda menos de un minuto.

### Dónde está cada cosa

| Ruta | Qué es |
|---|---|
| `notebooks/chulupi_generador.ipynb` | El generador. 12 secciones, cada una explicada en español: alfabeto, motor, léxico, raíces, español, oraciones, ideas, generación, verificación y uso. |
| `docs/specification/chulupi_lang_spec.md` | Especificación **v1.1.2** (la que usa este notebook). Cada regla tiene un código `CH-xxx`. |
| `docs/decisiones/PREGUNTAS.md` | Preguntas abiertas y decisiones tomadas: qué se interpretó, qué se corrigió y por qué. |
| `tests/casos_prueba.json` | Los 40 casos de oración (C01–C40, CH-1201). |
| `tests/regresion_ch710.json` | Los 102 casos de regresión con raíces reales (CH-710). |
| `data/lexicon/lexico_sin_raices.csv` | Léxico de producción (rol 1): 2.793 entradas, sin raíces. |
| `data/lexicon/REVISAR_lexico.md` | Qué revisar del léxico, por prioridad. |
| `data/lexicon/palabras_reales.txt` | 43.437 palabras reales de aymara (filtro CH-306, modo "corpus"). |
| `data/lexicon/conjugaciones.csv` | Conjugaciones del español (borrador automático, `revisado = n`: hay que revisarlas). |
| `data/lexicon/lexico_con_raices_v1.0.csv` (+ `.json`) | El diccionario con sus raíces inventadas, fijo para la versión 1.0 del léxico (CH-309). |
| `data/synthetic/v1.1.2_100k/` | El dataset generado: 100.523 pares verificados (ver su `README.md`). |
| `src/chulupi/prototipo/` | Prototipo de referencia en Python que entregó la especificación (el notebook reutiliza su lógica). |

### Orden recomendado para estudiarlo

1. Este README y `data/synthetic/v1.1.2_100k/README.md` (qué se produce).
2. `docs/specification/chulupi_lang_spec.md`, §0 (resumen) y los ejemplos de cada regla.
3. El notebook, sección por sección. Cada sección empieza con "Qué hace", sus reglas `CH-xxx`, qué entra, qué sale y un ejemplo.
4. `docs/decisiones/PREGUNTAS.md`, para entender las decisiones y lo que falta decidir.

### Relación con la versión v1.1

Los archivos de la v1.1 (`notebooks/generador_chulupi_colab.ipynb`, `docs/specification/artificial_lang_spec.md`, `data/lexicon/lexico_chulupi.csv` y `data/synthetic/v1.1_1k/`) siguen en el repositorio sin cambios. La v1.1.2 añade, entre otras cosas, el léxico de producción, el filtro "corpus", "el agua" (CH-1008) y las restricciones R21–R22; el detalle está en la cabecera de la especificación y en `PREGUNTAS.md`.

### Pendiente antes de entrenar con estos datos

- Revisar `data/lexicon/conjugaciones.csv` (2.490 filas con `revisado = n`).
- Revisar las clases del léxico que dan combinaciones raras ("niños largos", "el pez toma cerveza"); ver `REVISAR_lexico.md`.
- La especificación 1.1.3 todavía no se aplicó (`PREGUNTAS.md`, P-17).

---

## Arquitectura del repositorio

```text
.
├── docs/                                # Documentación, diseño experimental y referencias
│   ├── propuesta/
│   │   └── Propuesta_validada_Aymara_Espanol.docx
│   ├── especificacion/
│   │   ├── guia_estructural_aymara_v3.md    # Fuente lingüística (Hardman L1 + ILCNA-IPELC L2)
│   │   └── artificial_lang_spec.md          # Especificación oficial de Chulupi Lang v1.1
│   └── referencias/
│       └── 2406.09414v2.pdf                 # Depth Anything V2 (referencia conceptual sintético → real)
│
├── notebooks/                           # Notebooks autocontenidos para Google Colab
│   └── generador_chulupi_colab.ipynb        # Generador completo + pruebas CH-710, C01-C40 y V01-V31
│
├── src/                                 # Código Python modular (próximas fases)
│   ├── chulupi/                             # Motor y generador en módulos .py
│   ├── training/                            # Entrenamiento (NLLB-200, LoRA, preentrenamiento sintético)
│   └── evaluation/                          # Evaluación reproducible (SacreBLEU: chrF++, BLEU, ablaciones)
│
├── data/
│   ├── lexicon/                         # Diccionarios versionados (CH-309) y listas de palabras reales
│   │   ├── lexico_chulupi.csv               # Diccionario inicial v1.0 (93 entradas con raíces fijas)
│   │   └── README.md                        # Instrucciones para el Rol 1 (léxico completo ~3.130 entradas)
│   ├── synthetic/                       # Datasets sintéticos versionados por especificación y tamaño
│   │   └── v1.1_1k/
│   │       ├── chulupi_dataset_1k.jsonl     # Formato maestro oficial CH-1301 (idea, B, A, ES, palabras_b, dv)
│   │       ├── chulupi_modo_B_1000.tsv      # Pares Modo B (raíz inventada + sufijos aymaras) → Español
│   │       └── chulupi_modo_A_1000.tsv      # Pares Modo A (raíz y sufijos totalmente inventados) → Español
│   ├── real/                            # Corpus reales de aymara boliviano (AmericasNLP + curación humana)
│   │   ├── raw/                             # Datos originales sin modificar (con metadatos de origen/licencia)
│   │   └── processed/                       # Datos normalizados a la ortografía L2 (NFC, apóstrofo U+0027)
│   └── splits/                          # Particiones fijas train / dev / test bloqueadas (sin fuga de datos)
│
├── tests/                               # Pruebas automáticas (CH-710, C01-C40, verificador V01-V31)
└── experiments/                         # Resultados, configuraciones, tablas de métricas y ablaciones
```

---

## Guía rápida por rol

### 1. Generar o regenerar el dataset sintético (Google Colab)
1. Abrir `notebooks/generador_chulupi_colab.ipynb` en Google Colab.
2. Ejecutar **Entorno de ejecución → Ejecutar todo** (`Ctrl+F9`).
3. El notebook verifica automáticamente antes de generar:
   - **102/102** casos de regresión con raíces reales (`CH-710`, igualdad en Modo B y paralelismo en Modo A).
   - **64/64** celdas verbales de `paradigmas.yaml` (§8).
   - **40/40** casos oficiales de oración (`C01`–`C40`, incluidos los 17 `[ATESTIGUADO]` de L2).
   - Batería completa **`V01`–`V31`** (`CH-1302`) sobre el dataset generado.
4. Guardar cada nueva corrida en su carpeta versionada dentro de `data/synthetic/` (por ejemplo `data/synthetic/v1.1_50k/`).

### 2. Rol 1 — Léxico y filtro de palabras reales
- Subir `lexico_sin_raices.csv` (~3.130 entradas según `CH-402` y `CH-407`) a `data/lexicon/`.
- Subir `palabras_reales.txt` (tokens del lado aymara del *train* de AmericasNLP) a `data/lexicon/` para activar `modo_filtro="corpus"` (`CH-306`).
- **Regla de versionado (`CH-309`):** nunca editar raíces a mano en `lexico_chulupi.csv`. Cualquier cambio exige subir la versión del léxico y regenerar el dataset sintético completo.

### 3. Datos reales y particiones (`data/real/` y `data/splits/`)
- Conservar los archivos originales intactos en `data/real/raw/` con procedencia y licencia documentadas.
- Bloquear `train`/`dev`/`test` en `data/splits/` **antes** de hacer entrenamiento, aumento de datos o pseudo-etiquetado. El conjunto `test` nunca se usa para tomar decisiones de desarrollo.

### 4. Entrenamiento y evaluación (`src/` y `experiments/`)
- No subir checkpoints pesados (`.pt`, `.bin`, `.safetensors`) a Git; están bloqueados en `.gitignore`. Guardar modelos en Drive o Hugging Face Hub y versionar en `experiments/` solo configuraciones, semillas y métricas reproducibles (SacreBLEU `chrF++` / `BLEU`).

---

## Convenciones del repositorio

- **Codificación:** todos los textos (`.md`, `.csv`, `.tsv`, `.jsonl`) en **UTF-8 (NFC)** con apóstrofo interno `'` (`U+0027`, `CH-102`).
- **Inmutabilidad de versiones:** no sobrescribir una versión publicada en `data/synthetic/`; crear una nueva subcarpeta (`v1.1_10k`, `v1.2_50k`, etc.).
- **Ramas de trabajo:** trabajar cambios nuevos en ramas (`feat/...`, `data/...`, `exp/...`) y hacer *Pull Request* hacia `main`.
