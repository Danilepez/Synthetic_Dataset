# Guía estructural del aymara (v3)

**Fuentes**
- **L1** = Hardman, Vásquez y Yapita (2001, 2.ª ed.; 1.ª ed. 1988), *Aymara: Compendio de estructura fonológica y gramatical*, ILCA, La Paz. Fuente de las secciones 0–7 y 9. En v2 se contrastó con el libro completo (PDF de 393 pp.; página impresa = página del PDF − 28).
- **L2** = ILCNA–IPELC, *Aymar Aru Thakhi / Gramática de la lengua aymara* (gramática oficial), 1.ª ed. 2024 (RA 81/2024), versión PDF del 20/03/2025, 272 pp. Fuente de la sección 8, de la 5.2, del 0.2 y de las tablas de contraste 2.1, 3.4 y 4.1. Cubre fonología (pp.39–77), morfología (pp.80–240) y sintaxis (pp.241–255); en este PDF la página impresa coincide con la del PDF.
- *Aymara: Método Fácil* (Yapita) no se usó (PDF escaneado; reservado para ejemplos).

**Convenciones**
- Fuente = página **impresa** del libro (`L1 p.97`).
- Ejemplos: `aymara-segmentado` — GLOSA — "traducción".
- Las formas aymaras se conservan **tal como las escribe cada libro**. Para pasarlas a la escritura oficial, aplica las decisiones D1–D6 y la tabla 8.4.
- L1 segmenta con punto (`chur.t.wa`); aquí se cambió el punto por guion. L1 marca con una *c* o una *v* en subíndice lo que el sufijo exige antes y después (`–cta`, `–vta`; L1 p.67). Al extraer el texto, ese subíndice puede aparecer pegado al sufijo (`–citu` = `-itu` que pide consonante antes).
- `†` = segmentación o glosa del extractor, no del libro. `‡` = análisis propio del revisor (v2), no de ninguno de los dos libros. `FALTA` = el dato no figura en ninguna de las dos fuentes.
- Para ver qué cambió respecto a v1 y v2, consulta la sección 11; las discrepancias sin resolver y las reglas que no deben usarse en el generador están en las secciones 12 y 13.

---

## Decisiones del proyecto (v3, provisionales)

Criterio general (v3): **L2 es la referencia de la ortografía normalizada; L1 es la referencia del análisis morfológico.** Las terminologías y las segmentaciones de los dos libros no se fusionan automáticamente: cuando difieren, se documentan las dos. La columna "Estado" indica si la decisión está confirmada por las fuentes o pendiente de verificación.

| # | Tema | Decisión | Por qué / base | Estado |
|---|---|---|---|---|
| D1 | Ortografía de salida (corpus y generador) | **Alfabeto y normas de L2.** Una forma normalizada solo se da por buena si está atestiguada en L2 o se genera con un paradigma de L2. Las formas de L1 **no** se convierten automáticamente (ver 8.4) | L2 es la norma obligatoria en Bolivia (DS 20227, RM 599/2011; L2 p.71, 73–74) | Confirmada |
| D2 | Vocal larga | En la **escritura**: `ä ï ü` (precompuestos U+00E4, U+00EF, U+00FC). En las glosas de análisis de L1 se conserva su notación `:` | L2 p.46–47 (0 diacríticos combinantes en el PDF). L1 usa `:` al segmentar y admite `¨` (p.73); en su texto corrido escribe `ä` (`muytätaxa`, `mä qillqa`, p.57–58) | Confirmada |
| D3 | Apóstrofo de las glotalizadas | Hay que distinguir dos niveles. **(a) Representación publicada:** L2 imprime `’` (U+2019), ≈2.230 veces frente a 8 `'`; es la forma ortográfica de referencia. **(b) Normalización interna de datos:** el proyecto unifica todo en un solo carácter para que el tokenizador no vea dos palabras distintas. El carácter interno (`'` U+0027 o `’` U+2019) es decisión técnica del proyecto, no regla ortográfica; si se usa `'`, el texto publicado debe poder volver a `’` | L2 (pp.40–41 y todo el libro); L1 usa `'` | Nivel (a) confirmado; carácter interno: decisión técnica |
| D4 | Posesivo 1.ª persona | **Escritura normalizada: `-ja`**, la forma que L2 presenta como marca de 1.ª persona (p.149). **Análisis:** se conservan las variantes de L1 `-xa ~ -ja` y su alomorfo `-:` tras /a/ (p.205). L2 no dice que `-ja` sea "preferida" frente a otras: la da como la marca y menciona las variantes `-xa`, `-ña`, `-ŋa` y, en el sur, `-ya` (p.149) | L2 p.148–149, 173 (`sarañajawa`); L1 p.205 | Confirmada (como norma de L2) |
| D5 | 1.ª persona del tiempo simple: `-ta` (L1) y `-tha` (L2) | **No son variantes gráficas de lo mismo ni se convierten automáticamente.** Se conservan los dos análisis (ver 3.1 y 3.4). Correspondencia **funcional**: ambos marcan sujeto de 1.ª persona en el no-futuro (L1: interacción 1→3) y reaparecen en los tiempos compuestos (L1 `-ya:ta`, `-ta:ta`; L2 `-yätha`, `-tätha`). Diferencias: **(1) forma:** L1 da `/ta/` sin aspiración, idéntico en sonido a 2→3 `-ta` y distinguido de él solo por la morfofonémica (1→3 pierde su vocal; 2→3 la conserva; L1 p.77, 144, 159); L2 da `-tha` aspirado frente a `-ta` de 2.ª persona (p.61, 176). **(2) análisis:** L1 lo trata como una interacción sujeto→objeto (1→3); L2, como marca de sujeto. Ningún libro explica la diferencia de aspiración (dialectal, de transcripción o de análisis). **Para la escritura normalizada se usan las formas de L2** (`churtha`, L2 p.155; `sarthwa`, p.176), generadas desde su paradigma, no convirtiendo cadenas de L1 | L1 p.68, 77, 144, 159; L2 p.61, 155, 176 | Diferencia documentada; origen de la aspiración pendiente |
| D6 | Pérdida de vocales finales | Se distinguen tres niveles (detalle en 5.3). **(a) Elisión morfológica dentro de la palabra**, provocada por el sufijo siguiente: las dos fuentes la describen y la escriben (`chur-t-wa` L1; `lurthwa` L2). Se aplica en la escritura normalizada, **solo con las condiciones documentadas para cada sufijo**. **(b) Pérdida de la vocal final de palabra dentro de la frase** (complemento cero, modificador de 3 o más vocales, verbo nominalizado ante el verbo principal): L1 la describe como regla gramatical y la escribe (p.68, 72, 233); L2 la considera desonorización oral y manda escribir la vocal completa (p.66–70). **En la escritura normalizada se escribe la vocal completa (L2).** Las reglas de L1 se conservan como análisis, no como reglas de escritura. **(c) Realización oral:** no se representa en la escritura normalizada. La frecuencia de una forma en un corpus **no** decide su escritura; el corpus solo sirve para saber qué convención usan los datos y normalizarlos | L1 p.68, 72, 233; L2 p.60, 66–70, 75–77 | Confirmada como norma de L2; la diferencia de análisis queda documentada |
| D7 | Sufijos "dúctiles" de L2 | La ductilidad **no** es alternancia libre. L2 la define como sufijos que "a veces" eliden la vocal previa y "otras veces" no (p.60–61), pero **no da las condiciones**. Por tanto: (1) se documentan las formas atestiguadas en L2 tal como aparecen; (2) **el generador no produce variantes** de estos sufijos hasta que se documenten las condiciones; (3) la clasificación de cada sufijo se marca según su respaldo (ver 5.2). `-pacha`: L2 lo pone en la columna de dúctiles (`taqpacha`, `kimspacha`, `jiwaspacha` frente a `jupapacha`; p.63–64); L1 distingue al menos cuatro `-pacha` y dice que todos los sufijos `-pacha` piden consonante antes (fuertes), y que `taq.pacha` es un tronco fosilizado (p.209, 228). Clasificación de `-pacha` como dúctil: **pendiente de verificación** | L2 p.60–64; L1 p.209, 228 | Pendiente (condiciones no documentadas) |
| D8 | `maya/mä`, `paya/pä`, `khaya/khä` | Las dos formas son **válidas por escrito**, también delante de un nombre (L2 p.57: `Nayaxa pä/paya utanithwa`). La única condición documentada es de **pronunciación**: delante de un nombre se pronuncian `mä`/`pä`, y como numeral suelto `maya`/`paya` (L2 p.43). Esto es una excepción explícita al principio de "una sola forma escrita" de L2 (p.71, 74), igual que la escritura de compuestos (p.54–55). No hay regla documentada para elegir entre las dos al escribir | L2 p.43, 54–55, 57, 71, 74 | Confirmada (sin regla de elección) |
| D9 | Función de `-ru` y glosas | `-ru` **no** se glosa como acusativo. **ALL** = uso relacional: dirección, lugar, propósito, tiempo (siempre con nominales no humanos, y con humanos cuando no corresponden a la flexión). **COMPL.RU** = nominal humano marcado con `-ru` que corresponde a la persona complemento del sufijo de flexión (L1 p.210–211). En L1 ese complemento "suele ser la persona hacia la cual se dirige la acción" (p.211): a menudo es el **destinatario**, no un objeto directo. El objeto directo no personal es el complemento cero (L1 p.233) o, en L2, el caso `-ø` "acusativo" (p.154). L2 llama a `-ru` "complemento indirecto" y dirección (p.155). Con causativo `-ya-`, `-ru` puede marcar al agente (L1 p.212). Otras glosas: `-ti` = NEG en negativas y Q.YN en preguntas; `-ki` = LIM; `-kama` = UNTIL; `-ka-` = INCOMPL también en las negativas (L2 lo llama "negativo", p.65, 232) | L1 p.210–212, 233; L2 p.154–157 | Confirmada |
| D10 | Orden de palabras por defecto en el generador | **SOV** en la oración simple declarativa, con los complementos en el orden tiempo – lugar – objeto indirecto – objeto directo – verbo (L2). L1 describe el orden entre constituyentes como libre (cambia el estilo, no la gramática; p.293–294): esas permutaciones no se generan todavía | L2 p.241, 243, 255; L1 p.293–294 | Confirmada como norma de L2 |
| D11 | Segmentación del plural verbal y del progresivo | **No se mezclan.** Análisis L1: `-p-` + `-xa-`/`-ka-` y `-si-` + `-ka-` (L1 p.111–112). Análisis L2: `-pxa` y `-ska`, un morfema cada uno (L2 p.181, 202). Cada ejemplo se segmenta según su fuente y se indica cuál. La forma escrita es la misma en los dos análisis (`sarapxi`, `saraski`) | L1 p.111–112; L2 p.181, 202 | Diferencia documentada; elección para el tokenizador pendiente |
| D12 | Número gramatical y personas | Hay **cuatro personas**, definidas por la inclusión o exclusión del hablante y del destinatario, no por el número: 1 = hablante sin destinatario; 2 = destinatario sin hablante; 3 = ninguno; 4 = hablante y destinatario ("tú y yo"). La 4.ª no equivale al "nosotros" español: la 1.ª también puede ser plural ("nosotros exclusivo"). Ni las personas ni los pronombres marcan número (L1 p.18, 182). El plural se expresa opcionalmente con `-naka` en nombres y pronombres (L1: "plural de énfasis", p.182; L2: `nänaka`, `jumanaka`, `jupanaka`, `jiwasanaka`, p.181, 184) y en el verbo con `-p-` (L1) / `-pxa` (L2). L2 dice que la concordancia de número es opcional, aunque tiende a hacerse obligatoria por influencia del castellano (p.181, 242) | L1 p.18, 87–88, 182; L2 p.33, 148, 181–184, 242 | Confirmada |
| D13 | Conjunciones | El aymara **no tiene conjunciones como palabras independientes** equivalentes a "y", "o", "pero" del español (L2 p.32). La coordinación se hace con **sufijos** (`-mpi` "y, con"; `-sa` conectivo; `-cha` "o"; `-raki` "también"), con **yuxtaposición** y con formas de **`uka`** con sufijos (`uka-t`, `uk-xa-ru-xa` "y entonces") (L1 p.207–208, 212, 254–255, 312; L2 p.32, 159, 234, 237). No es correcto decir que el aymara "no puede coordinar" ni traducir esas formas como conjunciones independientes | L1 p.207–208, 212, 312; L2 p.32, 159, 234, 237 | Confirmada |

---

## Abreviaturas (lista única)

| Grupo | Abreviaturas |
|---|---|
| Persona y tiempo | `1` `2` `3` `4` (4 = hablante + destinatario, "tú y yo"; ver D12) · `X>Y` sujeto>objeto, glosado junto con el tiempo: `1>3.SIMP` · `SIMP` simple/no futuro · `FUT` · `IMP` · `REM.C` remoto cercano (personal) · `REM.L` remoto lejano (no personal) · `REM` sin precisar · `INFR` inferencial (`-pacha`) · `NI` no-involucrador (`-chi`) · `DES` desiderativo · `REPR` reprochador · `SUB` subordinador (`-sa`, `-sina`, `-ipana`; `-ipana` = sujetos diferentes, L1 p.161, L2 p.200) |
| Derivativos verbales | `CAUS` (`-ya-`) · `CAUS.R` (`-cha-`) · `REFL` (`-si1-`) · `PROG` (`-si2-`) · `BEN` (`-rapi-`) · `VICT` (`-raqa-`) · `APPR` (`-ni-`) · `DIST` (`-waya-`) · `AWAY` (`-nuku-`) · `UP` `DOWN` `OUT` `IN` (`-ta-` `-qa-` `-su-` `-nta-`) · `INCEP` · `MOM` (`-t'a-`) · `DIV` (`-ja-`) · `COMPL` (`-xa-`) · `INCOMPL` (`-ka-`) · `PL` (`-p-`) |
| Nombre | `PL` (`-naka`) · `POSS.1`–`POSS.4` · `POSR` (`-ni`) · `GEN` `LOC` (`-na`) · `ALL` (`-ru` relacional) / `COMPL.RU` (`-ru` complemento personal de la flexión; ver D9) · `ABL` (`-ta`) · `COM` (`-mpi`) · `BEN` (`-taki`) · `UNTIL` (`-kama`) · `CAUSE` (`-layku`) · `SIM` (`-jama`) · `INCL` (`-pacha1`) · `SELF` (`-pacha2`) · `AMONG` (`-pura`) · `DIM` `QUANT` `SIZE` `FULL` `WITHOUT` · `LOC.SIDE` `LOC.FRONT` `LOC.PLACE` `LOC.EXACT` `LOC.ON` `LOC.BESIDE` · `O` complemento cero (`LEXEMA.O` = nombre sin sufijo que pierde la vocal final) |
| Transpositores | `INF` (`-ña`) · `AG` (`-iri1`) · `NMLZ.PURP` (`-iri2`) · `NMLZ.RES` (`-ta`) · `NMLZ.LOC` (`-wi`) · `VBLZ` (genérico, derivativos que verbalizan) · `VBLZ.KA` (`-ka-`) · `VBLZ.LONG` (`-:-`, "ser") · `VBLZ.PTA` (`-pta-`) |
| Independientes y oracionales | `LIM` (`-ki`) · `ADD` (`-raki`) · `EMPH` (`-puni`) · `AFF` (`-wa`) · `TOP` (`-xa`) · `Q.YN` (`-ti`) · `Q.INF` (`-sa1`) · `Q.ALT` (`-cha`) · `Q.SUB` (`-tiya`/`-tixa`) · `NEG` (`-ti` con `jani`) · `FOLL` (`-sti`) · `POL` (`-ya`) · `CAT` (`-sa2`) · `EXCL` (`-:`) · `CERT` (`-pi`; L2 `-pï`) · `SUPP` (`-chi-`) · combinadas: `TOP.POL` `AFF.POL` `CAT.POL` `CAT.EXCL` `CERT.POL` |
| Notación | Glosas léxicas en español; un punto une palabras (`cargar.espalda`). Las tablas de L1 marcan con `c_v`, `v_c`, etc. lo que exige el sufijo antes y después (c = consonante, v = vocal; L1 p.67) |

En v2 se eliminó `OPT`: L2 no llama "optativo" a `-ipana` ni a `-pana`. Su "modo potencial u optativo" es `-sa` (= DES de L1; L2 p.192); `-pana` es su imperativo de 3.ª persona (= IMP 3>3; L2 p.195) y `-ipana` es subordinador de sujetos diferentes (= SUB; L2 p.200).

Equivalencias aplicadas al unir: en la Parte 3, `COP` pasó a `VBLZ.LONG`, `HAB` a `POSR`, `SIMIL` a `SIM`, `INTER` a `AMONG`, `ATEN` a `MOM`, `EMPH` (`-ya`) a `POL`, `PST.DIR` a `REM.C`, `PST.IND` a `REM.L` y `FUT.n` a `n>3.FUT`. En la Parte 1, `VBLZ` pasó a `VBLZ.LONG`/`VBLZ.KA` según el sufijo, y `NMLZ` a `NMLZ.RES`/`NMLZ.LOC`.

---
## 0. Rasgos generales

### 0.1 Según L1

Todo verbo conjugado obliga a marcar la fuente de los datos: conocimiento personal (lo visto o vivido por el hablante) frente a no-personal (lo dicho por otros, inferido, conjeturado o leído), distinción que también gobierna el uso de los sufijos oracionales (L1 p.17). Hay cuatro personas (1 = hablante sin destinatario; 2 = destinatario sin hablante; 3 = ninguno de los dos; 4 = ambos, «nosotros inclusivo»), que no especifican número ("cuatro personas, que no especifican número", L1 p.18), sin género, y la 2.ª es la más marcada (L1 p.18, p.88). Ver D12. Todo verbo es «interaccional»: cada sufijo flexional fusiona sujeto y complemento en una sola forma indivisible, con nueve interacciones posibles (L1 p.18, p.88, p.139). El tiempo se divide primero en futuro / no-futuro, porque el futuro se concibe «detrás» del hablante y presente/pasado «delante» (L1 p.19). Las raíces verbales son humanas o no-humanas sin marca morfológica; `-ya-` puede humanizar al sujeto (L1 p.19, p.80). La oración se define por sufijos oracionales, no por el verbo ni por el orden de palabras; no hay verbo copulativo (L1 p.20). Para funcionar como verbo, un tronco necesita flexión; los derivativos verbales (muchos de ubicación, dirección y movimiento) van antes de los independientes y de la flexión (L1 p.20–21, p.91). Casi todos los morfemas terminan en vocal, que se retiene o se suprime por influencia sobre todo regresiva del sufijo siguiente (L1 p.21–22); el acento recae en la penúltima vocal de la palabra (L1 p.22).

### 0.2 Según L2

El aymara es una lengua sufijante y aglutinante: no tiene prefijos, artículos ni conjunciones (estos dos últimos pueden aparecer como sufijos), y la oración se construye ordenando raíz más sufijos (L2 p.32, p.80). Todas las palabras y todos los sufijos terminan en vocal (final abierta; solo hay excepciones en las exclamaciones; L2 p.32, p.60, p.75). No hay género gramatical sino solo semántico, y hay cuatro personas: naya, juma, jupa, jiwasa (L2 p.33; L2 traduce `jiwasa` como "nosotros/as", pero es la persona que incluye al destinatario; ver D12). La ausencia de conjunciones se refiere a palabras independientes: la coordinación existe mediante sufijos y yuxtaposición (ver D13). El adjetivo antecede al nombre y el adverbio al verbo (L2 p.34). El orden básico de la oración declarativa es **SOV** (L2 p.241, 243), aunque se admiten permutaciones (`¿akaxa kunasa?` ~ `¿kunasa akaxa?`, p.243); dentro de la frase verbal, los complementos van en el orden tiempo – lugar – objeto indirecto – objeto directo – verbo (p.255). El pasado distingue conocimiento directo e indirecto (L2 p.34, p.55–56). L2 destaca unos 40 verbos de movimiento y un uso frecuente del pluscuamperfecto (L2 p.34). **Posibles tensiones con L1:** (a) la categoría "dúctil" no tiene correlato en la regla binaria de L1; (b) el sufijo de 1.ª persona es `-tha` en L2 y `-ta` en L1; (c) L2 prescribe recuperar la vocal final entre palabras, y atribuye a Hardman una escritura elisionista (p.72); (d) L2 declara SOV, mientras que L1 presenta el orden como libre (L1 p.293–294); (e) L2 trata como un solo morfema el plural verbal `-pxa` y el progresivo `-ska` (D11); (f) L2 usa otros nombres para varias categorías (tabla de equivalencias en 3.4). La comparación morfológica con L2 está en las secciones 2.1, 3.4 y 4.1.

## 1. Orden de palabras

| Construcción | Aymara | Español | Ejemplo | Fuente | Notas |
|---|---|---|---|---|---|
| Oración declarativa básica (equivalencia) | X-xa  Y-wa (sin cópula) | "A es B" | `misa-x jach'a-wa` — mesa-TOP grande-AFF — "la mesa es grande" | L1 p.172, 293, 296 | La oración se define por el sufijo oracional, no por el orden. Solo un -wa; -xa puede repetirse. El libro advierte que no hay que leer "-xa = sintagma nominal, -wa = sintagma verbal" (p.297). |
| Oración con verbo | (nominales) + verbo flexionado; -wa en el elemento que responde la pregunta subyacente | S V O | `naya-x sara-:-wa` — 1-TOP ir-1>3.FUT-AFF — "yo voy a ir" | L1 p.280, 297 | Los nominales que son el complemento de la flexión verbal suelen ir sin sufijo oracional (p.297). |
| Complemento directo (complemento cero) + verbo | nominal sin sufijo, pierde la vocal final, junto al verbo | V + objeto directo | `kun-s mun-ta` — qué.O-Q.INF querer-2>3.SIMP — "¿qué quiere Ud.?" | L1 p.233–234 | El complemento cero suele preceder inmediatamente a su verbo (p.233). Alomorfo cero de -wa tras él (p.281). La pérdida de vocal es análisis de L1; en la escritura normalizada de L2 la vocal se escribe (`T'ant'a muntha`, L2 p.67). Ver 5.3. |
| Complemento/relacional con caso | N-ru / N-ta / N-taki / N-mpi / N-na + verbo | prep. + N | `marka-ru-w sar-ta` — pueblo-ALL-AFF ir-1>3.SIMP — "fui al pueblo" | L1 p.213 | Ver sección 2. |
| Negación | jani-w … verbo-…-ti | no + V | `jani-w naya-x sum aymar parla-ñ yat-k-t-ti` — NEG-AFF 1-TOP bien aymara.O hablar-INF saber-INCOMPL-1>3.SIMP-NEG — "no sé hablar bien el aymara" | L1 p.301 | -ti va donde habría -wa; el verbo atrae a -ti (p.299–300). |
| Pregunta sí/no | -ti sobre el elemento preguntado | ¿…? | `Mariya-t wawa-r t'ant' chur-i` — María-Q.YN niño-COMPL.RU pan.O dar-3>3.SIMP — "¿dio María pan al niño?" | L1 p.282, 299–300 | La posición de -ti = posición de -wa en la respuesta (p.299). |
| Pregunta de información | interrogativo-sa (sobre el interrogativo o su frase) | qué/quién/dónde | `kuna-s suti-ma-xa` — qué-Q.INF nombre-POSS.2-TOP — "¿cuál es su nombre?" | L1 p.282 | Solo un -sa1 por oración. |
| Modificador + nombre | modificador (antes) + núcleo | adjetivo + N (en español va después) | `ch'iyar ch'uqi-wa` — negro papa-AFF — "es (una) papa negra" | L1 p.172, 245 | Regla 2/3 **de L1**: el modificador conserva su vocal final si tiene 2 vocales (`janq'u ch'uqi`) y la pierde si tiene 3 o más (`ch'iyar`) (p.244–245). Es análisis de L1; en la escritura normalizada de L2 se escribe completa (`Ch'iyara phisi`, L2 p.67). Ver 5.3. |
| Varios modificadores | Interrog./Dem./Pron. + Número + Tamaño + Color + Núcleo | | `kha: jach'a wila punku-n tinta-na` — aquel grande rojo puerta-POSR tienda-LOC — "en aquella tienda grande de puerta roja" | L1 p.251–252 | Orden "preferido"; tamaño y color pueden intercambiarse (p.263, nota 35). El sufijo va solo en el núcleo (p.250). |
| Poseedor + poseído | poseedor-na + poseído-POSS | "mi casa" | `naya-n uta-ja` — 1-GEN casa-POSS.1 — "mi casa" | L1 p.224, 247 | El POSS concuerda con la persona del poseedor; el poseedor pronominal puede omitirse (p.247). Recursivo (p.257). |
| Demostrativo + nombre | demostrativo (antes) + núcleo | este/ese + N | `kha: tinta-na` — aquel tienda-LOC — "en esa tienda de allá" | L1 p.248 | También `aka kimsa-x` — este tres-TOP — "estos tres" (p.249). |
| Número + nombre | número + nombre (sin -naka) | tres casas | `naya-x pusi uta-ni-:-t-wa` — 1-TOP cuatro casa-POSR-VBLZ.LONG-1>3.SIMP-AFF — "tengo cuatro casas" | L1 p.204, 207, 246 | -naka no se pone al nombre modificado por un número (p.207), pero el propio L1 trae `pusi jach'a janq'u uta-naka-pa-sa` (p.251). L2: "no lleva *generalmente* flexión de número" (p.154). Tratarlo como tendencia, no como prohibición. |
| Nombre + posicional | nombre + posicional-sufijos | "dentro del patio de su casa" | `uta taypi-pa-n` — casa medio-POSS.3-LOC — "dentro del patio de su casa" | L1 p.250 | Los sufijos van al núcleo (`[uta taypi]-pa-n`); `taypi uta-pa-n` = "en su casa del medio". |
| Frase con -mpi | N-mpi N-mpi | "A y B" | `tunka jamach'i-mpi suxta wisk'acha-mpi` — diez pájaro-COM seis vizcacha-COM — "con diez pájaros y seis vizcachas" | L1 p.208, 255 | Cada miembro lleva el mismo sufijo; la coordinación con -mpi es más común que con -na o -ni (p.254). |
| Cita | hablante + cita + sa-sa + sa-ña | "dijo que…" | `jupa-x wali-ki-w sa-sa-w s-i` — 3-TOP bien-LIM-AFF decir-SUB-AFF decir-3>3.SIMP — "dijo que estaba bien" | L1 p.314 | Única estructura multioracional ligada a un verbo (saña). |
| Subordinada regular | cláusula con -sa (conocimiento personal) / -sina (no personal), antes de la principal | gerundio / "después de…" | `mariya-x lapis ala-sa-w jupa-r chur-i` — María-TOP lápiz comprar-SUB-AFF 3-COMPL.RU dar-3>3.SIMP — "María, comprando un lápiz, se lo dio a él/ella" | L1 p.316 | Si los tiempos no son simultáneos, la subordinada precede a la principal; sujetos normalmente iguales (p.316). |
| Subordinada de propósito | verbo-iri / verbo-ña-taki, antes del verbo principal | "a + infinitivo" | `ch'uq al-iri-w sar-ta` — papa.O comprar-NMLZ.PURP-AFF ir-1>3.SIMP — "fui a comprar papas" | L1 p.213, 316 | Ver 7.2. |
| Subordinada con uka / -xa | cláusula (-xa/-sa/-tixa) + uka resumidor | relativa, "eso que…" | `kuna-tiy wakis-k-i uka` — qué-Q.SUB necesario-INCOMPL-3>3.SIMP eso — "todo lo que sea necesario, eso" | L1 p.289, 317–318 | Ver sección 6, fila "que". |

