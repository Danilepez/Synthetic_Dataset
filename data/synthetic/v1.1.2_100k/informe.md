# Informe de generación

- Especificación: 1.1.2 · léxico: 1.0 (2793 entradas) · semilla: 20261120
- Pedidos: 100,000 · ideas de cobertura (CH-404): 10,564 · generados: 110,564
- Descartados (D): 10,041 · finales en `pares.jsonl`: 100,523
- Tiempo total: 152.9 s (pruebas 6.9 s, ideas 41.1 s, cobertura 58.7 s, pares 17.1 s, verificación por par 27.2 s, verificación del conjunto 1.2 s, escritura 0.7 s)

## Verificaciones (CH-1302)

*Tipo*: **independiente** = se calcula aparte del código que generó el par; **coherencia** = vuelve a ejecutar ese mismo código (lo pide CH-1302): solo detecta que el resultado no se pueda reproducir.

| V | Qué | Acción | Tipo | Resultado |
|---|---|---|---|---|
| V01 | campos de CH-1301 | E | independiente | bien |
| V02 | NFC, apóstrofo, espacios | E | independiente | bien |
| V03 | mayúscula y puntuación | E | independiente | bien |
| V04 | solo letras del alfabeto | E | independiente | bien |
| V05 | fonotáctica de cada palabra | E | independiente | bien |
| V06 | raíces válidas y del léxico | E | independiente | bien |
| V07 | formas prohibidas | E | independiente | bien |
| V08 | orden de sufijos (§6) | E | independiente | bien |
| V09 | reconstrucción en B | E | coherencia | bien |
| V10 | pruebas antes de generar | E | coherencia | bien (sección 10.1) |
| V11 | A con las mismas bases e ids | E | independiente | bien |
| V12 | reconstrucción en A | E | coherencia | bien |
| V13 | A sin formas B | E | independiente | bien |
| V14 | orden de constituyentes | E | independiente | bien |
| V15 | -wa | E | independiente | bien |
| V16 | -xa | E | independiente | bien |
| V17 | negación y preguntas | E | independiente | bien |
| V18 | coordinación | E | independiente | bien |
| V19 | R1–R22 | D | coherencia | bien |
| V20 | compatibilidad semántica | D | coherencia | bien |
| V21 | plural del sujeto | E | independiente | bien |
| V22 | español desde la idea | E | coherencia | bien |
| V23 | tiempo español | E | independiente | bien |
| V24 | pronombre español | E | independiente | bien |
| V25 | concordancia | E | independiente | bien |
| V26 | una traducción por oración | E | independiente | bien |
| V27 | sin duplicados | D | independiente | 10041 casos |
| V28 | distribución ±10 % | A | independiente | 11 casos |
| V29 | cobertura ≥ 20 | A | independiente | 15 casos |
| V30 | reglas DV | A | independiente | 1 casos |
| V31 | raíces frente a palabras reales | E | independiente | bien |

## Distribuciones (V28)

| Marginal | Valor | Peso | Observado | Desvío relativo |
|---|---|---|---|---|
| predicado.modalidad | estar.afirmativa | 0.050 | 0.035 | 30% ⚠ |
| predicado.modalidad | estar.pregunta_info | 0.015 | 0.004 | 76% ⚠ |
| predicado.modalidad | estar.pregunta_si_no | 0.015 | 0.011 | 24% ⚠ |
| predicado.modalidad | ser.afirmativa | 0.060 | 0.044 | 27% ⚠ |
| predicado.modalidad | ser.pregunta_si_no | 0.020 | 0.018 | 12% ⚠ |
| predicado.modalidad | tener.afirmativa | 0.070 | 0.059 | 16% ⚠ |
| predicado.modalidad | tener.pregunta_si_no | 0.020 | 0.019 | 6% |
| predicado.modalidad | verbo.afirmativa | 0.420 | 0.462 | 10% ⚠ |
| predicado.modalidad | verbo.negativa | 0.140 | 0.149 | 7% |
| predicado.modalidad | verbo.pregunta_info | 0.090 | 0.089 | 1% |
| predicado.modalidad | verbo.pregunta_si_no | 0.100 | 0.110 | 10% ⚠ |
| tiempo (general) | SIMP | 0.400 | 0.398 | 0% |
| tiempo (general) | FUT | 0.250 | 0.249 | 0% |
| tiempo (general) | REM.C | 0.150 | 0.151 | 1% |
| tiempo (general) | REM.L | 0.200 | 0.202 | 1% |
| tiempo (negativa) | SIMP | 0.600 | 0.598 | 0% |
| tiempo (negativa) | FUT | 0.400 | 0.402 | 0% |
| persona (general) | 1 | 0.220 | 0.203 | 8% |
| persona (general) | 2 | 0.220 | 0.203 | 8% |
| persona (general) | 3 | 0.400 | 0.444 | 11% ⚠ |
| persona (general) | 4 | 0.160 | 0.150 | 6% |
| persona (REM.C) | 1 | 0.150 | 0.147 | 2% |
| persona (REM.C) | 2 | 0.100 | 0.100 | 0% |
| persona (REM.C) | 3 | 0.600 | 0.607 | 1% |
| persona (REM.C) | 4 | 0.150 | 0.146 | 3% |
| persona (REM.L) | 1 | 0.100 | 0.100 | 0% |
| persona (REM.L) | 2 | 0.100 | 0.098 | 2% |
| persona (REM.L) | 3 | 0.700 | 0.704 | 1% |
| persona (REM.L) | 4 | 0.100 | 0.099 | 1% |
| posicion_wa | verbo | 0.500 | 0.499 | 0% |
| posicion_wa | ninguna | 0.200 | 0.203 | 2% |
| posicion_wa | sujeto | 0.150 | 0.149 | 1% |
| posicion_wa | complemento | 0.150 | 0.149 | 1% |
| categoria_verbo | V_INTR | 0.200 | 0.172 | 14% ⚠ |
| categoria_verbo | V_MOV | 0.250 | 0.235 | 6% |
| categoria_verbo | V_TR | 0.400 | 0.418 | 5% |
| categoria_verbo | V_DITR | 0.150 | 0.175 | 16% ⚠ |
| sujeto plural | True | 0.300 | 0.287 | 4% |
| sujeto plural | False | 0.700 | 0.713 | 2% |

## Reglas derivadas (V30)

| DV | Proporción de pares |
|---|---|
| alguna DV | 50.1% |
| DV-01 | 0.2% |
| DV-02 | 0.8% |
| DV-03 | 10.1% |
| DV-04 | 8.6% |
| DV-05 | 14.4% |
| DV-06 | 8.0% |
| DV-07 | 0.3% |
| DV-08 | 10.6% |
| DV-09 | 1.8% |
| DV-10 | 4.2% |
| DV-11 | 2.7% |
| DV-12 | 1.5% |
| DV-13 | 3.8% |

## Cobertura (V29, CH-404)

Apariciones por entrada: mínimo 8, máximo 5,487. Entradas por debajo de 20: 15.

## Pendientes

- Conjugaciones sin revisar (P-07): 2490 filas de 2490.
- Filtro de palabras reales (CH-306): activo, modo 'corpus' (P-06 abierta).
- Léxico: de producción.
