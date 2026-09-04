#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
crear_transmittal.py — TRANSMITTAL N37 (P22-TM-09-000-037-0)

Submittals 25007-0086 y 25007-0087 (jue 27-Ago-2026) y 25007-0088 (vie 28-Ago-2026).
ENTREGAS 86 y 88. SIETE documentos.

VEREDICTO GLOBAL: 3 — To be revised. 2 Codigo 1, 4 Codigo 2 y 1 Codigo 3.
El codigo lo fija UN SOLO documento: el registro del FAT del tablero.

Mapa de subsecciones:
    2.1  Liquid Penetrant Examination Procedure Rev C  P22-BA-09-000-014  Code 2
    2.2  Radiography Examination Procedure Rev C       P22-BA-09-000-015  Code 2
    2.3  PLC/LCP Schematic Diagram Rev B               P22-CD-09-008-002  Code 2
    2.4  Instrument Location Layout Rev D              P22-DWG-09-008-001 Code 2
    2.5  I/O List Rev 6                                P22-LI-09-008-001  Code 1  IFC
    2.6  Tie-In Point Layout Rev 0                     P22-DWG-09-005-005 Code 1  IFC
    2.7  PLC/LCP FAT Procedure - Hardware Rev B        P22-PP-09-000-001  Code 3

=======================================================================
LO NUEVO DE ESTE TRANSMITTAL: LA EXIGENCIA DE CIERRE DOCUMENTAL
=======================================================================

Instruccion del usuario, 31-Ago-2026: por el estado de la construccion y el atraso
declarado, BW Water no puede seguir enviando documentos sueltos a medida que
construye. Debe entregar TODO lo pendiente cerrado, en una sola entrega
consolidada, a mas tardar el JUEVES 3 DE SEPTIEMBRE DE 2026. Tajante.

UBICACION: encabeza la Seccion 3, que ya es el inventario de lo abierto, de modo
que la orden queda justo encima de la lista de lo que hay que consolidar. Una
linea del Resumen Ejecutivo apunta ahi.

DESVIACION DECLARADA DEL FORMATO: el CLAUDE.md manda resumir en UNA LINEA lo que
no entra en la tabla de los tres pendientes mas graves. Aqui esa linea se
convierte ADEMAS en una tabla de cierre consolidado, porque una exigencia que no
nombra los documentos no es exigible. La linea de "Also open" se conserva para lo
que no entra en la tabla.

ALCANCE: ingenieria, planos y procedimientos. El Dossier de Fabricacion queda
declarado APARTE con su propia via, porque depende de registros que se generan
durante la fabricacion y exigirlo entero en tres dias seria refutable de
inmediato. De el se exige el PLAN DE ENTREGA con fechas.

CONSECUENCIA: documental, no contractual. Lo que llegue despues del jueves ya no
alcanza a entrar en un ciclo de revision antes de que abra el FAT y pasa al
dossier final. Es un hecho del calendario, no una amenaza.

🔴 NO ESCRIBIR LA FECHA DEL FAT. La Nota Tecnica P22-NT-09-000-003-0, emitida el
31-Ago, pregunta cual ventana gobierna: el Project Schedule Rev B la pone del 7 al
18 de septiembre y el Progress Update del 28-Ago del 15 al 25. Escribir una fecha
contradiria por escrito esa nota. Se dice "before the Factory Acceptance Test
opens", que es cierto con cualquiera de las dos. Las unicas fechas de septiembre
que SI aparecen son los vencimientos de la Clausula 37.2 (7 y 8) y el plazo de la
exigencia (3).

=======================================================================

REGLA DE ALCANCE. Los siete documentos responden a comentarios previos, de modo
que cada uno se revisa unicamente contra la instruccion escrita del transmittal
anterior. No se introducen observaciones nuevas.

SOBRE UN Rev 0 NO SE AGREGAN COMENTARIOS NUEVOS. Los dos documentos emitidos para
construccion —la I/O List Rev 6 y el Tie-In Point Layout Rev 0— van en Codigo 1 y
SIN CC_ADASA; lo que queda abierto en ellos viaja como NOTA en el texto de su
subseccion y en la Seccion 3, sin bajar el codigo. Los cuatro Codigo 2 y el
Codigo 3 son emisiones para aprobacion, donde la condicion todavia no vence.

