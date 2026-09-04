#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_plc_lcp_fat_procedure_revC.py
Anota el PLC/LCP FAT Procedure - Hardware Rev C (P22-PP-09-000-001) del submittal
25007-0090 (ENTREGA 90). Veredicto del TM N38: Code 2 - Approved as noted.

len(COMENTARIOS) = 2, espejo 1:1 del bloque Action de la subseccion 2.11
("OBS-01 and OBS-02 on the annotated PDF").

ALCANCE. Re-emision que responde al TM N37, subseccion 2.7, Code 3. Solo se
revisa contra esa instruccion escrita; no se introducen observaciones nuevas.

  OBS-01 del N37, emitir procedimiento separado del registro  -> CERRADO. No se anota.
  OBS-02 del N37, ocho items categoria A cerrados y firmados  -> SE TRASLADA. Pertenece
        al registro de la Rev B, no a este procedimiento en blanco. Va a la Seccion 3.
  OBS-03 del N37, citar esquematico e I/O List por revision   -> CERRADO. No se anota.
  OBS-04 del N37, cuatro entradas digitales del modulo -A2    -> CERRADO. No se anota.
  OBS-04 del N37, mapa de reles de salida                     -> NO CERRADO -> OBS-01
        ADASA declara el valor vinculante: la I/O List Rev 6, aprobada en Codigo 1,
        lleva el calentador CIP como item 108 sobre el rele KA8. No se le pide a BW
        Water que decida cual de sus dos columnas gobierna.
  OBS-05 del N37, instrumentos de ensayo identificados        -> CERRADO en estructura.
        La seccion existe y queda por completar en el ensayo. No se anota.
  NOTE-01 del N37, un solo numero de documento                -> CERRADO. No se anota.
  NOTE-02 del N37, terminal de operacion instalado            -> SE TRASLADA. Se responde
        sobre el esquematico, que no vino en este lote. Va a la Seccion 3.

El determinante cerro: la Rev B era el registro de un ensayo ya corrido, en 16
paginas fotografiadas con 1.378 caracteres extraibles; la Rev C es un
procedimiento nativo de 23 paginas con lugar, fecha y resultados en blanco. Ya no
se sostiene el Code 3. Lo que queda vive en la tabla de salidas digitales.

OBS-02 de este transmittal (TAG repetido) esta DENTRO del alcance de la OBS-04
del N37, que pidio reconciliar el mapa de reles: no es observacion nueva. El
procedimiento truncó los TAG al sufijo HS001; la I/O List los lleva completos con
el prefijo del equipo, de modo que el pedido es escribir el TAG completo.

Reparto por pagina (indices 0-based):
    13   tabla de salidas digitales, canal 7 y rele KA8 -> OBS-01
    13   misma tabla, TAG repetido en cinco filas       -> OBS-02
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-PP-09-000-001_C_PLC_LCP_FAT_Procedure.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR,
                       "P22-PP-09-000-001_C_PLC_LCP_FAT_Procedure_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 90", "25007-0090",
        "P22-PP-09-000-001_C PLC-LCP FAT Procedure - Hardware.pdf",
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
        "search": "Test – Analog Inputs",
        "page_fallback": 13,
        "page_min": 13,
        "text": (
            "OBS-01: this row states two different things\n"
            "about the same output.\n"
            "The test text of channel 7 describes relay KA8\n"
            "as the CIP heater on and off command. The\n"
            "remarks column of the same row marks KA8 as\n"
            "spare.\n"
            "The I/O List Rev 6, approved at Code 1, settles\n"
            "it: item 108 is the CIP heater on and off\n"
            "command, a dry-contact digital output. KA8 is\n"
            "not a spare.\n"
            "The input side of this reconciliation did\n"
            "close and is not repeated here.\n"
            "Correct: at Rev 0 correct the remarks column of\n"
            "this row against the I/O List Rev 6."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MENOR,
        "search": None,
        "page_fallback": 13,
        "page_min": 13,
        "text": (
            "OBS-02: five output rows carry the same tag.\n"
            "The rows for relays KA4 to KA8 test five\n"
            "different commands and all five are labelled\n"
            "HS001, which is only the tag suffix.\n"
            "The I/O List Rev 6 carries the full tag with the\n"
            "equipment prefix, so the CIP heater command is\n"
            "REL-09-001-HS001 and every output is unique.\n"
            "Correct: at Rev 0 write each output row with\n"
            "the full tag the I/O List carries."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
