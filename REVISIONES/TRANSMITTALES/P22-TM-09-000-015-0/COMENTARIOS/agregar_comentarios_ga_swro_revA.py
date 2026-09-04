"""
agregar_comentarios_ga_swro_revA.py
Anota PDF GA of SWRO System Skid Rev A (E33 / submittal 25007-0033).

Checklist (CLAUDE.md §3.10):
  1. Tabla OBS del transmittal: OBS-11 (BoM/valve schedule), OBS-12 (design pressure schedule)
  2. PDFs en submittal 25007-0033: 2
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 2
  5. IDs coinciden: OBS-11, OBS-12 (Section 2.9 del transmittal)

Veredicto: 2 - Approved as Noted (primera revision)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_A_GA_SWRO_Skid.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-DWG-09-005-008_A_GA_SWRO_Skid_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src_candidates = [
        "P22-DWG-09-005-008_A GA of SWRO System Skid​.pdf",
        "P22-DWG-09-005-008_A GA of SWRO System Skid.pdf",
    ]
    src = None
    for cand in src_candidates:
        candidate_path = os.path.normpath(os.path.join(
            SCRIPT_DIR, "..", "..", "..", "..",
            "ENTREGAS_BWWATER", "ENTREGA 33", cand,
        ))
        if os.path.exists(candidate_path):
            src = candidate_path
            break
    if src:
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print("ERROR: source PDF not found in ENTREGA 33 (checked both name variants).")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "NOTE-11",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Required as part of the GA package:\n"
            "- Number of pressure vessels per stage\n"
            "  (BOI-09-001 1st, BOI-09-002 2nd).\n"
            "- Number of membrane elements per\n"
            "  vessel (model).\n"
            "- Manifold material and pressure rating.\n"
            "- Function-vs-tag matrix for valves\n"
            "  shown on skid (VE-09-002 to 015,\n"
            "  VM-09-001 to 150, PSV-09-001).\n"
            "Reconciliation vs Valve List Rev D\n"
            "required."
        ),
    },
    {
        "id": "NOTE-12",
        "fill": MAYOR,
        "search": None,
        "page_fallback": 0,
        "text": (
            "Notes show 'SDSS' / 'SSDS' without:\n"
            "- ANSI flange class per service\n"
            "  (feed / interstage / reject /\n"
            "  permeate).\n"
            "- Pressure-temperature ratings.\n"
            "- Nominal wall thickness per line.\n"
            "Mirror Valve List Rev D ANSI 900# for\n"
            "SWRO HPP section, or reference a piping\n"
            "material spec document.\n"
            "Required for fabrication QA."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
