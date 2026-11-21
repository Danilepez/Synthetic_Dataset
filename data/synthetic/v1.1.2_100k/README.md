# Dataset sintético v1.1.2 — 100.523 pares

Generado con `notebooks/chulupi_generador.ipynb` (especificación **1.1.2**, léxico **1.0**, modo de filtro "corpus", semilla `20261120`).

| Archivo | Contenido |
|---|---|
| `chulupi_modo_B.tsv` | `src` (Chulupi modo B: raíces inventadas + sufijos reales del aymara) → `tgt` (español) → `id` del par |
| `chulupi_modo_A.tsv` | Lo mismo en modo A (raíces y sufijos inventados): la versión de control |
| `chulupi_dataset_100k.jsonl.gz` | Formato maestro CH-1301, comprimido: un par por línea con la idea, B, A, español, `palabras_b` y las reglas `dv`. Se abre con `gunzip -k chulupi_dataset_100k.jsonl.gz` o con `pandas.read_json(..., lines=True, compression="gzip")`. |
| `informe.md` | Resultado de las 31 verificaciones (V01–V31), distribuciones frente a `pesos.yaml`, cobertura y tiempos |

## Cómo se obtuvo

- 100.000 ideas por cuotas (CH-1104) + 10.564 ideas extra para que cada palabra del léxico aparezca al menos 20 veces (CH-404).
- Se descartaron 10.041 ideas repetidas (V27). Quedan 100.523 pares.
- **0 errores** en las verificaciones de tipo E.

## Avisos (no bloquean)

- **V28:** "ser", "estar" y "tener" salen algo menos de lo que piden los pesos (por ejemplo `estar.pregunta_info` 0,4 % frente a 1,5 %), porque sus frases cortas se repiten y se descartan.
- **V29:** 15 nombres de clase `tiempo` (semana, lunes, marzo…) aparecen entre 8 y 12 veces, no 20.
- **V30:** el 50,1 % de los pares usa alguna regla [DERIVADA], justo en el límite del 50 %.

## Antes de entrenar

Las conjugaciones del español (`data/lexicon/conjugaciones.csv`) son un borrador automático sin revisar. Si se corrige alguna, hay que volver a generar el dataset en una carpeta nueva (por ejemplo `v1.1.2_100k_r2/`): no se sobrescribe una versión publicada.
