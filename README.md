# Traductor Aymara Boliviano → Español (Preentrenamiento con Lengua Aglutinante Artificial — Chulupi Lang)

Repositorio de investigación para evaluar si el entrenamiento previo con una lengua aglutinante sintética controlada (**Chulupi Lang**, modelada sobre la morfología y sintaxis del aymara boliviano normalizado) mejora la traducción automática **aymara boliviano → español** en escenarios de bajos recursos.

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
