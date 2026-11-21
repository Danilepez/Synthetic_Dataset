# Borrador de `lexico_sin_raices.csv` — qué revisar

**Contenido:** 2.793 entradas con las columnas de CH-402, más la columna `admite_ben` (v1.1.2). Las columnas `raiz` y `silabas` están vacías: las llena el generador de raíces (§3).

| Categoría | Entradas | Objetivo CH-407 | Nota |
|---|---|---|---|
| N_HUM | 294 | 300 | Parentesco, oficios, roles y gentilicios |
| N_NOHUM | 1.700 | 1.700 | 1.142 escritas a mano y 558 abstractos añadidos automáticamente (ver abajo) |
| V_INTR | 125 | 150 | |
| V_MOV | 64 | 100 | En español no hay muchos más verbos de movimiento comunes |
| V_TR | 271 | 450 | |
| V_DITR | 37 | 100 | Ídem: los verbos con destinatario son pocos |
| ADJ | 272 | 300 | |
| ADV_T | 30 | 30 | Incluye `pasado_remoto` (v1.1.2) |

En total hay 497 verbos, frente a los 800 del objetivo. No los rellené con verbos raros: el déficit se compensa con más variedad de nombres. Si el equipo quiere más verbos, conviene añadirlos con los marcos que ya existen.

## Cómo se armó

- **Nombres, verbos, adjetivos y adverbios:** listas escritas a mano, por clase semántica y por marco verbal. Están en los archivos `datos_*.py`; el CSV se regenera con `construir_lexico.py`.
- **Rango (CH-402):** frecuencia del lema en el lado español del dataset de 18.000 pares, lematizado con spaCy. Las entradas que no aparecen van al final de su categoría y llevan la nota "sin frecuencia en el dataset".
- **Clases de los verbos:** cada verbo tiene un **marco** (anotado en `notas`, por ejemplo `marco T_COMER`) que fija sus clases de sujeto, objeto, instrumento y lugar, `obj_persona` y `admite_ben`. Para corregir un grupo entero basta con cambiar el marco en `datos_verbos.py`.

## Qué revisar, por prioridad

1. **Los 558 abstractos automáticos** (nota `AUTO: abstracto por sufijo`). Salen del dataset por terminación (-ción, -dad, -miento…). Quité los que no eran abstractos o eran delicados, pero conviene repasarlos y borrar los que sobren. Muchos vienen de la Constitución y de GlobalVoices.
2. **Marcos de los verbos.** Hay que revisar qué objetos acepta cada uno (`obj_clases`) y si tiene `obj_persona` y `admite_ben`. Es lo que más influye en que las oraciones tengan sentido.
3. **Adjetivos (`mod_clases`).** Hay que comprobar que cada adjetivo solo modifique lo que tiene sentido. Por ejemplo, "grande" ya no acepta `comida`, para evitar "pan grande".
4. **Géneros automáticos** (nota `género automático`), sacados de spaCy o de reglas. Ya corregí `papa`, `amapola`, `vicuña` y `tulipán`.
5. **Plurales y femeninos automáticos** (nota `plural automático`, `femenino y plural automáticos`).

## Avisos para el generador

- **Ids desde `L10001`.** Así no chocan con el léxico de ejemplo (`L0001`–`L0026`), que el notebook sigue necesitando para los 40 casos de prueba.
- **`ART_EL` en `notas`.** Son nombres femeninos que empiezan con *a* tónica (`agua`, `hacha`, `hambre`, `águila`, `área`, `ánfora`, `haba`). En singular llevan "el"/"un": "el agua", no "la agua". CH-1008 no lo contempla, así que hay que implementarlo.
- **Verbos reflexivos** (nota `reflexivo`): `esconderse`, `sentarse`, etc. La tabla de conjugaciones debe ponerles el pronombre.
- **Palabras andinas en el español** (`chuño`, `api`, `chairo`, `aguayo`, `yatiri`…): son normales en el español de Bolivia y se dejaron a propósito.
- **Verbos con objeto solo humano** (`entrevistar`, `felicitar`, `perdonar a alguien`…): quedaron fuera. Con CH-914 (objeto directo no humano) solo podrían usarse en transiciones.