**¿Es flexible el orden y de qué depende?** Sí, entre unidades sintácticas el orden es libre; el libro muestra 9 de las 25 permutaciones posibles de cinco unidades de una oración sin cambio gramatical ni semántico básico (p.294) y dice que el orden de palabras solo tiene significado gramatical dentro de las frases (p.293). Lo que fija el sentido es la posición de los sufijos oracionales: -wa/-ti/-sa1 caen en el elemento que responde (o plantea) la pregunta subyacente, y el material más interesante tiende a ir al comienzo en las respuestas (p.299). Dentro de la frase nominal el orden sí es fijo (modificador antes que núcleo; el núcleo lleva los sufijos de toda la frase, p.250), y el negativo y su verbo no tienen que estar contiguos (p.294). (Nota: con cinco unidades hay 120 permutaciones posibles, no 25; la cifra es del propio L1.)

**Según L2.** La norma oficial fija **SOV** como orden básico de la oración simple declarativa (L2 p.243: `Anuxa t'ant'a manq'i` "el perro come pan"; `Antukuxa aymara yatiqatayna` "Antonio había aprendido el aymara") y admite permutaciones (p.243). Para los complementos de la frase verbal da este orden (p.255):

| C. adv. de tiempo | C. adv. de lugar | Obj. indirecto | Obj. directo | Verbo |
|---|---|---|---|---|
| `Wasüruxa` "ayer" | `markata` "del pueblo" | `wawapataki` "para su hijo" | `t'ant'a` "pan" | `alani` "compró" |

Este es el orden por defecto que adopta D10.

## 2. Sufijos del nombre

Orden: RAÍZ – [sufijos de distribución limitada] – Clase I (localizadores, -ni, POSS, -naka, -mpi1, -pacha1; orden relativo poco fijo) – Clase II (un caso -ru / -ta / -taki / -mpi2 / -na, o complemento cero; luego -pacha2 / -kama / -jama) – Clase III (verbalizadores -ka- / -:- / -pta-) – independientes – oracional (L1 p.196–197, 210, 227–228, 235, 272).

| Sufijo | Función | Equivale en español | Ejemplo | Fuente | Notas |
|---|---|---|---|---|---|
| -naka | plural (opcional) | -s | `uta-naka` — casa-PL — "casas" | L1 p.206 | Su ausencia no indica singular (p.206). No va con -iri2 ni -rara. Con pronombres, plural de énfasis (p.182). |
| -xa ~ -ja | POSS.1 | mi/nuestro (sin "tú") | `uta-ja` — casa-POSS.1 — "mi/nuestra casa (no tuya)" | L1 p.205 | Alomorfo opcional: alargamiento vocálico tras /a/ (p.205). |
| -ma | POSS.2 | tu/su (de Ud.) | `uta-ma` — casa-POSS.2 — "tu casa" | L1 p.205 | POSS solo en nombres, temporales, posicionales e interrogativos correspondientes (p.205). |
| -pa | POSS.3 | su (de él/ella/ellos) | `uta-pa` — casa-POSS.3 — "su casa de él/ella/ellos" | L1 p.205 | Requieren vocal precedente (p.205). |
| -sa | POSS.4 | nuestro (incluyendo "tú") | `uta-sa` — casa-POSS.4 — "nuestra casa (mía y tuya)" | L1 p.205 | Homófono de -sa 'lado', -sa1 y -sa2 (ver 4). |
| -ni | POSR: poseedor / enumerador | tener, dueño de; "-ni" en números humanos | `uta-ni-wa` — casa-POSR-AFF — "es dueño/a de casa; tiene una casa" | L1 p.203–205 | Con números y qawqha marca "personas" (p.204). Tras -ña da obligación (p.204). No va con POSS delante (p.205). |
| -ru | ALL: relacional (dirección, lugar, propósito); COMPL.RU: nominal humano que es complemento de la flexión verbal (ver D9) | a, hacia | `marka-ru-w sar-ta` — pueblo-ALL-AFF ir-1>3.SIMP — "fui al pueblo" | L1 p.210–213 | Ver "Respuestas", pregunta 1. Pierde su vocal ante sufijos que piden consonante (p.211). |
| -ta | ABL: origen; también "en (vehículo)" | de, desde | `qhatu-t jut-ta` — mercado-ABL venir-1>3.SIMP — "vengo del mercado" | L1 p.214–217 | -xa-ta (LOC.ON-ABL) = "acerca de" (p.214). Distinto de -ta nominalizador (ver 7.2). |
| -taki | BEN: beneficiario / propósito | para | `aka-x juma-taki-w` — esto-TOP 2-BEN-AFF — "esto es para ti" | L1 p.217–221 | Con humano + -rapi- en el verbo = complemento; sin -rapi-, relacional (p.218). |
| -mpi (-mpi2) | COM: agente (con -ya-), instrumento, compañía | con, por (agente) | `lawa-mpi-w jiru-p-x-i` — palo-COM-AFF remover-PL-COMPL-3>3.SIMP — "lo removieron con un palo" | L1 p.221–224 | -mpi1 y -mpi2 nunca coinciden en un mismo tronco; se diferencian por función y orden (p.207, 221). |
| -na | GEN: poseedor humano; LOC: ubicación no humana | de (posesión), en | `naya-n uta-ja` — 1-GEN casa-POSS.1 — "mi casa"; `kajun manqha-n-k-i-w` — cajón dentro-LOC-VBLZ.KA-3>3.SIMP-AFF — "está adentro del cajón" | L1 p.224–227, 237 | El uso locativo ocurre solo con verbo; si no, se verbaliza con -ka- (p.227). No marca posesión en nominales no humanos (p.224). |
| -sa (localizador) | LOC.SIDE: lado | a este lado | `ak-sa-ru-wa` — este-LOC.SIDE-ALL-AFF — "a este lado" | L1 p.201 | Solo con demostrativos, kawki y maya; va pegado a la raíz (p.201). |
| -kata ~ -kati | LOC.FRONT: al frente | allá al frente | `khay-kati-n` — allá-LOC.FRONT-LOC — "allá al frente" | L1 p.201 | Solo con demostrativos y kawki. |
| -wja | LOC.PLACE: lugar | lugar de | `uta-wja` — casa-LOC.PLACE — "lugar de la casa" | L1 p.201–202 | Va antes de -jita si coocurren. |
| -jita | LOC.EXACT: lugar exacto | mismo | `akh-ita-n` — aquí-LOC.EXACT-LOC — "aquí mismo" | L1 p.202 | |
| -xa (localizador) | LOC.ON: encima, sobre | sobre | `uk-xa-ru` — eso-LOC.ON-ALL — "entonces" | L1 p.202 | Distinto de -xa oracional, -xa- completivo y -xa POSS.1. |
| -:xa | LOC.BESIDE: al lado de | junto a | `ak-sa-:xa-r` — este-LOC.SIDE-LOC.BESIDE-ALL — "a este lado" | L1 p.203 | Alarga la vocal precedente. |
| -mpi1 | COM: conjuntor | y, con | `kimsa-ni-mpi-w sara-ñani` — tres-POSR-COM-AFF ir-4>3.FUT — "con tres personas más iremos" | L1 p.207–208 | Precede a -pacha1 y a los casos. Une también oraciones: `uka-mpi-x`. |
| -pacha1 | INCL: inclusor | todos, también | `kimsa-n-pacha-w sara-ñani` — tres-POSR-INCL-AFF ir-4>3.FUT — "los tres iremos" | L1 p.209 | Distinto de -pacha2 (SELF) y de la raíz pacha. |
| -pacha2 | SELF: mismo | mismo, en persona | `jiwas-pach sara-ñani` — 4-SELF ir-4>3.FUT — "nosotros personalmente iremos" | L1 p.228 | Va después de los casos; `phaxs-pacha-t` (INCL) vs `phaxsi-t-pach` (SELF). |
| -kama | UNTIL: hasta; "cada uno" | hasta | `jichha-kama` — ahora-UNTIL — "hasta ahora" | L1 p.228–230 | Con humanos: "entre, cada uno"; con precios: "a X cada uno". |
| -jama | SIM: como, parecido a | como | `jach'-jama-wa` — grande-SIM-AFF — "es algo grande" | L1 p.230–233 | Puede repetirse (`kun-jam-jama-sa`). También independiente (cap. X). |
| (vocal final cae) | O: complemento cero | (objeto directo) | `ch'uq chur-ita` — papa.O dar-2>1.IMP — "dame papas" | L1 p.233–235 | Va tras los demás sufijos de Clase II. |
| -layku | CAUSE: "por, a causa de, a cambio de" | por | `manu-layku-w jut-ta` — deuda-CAUSE-AFF venir-1>3.SIMP — "vine a causa de una deuda" | L1 p.199 | Distribución limitada. Con -ña: "por aprender" (p.199). |
| -pura | AMONG: entre (recíproco) | entre | `warmi-pura` — mujer-AMONG — "entre mujeres" | L1 p.199 | Con humanos y pronombres. |
| otros limitados | -itu DIM; -ja QUANT; -ch'a SIZE; -rara FULL; -wisa WITHOUT; -qata (solo en nayra-qata) | | `yapu-x wali qala-rara-w` — chacra-TOP bien piedra-FULL-AFF — "la chacra está llena de piedras" | L1 p.198–200 | `challw-itu` "pececito"; `wal-ja` "mucho"; `ak-ch'a-wa` "de este tamaño"; `jinchu-wisa` "sordo". |

Pronombres: `naya` 1, `juma` 2, `jupa` 3, `jiwasa` 4 (sin marca de género ni número; no llevan -ni ni POSS ni -sa/-kata) — L1 p.182. Demostrativos: `aka` (aquí), `uka` (ahí), `khaya` (allá), `khuri` (más allá) — L1 p.183.

### 2.1 Contraste con L2 (morfología nominal, L2 pp.148–175)

L2 agrupa los sufijos del nombre en flexión de persona (posesivos), de número y de caso, y en derivación denominativa y deverbativa. Orden que da L2: **raíz – número – persona – caso** (`uta-naka-ja-na` "en mis casas", p.162). L1 admite que `-naka` vaya antes o después del posesivo, aunque lo más frecuente es antes (L1 p.207).

| Sufijo | Nombre en L2 | Etiqueta de esta guía | Ejemplo de L2 | Fuente L2 | Comparación con L1 |
|---|---|---|---|---|---|
| `-ja` / `-ma` / `-pa` / `-sa` | flexión de persona (posesivos) | POSS.1–POSS.4 | `uta-ja` "mi casa"; `phisi-ma` "tu gato"; `anu-pa` "su perro"; `phuchha-sa` "nuestra hija" | p.148–152 | Coincide. L2 da `-ja` como forma general de 1.ª persona (variantes `-xa`, `-ña`, `-ŋa`; en el sur, `-ya`): base de D4 |
| `-naka` | flexión de número | PL | `anu-naka` "perros" | p.152–154 | Coincide. Sin plural no implica singular; ante numeral o cuantificador "generalmente" no se pone; los pares del cuerpo no suelen pluralizarse; también hay reduplicación (`wara wara` "estrellas") |
| `-na` | genitivo | GEN | `tata-ja-na uta-pa` "la casa de mi papá" | p.154 | Coincide (L1 p.224) |
| `-ø` | acusativo (morfema cero): "objeto, meta" y adverbializador | O | `Wara wara-ø uñjtawa` "ves la estrella"; `jupaxa jawira-ø jali` "corre al río"; `jilamaxa qhathu-ø sari` "tu hermano fue a la feria" | p.154–155 | **Análisis distintos.** Correspondencia funcional con el complemento cero de L1 (nominal sin sufijo de caso ligado al verbo, que también puede expresar destino: `mark sar-ta` "fui al pueblo", L1 p.235). L1: se marca por la pérdida de la vocal final (p.233). L2: morfema cero, la vocal se escribe (ver D6). L2 añade que su análisis "requiere un análisis exhaustivo" (p.155) |
| `-ru` | direccional o ilativo: complemento indirecto, dirección, espacialidad, temporalidad, instrumento, propósito | ALL / COMPL.RU (D9) | `nayaxa wawaru t'ant'a churtha` "yo le di pan al niño"; `markaru jutani` "vendrá al pueblo"; `awayuru q'ipiñäni` "cargaremos en el aguayo" | p.155–157 | L2 llama "complemento indirecto" a lo que L1 llama complemento `-ru` de la flexión. Añade usos temporales (`jayp'uru` "por la tarde") e instrumentales |
| `-taki` | benefactivo | BEN | `jilaja-taki-wa alantha` "compré para mi hermano" | p.158 | Coincide |
| `-na` | locativo | LOC | `pampa-na ikitayna` "había dormido en la pampa" | p.158 | Coincide |
| `-ta` | ablativo (procedencia, materia, tema) | ABL | `marka-ja-ta juttha` "vengo de mi pueblo"; `qala-ta-wa` "es de piedra"; `uraqi-ta` "acerca del terreno" | p.158–159 | Coincide; L2 incluye "materia" y "acerca de" sin `-xa-` |
| `-mpi` | instrumental (compañía, instrumento, adición, conjunción) | COM | `tiwula-mpi wallata-mpi-wa jikisipxi` "el zorro y el ganso se encuentran" | p.159–160 | Coincide. En el sur aparece como `-nti` |
| `-kama` | limitativo ("hasta"; también exclusividad) | UNTIL | `marka-kama-wa sari` "fue hasta el pueblo"; `warmi-kama-wa` "solamente mujeres" | p.160 | Coincide (L1 p.228–230) |
| `-layku` | causal | CAUSE | `juma-layku-wa ukana irnaqtha` "por ti trabajo ahí" | p.160–161 | Coincide |
| `-jama` | comparativo (elide siempre la vocal previa) | SIM | `jaq-jama-wa sarnaqäta` "vas a andar como gente" | p.161 | Coincide |
| `-ni` | posesivo derivativo | POSR | `uta-ni` "dueño de casa" | p.163 | Coincide |
| `-wisa` | privativo | WITHOUT | `nayra-wisa` "ciego" | p.146, 164 | Coincide |
| `-pura` | "interacción recíproca entre semejantes" (L2 lo encabeza como "privativo", aparentemente por error) | AMONG | `warmi-pura-wa tantachasipxi` "se reúnen entre mujeres"; `kullak-pura-wa` "entre hermanas" | p.167 | L2 p.62 lo pone entre los **débiles**, pero en la p.167 da una condición: "cuando la raíz tiene tres o más sílabas elide la vocal precedente". L1 da ejemplos compatibles (`qam-ir-pura` "entre gente rica", `jupa-nak-pura`, p.199) |
| `-wja` | ubicativo | LOC.PLACE | `uka-wja-na ikiski` "está durmiendo en ese lugar" | p.167 | Coincide |
| `-kata` | locativo específico | LOC.FRONT | `uk-kata`, `jawir-kata` | p.62–63, 168 | Coincide |
| `-ch'a` | comparativo (tamaño) | SIZE | `uk-ch'a-pura-wa` "son del mismo tamaño" | p.167–168 | Coincide |
| `-pacha` | totalizador ("todo, entero") | INCL (L1 `-pacha1`) | `taqpacha`, `kimspacha`, `jiwaspacha`, `jupapacha` | p.63–64, 165 | **Contradicción.** L2 lo clasifica como **dúctil** (p.63–64). L1 distingue al menos cuatro sufijos `-pacha` y una raíz `pacha`; dice que todos los sufijos `-pacha` **piden consonante antes** y que `taq.pacha` "todo" es un tronco fosilizado (p.209, 228). `jupapacha` (vocal conservada) no encaja en la regla de L1. Clasificación pendiente (D7) |
| `-ïri` | ordinal | ‡ ORD (no está en la lista de L1) | `mayïri` "primero"; `kimsïri` "tercero" | p.167 | L1 lo analiza como `-:-` + `-iri` (cf. `kawk-i:r`, L1 p.69) |
| `-iri` | agentivo | AG | `umiri` "bebedor"; `awatiri` "pastor" | p.171–172 | Coincide. L2 registra `-ïri` para desambiguar: `jiliri` "el que crece" / `jilïri` "el mayor" |
| `-ña` | infinitivizador (infinitivo, concreto, obligativo, lugar/tiempo, instrumento) | INF | `sarañajawa` "debo ir"; `pichaña` "escoba"; `samaña` "descansadero" | p.172–174 | Coincide y amplía (L1 p.193–194) |
| `-ta` | resultante (participio) | NMLZ.RES | `p'akita` "roto"; `kutinitama yatthwa` "sé de tu regreso" | p.174 | Coincide |
| `-wi` | abstractivo: nombre de acción, lugar, abstracto | NMLZ.LOC | `tantachawi` "reunión"; `manq'awi` "comedor"; `lurawi` "acción" | p.174–175 | L2 amplía la función más allá del lugar. Alarga la vocal previa, pero no se escribe |
| Otros de L2 | `-lla` diminutivo, `-rara` ponderativo, `-pita` completivo, `-qata` posicional, `-tuqi` locativo direccional, `-lanti` supletorio, `-nama/-¨ma/-rana` aproximativo, `-k'alla` habitual, `-walla` cuantitativo, `-li` despectivo, `-la` ponderativo, `-nma` dubitativo | — | `janimna jutkchiti` "quizás no haya venido" (`-nma`) | p.164–171 | Varios no figuran en las tablas de L1 de esta guía; revisar si hacen falta en el generador |

## 3. Sufijos del verbo

Orden: RAÍZ – [Clase I: 1 `-cha-`; 2 `-ja-`; 3 `-su-`; 4 `-thapi-`/`-ra-`; 5 `-nuqa-`/`-qa-`/`-xata-`; 6 `-ta-`; 7 `-kata-`/`-kipa-`/`-naqa-`/`-nta-`/`-nuku-`/`-tata-`/`-xaru-`/`-xa:si-`/`-xaya-`; 8 `-t'a-`/`-ch'uki-`; 9 `-rpaya-`] – [Clase II: 1 `-ya-`; 2 `-si1-`; 3 `-ni-`; 4 `-waya-`; 5 `-rapi-`/`-raqa-`; 6 `-si2-`; 7 `-ka-`; 8 `-xa-`; 9 `-p-`; 10 `-ka-`/`-xa-`] – (sufijos independientes) – FLEXIÓN (persona+tiempo, un solo morfema) – (sufijos oracionales). (L1 p.97 Cuadro VI.1; p.88; p.140). La Clase I actúa sobre la raíz y rara vez pasa de 2–3 sufijos juntos; la Clase II actúa sobre la flexión/personas y admite hasta 7 en un tronco (L1 p.94, p.114, p.117). Tras la flexión solo pueden ir sufijos oracionales (L1 p.140).

### 3.1 Personas (sujeto → objeto)

| Sujeto → Objeto | Sufijo | Tiempo | Ejemplo | Fuente | Notas |
|---|---|---|---|---|---|
| 1→2 | `-sma` | SIMP | `sar-ta-ya-raq-sma` — ir-UP-CAUS-VICT-1>2.SIMP — "yo desperté (a su bebé)" | L1 p.144; ej. p.110 | c_v (ver «Notación» en Abreviaturas). |
| 2→1 | `-ista` | SIMP | `sista` — decir.2>1.SIMP — "tú me dices" (forma irregular de `sa-`, el libro no la segmenta) | L1 p.144; ej. p.142 | c_v. El aymara no tiene 2→4: `-ista` tomó el sentido 2→1 (nota 2, p.168–169). |
| 3→3 | `-i` | SIMP | `chur-i` — dar-3>3.SIMP — "él/ella le da/dió" (en `Jupa-w jupa-r t'ant' chur-i`) | L1 p.144; ej. p.87 | c_v. La 3.ª no se marca; la /i/ se absorbe fácilmente (p.159). |
| 1→3 | `-ta` | SIMP | `chur-t-wa` — dar-1>3.SIMP-AFF — "yo doy/di" | L1 p.144; ej. p.68 | c_c; la vocal de `-ta` cae ante `-wa`. Misma forma que 2→3 pero con consonante después. L2 da `-tha` para esta casilla (`churtha`, L2 p.155): correspondencia funcional, no variante gráfica (D5). |
| 4→3 | `-tan` | SIMP | `tuku-ya-p-x-tan-w` — terminar-CAUS-PL-COMPL-4>3.SIMP-AFF — "(nosotros) hemos terminado" | L1 p.144; ej. p.134 | c_c. La nasal marca 4.ª persona como sujeto (p.159). |
| 3→1 | `-itu` | SIMP | `us-utu` — doler-3>1.SIMP — "(la cabeza) me duele" (en `P'iqi-w us-utu`) | L1 p.144; ej. p.81 | c_v. Tras /u/ la /i/ se pierde (usu + -itu → us-utu; p.69). |
| 3→4 | `-istu` | SIMP | `sistu` — decir.3>4.SIMP — "él/ella nos dice" (irregular, sin segmentar) | L1 p.144; ej. p.142 | c_v. La /s/ interpolada marca 4.ª persona (p.159). |
| 2→3 | `-ta` | SIMP | `q'ip-ta-wa` — cargar.espalda-2>3.SIMP-AFF — "tú cargas" | L1 p.144; ej. p.77 | c_v (conserva su vocal ante `-wa`). /ta/ marca 2.ª persona en SIMP (p.159). |
| 3→2 | `-tam` | SIMP | `sistam` — decir.3>2.SIMP — "él/ella te dice" (irregular, sin segmentar) | L1 p.144; ej. p.142 | c_c. La 2.ª queda marcada dos veces (/ta/ + /m/) y la 3.ª ninguna (p.159). |
| 1→2 | `-:ma` | FUT | `ana-nuku-ya-si-ni-:ma` — arrear-AWAY-CAUS-REFL-APPR-1>2.FUT — "le dejaré a Ud." | L1 p.145; ej. p.118 | v_v. Misma forma que IMP 1→2. |
| 2→1 | `-ita:ta` | FUT | `Wali-ki-w, yati-cha-p-x-ita:ta-piy` — bien-LIM-AFF saber-CAUS.R-PL-COMPL-2>1.FUT-CERT.POL — "Bueno, Uds. por favor enséñenme" | L1 p.145; ej. p.289 | c_v. |
| 3→3 | `-ni` | FUT | `sara-raki-ni-w` — ir-ADD-3>3.FUT-AFF — "irá también" | L1 p.145; ej. p.131 | v_v. |
| 1→3 | `-:` | FUT | `naya-w sara-:` — 1-AFF ir-1>3.FUT — "yo iré" | L1 p.145; ej. p.152 | v_v. El sufijo es solo alargamiento vocálico. Igual a IMP 1→3 (p.152). |
| 4→3 | `-ñani` | FUT | `sara-p-xa-ñani` — ir-PL-COMPL-4>3.FUT — "iremos (todos)" | L1 p.145; ej. p.132 | v_v. Igual a IMP 4→3. |
| 3→1 | `-itani` | FUT | `irp-itani` — llevar-3>1.FUT — "(Roberto) me llevará" (en `Ruwirtu-w irp-itani`) | L1 p.145; ej. p.73 | c_v. |
| 3→4 | `-istani` | FUT | FALTA | L1 p.145 | c_v. En algunos dialectos `-stani` (p.145). Sin ejemplo localizado en L1 (pendiente). |
| 2→3 | `-:ta` | FUT | `juma-w sara-:ta` — 2-AFF ir-2>3.FUT — "tú irás / Ud. irá" | L1 p.145; ej. p.152 | v_v. |
| 3→2 | `-:tam` | FUT | `Khiti-s irpa-:tam` — quién-Q.INF llevar-3>2.FUT — "¿quién lo llevará a Ud.?" | L1 p.145; ej. p.73 | v_c. |

