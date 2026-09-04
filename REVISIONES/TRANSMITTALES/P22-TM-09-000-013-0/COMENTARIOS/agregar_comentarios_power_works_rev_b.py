#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anotaciones PDF — P22-DWG-09-007-005 Rev B
Typical Installation Details of Power Works

Transmittal N13 / Submittal 25007-0025
Fecha: 06-Apr-2026

Observaciones (3):
  NOTE-01 (MINOR):  Grounding conductor sizing basis not cited — pagina 9 (index 8)
  NOTE-02 (INFO):   Cable Tray Layout drawings not submitted — pagina 1 / cover (index 0)
  NOTE-03 (INFO):   ADASA duct bank interface data required — pagina 5 / PLC-LCP (index 4)
"""

import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
skill_path = os.path.normpath(
    os.path.join(SCRIPT_DIR, "..", "..", "..", "..", ".claude", "skills", "doc-annotator")
)
sys.path.insert(0, skill_path)
from doc_annotator import NOTE, MENOR, run_comentarios

# --- Rutas ---
PDF_LOCAL = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-005_B_PowerWorks.pdf"
)
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-007-005_B_CC_ADASA.pdf"
)

# Copiar PDF fuente si no existe localmente
if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(
        os.path.join(
            SCRIPT_DIR,
            "..", "..", "..", "..",
            "ENTREGAS_BWWATER",
            "ENTREGA 25",
            "P22-DWG-09-007-005_B Typical Installation Details of Power Works.pdf",
        )
    )
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print(f"PDF fuente copiado: {PDF_LOCAL}")
    else:
        print(f"ERROR: PDF fuente no encontrado en: {src}")
        sys.exit(1)

# ---------------------------------------------------------------------------
# Checklist pre-creacion (sec 3.10 CLAUDE.md):
# 1. OBS/NOTEs de seccion 2.2 del transmittal:
#    NOTE-01: sizing basis (pagina 9, index 8)
#    NOTE-02: Cable Tray Layout pending (pagina 1, index 0)
#    NOTE-03: duct bank interface (pagina 5, index 4 — PLC/LCP panel page)
# 2. len(COMENTARIOS) == 3 == total obs+notes de la seccion 2.2
# ---------------------------------------------------------------------------

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": None,
        "page_fallback": 8,  # Pagina 9 (0-based) — Grounding Link page
        "text": (
            "NOTE-01 (MINOR): Grounding conductor sizing basis not cited.\n"
            "Rev B specifies 16 mm\u00b2 (main bonding) and 4 mm\u00b2 (instrument "
            "grounds) but does not cite the NEC table or calculation basis "
            "(e.g. NEC 250.122). BW Water to confirm sizing basis in IFC (Rev 0) "
            "or supporting design calculation.\n"
            "Ref: TM N13 \u00a7 2.2 NOTE-01 | ADASA P22-TM-09-000-013-0"
        ),
    },
    {
        "id": "NOTE-02",
        "fill": NOTE,
        "search": None,
        "page_fallback": 0,  # Cover/title page
        "text": (
            "NOTE-02 (INFORMATIONAL): Cable Tray Layout drawings not submitted.\n"
            "This document provides typical installation details. The complete internal "
            "cable routing from LCP/MCC to each load (BH-09-001, BH-09-002, dosing pump, "
            "CIP heater, instrumentation) must be resolved in the Cable Tray Layout "
            "drawing(s) \u2014 a distinct deliverable not yet received. Required prior to "
            "IFC (Rev 0).\n"
            "Basis: ET \u2014 Scope of Supply (ET \u00a7 5.6)\n"
            "Ref: TM N13 \u00a7 2.2 NOTE-02 | ADASA P22-TM-09-000-013-0"
        ),
    },
    {
        "id": "NOTE-03",
        "fill": NOTE,
        "search": None,
        "page_fallback": 4,  # Pagina 5 (0-based) — PLC/LCP Panel installation detail
        "text": (
            "NOTE-03 (INFORMATIONAL): ADASA incoming connection via duct bank.\n"
            "ADASA will route the incoming power supply from the electrical room to this "
            "panel via underground duct bank. BW Water must confirm:\n"
            "(a) Number and diameter of conduits required at panel entry;\n"
            "(b) Terminal block / busbar arrangement for incoming conductors;\n"
            "(c) Conductor count and cross-section per circuit (main feeder, "
            "control power, UPS input).\n"
            "Required prior to duct bank civil works commencement.\n"
            "Basis: ET \u00a7 5.6 \u2014 Electrical Supply Limit\n"
            "Ref: TM N13 \u00a7 2.2 NOTE-03 | ADASA P22-TM-09-000-013-0"
        ),
    },
]

# Verificacion len(COMENTARIOS) == 3
assert len(COMENTARIOS) == 3, f"ERROR: se esperan 3 anotaciones, hay {len(COMENTARIOS)}"

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