DECISION QUE SIGUE ABIERTA Y QUE EL BLOQUE DE ACCION 2.3 PRESERVA: ADASA declaro
vinculante el terminal 2711P-T10C22D9P en el TM N30 y el registro del FAT prueba
que el tablero se armo con el 2711P-T10C21D8S. Exigir el cambio a dias del FAT
tiene impacto de plazo; aceptarlo en silencio renuncia a una declaracion propia.
El transmittal NO elige: pide que BW Water declare por escrito como propone
cerrar la brecha. Los dos caminos quedan abiertos.

SIN numeros manuales en add_heading(); referencias por NOMBRE de seccion; cero
simbolo de seccion; sin cifras de multa y sin invocar el umbral de treinta dias,
porque INT-08 sigue abierto y la Notificacion de Adjudicacion no esta en el
repositorio.

Fuente unica del contenido: P22-TM-09-000-037-0_TRANSMITTAL.md
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N37 ADASA-BW_WATER.docx")

# Enlace de descarga de la carpeta del N37. Publicar la carpeta, pegar el enlace y
# REGENERAR. El modo de falla del N30, N31 y N32 fue verificar el enlace sobre el
# script y no sobre el texto extraido del Word: verificar SIEMPRE sobre el .docx.
DOWNLOAD_LINK = (
    "https://lrg.synology.me:6501/d/s/19hY5AfCDswSNULyibAyAkLm46YnKjSb/Ndsy8yqJtB5k0V1z0TwcYNx4AiD_bgc--V7OAzaBpeA0"
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
    "Submittals 25007-0086 to 25007-0088, seven documents. Tally: 2 Code 1, "
    "4 Code 2, 1 Code 3. One document sets the code: the PLC/LCP FAT Procedure "
    "Rev B, submitted for approval as the completed record of a test already run."
)

DISPOSITION = [
    "Liquid Penetrant Examination Procedure Rev C — Code 2. Correct the report "
    "form, which still carries another contract.",
    "Radiography Examination Procedure Rev C — Code 2. Name the material and the "
    "wall range actually radiographed.",
    "PLC/LCP Schematic Diagram Rev B — Code 2. Add the CIP heater running feedback "
    "terminal; close the operator terminal catalogue number.",
    "Instrument Location Layout Rev D — Code 2. Fill the revision block; state the "
    "Equipment Layout revision on the drawing.",
    "I/O List Rev 6 — Code 1. No action.",
    "Tie-In Point Layout Rev 0 — Code 1. Not held; two notes stand.",
    "PLC/LCP FAT Procedure - Hardware Rev B — Code 3. Re-issue as Rev C.",
]

WHY3_LEAD = "Why Code 3 — PLC/LCP FAT Procedure Rev B."
WHY3 = (
    " The hardware test of the control panel was run on 3 to 5 August at the panel "
    "builder in Ningbo. ADASA received no notice and no witness attended, against "
    "row 6.2 of the approved Inspection and Test Plan, which assigns ADASA a witness "
    "point on that test, and against row 7.1, which is a hold point on ADASA approval "
    "of the detailed test procedure. The document submitted now is the completed "
    "record of that test, signed as Witnessed by (Client / Third-Party Inspector) by "
    "BW Water personnel. Its punch list marks ten items category A, defined in the "
    "document itself as items that must be resolved before panel dispatch, and "
    "eight of them carry target date, actual date and status blank. Three of the five "
    "points ADASA raised at Transmittal N27 remain open."
)

CLOSES_LEAD = "Two documents close long-standing items."
CLOSES = (
    " The Instrument Location Layout clears the Code 3 it has carried since "
    "Transmittal N23, and the Tie-In Point Layout reaches Rev 0 with the brine feed "
    "design pressure declared at 5 barG, consistent with the approved Line List. Two "
    "of the three non-destructive testing procedures also clear the acceptance "
    "criterion that returned them at Code 3."
)

RETURN_DATE = (
    "Clause 37.2 gives seven working days: 7 September for 25007-0086 and "
    "25007-0087, 8 September for 25007-0088. This transmittal is issued within all "
    "three. The forms asked for return three calendar days after issue, two of them "
    "on a Sunday."
)

