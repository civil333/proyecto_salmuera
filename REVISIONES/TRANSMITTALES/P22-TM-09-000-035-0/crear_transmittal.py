#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_transmittal.py — Transmittal N35 (P22-TM-09-000-035-0)

Submittal 25007-0081 (ENTREGA 81), recibido el jueves 20-Ago-2026. Cinco
documentos del paquete de calidad y fabricacion, todos re-emisiones que responden
al Transmittal N32.

VEREDICTO GLOBAL: 3 - To be revised. Recuento: 2 Codigo 1, 3 Codigo 3.

Mapa de subsecciones:
    2.1  HP and LP Pressure Test Procedure Rev 1   P22-BA-09-000-010  Codigo 1
    2.2  Painting Procedure Rev 1                  P22-BA-09-000-011  Codigo 1
    2.3  Liquid Penetrant Examination Proc. Rev B  P22-BA-09-000-014  Codigo 3
    2.4  Radiography Examination Procedure Rev B   P22-BA-09-000-015  Codigo 3
    2.5  Ultrasonic Thickness Procedure Rev B      P22-BA-09-000-016  Codigo 3

REGLA DE ALCANCE, fijada por el usuario antes de la revision. Los documentos que
llegan por sobre la Rev 0 ya estan emitidos para construccion: la revision
verifica si los comentarios previos cerraron y no introduce observaciones nuevas.
El mismo alcance se extendio a los tres procedimientos en Rev B. El universo de
los cinco es el Transmittal N32 y nada mas.

DECISION DE CODIGO DEL USUARIO. El `-010` quedo en Codigo 1 contra una propuesta
inicial de Codigo 3: el formulario del ensayo se incorporo, que era la parte
urgente, y lo que falta vive en OTRO formulario (el Pressure Test Record Chart,
sin numero ni revision), de modo que no es defecto intrinseco del documento
revisado y se sigue en la Seccion 3. Sobre un documento emitido para construccion
el Codigo 2 no tiene mecanismo: es 1 o es 3.

LO QUE SE RECONOCE POR ESCRITO, y no es cortesia:
  - `-014`: los umbrales del B31.3 agregado coinciden digito a digito con los del
    Apendice 6. El riesgo de un resultado distinto es nulo; lo que sostiene el
    codigo es el codigo que citara el registro del dossier.
  - `-015`: la Tabla 341.3.2-1 si se incorporo completa. Verificada por render a
    200 dpi, porque entra como imagen y no aparece en la extraccion de texto.
  - `-016`: es el que mas trabajo de los tres y cerro una de sus dos bloqueantes.
Decirlo hace mas dificil de discutir el Codigo 3, no mas facil.

FUERA DEL TRANSMITTAL, a proposito: el ensayo hidrostatico del 20-Ago y el TAG de
la linea del Spool 1 van por la cadena de inspecciones, en su propio correo del
mismo dia. Aca solo se cita el ensayo como evidencia de que el formulario del
`-010` ya esta en uso.

