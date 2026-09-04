"""
agregar_comentarios_itp_offsite_revA.py
Anota PDF ITP Offsite Rev A (E35 / submittal 25007-0035).

Checklist (CLAUDE.md Section 3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01..03, NOTE-01..03
  2. PDFs en submittal 25007-0035: 4 (este script cubre ITP Offsite)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 6
  5. IDs coinciden con .md transmittal Section 2.7

Veredicto: 2 - Approved as Noted
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-004_A_ITP_Offsite.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-004_A_ITP_Offsite_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 35",
        "P22-BA-09-000-004_A ITP Offsite.pdf",
    ))
    if os.path.exists(src):
        shutil.copy2(src, PDF_LOCAL)
        print("PDF source copied.")
    else:
        print(f"ERROR: source PDF not found:\n  {src}")
        sys.exit(1)

COMENTARIOS = [
    {
        "id": "OBS-01",
        "fill": MAYOR,
        "search": "Pressure and Leak Test Procedure",
        "page_fallback": 2,
        "text": (
            "OBS-01: Hydrostatic test\n"
            "pressures left as placeholders.\n"
            "Item 5.1 (LP PVC) reads 'Test\n"
            "Pressure = X bar'. Item 5.2 (HP\n"
            "SDX) reads 'Test Pressure = 1.5 x\n"
            "Design Pressure = Y bar'. Assign\n"
            "numerical values before first\n"
            "hydrostatic Hold Point. For HP\n"
            "with design pressure ~83 bar\n"
            "(Stage 2 reject), test pressure\n"
            "125-150 bar; for LP, >=1.5x max\n"
            "operating pressure of section."
        ),
    },
    {
        "id": "OBS-02",
        "fill": MAYOR,
        "search": "ADASA Code : P22-BA-09-000-003",
        "page_fallback": 0,
        "text": (
            "OBS-02: Document control\n"
            "inconsistencies. Cover declares\n"
            "code P22-BA-09-000-004 with Rev A\n"
            "and date 30-Apr-2026; page 2\n"
            "internal header declares code\n"
            "P22-BA-09-000-003 (PQP code) and\n"
            "Rev 0. Footer built on inherited\n"
            "template AQ-QAM-F017 Rev.3\n"
            "Effective 23.06.2023. Cover\n"
            "signatures only as initials\n"
            "(MF, MZ, MAZ, AAR). Reconcile\n"
            "code, revision, signatures and\n"
            "template metadata on IFC issue."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "PROV-PLAN-NDE-XXX",
        "page_fallback": 1,
        "text": (
            "OBS-03: Procedure references —\n"
            "22 placeholder codes across\n"
            "PROV-PROC, PROV-PLAN, PROV-CHK,\n"
            "PROV-LIST, PROV-DWG, PROV-CALC.\n"
            "Item 3.3 cites PROV-PLAN-NDE-XXX\n"
            "with literal 'XXX'. NDE Plan that\n"
            "PIE Base Section 6 mandates\n"
            "(RT/UT/PT minimum percentages by\n"
            "joint type) is not delivered.\n"
            "Assign final codes per\n"
            "P00-IT-00-000-101 and submit each\n"
            "procedure for ADASA review before\n"
            "the first Hold Point. Closure\n"
            "contingent on PQP Rev B emission."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "Min. 10%",
        "page_fallback": 1,
        "text": (
            "NOTE-01: Item 2.3 (PMI Super\n"
            "Duplex) reads 'Min. 10% or per\n"
            "Approved Quality Plan' with\n"
            "reference to procedure\n"
            "XESSB/PMI/026-A. ASME B31.3\n"
            "Chapter X and the project SCD\n"
            "specification typically require\n"
            "100% PMI verification on welded\n"
            "Super Duplex joints for\n"
            "high-pressure service. Confirm\n"
            "final acceptance criterion in\n"
            "writing on the IFC issue."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "Welder Qualification",
        "page_fallback": 1,
        "text": (
            "NOTE-02: Personnel certification\n"
            "and NCR procedure not addressed\n"
            "as dedicated items. PIE Base\n"
            "Section 6 requires welder\n"
            "qualification ASME IX with 100%\n"
            "WPS/PQR verification and NDT\n"
            "inspector ASNT (Levels II/III\n"
            "for VT, RT, UT, PT). Item 3.1\n"
            "covers welder qualification\n"
            "implicitly only. No dedicated\n"
            "items for ASME IX welder cert,\n"
            "ASNT NDT, or QA Manager qual.\n"
            "Item 7.9 mentions only 'Closure\n"
            "of FAT NCRs'; no fabrication-wide\n"
            "NCR flow. Add dedicated items on\n"
            "IFC issue."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": MENOR,
        "search": "20.25.6501",
        "page_fallback": 1,
        "text": (
            "NOTE-03: Header lists Project\n"
            "Number 20.25.6501 (BW Water\n"
            "internal) and Document No.\n"
            "BWW-ITP-002 Rev. 0. Add\n"
            "cross-reference to ADASA\n"
            "contract C-4300 / Project P22\n"
            "so the document is traceable\n"
            "across both numbering systems."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
