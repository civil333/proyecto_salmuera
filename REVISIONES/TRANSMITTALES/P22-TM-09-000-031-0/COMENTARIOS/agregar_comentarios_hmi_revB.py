#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agregar_comentarios_hmi_revB.py
Anota el HMI Display Screenshot Rev B (P22-LI-09-008-016), submittal 25007-0074
(E73). Veredicto del TM N31: Code 2 - Approved as noted.

len(COMENTARIOS) = 7, espejo 1:1 del bloque Action de la subseccion del HMI.

ALCANCE: solo los dos comentarios del TM N22 que la Rev B no levanto. Los tres
que si cerraron (tendencias, ruta de consignas, evidencia ISA-101) no se anotan.
  OBS-01            <- OBS-01 del N22, variables electricas
  OBS-02 a OBS-07   <- OBS-04 del N22, la mitad de consistencia de TAG

Estructura del archivo (indices 0-based):
    0        caratula
    1        indice
    2        introduccion y primera seccion de faceplates
    3..71    manual de faceplates (biblioteca Rockwell)
    72       panel de navegacion y lista de alarmas
    73       tendencias
    74       inicio de sesion
    75       pantallas 7.1 RO Overview y 7.2 RO Feed
    76       pantallas 7.3 RO 1st Stage y 7.4 RO 2nd Stage
    77       pantallas 7.5 RO CIP y 7.6 Antiscalant
    78, 79   Consolidated Comment Sheet

POR QUE LAS ANOTACIONES VAN EN EL FRONTISPICIO Y NO SOBRE CADA PANTALLA.
Se probo primero lo natural, una anotacion sobre la pagina de su pantalla, y el
render mostro que no sirve: las capturas ocupan el ancho util completo (x = 70 a
527 de una pagina de 595 pt) y la skill coloca la caja contra el margen derecho,
de modo que las cajas tapaban justo los TAG que seniala cada observacion - los
dos TE-09-002 de la pantalla de alimentacion y los dos VE-09-003 de la primera
etapa. No hay banda lateral libre en ninguna pagina de pantallas. Se adopta
entonces el mismo criterio con que se anoto la Rev A en el TM N22, que agrupo
las observaciones en el frontispicio por ser un documento de imagenes:
  indice (idx 1)        -> OBS-01 a OBS-04
  introduccion (idx 2)  -> OBS-05 a OBS-07
Cada texto abre nombrando su seccion y su pantalla, de modo que la anotacion es
autolocalizable sin depender de la pagina en la que este colocada.

DOCUMENTO DE IMAGENES: las paginas de pantallas son capturas rasterizadas y
"search" no encuentra nada en ellas. Todas las entradas van por page_fallback.

El color del recuadro transmite la severidad; el texto NO lleva etiqueta.
Cierre obligatorio: render PNG de las dos paginas anotadas, comprobando que las
cajas se leen completas y no se pisan entre si.
"""
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios  # noqa: E402

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-LI-09-008-016_B_HMI_Display_Screenshot.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-LI-09-008-016_B_HMI_Display_Screenshot_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 73",
        "P22-LI-09-008-016_HMI Display Screenshot_B.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found:\n  " + src)
        sys.exit(1)

COMENTARIOS = [
    # ---------------- indice: las cuatro de las paginas 76 ----------------
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-01 (Section 7.1, RO Overview): this\n"
            "screen displays the specific energy\n"
            "consumption in kWh/m3 and a total power\n"
            "figure, but no voltage and no current appear\n"
            "on any screen of this document. The Technical\n"
            "Specification (P22-ET-09-000-001-0), Section\n"
            "5.4 - Control System, requires the\n"
            "electrical-variables meter readings to be\n"
            "present on an HMI screen together with the\n"
            "specific energy consumption.\n"
            "Correct: add the meter readings for voltage,\n"
            "current and power to this screen, and express\n"
            "power in kW rather than kWh."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-02 (Section 7.1, RO Overview): in the\n"
            "ANTISCALANT block, TANK LSL and TANK LSH are\n"
            "both tagged LS-09-001. The Instrument List\n"
            "Rev E sets LS-09-001 as the high level switch\n"
            "and LS-09-002 as the low level switch, and the\n"
            "Antiscalant screen of Section 7.6 shows them\n"
            "correctly.\n"
            "Correct: tag the low level LS-09-002 and the\n"
            "high level LS-09-001."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-03 (Section 7.2, RO Feed): the pump\n"
            "between the cartridge filter and the first\n"
            "stage is tagged BH-09-002. The Equipment List\n"
            "Rev B assigns BH-09-001 to the RO HP Feed Pump\n"
            "and BH-09-002 to the CIP Pump, which is\n"
            "correctly tagged on the RO CIP screen of\n"
            "Section 7.5. The same tag is therefore on two\n"
            "different machines and BH-09-001 appears on no\n"
            "screen.\n"
            "Correct: tag this pump BH-09-001."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 1,
        "text": (
            "OBS-04 (Section 7.2, RO Feed): the two\n"
            "temperature indicators of the high-pressure\n"
            "pump both read TE-09-002. The Instrument List\n"
            "Rev E sets TE-09-001 as the RO HP Pump winding\n"
            "and TE-09-002 as the bearing; TE-09-001\n"
            "appears on no screen. The RO CIP screen\n"
            "resolves the equivalent pair correctly.\n"
            "Correct: tag the winding indicator TE-09-001\n"
            "and keep TE-09-002 on the bearing."
        ),
    },
    # ---------------- introduccion: las tres de la pagina 77 --------------
    {
        "id": "OBS-05",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 2,
        "text": (
            "OBS-05 (Section 7.3, RO 1st Stage): the valve\n"
            "to RO PERMEATE and the valve to MAKE-UP CIP\n"
            "are both tagged VE-09-003. The Valve List\n"
            "Rev D carries VE-09-005 for the CIP make-up\n"
            "and chemical fill service, and the Plant\n"
            "Control Philosophy Rev 0 confirms it on its\n"
            "page 55; VE-09-005 appears on no screen.\n"
            "Correct: tag the make-up CIP valve VE-09-005."
        ),
    },
    {
        "id": "OBS-06",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 2,
        "text": (
            "OBS-06 (Sections 7.3 and 7.4): PIT-09-005\n"
            "appears on the first-stage screen and on the\n"
            "second-stage screen. The Instrument List Rev E\n"
            "defines it as the RO 2nd Stage Feed Pressure\n"
            "Transmitter. On the first-stage screen it sits\n"
            "upstream of BOI-09-001, which is the position\n"
            "of PIT-09-003, the RO 1st Stage Feed Pressure\n"
            "Transmitter; PIT-09-003 appears on no screen.\n"
            "Correct: tag the first-stage feed pressure\n"
            "PIT-09-003."
        ),
    },
    {
        "id": "OBS-07",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 2,
        "text": (
            "OBS-07 (Sections 7.3 and 7.5): FIT-09-005\n"
            "appears on the first-stage screen and on the\n"
            "RO CIP screen. The Instrument List Rev E\n"
            "defines it as the CIP Cartridge Filter\n"
            "Discharge Flow Transmitter on the CIP pump\n"
            "discharge pipe. On the first-stage screen it\n"
            "sits in the reject line to brine drain, which\n"
            "is the position of FIT-09-004, the RO Train\n"
            "Reject Flow Transmitter; FIT-09-004 appears on\n"
            "no screen.\n"
            "Correct: tag the reject flow FIT-09-004."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
