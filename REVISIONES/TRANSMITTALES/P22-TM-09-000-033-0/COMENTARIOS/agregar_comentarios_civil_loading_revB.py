#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_civil_loading_revB.py
Anota el Civil and Loading Layout Rev B (P22-DWG-09-005-001), submittal
25007-0076 (E76). Veredicto del TM N33: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de su subseccion.

REGLA DE ALCANCE (criterio del usuario, 17-Ago-2026). La revision de un
documento que responde a comentarios previos se limita a SI ESOS COMENTARIOS
ESTAN CERRADOS. No se introducen observaciones nuevas. El alcance lo fija el
texto literal de la columna de comentario del cliente de la Consolidated Comment
Sheet, que en este plano transcribe la NOTE-01 del TM N16:

  "Please include on Rev 0 (IFC):
   1. Total weight of the modified 40 ft container.
   2. Confirm the RO Skid operating weight (items 6-7, 8,058 kg) fully accounts
      for all interior piping (super-duplex HP + process), including steel mass,
      fluid inventory and fittings, TOGETHER WITH SKID FRAME, pressure vessels
      and wet membranes. If any piping mass is excluded, declare it separately."

Respuesta de BW Water, dos lineas: "1. Total approximate weight indicated in the
revised drawing" y "2. Refer to notes in the drawing".

  Parte 1 -> NO CERRADA. El numero de la Nota 2, 13.300 kg, esta rotulado
             "container and its contents" y es la suma en seco del contenido SIN
             el contenedor y sin inventario de fluido -> OBS-01.
  Parte 2 -> NO CERRADA en lo que toca al marco del skid, que el pedido nombra
             literal y que tras reclasificar las filas 6 y 7 a RO PRESSURE
             VESSELS no quedo en ninguna fila -> OBS-02. El resto de la parte 2
             SI cerro: las Notas 3 y 4 y las seis filas nuevas responden que se
             contabiliza aparte.

SE RETIRAN, por ser comentarios nuevos y no cierre de la NOTE-01: los diametros
de anclaje de los detalles 4 y 5, el empotramiento de los plintos 5 y 7, el
escalon de 22 mm de los plintos centrales, el reparto de las seis filas nuevas
entre las dos fundaciones, el TAG del mezclador estatico y el peso de operacion
del estanque CIP. Todos quedan en el ledger de la E76 y los de obra civil en
_IMPACTO_OOCC_BL.md, para la conversacion con L&A.

Reparto por lamina (indices 0-based):
    0   caratula A4
    1   lamina 1 - planta, tabla de cargas de 23 filas y notas -> los dos
    2   lamina 2 - plintos, secciones y detalles de anclaje (sin anotar)
    3   Consolidated Comment Sheet
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

# --- Fast-save guard: 23.369 y 11.649 vectores en las dos laminas A1 -------
import fitz  # noqa: E402
_orig_save = fitz.Document.save


def _fast_save(self, filename, *a, **k):
    return _orig_save(self, filename, garbage=1, deflate=False)


fitz.Document.save = _fast_save
# ---------------------------------------------------------------------------

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-001_B_Civil_Loading_Layout.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-005-001_B_Civil_Loading_Layout_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 76",
        "P22-DWG-09-005-001_Civil and Loading Layout_Rev.B-006.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01: part 1 of the note raised at Transmittal\n"
            "N16 asked for the total weight of the modified 40\n"
            "ft container. Note 2 gives 13,300 kg labelled as\n"
            "the container and its contents, and that figure is\n"
            "the dry sum of the contents EXCLUDING the container\n"
            "and excluding all fluid inventory. Rows 1 to 16 in\n"
            "operation plus rows 17 to 23 dry give 30,529.5 kg.\n"
            "The conversion is right; what was summed is not\n"
            "what the label says.\n"
            "Correct: state the weight of the empty modified\n"
            "container, and reword Note 2 to say what its\n"
            "figure includes."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02: part 2 of the same note asked to confirm\n"
            "that the RO Skid operating weight accounts for the\n"
            "interior piping \"together with skid frame,\n"
            "pressure vessels and wet membranes\". The Notes 3\n"
            "and 4 and the six new rows answer what is counted\n"
            "separately, which closes that part. The skid frame\n"
            "does not: rows 6 and 7 were reclassified to RO\n"
            "PRESSURE VESSELS and Note 4 limits that weight to\n"
            "membranes and hydraulic contents, so the frame is\n"
            "in no row. PIPE SUPPORTS is another item.\n"
            "Correct: state in which row the skid frame is\n"
            "accounted for, or add its row."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
