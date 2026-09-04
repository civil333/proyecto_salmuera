#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TRANSMITTAL N27 ADASA-BW_WATER.
Submittals 25007-0063 (E63) + 25007-0064 (E64). Fecha emision: 13-Jul-2026.

Veredicto global: 3 - TO BE REVISED. Tally: 5 Code 2 + 1 Code 3.
Seis documentos. Re-escopeado de E63 (2 docs) a E63+E64 (6 docs): al llegar la
E64 con el correo del TM aun en BORRADOR, se aplica el patron validado de
re-escopear el TM en vez de abrir un N28.

Driver unico del veredicto (Code 3):
- HP and LP Pressure Test Procedure Rev C: responde a la observacion del N26
  adjuntando la Line List en vez de escribir la presion en el cuerpo, asi que esa
  tabla pasa a ser la instruccion ejecutable. La tabla ordena 75 bar de
  hidrostatica sobre DA-PVC-DN65-09-016 (RO Brine Discharge), PVC SCH 80 DN65 con
  brida Clase 150 que opera a 1 bar: el diseno de 50 bar viene arrastrado de la
  Rev C aprobada (TM N18), pero la columna HYDROTEST nueva lo vuelve ejecutable.
  Ademas la Line List adjunta se rotula "Rev 0" (nunca transmitida).

Cierres/aprobados con notas (Code 2):
- RO Vessel Hydrostatic Test Procedure Rev C: cierra el CRITICAL del N26. El
  formulario de 45,5 bar desaparecio; el test report real (17-Jun) evidencia los
  vessels ensayados a 91,01 bar (1.320 psi = 1,1x1200) y 136,52 bar (1.980 psi =
  1,1x1800), todos O.K., con certificados de calibracion. Housekeeping: fijar las
  presiones numericas en el cuerpo (OBS-01) y reconciliar la seleccion de
  manometro (OBS-02). Waiver ASME no se reabre.
- Painting Procedure Rev B: cumple las dos condiciones del N25 (equivalencia
  Jotun coat-by-coat + durabilidad marina C5-M). Tres correcciones al formulario.
- PLC/LCP Outline Panel Drawing Rev C: resuelve el gate del enclosure abierto en
  N20/N25. Exterior SS316L, gland plates SS316L, NEMA 4X/IP66, internos
  galvanizados/CRS aceptados per RFI-002; typo "SECONDE STAGE" corregido. Tres
  items menores (cable clamp TBC, fila MATERIAL, typos).
- PLC/LCP FAT Procedure - Hardware Rev A (NUEVO): FAT de hardware completo y
  solido. Driver de la nota = los planos gobernantes citados con codigo errado
  (ET en vez de CD). Tag AO y numero de documento a corregir.
- Operating and Maintenance Manual Rev A (NUEVO): manual servible; contenido
  especifico del proyecto correcto. CIP cross-ref, recuperacion 42/42,86, modelo
  de membrana; boilerplate a limpiar.

SIN numeros manuales en add_heading() (el template ADASA auto-numera H1/H2).
Referencias por NOMBRE de seccion. Cero simbolo de seccion.
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
OUTPUT = os.path.join(SCRIPT_DIR, "TRANSMITTAL N27 ADASA-BW_WATER.docx")

# Seis CC_ADASA (1 Code 3 + 5 Code 2). Ningun Code 1 en estas entregas.
# Reemplazar por el link de la carpeta Synology de ESTE transmittal antes de emitir.
DOWNLOAD_LINK = "PENDIENTE_LINK_SYNOLOGY_N27"


def add_hyperlink(paragraph, url, text):
    """Inserta un hipervinculo externo clicable (Arial 12, azul subrayado)."""
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


# ---------------------------------------------------------------------------
# Section 2 content. heading, code, status[], obs[(id,sev,topic)], action_paras[]
# Orden: el driver Code 3 (HP/LP) abre; luego los cinco Code 2, agrupados por
# paquete (QA/fabricacion: RO Hydro + Painting; tablero PLC: Outline + FAT; O&M).
# ---------------------------------------------------------------------------

