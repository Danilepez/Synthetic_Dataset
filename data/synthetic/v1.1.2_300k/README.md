# Dataset sintético v1.1.2 + R23 — 301.787 pares

Generado con `notebooks/chulupi_generador.ipynb` en la rama `dev/Camilo`: especificación **1.1.2**, léxico **1.0** (mismas raíces que `v1.1.2_100k`), filtro de raíces en modo "corpus", capa de realismo **R23** (`data/lexicon/realismo.yaml`) y semilla `20261126`.

| Archivo | Contenido |
|---|---|
| `chulupi_modo_B.tsv` | `src` (Chulupi modo B: raíces inventadas + sufijos reales del aymara) → `tgt` (español) → `id` del par |
| `chulupi_modo_A.tsv` | Lo mismo en modo A (raíces y sufijos inventados): la versión de control |
| `chulupi_dataset_300k.jsonl.gz` | Formato maestro CH-1301, comprimido: un par por línea con la idea, B, A, español, `palabras_b` y las reglas `dv`. Se abre con `gunzip -k` o con `pandas.read_json(..., lines=True, compression="gzip")`. |
| `informe.md` | Resultado de las 31 verificaciones (V01–V31), distribuciones frente a `pesos.yaml`, cobertura y tiempos |

## Cómo se obtuvo

- Se pidieron 360.000 ideas por cuotas (CH-1104), más 586 ideas extra para que cada palabra del léxico aparezca al menos 20 veces (CH-404).
- Se descartaron 58.799 ideas repetidas (V27). Quedan **301.787 pares**.
- **0 errores** en las verificaciones de tipo E. Las 128 pruebas previas pasan (124 de `dev/mazen` y 4 de la capa de realismo).
- Tiempo total: 37 minutos en una computadora con 12 GB de RAM.

## Qué cambia frente a `v1.1.2_100k`

- **Capa de realismo R23.** Cada verbo acepta solo los objetos abstractos, documentos, fenómenos e instrumentos que tienen sentido con él. También se restringen los casos de lugar de los verbos de movimiento, los adjetivos de los abstractos, la compañía, la causa y el beneficiario. Quedan **2.213 entradas** en uso de las 2.793 del léxico; las demás no tenían ningún uso natural. Ninguna raíz cambió.
- **Léxico revisado** (`src/chulupi/revision_lexico.py`). Se corrigieron las clases de 101 adjetivos y de 46 verbos, y los femeninos de mejor y peor.
- **Conjugaciones corregidas y revisadas.** Se compararon con verbecc y se corrigieron 21 filas en 18 verbos.
- **Concordancia de "nosotros"**: "Somos periodistas", no "Somos periodista".
- **Una traducción por oración (V26).** Salen 5 verbos (enamorarse, hervir, quedarse, transitar, trasladarse) cuya 3.ª persona coincidía con un nombre o un adjetivo.
- **Reglas [DERIVADA]**: 49,5 % de los pares (tope del 50 %). En el 100k era el 50,1 %.

En muestras de 100 a 150 oraciones revisadas a mano, las oraciones absurdas o con errores bajaron del **35 %** (100k) a cerca del **11 %**. Es una revisión del equipo, no de un hablante nativo.

## Avisos (no bloquean)

- **V28:** "ser", "estar" y "tener" salen algo por debajo de sus pesos (por ejemplo, `ser.afirmativa` 3,0 % frente a 6 %). Sus frases son cortas y se repiten, así que muchas se descartan como duplicadas.
- **V29:** 15 nombres de clase `tiempo` (semana, lunes, marzo…) aparecen entre 7 y 13 veces, no 20. Solo caben en UNTIL o en "Esa es una…".

## Distribución

| Tipo | % | Tiempo (verbales) | % | Persona | % |
|---|---|---|---|---|---|
| verbo, afirmativa | 47,7 | SIMP | 43,2 | 3.ª | 50,1 |
| verbo, negativa | 15,3 | FUT | 27,6 | 1.ª | 18,1 |
| verbo, pregunta sí/no | 11,4 | REM.L | 16,6 | 2.ª | 17,6 |
| verbo, pregunta de información | 9,1 | REM.C | 12,5 | 4.ª | 14,2 |
| tener | 7,4 | | | | |
| estar | 4,8 | | | | |
| ser | 4,3 | | | | |

En promedio, 3,6 palabras por oración aymara y 5,8 en español.
