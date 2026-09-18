#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_plc_lcp_schematic_revC.py
Anota el PLC/LCP Schematic Diagram Rev C (P22-CD-09-008-002) del submittal
25007-0093 (ENTREGA 93, recibido el 14-Sep-2026). Veredicto del TM N40: Code 2 -
Approved as noted, reiterado (tercer ciclo: N20, N37, N40).

len(COMENTARIOS) = 3, espejo 1:1 del bloque Action de la subseccion 2.2
("OBS-01, NOTE-01 and NOTE-02 on the annotated PDF").

ALCANCE. Solo los IDs del N37: OBS-01 (borne del calefactor) CERRADO en la hoja 37,
verificado por render; OBS-02 (terminal -D8S) NO CERRADO y refutado en la hoja de
comentarios -> OBS-01 de este ciclo; NOTE-01 (cita de revision) reconocido como error,
pero la hoja de comentarios repite un codigo equivocado -> NOTE-02. Hallazgo nuevo sobre
lo que BW Water agrego: los TAG de la hoja 37 son anotaciones del PDF -> NOTE-01.

IDs SECUENCIALES por (pagina, y del ancla), asignados por _ajustar_cajas (paginas 1-based):
    29   lista de materiales, fila 11                  -> OBS-01
    38   hoja 37, entradas -A3 (tags como FreeText)    -> NOTE-01
    71   hoja de comentarios consolidada               -> NOTE-02

Las anotaciones FreeText propias de BW Water en la hoja 37 (XA007, XA008, XB002 y el
poligono rojo) NO se tocan. ajustar_cajas() usa x1_max=880 para no tapar la columna del
cajetin de las laminas A3.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
sys.path.insert(0, SCRIPT_DIR)
from doc_annotator import MAYOR, NOTE, add_pdf_comments  # noqa: E402
from _ajustar_cajas import asignar_ids_secuenciales, ajustar_cajas  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-008-002_C_PLC_LCP_Schematic.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-008-002_C_PLC_LCP_Schematic_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 93",
        "P22-CD-09-008-002_C PLC-LCP Schematic Diagram.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    {
        "serie": "OBS", "fill": MAYOR,
        "search": "2711P-T10C21D8S", "page_fallback": 28, "page_min": 28,
        "text": "{ID}: row 11 still reads 2711P-T10C21D8S, third cycle. ADASA declared "
                "the 2711P-T10C22D9P binding at Transmittal N30 on the approved PLC and "
                "HMI Datasheet P22-ET-09-008-001 Rev 0 (two Ethernet RJ45 ports, 1 GB); "
                "an approved datasheet is not revised to the terminal installed. "
                "Correct: replace row 11 with the -D9P at Rev 0.",
    },
    {
        "serie": "NOTE", "fill": NOTE,
        "search": "CIP Heater Running", "page_fallback": 37, "page_min": 37,
        "text": "{ID}: the tags XA007, XA008 and XB002 and the red frame are PDF "
                "annotations, not drawing content; they do not travel with the native "
                "file or a print without comments. Correct: draw the three tags in the "
                "schematic at Rev 0.",
    },
    {
        "serie": "NOTE", "fill": NOTE,
        "search": "is fully sufficient", "page_fallback": 70, "page_min": 70,
        "text": "{ID}: the replies cite P22-ET-09-008-001 RevC as the PLC/LCP Panel "
                "Outline Drawing. That code is the PLC and HMI Datasheet, approved at "
                "Rev 0; the Outline is P22-CD-09-008-001 and this schematic is "
                "P22-CD-09-008-002. Correct: cite each document by its own code and "
                "revision on the comment sheet at Rev 0.",
    },
]

if __name__ == "__main__":
    assert len(COMENTARIOS) == 3, len(COMENTARIOS)
    orden = asignar_ids_secuenciales(PDF_LOCAL, COMENTARIOS)
    print("IDs por orden de aparicion:", orden)
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
    print("Ajuste de cajas:")
    ajustar_cajas(PDF_OUT, COMENTARIOS, x1_max=880)