Los paradigmas de IMP, REM.C, REM.L, INFR, NI, DES y REPR (las mismas nueve interacciones) están en 3.2 (L1 p.164–167, Cuadros VII.3.1–VII.3.3).

### 3.2 Tiempos y modos

| Tiempo/modo | Marca | Ejemplo | Fuente | Notas |
|---|---|---|---|---|
| SIMP (simple, no-futuro) | Sin marca de tiempo. Paradigma en 3.1. | `chur-t-wa` — dar-1>3.SIMP-AFF — "yo doy/di" (ej. en L1 p.68) | L1 p.143–144, p.159 | Conocimiento personal: lo visto o que se está haciendo; se traduce como presente o pasado (p.143). Sus formas reaparecen como indicadores de persona en casi todos los tiempos compuestos (p.143). |
| FUT (futuro) | Nasal y/o vocal larga. Paradigma en 3.1. | `naya-w sara-:` — 1-AFF ir-1>3.FUT — "yo iré" | L1 p.144–145, p.152, p.159 | Conocimiento personal: el hablante «atestigua» el futuro. Sirve como mandato cortés donde no se usaría el IMP (p.144). El futuro empieza de inmediato; no se solapa con el presente (p.144). |
| IMP (imperativo) | /m/ con 2.ª persona y /p/ con 3.ª: 1→2 `-:ma`; 2→1 `-ita`; 3→3 `-pa`; 1→3 `-:`; 4→3 `-ñani`; 3→1 `-itpa`; 3→4 `-istpa`; 2→3 `-m`; 3→2 `-:tpa(n)` ~ `-:tam`. | `jum sara-m` — 2 ir-2>3.IMP — "vaya Ud. / vé tú" | L1 p.152–153, p.164 | No realizado (presente). 1→2, 1→3, 4→3 y (opcional) 3→2 coinciden con el FUT, pero el sujeto del IMP no lleva sufijo oracional y pierde la vocal final (`jum`, `nay`). `-wa` no aparece salvo en 3→2; `-ya` es frecuente. Fuerte: entre personas de respeto se usa el FUT. Otro ejemplo: `ap-ta-ni-m` (L1 p.109). |
| REM.C (remoto cercano) | Se antepone `-ya:-` a los sufijos SIMP que empiezan por consonante: 1→2 `-ya:sma`; 1→3 `-ya:ta`; 2→3 `-ya:ta`; 4→3 `-ya:tan`; 3→2 `-ya:tam`. 3→3 `-:na`. Si el SIMP empieza por vocal: SIMP sin la /u/ final + `-ana`: 3→1 `-itana`; 3→4 `-istana`. 2→1 `-ista:sta` ~ `-ista` (ver Pendientes). | `Jupa-w (jupa-r) chura-:na` — 3-AFF (3-COMPL.RU) dar-3>3.REM.C — "ella se lo ha dado (yo lo vi)" | L1 p.145–147, p.164 | Conocimiento personal. Pasado distante con recuerdo propio, sorpresa o contradicción cuando ya se tenía la información (p.147). Las formas de 1.ª y 2.ª persona solo son plenamente funcionales en hablantes mayores (p.146). Se traduce con el pretérito perfecto. |
| REM.L (remoto lejano) | 3→3 `-tayna` (variantes dialectales `-ta:na`, `-ta:ña`, `-taña`). Antes de SIMP con consonante inicial: `-ta:` + sufijo: 1→2 `-ta:sma`; 1→3 `-ta:ta`; 2→3 `-ta:ta`; 4→3 `-ta:tan`; 3→2 `-ta:tam`. Con vocal inicial, reduplicación: 3→1 `-itu:tu`; 3→4 `-istu:stu`; 2→1 `-ista:sta`. | `Jupa-w (jupa-r) chura-tayna` — 3-AFF (3-COMPL.RU) dar-3>3.REM.L — "ella se lo había dado a él (pero yo no vi el acto de dar)" | L1 p.147–148, p.164 | Conocimiento no-personal (rumor, mito, sorpresa por información nueva). Se traduce con el pluscuamperfecto (p.148). 1.ª y 2.ª persona casi no ocurren (p.146). |
| INFR (inferencial) | `-pacha` + terminaciones del SIMP: 3→3 `-pacha`; 1→2 `-pachasma`; 2→1 `-pachista`; 1→3 `-pachata`; 4→3 `-pachatan`; 3→1 `-pachitu`; 3→4 `-pachistu`; 2→3 `-pachata`; 3→2 `-pachatam` (p.165; ver Pendientes). | `chur-pacha-wa` — dar-3>3.INFR-AFF — "el/ella ha debido dar" | L1 p.148–149, p.165 | No-personal: deducción por evidencia indirecta; tiempo de acción paralelo al SIMP. Alta probabilidad; se traduce con «deber» o «a lo mejor» (p.149). Compuestos: con FUT 3→3 `-pachani`, con REM.C 3→3 `-pacha:na` (p.156–157; ejemplos `chur-pachani`, `chur-pacha:na` = "tal vez ella le dará / tal vez él le dio"). |
| NI (no-involucrador, `-chi`) | `-chi` + terminaciones del SIMP: 3→3 `-chi`; 2→1 `-chista`; 3→1 `-chitu`; 3→4 `-chistu`; 1→2 `-ssma` (< \*chsma); 1→3 y 2→3 `-sta` (< \*chta); 4→3 `-stan`; 3→2 `-stam`. | `inas chur-s-ta` — quizás dar-NI-2>3.SIMP — "tal vez diste" | L1 p.69, p.149–152, p.165 | No-personal; hipotético / conjetural / resignación. Nunca con `-wa` ni con preguntas `-sa`/`-ti`; exige `-chim`~`-chix` cuando la situación es alarmante. Reducción /ch/→/s/ crea homofonía (`ap-s-ta` «quizás llevé», de `apa-chi-ta`, coincide con `ap-s-ta` «saqué», de `apa-su-ta`; p.151). Compuestos NI + FUT/REM.L/REM.C/DES/REPR (3→3: `-chini`, `-chitayna`, `-chi:na`, `-chispa(n)`, `-chisapa:na`) en L1 p.158 (Cuadro VII.1). |
| DES (desiderativo) | Marca /s/: 1→2 `-irisma`; 2→1 `-itasma`; 3→3 `-spa`; 1→3 `-irista`; 4→3 `-sna`; 3→1 `-itaspa(n)`; 3→4 `-(i)staspa(n)`; 2→3 `-sma`; 3→2 `-iristam` ~ `-irispa(n)` (p.166). | `Jani-w khuchi-mp ana-k-irist-ti` — NEG-AFF chancho-COM arrear-INCOMPL-1>3.DES-NEG — "prefiero no llevar los chanchos (con las ovejas)" | L1 p.153–154, p.166 | No realizado, futuro en tiempo de acción; deseo, advertencia, recomendación; emotividad positiva. Formas muy irregulares (resultado de dos paradigmas fundidos, nota 9, p.169). Se traduce con condicional o subjuntivo. |
| REPR (reprochador) | DES + `-:na` (REM.C): 1→2 `-iriskasama:na`; 2→1 `-itasama:na`; 3→3 `-sapa:na`; 1→3 `-iriska:ta`; 4→3 `-sana`; 3→1 `-itasapa:na`; 3→4 `-(i)st{u~a}sapana`; 2→3 `-sama:na`; 3→2 `-iriskatama:na`. | `Aymar yati-qa-sama:na` — aymara.O saber-DOWN-2>3.REPR — "Ud. debería haber aprendido aymara" | L1 p.155–156, p.166 | No realizado, pasado en tiempo de acción; reproche o lamento, impacto emotivo siempre negativo; la forma más usada es 2→3. Las formas no son fáciles de predecir (p.155). |
| Saña (verbo de encajamiento: cita / pensamiento) | Raíz `sa-`, única de una vocal, con conjugación irregular: si ante consonante resultaría un grupo inicial se antepone `si-`/`ji-`. SIMP: 1→2 `sissma`~`jissma`; 2→1 `sista`; 3→3 `si`; 1→3 `sista`~`jista`; 4→3 `sistan`~`jistan`; 3→1 `situ`; 3→4 `sistu`; 2→3 `sista`~`jista`; 3→2 `sistam`~`jistam`. | `sista` — decir.1>3.SIMP — "(yo) le digo a él/ella" (irregular, sin segmentar) | L1 p.141–143 | Informa citas de conocimiento no-personal; el subordinador `-sa` (`sa-sa` «diciendo») acompaña al verbo citante. Si cita y `saña` tienen las mismas personas, expresa pensamiento o plan. Con DES/IMP/INFR/NI también antepone `si-`/`ji-` (`sispa`, `sispacha`, `sischi`; p.142). |
| Subordinación general (no es flexión estricta) | `-sa` (v_v), `-sina` (v_c), `-ipana` (c); los independientes se colocan después de ellos. | `pis-t'a-sa-w` — pesar-MOM-SUB-AFF — "tan pronto como yo pese (las papas)"; `jut-xa-sin` — venir-COMPL-SUB — "al regresar" | L1 p.160–161, p.167 | `-sina` es el más frecuente en mitos (suele ir con REM.L), no suele tomar `-wa`; `-sa` sí, y ocurre con el citativo; `-sina` también con el futuro y hechos proyectados (p.160). `-ipana` es poco común y solo con sujetos distintos (en La Paz; p.161). |

### 3.3 Derivativos comunes y negación

Se eligen 15 derivativos por frecuencia (L1 p.130, Apéndice C) o importancia. Nombre de clase/posición: Cuadro VI.1 (L1 p.97).

| Sufijo | Función | Ejemplo | Fuente | Notas |
|---|---|---|---|---|
| `-ya-` (CAUS) | Causativo de agente (Clase II, pos. 1): «hacer que alguien haga». Actúa sobre las personas; puede verbalizar y reduplicarse; admite complemento `-mpi` (nuevo actor). | `apa-ya-ña` — llevar-CAUS-INF — "enviar, mandar" | L1 p.108 | v_. Ante consonante se reduce a `-y-` (`achu-y-ta`, p.80). Reduplicado: `suti-ya-ya-ña` «causar bautizar». Frec. 38. |
| `-cha-` (CAUS.R) | Causativo de raíz/acción (Clase I, pos. 1); verbaliza nominales. | `yati-cha-ña` — saber-CAUS.R-INF — "enseñar" | L1 p.98, p.114 | v_. Combinable con `-ya-`: `yati-cha-ya-ña` «hacer que alguien enseñe» (p.114). Frec. 6. |
| `-si1-` (REFL) | Reflexivo/recíproco (Clase II, pos. 2): acción para uno mismo o entre las personas de la flexión. | `apa-si-ña` — llevar-REFL-INF — "llevarse (uno mismo)" | L1 p.108–109 | v_. No ocurre con `-rapi-` ni `-raqa-`. El más frecuente de todos (88). |
| `-rapi-` (BEN) | Beneficiario (Clase II, pos. 5): añade una persona beneficiaria a la flexión; el nominal toma `-taki` en vez de `-ru`. | `chura-rap-ta` — dar-BEN-1>3.SIMP — "(le) di (pan) para ella" | L1 p.109–110 | v_. Excluyente con `-raqa-`. Frec. 9. |
| `-ni-` (APPR) | Aproximador (Clase II, pos. 3): las personas están cerca o se acercan. | `apa-ni-ña` — llevar-APPR-INF — "traer (acercándose)" | L1 p.109 | v_. Frec. 67. |
| `-waya-` (DIST) | Distanciador (Clase II, pos. 4): personas lejos o alejándose. | `apa-waya-ña` — llevar-DIST-INF — "llevar de paso" | L1 p.109, p.116 | v_. Variantes: `-wa-` si sigue vocal exigida; siempre `-way-` ante consonante. Con `-ni-`: acción circular (`apa-ni-waya-ña` «recoger de paso y traer de vuelta», p.116). Frec. 57. |
| `-si2-` (PROG) | Continuativo (Clase II, pos. 6); siempre con `-ka-`. | `sara-s-ka-ña` — ir-PROG-INCOMPL-INF — "estar yendo" | L1 p.111 | v_. Distinto de `-si1-`. No ocurre con `-xa-`. Frec. 48. |
| `-ka-` (INCOMPL) | Adelantador/incompletivo (Clase II, pos. 7): «adelante»; acompaña a `-si2-`, a `-p-` y al negativo `-ti`. | `sar-ka-ña` — ir-INCOMPL-INF — "ir adelante" | L1 p.111 | c_. No es en sí negativo. Frec. 85. |
| `-xa-` (COMPL) | Completivo respecto a personas (Clase II, pos. 8): acción ya completada. | `chur-xa-ña` — dar-COMPL-INF — "devolver" | L1 p.111, p.115 | c_. Distinto de `-su-` (actúa sobre la raíz). Frec. 85. |
| `-p-` (PL) | Plural del sujeto, del complemento o de ambos (Clase II, pos. 9); opcional. | `parla-p-xa-ña` — hablar-PL-COMPL-INF — "haber hablado ya (plural)" | L1 p.112 | v_. Único derivativo que termina en consonante y que no puede preceder directamente a la flexión: exige luego `-ka-` o `-xa-` (p.112). Frec. 32. |
| `-t'a-` (MOM) | Acción momentánea, corta; suaviza pedidos y mandatos (Clase I, pos. 8); puede verbalizar. | `parl-t'a-ña` — hablar-MOM-INF — "conversar unos pocos minutos" | L1 p.106 | c_. El más frecuente de la Clase I (79). |
| `-ja-` (DIV) | Divisor (Clase I, pos. 2); es el que más verbaliza nominales (`ut-ja-ña`). | `ap-ja-ña` — llevar-DIV-INF — "ayudar a llevar" | L1 p.98–99 | c_. Sentido poco predecible fuera de «dividir». Frec. 40. |
| `-su-` (OUT) | «Hacia afuera» o completivo (Clase I, pos. 3). | `ap-su-ña` — llevar-OUT-INF — "sacar" | L1 p.99 | c_. Completivo: `al-su-ña` «comprar en cantidad». Frec. 26. |
| `-ta-` (UP) | «Hacia arriba» o inceptivo (Clase I, pos. 6). | `ap-ta-ña` — llevar-UP-INF — "levantar, alzar" | L1 p.102 | c_. Inceptivo: `ark-ta-ña` «perseguir». Homófono de otros cuatro `-ta` (ver §5). Frec. 37. |
| `-nta-` (IN) | «Hacia adentro» con verbos de movimiento; inceptivo con los demás (Clase I, pos. 7); puede verbalizar. | `apa-nta-ña` — llevar-IN-INF — "meter, introducir" | L1 p.104 | v_. Inceptivo: `parla-nta-ña` «comenzar a hablar». No coocurre con el nominal `-ta` «de, desde» (p.115). Frec. 12. |
| Negación: `jani`/`jan` … `-ti` | Negación oracional: nominal `jani` (o `jan`) + sufijo oracional `-ti` al final; `-wa` aparece en `jani-w`. | `Jani-w sar-k-i-ti` — NEG-AFF ir-INCOMPL-3>3.SIMP-NEG — "él no ha ido / no va"; prohibición: `jan uka-t pall-ja-ni-p-ka-m-ti` — NEG eso-ABL escoger-DIV-APPR-PL-INCOMPL-2>3.IMP-NEG — "no escojan de ese" | L1 p.111, p.132; `jani` en p.83 | `-ka-` ocurre con regularidad con `-ti` (p.111). Reglas de `jani`, `jan` y `-ti`: ver 7.3 B (L1 p.189, 249–250, 283, 299–302). L2 llama "negativo" a `-ka` (p.232); aquí se glosa INCOMPL (D9). `-ti` también es el interrogativo sí/no (p.68). |

Otros derivativos (en una línea; L1 p.99–110): `-thapi-` juntar, `-ra-` serie/inversa, `-nuqa-` colocar, `-qa-` abajo, `-xata-` encima, `-kata-` a través, `-kipa-` pasar una esquina, `-naqa-` difuso, `-nuku-` alejar/desviar, `-tata-` dispersar, `-xaru-` preparativo, `-xa:si-` sostener, `-xaya-` atención, `-ch'uki-` detenido, `-rpaya-` múltiple/inversa, `-raqa-` victimario. Fosilizados e improductivos: `-ki-`, `-li-`, `-nki-`, `-pa-` (L1 p.95–96).

### 3.4 Contraste con L2 (morfología verbal, L2 pp.175–224)

**Correspondencias de nombres.** La tabla empareja las categorías por su función. **No implica que los análisis sean idénticos:** varios difieren en la forma de cita, la segmentación o el tipo de sufijo (por ejemplo, INFR es un tiempo en L1 y un sufijo independiente en L2). En los ejemplos se usa la segmentación de la fuente de la que vienen (D11).

| L1 (etiqueta de esta guía) | L2 | Marca en L2 | Fuente L2 |
|---|---|---|---|
| SIMP | tiempo presente/pasado (no-futuro) | sin marca | p.183–184 |
| REM.C | pasado testimonial o experimentado | `-yä` (3.ª persona `-¨na`) | p.184–185 |
| REM.L | pasado no testimonial (narrativo, mítico) | `-tä` ~ `-taya` | p.186–187 |
| FUT | futuro (no realizado) | `-¨` ~ `-ŋa` (1), `-¨ta` ~ `-ŋta` (2), `-ni` (3), `-ñäni` (4) | p.187–190 |
| DES | modo potencial u optativo | `-sa` (`sariristha`, `sarasma`, `saraspa`, `sar(a)sna`) | p.192–193 |
| NI | modo dubitativo | `-chi`, reducido a `-s` (`sarstha`, `sarsta`, `sarchi`, `sarstana`); suele ir con `inasa` | p.193–194 |
| INFR | sufijo independiente "dubitativo objetivo" | `-pacha` (`sarpachawa` "ha debido ir"; `qurïpachawa` "debe ser oro") | p.229 |
| IMP | modo imperativo | `-ma`/`-m` (2), `-pa(na)` (3), `-ñäni` (4), `-ita` (2→1) | p.194–197 |
| SUB `-sina` / `-sa` | subordinación de sujeto idéntico, anticipatoria / simultánea | `-sina`, `-sa` | p.198–199 |
| SUB `-ipana` | subordinación de sujetos diferentes ("consecutivo") | `-ipana` (`Tatama jutipana thuqhuñäni` "bailaremos después que venga tu papá") | p.200 |
| Q.SUB `-tixa` | subordinador condicional (sujetos diferentes) | `-tixa` (`Ikïtatixa jaytjawayamawa` "si te duermes, te dejaré") | p.200 |
| PL `-p-` + COMPL/INCOMPL | flexión de número verbal | `-pxa`, un solo morfema (D11) | p.181–182 |
| PROG `-si2-` + INCOMPL `-ka-` | progresivo | `-ska`, un solo morfema (D11) | p.202 |
| MOM `-t'a-` | incoativo / momentáneo | `-t'a` | p.201–202 |
| COMPL `-xa-` | completivo | `-xa` | p.204–205 |
| INCOMPL `-ka-` (con `-ti`) | "negativo" | `-ka` | p.65, 232 |
| `-xa:si-` | estativo | `-xasi` | p.204 |
| `-ra-` | distributivo y contrastivo | `-ra` | p.205 |
| DIV `-ja-` | divisor | `-ja` | p.206 |
| IN / OUT / UP / DOWN | inductivo / eductivo / ascensor / descensor | `-nta` / `-su` / `-ta` / `-qa` | p.208–210 |
| APPR `-ni-` | cislocativo/translocativo | `-ni` | p.211 |
| DIST `-waya-` | incidental | `-waya` | p.213 |
| CAUS / REFL / BEN / VICT | causativo / reflexivo-recíproco / benefactivo / detrimentativo | `-ya` / `-si` / `-rapi` / `-raqa` | p.219–221 |
| CAUS.R `-cha-` | factivo (verbaliza nombres) | `-cha` | p.222–223 |
| VBLZ.PTA `-pta-` | transformativo | `-pta` (`waliptaña` "sanarse") | p.223–224 |
| VBLZ.KA `-ka-` / VBLZ.LONG `-:-` | existencial: `-ka` ("estar") ~ `-¨` ("ser") | `yapupankaña` "estar en su chacra"; `jach'äña` "ser grande" | p.224–225 |

**Paradigma de persona en L2 (p.176–181).** Sujeto: `-tha` (1), `-ta` (2), `-i` (3; tras raíz en /u/ desaparece en singular: `thuqhuwa` "baila"), `-tana` (4). Transiciones: `-sma` (1→2), `-ista` (2→1), `-itu` (3→1), `-tama` (3→2), `-istu` (3→4). L2 no trata 1→3, 2→3 y 4→3 como transiciones aparte: usa las formas de sujeto. Ejemplos: `T'ant'a chursma` "te doy pan"; `T'ant'a churista` "me das pan"; `T'ant'a churitu` "me da pan"; `T'ant'a churtama` "te da pan"; `T'ant'a churistu` "nos da pan" (p.179–180).

**Paradigmas de tiempo en L2 con `sara-` "ir"** (pp.184–190):

| Persona | Presente/pasado | Pasado testimonial | Pasado no testimonial | Futuro | Potencial (= DES) | Dubitativo (= NI) |
|---|---|---|---|---|---|---|
| 1 | `sartha` | `sarayätha` | `saratätha` ~ `sarataytha` | `sarä` ~ `saraŋa` | `sariristha` | `sarstha` |
| 2 | `sarta` | `sarayäta` | `saratäta` ~ `saratayta` | `saräta` | `sarasma` | `sarsta` |
| 3 | `sari` | `saräna` | `saratäna` ~ `saratayna` | `sarani` | `saraspa` | `sarchi` |
| 4 | `sartana` | `sarayätana` | `saratätana` ~ `sarataytana` | `sarañäni` | `sar(a)sna` | `sarstana` |

Plural en L2: se intercala `-px(a)-` (`sarapxtha`, `sarapxayätha`, `sarapxäta`, `sarapxaspa`, `sarapxchi`). Nota: en el plural del pasado testimonial de 3.ª persona L2 escribe `sarapxäna` (p.185).

**Observaciones.**
- La 1.ª persona del futuro alterna en L2 entre alargamiento y la nasal velar `-ŋa` (`saraŋa`), conservada en algunas variedades (p.187). La `ŋ` no está en el alfabeto oficial; tratarla como variante oral.
- L2 llama "intimativo (2→1)" a `-ita`, pero lo describe "de primera a segunda persona" (p.197); por los ejemplos (`¡Churita!` "¡dame!"), el sentido es 2→1, como en L1.
- L2 dice que `-tixa` "requiere la presencia de sufijos de flexión de persona" (p.200); en L1 es el combinado Q.SUB (`-ti` + `-xa`, p.289).

## 4. Sufijos independientes y oracionales

