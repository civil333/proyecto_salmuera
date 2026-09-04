"""
agregar_comentarios_pqp_revA.py
Anota PDF Project Quality Plan Rev A (E35 / submittal 25007-0035).

Checklist (CLAUDE.md Section 3.10):
  1. Tabla OBS/NOTE del transmittal: OBS-01..04, NOTE-01..05
  2. PDFs en submittal 25007-0035: 4 (este script cubre PQP)
  3. Cross-cutting: ninguna
  4. len(COMENTARIOS) = 9
  5. IDs coinciden con .md transmittal

Veredicto: 3 - To Be Revised (elevado de Code 2 tras cross-check con PIE Base)
"""
import sys
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser("~/.claude/skills/doc-annotator"))
from doc_annotator import CRITICAL, MAYOR, MENOR, run_comentarios

PDF_LOCAL = os.path.join(SCRIPT_DIR, "P22-BA-09-000-003_A_PQP.pdf")
PDF_OUT = os.path.join(SCRIPT_DIR, "P22-BA-09-000-003_A_PQP_CC_ADASA.pdf")

if not os.path.exists(PDF_LOCAL):
    src = os.path.normpath(os.path.join(
        SCRIPT_DIR, "..", "..", "..", "..",
        "ENTREGAS_BWWATER", "ENTREGA 35",
        "P22-BA-09-000-003_A PQP.pdf",
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
        "fill": CRITICAL,
        "search": "Quality Objectives",
        "page_fallback": 4,
        "text": (
            "OBS-01: Inspection matrix per\n"
            "PIE Base Sections 5-11 absent.\n"
            "PIE Base lines 170-197 require\n"
            "unique source reference, numerical\n"
            "value, tolerance, frequency and\n"
            "approved procedure for each item.\n"
            "PIE Base Section 5 declares generic\n"
            "references 'Segun ET / Cumplir\n"
            "especificacion / Segun plano /\n"
            "Practica estandar' NO SERAN\n"
            "ACEPTABLES. Section 6.1 lists four\n"
            "generic objectives that close no\n"
            "PIE cell. Issue Rev B with the\n"
            "PIE Detallado aprobado por ADASA."
        ),
    },
    {
        "id": "OBS-02",
        "fill": CRITICAL,
        "search": "Inspection and Test Plans",
        "page_fallback": 5,
        "text": (
            "OBS-02: FAT scope absent. PIE\n"
            "Base Section 7 defines nine FAT\n"
            "items, seven of them Hold Points\n"
            "(7.1 procedure approval, 7.2\n"
            "visual, 7.3 dimensional, 7.5\n"
            "PLC/HMI, 7.7 SEC, 7.9 Approval\n"
            "Certificate). BAE - Payment\n"
            "Milestones ties 40% of contract\n"
            "value to the FAT Approval\n"
            "Certificate. PQP Rev A has no FAT\n"
            "section, no procedure reference,\n"
            "and no commitment to issue the\n"
            "Acta de Aprobacion FAT as\n"
            "deliverable. Rev B must include\n"
            "the dedicated FAT section."
        ),
    },
    {
        "id": "OBS-03",
        "fill": MAYOR,
        "search": "PROCEDURE",
        "page_fallback": 4,
        "text": (
            "OBS-03: Procedure codes absent.\n"
            "ET - Supplier Responsibilities\n"
            "(Section 7) and PIE Base Section 6\n"
            "require approved procedures for\n"
            "Welding (ASME IX WPS/PQR), NDT,\n"
            "PMI, Hydrostatic LP/HP,\n"
            "Preservation, FAT and Painting.\n"
            "Technical Offer Rev1 left these as\n"
            "'Manufacturer Standard Procedure'\n"
            "placeholders. Rev B must assign\n"
            "final codes per P00-IT-00-000-101\n"
            "and submit each procedure for\n"
            "ADASA review before the first Hold\n"
            "Point of each activity."
        ),
    },
    {
        "id": "OBS-04",
        "fill": MAYOR,
        "search": "Inspection and Test Plans",
        "page_fallback": 5,
        "page_min": 5,
        "text": (
            "OBS-04: Hold and Witness Points\n"
            "not defined. PIE Base Section 4\n"
            "sets H/W/S/R intervention scheme\n"
            "with mandatory prior notification\n"
            "for Hold Points. PIE Base matrix\n"
            "lists 12+ Hold Points\n"
            "(high-pressure hydrostatic, FAT\n"
            "items 7.1/7.2/7.3/7.5/7.7/7.9,\n"
            "dossier final, release for\n"
            "shipment). PQP defines no\n"
            "notification scheme, no H/W tags\n"
            "and no scheduled dates. Rev B must\n"
            "adopt the H/W/S/R taxonomy on the\n"
            "matrix."
        ),
    },
    {
        "id": "NOTE-01",
        "fill": MAYOR,
        "search": "Revision No.: A",
        "page_fallback": 0,
        "text": (
            "NOTE-01: Document control\n"
            "inconsistencies. Cover declares\n"
            "Rev A and code P22-BA-09-000-003.\n"
            "Page 2 internal header declares\n"
            "Rev. No. 0 and code QAM-PQP-001\n"
            "(BW Water corporate form) with\n"
            "inherited template dates Issue\n"
            "16-JUN-2025 / Effective\n"
            "17-JUL-2025. Cover signatures only\n"
            "as initials (MF, MZ, MAZ, AAR).\n"
            "Reconcile revision label, code,\n"
            "signatures and dates on Rev B."
        ),
    },
    {
        "id": "NOTE-02",
        "fill": MAYOR,
        "search": "Inspection and test plan for OFFSITE",
        "page_fallback": 5,
        "text": (
            "NOTE-02: Attachment Section 7.1\n"
            "lists single BWW-ITP-002 Offsite;\n"
            "row 2 of the table is truncated.\n"
            "Onsite, FAT and Commissioning ITPs\n"
            "missing. PIE Base Sections 9 (site\n"
            "reception), 10 (installation) and\n"
            "11 (performance tests) require\n"
            "dedicated ITPs absent from this\n"
            "document. Rev B must add the\n"
            "missing ITPs under codes per\n"
            "P00-IT-00-000-101."
        ),
    },
    {
        "id": "NOTE-03",
        "fill": MAYOR,
        "search": "REFERENT",
        "page_fallback": 3,
        "text": (
            "NOTE-03: PMI commitment absent.\n"
            "PIE Base Section 6 requires\n"
            "minimum 10% PMI on Super Duplex\n"
            "UNS S32750 by XRF; ET - Material\n"
            "Verification specifies the\n"
            "spectrometric method. Technical\n"
            "Offer Rev1 line 3948 only commits\n"
            "MTR per EN 10204. The PQP must\n"
            "declare PMI procedure code,\n"
            "sampling percentage and matrix\n"
            "position. ADASA may require 100%\n"
            "PMI on critical high-pressure\n"
            "welds via the approved PQP."
        ),
    },
    {
        "id": "NOTE-04",
        "fill": MAYOR,
        "search": "Project Manager",
        "page_fallback": 3,
        "text": (
            "NOTE-04: Personnel certification\n"
            "not addressed. PIE Base Section 6\n"
            "(Welding) requires welder\n"
            "qualification per ASME IX with\n"
            "100% verification of WPS/PQR. NDT\n"
            "inspectors require ASNT level for\n"
            "VT, UT, RT and PT. PQP Section 5\n"
            "lists managerial roles only. Rev B\n"
            "must add a personnel qualification\n"
            "section listing welder ASME IX\n"
            "certification, NDT inspector ASNT\n"
            "level and QA Manager qualification."
        ),
    },
    {
        "id": "NOTE-05",
        "fill": MENOR,
        "search": "ISO 9001",
        "page_fallback": 3,
        "text": (
            "NOTE-05: Organisation and ISO\n"
            "9001. Section 5 narrative without\n"
            "organisation chart or RACI matrix.\n"
            "Section 6.4 declares NCR control\n"
            "in a single sentence without flow,\n"
            "format or escalation timeline.\n"
            "ISO 9001:2015 cited in Section 4.0\n"
            "without certificate of compliance\n"
            "attached and without scope\n"
            "coverage of the manufacturing site.\n"
            "Rev B should attach the\n"
            "certificate, declare its scope and\n"
            "add an organisation chart with\n"
            "NCR escalation path."
        ),
    },
]

if __name__ == "__main__":
    run_comentarios(PDF_LOCAL, PDF_OUT, COMENTARIOS)