SECTIONS = [
    dict(
        heading="HP and LP Pressure Test Procedure Rev C — P22-BA-09-000-010",
        code="Response Code: 3 — To Be Revised",
        status=[
            ("Status.", {"bold": True}),
            (" Rev C keeps the correct ASME B31.3 factors (1.5 times design pressure "
             "for the hydrostatic step, 1.1 times for the pneumatic step) and answers "
             "the Transmittal N26 observation by attaching the Line List, whose new "
             "HYDROTEST PRESS. column gives a value for every line. Since the body "
             "still writes no pressure, that column is the operative instruction, and "
             "it cannot be executed safely. Each value in it is 1.5 times the design "
             "pressure of its line. The arithmetic is right, and so is the result on "
             "the Super Duplex circuit (135 bar on the lines designed for 90 bar, 120 "
             "bar on those designed for 80 bar) and on the PVC lines designed for 2 "
             "and 5 bar (3 and 7.5 bar). The RO Brine Discharge breaks it: the line is "
             "PVC Schedule 80 yet carries a 50 bar design pressure, so the column "
             "orders 75 bar on a plastic line. The attachment also has no approved "
             "revision status. Annotations on "
             "P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "CRITICAL",
             "The attached Line List sets line DA-PVC-DN65-09-016 (RO Brine Discharge, "
             "POLYVINYL CHLORIDE SCH 80, DN65, wall 6.02 mm, operating pressure 1 bar) "
             "at a 50 bar design pressure, and its HYDROTEST PRESS. column therefore "
             "orders 75 bar. A PVC Schedule 80 DN65 line with Class 150 flanges does "
             "not withstand 75 bar at the 45 degree Celsius design temperature that "
             "the same list assigns to it; a shop testing to this instruction would "
             "rupture the line and injure the crew. The 50 bar design value is carried "
             "over from Line List Rev C, and ADASA did not raise it when that revision "
             "was approved at Transmittal N18; the hydrostatic column added in this "
             "attachment is the change that turns it into an executable test pressure. "
             "Reconcile the line: either the piping class or the design pressure of the "
             "RO Brine Discharge is wrong, and the resulting test pressure must be "
             "consistent with the class actually installed. The requirement is the "
             "Technical Specification (P22-ET-09-000-001-0), Section 5.2.1 - "
             "Low-Pressure Piping, which fixes PVC to ASTM D1784 and D1785, Schedule "
             "80, with Class 150 flanges, and ASME B31.3 for the test itself."),
            ("OBS-02", "MAJOR",
             "The attached Line List is labelled \"Rev. No: 0\". The revision ADASA "
             "approved is Rev C (Code 1 at Transmittal N18, 18-May-2026) and it carries "
             "no HYDROTEST PRESS. column, so the pressure the inspector signs against "
             "comes from a revision that has never been transmitted for review. "
             "Transmit the corrected Line List revision as a submittal, and cite it in "
             "the procedure body by document number and revision."),
            ("OBS-03", "MINOR",
             "The body still writes no numeric test pressure. Clauses 5.5.12 and 5.6.12 "
             "refer only to \"design pressure in the approved line list\", and both "
             "state it as a minimum rather than the single value to apply. State on the "
             "face of the procedure the governing envelope for each circuit (135 bar "
             "high pressure and 7.5 bar low pressure, per rows 5.2 and 5.1 of the "
             "approved Inspection and Test Plan), naming the Line List revision that "
             "fixes the value line by line."),
            ("OBS-04", "MINOR",
             "Subsection 5.7.2 (Weld Joints) still skips 5.7.2.2 — the sequence runs "
             "5.7.2.1, 5.7.2.3, 5.7.2.4, 5.7.2.5. The pneumatic-section gap at 5.6.5 is "
             "corrected, but this is the second consecutive revision in which the reply "
             "reports the numbering defect as resolved while the gap survives."),
            ("NOTE-01", "NOTE",
             "The Pressure and Leak Test Report form (AQ-QAM-F018 Rev 4) is now attached "
             "and carries no pre-printed pressure, which closes the Transmittal N26 "
             "note. It has no field for the required test pressure, only for the "
             "pressure actually applied; add one, referencing the approved Line List "
             "revision, so the inspector contrasts the applied value against the "
             "specified one."),
        ],
        action_paras=[
            [("Action — re-issue as Rev D:", {"bold": True}),
             (" correct the RO Brine Discharge line so that its class, design pressure "
              "and test pressure are consistent, and re-issue the Line List accordingly "
              "(OBS-01); transmit that Line List revision for record and cite it in the "
              "body (OBS-02); state the governing test-pressure envelope per circuit on "
              "the face of the procedure (OBS-03); close the numbering gap at 5.7.2.2 "
              "(OBS-04). The high-pressure hydrostatic test remains a Hold Point, and "
              "no line is to be tested until the governing Line List revision is "
              "transmitted.",)],
        ],
    ),
    dict(
        heading="RO Vessel Hydrostatic Test Procedure Rev C — P22-BA-09-000-009",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Rev C closes the critical observation of Transmittal N26. The embedded "
             "Protec form that printed 45.5 bar is removed, and in its place the actual "
             "dimensional and hydrostatic test report of 17-Jun-2026 records the vessels "
             "tested at their required pressures: 91.01 bar on the BPV81200SP7 vessels "
             "(1,320 psi, 1.1 times the 1,200 psi design) and 136.52 bar on the "
             "BPV81800SP7 vessels (1,980 psi, 1.1 times the 1,800 psi design), all units "
             "passing, with the gauge calibration certificates attached. This is the "
             "test for which the ASME code stamp was waived, and the record now "
             "evidences it was performed at the pressures the Inspection and Test Plan "
             "and the 02-Jun-2026 waiver require. Two items remain on the document "
             "itself. Annotations on "
             "P22-BA-09-000-009_C_RO_Vessel_Hydrostatic_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MINOR",
             "The procedure body still states only the generic rule \"1.1 times the "
             "design pressure for ASME certified vessels\" and writes no binding numeric "
             "test pressure, although its own attached report and the reply to "
             "Transmittal N26 (\"revise as per comment\") fix the values. State on the "
             "face of the procedure the governing test pressures — 1,320 psi (91.0 bar) "
             "for the BPV81200SP7 and 1,980 psi (136.5 bar) for the BPV81800SP7 — so "
             "the document is self-contained. Acceptance rests on the attached report, "
             "which already evidences compliance; no re-test is required."),
            ("OBS-02", "MINOR",
             "Neither of the two attached gauge calibration certificates falls within "
             "the gauge-selection window the procedure sets for itself (a dial range "
             "about twice the test pressure, not exceeding four times nor less than 1.5 "
             "times): certificate 27258 covers 0 to 160 bar, 1.17 times the 136.5 bar "
             "test and below the 1.5-times floor, and certificate 27249 covers 0 to "
             "2500 bar, far above the four-times ceiling. Reconcile the gauge selection "
             "with the procedure's own criterion, or state which gauge governs each "
             "test."),
            ("NOTE-01", "NOTE",
             "This closes the critical observation carried since Transmittal N23 and "
             "re-stated at Transmittal N26. The ASME stamp waiver of 02-Jun-2026 is not "
             "reopened, and a single calibrated gauge is accepted for the vessel "
             "hydrostatic test."),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new revision required:", {"bold": True}),
             (" state the binding test pressures on the face of the procedure (OBS-01), "
              "and reconcile the gauge selection with the procedure's own criterion "
              "(OBS-02). ADASA's acceptance rests on the attached 17-Jun-2026 report, "
              "which already evidences the vessels were tested and passed at the "
              "required pressures.",)],
        ],
    ),
    dict(
        heading="Painting Procedure Rev B — P22-BA-09-000-011",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Rev B meets the two conditions ADASA set at Transmittal N25 for using a "
             "system other than Sherwin-Williams. The Jotun technical letter of "
             "02-Jul-2026 (TSS-DD-MYPC039-26) and the three product data sheets give "
             "the product-to-product equivalence against the architecture fixed by the "
             "approved Painting Specification (P22-ET-09-006-002) Rev C. The "
             "correspondence holds coat by coat: zinc-rich epoxy primer at 80 "
             "micrometres (Barrier 80, compliant with SSPC Paint 20 level 2), "
             "micaceous-iron-oxide high-build epoxy midcoat at 200 micrometres "
             "(Penguard Midcoat M20), aliphatic polyurethane topcoat at 75 micrometres "
             "(Hardtop XP), 355 micrometres in total. The letter also confirms "
             "suitability for the ISO 12944 C5-M corrosivity category, which is the "
             "marine durability the coastal site requires. The scope is now bounded to "
             "ASTM A-36 carbon steel with stainless steel and non-metallic surfaces "
             "excluded, and the quality control incorporates the adhesion pull-off "
             "test, the ISO 2808 measurement method and the SSPC-SP10 blast reference. "
             "The inspection form in Appendix A does not close, and it is the record "
             "the quality inspector signs. Annotations on "
             "P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "The anchor-profile contradiction is half corrected. The procedure body "
             "and the acceptance row of the inspection form now read 50 to 80 "
             "micrometres, but the BLASTING ACTIVITY criterion in that same form still "
             "reads 40 to 75 micrometres, so the inspector works against two "
             "incompatible criteria and can accept a 40 micrometre profile. That floor "
             "sits below the 50 micrometre lower bound ADASA required at Transmittal "
             "N23, and below the 50 micrometre anchor profile of the Technical "
             "Specification (P22-ET-09-000-001-0), Section 5.1.9 - Support Frame. Unify "
             "the form to the single 50 to 80 micrometre criterion the procedure itself "
             "adopts."),
            ("OBS-02", "MINOR",
             "The inspection form still carries \"Specified DFT: xxx um\" as a "
             "placeholder and leaves the Type row of the painting system blank, so the "
             "nominal dry film thickness per coat appears nowhere on the record. Print "
             "the nominal values (80, 200 and 75 micrometres, not less than 355 "
             "micrometres in total) and the product per coat."),
            ("OBS-03", "MINOR",
             "The finish colour is absent from the PAINTING SYSTEM block and from the "
             "Colour row of the inspection form. RAL 5012 (Luminous Blue) is fixed for "
             "the structural support frame by the approved Painting Specification Rev C "
             "and by the Technical Specification, Section 5.1.9 - Support Frame. "
             "Referring the inspector to the specification is a valid source, but the "
             "record being signed must carry the colour."),
            ("NOTE-01", "NOTE",
             "Closure of the two Transmittal N23 major observations: the coating-system "
             "substitution is now substantiated coat by coat against the approved "
             "Painting Specification, and the marine durability is demonstrated. ADASA "
             "raises no further objection to the Jotun system for the ASTM A-36 support "
             "frame."),
            ("NOTE-02", "NOTE",
             "SSPC-SP10 and NACE No. 2 are the same standard, so the SSPC-SP10 "
             "reference now in the procedure satisfies that item and no separate NACE "
             "citation is required."),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new procedure revision required:",
              {"bold": True})],
            [("1. Unify the anchor-profile criterion in the inspection form to 50 to 80 "
              "micrometres, removing the 40 to 75 micrometre entry (OBS-01).",)],
            [("2. Print the nominal dry film thickness and the product for each coat in "
              "the inspection form, replacing the \"xxx\" placeholder (OBS-02).",)],
            [("3. State RAL 5012 (Luminous Blue) as the finish colour in the "
              "painting-system block and in the inspection form (OBS-03).",)],
            [("ADASA's acceptance is conditioned on the coating actually applied being "
              "the C5-M certified Jotun system, no less than 355 micrometres total dry "
              "film thickness, RAL 5012, over an anchor profile of 50 to 80 "
              "micrometres.",)],
        ],
    ),
    dict(
        heading="PLC/LCP Outline Panel Drawing Rev C — P22-CD-09-008-001",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" Rev C resolves the enclosure gate opened at Transmittal N20 and carried "
             "through Transmittal N25. The drawing now specifies the exterior body, "
             "door, roof, rear panel, plinth and gland plates in SS316L, the interior "
             "mounting components in galvanised or cold-rolled steel painted RAL 7035, "
             "and the protection class as NEMA 4X and IP66 — the configuration settled "
             "in the RFI-002 reply of 07-Jul-2026 and coherent with the approved LCP "
             "Datasheet and the IFC Single Line Diagram. A dedicated Hoffman Cabinet "
             "Material Specifications note on sheet 5 states it explicitly, with the "
             "exterior parts in SS316L and the internal mounting components noted as "
             "not affecting the enclosure rating. The \"SECONDE STAGE\" typo is "
             "corrected. The drawing is approved as noted, with the internal galvanised "
             "and cold-rolled-steel components accepted and not reopened. Three minor "
             "items remain on the drawing itself. Annotations on "
             "P22-CD-09-008-001_C_Outline_Panel_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MINOR",
             "The cable-clamp schedule (note 14) leaves the 30 to 34 mm clamp diameter "
             "as \"TBC (to be confirmed)\". Finalise the value on the drawing when "
             "issuing Rev 0."),
            ("OBS-02", "MINOR",
             "The MATERIAL row (note 7) lists the enclosure frame, roof, rear panel and "
             "door under \"SHEET STEEL (INTERIOR ONLY) 2.0 mm\", while the COLOR row and "
             "the sheet-5 material specification make those same exterior surfaces "
             "SS316L 2.0 mm. Reword the row to separate the SS316L exterior skin from "
             "the interior sheet steel, so the drawing does not read as two materials "
             "for one part."),
            ("OBS-03", "MINOR",
             "Two labels do not match their content: note 12 reads \"CABLE DNRY\" for "
             "what the drawing describes as bottom cable entry, and the gateway TP1 is "
             "described as a \"Profibus-DP Module\" while its model, PLX32-EIP-MBTCP, is "
             "an EtherNet/IP to Modbus TCP gateway. Correct the descriptions."),
            ("NOTE-01", "NOTE",
             "The enclosure gate that held panel fabrication release since Transmittal "
             "N20 is closed. The approach ADASA accepted in the RFI-002 reply — SS316L "
             "exterior with galvanised or mill-finish internal mounting components, "
             "provided NEMA 4X is maintained — is correctly reflected, and those "
             "internal components are not reopened. BW Water's comment sheet on sheet 14 "
             "commits to re-issuing the Single Line Diagram to read \"SS316L Panel, "
             "NEMA 4X/IP66\"; that update is tracked in Section 3."),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new revision required:", {"bold": True}),
             (" confirm the cable-clamp diameter (OBS-01), reword the MATERIAL row "
              "(OBS-02) and correct the two descriptions (OBS-03) when issuing Rev 0. "
              "The enclosure specification is accepted as coherent with the approved "
              "LCP Datasheet and Single Line Diagram.",)],
        ],
    ),
    dict(
        heading="PLC/LCP FAT Procedure - Hardware Rev A — P22-PP-09-000-001",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" This first-issue hardware FAT procedure covers the panel completely and "
             "soundly: dimensional and material verification against the approved "
             "drawings, earth continuity at 0.1 ohm per connection, insulation "
             "resistance at 100 megohm and 500 VDC with the electronics disconnected, "
             "AC and DC distribution, the VFD1 (93 kW, RO HP Feed Pump) and VFD2 "
             "(11 kW, CIP Pump) functional and protection tests, the full PLC static "
             "I/O wiring test channel by channel, and the HMI, network and gateway "
             "checks. The coverage matches what the Technical Specification requires: "
             "the four hardwired relay-contact signals to the plant control system "
             "(system enable, running, fault and local/remote), the Pt-100 winding and "
             "bearing elements on both motors per the Technical Specification "
             "(P22-ET-09-000-001-0), Section 5.3 - Electrical Motors, and the vibration "
             "transmitters. The VFD ratings match the Electrical Load List, and the "
             "material checks reflect the resolved SS316L / NEMA 4X enclosure. Four "
             "documentary items remain on the procedure itself. Annotations on "
             "P22-PP-09-000-001_A_FAT_Procedure_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MAJOR",
             "The Reference Documents table and the Drawing Reference cite the "
             "governing drawings under the wrong code — \"P22-ET-09-008-001\" for the "
             "Outline Panel Drawing and \"P22-ET-09-008-002\" for the Schematic "
             "Diagram. The Outline is P22-CD-09-008-001 (the Rev C in this submittal) "
             "and the Schematic is P22-CD-09-008-002; P22-ET-09-008-001 is a different, "
             "real document, the PLC and HMI Panel Component Datasheet. A controlled "
             "test procedure must point its witnesses to the correct governing "
             "drawings. Correct the two references."),
            ("OBS-02", "MINOR",
             "The AO Channel 3 tag for the Antiscalant Dosing Pump 2 speed control "
             "reads \"BDS-09-001-SIC001\", the tag of Pump 1; the approved IO List "
             "assigns Pump 2 \"BDS-09-002-SIC001\". The project information block also "
             "states the document number as \"P22-PP-000-001\", missing the area "
             "segment (P22-PP-09-000-001). Correct both."),
            ("OBS-03", "MINOR",
             "Two acceptance criteria do not match the approved documents. The "
             "mounting-plate material is written as hot-dip galvanised while the Outline "
             "Rev C specifies zinc-plated (both acceptable internal finishes, but the "
             "criterion should match the drawing), and the Antiscalant Dosing Pump "
             "running signals are tested as hardwired digital inputs while the approved "
             "IO List defines them as soft signals over Ethernet/IP, the field scheme "
             "accepted at Transmittal N20. Reconcile the procedure with the approved IO "
             "List; no change of signal type is required."),
            ("NOTE-01", "NOTE",
             "The FAT methodology, acceptance criteria and I/O coverage are complete "
             "and consistent with the approved IO List and the Technical Specification. "
             "No functional gap is raised."),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new revision required:", {"bold": True}),
             (" correct the governing-drawing references (OBS-01), the analogue-output "
              "tag and document number (OBS-02), and the two acceptance criteria so "
              "they match the approved documents (OBS-03).",)],
        ],
    ),
    dict(
        heading="Operating and Maintenance Manual Rev A — P22-BA-09-000-012",
        code="Response Code: 2 — Approved as Noted",
        status=[
            ("Status.", {"bold": True}),
            (" This first-issue operating and maintenance manual carries the "
             "project-specific content correctly: the six-by-four vessel array with "
             "seven elements each (70 membranes), consistent with the offer and with "
             "the hydrostatic test report; the feed and operating pressures (about 52 "
             "to 55 bar at the high-pressure pump discharge, with the turbochargers "
             "providing the interstage boost); the 42.86 per cent recovery; the "
             "control-sequence matrix for service, shutdown and CIP; the cleaning "
             "chemistry; and the equipment tags. The installation, membrane-loading and "
             "cartridge-loading procedures are complete. Three content items and some "
             "generic template language remain to tidy. Annotations on "
             "P22-BA-09-000-012_A_OM_Manual_CC_ADASA.pdf.",),
        ],
        obs=[
            ("OBS-01", "MINOR",
             "The CIP Procedures subsection (4.3.5) is a generic five-step infographic "
             "that neither references the detailed CIP matrices in the Control Sequence "
             "(section 4.4), where the acid and caustic wash steps, setpoints and "
             "recirculation actually live, nor states the recipe basis. Link the "
             "subsection to the control-sequence matrices and state the acid and "
             "caustic wash basis and the governing pH and temperature setpoints."),
            ("OBS-02", "MINOR",
             "The recovery rate is given as 42 per cent in the process description and "
             "42.86 per cent in the control sequence; the offer fixes 42.85 to 42.86 "
             "per cent. Align the process description."),
            ("OBS-03", "MINOR",
             "Table 2.1 assigns the first-stage membrane as \"LG SW 400 SR\" and the "
             "second stage as \"LG SW 400 R G2 UHP\". Confirm the first-stage element "
             "against the approved LG membrane datasheet."),
            ("NOTE-01", "NOTE",
             "The manual carries generic template language that misdescribes the "
             "service (\"potable, industrial and wastewater reuse applications\", "
             "\"PASS RO unit\"). The project-specific technical content is present and "
             "correct; the boilerplate is to be cleaned at issue."),
        ],
        action_paras=[
            [("Action to issue at IFC Rev 0 — no new revision required:", {"bold": True}),
             (" link and complete the CIP procedures subsection (OBS-01), align the "
              "recovery figure (OBS-02), confirm the first-stage membrane model "
              "(OBS-03) and clean the generic template language (NOTE-01).",)],
        ],
    ),
]

