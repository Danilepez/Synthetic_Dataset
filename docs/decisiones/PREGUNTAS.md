# Preguntas abiertas: generador de Chulupi Lang

Cada pregunta da la regla afectada, el problema y una propuesta. Mientras nadie decida otra cosa, el notebook aplica la propuesta.

## Abiertas

### P-02 · `idea.schema.yaml` no es YAML válido (CH-1102)
- **Problema.** Algunas líneas usan `X | Y` para decir "X o Y": `od_coord: [NP, NP] | null`, `adv_t: "id ADV_T" | null`, `ser: {adj: "id ADJ"} | {np: NP}`. Un lector de YAML no las acepta.
- **Propuesta.** En la v1.2, entrecomillar esos valores (`od_coord: "[NP, NP] | null"`). Mientras tanto, el notebook los entrecomilla al leerlos (`cargar_yaml`, sección 1) y lo avisa. Solo cambia la lectura, no el significado.

### P-03 · `excluye` de `slots.yaml` frente a las plantillas ESTAR y TENER (CH-601)
- **Problema 1.** `excluye` tiene `[LOC, AFF]` y `[LOC, Q.INF]`, pero la plantilla ESTAR exige LOC seguido de AFF o Q.INF (`utankthwa`, `kawkinkisa`). Aplicada a todas las palabras, la lista rechaza formas atestiguadas.
- **Problema 2.** El texto de CH-601 dice "LOC solo [lleva] VBLZ.KA". `excluye` no prohíbe LOC + TOP.
- **Propuesta.** `excluye` se aplica solo a las palabras NP_NORMAL, porque ESTAR, TENER y SER ya fijan su estructura. Además se aplica el texto de CH-601: tras LOC solo puede ir VBLZ.KA. En la v1.2, decirlo en `slots.yaml` y añadir `[LOC, TOP]`.

### P-05 · Léxico de prueba frente a léxico de producción (CH-402, CH-1201); afecta a F2 y F3
- **Problema.** `lexico_sin_raices.csv` no está. Según lo pedido, se usan las 25 entradas de §4.1, que ya traen raíz. Los 40 casos de `casos_prueba.json` esperan justo esas raíces (`lisqu`, `ch'ixra`…). Cuando llegue el léxico real, el generador de raíces dará otras y los 40 casos fallarían.
- **Propuesta.** (a) Con el respaldo de §4.1, las raíces de la especificación se conservan y solo se validan (CH-201 a CH-310). (b) Los 40 casos siempre se prueban con un léxico fijo de prueba (§4.1 + LV01–LV18), aparte del léxico de producción.

### P-09 · Demostrativo sujeto de "ser": "eso" o "ese" (CH-1008, regla 1 y regla 5)
- **Problema.** El nuevo ejemplo de la regla 5 dice "eso es pan" (demostrativo neutro). Pero la regla 1 y el ejemplo `Aka-xa chimula-wa.` → "Esta es una casa." hacen que el demostrativo concuerde con el nombre. Con esa regla sale "Ese es pan.".
- **Propuesta.** Se mantiene la concordancia, que es lo que hacen el prototipo y la regla 1: "Ese es pan.". Si el equipo quiere el neutro ("esto / eso / aquello") con nombres no contables, hay que decirlo en una regla.

### P-10 · Transición frente a la cuota de persona (CH-1104, CH-1109)
- **Problema.** CH-1104 fija la persona del sujeto en la cuota. CH-1109 dice que "se elige primero la transición; fija la persona del sujeto". Las dos cosas no pueden pasar a la vez.
- **Propuesta.** Manda la cuota (CH-1104). En SIMP, con un verbo `obj_persona = s`, la transición se sortea solo entre `objeto_3` y las transiciones cuyo sujeto es la persona de la cuota, renormalizando los pesos. Con persona 4 no hay transición. Así, las transiciones salen algo menos que el 7 % cada una.