POINTER = (
    "The consolidated close-out of all outstanding documentation, and its date, are "
    "set out under Pending Observations from Previous Transmittals."
)

# --- Seccion 2 -------------------------------------------------------------
S21_STATUS = (
    "The determinant closed. Clause 13.0 now offers a single acceptance criterion, "
    "ASME B31.3 paragraph 341.3.2 with its thresholds, and the Section VIII Division "
    "1 Appendix 6 block is gone; the form the examiner signs declares that same "
    "criterion. What did not close is the report form itself, which still carries the "
    "report number and the job number of another contract, three consumable batch "
    "numbers, and an observations column pre-written with the result. That form is "
    "the sheet that enters the quality dossier, and this is the second time it is "
    "raised. Itemised in P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf."
)
S21_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new procedure revision required:"
)
S21_ACTION = (
    " clear the report form of the identifiers of another contract and of the "
    "pre-written result, and align the procedure revision it cites with the revision "
    "of the document (OBS-01 to OBS-03 and NOTE-01 on the annotated PDF). The comment "
    "sheet answers that the point was revised as per comment, against a block that "
    "names the report form data of another contract; that reply does not match the "
    "document."
)

S22_STATUS = (
    "The determinant closed in both halves. The five acceptance codes of clause 23.0 "
    "came down to one, and the geometric unsharpness limit of 1.8 mm, which is the "
    "Section I dispensation for power piping and which B31.3 does not grant, was "
    "replaced by the 0.020 in. of Table T-274 with its text reproduced. What remains "
    "is scope: clause 1.0 still reads generically and names neither the ASTM A790 UNS "
    "S32750 nor the 6.02 to 8.56 mm wall range actually radiographed on this module, "
    "and the cover still carries the document number of a positive material "
    "identification procedure. Itemised in "
    "P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf."
)
S22_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new procedure revision required:"
)
S22_ACTION = (
    " state the material and the wall thickness range of this module in the scope, "
    "and correct the document number on the cover (OBS-01 and NOTE-01 to NOTE-03 on "
    "the annotated PDF)."
)

S23_STATUS = (
    "Second cycle on the condition of Transmittal N20. The reconciliation of inputs "
    "and outputs against the approved I/O List is nearly complete: the CIP heater "
    "output is wired on sheet 39 through relay KA8, the four spare inputs on sheet 35 "
    "match the three rows the I/O List deleted at Rev 6, and the air conditioning "
    "signals are on sheets 37 and 38. One terminal is missing: CIP HEATER RUNNING, "
    "item 109 of the I/O List Rev 6, has no terminal on any of the four digital input "
    "sheets, nineteen assigned against twenty active in the list, with thirteen free "
    "terminals available. The heater output was wired and its running feedback was "
    "not. Separately, the bill of materials on sheet 28 still lists the operator "
    "terminal as 2711P-T10C21D8S. Itemised in "
    "P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf."
)
S23_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new schematic revision required:"
)
S23_ACTION = (
    " assign a digital input terminal to CIP HEATER RUNNING and cite the I/O List by "
    "its code and its numeric revision, since the comment sheet answers against an "
    "I/O List Rev B that does not exist. On the operator terminal, ADASA declared the "
    "2711P-T10C22D9P binding at Transmittal N30 and the record of the panel test now "
    "shows the 2711P-T10C21D8S installed: state in writing how BW Water proposes to "
    "close that gap, together with the two Ethernet ports the approved datasheet "
    "requires (OBS-01 to OBS-02 and NOTE-01 on the annotated PDF)."
)