SIN numeros manuales en add_heading() (el template ADASA auto-numera H1/H2).
Referencias del cuerpo por NOMBRE de seccion, no por numero. Cero simbolo de
seccion.
"""
import os
import sys

sys.path.insert(0, os.path.expanduser("~/.claude/skills/template-adasa"))

from ejemplo_documento import (  # noqa: E402
    crear_documento_adasa,
    aplicar_arial_12,
    add_simple_table,
    add_bullet as _add_bullet_native,
)
from docx import Document  # noqa: E402
from docx.oxml import OxmlElement  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402
from docx.opc.constants import RELATIONSHIP_TYPE as RT  # noqa: E402


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N35 ADASA-BW_WATER.docx")

# Enlace de descarga de la carpeta del N35, publicado el 20-Ago-2026.
# El modo de falla del N30, N31 y N32 fue verificar el enlace sobre el script y
# no sobre el texto extraido del Word. Verificar SIEMPRE sobre el .docx emitido.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19YAtLM7VpZHgw8EqV1StbIjc46CGmqy/"
    "FRH14L__RLZ3Y-BIAYpwIZHqO5Q90IUV-Z7KA1hokcQ0"
)


def add_hyperlink(paragraph, url, text):
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    rfonts.set(qn("w:ascii"), "Arial")
    rfonts.set(qn("w:hAnsi"), "Arial")
    rpr.append(rfonts)
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "24")
    rpr.append(sz)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    run.append(t)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)
    return hyperlink


def add_para(doc, runs):
    para = doc.add_paragraph()
    for item in runs:
        text = item[0]
        attrs = item[1] if len(item) > 1 else {}
        run = para.add_run(text)
        if attrs.get("bold"):
            run.bold = True
        if attrs.get("italic"):
            run.italic = True
    aplicar_arial_12(para)
    return para


def add_bullet(doc, text):
    _add_bullet_native(doc, text, size=11, space_after_pt=12)


# --- Seccion 1 -------------------------------------------------------------
VERDICT = (
    "Five documents from submittal 25007-0081, received on 20 August, all of them "
    "re-issues answering Transmittal N32. Tally: 2 Code 1, 3 Code 3."
)

SCOPE = (
    "Each document was reviewed against the points Transmittal N32 set for it, and "
    "against nothing else."
)

DISPOSITION = [
    "HP and LP Pressure Test Procedure Rev 1 — Code 1. No action on this document.",
    "Painting Procedure Rev 1 — Code 1. No action.",
    "Liquid Penetrant Examination Procedure Rev B — Code 3. State one acceptance "
    "criterion, in the clause and on the report form.",
    "Radiography Examination Procedure Rev B — Code 3. State the geometric "
    "unsharpness limit that applies to the wall radiographed here.",
    "Ultrasonic Thickness Procedure Rev B — Code 3. State the acceptance criterion "
    "of the approved NDE Plan in clause 9.0.",
]

WHY_CODE3_LEAD = (
    "The three are re-issued without a consolidated comment sheet, so ADASA verified "
    "the closure by comparing the text of Rev A against Rev B. Against that "
    "comparison:"
)

WHY_CODE3_ITEMS = [
    "The liquid penetrant procedure added ASME B31.3 to clause 13.0 but kept "
    "Appendix 6 of the pressure vessel code beside it, and the report form is "
    "unchanged and still declares Appendix 8. Eleven lines changed in the whole "
    "document.",
    "The radiography procedure attached Table 341.3.2-1 of ASME B31.3 in full, which "
    "is a real closure. Clause 23.0 still lists five codes without stating which "
    "governs, and clause 12.1 is unchanged. It admits 1.8 mm of geometric unsharpness, "
    "three and a half times what T-274 of ASME Section V, Article 2 allows for the "
    "6.02 to 8.56 mm wall radiographed on this module.",
    "The ultrasonic procedure closed its technique sheet, which now reads for "
    "UNS S32750 throughout, and this is the document that changed most. Clause 9.0, "
    "however, moved from the client's discretion to SA-790, which is the material "
    "specification of the pipe and not a thickness criterion. The NDE Plan Rev C, "
    "approved at Code 1, requires the measured thickness to be equal to or greater "
    "than the minimum required thickness of the design code and the engineering "
    "calculation.",
]

ABOVE_REV0 = (
    "The pressure test procedure now carries form AQ-QAM-F018 Rev 4, and the painting "
    "inspection form reads RAL 5012 Luminous Blue in the Colour row. What remains open "
    "on the pressure test record is a separate form and is tracked in Pending "
    "Observations from Previous Transmittals."
)

TEST_PRESSURE_RULE = (
    "The 135 bar of row 5.2 of the Inspection and Test Plan is 1.5 times the highest "
    "design pressure of the circuit, 90 barG, and not a single value for every super "
    "duplex line. Each line is tested at 1.5 times its own design pressure per the "
    "approved Line List: 75, 90, 120 or 135 barG. The HP and LP Pressure Test Procedure "
    "section of this transmittal states it line by line, and that table is binding for "
    "the tests that remain. No test of the super duplex circuit is to be run until BW "
    "Water confirms in writing the pressure it will apply to each line."
)

RETURN_DATE = (
    "The Submittal Form requests a response by Sunday 23 August. ADASA's review period "
    "under Clause 37.2 of the BAE is seven working days from receipt, which falls on "
    "Monday 31 August. This is the third consecutive submittal whose requested return "
    "date sits below the contractual period, and ADASA asks that future forms state a "
    "date consistent with it."
)

# --- Seccion 2 -------------------------------------------------------------
S21_STATUS = (
    "Reviewed against the single point Transmittal N32 raised on the Rev 0, and "
    "against nothing else. That point is closed on this document: form AQ-QAM-F018, "
    "Pressure and Leak Test Report, Rev 4 is now attached as page 11 of the procedure, "
    "blank and identified. It restores the form that had been present in Rev C and "
    "absent since Rev D. The inspection of 20 August confirms it in practice, since "
    "both test records of that day were raised on this form."
)

S21_CERTIFICATE = (
    "Rows 5.1 and 5.2 of the Inspection and Test Plan (P22-BA-09-000-004) Rev 0 "
    "require a pressure against time graphic as the certificate, and row 5.2 is a hold "
    "point. Form AQ-QAM-F018 records point values, not a curve. The graphic is in fact "
    "produced: the records of 20 August include a Pressure Test Record Chart with the "
    "pressure steps, the start and finish time of each and the signatures of both "
    "parties. That chart carries no document number and no revision, and this "
    "procedure neither identifies nor incorporates it."
)

S21_RULE_LEAD = "ADASA states the test pressure rule, which this procedure leaves open."

S21_RULE = (
    " Clause 5.5.12 says in one sentence that HP piping will test to 135 bar and LP to "
    "7.5 bar, and that the testing pressure will refer to the approved Line List. Those "
    "are two different instructions: a pair of fixed values, and a table that prescribes "
    "six. The factor itself is written nowhere in the procedure. ADASA states which "
    "governs. The 135 bar of row 5.2 of the Inspection and Test Plan is the factor "
    "applied to the highest design pressure of the circuit, 1.5 x 90 barG, as row 5.2 of "
    "the Inspection and Testing Base Plan (P22-IT-09-000-001-0) sets it and ASME B31.3 "
    "para. 345.4.2 requires. It is therefore not a single value for every super duplex "
    "line. Each line is tested at 1.5 times the design pressure that the Line List "
    "(P22-LI-09-009-003) Rev 0, approved at Code 1 in Transmittal N29, assigns to it, and "
    "that ratio holds exactly across its 34 rows. The table below states it line by line "
    "and is binding for the tests that remain."
)

S21_RISK_LEAD = "Reading 135 bar as a single value would over-pressurise seven of the eleven lines."

S21_RISK = (
    " Four super duplex lines are designed for 90 barG and test at 135. The remaining "
    "seven are designed for 50, 60 or 80 barG and test at 75, 90 or 120. Testing the two "
    "turbocharger brine outlets, designed for 50 barG, at 135 bar would be 2.7 times "
    "their design pressure, and the high-pressure pump discharge 2.25 times its own. That "
    "is the failure mode Transmittal N27 raised as a critical finding when a 75 bar test "
    "was ordered on a 5 barG PVC line, and it now sits inside the super duplex circuit, "
    "upstream and downstream of the two Fedco HPB-60 units SIP-09-001 and SIP-09-002."
)

S21_ACTION_LEAD = "Action: none on this document — accepted; issue directly at IFC Rev 0."

S21_ACTION = (
    " Two binding conditions apply to the tests that remain. First, the pressure of each "
    "line is the one stated in the table above, 1.5 times its design pressure per the "
    "approved Line List. No test of the super duplex circuit is to be run until BW Water "
    "confirms in writing the pressure it will apply to each line against that table, and "
    "row 5.2 is a hold point, so ADASA controls its execution. Second, each test "
    "record is to state the design pressure of the line alongside the test pressure, "
    "since form AQ-QAM-F018 has no such column and a certificate reading 90 bar cannot "
    "otherwise be traced to the row that governs it. Related deliverable tracked in "
    "Pending Observations from Previous Transmittals: issue the Pressure Test Record "
    "Chart as a controlled form, with a document number and revision, and incorporate it "
    "into this procedure."
)

# Tabla por TAG, espejo exacto de la del correo del 20-Ago. Las once lineas de super
# duplex de la Line List Rev 0, aprobada en Codigo 1 en el TM N29. Relacion 1,5 exacta.
PRESSURE_TABLE = [
    ("DA-SSD-DN100-09-003", "RO HP Feed Pump Discharge", "60", "90"),
    ("DA-SSD-DN100-09-004", "1st Stage RO Feed", "80", "120"),
    ("DA-SSD-DN80-09-005", "1st Stage RO Reject", "80", "120"),
    ("DA-SSD-DN80-09-006", "2nd Stage RO Feed", "90", "135"),
    ("DA-SSD-DN65-09-007", "2nd Stage RO Reject", "90", "135"),
    ("DA-SSD-DN65-09-008", "Interstage Turbocharger Brine Outlet", "50", "75"),
    ("DA-SSD-DN65-09-009", "Feed Turbocharger Brine Outlet", "50", "75"),
    ("CP-SSD-DN100-09-014", "CIP Feed to 1st Stage RO", "80", "120"),
    ("CP-SSD-DN80-09-015", "CIP Feed to 2nd Stage RO", "90", "135"),
    ("CP-SSD-DN80-09-044", "1st Stage CIP Reject Out", "80", "120"),
    ("CP-SSD-DN65-09-045", "2nd Stage CIP Reject Out", "90", "135"),
]

PRESSURE_TABLE_NOTE = (
    "The twenty-three plastic lines test at 3 or 7.5 barG and none above 7.5. Of the "
    "eleven super duplex lines, only four test at 135 barG."
)

S22_STATUS = (
    "Reviewed against the condition Transmittal N32 set on the Rev 0, and against "
    "nothing else. The Colour row of the inspection form now reads RAL 5012 Luminous "
    "Blue for the third coat, consistent with page 9 of the procedure and with the "
    "Painting Specification (P22-ET-09-006-002) Rev C approved at Code 1. The anchor "
    "profile remains at 50 to 80 micrometres in both rows of the form and the product "
    "of each coat is stated. On the nominal thickness per coat, Transmittal N32 "
    "recorded that this is not a condition, and ADASA does not reopen it."
)

S22_ACTION = "Action: none — accepted; issue directly at IFC Rev 0."

S23_STATUS = (
    "Reviewed against the five points of Transmittal N32. The acceptance criterion of "
    "ASME B31.3 was added to clause 13.0, but Appendix 6 of ASME Section VIII Div. 1 "
    "was left in place beside it, so the clause now offers two criteria and states "
    "neither as governing. The report form is unchanged and still declares Appendix 8 "
    "of the same pressure vessel code. None of the three tidying items was attended. "
    "Itemised in P22-BA-09-000-014_B_Liquid_Penetrant_Procedure_CC_ADASA.pdf."
)

S23_EFFECT_LEAD = "On the practical effect, ADASA is explicit:"

S23_EFFECT = (
    " the thresholds of the added B31.3 text match those of Appendix 6 digit for "
    "digit, so no examination result turns on the choice. What turns on it is the code "
    "the record cites when it enters the fabrication dossier, and the Technical "
    "Specification (P22-ET-09-000-001-0), Section 8 - Inspections During Manufacturing, "
    "together with the NDE Plan Rev C, makes that ASME B31.3."
)

S23_ACTION_LEAD = "Action — re-issue as Rev C:"

S23_ACTION = (
    " state ASME B31.3 para. 341.3.2 and Table 341.3.2 as the single acceptance "
    "criterion in clause 13.0 and on the report form, deleting the references to "
    "Appendix 6 and Appendix 8. Close at the same issue the report form data of "
    "another contract, the revision index of the attached procedure and the purpose "
    "clause of the cover section (OBS-01, OBS-02 and NOTE-01 on the annotated PDF)."
)

S24_STATUS = (
    "Reviewed against the five points of Transmittal N32. Table 341.3.2-1 of ASME "
    "B31.3 2024 is now attached in full at the end of the procedure, which is what was "
    "asked for and is acknowledged as such. Clause 23.0 nonetheless keeps the list of "
    "five codes and the formula that the criteria shall be in accordance with the "
    "specific contract specification, so the interpreter still chooses. Clause 12.1 is "
    "unchanged. Itemised in P22-BA-09-000-015_B_Radiography_Procedure_CC_ADASA.pdf."
)

S24_CLAUSE_LEAD = "Clause 12.1 is what governs this code."

S24_CLAUSE = (
    " The 1.8 mm it states is the dispensation of paragraph PW-51.1 of ASME Section I "
    "for items carrying the PP stamp, that is power piping to ASME B31.1. This module "
    "is process piping to ASME B31.3, whose paragraph 344.5.1 refers radiography "
    "wholly to Section V, Article 2. For the DN65, DN80 and DN100 lines of ASTM A790 "
    "UNS S32750 that carry 10 per cent radiography on the approved Line List, 6.02 to "
    "8.56 mm of wall, T-274 requires 0.020 in."
)

S24_ACTION_LEAD = "Action — re-issue as Rev C:"

S24_ACTION = (
    " state ASME B31.3 para. 341.3.2 and Table 341.3.2 as the acceptance criteria of "
    "clause 23.0, in place of the list of five codes, and replace the 1.8 mm of clause "
    "12.1 with the T-274 limit applicable to this wall. Close at the same issue the "
    "scope, the numbering and the purpose clause of the cover section (OBS-01, OBS-02 "
    "and NOTE-01 on the annotated PDF)."
)

S25_STATUS = (
    "Reviewed against the six points of Transmittal N32. This is the document that "
    "changed most of the three, with nine changes of content, and one of its two "
    "blocking items is closed: the scope, the calibration block of clause 4.1 and "
    "Appendix 1 all declare UNS S32750, where Rev A was written for carbon steel. "
    "Itemised in P22-BA-09-000-016_B_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf."
)

S25_CRITERION_LEAD = "The acceptance criterion is what governs this code."

S25_CRITERION = (
    " Clause 9.0 moved from acceptance at the discretion of the client to acceptance "
    "per ASME Section II, SA-790, which is the material specification of the pipe: "
    "chemistry, mechanical properties and supply tolerances. It does not state when a "
    "thickness reading is acceptable. The NDE Plan (P22-BA-09-000-005) Rev C, approved "
    "at Code 1, does: the measured thickness shall be equal to or greater than the "
    "minimum required thickness of the applicable design code and the engineering "
    "calculation. That comparison is what a fabrication baseline measurement resolves, "
    "and it is absent."
)

S25_ACTION_LEAD = "Action — re-issue as Rev C:"

S25_ACTION = (
    " state the NDE Plan acceptance criterion in clause 9.0, and write the material as "
    "UNS S32750 throughout, with the sound velocity used and the second grade of the "
    "calibration block corrected. Close at the same issue the couplant of the report "
    "form, the reference list and the purpose clause of the cover section (OBS-01, "
    "NOTE-01 and NOTE-02 on the annotated PDF)."
)

# --- Seccion 3 -------------------------------------------------------------
PENDING = [
    ("N25, N29, N30", "Fabrication and testing dossier",
     "Item 65 remains NOT DELIVERED. The index has reached Rev B; no record has "
     "followed it. It sustains items 8.3 and 8.4 of the Inspection and Testing Base "
     "Plan, on which 40 per cent of payment depends", "Open, overdue"),
    ("N26, N30", "Endorsed structural calculation report",
     "The report governs the anchorage figures of two general arrangement drawings "
     "and the foundations already built at site", "Open, overdue"),
    ("N28, N34", "Instrument List (P22-LI-09-008-003) Rev E",
     "Re-issue with VT-09-001 ranged at the binding 0 to 12 mm/s rms, so that the "
     "high-pressure pump vibration trip of 10 mm/s can act. Rev E still reads 0 to "
     "8.9 mm/s rms", "Open"),
    ("N32, N35", "Pressure Test Record Chart",
     "Issue as a controlled form, with a document number and revision, and incorporate "
     "it into the HP and LP Pressure Test Procedure. It is the form that produces the "
     "pressure against time certificate required by rows 5.1 and 5.2 of the Inspection "
     "and Test Plan, and it currently carries no identification", "Open, raised here"),
    ("N27, N35", "Test pressure of the super duplex circuit",
     "Confirm in writing the pressure to be applied to each line against the table in "
     "the HP and LP Pressure Test Procedure section of this transmittal, 1.5 times the "
     "design pressure of the approved Line List. No test of the super duplex circuit is "
     "to be run until that confirmation is received. Each record is to state the design "
     "pressure of the line alongside the test pressure", "Open, raised here"),
]

ALSO_OPEN = (
    "the liquid penetrant records of 7 August, examined five days before their "
    "procedure was submitted, and the measurement point drawing required by row 7.8 of "
    "the Inspection and Test Plan alongside the ultrasonic procedure. Also the six tag "
    "reconciliation of the HMI Display Screenshot Rev B, and the design pressure at "
    "the brine feed tie-in point."
)

# --- Seccion 4 -------------------------------------------------------------
ATTACHMENTS = [
    ("Liquid Penetrant Examination Procedure Rev B", "3",
     "P22-BA-09-000-014_B_Liquid_Penetrant_Procedure_CC_ADASA.pdf"),
    ("Radiography Examination Procedure Rev B", "3",
     "P22-BA-09-000-015_B_Radiography_Procedure_CC_ADASA.pdf"),
    ("Ultrasonic Thickness Procedure Rev B", "3",
     "P22-BA-09-000-016_B_Ultrasonic_Thickness_Procedure_CC_ADASA.pdf"),
]

ATTACH_NOTE = (
    "All documents with open observations carry annotated PDFs, the three Code 3. The "
    "two Code 1 documents, the HP and LP Pressure Test Procedure and the Painting "
    "Procedure, carry none."
)

# --- Seccion 5 -------------------------------------------------------------
RESPONSE_SUMMARY = [
    ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "1", "25007-0081",
     "1 — Approved"),
    ("P22-BA-09-000-011", "Painting Procedure", "1", "25007-0081", "1 — Approved"),
    ("P22-BA-09-000-014", "Liquid Penetrant Examination Procedure", "B", "25007-0081",
     "3 — To be revised"),
    ("P22-BA-09-000-015", "Radiography Examination Procedure", "B", "25007-0081",
     "3 — To be revised"),
    ("P22-BA-09-000-016", "Ultrasonic Thickness Procedure", "B", "25007-0081",
     "3 — To be revised"),
]

CLOSING = (
    " The three non-destructive testing procedures fix the code: none states the "
    "acceptance criterion that the Technical Specification, Section 8 - Inspections "
    "During Manufacturing, and the NDE Plan Rev C make applicable to this scope. "
    "Records produced under a procedure that is not approved are not admissible into "
    "the fabrication dossier."
)


if __name__ == "__main__":
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N35 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-035-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To be revised.", {"bold": True}),
        (" " + VERDICT,),
    ])
    add_para(doc, [("Scope of this review.", {"bold": True}), (" " + SCOPE,)])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for item in DISPOSITION:
        add_bullet(doc, item)
    add_para(doc, [
        ("Why Code 3 — the three non-destructive testing procedures.", {"bold": True}),
        (" " + WHY_CODE3_LEAD,),
    ])
    for item in WHY_CODE3_ITEMS:
        add_bullet(doc, item)
    add_para(doc, [
        ("Both procedures issued above Rev 0 are Code 1.", {"bold": True}),
        (" " + ABOVE_REV0,),
    ])
    add_para(doc, [
        ("Test pressure of the super duplex circuit.", {"bold": True}),
        (" " + TEST_PRESSURE_RULE,),
    ])
    add_para(doc, [("Return date.", {"bold": True}), (" " + RETURN_DATE,)])
    add_para(doc, [
        ("Pending Observations from Previous Transmittals lists the items open from "
         "earlier transmittals.",),
    ])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    doc.add_heading(
        "HP and LP Pressure Test Procedure Rev 1 — P22-BA-09-000-010", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S21_STATUS,)])
    add_para(doc, [
        ("One element of the certificate lives outside this document.", {"bold": True}),
        (" " + S21_CERTIFICATE,),
    ])
    add_para(doc, [(S21_RULE_LEAD, {"bold": True}), (S21_RULE,)])
    add_simple_table(
        doc,
        [("Line", "Description", "Design barG", "Test barG")] + PRESSURE_TABLE)
    add_para(doc, [(PRESSURE_TABLE_NOTE,)])
    add_para(doc, [(S21_RISK_LEAD, {"bold": True}), (S21_RISK,)])
    add_para(doc, [(S21_ACTION_LEAD, {"bold": True}), (S21_ACTION,)])

    doc.add_heading("Painting Procedure Rev 1 — P22-BA-09-000-011", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S22_STATUS,)])
    add_para(doc, [(S22_ACTION, {"bold": True})])

    doc.add_heading(
        "Liquid Penetrant Examination Procedure Rev B — P22-BA-09-000-014", level=2)
    add_para(doc, [("Response Code: 3 — To be revised", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S23_STATUS,)])
    add_para(doc, [(S23_EFFECT_LEAD, {"bold": True}), (S23_EFFECT,)])
    add_para(doc, [(S23_ACTION_LEAD, {"bold": True}), (S23_ACTION,)])

    doc.add_heading(
        "Radiography Examination Procedure Rev B — P22-BA-09-000-015", level=2)
    add_para(doc, [("Response Code: 3 — To be revised", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S24_STATUS,)])
    add_para(doc, [(S24_CLAUSE_LEAD, {"bold": True}), (S24_CLAUSE,)])
    add_para(doc, [(S24_ACTION_LEAD, {"bold": True}), (S24_ACTION,)])

    doc.add_heading(
        "Ultrasonic Thickness Procedure Rev B — P22-BA-09-000-016", level=2)
    add_para(doc, [("Response Code: 3 — To be revised", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S25_STATUS,)])
    add_para(doc, [(S25_CRITERION_LEAD, {"bold": True}), (S25_CRITERION,)])
    add_para(doc, [(S25_ACTION_LEAD, {"bold": True}), (S25_ACTION,)])

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading("PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_simple_table(
        doc,
        [("Origin TM", "Document", "Observation", "Status")] + PENDING)
    add_para(doc, [("Also open: ", {"bold": True}), (ALSO_OPEN,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Code", "Annotated PDF")] + ATTACHMENTS)
    add_para(doc, [(ATTACH_NOTE,)])
    dl = doc.add_paragraph()
    dl.add_run("Download — this transmittal and the annotated PDFs: ").bold = True
    aplicar_arial_12(dl)
    add_hyperlink(dl, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Submittal", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.", {"bold": True}),
        (CLOSING,),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. Publicar la "
              "carpeta en Synology, pegar el enlace y REGENERAR antes de emitir.")