### P-12 · Adverbio de tiempo con "ser", "estar" y "tener" (CH-901, CH-1011)
- **Problema.** CH-901 dice que en estos predicados "no hay posiciones 4 a 7", así que la posición 3 (tiempo) quedaría permitida. Pero CH-1011 ("sujeto – verbo – predicado") y el español del prototipo no escriben el adverbio: "Yo tengo pan ayer" saldría sin "ayer" en español.
- **Propuesta.** Estos predicados no llevan `adv_t`. El validador lo rechaza (CH-908) y el generador no lo sortea.

### P-11b · Categoría de los nombres fuera del sujeto (CH-402, CH-403)
- **Problema.** `sujeto_clase_humana` (v1.1.2) decide la categoría del sujeto. Otras funciones también aceptan `N_HUM` y `N_NOHUM`: la compañía (COM, `persona|animal`) y CAUSE (`abstracto|persona`). Para ellas no hay pesos.
- **Propuesta.** Las dos categorías pesan lo mismo (0,5 / 0,5) y después se aplica Zipf dentro de la elegida. Si el equipo quiere otros pesos, añadirlos a `pesos.yaml`.

### P-16 · Detalles de la v1.1.2 que se interpretaron
- **Problema.** La especificación 1.1.2 no llegó en el mensaje. Los cambios se escribieron a partir de su descripción. Tres puntos no estaban dichos:
  1. `pasado_remoto` tampoco va con el progresivo, como `pasado` en CH-917.
  2. El lugar de "estar en" (N-LOC-VBLZ.KA) cuenta como frase de lugar: no lleva numeral.
  3. Con un poseedor, la frase lleva POSS.3, así que una frase con UNTIL tampoco lleva poseedor (R10, CH-601).
- **Propuesta.** Confirmar los tres. Si llega el texto de la 1.1.2, comparar con `datos/chulupi_lang_spec.md`.

### P-15 · Duplicados y cobertura con el léxico de producción (V27, V29, CH-404)
- **Datos (léxico de 2.793 entradas, prueba aislada con 10.000 ideas).** CH-404 añade 41.036 ideas de cobertura, ya sin duplicados (revisión 6). V27 descarta 390 duplicados de las ideas por cuotas. Quedan 15 entradas por debajo de 20 apariciones, todas nombres de clase `tiempo` (semana, hora, marzo, lunes…). Solo caben en UNTIL (raíz de 2 sílabas) o en "Esa es X.", y esas ideas se repiten.
- **Efecto.** Con pocas ideas por cuotas, la cobertura domina y V28 avisa en 20 marginales. Con 100.000 ideas pesará mucho menos.
- **Propuesta.** Aceptar el aviso (A) para esas 15 entradas. Si el equipo quiere cubrirlas, hacen falta más funciones para los nombres de `tiempo` (una regla nueva) o quitarlas del léxico.

### P-17 · Especificación 1.1.3 no recibida
- **Problema.** El responsable mencionó cambios de una especificación 1.1.3 (DV-05, `-tayna`, P-15, V26…) "del mensaje anterior". Ese mensaje no llegó a esta sesión, así que no se aplicó ninguno.
- **Propuesta.** Enviar el texto de la 1.1.3. Si cambia sufijos o filtros de raíces (CH-305 a CH-310), hay que subir `VERSION_LEXICO` para regenerar las raíces, que ya están fijadas en `salida/lexico.csv`.

### P-18 · Formas de nombre con dos géneros en el léxico de producción
- **Problema.** Siete formas aparecen en dos entradas con distinto género: `política(s)` (L10004 var / L10315 f), `música` (L10026 var / L10515 f), `corredor(es)` (L10093 var / L10858 m) y `cartera(s)` (L10182 var / L11443 f). Es correcto en español (persona y cosa). Pero en la verificación V25 ("la política…") la concordancia se decide por la forma, no por la entrada.
- **Propuesta.** Dejarlas: V25 acepta cualquiera de los dos géneros de la forma. El rol 1 puede revisarlas al repasar `REVISAR_lexico.md`.

## Decisiones tomadas