S24_STATUS = (
    "The determinant closed. The geometry is now drawn against the Equipment Layout "
    "Rev D, which reached Code 1 at Transmittal N33, so the dependency on a "
    "superseded drawing is lifted, and the title block code and the issue date are "
    "correct. Two changes to the drawing itself remain, both verified by render of "
    "the title block. The revision block carries four rows, D, C, B and A, and all "
    "four repeat the same description, ISSUED FOR APPROVAL, with the change notice "
    "column blank, so no row states what changed at its issue; and the row of Rev C, "
    "which reads APR.17.26 on the drawing issued at Rev C, now reads JUN.16.26, so "
    "the April issue was overwritten instead of a row being added and the two Rev C "
    "issues that the original observation was about are still not distinguishable. "
    "And the declaration that the drawing follows the Equipment Layout Rev D lives "
    "only on the reply sheet: the note box of both sheets is empty and there is no "
    "reference document list. Itemised in "
    "P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf."
)
S24_ACTION_LEAD = (
    "Action to issue at IFC Rev 0 — no new drawing revision required:"
)
S24_ACTION = (
    " fill the revision block with what changed at each issue instead of repeating "
    "the same description, and restore the April issue date on the row of Rev C so "
    "the two issues that carried that letter are distinguishable. The note box is "
    "to state the Equipment Layout revision the drawing is built on (OBS-01 to "
    "OBS-02 on the annotated PDF). The change notice column is not required: it is "
    "empty on the Equipment Layout as well, so it is a project convention and not "
    "an omission."
)

S25_STATUS = (
    "The single action of Transmittal N28 closed, and it was verified on the list and "
    "not on the declaration: row 108 carries REL-09-001, HS001, CIP HEATER ON/OFF "
    "COMMAND as a dry contact output, and row 109 carries REL-09-001, XB002, CIP "
    "HEATER RUNNING as the input in the opposite direction, both at revision 6. The "
    "list is issued for construction, so the condition fell due at this issue and "
    "there is no substantive defect against it."
)
S25_ACTION_LEAD = (
    "Action: none on this document — accepted; issue directly at IFC Rev 0."
)
S25_ACTION = (
    " Related deliverable tracked under Pending Observations from Previous "
    "Transmittals: the running feedback that this list now defines still has no "
    "terminal on the schematic diagram, and the four digital inputs signed off on the "
    "panel test record are not the four this revision carries."
)

S26_STATUS = (
    "The oldest open document of the package reaches Rev 0 with its substantive point "
    "closed. The tie-in schedule now carries a complete DESIGN PRESSURE column and "
    "the brine feed point TP-DA P8-001, 4 inch, class 150 to ASME B16.5, is declared "
    "at 5 barG, which matches the line DA-PVC-DN100-09-001 of the Line List Rev 0 "
    "approved at Code 1: the ADASA acceptance of the ANSI 150 class is satisfied. The "
    "drawing is issued for construction and is not held."
)
S26_ACTION_LEAD = (
    "Action: none on this document — accepted; issue directly at IFC Rev 0."
)
S26_ACTION = (
    " Two notes to fold into the next natural issue, neither of which holds a drawing "
    "that already governs construction. First, the reply states that TP-AS P11-001 is "
    "not a flanged connection and that the termination is the valve itself; the two "
    "cells still read as a dash and the drawing does not say it, so the sheet should "
    "carry what the reply says. Second, the DRAWING STATUS field of the title block "
    "reads ISSUED FOR APPROVAL while the revision row of the same title block and the "
    "submittal form both read ISSUED FOR CONSTRUCTION, and the cover still carries "
    "Revision A dated 02/04/2026."
)

S27_STATUS = (
    "This revision is not a procedure. It is the completed record of the hardware "
    "test of the control panel, run on 3 to 5 August at the panel builder in Ningbo, "
    "submitted as an approval revision three weeks later. The condition of its Code 2 "
    "at Transmittal N27 was tied to a milestone that was not Rev 0: it read before "
    "witnessing, and that milestone passed. Three of the five points remain open. The "
    "Eight of the ten category A punch list items, all raised by the BW Water "
    "engineer, have target date, actual date and status blank, and the closing block of the punch "
    "list is empty; an attached rectification report declares them executed with "
    "photographs, unsigned, undated and unwitnessed. Six of the eight are signals the "
    "approved I/O List has carried since revisions 3 and 4. The document is "
    "photographed rather than issued, and eleven of its sixteen pages return no "
    "readable text. Itemised in "
    "P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf."
)
S27_ACTION_LEAD = "Action — re-issue as Rev C:"
S27_ACTION = (
    " submit the procedure as a procedure, separate from any record, citing the "
    "schematic diagram and the I/O List by code and by issued revision; close the "
    "eight open category A punch list items with target date, actual date, status and "
    "signature, and have the closure witnessed; reconcile the four digital inputs "
    "and the output relay map signed off on the record against the I/O List Rev 6 "
    "and the schematic Rev B, which today state three different things; and list "
    "the model, serial number and calibration certificate of each test instrument, "
    "as safety requirement 3 of "
    "the document itself requires (OBS-01 to OBS-05 and NOTE-01 to NOTE-02 on the "
    "annotated PDF)."
)