ADDRESSED_TEXT = (
    "The Painting Procedure returns at Rev B — the item open since Transmittal N23 — "
    "and closes, so that with the NDE Plan (closed at Transmittal N26) three of the "
    "four quality and fabrication procedures opened at Transmittal N23 are now at "
    "IFC; only the HP and LP Pressure Test Procedure remains. The RO Vessel "
    "Hydrostatic Test Procedure, the fourth, returns at Rev C and closes its critical "
    "observation: the attached report evidences the vessels were tested at 1.1 times "
    "their design pressures, and it is approved as noted. The PLC/LCP Outline Panel "
    "Drawing returns at Rev C and resolves the enclosure gate open since Transmittal "
    "N20, re-issued at the SS316L / NEMA 4X configuration settled in the RFI-002 "
    "reply; panel fabrication release is no longer gated on the enclosure. The Jotun "
    "make stays substantiated and is not reopened; the 4-20 mA plus HART point stays "
    "satisfied at the instrument level; the ASME stamp remains waived; the soft-I/O "
    "field scheme over Ethernet/IP accepted at Transmittal N20 is not reopened."
)

PENDING_OPEN = [
    ("TM N22 Section 2.1",
     "Plant Control Philosophy children: Operating Sequence Charts "
     "(P22-LI-09-008-017), Alarm and Control Setpoint List (P22-LI-09-008-015) and "
     "Control Matrix",
     "The operative numerical control logic remains in child documents not delivered; "
     "it gates the IO List reaching issue for construction",
     "OPEN and overdue: not delivered by the 10-Jul-2026 deadline; the seventh cycle "
     "with that logic outside the package"),
    ("TM N26 Section 2.6",
     "UHPRO Structural Calculation Report (P22-CD-09-005-001)",
     "The base-bolt design omits the main process equipment — high-pressure pump, "
     "turbochargers, RO cartridge filter and RO pressure vessels — all carried as "
     "seismic mass in the model. This report also governs the anchor reaction forces of "
     "the Antiscalant Dosing Pump Skid and the NCh 2369 anchor loads of the CIP "
     "Flushing Tank and the Antiscalant Dosing Tank",
     "OPEN: to re-issue as Rev B; no new revision in this delivery"),
    ("TM N26 Section 2.8",
     "GA of Antiscalant Dosing Tank (P22-DWG-09-005-015)",
     "The NCh 2369 anchor-bolt loads and qualification are still deferred",
     "OPEN: to re-issue as Rev C; no new revision in this delivery"),
    ("TM N22 Section 2.2",
     "Equipment Layout (P22-DWG-09-005-003)",
     "The RO Cartridge Filter is still drawn horizontal against its own vertical "
     "datasheet",
     "OPEN: to re-issue as Rev D; no new revision in this delivery"),
    ("TM N4 NOTE-05",
     "HMI Screenshots (P22-BREAD-09-008-001)",
     "Committed at Transmittal N4, never submitted — the oldest open commitment in the "
     "project",
     "OPEN: not delivered"),
]

