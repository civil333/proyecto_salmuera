#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_hmi_revC.py
Anota el HMI Display Screenshot Rev C (P22-LI-09-008-016) del submittal
25007-0090 (ENTREGA 90). Veredicto del TM N38: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.10
("OBS-01 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N31, subseccion 2.5, Code 2, que dejo
siete observaciones y un pedido de declaracion. Solo se revisa contra esa
instruccion escrita; no se introducen observaciones nuevas.

  OBS-01 del N31, variables electricas y potencia en kW  -> CERRADO. No se anota.
  OBS-02 del N31, LS-09-002 en nivel bajo                -> CERRADO. No se anota.
  OBS-03 del N31, BH-09-001 en la bomba de alta          -> CERRADO. No se anota.
  OBS-04 del N31, TE-09-001 en el devanado               -> CERRADO. No se anota.
  OBS-05 del N31, VE-09-005 en la reposicion CIP         -> CERRADO. No se anota.
  OBS-06 del N31, PIT-09-003 en primera etapa            -> NO CERRADO, INVERTIDO -> OBS-01
        ADASA declara la asignacion en vez de pedir que la reconcilien. Ademas
        PIT-09-005 es la variable de proceso del lazo que gobierna el bypass del
        turbocargador VE-09-002 en el Control Narrative Rev 1: el TAG cruzado cae
        justo sobre el lazo que protege ese equipo.
  OBS-07 del N31, FIT-09-004 en el rechazo a drenaje     -> CERRADO. No se anota.
  Pedido del N31, donde se muestran PIT-09-008/FIT-09-002-> CERRADO. No se anota.

Seis de siete cerradas. La hoja de comentarios de BW Water declara solo dos
acciones; la verificacion por render muestra que hicieron mas de lo que
declararon, y eso se reconoce en el Status de la subseccion.

VERIFICACION OBLIGATORIA. Las pantallas son IMAGENES: get_text() devuelve vacio
en las paginas de proceso y el anclaje por texto NO funciona. Se usa page_fallback
con posicion fija y se comprueba el cuadro por render PNG.

Reparto por pagina (indice 0-based):
    76   pantallas 7.3 RO 1st Stage y 7.4 RO 2nd Stage -> OBS-01
         (las dos pantallas del hallazgo estan en la misma pagina)
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-016_C_HMI_Display_Screenshot.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR,
                       "P22-LI-09-008-016_C_HMI_Display_Screenshot_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 90", "25007-0090",
        "P22-LI-09-008-016_C HMI Display Screenshot.pdf",
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
        "page_fallback": 76,
        "page_min": 76,
        "offset_y": 250,
        "text": (
            "OBS-01: the two feed pressure transmitters are\n"
            "crossed between these two screens.\n"
            "The RO 1st Stage screen shows PIT-09-005\n"
            "upstream of BOI-09-001. The RO 2nd Stage screen\n"
            "has been changed to show PIT-09-003 upstream of\n"
            "BOI-09-002.\n"
            "The Instrument List Rev F defines PIT-09-003 as\n"
            "the RO 1st Stage Feed Pressure Transmitter and\n"
            "PIT-09-005 as the RO 2nd Stage one.\n"
            "PIT-09-005 is also the process variable of the\n"
            "loop that governs the turbocharger bypass\n"
            "VE-09-002 in the Control Narrative Rev 1.\n"
            "The remaining six observations of Transmittal\n"
            "N31 are closed and are not repeated here.\n"
            "Correct: at Rev 0 tag the first-stage feed\n"
            "PIT-09-003 and the second-stage feed PIT-09-005."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
