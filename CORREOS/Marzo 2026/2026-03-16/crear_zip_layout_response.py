import zipfile, os

BASE = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
)

files = [
    ("01_ADASA-Response-25007-PL-0001-rev1_16Mar2026.docx",
     r"CORREOS\Marzo 2026\2026-03-16\2026-03-16_Response-Layout-Proposal.docx"),
    ("02_TM-N4_P22-TM-09-000-004-0_CableTrayLayout-Code1.docx",
     r"REVISIONES\TRANSMITTALES\P22-TM-09-000-004-0\TRANSMITTAL N4 ADASA-BW_WATER.docx"),
    ("03_TM-N5-Rev1_P22-TM-09-000-005-1_CIPConstraint-3.5m.docx",
     r"REVISIONES\TRANSMITTALES\P22-TM-09-000-005-1\TRANSMITTAL N5 Rev 1 ADASA-BW_WATER.docx"),
    ("04_Email-26Feb2026_CIPLayout-TieIn-FormalRequest.docx",
     r"CORREOS\Febrero 2026\2026-02-26\2026-02-26_Request-Tie-in-Definition-CIP-External-Layout.docx"),
    ("05_TM-N7_P22-TM-09-000-007-0_PipingLayout-Code3.docx",
     r"REVISIONES\TRANSMITTALES\P22-TM-09-000-007-0\TRANSMITTAL N7 ADASA-BW_WATER.docx"),
    ("06_BW-Water-Preliminary-Schedule.pdf",
     r"PROGRAMA y CONTRATO\pdf\Project TalTal-Preliminary Taltal Schedule.pdf"),
    ("07_BW-Water-Proposal-25007-PL-0001-rev1.pdf",
     r"MINUTAS DE REUNION\CAMBIO EN LAYOUT\25007-PL-0001_rev.1.pdf"),
    ("08_PipingLayout-P22-DWG-09-005-004-RevA.pdf",
     r"ENTREGAS_BWWATER\ENTREGA 14\P22-DWG-09-005-004_Piping Layout_Rev.A.pdf"),
    ("09_CableTrayLayout-P22-DWG-09-007-004-RevA.pdf",
     r"ENTREGAS_BWWATER\ENTREGA 11\P22-DWG-09-007-004 RevA Cable Tray Layout and Support Details.pdf"),
]

OUTPUT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "2026-03-16_Response-Layout-Proposal_Attachments.zip"
)

with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
    for zip_name, rel_path in files:
        src = os.path.join(BASE, rel_path)
        if os.path.exists(src):
            zf.write(src, zip_name)
            print(f"  OK  {zip_name}")
        else:
            print(f"  FALTA: {rel_path}")

print(f"\nZIP generado: {OUTPUT}")