OVERDUE = [
    "Grounding Point and Power Panel Location Layout Rev F — committed for "
    "17-Jun-2026, escalated to 10-Jul-2026, not delivered.",
    "FAT and SAT comparison table — committed for 15-Jun-2026, escalated to "
    "10-Jul-2026, not delivered.",
    "The three mechanical installation-route plans (Maintenance Lifting Points, 3D "
    "Model, GA RO HP Pump) — committed for 26-Jun-2026, escalated to 10-Jul-2026, not "
    "delivered.",
    "The Plant Control Philosophy children — escalated to 10-Jul-2026, not delivered.",
]

CROSS_DOC = [
    "Line List (P22-LI-09-009-003): re-issue with the RO Brine Discharge line "
    "reconciled and transmit it for record, since it is the document that fixes the "
    "test pressure of the HP and LP Pressure Test Procedure (Section 2.1, OBS-01 and "
    "OBS-02).",
    "Single Line Diagram: BW Water's comment sheet on the Outline drawing commits to "
    "re-issuing it to read \"SS316L Panel, NEMA 4X/IP66\", aligning it with the "
    "accepted enclosure; transmit the revised Single Line Diagram for record.",
    "Container base-bolt interface: the tension and shear demands at the container "
    "base, required as input to the OOCC foundation design, tracked since Transmittal "
    "N26 and not delivered.",
    "Module Seismic Calculation Report: the endorsed report backing the anchor reaction "
    "forces used by the equipment general arrangements, governed by the Structural "
    "Calculation Report and not delivered.",
]

