"""Revisión de realismo del léxico de producción v1.0 (rama dev/Camilo).

Corrige columnas de data/lexicon/lexico_sin_raices.csv que eran demasiado amplias. No cambia ids,
raíces ni formas del español salvo dos femeninos erróneos (mejor, peor). Es idempotente: se puede
volver a ejecutar sin efecto.

Uso:  python src/chulupi/revision_lexico.py data/lexicon/lexico_sin_raices.csv
"""
import csv
import sys

PER, ANI, COM, BEB, ROP, HER, REC, PLA, LUG, VIV, TIE, ABS, OBJ = (
    "persona", "animal", "comida", "bebida", "ropa", "herramienta", "recipiente", "planta",
    "lugar", "vivienda", "tiempo", "abstracto", "objeto")


def j(*clases):
    return "|".join(clases)


# 1. Adjetivos: clases que pueden modificar (mod_clases, CH-406).
COLORES_COSAS = j(ANI, COM, ROP, HER, REC, PLA, VIV, OBJ)
MOD_CLASES = {
    # estado físico de las cosas
    "abierto": j(ROP, REC, VIV, OBJ), "cerrado": j(ROP, REC, VIV, OBJ),
    "lleno": j(REC, VIV, LUG), "vacío": j(REC, VIV, LUG),
    "duro": j(COM, HER), "blando": j(COM, OBJ),
    "seco": j(COM, ROP, PLA, OBJ, LUG), "mojado": j(ANI, ROP, PLA, OBJ, PER),
    "entero": j(COM, REC), "perdido": j(ANI, ROP, HER, REC, OBJ),
    "pesado": j(ANI, ROP, HER, REC, OBJ, COM), "liviano": j(ROP, HER, REC, OBJ),
    "ligero": j(ROP, HER, REC, OBJ, COM),
    "suave": j(ANI, ROP, OBJ, COM, BEB), "áspero": j(ROP, OBJ, HER), "rugoso": j(OBJ, PLA, HER),
    "liso": j(ROP, OBJ, HER, REC), "brillante": j(OBJ, HER, REC, ROP),
    "transparente": j(REC, OBJ, BEB, ROP), "opaco": j(REC, OBJ, ROP),
    "dorado": j(OBJ, REC, HER, ROP, COM), "plateado": j(OBJ, REC, HER, ROP),
    "quemado": j(COM, OBJ, ROP, VIV, PLA),
    "sucio": j(ANI, ROP, HER, REC, VIV, LUG, OBJ, BEB), "limpio": j(ANI, ROP, HER, REC, VIV, LUG, OBJ, BEB),
    "afilado": j(HER, OBJ), "puntiagudo": j(HER, OBJ, PLA),
    "cuadrado": j(OBJ, REC, COM), "redondo": j(OBJ, REC, COM), "plano": j(OBJ, LUG, HER),
    "roto": j(OBJ, HER, REC, ROP, VIV), "torcido": j(OBJ, HER, PLA), "recto": j(OBJ, HER, PLA),
    "escondido": j(ANI, OBJ, HER, REC, COM, LUG, VIV), "gratuito": j(COM, BEB, OBJ),
    "nuevo": j(ROP, HER, REC, OBJ, VIV, LUG, ABS),
    "usado": j(ROP, HER, REC, VIV, OBJ), "moderno": j(ROP, HER, REC, LUG, VIV, OBJ),
    "tejido": j(ROP, OBJ), "bordado": j(ROP, OBJ), "lanudo": j(ANI, ROP), "peludo": j(ANI, ROP),
    "ocupado": j(PER, LUG, VIV), "desocupado": j(LUG, VIV),
    # colores (sin bebidas, salvo morado: "chicha morada")
    "claro": COLORES_COSAS, "oscuro": j(ANI, COM, ROP, HER, REC, PLA, LUG, VIV, OBJ),
    "negro": COLORES_COSAS, "blanco": COLORES_COSAS, "gris": COLORES_COSAS, "marrón": COLORES_COSAS,
    "café": COLORES_COSAS, "amarillo": COLORES_COSAS, "rojo": COLORES_COSAS,
    "verde": j(COM, ROP, HER, REC, PLA, VIV, OBJ), "azul": j(ROP, HER, REC, PLA, VIV, OBJ),
    "celeste": j(ROP, HER, REC, PLA, VIV, OBJ), "rosado": j(ROP, HER, REC, PLA, VIV, OBJ, COM),
    "anaranjado": j(ROP, HER, REC, PLA, VIV, OBJ, COM), "morado": j(ROP, HER, REC, PLA, VIV, OBJ, COM, BEB),
    # tamaño
    "gordo": j(PER, ANI), "flaco": j(PER, ANI), "delgado": j(PER, ANI, ROP, HER, PLA, OBJ),
    "largo": j(ANI, ROP, HER, REC, PLA, LUG, VIV, ABS, OBJ), "corto": j(ANI, ROP, HER, REC, PLA, LUG, VIV, ABS, OBJ),
    "ancho": j(ROP, HER, REC, PLA, LUG, VIV, OBJ), "estrecho": j(ROP, HER, REC, LUG, VIV, OBJ),
    "fino": j(ROP, HER, REC, PLA, OBJ), "grueso": j(ROP, HER, REC, PLA, OBJ, ANI),
    "alto": j(PER, ANI, PLA, LUG, VIV), "bajo": j(PER, PLA, LUG, VIV),
    # valoración
    "importante": j(PER, LUG, VIV, ABS, OBJ),
    "necesario": j(COM, BEB, ROP, HER, REC, OBJ, ABS),
    "útil": j(HER, REC, OBJ, ROP, ABS), "inútil": j(HER, REC, OBJ, ROP, ABS),
    "especial": j(PER, COM, BEB, ABS),
    # "mejor" y "peor" van antes del nombre en español ("el mejor papá"); el generador los pone después.
    "mejor": j(ABS), "peor": j(ABS),
    "normal": j(PER, ANI, ABS, OBJ),
    # origen
    "nativo": j(PER, ANI, PLA), "aymara": j(PER, ROP, COM), "quechua": j(PER, ROP, COM),
    "boliviano": j(PER, COM, BEB, ROP), "argentino": j(PER, COM, BEB, ROP), "chileno": j(PER, COM, BEB, ROP),
    "peruano": j(PER, COM, BEB, ROP), "brasileño": j(PER, COM, BEB, ROP), "mexicano": j(PER, COM, BEB, ROP),
    "extranjero": j(PER, COM, BEB, ROP), "andino": j(PER, ANI, COM, ROP, LUG, PLA),
    "originario": j(ABS), "mundial": j(ABS), "indígena": j(PER, LUG, ABS),
    "plurinacional": j(LUG, ABS), "bolivianista": j(ABS),
    # lugares
    "montañoso": j(LUG), "nevado": j(LUG), "tropical": j(LUG), "poblado": j(LUG), "templado": j(LUG),
    "profundo": j(LUG, REC),
    "ácido": j(COM, PLA),
}
# Formas femeninas erróneas del borrador.
FORMAS = {"mejor": {"es_f": "mejor", "es_pl_f": "mejores"}, "peor": {"es_f": "peor", "es_pl_f": "peores"}}

