"""
agregar_comentarios_pid.py
Anota PDF Piping & Instrumentation Diagram Rev D (E41 / submittal 25007-0041, 13 pag).

NOTA (re-disposicion 18-May-2026): P&ID Rev D = Code 1 - Approved (plano
aceptado as-is; TM N13 NOTE-01 cerrado). Code 1 NO lleva CC_ADASA (regla
CLAUDE.md section 3.8). Este script y su _CC_ADASA.pdf NO se emiten; traza
interna. Los entregables residuales (CIT-09-004 en Instrument List/Line List +
nota de respuesta del lazo; consistencia dual-value) se trackean en la
Seccion 3 del transmittal.

Checklist (CLAUDE.md section 3.8):
  1. Tabla NOTE del transmittal Section 2.5: NOTE-01 = 1
  2. PDFs en submittal 25007-0041: 1
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 1
  5. IDs coinciden: Section 2.5 del transmittal TM N18 (re-escopeado)

Veredicto: 2 - Approved as Noted (cierra TM N13 NOTE-01 vía CCS; NOTE-01 sobre
cambio BW-initiated de tapping de CIT-09-004). CCS en pagina 13 del PDF.
page_fallback 0-based (memoria feedback_doc_annotator_page_fallback_0based).
Texto sin etiqueta de criticidad; fill transmite severidad.
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-009-002_D_PID.pdf")
PDF_OUT = os.path.join(
    SCRIPT_DIR, "P22-DWG-09-009-002_D_PID_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 41",
        "P22-DWG-09-009-002_D - Piping & Instrumentation Diagram.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-01",
        "fill": MENOR,
        "search": "instrumentation tapping of CIT-09-004",
        "page_fallback": 12,  # 0-based -> pagina 13 (Consolidated Comment Sheet)
        "text": (
            "NOTE-01: CIT-09-004 instrumentation tapping\n"
            "change. A BW-initiated change adds an\n"
            "orifice plate + needle valve upstream of\n"
            "the interstage conductivity analyzer\n"
            "CIT-09-004 to reduce line pressure and\n"
            "protect the sensor. Protection intent is\n"
            "sound but the change was not requested by\n"
            "ADASA and affects an instrument feeding the\n"
            "interstage salt-rejection indicator\n"
            "(OBS-03). TM N13 NOTE-01 (CIP Tank 6.81 vs\n"
            "6.1 m3) CLOSED at P&ID level: total 6.8 /\n"
            "effective 6.1, both annotated.\n"
            "\n"
            "Action to issue at IFC Rev 0 -- no new\n"
            "P&ID revision required; the drawing is\n"
            "accepted as-is:\n"
            "1) Keep the dual-value annotation (CIP\n"
            "   Tank 6.8 total / 6.1 effective;\n"
            "   Antiscalant Tank 0.34 / 0.27 m3);\n"
            "   confirm at Rev 0 it matches the CIP\n"
            "   Tank datasheet and the Equipment List.\n"
            "2) Issue Instrument List Rev D + Line\n"
            "   List Rev C reflecting the orifice /\n"
            "   needle valve on the CIT-09-004 tapping.\n"
            "3) Submit a short engineering note that\n"
            "   the pressure-reduction does not lag or\n"
            "   dead-leg the interstage salt-rejection\n"
            "   indicator.\n"
            "ADASA accepts the P&ID at IFC Rev 0 once\n"
            "items 1-3 are reviewed; the P&ID drawing\n"
            "itself requires no change."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