ATTACHMENTS = [
    ("HP and LP Pressure Test Procedure Rev C", "Code 3",
     "P22-BA-09-000-010_C_HP_LP_Pressure_Test_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01"),
    ("RO Vessel Hydrostatic Test Procedure Rev C", "Code 2",
     "P22-BA-09-000-009_C_RO_Vessel_Hydrostatic_CC_ADASA.pdf",
     "OBS-01, OBS-02, NOTE-01"),
    ("Painting Procedure Rev B", "Code 2",
     "P22-BA-09-000-011_B_Painting_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01, NOTE-02"),
    ("PLC/LCP Outline Panel Drawing Rev C", "Code 2",
     "P22-CD-09-008-001_C_Outline_Panel_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01"),
    ("PLC/LCP FAT Procedure - Hardware Rev A", "Code 2",
     "P22-PP-09-000-001_A_FAT_Procedure_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01"),
    ("Operating and Maintenance Manual Rev A", "Code 2",
     "P22-BA-09-000-012_A_OM_Manual_CC_ADASA.pdf",
     "OBS-01, OBS-02, OBS-03, NOTE-01"),
]

RESPONSE_SUMMARY = [
    ("P22-BA-09-000-010", "HP and LP Pressure Test Procedure", "C",
     "3 — To Be Revised"),
    ("P22-BA-09-000-009", "RO Vessel Hydrostatic Test Procedure", "C",
     "2 — Approved as Noted"),
    ("P22-BA-09-000-011", "Painting Procedure", "B", "2 — Approved as Noted"),
    ("P22-CD-09-008-001", "PLC/LCP Outline Panel Drawing", "C",
     "2 — Approved as Noted"),
    ("P22-PP-09-000-001", "PLC/LCP FAT Procedure - Hardware", "A",
     "2 — Approved as Noted"),
    ("P22-BA-09-000-012", "Operating and Maintenance Manual", "A",
     "2 — Approved as Noted"),
]


