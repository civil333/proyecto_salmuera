#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_valve_list_revE.py
Anota la Valve List Rev E (P22-LI-09-005-002) del submittal 25007-0091
(ENTREGA 91). Veredicto del TM N39: Code 2 - Approved as noted.

len(COMENTARIOS) = 1, espejo 1:1 del bloque Action de la subseccion 2.1
("OBS-01 on the annotated PDF").

ALCANCE. Re-emision comprometida por escrito por BW Water para TRES cambios. Solo
se revisa contra esos tres; no se introducen observaciones nuevas.

  Cuatro TAG del modelo 3D ausentes de las listas aprobadas  -> CERRADO. No se anota.
  Valvula reductora en CIT-09-004 en vez de placa de orificio -> CERRADO. No se anota.
  Succion de la bomba CIP en SS316 reflejada en la lista      -> NO CERRADO -> OBS-01

Los cuatro TAG estan y los cuatro figuran en el P&ID Rev 0 aprobado; VRP-09-001 es
la valvula reductora. El tercero no: la linea CP-SS316-DN150-09-022 es 316L en la
Line List Rev 1 aprobada en Codigo 1, y la valvula que esta sobre ella sigue en PVC.

Verificacion del vinculo entre la valvula y la linea, que es lo que sostiene la
observacion: en el P&ID Rev 0, hoja 11, el rotulo CP-SS316-DN150-09-022 esta a 16
puntos de VM-09-065, que es ademas la unica valvula DN150 del circuito CIP.

FUERA DE ALCANCE, en _ANALISIS_N39.md con su razon: la tension de los actuadores
(alcance interno del proveedor), la portada que declara Rev A, el historial que no
coincide con el del cajetin y la hoja de comentarios sin comentarios transcritos.

Reparto por pagina (indices 0-based):
    1    tabla de valvulas, fila de VM-09-065   -> OBS-01
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, add_pdf_comments  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_E_Valve_List.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-LI-09-005-002_E_Valve_List_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 91", "P22-LI-09-005-002_E Valve List.pdf",
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
        "search": "VM-09-065",
        "page_fallback": 1,
        "page_min": 1,
        # El cuadro no puede pasar de unas dieciocho lineas: la lamina mide 842 pt
        # de alto y un texto mas largo se dibuja fuera del area visible, de modo
        # que se pierde la primera linea, que es la que lleva el identificador.
        "text": (
            "OBS-01: this valve sits on a line the approved\n"
            "Line List carries in stainless steel, and it is\n"
            "still listed in PVC.\n"
            "ADASA acknowledges the two changes that are done:\n"
            "the four valve tags of the 3D model comment sheet\n"
            "are in and all four are on the P&ID Rev 0, and\n"
            "VRP-09-001 is the pressure regulating valve that\n"
            "replaces the orifice plate at CIT-09-004.\n"
            "The third change is not reflected. The CIP pump\n"
            "suction line CP-SS316-DN150-09-022 is 316L on the\n"
            "Line List Rev 1, approved at Code 1 in Transmittal\n"
            "N38. This valve is the one on that line and the\n"
            "only DN150 valve of the CIP circuit, and it reads\n"
            "PVC body, PVC trim, PVC disc and EPDM seat, with\n"
            "ANSI 150 lug ends.\n"
            "Correct: at Rev 0 state the body, trim and seat\n"
            "material of this valve against the approved Line\n"
            "List, and its end connection and rating."
        ),
    },
]

if __name__ == "__main__":
    r = add_pdf_comments(PDF_LOCAL, PDF_OUT, COMENTARIOS)
    print(r)