| Sufijo | Tipo (independiente / oracional) | Función | Posición | Ejemplo | Fuente |
|---|---|---|---|---|---|
| -puni ~ -pini | independiente | EMPH: énfasis, "siempre", sorpresa, compromiso | tras sufijos nominales/verbales y antes de flexión y oracionales; orden libre con otros independientes | `jichha-ki-puni-w sar-ta` — ahora-LIM-EMPH-AFF ir-1>3.SIMP — "es la primera vez que voy" | L1 p.273, 283 |
| -ki | independiente | LIM: "no más", suaviza imperativos | igual | `wali-ki-w` — bien-LIM-AFF — "está bien" | L1 p.273 |
| -raki | independiente (actúa a menudo como oracional) | ADD: "también"; además queja, advertencia, objeción, desafío | igual | `aka-x ch'uqi-raki-ki-ti` — esto-TOP papa-ADD-LIM-Q.YN — "¿y esto es papa también?" | L1 p.274–276 |
| -jama | nominal con funciones de independiente | SIM: "como"; con verbos, duda o tentatividad ("parece que") | tras todos los sufijos nominales; antes de otros independientes | `jach'-jama-wa` — grande-SIM-AFF — "es algo grande" | L1 p.276–277 |
| -xa | oracional | TOP: tópico (con -wa); atenuador ("¿está bien?") | final de la palabra; puede repetirse tantas veces como palabras | `sara-:-xa` — ir-1>3.FUT-TOP — "iré, supongo, ¿está bien?" | L1 p.280 |
| -wa | oracional | AFF: afirmativo, conocimiento personal; alomorfo cero tras complemento cero o frase con -ta/-na | solo uno por oración; no en imperativos ni con -chi- | `naya-x sara-:-wa` — 1-TOP ir-1>3.FUT-AFF — "yo voy a ir" | L1 p.280–281 |
| -sa1 | oracional | Q.INF: pregunta de información | con interrogativo | `kuna-s suti-ma-xa` — qué-Q.INF nombre-POSS.2-TOP — "¿cuál es su nombre?" | L1 p.281–282 |
| -ti (pregunta) | oracional | Q.YN: pregunta sí/no | sobre la construcción que se espera en la respuesta | `Mariya-t wawa-r t'ant' chur-i` — María-Q.YN niño-COMPL.RU pan.O dar-3>3.SIMP — "¿dio María pan al niño?" | L1 p.282–283 |
| -ti (negación) | oracional | NEG: obligatorio en toda negativa, junto con jani | donde iría -wa | `jani-w Mariya-:-k-i-ti` — NEG-AFF María-VBLZ.LONG-INCOMPL-3>3.SIMP-NEG — "no fue María" | L1 p.283 |
| -sti | oracional | FOLL: "seguidor del tema"; cortesía; puede reemplazar a -xa, -sa1, -ti | puede repetirse en la oración | `jupa-sti Karlu sa-ta-w` — 3-FOLL Carlos decir-NMLZ.RES-AFF — "y él se llama Carlos" | L1 p.283–284, 310 |
| -ya | oracional | POL: cortesía, vocativo, atenuador | donde iría cualquiera de los 4 primeros; frecuente con imperativo | `juma-ki-y amuy-t'a-m` — 2-LIM-POL pensar-MOM-2>3.IMP — "piénsalo tú" | L1 p.284 |
| -sa2 | oracional | CAT: catalogador (listas), indefinido con interrogativo, enlaza oraciones | | `jani-w kun-sa` — NEG-AFF qué-CAT — "nada" | L1 p.285–286 |
| -cha | oracional | Q.ALT: pregunta alternativa ("o") | segunda alternativa; también atenúa | `yuqalla-t imilla-cha` — muchacho-Q.YN muchacha-Q.ALT — "¿es varón o mujer?" | L1 p.286 |
| -pi | oracional | CERT: "por supuesto" | rara vez sin -: | `wali-k-pi` — bien-LIM-CERT — "está bien, por supuesto" | L1 p.286 |
| -: | oracional | EXCL: exclamatorio | suele ir tras otro oracional | FALTA ejemplo limpio (L1 p.287 da uno con ut-j sin glosar) | L1 p.287 |
| -chi- (+ -m / -xa) | oracional | SUPP: suposicional | exige -m o -xa detrás; solo con flexión no-involucrador (NI) | `uka-x ch'usa uta-ki-:-chi-xay` — eso-TOP vacío casa-LIM-VBLZ.LONG-SUPP-TOP.POL — "pero esa casa está tan vacía" | L1 p.287–288 |
| -xaya / -xa: | oracional (comb.) | TOP.POL | combinaciones con -: y -ya posibles con todos menos -chi- | ver ejemplo de -chi- | L1 p.287–288 |
| -waya | oracional (comb.) | AFF.POL: baja la importancia sin invalidar | | FALTA ejemplo glosable (L1 p.288 da `…-ki-way` con uñ-j-t' sin glosar) | L1 p.288 |
| -saya / -sa: | oracional (comb.) | CAT.POL / CAT.EXCL "pero" | | `aymar parl-xa-rak-ta-sa:` — aymara.O hablar-COMPL-ADD-2>3.SIMP-CAT.EXCL — "¡pero si Ud. ya habla aymara!" | L1 p.276, 288 |
| -piya / -piy | oracional (comb.) | CERT.POL: añade fuerza; combinación muy frecuente | | `Juta-ki-:ta-piy` — venir-LIM-2>3.FUT-CERT.POL — "venga nuevamente, por favor" | L1 p.289 |
| -tiya / -tixa | oracional (comb.) | Q.SUB: marca interrogativos y -ti en subordinadas | en cláusulas con uka | `kuna-tiy wakis-k-i uka` — qué-Q.SUB necesario-INCOMPL-3>3.SIMP eso — "todo lo que sea necesario, eso" | L1 p.289–290, 317 |
| -chim / -chix / -tisti | oracional (comb.) | suposición / pregunta de duda y perplejidad | máximo dos oracionales por palabra | `nina-xa-chi-m` ~ `nina-:-chi-m` — fuego-POSS.1-SUPP — "puede ser mi fuego" (L1 p.205; la `-m` final no se glosa por separado†); `-tisti`: `juma-naka-st yati-si-xa-sma-tisti` — 2-PL-FOLL saber-REFL-COMPL-2>3.DES-Q.YN.FOLL† — "¿pero Uds. se acostumbrarían allí?" (L1 p.290) | L1 p.205, 289–290 |

Nota: no se hallaron combinaciones de más de dos sufijos oracionales (L1 p.287).

### 4.1 Contraste con L2 (sufijos independientes y oracionales, L2 pp.225–238)

L2 divide los oracionales en afirmativo/negativos e interrogativos. Según L2, "generalmente" van una sola vez por oración (con excepciones) y solo en los constituyentes mayores de la oración principal (p.230).

| Sufijo | Nombre en L2 | Etiqueta de esta guía | Ejemplo de L2 | Fuente L2 | Comparación con L1 |
|---|---|---|---|---|---|
| `-raki` | "similativo" (también advertencia o amenaza) | ADD | `jupaxa anatarakiwa` "él/ella también juega"; `Anumaraki achjitaspa` "cuidado, me muerde tu perro" | p.225–227 | Coincide. El nombre "similativo" no debe confundirse con SIM (`-jama`) |
| `-ki` | limitativo | LIM | `t'ant'aki alaniwaytha` "pan nomás compré" | p.227–228 | Coincide |
| `-puni` | certitudinal | EMPH | `jupapuniwa lurani` "él/ella siempre lo hará" | p.228 | Coincide |
| `-pacha` | dubitativo objetivo | INFR | `sarpachawa` "ha debido ir" | p.229 | L1 lo trata como tiempo verbal inferencial (p.148–149); L2, como independiente que también se usa con nombres (`qurïpachawa` "debe ser oro") |
| `-wa` | declarativo (fuente primaria, conocimiento de causa) | AFF | `mamajaxa jutaniwa` ~ `mamajawa jutani` "mi mamá vendrá" | p.230–231 | Coincide; marca la palabra más enfatizada |
| `-xa` | topicalizador (por lo general marca el sujeto; puede repetirse) | TOP | `jilaqataxa janiwa jutkaniti` "la autoridad no vendrá" | p.231 | Coincide |
| `-ti` | negativo (con `jani` y `-ka`) / interrogativo sí-no | NEG / Q.YN | `janiwa khitisa sarkaniti` "nadie irá"; `¿jilamaxa jutaniti?` "¿vendrá tu hermano?" | p.231–232, 235–236 | Coincide. L2 presenta `-ka` como parte de la negación ("para completar la idea de negación", p.231–232); L1 dice que suele ir pero no es obligatorio (p.283, 301) |
| `-ya` | enfático propositivo (satisfacción, disgusto, ruego) | POL | `¡jinaya sarañäni!` "¡vamos pues!" | p.232–233 | Coincide |
| `-pï` | enfático afirmativo | CERT | `ukhamapï` "así es pues" | p.233 | L1 escribe `-pi` y dice que rara vez va sin `-:` (p.286); L2 escribe la vocal larga dentro del sufijo |
| `-sa` | conectivo (coordinación) | CAT | `ch'uqisa apillasa` "la papa y la oca" | p.234 | Coincide con `-sa2` |
| `-sa` (con `jani`) | negativo condicional, "mejor no" | ‡ NEG.COND (no está en la lista de L1) | `janisa sarkamti` "mejor no vayas"; `janisa jutkpanti` "mejor que no venga" | p.234–235 | No figura en las tablas de esta guía tomadas de L1; verificar en L1 cap. XI |
| `-sa` (con interrogativo) | interrogativo informativo | Q.INF | `¿kawkirusa sarañäni?` "¿a dónde iremos?" | p.236 | Coincide con `-sa1` |
| `-sti` | interrogativo reanudador ("¿y…?") | FOLL | `¿jumasti?` "¿y tú?"; `¿jilamasti?` "¿y tu hermano?" | p.237 | Coincide |
| `-cha` | interrogativo conjuntivo ("¿o…?") | Q.ALT | `¿usutacha?` "¿o está enferma?" | p.237–238 | Coincide |

## 5. Cambios al unir sufijos

### 5.1 Según L1

| Regla | Antes → Después | Qué sufijos la provocan | Fuente | Notas |
|---|---|---|---|---|
| Retención / supresión regresiva de la vocal final | `chura- + -ta(c_c) + -wa` → `chur-t-wa` «yo doy/di»; `chura- + -ta(v_c) + -wa` → `chura-ta-wa` «lo dado» | Todo sufijo: «sigue a consonante» = suprime la vocal del morfema anterior; «sigue a vocal» = la retiene. Cada sufijo impone su condición (Cuadros IV.1–IV.7). | L1 p.67–68, p.70 | Proceso dominante de la morfofonémica aymara; el condicionamiento morfológico predomina sobre el fonológico (p.21). `-wa` oracional no impone nada: lo deciden el morfema previo y la sintaxis (p.68). |
| Lista de derivativos por vocal/consonante previa | `apa- + -ni-` → `apa-ni-ña` (retiene) frente a `apa- + -ta-` → `ap-ta-ña` (suprime) | v_ (piden vocal antes): `-cha-`, `-kipa-`, `-ni-`, `-nta-`, `-nuku-`, `-p-`, `-qa-`, `-ra-`, `-rapi-`, `-raqa-`, `-rpaya-`, `-si1-`, `-si2-`, `-tata-`, `-waya-`, `-ya-`. c_ (piden consonante antes): `-ch'uki-`, `-ja-`, `-ka-`, `-kata-`, `-naqa-`, `-nuqa-`, `-su-`, `-ta-`, `-t'a-`, `-thapi-`, `-xa-`, `-xaru-`, `-xa:si-`, `-xata-`, `-xaya-`. | L1 p.113 (cf. p.102, p.109) | Los que empiezan por /w/, /r/, /y/ o por grupo consonántico piden vocal; todos los que empiezan por /x/ piden consonante (p.113). Un tronco previo actúa como raíz de dos vocales, sea cual sea su longitud (p.114). Ejemplos: `al-j-kata-ña` «venderlo todo» (p.103); `sara-q-ta-waya-ña` (p.115). |
| Raíces de tres o más vocales | `ch'iyara uta` → `ch'iyar uta` «casa negra»; `uta` y `ch'uxña` conservan su vocal | Construcciones sintácticas complejas; se aplica con limitación en la formación de nominales. | L1 p.68, p.113–114 | Ante sufijos, la vocal final de estas raíces se suprime con frecuencia sin importar el sufijo (p.113–114). |
| Verbos nominalizados antes del verbo principal | `liyi-ña` → `liyi-ñ` (con `yati-qa-ñ`, `mun-t-wa`) | `-ña`, `-iri` (nominalizadores de la frase verbal). | L1 p.72 | Todas esas formas tienen tres vocales o más y pierden la vocal final. Ejemplos: `Liyi-ñ yati-qa-ñ mun-t-wa` «quiero aprender a leer»; `Uñ-j-ir sara-:` «iré a ver». |
| Reducción de geminadas consonánticas | `aka-n-ka-ka-t-ti` → `aka-n-k-k-t-ti` /akankti/ (escrito `akankktti`) | Cadena de supresiones que deja consonantes iguales contiguas (alomorfo cero). | L1 p.68 | La geminación puede recuperarse al pronunciar: /akanktti/. Ejemplo: `Jani-w akankktti` «no estoy aquí». Discrepancia de grafía: ver Pendientes. |
| Grupos vocálicos geminados | `uka aru-wa` → /ukaruwa/; `kawki + -:- + -iri` → /kawkiri/ «cuál» | Retención vocálica en frase nominal con vocal final del modificador = vocal inicial del núcleo; límites de morfema. | L1 p.69 | Pueden dar vocal larga o reducirse a vocal simple; en los límites morfémicos suelen reducirse. |
| Predominio de /u/ | `usu- + -itu` → `us-utu` «estoy enfermo»; `katu- + -iri` → `katu-ri` «el que agarra»; `irpsu- + -ita:ta` → `irpsu-täta` «tú me vas a sacar» | Sufijos que empiezan por /i/ tras una raíz o sufijo terminado en /u/ (`-itu`, `-iri`, `-ita:ta`). | L1 p.69 | La /u/ final domina a la /i/ inicial del sufijo siguiente. En el texto extraído de L1 aparecen como `–citu`, `–ciri`, `–citäta`: la *c* es el subíndice "pide consonante antes" (L1 p.67). L1 escribe aquí `-itäta` con diéresis (p.69). |
| /ch/ → /s/ | `chura- + -chi + -ta` → `chur-s-ta` «tal vez diste»; `apa- + -chi + -ta` → `ap-s-ta` «quizás llevé» | `-chi` (no-involucrador y sus compuestos). | L1 p.69, p.151 | Ocurre cuando /ch/ deja de ser la consonante final del grupo; el geminado resultante se reduce. `ap-s-ta` «quizás llevé» es homófono de `ap-s-ta` «saqué» (de `apa-su-ta`; p.151), lo que lleva a reducir el NI casi a 3→3. |
| /j/ → aspiración /h/ | `-j-` → `-h-` tras oclusiva | Sufijos que empiezan por /j/ (sobre todo los nominales `-ja`, `-jama`). | L1 p.69–70 | Fosilizado en `ukhama` «así» y `akhama` «de este modo». La forma base sin aspiración: FALTA en L1. |
| Alargamiento vocálico | `chura- + -:na` → `chura-:na` (la vocal se conserva) | Morfemas que son o empiezan con alargamiento (`-:`, `-:ma`, `-:ta`, `-:tam`, `-:na`). | L1 p.71, p.22 | Piden vocal previa. Si les sigue un sufijo que pide consonante, el alargamiento se acorta pero la vocal no se suprime: la vocal ante un sufijo c_ revela el alargamiento oculto. Una vocal larga final nunca se suprime. |
| /i/ inicial pide consonante | `irpa- + -itani` → `irp-itani` «me llevará» | Sufijos con /i/ inicial (`-itu`, `-ista`, `-itani`, `-iri`…). | L1 p.71 (ej. p.73) | No hay grupos vocálicos (diptongos) en aymara. `i` es la única vocal inicial de sufijo. |
| Reducción ante consonante de `-ya-`, `-rapi-`, `-waya-` | `achu-ya- + -ta` → `achu-y-ta`; `chura-rapi- + -ta` → `chura-rap-ta`; `-waya-` → `-way-` | Sufijos que piden consonante antes (`-ta` 1→3, `-ka-`, `-t'a-`…). | L1 p.80, p.108, p.110; `-waya-` p.109 | `-waya-` varía libremente con `-wa-` si lo que sigue pide vocal; ante consonante es siempre `-way-`. Ejemplos: `phutukraphiy-t'a-ni-way-ta` (p.116); `sara-way-k-xa-:` (p.112). |
| Complemento cero | `t'ant'a` → `t'ant'`; `Mariya` → `Mariy` | Nominal complemento del tronco verbal, sin sufijo nominal; se marca solo por perder la vocal final. | L1 p.72, p.86 | Inhibe `-wa` salvo que sea la última palabra de la oración. Ejemplos: `t'ant' chur-i`; `Mariy q'ipi-xa` «llevó a María». |
| Frase nominal: el modificador conserva su vocal | `aka jathi q'ipi-wa` «este atado pesado» | Modificador + núcleo (salvo modificadores de ≥3 vocales). | L1 p.71 | Regla sintáctica; con varios modificadores depende de los constituyentes inmediatos (p.71). |
| Prefijo `si-`/`ji-` en `saña` | `sa- + -ta` → \*`sta` → `sista` ~ `jista` | Sufijos flexionales que piden consonante previa y producirían grupo inicial (SIMP, DES, IMP, INFR, NI). | L1 p.141–142 | Variación libre `si-`/`ji-`. Ejemplos: `sissna`, `sispa`, `sispacha`, `sischi` (p.142). Algunos dialectos sí admiten grupos iniciales (nota 3, p.169). |
| Homófonos distinguidos por c/v | `q'ip-t-wa` (1→3), `q'ip-ta-wa` (2→3), `q'ipi-ta-wa` (NMLZ «lo cargado»), `q'ipi-t-wa` (ABL «del atado»), `q'ip-ta-` (tronco con `-ta-` UP «alzar un atado») | Los cinco `-ta` (c_c, c_v, v_v, v_c y derivativo c_). | L1 p.77 (Cuadro IV.8) | La morfofonémica diferencia homófonos: la presencia o ausencia de vocal ante `-ta` revela de cuál se trata. |
| Condicionamiento según la clase de sufijo | — | Flexionales: especifican ambiente antes y después. Derivativos verbales: solo el previo (excepto `-p-`, que también condiciona lo que sigue: no puede preceder directamente a la flexión). Nominales: el previo. Independientes: exigen vocal previa. Oracionales: se acomodan. Alternadores temáticos: patrón propio. | L1 p.70 | Los derivativos del verbo están determinados por la flexión o por el derivativo siguiente. Todas las tablas de condicionamiento (c/v) están en IV.1–IV.7 (p.74–77). |

### 5.2 Según L2 (y comparación con L1)

| Regla | Antes → Después | Qué sufijos la provocan | Fuente | ¿Coincide con L1? |
|---|---|---|---|---|
| Elisión de la vocal precedente (sufijo "fuerte", Ross) | `lura+tha+wa` → `lur(a)-th(a)-wa` → `lurthwa` — hacer-1>3.SIMP-AFF — "hago"; `lur(a)-ta-wa` → `lurtawa` — hacer-2>3.SIMP-AFF — "haces"; `an(u)-jama` — perro-SIM — "como el perro"; `mun(a)-th(a)` — querer-1>3.SIMP — "quiero"; `ap(a)-ta` — llevar-2>3.SIMP — "llevas"; `sar(a)-i` — ir-3>3.SIMP — "fue/va"; `jut(a)-pana` — venir-3>3.IMP — "que venga" (imperativo de 3.ª persona, L2 p.195) | Fuertes (L2 p.62–63): -jama, -tha, -ta (2), -i (3), -pana, -su, -kata, -xa (jawirpatxa) | L2 p.60–63 | Sí en el mecanismo (el sufijo hace caer la vocal). L1 lo expresa como exigencia C/V del sufijo; L2, como propiedad idiosincrática de cada morfema (p.66) |
| Sufijo "débil": conserva la vocal precedente | `anu-ma` — perro-POSS.2 — "tu perro"; `uta-ni` — casa-POSR — "dueño de casa"; `warmi-pura` — mujer-AMONG† — "entre mujeres"; `sara-ñäni` — ir-4>3.FUT — "vamos"; `manq'a-ña` — comer-INF — "comer" | Débiles (L2 p.62–63): -ru, -mpi, -taki, -ni, -raki, -ya, -layku, -rara, -cha, -pura, -ña, -ma | L2 p.60–63 | Sí (equivale a "conserva la vocal") |
| Sufijo "dúctil": según L2, "a veces" elide la vocal previa y "otras veces" no | Formas atestiguadas en L2: `an-ma` y `anu-ma` "tu perro"; `uk-nama` y `uka-nama` "por ese lado"; `ap-naqa-ña` y `apa-naqa-ña` "manejar" (la segmentación con guion es del extractor†; L2 escribe `an.ma`, `uk.nama`, `ap.naqa.ña`) | Dúctiles (L2 p.62–64): `-kama`, `-sti`, `-chiqa ~ -chaqa`, `-ya`, `-pacha`; en los ejemplos de la p.62 también `-ma`, `-nama`, `-naqa` | L2 p.60–64 | **Diferencia de enfoque.** L1 asigna a cada sufijo una exigencia fija (pide vocal o pide consonante), pero para algunos da condiciones que explican parte de la variación (ver 5.2.1). L2 no da condiciones. **No es alternancia libre: el generador no debe producir variantes** (D7) |
| La vocal propia de -tha cae ante -wa; la de -ta (2) se conserva | `th(a)-wa` → `thwa`; `ta-wa` → `tawa` | L2 no dice cuál de los dos morfemas lo provoca (p.61) | L2 p.61 | **No** coincide el sufijo de 1.ª persona (L1 `-ta`, L2 `-tha`) |
| 3.ª y 4.ª persona | `lur(a)-i-wa` → `luriwa` — hacer-3>3.SIMP-AFF — "hace"; `lura-ñäni-wa` → `lurañäniwa` — hacer-4>3.FUT-AFF — "hacemos" (así traduce L2; `-ñäni` es futuro/exhortativo, "haremos, hagamos"; el presente de 4.ª persona es `lurtanwa`, L2 p.178) | El texto dice "no existe la pérdida de vocales", pero su propia tabla pone `lur(a).i.wa` y `sar(a)+i` | L2 p.61–62 | Contradicción interna de L2. L1: `-i` (3→3) pide consonante antes (`chur-i`, p.144), así que la vocal de la raíz sí cae |
| Hacinamiento y geminación consonántica (consecuencia de las elisiones; hasta 6 consonantes seguidas). Se escribe el grupo; en habla rápida se fusiona | `yat(i)-x(a)-th(a)-wa` → `yatxthwa` — saber-COMPL-1>3.SIMP-AFF — "ya sé"; `jut(a)-th(a)-wa` → `jutthwa` — venir-1>3.SIMP-AFF — "vine"; `manq'(a)-th(a)-wa` → `manq’thwa` — comer-1>3.SIMP-AFF — "como"; `jiskh(i)-t'(a)-k(a)-th(a)-ti` → `jiskht’kthti` — preguntar-MOM-INCOMPL-1>3.SIMP-NEG — "no pregunté" (L2 llama "negativo" a `-ka`; ver D9) | Sufijos fuertes encadenados (-t’a, -ka, -tha, -xa, -ti) | L2 p.64–65 | Sí en el efecto (L1: chur-t-wa) |
| Elisión intraléxica idiosincrática: depende de cada morfema, no de la sílaba ni del acento | Ver filas anteriores | Cada morfema | L2 p.66 | Sí (L1: "cada sufijo exige…") |
| Pérdida de y/w entre vocales idénticas → vocal larga | `maya` ~ `mä`; `phayaña` ~ `phäña`; `wawanaka` ~ `wänaka` — niños — "niños"; `chayaka` ~ `chäka` | Ninguno (proceso léxico) | L2 p.43, p.57 | Sí en el resultado: L1 escribe `ma:` "uno" (p.295) y su texto corrido `mä`, `pä` (p.57–58) |
| Pérdida de segmentos que deja vocal larga en el verbo | `chura-¨` → `churä` — dar-1>3.FUT — "yo daré"; `muna-yätha` → `munayätha` — querer-1>3.REM.C — "yo quería" | -¨ (FUT.1), -¨ta (FUT.2), -yätha / -tätha (pasados) | L2 p.55–56 | Parcial (L1 `sara-:` ↔ L2 `sarä`) |
| Cópula kankaña reducida | `jach'a kankthwa` → `jach’äthwa` — grande-VBLZ.LONG-1>3.SIMP-AFF† — "soy grande"; `utana kankthwa` → `utankthwa` — "estoy en casa" (con vestigio, sin diéresis) | Persona verbal (-tha) | L2 p.50–51 | Sí en la forma, no en el análisis: L1 no deriva `-:-` ni `-ka-` de un verbo `kankaña`; los trata como verbalizadores defectivos (VBLZ.LONG, VBLZ.KA; p.89, 162, 236–240) |
| Fusión vocálica en compuestos | `jach'a uru` → `jach’üru` — "gran día"; `phaxsi uru` → `phaxsüru` — "día lunes" (L2 imprime `Paxsi`) | Ninguno (límite entre palabras) | L2 p.53–54 | Parcial: L1 describe la fusión de vocales iguales entre modificador y núcleo (`uka aru-wa` = /ukaruwa/, p.69), pero no como composición |
| `-ipana` tras vocal | `uru-ki-ipana` → `urukïpana` (análisis de L2) | `-ipana`, que según L2 p.53 expresa "un deseo para 'que sea'" y es el único sufijo que empieza y termina en vocal (afirmación inexacta: también `-i`, `-iri`, `-itu`, `-ista` empiezan en vocal) | L2 p.53 | **Diferencia no resuelta.** L1 solo describe `-ipana` como subordinador poco frecuente con sujetos distintos (p.161), igual que L2 p.200 (`Tatama jutipana thuqhuñäni`). El uso desiderativo de L2 p.53 no figura en L1. **Hipótesis del revisor (‡), no confirmada por ninguna fuente:** `uru-ki-:-pana` (alargamiento "ser" + imperativo de 3.ª `-pana`, L2 p.195). Pendiente de verificación; no usar como regla |
| Desonorización interléxica (la vocal final se debilita en la frase pero **se escribe**): modificadores de ≥3 sílabas en frases nominales; complementos de frase verbal | `machaqa mara` (modificador trisílabo; L2 p.67 no da la forma oral); `t'ant'a muntha` [t’ant’(a) muntha] — "quiero pan"; `awichax(a) wak(a)w(a) awati` → `Awichaxa wakwa awati` — "La abuela pastea la vaca" | No son sufijos: es un proceso sintáctico | L2 p.66–70 | **No**. L1 trata la caída de la vocal del complemento cero como obligatoria y gramatical (p.233) y la de las raíces de 3 vocales como regla (p.68); L2, como desonorización que no se escribe. Ver D6 |
| Cambio fonético junto a postvelares (no se escribe) | `iqiqu` → [eqeqo] | Consonantes /q, qh, q’, x/ | L2 p.45 | Sí: L1 dice que las postvelares hacen las vocales más abiertas y posteriores (p.22) |
| Adaptación de préstamos | `lápiz` → `lapisa` | Ninguno | L2 p.77 | **No** en la escritura: L1 escribe el préstamo sin vocal final añadida (`lapis ala-sa-w`, p.316; `liwru`, `misa`, `Mariya` sí terminan en vocal). Convertir con la tabla 8.4 |

### 5.2.1 Respaldo de cada sufijo "dúctil" (v3)

Condiciones que **sí** están documentadas, sufijo por sufijo. Lo que no aparece aquí no tiene condición documentada.

| Sufijo | Clasificación en L2 | Formas atestiguadas en L2 | Qué dice L1 | Condición documentada | Estado |
|---|---|---|---|---|---|
| `-kama` | Débil (`uta.kama`, p.62) **y** dúctil (p.62) | Con elisión: `suykama`, `tumpkama`, `puriñkama`, `jikisiñkama`; sin elisión: `utakama`, `markakama`, `qullukama`, `tunkakama`, `payakama` (p.62) | Tiene la morfofonémica de `-layku` (p.228): la raíz **conserva** su vocal final salvo que tenga **tres o más vocales**; tras una frase nominal "puede o no" suprimirla (p.199) | Parcial (L1): explica `puriñkama` y `jikisiñkama` (raíces de 3 vocales) y las formas sin elisión; no explica `suykama` ni `tumpkama` | Pendiente |
| `-sti` | Dúctil (p.62–63) | `¿jichhasti?`, `¿purinisti?`, `¿jumasti?`, `¿ukatsti?` (p.63) | Oracional: los oracionales "se acomodan" al ambiente previo (p.70) | Ninguna explícita; `ukat-sti` sigue a `uka-t` (ABL ya sin vocal) | Pendiente |
| `-chiqa ~ -chaqa` | Dúctil (p.63) | `thakhichiqa`, `qulluchiqa`, `uyuchiqa`, `satachaqana`, `jawirchaqa` (p.63) | L1 trata `chiqa` como raíz "recto, verdad" (p.174) que funciona en frases posicionales: `manqha chiqa` "directamente por el interior", `Taypi chiqan ut.j.i` (p.246) | Ninguna | Pendiente |
| `-ya` "pues" | Débil (`tiwanaya`, `utaya`…) **y** dúctil (`sarpaya`, `saramaya`, `sarajaya`) (p.63) | Las de la izquierda | Oracional (POL): "se acomoda" (p.70) | Ninguna. En los ejemplos dúctiles, `-ya` sigue a formas verbales (`sar-pa`, `sara-ma`) | Pendiente |
| `-pacha` "todo" | Dúctil (p.63–64) | `taqpacha`, `kimspacha`, `jiwaspacha`, `jupapacha` | Todos los `-pacha` piden consonante antes; `taq.pacha` es fosilizado (p.209) | Contradicción entre fuentes | Pendiente |
| `-ma` POSS.2 | Débil (`anu.ma`) **y** dúctil (`an.ma ~ anu.ma`) (p.62) | `anuma`, `anma` | Los posesivos "requieren de una vocal que los preceda" (p.205) | Contradicción entre fuentes | Pendiente |
| `-nama` | Dúctil (`uk.nama ~ uka.nama`, p.62) | `uknama`, `ukanama` | `-nama` "a través de" (Tiwanaku) pide consonante antes (p.230) | Contradicción entre fuentes | Pendiente |
| `-naqa-` | Dúctil (`ap.naqa.ña ~ apa.naqa.ña`, p.62) | `apnaqaña`, `apanaqaña` | Derivativo que pide consonante antes (p.113) | Contradicción entre fuentes | Pendiente |
| `-pura` | Débil (p.62) | `warmipura`; `kullakpura` (p.167) | `qam-ir-pura`, `jupa-nak-pura` (p.199) | L2 p.167: elide tras raíz de 3 o más sílabas | Confirmada (como condición de L2) |

### 5.3 Pérdida de vocales finales: tres niveles (v3)

| Nivel | Qué es | L1 | L2 | Escritura normalizada (L2) | Uso en el generador |
|---|---|---|---|---|---|
| (a) Elisión morfológica dentro de la palabra | El sufijo siguiente hace caer la vocal del morfema anterior | Exigencia c/v de cada sufijo (p.67–77): `chur-t-wa` "yo doy/di" | Sufijos fuertes (p.60–66): `lurthwa` "hago"; `yatxthwa` "ya sé"; se mantienen por escrito (p.66) | **Se escribe la elisión** | Sí, solo con la condición documentada de cada sufijo (5.1, 5.2) |
| (b1) Complemento cero | Nominal objeto sin sufijo, junto al verbo | Pérdida "obligatoria" de la vocal final; es la marca gramatical (p.233): `t'ant' chur-i` (p.87) | Desonorización oral; se escribe completa: `T'ant'a muntha` (p.67); `Nayaxa wawaru t'ant'a churtha` (p.155) | **Vocal completa** | No aplicar la regla de L1 en la escritura |
| (b2) Modificador de 3 o más vocales | Adjetivo u otro modificador ante el núcleo | Pierde la vocal: `ch'iyar uta` "casa negra" (p.68); `ch'iyar ch'uqi-wa` (p.245) | Desonorización; se escribe completa: `Ch'iyara phisi` "gato negro", `Aymara aru` (p.67) | **Vocal completa** | No aplicar la regla de L1 en la escritura |
| (b3) Verbo nominalizado ante el verbo principal | `-ña`, `-iri` | Pierde la vocal: `Liyi-ñ yati-qa-ñ mun-t-wa` "quiero aprender a leer"; `Uñ-j-ir sara-:` "iré a ver" (p.72) | Se escribe completa: `Manq'iri sarañäni` "vamos a comer"; `¡Anatiri jutama!` "¡ven a jugar!" (p.67) | **Vocal completa** | No aplicar la regla de L1 en la escritura |
| (c) Realización oral | Ensordecimiento o caída al hablar | L1 la transcribe en su escritura | `[Tatax(a) utaruw(a) sari]` → `Tataxa utaruwa sari` (p.68) | No se representa | No |

Caso límite documentado: en `Awichaxa wakwa awati` "la abuela pastea la vaca" (L2 p.68), L2 escribe `wakwa` (waka + `-wa`): la elisión es **dentro de la palabra**, nivel (a), y L2 la mantiene, mientras restituye las vocales finales de palabra. Por tanto, el nivel (b) no autoriza a borrar vocales dentro de la palabra ni el (a) a borrarlas entre palabras.

## 6. Español → Aymara

| En español | En aymara se hace… | Ejemplo | Fuente |
|---|---|---|---|
| el, la, un, una | No hay artículos. "Un/una" puede ser `ma:` "uno"; el nominal sin marca no indica singular ni definitud. Los demostrativos van antes del nombre. | `ma: tata-w pata-tuqi-n ma: iskuyla-r pur-i` — uno señor-AFF altiplano-alrededor-LOC uno escuela-ALL llegar-3>3.SIMP — "un señor llega a una escuela en el altiplano" | L1 p.295, 206 |
| a, de, en, con, para, hasta, desde, por | Sufijos de caso: a = -ru; de/desde = -ta; en/de (posesión) = -na; con = -mpi; para = -taki; hasta = -kama; por (causa) = -layku. | `marka-ru-w sar-ta` — pueblo-ALL-AFF ir-1>3.SIMP — "fui al pueblo"; `qhatu-t jut-ta` — mercado-ABL venir-1>3.SIMP — "vengo del mercado"; `jichha-kama` — ahora-UNTIL — "hasta ahora"; `manu-layku-w jut-ta` — deuda-CAUSE-AFF venir-1>3.SIMP — "vine a causa de una deuda" | L1 p.210–230, 199 |
| ser / estar | Equivalencia sin cópula (-xa … -wa); "ser X" con verbalizador -:- + flexión; "estar en / ser de" con -n-ka- (-na + -ka-). | `misa-x jach'a-wa` — mesa-TOP grande-AFF — "la mesa es grande"; `naya-x Juwana Waskisa-:-t-wa` — 1-TOP Juana Vásquez-VBLZ.LONG-1>3.SIMP-AFF — "yo soy Juana Vásquez"; `misa taypi-n-k-i-w` — mesa medio-LOC-VBLZ.KA-3>3.SIMP-AFF — "en medio de la mesa" | L1 p.172, 239, 237, 296 |
| tener | Poseedor -ni (+ -:- si lleva flexión); o poseedor-na + poseído con POSS; también el verbo ut.ja.ña "existir, pertenecer a". Obligación: -ña + -ni. | `naya-x pusi uta-ni-:-t-wa` — 1-TOP cuatro casa-POSR-VBLZ.LONG-1>3.SIMP-AFF — "tengo cuatro casas". L2 escribe esta construcción **sin diéresis**: `Nayaxa pä/paya utanithwa` "yo tengo dos casas" (L2 p.57; también `masinakanithwa`, p.47) | L1 p.203–204, 257–258; L2 p.47, 57 |
| no | `jani` + -wa en jani y -ti donde iría -wa; el verbo suele llevar -ka- (no obligatorio). Respuestas a -sa: `jani-w` + interrogativo con -sa2. | `jani-w Mariya-:-k-i-ti` — NEG-AFF María-VBLZ.LONG-INCOMPL-3>3.SIMP-NEG — "no fue María" | L1 p.283, 299–302 |
| pregunta sí/no | -ti sobre el elemento preguntado; -xa atenuado ("¿está bien?"). | `Mariya-t wawa-r t'ant' chur-i` — María-Q.YN niño-COMPL.RU pan.O dar-3>3.SIMP — "¿dio María pan al niño?" | L1 p.282, 299 |
| pregunta con qué/quién/dónde | Interrogativo (khiti, kuna, kawki, qawqha, kamisa) + -sa1; con casos: `kuna-ru-s`, `kawki-n-s`… | `kawki-ru-s sar-ta` — dónde-ALL-Q.INF ir-2>3.SIMP — "¿dónde fuiste?" | L1 p.185–187, 213 |
| "que" (relativa) | No hay pronombre relativo: la subordinación se logra con `uka` como resumidor, -xa/-sa2/-tixa en lugar de -wa, y interrogativos con -tixa/-tiya que pasan a indefinidos. | `kuna-tiy wakis-k-i uka` — qué-Q.SUB necesario-INCOMPL-3>3.SIMP eso — "todo lo que sea necesario, eso" | L1 p.289, 317, 321 (nota 4) |
| pronombres yo, tú, él, nosotros | `naya` (1), `juma` (2), `jupa` (3), `jiwasa` (4, "tú y yo"); sin género ni número; -naka solo de énfasis. | `jiwas-pach sara-ñani` — 4-SELF ir-4>3.FUT — "nosotros personalmente iremos" | L1 p.182, 228 |
| y / pero (coordinación) | y = -mpi (o -sa2 en listas, o yuxtaposición); o = -cha; también = -raki; pero = -sa: o `uka-x`. | `juwanti-mp piruti-mp juma-mp sara-ñani` — Juan-COM Pedro-COM 2-COM ir-4>3.FUT — "vayamos tú, Juan, Pedro y yo" | L1 p.208, 285, 312 |
| cuando / si / porque (subordinadas) | cuando/mientras (acciones cercanas): verbo-sa / -sina; "para": -iri / -ña-taki; "si": desiderativo + -xa o dos cláusulas yuxtapuestas; con sujetos distintos, L2 da `-tixa` condicional (`Ikïtatixa jaytjawayamawa` "si te duermes, te dejaré", L2 p.200); "después que" con sujetos distintos: `-ipana` (`Tatama jutipana thuqhuñäni`, L2 p.200); "porque": `uka-t` (conexión íntima, causa) entre oraciones. | `mariya-x lapis ala-sa-w jupa-r chur-i` — María-TOP lápiz comprar-SUB-AFF 3-COMPL.RU dar-3>3.SIMP — "María, comprando un lápiz, se lo dio a él/ella"; `juta-spa-x sara-p-x-sna-w` — venir-3>3.DES-TOP ir-PL-COMPL-4>3.DES-AFF — "si viniera, podríamos ir" | L1 p.298, 313, 316–317; L2 p.198–200 |

## 7. Nominalización y verbalización

### 7.1 Parte verbal

| Sufijo | Cambia (verbo→nombre / nombre→verbo) | Función | Ejemplo | Fuente |
|---|---|---|---|---|
| `-ña` | verbo→nombre | Forma citacional / infinitiva de la raíz verbal. Nominaliza los verbos de las frases verbales; es la base del propósito (`-ña-taki`) y del obligatorio. | `liyi-ñ yati-qa-ñ mun-t-wa` — leer-INF saber-DOWN-INF querer-1>3.SIMP-AFF — "quiero aprender a leer" | L1 p.80, p.72, p.89 |
| `-ta` (resultante) | verbo→nombre | «Lo V-do», resultado de la acción. Distinto del derivativo `-ta-` (UP/INCEP). | `chura-ta-wa` — dar-NMLZ.RES-AFF — "lo dado"; `q'ipi-ta-wa` — cargar.espalda-NMLZ.RES-AFF — "lo cargado (es)" | L1 p.68, p.77, p.89 |
| `-wi` | verbo→nombre | NMLZ.LOC: lugar u ocasión de la acción (ver 7.2 y 7.3 C; L1 p.195). L2 amplía: también nombre de acción y abstracto (`tantachawi` "reunión", `lurawi` "acción"; L2 p.174–175). | `ch'uñu-:-wi-r` — chuño-VBLZ.LONG-NMLZ.LOC-ALL — "(al) lugar de hacer chuño" | L1 p.89, p.76; ej. p.132 |
| `-iri` | verbo→nombre | Agentivo «el que V». Como subordinador de propósito no marca persona. | `sar-iri` — ir-AG — "la persona que va"; propósito: `al-iri` — comprar-NMLZ.PURP — "para comprar" (ver `-iri2` en 7.2) | L1 p.90; propósito p.161 |
| `-ña-xa` / `-ña-ma` / `-ña-pa` / `-ña-sa` (obligatorio) | verbo→nombre | Obligación: construcción nominal posesiva sobre el infinitivo; 1, 2, 3 y 4 respectivamente, solo como sujetos; el pronombre toma `-n`. | `naya-n qillqa-ña-xa-w` — 1-GEN escribir-INF-POSS.1-AFF — "tengo que escribir" (con D4: `qillqañajawa`; L2 `sarañajawa` "debo ir", p.173) | L1 p.162, p.167 |
| `-ña-taki` | verbo→nombre | Subordinador de propósito, de horizontes más amplios que `-iri`; es construcción nominal y admite las cuatro personas nominales. | `chura-ña-taki` — dar-INF-BEN — "para dar (a Susana)" | L1 p.161 |
| `-:-` (alargamiento vocálico) | nombre→verbo | Verbalizador defectivo: «ser N». Solo admite flexiones 1→3, 2→3, 3→3 y 4→3, derivativos de la Clase II y `-t'a-`. | `wawa-:-ña` — bebé-VBLZ.LONG-INF — "ser niño"; en oración: `Juwanti Mamani-:-t-wa` — Juan Mamani-VBLZ.LONG-1>3.SIMP-AFF — "soy Juan Mamani" | L1 p.89, p.162 |
| `-ka-` | nombre→verbo | Verbalizador defectivo: «estar en». Mismas restricciones que `-:-`. | `uta-n-ka-ña` — casa-LOC-VBLZ.KA-INF — "estar en (una) casa"; en oración: `aka-n-ka-s-k-t-wa` — aquí-LOC-VBLZ.KA-PROG-INCOMPL-1>3.SIMP-AFF — "estoy aquí" | L1 p.89, p.162 |
| `-pta-` | nombre→verbo | Verbalizador pleno: "llegar a ser" (ver 7.3 C). L2: "transformativo" (p.223). | `wali-pta-ña` — bien-VBLZ.PTA-INF — "sanarse" | L1 p.89, p.240–241 |
| Derivativos con doble función: `-cha-`, `-ja-`, `-thapi-`, `-ra-`, `-nuqa-`, `-kata-`, `-kipa-`, `-nta-`, `-nuku-`, `-tata-`, `-t'a-` y `-ya-` | nombre→verbo | Verbalizan raíces nominales y producen un verbo pleno que admite cualquier sufijo verbal posterior (a diferencia de `-:-` y `-ka-`). Actúan como troncos, no como temas. | `ut-ja-ña` — casa-VBLZ-INF — "existir, vivir en alguna parte"; `wawa-cha-ña` — bebé-CAUS.R-INF — "parir (animales)"; `suti-ya-ña` — nombre-CAUS-INF — "bautizar" | L1 p.89, p.94–95, p.97, p.108 |
| Alternancia temática (cadena) | verbo↔nombre | Los alternadores temáticos pueden repetirse (máximo desconocido) y alternar tema verbal y nominal; la flexión cierra la forma. | `sar-iri-:` — ir-AG-VBLZ.LONG — "ser la persona que va" (tema verbal) | L1 p.89–91 |

Nota: la mayoría de las raíces verbales y muchos temas verbales pueden nominalizarse; las raíces nominales y verbales «dobles» (`manq'a` «comida» / `manq'a-` «comer») toman sufijos de ambas clases sin cambio (L1 p.79).

### 7.2 Parte nominal

| Sufijo | Cambia (verbo→nombre / nombre→verbo) | Función | Ejemplo | Fuente |
|---|---|---|---|---|
| -iri1 | verbo→nombre | AG: actor / acción habitual | `al-iri` — comprar-AG — "comprador" | L1 p.190–191 |
| -iri2 | verbo→nombre (defectivo) | NMLZ.PURP: propósito; no toma sufijos nominales | `sirwis al-iri-w sara-:` — cerveza.O comprar-NMLZ.PURP-AFF ir-1>3.FUT — "voy a ir a comprar cerveza" | L1 p.192 |
| -ña | verbo→nombre | INF: infinitivo, nombre de acción; obligación; con -taki "para" | `ch'uqi-w ala-ni-ña` — papa-AFF comprar-APPR-INF — "hay que comprar papa" | L1 p.193–194 |
| -ta | verbo→nombre | NMLZ.RES: resultante (lo hecho, estado) | `ala-ta` — comprar-NMLZ.RES — "lo que se ha comprado" | L1 p.191, 195 |
| -wi | verbo→nombre | NMLZ.LOC: lugar u ocasión de la acción | `ala-wi` — comprar-NMLZ.LOC — "mercado" | L1 p.191, 195 |
| -ka- | nombre→verbo (defectivo) | VBLZ.KA: ubicación/posesión (`-n-ka-`) | `uta-n-ka-ña` — casa-LOC-VBLZ.KA-INF — "estar en casa" | L1 p.173, 236–238 |
| -:- (alargamiento) | nombre→verbo (defectivo) | VBLZ.LONG: "ser X", existencia | `warmi-:-ña` — mujer-VBLZ.LONG-INF — "ser mujer" | L1 p.173, 238–240 |
| -pta- | nombre→verbo (completo) | VBLZ.PTA: "llegar a ser" | `wali-pta-ña` — bien-VBLZ.PTA-INF — "sanarse" | L1 p.240–241 |
| -ya- y otros derivacionales verbales | nombre→verbo (completo) | CAUS y otros (-cha-, -ja-, -ra-, -thapi-, -nuqa-, -kata-, -nta-, -tata-, -nuku-, -t'a-) | `suti-ya-ña` — nombre-CAUS-INF — "bautizar" | L1 p.189–191, 266 |

### 7.3 Aclaraciones (respuestas de la extracción)

**A. ¿Cuándo -ru marca el complemento (COMPL.RU) y cuándo es relacional (ALL)?**
El libro no usa "acusativo"; llama a -ru sufijo complemento/relacional direccional "a, hacia" (L1 p.210). Reglas que da:
- Nominal **humano** con -ru: es complemento de la flexión verbal si corresponde a la persona objeto del sufijo flexional (`khiti-ru-s awtu-t apa-ni` "¿a quién llevará en el carro?", p.211); si no, es relacional (p.211). Solo los verbos que "gobiernan" -ru lo toman como complemento (p.210).
- Nominal **no humano** con -ru: siempre relacional (dirección, lugar o propósito), nunca complemento de la flexión (p.212): `uta-ru-w ch'uq apa-ñani` "llevaremos papa a la casa" (p.212); responde a kawki-ru-sa, kawkha-ru-sa, kuna-ru-sa (p.212–213).
- El objeto directo propiamente dicho es el **complemento cero** (pérdida de la vocal final), no -ru (p.233); el mismo nominal puede ser cero o -ru: `mark sar-ta` / `marka-ru-w sar-ta` (p.235).
- Con -ya- causativo en el verbo, -ru puede marcar al agente (p.212); con complemento de 1ª/2ª persona se usa -mpi en su lugar (p.212, 221).
- Un complemento -taki tiene precedencia sobre -ru y -ta, que pasan a relacionales (p.218).
Glosa adoptada (D9): ALL para el uso relacional; COMPL.RU para el nominal humano con -ru que corresponde a la persona complemento de la flexión. No se usa ACC: ese complemento suele ser el destinatario ("la persona hacia la cual se dirige la acción", p.211), no un objeto directo. Además, solo ciertos verbos admiten complemento -ru: `apa.ña` "llevar" no lo toma sin un direccional `-ta` (p.212), así que el generador necesita información léxica del verbo para asignar COMPL.RU (ver sección 13).

**B. Funciones de jani / jan y distribución de -ti (negación y pregunta).**
- `jani` "no" es una raíz nominal limítrofe, casi partícula (p.189); `jan` es su forma con pérdida de vocal final cuando modifica en una frase (`jan uka-x`, p.249–250). Derivados fosilizados: `jan-ja ~ jan-jama` "no creo", `jani-ra` "todavía no", `jani-kucha` "mejor no" (p.189).
- Negación básica: `jani` + -wa; -ti donde iría -wa; -xa como siempre (p.299). -ti es obligatorio, pero solo no basta: siempre va con jani (p.283). El verbo atrae al -ti (p.299–300) y suele llevar -ka- incompletivo, aunque no es obligatorio (p.283, 301).
- -ti pregunta sí/no: va sobre la construcción que se espera en la respuesta (p.282). `jani-t` con -ti directo en jani = pregunta negativa que espera "sí" (p.302). -sti reemplaza a -xa cuando -ti ocurre en jani (p.310).
- Respuestas negativas a preguntas con -sa1: `jani-w` + interrogativo con -sa2 (`jani-w kun-sa` "nada", p.285, 302).
- El libro trata -ti de pregunta y -ti de negación como dos sufijos homófonos (p.282).

**C. Función de -wi, de -pta- y sentido de -ta nominalizador (Cap. IX).**
- **-wi**: nominalizador de "lugar u ocasión de la acción" (p.195); en el cap. IX, "lugar/ceremonia" (p.265, 269). Suele alargar un poco la vocal precedente. `ala-wi` "mercado", `suti-ya-wi` "bautizo", `sar-naqa-wi` "manera de vivir" (p.191, 195).
- **-pta-**: verbalizador de nombres, verbo completo, "llegar a ser" (p.240); requiere vocal precedente: `wali-pta-ña` "sanarse", `ch'iyara-pta-ña` "volverse negro", `qam-iri-pta-ña` "enriquecerse" (p.240–241). No existe otro uso de -pta- (p.266).
- **-ta nominalizador**: "resultante" (p.195, 265): convierte el verbo en lo resultante o el estado (`ala-ta` "lo que se ha comprado", `suti-ya-ta` "la persona bautizada", `usu-ta` "enfermo/a", p.191, 195, 239). Se distingue de -ta ABL porque conserva su vocal ante sufijos oracionales, mientras que -ta "de, desde" la pierde (p.214); con -:- se reverbaliza (`usu-ta-:-` "estar enfermo", p.239).

## 8. Alfabeto y escritura

### 8.1 Alfabeto oficial

Oficializado por el DS 20227 (1984), reproducido como recuadro ilustrado en L2 p.35 (30 casillas: 29 letras más el signo de la diéresis). El cuadro fonológico con los mismos símbolos está en L2 p.40.

- **Vocales (3):** a, i, u (sistema trivocálico; L2 p.39). Con alargamiento: ä, ï, ü (L2 p.46–47).
- **Consonantes (26; L2 p.40):**
  - Oclusivas simples: p, t, ch, k, q
  - Oclusivas aspiradas: ph, th, chh, kh, qh
  - Oclusivas glotalizadas: p’, t’, ch’, k’, q’
  - Fricativas: s, j, x
  - Nasales: m, n, ñ
  - Líquidas laterales: l, ll
  - Líquida vibrante: r
  - Semiconsonantes: w, y
- **Signo de la diéresis (¨):** casilla 30 del recuadro de L2 p.35.
- **Orden del recuadro (L2 p.35):** A, CH, CHH, CH’, I, J, K, KH, K’, L, LL, M, N, Ñ, P, PH, P’, Q, QH, Q’, R, S, T, TH, T’, U, W, X, Y, ¨.
- **Letras del castellano ausentes en aymara (L2 p.44):** B, C, D, F, G, H, V, Z. La h solo aparece dentro de los dígrafos aspirados (ph, th, chh, kh, qh).
- **Africadas:** /ch, chh, ch’/ se agrupan con las oclusivas por su comportamiento funcional (L2 p.40).

### 8.2 Vocal larga

| Uso del alargamiento | Cómo se escribe | Ejemplo | Fuente |
|---|---|---|---|
| Representación general | Diéresis sobre la vocal: a→ä, i→ï, u→ü | `chäka` — tallo.seco.de.quinua — "tallo seco de quinua" (< `chayaka`) | L2 p.46–47 |
| Compensatorio: cae y/w entre vocales idénticas | Diéresis. En la escritura se conservan **las dos formas** (maya/mä, paya/pä, khaya/khä), también ante un nombre (`pä/paya utanithwa`, p.57). Lo obligatorio ante un nombre es la *pronunciación* `mä`/`pä` (p.43). Ver D8 | `pä uta` — dos casa — "dos casas" | L2 p.43, p.57 |
| Valor fonémico (según L2: palabras sin pérdida de segmento que la diéresis distingue) | Diéresis en la vocal que corresponde | `qüña` "estanque de agua" frente a `quña` "suave"; `yäpa` "perfecto" frente a `yapa` "aumento"; `umäña` "ser agua" frente a `umaña` "tomar" (p.48–49). **`umäña`:** L2 la pone en este grupo (sin pérdida de segmento), pero su traducción "ser agua" corresponde al alargamiento con valor de "ser" de la sección siguiente (p.49–52). L2 no la segmenta; L1 solo registra `uma.ña` "tomar, beber" (p.117, 127) y no registra `umäña`. Segmentación y clasificación: **pendientes de verificación** (se retiró la segmentación `agua-VBLZ.LONG-INF†` de v2) | L2 p.48–49 |
| Lexicalizado (forma corta con valor propio) | Diéresis; la forma completa es alternativa de recuperación | `kürmi` — arco.iris — "arco iris" (< `kuyurmi`); `yä` — objeto — "objeto / cosa" (< `yaya`) | L2 p.47 |
| Verbo ser/estar (kankaña) reducido a alargamiento | Diéresis (L2 la nota `-¨`). Si queda vestigio del verbo (-n-k-, -ka-) no hay diéresis | `jach'a-¨-th(a)-wa`† — grande-VBLZ.LONG-1>3.SIMP-AFF — "soy grande" (`jach’äthwa`, < `jach’a kankthwa`); `uta-¨-ni-wa`† — casa-VBLZ.LONG-3>3.FUT-AFF — "será casa" (frente a `uta-ni-wa` — casa-POSR-AFF — "tiene casa"); `jaqi-¨-ña`† — persona-VBLZ.LONG-INF — "ser persona" | L2 p.49–52 |
| Sufijo `-ipana` (empieza y termina en vocal) | Diéresis en la primera vocal del sufijo | `Aski urukïpanaya` y otras fórmulas (`Aski jayp'ukïpanaya`, `Suma jakawikïpanaya`…), que L2 analiza como `aski uru-ki-ipana-ya` (p.53). L2 no las traduce. La hipótesis ‡ `uru-ki-:-pana-ya` (ver 5.2) está pendiente de verificación | L2 p.53 |
| Marca de composición (2.ª palabra empieza en vocal) | Diéresis en la vocal fusionada. L2 prefiere escribir las palabras **por separado**; ambas formas son válidas si la compuesta predomina en la oralidad | `jach'a uru` → `jach’üru` — grande día — "gran día"; `jichha uru` → `jichhüru` — ahora día — "hoy día" | L2 p.53–55 |
| Futuro | `-¨` (1), `-¨ta` (2), `-ni` (3), `-ñäni` (4) | `chura-¨` — dar-1>3.FUT — "yo daré" (`churä`); `chura-¨ta` — dar-2>3.FUT — "tú darás"; `chura-ni` — dar-3>3.FUT — "él/ella dará"; `chura-ñäni` — dar-4>3.FUT — "nosotros daremos"; `sara-¨` — ir-1>3.FUT — "yo iré" (`sarä`) | L2 p.55 |
| Pasado de conocimiento directo (por pérdida de segmentos) | `-yätha`, `-yäta`, `-¨na`, `-yätana` | `muna-yätha` — querer-1>3.REM.C — "yo quería"; `muna-¨na` — querer-3>3.REM.C — "él/ella quería" (`munäna`) | L2 p.34, p.56 |
| Pasado de conocimiento indirecto | `-tätha`, `-täta`, `-täna` (o `-tayna`), `-tätana` | `muna-tätha` — querer-1>3.REM.L — "yo había querido"; `muna-täna` ~ `muna-tayna` — querer-3>3.REM.L — "él/ella había querido" | L2 p.34, p.56 |

### 8.3 Reglas de escritura y normalización

| Regla | Ejemplo correcto | Ejemplo incorrecto (si lo da) | Fuente |
|---|---|---|---|
| La escritura es **fonémica**, no fonética: "la gramática normaliza la escritura, no la oralidad". Escribir como se habla se califica de "aberración lingüística" | `tata-xa uta-ru-wa sar(a)-i`† — padre-TOP casa-ALL-AFF ir-3>3.SIMP — "El padre/señor fue/va a la casa" (se escribe `Tataxa utaruwa sari`) | `[Tatax(a) utaruw(a) sari]` (transcripción oral) | L2 p.60, p.68–70 |
| Toda palabra termina en vocal. **Se recuperan por escrito** las vocales finales ensordecidas dentro de la frase. Se exceptúan las exclamaciones (¡chhuy!, ¡ay!, ¡alalay!) | `Aymara aru qillqañäni` (traducción FALTA); `machaqa mara` — nuevo año — "año nuevo" | `[Aymar(a) ar(u) qellqañäni]`; `[Akax(a) nän(a) utajawa]` | L2 p.60, p.67, p.70, p.75 |
| La vocal final completa evita ambigüedad semántica (no hay contexto que la resuelva en el texto escrito) | `tata-xa jatha q'ipinitayna` — padre-TOP semilla cargar.REM.L — "El papá había cargado la semilla"; `tata-xa jathi q'ipinitayna` — padre-TOP pesado cargar.REM.L — "El papá había cargado algo pesado" (verbo sin segmentar) | `[Tatax jath q’epinitayna]` (sirve para ambos); `[ar]` = aru o ari | L2 p.76–77 |
| Las **elisiones intraléxicas** (dentro de la palabra) se mantienen en la escritura. Solo se pueden recuperar vocales si no cambia el significado | `lur(a)-th(a)-wa` — hacer-1>3.SIMP-AFF — "hago" → se escribe `lurthwa`; `jani-wa jiskh(i)-t'(a)-k(a)-th(a)-ti` — NEG-AFF preguntar-MOM-INCOMPL-1>3.SIMP-NEG — "no pregunté" → `janiwa jiskht’kthti`. Recuperación posible: `tantathapiña` (`tantachthapiña`) — juntar — "juntar" | FALTA | L2 p.61, p.65–66 |
| **Una sola forma escrita** por palabra; la variación (dialectal, sociolectal, idiolectal) es solo oral. La forma escrita es la históricamente más conservada de cada territorio. Para la enseñanza no se presenta una palabra con más de una forma | `wampu` ~ `yampu` "balsa" (variación oral w~y; L2 no dice cuál se escribe) | **Excepciones documentadas en la propia L2:** `maya/mä`, `paya/pä`, `khaya/khä` se mantienen en las dos formas (p.57); los compuestos pueden escribirse separados o unidos si la forma compuesta predomina en la oralidad (p.54–55); las dos formas normativas de la vocal larga, recuperación de la forma completa o diéresis (p.47) | L2 p.43, 47, 54–55, 57, 71, 74 |
| Maya/paya/khaya y mä/pä/khä: se mantienen **ambas formas** en la escritura | `nayaxa pä/paya uta-ni-th(a)-wa`† — yo-TOP dos casa-POSR-1>3.SIMP-AFF — "Yo tengo dos casas" | FALTA | L2 p.57 |
| Palabras compuestas: se evitan; se escribe cada palabra por separado | `jach'a uru` — grande día — "gran día" | `jach’üru` también es válida si predomina en la oralidad | L2 p.53–55 |
| Préstamos terminados en consonante reciben vocal final (se "refonemizan") | `lapisa` — lápiz — "lápiz"; `lunisa` — lunes — "lunes"; `riluju` — reloj — "reloj"; `silulara` — celular — "celular"; `philiksu` — Félix — "Félix" | FALTA | L2 p.77 |
| Aspiradas = dígrafo con h (ph, th, chh, kh, qh); glotalizadas = apóstrofo (p’, t’, ch’, k’, q’). Una raíz admite más de una aspirada o glotalizada | `phisi` — gato — "gato"; `p’isi` — ajustado — "ajustado"; `t’ant’a` — pan — "pan"; `ch’umphi` — castaño — "castaño" | FALTA | L2 p.41–42 |
| j (velar) y x (postvelar) son fonemas distintos: no se confunden | `ch’uju` — silencio — "silencio"; `ch’uxu` — tos — "tos" | FALTA | L2 p.42 |
| Restricciones de posición de **x** y **r** | L2: **x** "no aparece en posición inicial absoluta de las palabras raíces" (p.42): `suxta` "seis". **r** "no aparece en posición inicial de palabra", pero "en palabras refonemizadas puede aparecer al inicio" (p.44): `riyata` "reata" (también es la palabra que ilustra la R en el recuadro del alfabeto, p.35); préstamos `ratuki`, `riyata`, `rumarisu`, `rimiña` (p.44). L1: /x/ y /r/ "no se han encontrado en posición inicial en palabras nativas"; en préstamos /r/ puede ser inicial (`rusintita`, p.41) | Casos sin explicar en L2: `rixinta` "firma" y `raphaku` "polilla" aparecen en la misma lista de ejemplos de /r/ (p.44) y `rixinta` también entre los de /x/ (p.42), sin indicar si son préstamos. No formular la regla como absoluta: "no inicial en palabras nativas; posible en préstamos" | L1 p.41; L2 p.35, 42, 44 |
| Restricción: en una raíz, oclusivas de igual articulación comparten aspiración o glotalización | `phapha` — tierra.suelta — "tierra suelta"; `k’ak’a` — grieta — "grieta" | FALTA ("generalmente", no es regla absoluta) | L2 p.41–42 |
| Junto a postvelares (q, qh, q’, x) las vocales i/u se pronuncian [e]/[o] **pero se escriben i/u** | `iqiqu` — dios.abundancia — "Dios de la abundancia" (pron. [eqeqo]); `q’illu` — amarillo — "amarillo" (pron. [q’ellu]) | FALTA (L2 da la pronunciación como contraste, no como error) | L2 p.45–46 |
| El acento no se escribe: recae en la penúltima sílaba y se desplaza al añadir sufijos. La entonación suele descender desde la penúltima | `uma-mpi` — agua-COM — FALTA; `sara-ña` — ir-INF — FALTA | FALTA | L2 p.57–58 |
| Estructura silábica (referencia para validar): raíces mayormente bisílabas; sílabas V, CV, VC, CVC; sufijos casi siempre CV (raros -mpi, -nta, -iri) | `man-q’a` — comida — "comida" | FALTA | L2 p.58–59 |

Marco normativo citado: DS 20227 (alfabeto único) y RM 599 de 2011 (principios de escritura; "Documento de Normalización" de aplicación obligatoria en el Sistema Educativo Plurinacional) (L2 p.71, p.73–74).

### 8.4 Correspondencias L1 (Compendio) ↔ L2 (oficial)

**v3: esta tabla ya no es una tabla de conversión automática.** Registra cómo escribe y analiza cada fuente el mismo rasgo, con formas atestiguadas de ambos libros. Para la escritura normalizada vale la forma de L2 (D1). Una forma de L2 que no esté atestiguada se marca como **hipotética** y no debe usarse en el generador (sección 13).

| Rasgo | L1 (forma atestiguada) | L2 (forma atestiguada) | Tipo de relación | Escritura normalizada | Fuente |
|---|---|---|---|---|---|
| Vocal larga | `:` al segmentar: `naya-w sara-:` "yo iré" (p.152); `ma:` "uno" (p.295). En texto corrido, `ä` (`muytätaxa`, `mä qillqa`, p.57–58) | Diéresis: `Nayaxa sarä` "yo iré" (p.55); `mä`/`maya` (p.43, 57) | Misma realidad; distinta notación | Diéresis (D2) | L1 p.57–58, 73, 152, 295; L2 p.43, 46–47, 55–57 |
| Codificación de la diéresis | — | Precompuestos U+00E4, U+00EF, U+00FC; ningún diacrítico combinante en el PDF | — | Precompuestos | L2 (verificado en el PDF) |
| Posesivo 1.ª persona | `uta-ja` "mi casa" (p.205); `tata-xa-wa` "es mi padre" (p.172); variante `-:` (`nina-:-chi-m`, p.205) | `utaja` (p.149); `tatajaxa` (p.75); `sarañajawa` "debo ir" (p.173) | L1 documenta variación `-xa ~ -ja ~ -:`; L2 adopta `-ja` | `-ja` (D4) | L1 p.172, 205; L2 p.75, 148–149, 173 |
| x y j | `-xa` TOP, `-xa-` COMPL, `-ja-` DIV, POSS.1 `-xa ~ -ja` | j velar, x postvelar; `-xa` topicalizador y `-x(a)` completivo (`yatxthwa`, p.64) | Mismas letras y fonemas | Igual | L1 p.205; L2 p.33, 40, 42, 64 |
| Aspiradas (h) | `khusu`, `phisi` | `khusu` "espeso", `phisi` "gato" (p.41) | Igual | Igual | L2 p.40–41 |
| Glotalizadas (apóstrofo) | `'` (U+0027) | `’` (U+2019) en la publicación; 8 `'` sueltos | Misma letra; distinto carácter | `’` en la publicación de L2; carácter interno según D3 | L2 (verificado en el PDF) |
| Separador de morfemas | `.` (`chur.t.wa`, p.68); en esta guía, `-` | `.` en tablas y paréntesis para la vocal elidida (`lur(a).th(a).wa`, p.61) | Convención de análisis | No se escribe | L1 p.68; L2 p.13, 60–61 |
| 1.ª persona, tiempo simple | `/ta/`, pierde su vocal: `chur-t-wa` "yo doy/di" (p.68); 2→3 también `-ta` pero conserva la vocal: `q'ip-ta-wa` (p.77) | `-tha` frente a `-ta` (2.ª): `churtha` "le di" (p.155); `sarthwa` "voy/fui" (p.176); `lurthwa` "hago" (p.61) | **Correspondencia funcional, forma distinta** (D5). No se convierte una cadena en la otra | Formas de L2, generadas desde su paradigma | L1 p.68, 77, 144, 159; L2 p.61, 155, 176 |
| Elisión entre palabras | Se escribe: `t'ant' chur-i` (p.87); `ch'iyar uta` (p.68) | Vocal completa: `Tatamaru t'ant'a churi` "le dio pan a tu padre" (p.155); `Ch'iyara phisi` (p.67) | **Análisis distintos** (D6, 5.3) | Vocal completa | L1 p.68, 87, 233; L2 p.66–70, 155 |
| Interrogativos | `qawqha` "cuánto" (p.84, 185); `kawkha` "¿qué lugar?" = `kawki` + `-ja` fosilizado (p.187) | `qawqha ~ qayqa` "cuánto" (p.43); `kawki` "dónde" (p.236). `kawkha`: no atestiguado | `qawqha` igual; `kawkha` sin forma en L2 | `qawqha`; `kawkha`: pendiente | L1 p.84, 185, 187; L2 p.43, 236 |
| "Ser N" | Verbalizador `-:-`: `Juwanti Mamani-:-t-wa` "soy Juan Mamani" (p.162) | Diéresis, explicada como el verbo `kankaña` reducido: `jach'äthwa` "soy grande" (p.51); tras `-ni` POSR, sin diéresis: `utanithwa` "tengo casa(s)" (p.57) | **Análisis distintos** (verbalizador frente a verbo reducido) | Solo formas atestiguadas en L2 | L1 p.89, 162, 239; L2 p.47, 49–52, 57, 224 |
| 4.ª persona, tiempo simple | `-tan`: `tuku-ya-p-x-tan-w` (p.134) | `-tana`: `sartana` (p.184); ante `-wa`, `manq'tanwa` (p.178) | Misma casilla del paradigma; forma de cita distinta (vocal final) | Formas de L2 | L1 p.144; L2 p.178, 184 |
| 3→2, tiempo simple | `-tam` (p.144) | `-tama`: `churtama` "te da pan" (p.180) | Misma casilla; forma de cita distinta | Formas de L2 | L1 p.144; L2 p.180 |
| 4.ª persona, futuro | `-ñani`: `sara-ñani` (p.209) | `-ñäni`: `sarañäni` (p.55, 190) | Misma casilla; L2 escribe vocal larga | Formas de L2 | L1 p.145, 209; L2 p.55, 190 |
| Remoto cercano, remoto lejano y desiderativo, 1.ª persona | `-ya:ta`, `-ta:ta`, `-irista` (cuadros, p.164–166) | `sarayätha` (p.185), `saratätha` (p.186), `sariristha` (p.192) | Misma casilla; formas distintas (aspiración y vocal larga) | Formas de L2 | L1 p.164–166; L2 p.185–186, 192 |
| Certeza | `-pi`, casi siempre con `-:` (`ukhama.raki.pi:`, p.289) | `-pï`: `ukhamapï` "así es pues" (p.233) | Misma marca; L2 escribe la vocal larga dentro del sufijo | Formas de L2 | L1 p.286, 289; L2 p.233 |
| Plural verbal y progresivo | `-p-` + `-xa-`/`-ka-`; `-si-` + `-ka-` (`sara-s-ka-ña`, p.111) | `-pxa`, `-ska` (`sarapxi`, p.181; `saraskaña`, p.202) | **Segmentaciones distintas** (D11); misma forma escrita | Igual | L1 p.111–112; L2 p.181, 202 |
| Préstamos | Sin vocal añadida: `lapis` (p.316) | Con vocal final: `lapisa` (p.77) | Diferencia de norma | Regla de L2 | L1 p.316; L2 p.77 |

**Formas hipotéticas (no atestiguadas en L2; no usar en el generador):** `churäna` (de L1 `chura-:na`, p.147); `churthwa` (de L1 `chur-t-wa`); `Juwanti Mamanïthwa` (de L1 `Juwanti Mamani-:-t-wa`); `kawkha` escrito según L2. Son extrapolaciones del patrón de L2, no formas documentadas.

## 9. Ejemplos

Los ejemplos están tal como los escribe y segmenta L1 (con `-ta` de 1.ª persona, `-xa` de POSS.1, `:` y elisiones). **Son ejemplos de análisis, no de escritura normalizada:** no se convierten automáticamente a la ortografía de L2 (D1, D5). Para ejemplos documentados de los dos libros, uno al lado del otro, ver la tabla de validación (sección 10).

### 9.1 Verbo (L1)

- `chur-t-wa` — dar-1>3.SIMP-AFF — "yo doy/di" — L1 p.68
- `q'ip-ta-wa` — cargar.espalda-2>3.SIMP-AFF — "tú cargas" — L1 p.77
- `Jupa-w jupa-r t'ant' chur-i` — 3-AFF 3-COMPL.RU pan.O dar-3>3.SIMP — "él/ella le da/dió pan a él/ella" — L1 p.87
- `P'iqi-w us-utu` — cabeza-AFF doler-3>1.SIMP — "la cabeza me duele" — L1 p.81
- `Ch'uq achu-y-ta` — papa.O producirse-CAUS-1>3.SIMP — "yo produzco papas / hago que las papas se produzcan" — L1 p.80
- `Marka-ru-w waw irpa-:` — pueblo-ALL-AFF niño.O llevar-1>3.FUT — "yo llevaré el niño al pueblo" — L1 p.81
- `Khiti-s irpa-:tam` — quién-Q.INF llevar-3>2.FUT — "¿quién lo llevará a Ud.?" — L1 p.73
- `Ruwirtu-w irp-itani` — Roberto-AFF llevar-3>1.FUT — "Roberto me llevará" — L1 p.73
- `Jupa-naka-w naya-r parla-p-x-itu` — 3-PL-AFF 1-COMPL.RU hablar-PL-COMPL-3>1.SIMP — "ellos me hablaron" — L1 p.112
- `Jupa-w (jupa-r) chura-:na` — 3-AFF (3-COMPL.RU) dar-3>3.REM.C — "ella se lo ha dado (yo lo vi)" — L1 p.147
- `Jupa-w (jupa-r) chura-tayna` — 3-AFF (3-COMPL.RU) dar-3>3.REM.L — "ella se lo había dado a él (pero yo no vi el acto de dar)" — L1 p.148
- `Chur-pacha-wa` — dar-3>3.INFR-AFF — "el/ella ha debido dar" — L1 p.149
- `Aymar yati-qa-sama:na` — aymara.O saber-DOWN-2>3.REPR — "Ud. debería haber aprendido aymara" — L1 p.155
- `Jani-w khuchi-mp ana-k-irist-ti` — NEG-AFF chancho-COM arrear-INCOMPL-1>3.DES-NEG — "prefiero no llevar los chanchos (con las ovejas)" — L1 p.154
- `Aka-n-ka-s-k-t-wa` — aquí-LOC-VBLZ.KA-PROG-INCOMPL-1>3.SIMP-AFF — "estoy aquí" — L1 p.162
- `Naya-n qillqa-ña-xa-w` — 1-GEN escribir-INF-POSS.1-AFF — "tengo que escribir" — L1 p.162
- `Jani-w sar-k-i-ti` — NEG-AFF ir-INCOMPL-3>3.SIMP-NEG — "él no ha ido / no va" — L1 p.111
- `Naya-w jupa-r jupa-mp t'ant' chura-y-ta` — 1-AFF 3-COMPL.RU 3-COM pan.O dar-CAUS-1>3.SIMP — "yo hago que él dé pan a ella" — L1 p.108
- `Naya-w (jupa-r) jupa-tak t'ant' chura-rap-ta` — 1-AFF (3-COMPL.RU) 3-BEN pan.O dar-BEN-1>3.SIMP — "yo le di (a él) pan para ella" — L1 p.110
- `Naya-x juma-n wawa-m sar-ta-ya-raq-sma` — 1-TOP 2-GEN bebé-POSS.2 ir-UP-CAUS-VICT-1>2.SIMP — "yo desperté a su bebé (Ud. no quería que lo hiciera)" — L1 p.110
- `Jichha-x wawa-nak ap-ta-ni-m` — ahora-TOP niño-PL.O llevar-INCEP-APPR-2>3.IMP — "ahora traiga a los niños" — L1 p.109
- `Ukha-n aka phutukraphiy-t'a-ni-way-ta` — allí-LOC esto fotografía-MOM-APPR-DIST-1>3.SIMP — "saqué esta fotografía allí" — L1 p.116
- `Sara-way-k-xa-:` — ir-DIST-INCOMPL-COMPL-1>3.FUT — "seguiré yendo adelante (pero puedo no regresar nunca)" — L1 p.112
- `Phina-t ch'uq pis-t'a-sa-w, Uliwya-r chura-ni-:` — montón-ABL papa.O pesar-MOM-SUB-AFF Olivia-COMPL.RU dar-APPR-1>3.FUT — "tan pronto como yo pese las papas de la pila, se las iré a dar a Olivia" — L1 p.161
- `Pall-ja-si-p-ka-rak-t-wa` — escoger-DIV-PROG-PL-INCOMPL-ADD-1>3.SIMP-AFF — "estamos aún escogiendo" — L1 p.133

### 9.2 Nombre y sintaxis (L1)

- `misa-x jach'a-wa` — mesa-TOP grande-AFF — "la mesa es grande" (L1 p.172)
- `jupa-x naya-n tata-xa-wa` — 3-TOP 1-GEN padre-POSS.1-AFF — "él es mi padre" (L1 p.172)
- `naya-x sara-:-wa` — 1-TOP ir-1>3.FUT-AFF — "yo voy a ir" (L1 p.280)
- `ch'iyar ch'uqi-wa` — negro papa-AFF — "es (una) papa negra" (L1 p.245)
- `uka-x wila punku-n tinta-wa` — eso-TOP rojo puerta-POSR tienda-AFF — "esa es una tienda de puerta roja" (L1 p.204)
- `naya-x pusi uta-ni-:-t-wa` — 1-TOP cuatro casa-POSR-VBLZ.LONG-1>3.SIMP-AFF — "tengo cuatro casas" (L1 p.204)
- `liwru-x kawkha-n-k-i-sa` — libro-TOP dónde-LOC-VBLZ.KA-3>3.SIMP-Q.INF — "¿dónde está el libro?" (L1 p.237)
- `misa taypi-n-k-i-w` — mesa medio-LOC-VBLZ.KA-3>3.SIMP-AFF — "en medio de la mesa" (L1 p.237)
- `jupa-n-k-i-ti` — 3-GEN-VBLZ.KA-3>3.SIMP-Q.YN — "¿es de él?" (L1 p.236)
- `naya-x Juwana Waskisa-:-t-wa` — 1-TOP Juana Vásquez-VBLZ.LONG-1>3.SIMP-AFF — "yo soy Juana Vásquez" (L1 p.239)
- `jani-w Mariya-:-k-i-ti` — NEG-AFF María-VBLZ.LONG-INCOMPL-3>3.SIMP-NEG — "no fue María" (L1 p.282)
- `jani-w naya-x sum aymar parla-ñ yat-k-t-ti` — NEG-AFF 1-TOP bien aymara.O hablar-INF saber-INCOMPL-1>3.SIMP-NEG — "no sé hablar bien el aymara" (L1 p.301)
- `Mariya-t wawa-r t'ant' chur-i` — María-Q.YN niño-COMPL.RU pan.O dar-3>3.SIMP — "¿dio María pan al niño?" (L1 p.282)
- `kuna-s suti-ma-xa` — qué-Q.INF nombre-POSS.2-TOP — "¿cuál es su nombre?" (L1 p.282)
- `kawki-ru-s sar-ta` — dónde-ALL-Q.INF ir-2>3.SIMP — "¿dónde fuiste?" (L1 p.213)
- `marka-ru-w sar-ta` — pueblo-ALL-AFF ir-1>3.SIMP — "fui al pueblo" (L1 p.213)
- `mark sar-ta` — pueblo.O ir-1>3.SIMP — "fui al pueblo" (L1 p.235)
- `khiti-ru-s awtu-t apa-ni` — quién-COMPL.RU-Q.INF auto-ABL llevar-3>3.FUT — "¿a quién llevará (él) en el carro?" (L1 p.211)
- `ch'uq chur-ita` — papa.O dar-2>1.IMP — "dame papas" (L1 p.233)
- `ch'uq ala-ña-taki-w sar-ta` — papa.O comprar-INF-BEN-AFF ir-1>3.SIMP — "fui para comprar papas" (L1 p.220)
- `lawa-mpi-w jiru-p-x-i` — palo-COM-AFF remover-PL-COMPL-3>3.SIMP — "lo removieron con un palo" (L1 p.224)
- `manu-layku-w jut-ta` — deuda-CAUSE-AFF venir-1>3.SIMP — "vine a causa de una deuda" (L1 p.199)
- `sara-ña-xa-w` — ir-INF-POSS.1-AFF — "tengo que ir" (L1 p.205)
- `jupa-x wali-ki-w sa-sa-w s-i` — 3-TOP bien-LIM-AFF decir-SUB-AFF decir-3>3.SIMP — "dijo que estaba bien" (L1 p.314)

## 10. Validación

### 10.1 Tabla de validación con ejemplos documentados (v3)

Todas las formas de esta tabla están **atestiguadas** en la fuente y la página indicadas (comprobado contra el texto de los PDF). Columna "Segmentación": si la segmentación es del libro, se indica "(fuente)"; si la hizo esta guía, se marca con `†`. La traducción es la del libro. **Ninguna oración de esta tabla fue inventada.** Las formas hipotéticas están aparte, en 10.2.

**A. Escritura normalizada (L2)**

| # | Forma tal como la escribe L2 | Segmentación y glosa | Traducción de L2 | Fuente | Regla que valida |
|---|---|---|---|---|---|
| 1 | `Nayaxa wawaru t'ant'a churtha.` | `naya-xa wawa-ru t'ant'a chur-tha` — 1-TOP niño-COMPL.RU pan dar-1(>3).SIMP † | "Yo le di pan al niño" | L2 p.155 | D5 (`-tha`); D6 (vocal completa en el objeto `t'ant'a`); D9 (`-ru` con humano destinatario; L2 lo llama objeto indirecto) |
| 2 | `Tatamaru t'ant'a churi.` | `tata-ma-ru t'ant'a chur-i` — padre-POSS.2-COMPL.RU pan dar-3>3.SIMP † | "Le dio pan a tu padre" | L2 p.155 | D6; D9 |
| 3 | `Markaru jutani.` | `marka-ru juta-ni` — pueblo-ALL venir-3>3.FUT † (futuro de 3.ª `-ni`, L2 p.189) | "Vendrá al pueblo" | L2 p.156 | D9 (`-ru` relacional, no humano) |
| 4 | `Nayaxa sarthwa.` | `naya-xa sar-th-wa` — 1-TOP ir-1.SIMP-AFF † | "Yo voy/fui" | L2 p.176 | D5; elisión morfológica (5.3 a) |
| 5 | `Jumaxa manq'tawa.` | `juma-xa manq'-ta-wa` — 2-TOP comer-2.SIMP-AFF † | "Tú comes/comiste" | L2 p.177 | D5 (`-ta` de 2.ª conserva su vocal ante `-wa`) |
| 6 | `Jiwasaxa manq'tanwa.` | `jiwasa-xa manq'-tan-wa` — 4-TOP comer-4.SIMP-AFF † | "Nosotros comemos/comimos" | L2 p.178 | D12 (4.ª persona); 8.4 (`-tana`) |
| 7 | `uta.ja` | `uta-ja` — casa-POSS.1 (fuente) | "mi casa" | L2 p.149 | D4 |
| 8 | `Sarañajawa` | `sara-ña-ja-wa` — ir-INF-POSS.1-AFF † | "Debo ir" | L2 p.173 | D4 (obligativo con `-ja`) |
| 9 | `Nayaxa pä/paya utanithwa.` | `naya-xa pä/paya uta-ni-th-wa` — 1-TOP dos casa-POSR-1.SIMP-AFF † | "Yo tengo dos casas" | L2 p.57 | D8 (dos formas válidas por escrito); sin diéresis tras `-ni` (8.4) |
| 10 | `Anuxa t'ant'a manq'i` | `anu-xa t'ant'a manq'-i` — perro-TOP pan comer-3>3.SIMP † | "El perro come pan" | L2 p.243 | D10 (SOV); D6 |
| 11 | `Wasüruxa markata wawapataki t'ant'a alani` | `wasüru-xa marka-ta wawa-pa-taki t'ant'a alani` — ayer-TOP pueblo-ABL hijo-POSS.3-BEN pan comprar.? † | "Ayer compró pan del pueblo para su hijo" | L2 p.255 | D10 (orden de complementos). **Glosa del verbo pendiente:** `alani` puede ser `ala-ni` (3>3.FUT, "comprará") o `ala-n-i` (APPR + 3>3.SIMP, "compró y trajo"); la traducción de L2, "compró", y `wasüru` "ayer" apuntan a la segunda, pero L2 no segmenta |
| 12 | `Tataxa utaruwa sari.` (forma oral: `Tatax(a) utaruw(a) sari`) | `tata-xa uta-ru-wa sar-i` — señor-TOP casa-ALL-AFF ir-3>3.SIMP † | "El padre/señor fue/va a la casa" | L2 p.68 | D6 (5.3 c: la forma oral no se escribe) |
| 13 | `Awichaxa wakwa awati.` | `awicha-xa wak-wa awat-i` — abuela-TOP vaca-AFF pastear-3>3.SIMP † | "La abuela pastea la vaca" | L2 p.68 | 5.3: elisión dentro de la palabra (`wak-wa`) que L2 sí escribe |
| 14 | `Janiwa jiskht'kthti` | `jiskh(i)-t'(a)-k(a)-th(a)-ti` (fuente, L2 p.65); glosa: preguntar-MOM-INCOMPL-1.SIMP-NEG (L2 llama "negativo" a `-ka`; ver D9) | "No pregunté" | L2 p.65 | 5.3 a; D9 |
| 15 | `Jilaqataxa janiwa jutkaniti.` | `jilaqata-xa jani-wa jut-ka-ni-ti` — autoridad-TOP NEG-AFF venir-INCOMPL-3>3.FUT-NEG † | "La autoridad no vendrá" | L2 p.231 | Negación `jani … -ti` |
| 16 | `¿Jilamaxa jutaniti?` | `jila-ma-xa juta-ni-ti` — hermano-POSS.2-TOP venir-3>3.FUT-Q.YN † | "¿Vendrá tu hermano?" | L2 p.235 | `-ti` interrogativo (Q.YN) |
| 17 | `Tatama jutipana thuqhuñäni.` | `tata-ma jut-ipana thuqhu-ñäni` — padre-POSS.2 venir-SUB bailar-4.FUT † | "Bailaremos después que venga tu papá" | L2 p.200 | `-ipana` = sujetos diferentes (coincide con L1 p.161) |
| 18 | `Ch'uqisa apillasa aka maraxa achuniwa.` | `ch'uqi-sa apilla-sa aka mara-xa achu-ni-wa` — papa-CAT oca-CAT este año-TOP producir-3>3.FUT-AFF † | "La papa y oca producirá este año" | L2 p.234 | D13 (coordinación con `-sa`) |
| 19 | `Tiwulampi wallatampiwa jikisipxi.` | `tiwula-mpi wallata-mpi-wa jikisi-px-i` — zorro-COM ganso-COM-AFF encontrarse-PL-3>3.SIMP † (plural según el análisis de L2, `-pxa`; D11) | "El zorro y el ganso se encuentran" | L2 p.160 | D13 (coordinación con `-mpi`) |
| 20 | `(Jupanakaxa) sarapxi` | `jupa-naka-xa sara-px-i` — 3-PL-TOP ir-PL-3>3.SIMP † (plural según el análisis de L2, `-pxa`; D11) | "Ellos/ellas van/fueron" | L2 p.184 | D11; D12 (plural opcional) |
| 21 | `Ch'iyara phisi` (forma oral con modificador desonorizado) | `ch'iyara phisi` — negro gato | "Gato negro" | L2 p.67 | D6, 5.3 b2 |
| 22 | `T'ant'a muntha` (oral `T'ant'(a) muntha`) | `t'ant'a mun-tha` — pan querer-1.SIMP † | "Quiero pan" | L2 p.67 | D6, 5.3 b1 |

**B. Análisis (L1) — no son formas de escritura normalizada**

| # | Forma tal como la escribe L1 | Segmentación y glosa | Traducción de L1 | Fuente | Regla que valida |
|---|---|---|---|---|---|
| 23 | `chur.t.wa` | `chur-t-wa` (fuente) — dar-1>3.SIMP-AFF | "yo doy/di" | L1 p.68 | D5 (1→3 `-ta` pierde su vocal) |
| 24 | `q'ip.ta.wa` | `q'ip-ta-wa` (fuente) — cargar.espalda-2>3.SIMP-AFF | "tú cargas" | L1 p.77 | D5 (2→3 `-ta` conserva su vocal) |
| 25 | `Jupa.w jupa.r t'ant' chur.i.` | `jupa-w jupa-r t'ant' chur-i` (fuente) — 3-AFF 3-COMPL.RU pan.O dar-3>3.SIMP | "él/ella le da/dio pan a él/ella" | L1 p.87 | D9 (complemento de la flexión = destinatario); 5.3 b1 (complemento cero) |
| 26 | `Mariya.t wawa.r t'ant' churi.` | `Mariya-t wawa-r t'ant' chur-i` † — María-Q.YN niño-COMPL.RU pan.O dar-3>3.SIMP | "¿Dio María pan al niño?" | L1 p.282 | D9; `-ti` en el elemento preguntado |
| 27 | `Khiti.ru.s awtu.t apa.ni.` | `khiti-ru-s awtu-t apa-ni` (fuente) — quién-COMPL.RU-Q.INF auto-ABL llevar-3>3.FUT | "¿A quién llevará (él) en el carro?" | L1 p.211 | D9 (L1 lo identifica expresamente como complemento de la flexión) |
| 28 | `Uta.ru.w ch'uq apa.ñani.` | `uta-ru-w ch'uq apa-ñani` (fuente) — casa-ALL-AFF papa.O llevar-4>3.FUT | "Llevaremos papa a la casa" | L1 p.212 | D9 (`-ru` relacional con no humano) |
| 29 | `ch'iyar uta` | `ch'iyar uta` (fuente) — negro casa | "casa negra" | L1 p.68 | 5.3 b2 (regla de L1; en L2 se escribe completa) |
| 30 | `Liyi.ñ yati.qa.ñ mun.t.wa.` | `liyi-ñ yati-qa-ñ mun-t-wa` (fuente) — leer-INF saber-DOWN-INF querer-1>3.SIMP-AFF | "Quiero aprender a leer" | L1 p.72 | 5.3 b3 (regla de L1) |
| 31 | `Kimsa.n.pacha.w sara.ñani.` | `kimsa-n-pacha-w sara-ñani` (fuente) — tres-POSR-INCL-AFF ir-4>3.FUT | "Los tres iremos" | L1 p.209 | D7 (`-pacha1` pide consonante en L1) |
| 32 | `Manu.layku.w jut.ta.` | `manu-layku-w jut-ta` (fuente) — deuda-CAUSE-AFF venir-1>3.SIMP | "Vine a causa de una deuda" | L1 p.199 | 5.2.1 (raíz de 2 vocales conserva su vocal ante `-layku`) |
| 33 | `Juwanti.mp Piruti.mp juma.mp sara.ñani.` | `Juwanti-mp Piruti-mp juma-mp sara-ñani` (fuente) — Juan-COM Pedro-COM 2-COM ir-4>3.FUT | "Vayamos tú, Juan, Pedro y yo" | L1 p.208 | D13 (coordinación con `-mpi`); D12 (4.ª persona incluye al destinatario) |
| 34 | `Wali.ki.w, yati.cha.p.x.ita:ta.piy.` | `wali-ki-w yati-cha-p-x-ita:ta-piy` (fuente) — bien-LIM-AFF saber-CAUS.R-PL-COMPL-2>1.FUT-CERT.POL | "Bueno, Uds. por favor enséñenme" | L1 p.289 | Paradigma FUT 2→1; D11 (segmentación de L1 del plural) |

**C. Pares contrastivos (misma regla en las dos fuentes)**

| Rasgo | L1 | L2 | Resultado |
|---|---|---|---|
| Objeto "pan" con el verbo "dar" | `t'ant' chur.i` (#25) | `t'ant'a churi` (#2) | Mismo esquema sintáctico; L1 elide y L2 escribe la vocal. Sin contradicción con D6: L2 para la escritura, L1 para el análisis |
| 1.ª persona simple | `chur.t.wa` (#23) | `churtha` (#1), `sarthwa` (#4) | Correspondencia funcional, forma distinta (D5). No hay ningún par de la misma palabra con `-wa` en las dos fuentes (`churthwa` no está atestiguado) |
| `-ru` con humano | `jupa.r` (#25), `khiti.ru.s` (#27) | `wawaru` (#1), `tatamaru` (#2) | En los cuatro el nominal humano es destinatario o complemento personal: COMPL.RU (D9), no objeto directo |
| `-ru` con no humano | `uta.ru.w` (#28) | `markaru` (#3) | ALL en las dos fuentes |
| Coordinación | `-mp … -mp` (#33) | `-mpi … -mpi` (#19), `-sa … -sa` (#18) | Coinciden (D13) |
| Plural verbal | `-p.x-` (#34) | `-pxi` (#19, #20) | Misma forma escrita; segmentación distinta (D11) |

Comprobación de coherencia: ninguna de las reglas corregidas (D4–D13, 5.3, 8.4) produce para estos ejemplos una forma distinta de la que escribe su fuente. Las reglas de L1 de la tabla B **no** se aplicaron a la tabla A.

### 10.2 Formas hipotéticas (no atestiguadas; no usar)

| Forma | De dónde sale | Por qué no se usa |
|---|---|---|
| `churthwa` | Paradigma de L2 aplicado a `chura-` + `-wa` | L2 solo atestigua `churtha` (sin `-wa`); es la combinación esperable, pero no documentada |
| `churäna` | L1 `chura-:na` (p.147) con la notación de L2 | Patrón de `munäna` (p.56) y `saräna` (p.185); no atestiguada |
| `Juwanti Mamanïthwa` | L1 `Juwanti Mamani-:-t-wa` (p.162) | La diéresis con nombres propios no está atestiguada en L2 |
| `uru-ki-:-pana-ya` | Hipótesis del revisor para `urukïpanaya` | Ninguna fuente la confirma (ver 5.2) |

### 10.3 Prueba con el corpus de entrenamiento (pendiente: requiere los datos)

La prueba con oraciones del corpus (por ejemplo, el dev de AmericasNLP) **no se ha hecho**: no hay oraciones del corpus en las fuentes de esta guía. Cuando se haga, se registrarán solo oraciones reales, con su traducción, y para cada una: segmentación según esta guía, si se pudo analizar y qué faltó. Además, se anotará qué convención usa el corpus en cada uno de estos puntos: `-tha`/`-ta` (D5), vocales finales (D6), apóstrofo y vocal larga (D2, D3), `mä`/`maya` (D8), orden de palabras (D10) y `-px-`/`-sk-` (D11). **Estos datos sirven para normalizar el corpus hacia la escritura de L2, no para cambiar la norma** (D6).

---
## 11. Verificación y registro de cambios

### 11.1 Cómo se verificó
- **v3:** todas las formas de la tabla 10.1 y de la tabla 8.4, y las páginas nuevas citadas en D3–D13, 5.2.1, 5.3, 12 y 13, se comprobaron contra el texto extraído de los dos PDF; el recuadro de dúctiles de L2 (p.62–64) se comprobó en imagen.
- **L1:** el texto del PDF completo se extrajo con `pdftotext`. Se comprobaron automáticamente las **218 formas aymaras** de las filas que citan a L1, quitando separadores y `:`. **182** aparecen en la página citada o en la vecina. Las 36 restantes se revisaron a mano: son formas de L2 en filas mixtas, filas que citan varias páginas o palabras partidas por la maquetación (`kha: jach'a wila punku n tinta .na`, p.252). El único desajuste real era que la fila SIMP citaba pp.143–144 para `chur-t-wa`, que está en la p.68; ya está corregido.
- **L1, revisión manual:** paradigmas SIMP y FUT (p.144–145, coinciden con 3.1 incluidas las marcas c/v); POSS (p.205); `-naka` (p.207, 251); orden de palabras (p.293–294); complemento cero (p.233); `-ipana` (p.161); preguntas (p.282, 286); cita (p.314); INFR (p.149, 157, 165); notación (p.67–69, 73); interrogativos (p.84, 185, 187).
- **L2:** se leyeron las pp.32–80 completas y las secciones de morfología y sintaxis citadas en 2.1, 3.4 y 4.1. Se verificaron visualmente el recuadro del alfabeto (p.35, 30 casillas) y el cuadro contrastivo (p.44). La codificación se contó en el texto extraído: `ä` 444, `ü` 160, `ï` 81, ningún diacrítico combinante; `’` ≈2.230 contra 8 `'`.

### 11.2 Correcciones de v2 (respecto a v1)
| Dónde (v1) | Decía | Ahora |
|---|---|---|
| 0.2 | "L2 no declara el orden SOV" | L2 declara SOV (p.241, 243) y el orden de complementos (p.255) |
| 0.2 | L2 solo trata los sufijos en una introducción (p.80) | L2 tiene morfología (pp.80–240) y sintaxis (pp.241–255); comparación en 2.1, 3.4 y 4.1 |
| D8, 8.2 | `mä`/`pä` obligatorios ante nombre | Obligatorios en la pronunciación; en la escritura valen las dos formas (L2 p.43, 57) |
| D10 | FALTA | SOV por defecto (L2) |
| Abreviaturas, 5.2, 8.2 | `OPT` para `-ipana`/`-pana`, atribuido a L2 | Eliminado. `-pana` = 3>3.IMP (L2 p.195); `-ipana` = SUB (L1 p.161, L2 p.200) |
| 5.2, 8.3 | `-k(a)` glosado NEG | INCOMPL (D9) |
| 5.1 | `-citu`, `-ciri`, `-citäta` | `-itu`, `-iri`, `-ita:ta` (la *c* era el subíndice de L1) |
| 8.4 | L1 escribe la vocal larga solo con `:` | `:` al segmentar; `¨` en el texto corrido (L1 p.57–58, 69, 73) |
| 8.4 | `kawkha` (L1) = "cuánto"? | `kawkha` = "¿qué lugar?"; "cuánto" = `qawqha` (L1 p.185, 187) |
| 8.4 | Elisión entre palabras en L1: FALTA | L1 escribe la elisión (p.57–58, 68, 233) |
| 8.4 | POSS.1 en L2: FALTA | `-ja` (L2 p.148–149) |
| 8.4 | `churthwa` no atestiguado en L2 | `churtha` (L2 p.155) |
| 3.1, 9.1 | `quién-Q` | `quién-Q.INF` |
| 7.1 | `-iri` de propósito glosado AG; `-wi` y `-pta-` con FALTA | NMLZ.PURP; función de `-wi` y `-pta-` completada |
| 3.3 | Reglas de `jani`/`-ti`: FALTA | Remite a 7.3 B |
| 1 (`-naka`) | Prohibido con números | Tendencia (L1 p.207 frente a p.251; L2 p.154) |

### 11.3 Añadidos de v2
- Decisiones D6 ampliada (modificadores), D11 (segmentación de `-pxa` y `-ska`) y precisiones en D2, D4, D5 y D9.
- Secciones 2.1, 3.4 y 4.1 (contraste con la morfología de L2) y el orden de complementos de L2 en la sección 1.
- Nuevas filas en 8.4: `-tan`→`-tana`, `-tam`→`-tama`, `-ñani`→`-ñäni`, 1.ª persona de los remotos y del potencial, `-pi`→`-pï`, plural y progresivo, préstamos; excepción de `utanithwa` (sin diéresis tras `-ni`).
- Ejemplos nuevos de L1: FUT 2>1, `-piya`, `-chim`, `-tisti`.
- Comparación con L1 en las filas de 5.2 que decían FALTA.

### 11.4 Registro de cambios de v3 (revisión correctiva)

Formato por problema: sección afectada · qué estaba mal · qué dice L1 · qué dice L2 · tipo (contradicción / diferencia de enfoque / explicación incompleta) · corrección · estado.

| # | Sección y regla | Qué estaba mal en v2 | L1 | L2 | Tipo | Corrección en v3 | Estado |
|---|---|---|---|---|---|---|---|
| 1 | D5; 3.1; 8.4; 9 | Trataba `-ta` (L1) como forma gráfica de `-tha` (L2) y proponía leer una como la otra; 9 convertía `chur-t-wa` → `churthwa` | 1→3 `/ta/`, pierde su vocal; idéntico en sonido a 2→3 `-ta`, que la conserva (p.77, 144, 159) | `-tha` (1.ª) frente a `-ta` (2.ª) (p.61, 176); `churtha` (p.155) | Diferencia de forma y de análisis; causa no explicada por ninguna fuente | D5 reescrita: correspondencia funcional, sin conversión automática; la escritura usa el paradigma de L2. 8.4 pasa a ser tabla de correspondencias. `churthwa` pasa a "hipotética" (10.2) | Diferencia confirmada; causa pendiente |
| 2 | D6; 1; 5.2; 5.3 (nueva); 8.4 | El corpus decidía la escritura ("si el corpus elide, se aplica la regla O"); no distinguía elisión morfológica, realización oral y ortografía | Pérdida de vocal final como marca gramatical del complemento cero (p.233), del modificador de 3 o más vocales (p.68) y del verbo nominalizado (p.72) | Elisión intraléxica: se escribe (p.61–66). Entre palabras: desonorización oral; vocal completa por escrito, "obligatoriamente" (p.66–70) | Diferencia de enfoque | D6 reescrita con tres niveles; nueva 5.3; las reglas de L1 quedan como análisis; el corpus no decide la norma | Confirmada |
| 3 | D7; 5.2; 5.2.1 (nueva); 2.1 | "Elisión opcional: el generador puede variar"; `-pacha` dado como dúctil sin contrastar | Cada sufijo con exigencia fija; condición documentada para `-layku`/`-kama` (raíz de 3 o más vocales, p.199, 228); todos los `-pacha` piden consonante (p.209, 228) | Dúctiles "a veces" fuertes y "otras" débiles, sin condiciones (p.60–64); `-pacha` en la columna de dúctiles (p.63–64) | Contradicción (`-pacha`, `-ma`, `-nama`, `-naqa-`); explicación incompleta (condiciones) | D7 reescrita: no hay alternancia libre; el generador no varía; tabla 5.2.1 con el respaldo de cada sufijo | Pendiente |
| 4 | D9; abreviaturas; 2; 2.1; 7.3 A; 9; ejemplos de 1, 4 y 6 | `-ru` humano glosado `ACC`; en algunos ejemplos un destinatario humano aparecía como `ALL` | `-ru` complemento (persona complemento de la flexión, "la persona hacia la cual se dirige la acción") frente a relacional (p.210–212) | `-ru` "complemento indirecto" y dirección; acusativo = `-ø` (p.154–157) | Diferencia de terminología | Etiqueta `COMPL.RU` para el complemento personal y `ALL` para el relacional; todos los `ACC` reemplazados; se advierte que el complemento suele ser destinatario | Confirmada |
| 5 | 0.1; 0.2; abreviaturas; D12 (nueva) | "4 = 'nosotros' inclusivo" equiparaba la 4.ª persona con el plural español; no explicaba el número | Cuatro personas "que no especifican número"; pronombres sin número; `-naka` "plural de énfasis" (p.18, 182) | Plural con `-naka` y `-pxa`; concordancia de número opcional (p.181, 242) | Explicación incompleta | D12 | Confirmada |
| 6 | 0.2; D13 (nueva) | "No tiene conjunciones", sin matizar | Coordinación por yuxtaposición, `-sa2`, `-cha` y usos de `uka` (p.312); `-mpi1` conjuntor (p.207–208) | "No tiene … conjunciones", pero "pueden aparecer representados mediante sufijos" (p.32) | Explicación incompleta | D13 | Confirmada |
| 7 | D3; 8.4 | Fijaba `'` como norma sin separar la normalización interna de la ortografía publicada | `'` | `’` en todo el libro | Diferencia de nivel | D3 distingue la representación publicada (`’`, L2) del carácter interno (decisión técnica) | Confirmada (nivel a); nivel b: decisión técnica |
| 8 | D11; 3.4; 8.4; 10 | Riesgo de mezclar segmentaciones | `-p-` + `-xa-`/`-ka-`; `-si-` + `-ka-` | `-pxa`, `-ska` | Diferencia de análisis | Cada ejemplo usa la segmentación de su fuente y lo indica; 3.4 aclara que las correspondencias no son identidades | Diferencia confirmada; elección pendiente |
| 9 | 5.2; 8.2; Pendientes | La hipótesis `-:-` + `-pana` para `urukïpanaya` se presentaba como "más coherente" | Solo `-ipana` subordinador de sujetos distintos (p.161) | `-ipana` desiderativo (p.53) y consecutivo de sujetos diferentes (p.200) | Diferencia no resuelta | La hipótesis queda marcada ‡ y pendiente; no se usa como regla | Pendiente |
| 10 | D8; 8.2; 8.3 | Faltaba documentar las excepciones a "una sola forma escrita" | `ma:` (p.295); `mä`, `pä` en texto corrido (p.57–58) | Dos formas válidas por escrito (p.57); pronunciación `mä`/`pä` ante nombre (p.43); "una sola forma escrita" (p.71, 74); compuestos (p.54–55) | Explicación incompleta | D8 y fila de 8.3 con las excepciones explícitas; sin regla de elección | Confirmada |
| 11 | 8.4 (fila "separador") | Ponía `chur-t-wa` → `lur(a)-th(a)-wa` como si fueran la misma palabra | `chur.t.wa` "yo doy/di" (p.68) | `lur(a).th(a).wa` "hago" (p.61); `churtha` (p.155) | Error de la guía | Las raíces se muestran por separado; no se intercambian | Corregido |
| 12 | 8.2 (`umäña`) | Segmentación `agua-VBLZ.LONG-INF†` presentada sin advertencia | Solo `uma.ña` "tomar" (p.117, 127) | `umäña` "ser agua" dentro del alargamiento "con valor fonémico" (sin pérdida de segmento), aunque su traducción es copulativa (p.48–49) | Explicación incompleta en L2 | Segmentación retirada; clasificación pendiente | Pendiente |
| 13 | 8.3 (x, r) | Regla de `r` sin la versión de L1 ni los casos sin explicar | /x/ y /r/ no iniciales en palabras nativas; /r/ inicial en préstamos (p.41) | x no inicial en raíces (p.42); r no inicial salvo en refonemizadas (p.44); `rixinta`, `raphaku` sin explicar | Explicación incompleta | Regla reformulada como "no inicial en palabras nativas", con los casos sin explicar | Confirmada; casos pendientes |
| 14 | D4; 8.4 | Hablaba de forma "preferida" | `-xa ~ -ja` y alomorfo `-:` (p.205) | `-ja` como marca de 1.ª persona, con variantes (p.149) | Diferencia de enfoque | D4: `-ja` es la forma normativa de L2; el análisis conserva la variación de L1 | Confirmada |
| 15 | 10 | Tabla de prueba vacía | — | — | — | Tabla 10.1 con 34 ejemplos atestiguados y comprobados; 10.2 con las formas hipotéticas; 10.3 deja la prueba con corpus como pendiente, sin tabla vacía | Confirmada |
| 16 | 2.1 (`-ø`) | "Equivale al complemento cero de L1" | Complemento cero marcado por pérdida de vocal (p.233) | Acusativo `-ø`, vocal escrita; también "meta" (p.154–155) | Diferencia de análisis | "Correspondencia funcional; análisis distintos" | Confirmada |

---
## 12. Discrepancias L1–L2 que todavía no pueden resolverse

Se documentan sin reconciliarlas. "Tipo": C = contradicción; E = diferencia de enfoque o de análisis; I = información insuficiente en las fuentes.

| # | Tema | L1 | L2 | Tipo | Qué haría falta para resolverla |
|---|---|---|---|---|---|
| 1 | 1.ª persona simple | `/ta/` sin aspiración, distinguido de 2→3 solo por la morfofonémica (p.77, 144, 159) | `-tha` aspirado frente a `-ta` (p.61, 176) | E/I | Saber si la diferencia es dialectal, de transcripción o de análisis; ninguna fuente lo explica |
| 2 | Vocal final entre palabras | Pérdida gramatical (complemento cero, modificador de 3 o más vocales, verbo nominalizado; p.68, 72, 233) | Desonorización oral; se escribe completa (p.66–70) | E | Para la escritura manda L2 (D6); la discrepancia de análisis sigue abierta |
| 3 | `-pacha` | Al menos cuatro sufijos `-pacha`, todos piden consonante; `taq.pacha` fosilizado (p.209, 228) | Un `-pacha` "todo, entero" dúctil (`jupapacha` conserva la vocal; p.63–64) y un `-pacha` independiente "dubitativo objetivo" (p.229) | C | Ejemplos con condiciones de ambas fuentes |
| 4 | Categoría "dúctil" | Cada sufijo tiene exigencia fija; condiciones para `-layku`/`-kama` (p.199, 228) | Sufijos que "a veces" eliden, sin condiciones (p.60–64); `-kama`, `-ya` y `-ma` aparecen a la vez como débiles y dúctiles (p.62–63) | C/I | Condiciones de L2 para cada sufijo |
| 5 | `-ma` POSS.2, `-nama`, `-naqa-` | Posesivos piden vocal antes (p.205); `-nama` y `-naqa-` piden consonante (p.113, 230) | Los tres con formas alternantes (`an.ma ~ anu.ma`, `uk.nama ~ uka.nama`, `ap.naqa.ña ~ apa.naqa.ña`, p.62) | C | Igual que 4 |
| 6 | Plural verbal y progresivo | `-p-` + `-xa-`/`-ka-`; `-si-` + `-ka-` (p.111–112) | `-pxa`, `-ska` (p.181, 202) | E | Decisión de proyecto para el tokenizador (D11) |
| 7 | `-ka-` con negación | INCOMPL; no es negativo en sí (p.111) | "Negativo"; antecede a `-ti` "para dar sentido y completar la idea de negación" (p.65, 231–232) | E | L1 dice que suele aparecer pero no es obligatorio (p.283, 301); L2 lo presenta como parte de la negación, sin decir si puede faltar |
| 8 | Objeto sin sufijo | Complemento cero, marcado por la pérdida de vocal (p.233) | Acusativo `-ø`, vocal escrita; también "meta" (p.154–155) | E | — (la escritura sigue a L2) |
| 9 | `-ru` | Complemento de la flexión (humano) frente a relacional (p.210–212) | Complemento indirecto y dirección (p.155–157) | E | Terminológica; resuelta en la glosa (D9), no en el análisis |
| 10 | `-ipana` | Subordinador de sujetos distintos, poco frecuente en La Paz (p.161) | Subordinador consecutivo de sujetos diferentes (p.200) **y** sufijo desiderativo "que sea" en fórmulas (`urukïpanaya`, p.53) | I | Confirmar si el uso de p.53 es el mismo sufijo; hipótesis ‡ en 5.2 |
| 11 | "Ser N" | Verbalizador `-:-` (p.162, 238–240) | Verbo `kankaña` reducido a diéresis (p.49–52, 224) | E | — |
| 12 | Remoto cercano de 1.ª y 2.ª persona | "Solo plenamente funcionales en hablantes mayores" (p.146) | Paradigma completo y de uso normal (`sarayätha`, p.185) | E/I | Datos de uso actual |
| 13 | INFR | Tiempo verbal (p.148–149); formas inconsistentes en el propio L1 (3→2 `-pachatan` p.149 / `-pachatam` p.165; INFR+REM.C 4→3 p.157 / p.165) | Sufijo independiente "dubitativo objetivo", también con nombres (p.229) | C (dentro de L1) / E | Corregir L1 con otra fuente |
| 14 | `-naka` con numerales | Prohibido (p.207), pero atestiguado (p.251) | "Generalmente" no (p.154) | C (dentro de L1) | Datos |
| 15 | Orden de palabras | Libre entre constituyentes; cambia el estilo (p.293–294) | SOV básico, con permutaciones posibles (p.241, 243) | E | — (el generador usa SOV, D10) |
| 16 | Préstamos | Sin vocal añadida (`lapis`, p.316) | Vocal final añadida (`lapisa`, p.77) | E | — (la escritura sigue a L2) |
| 17 | Ordinal | `kawk-i:r` = `-:-` + `-iri` (p.69) | Sufijo `-ïri` ordinal (`mayïri`, p.167) | E | — |
| 18 | `umäña` | No registrada | "Valor fonémico" sin pérdida de segmento, pero traducida "ser agua" (p.48–49) | I (en L2) | Segmentación de L2 |
| 19 | `kawkha` | "¿qué lugar?" (p.187) | No atestiguada | I | — |
| 20 | `-ti` de `akankktti` "no estoy aquí" | Rotulado "interrogativo sí/no" (p.68) en una oración negativa | — | C (dentro de L1) | — |

## 13. Reglas que NO deben usarse todavía en un generador automático

| # | Regla o recurso | Motivo | Dónde se documenta |
|---|---|---|---|
| 1 | Cualquier conversión automática de formas de L1 a la ortografía de L2 (`-ta` → `-tha`, `:` → diéresis, `-tan` → `-tana`, `-ñani` → `-ñäni`, `-xa` → `-ja`…) | Análisis distintos (D1, D5); solo valen formas atestiguadas en L2 o generadas desde un paradigma de L2 | D1, D5, 8.4 |
| 2 | Regla del complemento cero de L1 (borrar la vocal final del objeto) para escribir | L2 manda escribir la vocal (D6) | 5.3 b1 |
| 3 | Regla 2/3 de L1 (borrar la vocal final del modificador de 3 o más vocales) para escribir | Ídem | 5.3 b2 |
| 4 | Elisión del verbo nominalizado ante el verbo principal (L1 p.72) para escribir | Ídem | 5.3 b3 |
| 5 | Variación de los sufijos dúctiles (`-kama`, `-sti`, `-chiqa`, `-ya`, `-pacha`, `-ma`, `-nama`, `-naqa-`) | Sin condiciones documentadas; no es alternancia libre (D7) | 5.2.1 |
| 6 | Elección automática entre `maya/mä`, `paya/pä`, `khaya/khä` | Las dos formas son válidas y no hay regla de elección para la escritura (D8) | D8 |
| 7 | Asignar `COMPL.RU` a cualquier nominal humano con `-ru` | Depende de qué verbos gobiernan un complemento `-ru` (L1 p.210, 212); falta información léxica | D9, 7.3 A |
| 8 | Permutaciones de constituyentes (L1 p.293–294) | La posición de `-wa`/`-ti`/`-sa` depende de la pregunta subyacente; no está modelada. Usar solo SOV (D10) | D10, sección 1 |
| 9 | Análisis `-:-` + `-pana` para `urukïpanaya`; el uso desiderativo de `-ipana` | Hipótesis no confirmada | 5.2, 12 #10 |
| 10 | Formas hipotéticas de 10.2 (`churthwa`, `churäna`, `Juwanti Mamanïthwa`) | No atestiguadas | 10.2 |
| 11 | Plural nominal `-naka` combinado con numerales | Contradicción en L1; tendencia en L2 | 12 #14 |
| 12 | Paradigmas de L1 con formas inconsistentes o sin ejemplo: INFR (3→2, 4→3 con REM.C), DES y REPR ("muy irregulares", p.154–155), FUT 3→4 | Formas no confirmadas | 3.2, 12 #13 |
| 13 | Remoto cercano de 1.ª/2.ª persona como forma frecuente | L1 lo limita a hablantes mayores (p.146) | 12 #12 |
| 14 | `umäña` y la diéresis "copulativa" fuera de las formas atestiguadas (por ejemplo, tras `-ni`, donde L2 escribe `utanithwa`) | Clasificación y segmentación pendientes | 8.2, 8.4 |
| 15 | Variantes no normativas que L2 menciona (`-ŋa` futuro, `-ŋa`/`-ña`/`-ya` POSS.1, `-nti` por `-mpi`, `-taya` por `-tä`) | Variación oral o regional; no son forma escrita normalizada | 2.1, 3.4 |
| 16 | Sufijos de L2 sin correlato verificado en esta guía (`-lla`, `-tuqi`, `-lanti`, `-nama`, `-k'alla`, `-walla`, `-nma`, `-sa` negativo condicional) | Sin contraste con L1 ni condiciones de uso | 2.1, 4.1 |

---
## Pendientes

### Resueltos al unir las partes (v1)
- Sufijos oracionales, independientes y nominales (pendiente de la Parte 1): resueltos en las secciones 2 y 4.
- `jani`/`jan`/`-ti`, `-wi`, `-pta-` y `-ta` nominalizador (Parte 1): resueltos en 7.3.
- `-spa` (Parte 2): es DES 3>3 (tabla 3.2, L1 p.166).
- "R" sin precisar (Parte 2): `-ya:-`/`-:na` = REM.C y `-tayna`/`-ta:-` = REM.L (tabla 3.2).
- 1.ª persona `-ta`/`-tha` (Parte 3 #1) → D5. POSS.1 (Parte 3 #2) → D4. Notación `:`/`¨` y apóstrofo (Parte 3 #12) → D2, D3. Elisión entre palabras (Parte 3 #10) → D6.

### Resueltos en v2 (con los dos libros completos)
- **`-ipana` subordinador:** L1 (p.161) y L2 (p.200) coinciden: subordinador de sujetos diferentes. La etiqueta `OPT` se eliminó. El uso desiderativo de L2 p.53 (`urukïpanaya`) sigue sin resolver: ver sección 12.
- **`-naka` con números:** L1 se contradice (p.207 frente a p.251); L2 dice "generalmente" no (p.154). Se trata como tendencia.
- **POSS.1:** L2 da `-ja` como forma de 1.ª persona (p.148–149). D4 confirmado.
- **1.ª persona:** L2 `-tha` (p.176; `churtha`, p.155); L1 `-cta` (p.68, 144). D5 quedaba para el corpus en v2; en v3 se documentan las dos formas sin conversión y la escritura usa el paradigma de L2.
- **Orden de palabras:** L2 declara SOV y da el orden de complementos (p.241, 243, 255). D10 adopta SOV por defecto.
- **`kawkha` / `qawqha`:** lexemas distintos ("¿qué lugar?" / "cuánto"; L1 p.185, 187).
- **Escritura de L1:** escribe la elisión entre palabras (p.57–58, 68, 233) y usa `:` al segmentar y `¨` en el texto corrido (p.57–58, 69, 73).
- **`mä`/`maya`:** en la escritura valen las dos formas también ante nombre (L2 p.57). D8 corregido.
- **Ejemplos que faltaban:** FUT 2>1 (L1 p.289), `-piya` (p.289), `-chim` (p.205) y `-tisti` (p.290).
- **Comparación morfológica con L2:** secciones 2.1, 3.4 y 4.1.

### Abiertos (prioridad para la siguiente etapa)

> **v3:** la lista completa de discrepancias sin resolver está en la sección 12 y las reglas vetadas para el generador, en la 13. Esta lista se conserva como registro de v2.

1. D5, D6, D8, D10 y D11: resolver con la prueba de la sección 10.
2. D11: decidir si el tokenizador sigue a L1 (`-p-x-`, `-s-k-`) o a L2 (`-pxa`, `-ska`).
3. Sufijos "dúctiles" con clasificación inconsistente dentro de L2 (p.62–63).
4. Ejemplos que siguen faltando: FUT 3>4 (`-istani`), varias celdas de IMP, DES y REPR, y los oracionales `-:` (EXCL) y `-waya` (AFF.POL). Buscar en L1 caps. VII y XI.
5. `-ti` final de `akankktti` "no estoy aquí": L1 lo rotula "interrogativo sí/no" (p.68); en la negación debería ser NEG.
6. INFR 3→2 (`-pachatan`, p.149, frente a `-pachatam`, p.165) e INFR+REM.C 4→3 (p.157 frente a p.165): elegir una forma. Por el patrón del SIMP (`-tam`), la más probable es `-pachatam`.
7. Sufijos de L2 sin correlato en esta guía (`-lla`, `-tuqi`, `-lanti`, `-nama`, `-k'alla`, `-walla`, `-nma`; `-sa` negativo condicional): decidir si entran en el generador.
8. Contradicciones internas de L2, para no copiarlas a la guía:
   - `-ipana` "único sufijo que empieza y termina en vocal" (p.53) y "único de tres sílabas" (p.200). Lo contradicen `-i`, `-iri`, `-itu` y la lista de sufijos de tres sílabas de la p.145 (`-irisma`, `-istani`).
   - `/r/` "no aparece en posición inicial" (p.44), pero la misma lista trae `rixinta` y `raphaku`.
   - `-ita` "de primera a segunda persona" (p.197), cuando sus ejemplos son 2→1.
   - `lurañäniwa` traducido "hacemos" (p.61), cuando es futuro.
   - `-pura` encabezado como "privativo" (p.167), cuando describe reciprocidad.
   - El texto dice que en 3.ª y 4.ª persona no cae la vocal, pero la tabla escribe `lur(a).i.wa` (p.61).

### Notas de extracción originales (detalle por parte)

> **Nota v2.** Estas notas son las de v1, cuando la extracción trabajó con un fragmento de L1 (pp.17–24 y 67–170) y con L2 hasta la p.80. Los dos libros ya están completos; lo resuelto con ellos figura arriba, en "Resueltos en v2". Se conservan como registro.
#### Parte 1 (verbo)

Fuera del fragmento (no están los Caps. I, III, VIII–XII ni el glosario de sufijos oracionales):
- Los sufijos oracionales (`-wa`, `-xa`, `-sa`/`-s`, `-ti`, `-ya`, `-chi(m)`, `-pi`…), los independientes (`-raki`, `-ki`, `-puni`…) y los nominales (`-ru`, `-ta`, `-na`/`-n`, `-taki`, `-mpi`, `-naka`, posesivos) solo se mencionan; sus reglas y funciones: FALTA. Glosas provisionales mías: `-wa` AFF, `-xa` TOP, `-sa`/`-s` Q, `-ti` NEG (y Q), `-raki` ADD (por «también», p.131), `-n` LOC/GEN, `-ru` ACC cuando marca el complemento de la flexión y ALL cuando es direccional (p.86, p.115), `-mpi` COM, `-taki` BEN, `-ta` ABL.
- Cap. IX (verbalizadores y nominalizadores): `-wi`, `-pta-` y el sentido de `-ta` nominalizador solo se nombran; función de `-wi` deducida del único ejemplo (p.132).
- Funciones de `jani` y `jan`, y distribución de `-ti`: FALTA (Cap. VIII 1.4 y XII).
- Ejemplos con segmentación propia que no hay en el fragmento: FUT 2→1 (`-ita:ta`) y 3→4 (`-istani`); IMP 1→2, 2→1, 3→1, 3→4, 3→2; DES salvo 1→3; REPR salvo 2→3; REM.C/REM.L distintos de 3→3; NI de 1.ª/2.ª/4.ª. De `saña` solo hay formas sueltas sin segmentar (p.142).

Inconsistencias dentro del libro (se transcribió cada dato con su página):
- REM.C 2→1: p.147 dice que esa interacción usa el SIMP o el REM.L por homofonía con 3→4, pero el Cuadro VII.3.1 (p.164) da `-ista:sta` ~ `-ista`.
- INFR 3→2: `-pachatan` en p.149 frente a `-pachatam` en p.165; INFR+REM.C 4→3: `-pachaya:tan` en p.157 frente a `-pachaya:ta` en p.165.
- IMP 2→3 `-m`: v_v en p.153, v_c en p.164. DES 3→4: `-(i)staspa(n)` en p.154 y `-(i)st{u~a}spa(n)` en p.166 (extracción ambigua). El libro mismo advierte que el DES es muy irregular y que el REPR no es fácil de predecir (p.154–155).
- Cap. VI: p.107 dice que la Clase II tiene 11 sufijos, pero se describen 10 (el Cuadro VI.1 repite `-ka-`); p.94 dice que 10 sufijos de la Clase I verbalizan, el cuadro marca 11 con «//».
- p.117: el ejemplo `apa-ya-ni-waya-si-p-k-i` rotula la `-si-` como `-si1-` tras `-waya-`, pero el Cuadro VI.1 coloca `-si1-` antes de `-ni-` (lo coherente sería `-si2-`).
- p.121, notas 2 y 6: «estudios posteriores» (Briggs 1976) contradicen que `-su-` no verbalice y admiten que `-si-` sí puede; las afirmaciones «no verbaliza» del texto (`-su-`, `-qa-`, `-ta-`, `-xata-`, `-xaru-`…) son provisionales.
- p.68: `aka-n-k-k-t-ti` se da como /akankti/ pero se escribe `akankktti`; el `-ti` final se rotula «interrogativo sí/no» aunque la oración es negativa («no estoy aquí»); la misma forma `-ti` marca negación en p.111.
- Cuadro IV.6 (p.76), según la extracción de texto, no lista `-qa-` ni `-p-`, que sí figuran como «vocal precedente» en p.113; se siguió p.113. En el Apéndice C (p.130) `-rpaya-` aparece como «–rgaya–».
- Dialectos: REM.L 3→3 tiene cuatro variantes (`-tayna`, `-ta:na`, `-ta:ña`, `-taña`; p.147); `-istani` ~ `-stani` (p.145); `-ipana` es de La Paz (p.161); algunos dialectos permiten grupos consonánticos iniciales (nota 3, p.169).

Método y verificación:
- Páginas: las del libro impreso (el fragmento cubre pp.17–24 y 67–170). Verificadas visualmente contra la imagen: Cuadro VI.1 (p.97), p.155 (REPR) y Cuadro VII.3.1 (p.164). El resto de los cuadros (IV.1–IV.8, VII.1, VII.3.2–VII.3.4) se leyó del texto extraído; las letras c/v de esos cuadros no se comprobaron en imagen.
- Frecuencias (Apéndice C, p.130) provienen de un corpus pequeño (nueve diálogos y ocho cuentos, trabajo de 1969–1971); sirven solo para ordenar.
- Los ejemplos de 9a se tomaron literalmente del libro; solo cambiaron los puntos por guiones y se añadieron glosas y la fuente. Las glosas léxicas de raíces no definidas en el libro (p. ej. `khuchi` «chancho», `ukha` «allí») salen de la traducción que da el libro para toda la oración.

#### Parte 2 (nombre y sintaxis)

- **Contradicción -naka con números**: L1 p.207 y nota 34 dicen que -naka no va en un nombre modificado por número (`*pusi uta-naka`, se dice `pusi uta`), pero el ejemplo de p.251 trae `pusi jach'a janq'u uta-naka-pa-sa`.
- **ACC**: el libro no define ACC; la distinción -ru complemento/relacional es mía en la glosa (ver respuesta 1).
- **-spa** (3>3.DES) no está glosado explícitamente en este fragmento; lo glosé por analogía con -sma y -sna (L1 p.233, 286). Verificar con la Parte 1.
- **REM**: los ejemplos con -tayna / -ya:t aparecen solo como "R"; hay que decidir si son REM.C o REM.L con la Parte 1 (no usados en 9b).
- **Subordinada condicional**: L1 p.298 imprime `sara.p.x.a.ñani.w` (con "x.a" separado); no lo usé. Faltan reglas explícitas para "si" y "cuando" más allá de -sa/-sina y -xa.
- **Errores de impresión probables**: p.282 `t'ant'.t chur.i.ti` (-t y -ti a la vez); p.193 `Ch'unu.ch.iri`; p.227 glosas "2p 1p" en `Naya.n.x paya.w uta.jx`.
- **-sa1 / -sa2 y -ti (Q/NEG)**: el libro los trata como homófonos por razones comparativas (p.282, 292 nota 4); a veces la diferencia no es observable.
- **-chi- vs. flexión NI**: p.287 dice que -chi- solo ocurre con flexión no-involucrador, pero en `uta-ki-:-chi-xay` no se ve flexión separada; la glosa SUPP es provisional.
- **Variación dialectal**: orden de -mpi1 con -:xa/-ta/-xa/-pacha1 difiere entre Qumpi y Tiwanaku (p.208, 256); orden de localizadores y POSS "todas las combinaciones aceptables" (p.206).
- **Ejemplos FALTA** en la sección 4: -: , -waya, -piya, -chim/-chix/-tisti (el libro da ejemplos que incluyen segmentos sin glosa en L1).
- **No cubierto**: numerales y temporales (L1 p.174–181), solo se tomó lo necesario para el orden (número + nombre). Tampoco se resumieron los verbos derivacionales de Clase I de la lista de p.190 más allá de nombrarlos.
- **Ambigüedad de kuna-t-sa**: "¿de qué?" vs. "¿por qué?" (p.216); `-xa-ta` ("acerca de") se trata a veces como un solo sufijo (p.261, notas 13 y 23).

#### Parte 3 (alfabeto)

1. **1.ª persona simple:** L1 `-ta` (L1: `chur-t-wa`) frente a L2 `-tha`. Comprobar en L1 si es `-ta`, `-t(a)` o una diferencia ortográfica.
2. **POSS.1:** L2 no da el paradigma. Falta confirmar `-ja ~ -xa` (L1). Ojo: `tataxa` en L2 es tata + TOP (p.68), así que `tata-xa` como POSS.1 de L1 no tiene respaldo en L2. `kullakañawa` (p.68, "mi hermana") no se explica.
3. **Texto contra recuadro (p.40):** el texto habla de seis órdenes que incluyen "glotales", pero el cuadro solo tiene cinco columnas y pone j en velares y x en postvelares.
4. **Contradicción de L2 (p.61):** "en la 3.ª y 4.ª persona no hay pérdida de vocales", pero su tabla trae `lur(a).i.wa` y `sar(a)+i`.
5. **Clasificación inconsistente (p.62–63):** -kama aparece como débil (`uta.kama`) y como dúctil; -ya y -ma aparecen en dos clases.
6. **Tabla p.65:** `juta.tha` = "vengo" y `juta.tha.wa` = "vine" (misma -tha); la fila `iki.ka.tha.ti` tiene dos glosas ("no duermo" y "¿dormí?").
7. **`phäña`** tiene tres glosas en L2: "leña" (p.43), "cocinar" (p.46) y "bosta" (p.47), con formas completas distintas (phayaña, phayana).
8. **Una forma contra dos formas:** L2 pide una sola forma escrita (p.71, p.74) pero conserva maya/mä (p.57) y compuestos en ambas formas (p.55). Decidir cuál usa el proyecto.
9. **`-ipana`:** L2 dice que es el único sufijo que empieza con vocal (p.53), pero `-i` (3.ª persona, p.62) también.
10. **Elisión entre palabras en L1:** L2 llama "elisionista" a la tradición de Hardman (escrito "Hartman" en p.72). Verificar si L1 escribe `tatax utaruw sari` o la forma completa.
11. **`kawkha` frente a `qawqha`** (p.43): confirmar que son léxemas distintos.
12. **Decisión de notación:** `:` (L1) frente a `¨` (L2). Unificar en el corpus y normalizar `’` → `'` (o al revés).
13. **FALTA en el fragmento:** reglas de guion, mayúsculas, puntuación y división de palabras; paradigma completo de sufijos personales; traducción de varios ejemplos (aru/ari, -ipana, p.58).
14. **Numeración de L2:** hay dos secciones "1.3" (p.34 y p.36). El recuadro del alfabeto (p.35) es una imagen; las palabras ilustrativas bajo cada letra no se transcriben por ser ilegibles a ese tamaño.