def main() -> None:
    if DOWNLOAD_LINK.startswith("PENDIENTE"):
        print("AVISO: DOWNLOAD_LINK sin definir — reemplazar antes de emitir.")

    crear_documento_adasa(
        titulo=("TECHNICAL REVIEW TRANSMITTAL N27 — SECOND STAGE RO "
                "BRINE MODULE"),
        codigo="P22-TM-09-000-027-0",
        output_filename=OUTPUT,
        incluir_toc=True,
    )

    doc = Document(OUTPUT)

    # 1. EXECUTIVE SUMMARY
    doc.add_heading("EXECUTIVE SUMMARY", level=1)
    add_para(doc, [
        ("TRANSMITTAL VERDICT: 3 — To Be Revised.", {"bold": True}),
        (" Six documents across two submittals (25007-0063 and 25007-0064). Tally: 5 "
         "Code 2, 1 Code 3. The single Code 3 is the HP and LP Pressure Test "
         "Procedure, whose attached Line List orders a 75 bar hydrostatic test on a "
         "PVC line rated far below that pressure. The other five are approved as noted, "
         "and two of them close gates open for months: the RO Vessel Hydrostatic Test "
         "Procedure now carries the actual test report at the correct pressures, and "
         "the PLC/LCP Outline Panel Drawing re-issues at the SS316L / NEMA 4X enclosure "
         "settled in the RFI-002 reply.",),
    ])
    add_para(doc, [("Disposition at a glance:", {"bold": True})])
    add_bullet(doc,
               "HP and LP Pressure Test Procedure Rev C — Code 3. The attached Line "
               "List carries an unsafe test pressure and no approved revision status.")
    add_bullet(doc,
               "RO Vessel Hydrostatic Test Procedure Rev C — Code 2. The 45.5 bar "
               "error is gone; the attached report evidences testing at 1,320 and "
               "1,980 psi (1.1 times design). The body should still carry the binding "
               "pressures.")
    add_bullet(doc,
               "Painting Procedure Rev B — Code 2. Coating system and marine "
               "durability substantiated; three entries on the inspection form remain "
               "to be corrected at issue.")
    add_bullet(doc,
               "PLC/LCP Outline Panel Drawing Rev C — Code 2. Enclosure gate resolved "
               "per RFI-002 (SS316L exterior, NEMA 4X and IP66); minor field and "
               "wording corrections remain.")
    add_bullet(doc,
               "PLC/LCP FAT Procedure - Hardware Rev A — Code 2. Complete and sound "
               "hardware FAT; the governing drawings are cited under the wrong document "
               "code.")
    add_bullet(doc,
               "Operating and Maintenance Manual Rev A — Code 2. Serviceable first "
               "issue; the CIP subsection, a recovery figure and a membrane model to "
               "reconcile.")
    add_para(doc, [
        ("Why Code 3 — HP and LP Pressure Test Procedure:", {"bold": True}),
        (" Rev C answers the Transmittal N26 observation by attaching the Line List "
         "rather than writing the pressure in the body, so that attachment is now the "
         "instruction the shop follows. It sets line DA-PVC-DN65-09-016 (RO Brine "
         "Discharge, PVC Schedule 80, DN65, operating at 1 bar) at a 50 bar design "
         "pressure, and its hydrostatic column duly orders 75 bar. A PVC Schedule 80 "
         "line with Class 150 flanges withstands nothing close to that at the 45 degree "
         "Celsius design temperature the same list assigns it: a shop testing to this "
         "instruction would rupture the line. The 50 bar design value comes across from "
         "Line List Rev C, which ADASA approved at Transmittal N18; the hydrostatic "
         "column added in this attachment is the change that converts it into an "
         "executable test pressure. The attachment also carries no approved status. It "
         "is labelled Rev 0, a revision never transmitted, while the approved Rev C has "
         "no hydrostatic column at all, leaving the pressure the inspector would sign "
         "against without an approved source.",),
    ])
    add_para(doc, [
        ("Two long-standing items close in this transmittal. The RO Vessel Hydrostatic "
         "Test Procedure, the test for which the ASME code stamp was waived, now "
         "attaches the 17-Jun report evidencing the vessels were tested at 1.1 times "
         "their design pressures; and the PLC/LCP Outline Panel Drawing re-issues at "
         "the enclosure configuration settled in the RFI-002 reply, releasing the panel "
         "fabrication gate held since Transmittal N20.",)])
    add_para(doc, [
        ("Section 3 details the open and overdue inventory that these two submittals "
         "did not close.",)])

    # 2. OBSERVATIONS BY DOCUMENT
    doc.add_heading("OBSERVATIONS BY DOCUMENT", level=1)
    for sec in SECTIONS:
        doc.add_heading(sec["heading"], level=2)
        add_para(doc, [(sec["code"], {"bold": True})])
        add_para(doc, sec["status"])
        if sec.get("obs"):
            add_simple_table(
                doc, [("ID", "Severity", "Topic")] + list(sec["obs"]))
        for ap in sec["action_paras"]:
            add_para(doc, ap)

    # 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS
    doc.add_heading(
        "PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS", level=1)
    add_para(doc, [("These submittals delivered E63 and E64.",)])
    add_para(doc, [
        ("Addressed in this transmittal: ", {"bold": True}),
        (ADDRESSED_TEXT,)])
    add_para(doc, [
        ("Open from previous transmittals — the most serious:", {"bold": True})])
    add_simple_table(doc, [
        ("Origin TM", "Document", "Observation", "Status")] + PENDING_OPEN)
    add_para(doc, [
        ("Overdue deliverables (today is 13-Jul-2026):", {"bold": True})])
    for txt in OVERDUE:
        add_bullet(doc, txt)
    add_para(doc, [("Cross-document deliverables:", {"bold": True})])
    for txt in CROSS_DOC:
        add_bullet(doc, txt)

    # 4. ATTACHMENTS
    doc.add_heading("ATTACHMENTS", level=1)
    add_simple_table(
        doc,
        [("Document", "Verdict", "Annotated File", "Annotations")]
        + ATTACHMENTS)
    add_para(doc, [(
        "All six documents carry annotated PDFs (1 Code 3 and 5 Code 2). No document "
        "in these submittals is Code 1 — Approved.",)])
    dl = doc.add_paragraph()
    dl.add_run("Download — this transmittal and the six annotated PDFs: ").bold = True
    aplicar_arial_12(dl)
    add_hyperlink(dl, DOWNLOAD_LINK, DOWNLOAD_LINK)

    # 5. RESPONSE SUMMARY
    doc.add_heading("RESPONSE SUMMARY", level=1)
    add_simple_table(
        doc,
        [("Document Code", "Title", "Rev", "Response Code")]
        + RESPONSE_SUMMARY)
    add_para(doc, [
        ("Overall Transmittal Verdict: 3 — TO BE REVISED.", {"bold": True}),
        (" Tally: 5 Code 2, 1 Code 3. The verdict rests on the one Code 3, the HP and "
         "LP Pressure Test Procedure, whose attached Line List orders 75 bar on a PVC "
         "line and carries no approved revision status. The other five documents are "
         "approved as noted and issue directly at IFC Rev 0 with the corrections of "
         "Section 2 incorporated; among them, the RO Vessel Hydrostatic Test Procedure "
         "and the PLC/LCP Outline Panel Drawing close the ASME-waived vessel test and "
         "the enclosure fabrication gate respectively. Documents not appearing in this "
         "response are unaffected by this transmittal.",),
    ])

    doc.save(OUTPUT)
    print(f"Documento generado: {OUTPUT}")


if __name__ == "__main__":
    main()