# 2. Verbos: clases del objeto (obj_clases) y del sujeto (suj_clases) demasiado amplias.
OBJ_CLASES = {
    "construir": j(VIV, OBJ), "crear": j(OBJ, HER, REC, ROP), "elaborar": j(COM, OBJ, ROP),
    "ordenar": j(OBJ, ROP, HER, REC, VIV), "conectar": j(OBJ, HER), "diseñar": j(OBJ, ROP, VIV, HER),
    "instalar": j(OBJ, HER), "fabricar": j(OBJ, HER, REC, ROP),
    "decorar": j(VIV, OBJ, REC, ROP, COM), "adornar": j(VIV, OBJ, REC, ROP, COM),
    "modelar": j(OBJ, REC), "pintar": j(OBJ, VIV, REC), "tallar": j(OBJ, HER, REC),
    "dibujar": j(OBJ, ANI, PLA, VIV, LUG),
    "escribir": j(OBJ, ABS),
    # guardar cosas: sin animales ("almacenar la vicuña")
    "almacenar": j(COM, BEB, ROP, HER, REC, PLA, OBJ), "acumular": j(COM, BEB, ROP, HER, REC, PLA, OBJ),
    "empacar": j(COM, BEB, ROP, HER, REC, OBJ), "desempacar": j(COM, BEB, ROP, HER, REC, OBJ),
    "colocar": j(COM, BEB, ROP, HER, REC, PLA, OBJ), "acomodar": j(COM, BEB, ROP, HER, REC, PLA, OBJ),
    "descargar": j(COM, BEB, ROP, HER, REC, PLA, OBJ), "envolver": j(COM, ROP, HER, REC, PLA, OBJ),
    # cocina: verbos que solo se dicen de comida sólida ("amasar el agua")
    "amasar": j(COM), "moler": j(COM, PLA), "pelar": j(COM, PLA), "rellenar": j(COM), "tostar": j(COM),
    "asar": j(COM), "hornear": j(COM), "freír": j(COM), "guisar": j(COM), "sazonar": j(COM), "rebanar": j(COM, PLA),
    "doblar": j(ROP, OBJ),
}
SUJ_CLASES = {
    "hervir": j(BEB, COM, REC), "arder": j(OBJ, PLA, ROP), "humear": j(COM, BEB),
    "brillar": j(OBJ, HER, REC, ROP), "romperse": j(OBJ, HER, REC, ROP), "quebrarse": j(OBJ, HER, REC),
    "secarse": j(ROP, PLA, COM), "derretirse": j(COM, OBJ), "oxidarse": j(HER, OBJ, REC),
    "pudrirse": j(COM, PLA), "sonar": j(OBJ),
}


