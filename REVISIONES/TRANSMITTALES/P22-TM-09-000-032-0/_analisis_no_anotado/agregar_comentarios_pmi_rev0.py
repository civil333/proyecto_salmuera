#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_pmi_rev0.py
Anota el PMI Procedure Rev 0 (P22-BA-09-000-006) del submittal 25007-0075.
Veredicto del TM N32: Code 1 - Approved.

TRAZA INTERNA - NO SE EMITE. Un Codigo 1 no lleva CC_ADASA. Este PDF es el
respaldo del analisis: no se adjunta ni se sube al enlace de descarga.

TRIAJE DEL 12-AGO. El primer borrador dejaba este documento sin codigo, con dos
puntos abiertos. Contrastado contra el texto literal de lo que ADASA pidio, BW
Water contesto las dos cosas:
  - La OBS-02 del TM N20 pedia "add a project-applicability statement at IFC
    Rev 0". La agregaron en la clausula 2.0 del frontispicio: "10 percent of the
    Super duplex high pressure piping component will be tested and witness by
    ADASA". Exigir ademas que la clausula 8.1 y el Apendice 1 dejaran de citar
    PTS 15.02.01 era leer mas estricto que la instruccion escrita.
  - La OBS-01 del TM N20 y el correo del 06-Ago pedian la base de aceptacion.
    Esta en la nueva clausula 13.4, y se borraron las dos clausulas que remitian
    la aceptacion a normas de refineria.
  - El 5% de perneria NO se reapoya: la ET no lista pernos ni tuercas entre los
    componentes con PMI ("tuberias, accesorios, cuerpos de valvula, bridas"), de
    modo que fue pedido nuevo de ADASA y ya esta cumplido a 10% en las filas de
    canieria.

Lo que queda son dos items de ASEO que el transmittal lleva a la Seccion 3 para
la proxima emision natural, y que NO son condicion. Se anotan con esa etiqueta
para que la traza no se lea como una exigencia.

len(COMENTARIOS) = 2, espejo de los dos items de aseo de la Seccion 3.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import NOTE, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-006_0_PMI_Procedure.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-006_0_PMI_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 75",
        "P22-BA-09-000-006_0_ PMI PROCEDURE.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "Acceptance and rejection criteria shall be specified by the customer",
        "page_fallback": 17,
        "text": (
            "NOTE-01: housekeeping for the next natural\n"
            "issue of this procedure. Not a condition of\n"
            "this approval.\n"
            "The acceptance basis asked for on 6 August is\n"
            "now stated in clause 13.4, which closes the\n"
            "point. Clauses 13.1 and 13.2 still give a\n"
            "generic answer alongside it, so the section\n"
            "reads three ways.\n"
            "At the next issue: state the basis once, on\n"
            "conformity to UNS S32750, and spell the\n"
            "designation with that prefix."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": "extent of PMI testing",
        "page_fallback": 12,
        "text": (
            "NOTE-02: housekeeping for the next natural\n"
            "issue of this procedure. Not a condition of\n"
            "this approval.\n"
            "The project applicability requested at\n"
            "Transmittal N20 is declared in the scope of the\n"
            "cover section, and the bolt and nut sampling of\n"
            "Appendix 1 is now 10% per lot for piping, which\n"
            "closes the point. This clause and the heading\n"
            "of Appendix 1 still refer the extent to\n"
            "PTS 15.02.01.\n"
            "At the next issue: align both with the extent\n"
            "the cover section already declares and with row\n"
            "2.4 of the Inspection and Test Plan."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