- **20-11-2026 · P-06 resuelta (CH-306).** Modo "corpus", con `datos/palabras_reales.txt` (43.437 palabras del dataset de 18k y de la guía) y umbral 5. Es el valor de `MODO_FILTRO` y de `generador_raices.yaml`. Con él, P-14 deja de ser un problema: todas las palabras gramaticales del modo A pasan. Lo decidió el responsable del proyecto.
- **20-11-2026 · Ids de 4 o más cifras (CH-402).** `L0001…` y `L10001…` valen, en la sección 5 y en R22. El léxico de producción usa `L10001…` para no chocar con el de ejemplo. CH-402 lo dice explícitamente. Lo decidió el responsable del proyecto.
- **20-11-2026 · Desviación de CH-407.** El léxico de producción tiene 497 verbos en lugar de 800 (V_INTR 125, V_MOV 64, V_TR 271, V_DITR 37). Se acepta para esta versión. Lo decidió el responsable del proyecto.
- **20-11-2026 · Léxico de producción 1.0.** `datos/lexico_sin_raices.csv` (2.793 entradas). Raíces generadas en modo "corpus" y fijadas en `salida/lexico.csv` + `salida/lexico_version.json`. Las siguientes ejecuciones las conservan (CH-309); para regenerarlas hay que subir `VERSION_LEXICO`.
- **20-11-2026 · Revisión de código, decisiones 5, 9 y 10** (aprobadas por el responsable del proyecto):
  - **5 (CH-903, regla 2).** En una pregunta de información sin sujeto expreso, el adverbio de tiempo lleva `-xa`; con `khiti` como sujeto, no.
  - **9 (CH-1008, regla 9).** Femeninos con *a-* tónica, marcados `ART_EL` en `notas`: "el agua", "un hacha", "del águila"; en plural y con demostrativos, femenino ("las aguas", "esta agua").
  - **10 (CH-912).** Los nombres no contables no llevan numeral ni plural.
  - Las tres se escribieron en la especificación (CH-402, CH-912, CH-1008) y tienen pruebas.
- **20-11-2026 · Revisión de código, correcciones.**
  - "les" con numeral (CH-1009).
  - V26 con pares m/f explícitos.
  - V25 comprueba el adjetivo de "ser", el clítico y solo las palabras de la idea.
  - V13 morfema final y palabras gramaticales.
  - V14–V16 deducidos de los ids, sin la anotación del constructor.
  - El informe dice qué verificaciones son independientes y cuáles de coherencia.
  - Cobertura sobre ideas únicas.
  - Raíces conservadas entre ejecuciones (CH-309).
  - El léxico de producción sin `palabras_reales.txt` se detiene.
  - Parámetro `GENERAR`.
- **20-11-2026 · Especificación 1.1.2** (en `datos/chulupi_lang_spec.md`; ver P-16):
  - INT.QUE en modo A es `sipu` (antes `mulu`, palabra real: "mulu mulu" = gato montés). Cambiado en CH-505, `morfemas.yaml`, CH-906, CH-1011, C32 (`casos_prueba.json`) y `chulupi_motor.py`.
  - ADV_T `pasado_remoto` (CH-401, CH-402, CH-917, CH-1001). "ayer" (`pasado`) solo va con SIMP. Entrada de prueba L0026 "antes", raíz `lasmiq'a` generada por §3 (semilla `semilla_raices + 26`, pasa CH-201 a CH-310). El ejemplo de CH-903 pasa a usar "antes".
  - CAUSE solo con `V_MOV` y `V_INTR` (CH-406).
  - Columna `admite_ben` (CH-402, CH-406): BEN solo si es `s`. En el ejemplo: comprar, cortar y dar `s`; comer y ver `n`.
  - Las frases de lugar no llevan numeral (CH-912).
  - `pesos.yaml`: `sujeto_clase_humana: 0.60`.
  - Lo decidió el responsable del proyecto.
