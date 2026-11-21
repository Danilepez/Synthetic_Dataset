# Prototipo de referencia

Código Python que acompaña a la especificación (Anexo B de `docs/specification/chulupi_lang_spec.md`). El notebook `notebooks/chulupi_generador.ipynb` reutiliza su lógica; los errores del prototipo que se corrigieron están en `docs/decisiones/PREGUNTAS.md` ("Errores del prototipo corregidos").

| Archivo | Contenido |
|---|---|
| `chulupi_motor.py` | Grafemas, validación de palabras, tabla de morfemas B/A y el algoritmo de construcción de palabras (CH-701) |
| `chulupi_oraciones.py` | Constructor de oraciones B/A (§9) y del español (§10), con el léxico de ejemplo |
| `test_chulupi.py` | Pruebas: CH-710, los 40 casos, [ATESTIGUADO], CH-1013 |

Para ejecutar las pruebas (lee los datos de `tests/`):

```bash
cd src/chulupi/prototipo
python -m unittest test_chulupi -v
```