def main(ruta):
    with open(ruta, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        campos, filas = r.fieldnames, list(r)
    hechos = {"mod": set(), "formas": set(), "obj": set(), "suj": set()}
    for f in filas:
        if f["cat"] == "ADJ" and f["es_m"] in MOD_CLASES:
            f["mod_clases"] = MOD_CLASES[f["es_m"]]
            hechos["mod"].add(f["es_m"])
        if f["cat"] == "ADJ" and f["es_m"] in FORMAS:
            f.update(FORMAS[f["es_m"]])
            hechos["formas"].add(f["es_m"])
        if f["cat"] in ("V_TR", "V_DITR") and f["es_m"] in OBJ_CLASES:
            f["obj_clases"] = OBJ_CLASES[f["es_m"]]
            hechos["obj"].add(f["es_m"])
        if f["cat"].startswith("V_") and f["es_m"] in SUJ_CLASES:
            f["suj_clases"] = SUJ_CLASES[f["es_m"]]
            hechos["suj"].add(f["es_m"])
    faltan = (set(MOD_CLASES) - hechos["mod"]) | (set(FORMAS) - hechos["formas"]) | \
             (set(OBJ_CLASES) - hechos["obj"]) | (set(SUJ_CLASES) - hechos["suj"])
    if faltan:
        raise SystemExit(f"No están en el léxico: {sorted(faltan)}")
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\r\n")   # el archivo del repositorio usa CRLF
        w.writeheader()
        w.writerows(filas)
    print(f"Adjetivos: {len(hechos['mod'])} · formas: {len(hechos['formas'])} · "
          f"objetos de verbos: {len(hechos['obj'])} · sujetos de verbos: {len(hechos['suj'])}.")


if __name__ == "__main__":
    main(sys.argv[1])