# --- Seccion 3: la exigencia, que encabeza -------------------------------
DEMAND_LEAD = (
    "BW Water is to stop submitting documents one at a time as construction "
    "proceeds, and is to deliver every outstanding engineering document, drawing and "
    "procedure in a single consolidated submission, no later than Thursday 3 "
    "September 2026."
)
DEMAND_WHY = (
    "Three facts make this necessary, and none of them is a matter of opinion. "
    "Documents are arriving after the thing they describe exists: the record of the "
    "panel test arrives now and the test was run on 3 to 5 August; the Tie-In Point "
    "Layout arrives at Rev 0 with fabrication under way; the I/O List arrives issued "
    "for construction. The review cycle has stopped serving its purpose: the review "
    "period of 25007-0088 under Clause 37.2 expires after the Factory Acceptance Test "
    "opens, so ADASA is asked to review the gate document of a test that has already "
    "started. And this is the fifth consecutive batch whose forms ask for return "
    "inside three calendar days against the seven working days of Clause 37.2, twice "
    "falling on a weekend."
)
DEMAND_CONSEQ_LEAD = (
    "What arrives after Thursday 3 September no longer fits a review cycle before the "
    "Factory Acceptance Test opens, and passes to the final dossier."
)
DEMAND_CONSEQ = " ADASA is stating a fact about the calendar, not a position."

PENDING_LEAD = "The three most serious items carried forward:"

PENDING = [
    ("N30",
     "Shop fabrication set 25007-ME-PI-0901-0006 to -0016",
     "Eleven drawings across seventeen sheets, stamped for construction, removed "
     "from the Piping Layout at Rev D and never submitted as a deliverable of their "
     "own with an ADASA code and revision index. Their two pressure-containment "
     "findings are unanswered: threaded austenitic instrument branches on super "
     "duplex lines rated 60 to 90 barG design, and an undeclared specification break "
     "between the super duplex and PVC systems",
     "Open, aggravated by the withdrawal without re-submission"),
    ("N25, N29, N30",
     "Fabrication and testing dossier",
     "Item 65 remains NOT DELIVERED. The index has reached Rev B and returned at "
     "Code 3; no record has followed it. It sustains rows 8.3 and 8.4 of the "
     "Inspection and Test Plan, on which 40 per cent of payment depends",
     "Open, overdue"),
    ("N26, N30",
     "Endorsed structural calculation report P22-CD-09-005-001",
     "Issued at Rev 0 for construction carrying internal initials only. It has yet "
     "to be issued with the endorsement of a professional engineer registered in "
     "Chile, undertaken in writing three times",
     "Open, overdue"),
]

CLOSEOUT_LEAD = (
    "The consolidated submission of Thursday 3 September is to contain, at minimum:"
)

CLOSEOUT = [
    ("P22-BA-09-000-016 Ultrasonic Thickness Procedure",
     "Rev C. The only one of the three non-destructive testing procedures that has "
     "not returned", "Code 3 since N35"),
    ("P22-ET-09-009-002, -007 and -008 Fedco datasheets",
     "Rev 0 for construction, deleting STYLE 77 from the four connection callouts",
     "N36"),
    ("P22-LI-09-008-003 Instrument List",
     "Re-issue with VT-09-001 ranged at 0 to 12 mm/s rms", "N34"),
    ("25007-ME-PI-0901-0006 to -0016",
     "Eleven shop fabrication drawings across seventeen sheets, submitted as a "
     "deliverable of their own with code and revision", "N30"),
    ("P22-CD-09-005-001 Structural Calculation Report",
     "With the endorsement of a professional engineer registered in Chile",
     "N26, N30"),
    ("P22-DWG-09-009-002, P22-LI-09-009-003 and the fabrication drawings",
     "Line numbering unified against the approved Line List",
     "Coordination meeting of 26 August"),
    ("P22-BA-09-000-012 Operating and Maintenance Manual", "Rev B",
     "Code 3 since N27"),
    ("P22-BA-09-000-013 Fabrication and Testing Dossier Index", "Rev C",
     "Code 3 since N34"),
    ("P22-LI-09-008-016 HMI Display Screenshot",
     "Rev 0 with the six tags reconciled", "Code 2 since N31"),
    ("Factory Acceptance Test procedure of the module",
     "Never delivered. Required by Section 8.1 of the Technical Specification",
     "ET Section 8.1"),
    ("Preservation, Packaging and Transport Procedure",
     "Hold point for approval prior to shipment", "BAE Clause 41"),
    ("P22-LI-09-005-001 Equipment List and P22-LI-09-005-002 Valve List",
     "Re-issue, undertaken in writing on the 3D Model comment sheet", "N36"),
]