- **20-11-2026 · P-01 resuelta.** La especificación se llama `datos/chulupi_lang_spec.md`, como dice CLAUDE.md. El notebook solo busca ese nombre.
- **20-11-2026 · Prueba del proceso completo.** 100.000 pares con el léxico de ejemplo, en `salida/prueba_lexico_ejemplo/`, marcados "NO USAR PARA ENTRENAR" (campo `uso` y `LEEME.txt`). La carpeta no va al control de versiones. Lo decidió el responsable del proyecto.
- **20-11-2026 · Especificación 1.1.1.** Cambios copiados en `datos/chulupi_lang_spec.md`:
  - CH-406: BEN solo con `V_TR` y `V_DITR`; `V_MOV` y `V_INTR` no llevan objeto indirecto.
  - CH-1103: R21 (un lexema no se repite en la idea) y R22 (solo entradas `L…` del léxico de producción; `LV01`–`LV18` solo para pruebas).
  - `pesos.yaml`: `categoria_verbo` y `oi_otros` → `oi_V_TR`.
  - El notebook comprueba la versión 1.1.1. Lo decidió el responsable del proyecto.
- **20-11-2026 · P-11 (verbos).** Primero la categoría con `categoria_verbo`, después Zipf dentro de ella. Los nombres siguen abiertos (P-11). Lo decidió el responsable del proyecto.
- **20-11-2026 · P-13 confirmada.** COM es instrumento si el verbo tiene `instr_clases`. Si no, es compañía, solo con `V_MOV` o `V_INTR` y sujeto `persona` (también `khiti`, CH-906). Si no cabe ninguna de las dos, no hay COM. Una prueba lo comprueba en 10.000 ideas.
- **20-11-2026 · P-07 resuelta (§10).** El borrador de las conjugaciones forma parte de la tarea. La celda 7.2 genera `datos/conjugaciones.csv` con un conjugador propio, sin bibliotecas: regulares, cambios de vocal, cambios de escritura y una tabla de irregulares. Cada fila nueva lleva `revisado = n`; el notebook avisa sin detenerse, y las filas que ya existen no se tocan nunca. Control: para los 10 verbos del prototipo da exactamente sus formas. El error claro queda solo para los verbos que no están en la tabla. Lo decidió el responsable del proyecto.
- **20-11-2026 · P-08 resuelta (CH-1008, regla 5).** Era un error de la especificación; el prototipo tenía razón. La regla 5 pasa a decir: "nombre no humano: 'un / una' si es contable y singular; nada si es plural o no contable". Se corrigió en `datos/chulupi_lang_spec.md` y en el notebook, con una prueba ("Ese es pan."). Lo decidió el responsable del proyecto.
- **20-11-2026 · P-04 resuelta (CH-306).** El equipo entregó `datos/palabras_reales.txt`. La sección 6 aplica el filtro con esa lista. Queda abierto el modo (P-06).
- **20-11-2026 · Lugar de los 40 casos (CH-1201).** Necesitan el constructor de oraciones (sección 8). La sección 4 prueba CH-710. Los 40 casos van al final de la sección 8, y la sección 10 repite todas las pruebas antes de generar. Lo decidió el responsable del proyecto.

## Errores del prototipo corregidos

- **Motor.** Ninguno. El motor (`chulupi_motor.py`) da las mismas salidas que la especificación en los 102 casos de CH-710, los 64 paradigmas y los 16 ejemplos de §7.1.
- **`chulupi_oraciones.py`, `genero_np` (incumplía CH-1010).** Por la precedencia de `or … if … else`, un nombre de género fijo tomaba el `genero` de la idea: `{"n": "L0004", "genero": "m"}` daba "el mujer". Corregido en la sección 7: el campo solo cuenta si el nombre es `var`.
- **`chulupi_oraciones.py`, "ser" + adjetivo (incumplía CH-405).** El adjetivo concordaba con `sujeto.genero`, que no existe en sujetos no humanos: "La casa es rojo". Corregido: con un sujeto nombre, concuerda con el género de ese nombre ("La casa es roja").
- Ninguna de las dos correcciones cambia los 40 casos de CH-1201.
- **`chulupi_oraciones.py`, `-xa` en preguntas sin sujeto (incumplía CH-903, regla 2).** `top = expreso == "ninguno" and inter is None` dejaba sin `-xa` el adverbio en `que_od`, `donde_all` y `quien_oi`. Corregido en la sección 8 (`inter != "quien_suj"`). Tampoco cambia los 40 casos.
- **`chulupi_oraciones.py`, "le" con numeral (incumplía CH-1009).** El clítico miraba solo `plural` y no el numeral: "le doy pan a tres maestros". Corregido en la sección 7.
