#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_plc_lcp_schematic_revB.py
Anota el PLC/LCP Schematic Diagram Rev B (P22-CD-09-008-002) del submittal
25007-0086 (ENTREGA 86). Veredicto del TM N37: Code 2 - Approved as noted.

len(COMENTARIOS) = 3, espejo 1:1 del bloque Action de la subseccion 2.3
("OBS-01 to OBS-02 and NOTE-01 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N20, subseccion 2.7, Code 2, con una sola
NOTE-01: confirmar la asignacion de entradas y salidas despues de emitida la
Control Philosophy Rev D. Solo se revisa contra esa instruccion escrita.

  NOTE-01 del N20, reconciliar la asignacion de I/O -> CIERRE PARCIAL -> OBS-01
                                                      y la cita -> NOTE-01

La reconciliacion esta casi hecha y se verifico sobre las laminas, no sobre la
declaracion: la lamina 39 cablea la salida del calentador de CIP en el modulo -A4,
salida 7, con el rele KA8; las entradas 1 a 4 de la lamina 35 figuran como reserva,
coherente con las tres filas que la Rev 6 elimino; y las señales del equipo de aire
acondicionado estan en las laminas 37 y 38. Falta un borne.

LA OBS-02 NO ES OBSERVACION NUEVA. El terminal de operacion se declaro vinculante
en el TM N30, que nombro a este esquematico entre los cuatro documentos a corregir,
y no se corrigio. Ahora ademas hay evidencia de que el tablero se armo con el -D8S:
el registro del FAT de la ENTREGA 88 visa la fila que lo da por instalado.

🔴 DECISION RESERVADA AL USUARIO, que este texto preserva. Caben dos caminos —exigir
el terminal declarado, con impacto de plazo a dias del FAT, o aceptar el -D8S y
exigir por escrito como cumple el requisito de dos puertos Ethernet del datasheet
aprobado—. El comentario pide DECLARAR POR ESCRITO como se cierra la brecha, que no
cierra ninguno de los dos caminos.

Reparto por pagina (indices 0-based):
    28   lista de materiales del tablero de control -> OBS-02
    35   primera lamina de entradas digitales       -> OBS-01
    70   hoja de comentarios consolidada            -> NOTE-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, NOTE, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-CD-09-008-002_B_PLC_LCP_Schematic.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 86",
        "P22-CD-09-008-002_B PLC-LCP Schematic Diagram.pdf",
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
        "search": "SPARE",
        "page_fallback": 35,
        "page_min": 35,
        "text": (
            "OBS-01: the CIP heater running feedback has\n"
            "no terminal.\n"
            "The reconciliation is otherwise done: the\n"
            "heater output is wired on sheet 39 through\n"
            "relay KA8, inputs 1 to 4 here are spare,\n"
            "consistent with the three rows deleted at\n"
            "I/O List Rev 6, and the air conditioning\n"
            "signals are on sheets 37 and 38.\n"
            "CIP HEATER RUNNING, item 109 of the I/O\n"
            "List Rev 6, has no terminal on any of the\n"
            "four digital input sheets: nineteen inputs\n"
            "assigned against twenty active in the list,\n"
            "with thirteen free terminals.\n"
            "Correct: assign it a digital input terminal\n"
            "when the schematic is issued at Rev 0."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "2711P-T10C21D8S",
        "page_fallback": 28,
        "page_min": 28,
        "text": (
            "OBS-02: the operator terminal is not the one\n"
            "ADASA declared binding.\n"
            "Row 11 of this bill of material reads HMI1,\n"
            "Touch Screen, 2711P-T10C21D8S, Allen-Bradley, and\n"
            "it is the only full catalogue number in the 71\n"
            "sheets.\n"
            "At Transmittal N30 ADASA declared the\n"
            "2711P-T10C22D9P binding, on rows 15 and 18 of the\n"
            "approved datasheet, which require two Ethernet\n"
            "RJ45 ports and 1 GB; the -D8S carries one port\n"
            "and 512 MB. That transmittal named this schematic\n"
            "among the documents to be corrected, and the\n"
            "comment sheet of this revision carries no row for\n"
            "the point.\n"
            "The point is no longer documentary: the record of\n"
            "the panel hardware test signs off the row that\n"
            "verifies the -D8S installed on the inner door.\n"
            "Correct: state in writing how BW Water proposes\n"
            "to close this gap, and how the terminal supplied\n"
            "meets the two Ethernet ports of the approved\n"
            "datasheet, before the schematic is issued at\n"
            "Rev 0."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": NOTE,
        "search": "I/O List RevB",
        "page_fallback": 70,
        "page_min": 70,
        "text": (
            "NOTE-01: the reply cites a revision that does not\n"
            "exist.\n"
            "The reply reads has been added and revised in I/O\n"
            "List RevB. That list carries numeric revisions\n"
            "and the revision issued for construction with\n"
            "this same submittal is Rev 6.\n"
            "Correct: cite the I/O List by its code,\n"
            "P22-LI-09-008-001, and by its numeric revision on\n"
            "the comment sheet issued at Rev 0."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