OM_LEAD = "On the Operating and Maintenance Manual there is no dependency left."
OM = (
    " It was returned at Code 3 at Transmittal N27 because sections 4.4 and 4.5 "
    "reproduced logic assigned to control documents that were then open. Those "
    "documents have closed: the Alarm and Interlock List and the Control and Sequence "
    "Chart were both issued at Rev 0 and approved at Code 1 at Transmittal N34. "
    "Nothing now holds the manual."
)

DOSSIER_LEAD = (
    "The fabrication and testing dossier is treated separately, and is not part of "
    "the Thursday submission."
)
DOSSIER = (
    " It depends on records generated during fabrication. What ADASA requires by "
    "Thursday 3 September is the delivery plan of the dossier, with dates by section, "
    "against the index at Rev C."
)

ALSO_OPEN_LEAD = "Also open:"
ALSO_OPEN = (
    " the liquid penetrant records of 7 August, examined five days before their "
    "procedure was submitted; the measurement point drawing required by row 7.8 of "
    "the Inspection and Test Plan; and the Pressure Test Record Chart as a controlled "
    "form. Entering the list with this transmittal: the reconciliation of the four "
    "digital inputs and of the output relay map between the panel test record, the "
    "I/O List Rev 6 and the schematic Rev B, which today state three different "
    "things. Closing with this transmittal, and leaving the list: the design pressure "
    "at the brine feed tie-in point."
)

# --- Seccion 4 -------------------------------------------------------------
ATTACHMENTS = [
    ("Liquid Penetrant Examination Procedure Rev C", "2",
     "P22-BA-09-000-014_C_Liquid_Penetrant_CC_ADASA.pdf"),
    ("Radiography Examination Procedure Rev C", "2",
     "P22-BA-09-000-015_C_Radiography_CC_ADASA.pdf"),
    ("PLC/LCP Schematic Diagram Rev B", "2",
     "P22-CD-09-008-002_B_PLC_LCP_Schematic_CC_ADASA.pdf"),
    ("Instrument Location Layout Rev D", "2",
     "P22-DWG-09-008-001_D_Instrument_Location_Layout_CC_ADASA.pdf"),
    ("PLC/LCP FAT Procedure - Hardware Rev B", "3",
     "P22-PP-09-000-001_B_PLC_LCP_FAT_Procedure_CC_ADASA.pdf"),
]
ATTACH_NOTE = (
    "All documents with open observations or notes carry annotated PDFs, four Code 2 "
    "and one Code 3. Only the two Code 1 — Approved documents carry none."
)
DOWNLOAD_LEAD = "The annotated PDFs are available at the following download link:"

# --- Seccion 5 -------------------------------------------------------------
RESPONSE_SUMMARY = [
    ("P22-BA-09-000-014", "Liquid Penetrant Examination Procedure", "C",
     "25007-0086", "2 — Approved as noted"),
    ("P22-BA-09-000-015", "Radiography Examination Procedure", "C",
     "25007-0086", "2 — Approved as noted"),
    ("P22-CD-09-008-002", "PLC/LCP Schematic Diagram", "B",
     "25007-0086", "2 — Approved as noted"),
    ("P22-DWG-09-008-001", "Instrument Location Layout", "D",
     "25007-0086", "2 — Approved as noted"),
    ("P22-LI-09-008-001", "I/O List", "6", "25007-0086", "1 — Approved"),
    ("P22-DWG-09-005-005", "Tie-In Point Layout", "0", "25007-0087",
     "1 — Approved"),
    ("P22-PP-09-000-001", "PLC/LCP FAT Procedure - Hardware", "B",
     "25007-0088", "3 — To be revised"),
]


if __name__ == "__main__":
    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N37 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-037-0",
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
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    for item in DISPOSITION:
        add_bullet(doc, item)
    add_para(doc, [(WHY3_LEAD, {"bold": True}), (WHY3,)])
    add_para(doc, [(CLOSES_LEAD, {"bold": True}), (CLOSES,)])
    add_para(doc, [("Return date.", {"bold": True}), (" " + RETURN_DATE,)])
    add_para(doc, [(POINTER, {"bold": True})])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)

    doc.add_heading(
        "Liquid Penetrant Examination Procedure Rev C — P22-BA-09-000-014",
        level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S21_STATUS,)])
    add_para(doc, [(S21_ACTION_LEAD, {"bold": True}), (S21_ACTION,)])

    doc.add_heading(
        "Radiography Examination Procedure Rev C — P22-BA-09-000-015", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S22_STATUS,)])
    add_para(doc, [(S22_ACTION_LEAD, {"bold": True}), (S22_ACTION,)])

    doc.add_heading(
        "PLC/LCP Schematic Diagram Rev B — P22-CD-09-008-002", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S23_STATUS,)])
    add_para(doc, [(S23_ACTION_LEAD, {"bold": True}), (S23_ACTION,)])

    doc.add_heading(
        "Instrument Location Layout Rev D — P22-DWG-09-008-001", level=2)
    add_para(doc, [("Response Code: 2 — Approved as noted", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S24_STATUS,)])
    add_para(doc, [(S24_ACTION_LEAD, {"bold": True}), (S24_ACTION,)])

    doc.add_heading("I/O List Rev 6 — P22-LI-09-008-001", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S25_STATUS,)])
    add_para(doc, [(S25_ACTION_LEAD, {"bold": True}), (S25_ACTION,)])

    doc.add_heading("Tie-In Point Layout Rev 0 — P22-DWG-09-005-005", level=2)
    add_para(doc, [("Response Code: 1 — Approved", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S26_STATUS,)])
    add_para(doc, [(S26_ACTION_LEAD, {"bold": True}), (S26_ACTION,)])

    doc.add_heading(
        "PLC/LCP FAT Procedure - Hardware Rev B — P22-PP-09-000-001", level=2)
    add_para(doc, [("Response Code: 3 — To be revised", {"bold": True})])
    add_para(doc, [("Status.", {"bold": True}), (" " + S27_STATUS,)])
    add_para(doc, [(S27_ACTION_LEAD, {"bold": True}), (S27_ACTION,)])

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    #    La exigencia ENCABEZA la seccion. Ver la cabecera del script.
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [(DEMAND_LEAD, {"bold": True})])
    add_para(doc, [(DEMAND_WHY,)])
    add_para(doc, [(DEMAND_CONSEQ_LEAD, {"bold": True}), (DEMAND_CONSEQ,)])
    add_para(doc, [(PENDING_LEAD,)])
    add_simple_table(
        doc,
        [("Origin TM", "Document", "Observation", "Status")] + PENDING)
    add_para(doc, [(CLOSEOUT_LEAD, {"bold": True})])
    add_simple_table(
        doc,
        [("Document", "Required", "Origin")] + CLOSEOUT)
    add_para(doc, [(OM_LEAD, {"bold": True}), (OM,)])
    add_para(doc, [(DOSSIER_LEAD, {"bold": True}), (DOSSIER,)])
    add_para(doc, [(ALSO_OPEN_LEAD, {"bold": True}), (ALSO_OPEN,)])

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Code", "Annotated PDF")] + ATTACHMENTS)
    add_para(doc, [(ATTACH_NOTE,)])
    p = doc.add_paragraph()
    r = p.add_run(DOWNLOAD_LEAD + " ")
    r.bold = True
    aplicar_arial_12(p)
    add_hyperlink(p, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Submittal", "Response Code")]
        + RESPONSE_SUMMARY)

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: el enlace de descarga sigue en placeholder. "
              "Publicar la carpeta, pegar el enlace y REGENERAR.")
