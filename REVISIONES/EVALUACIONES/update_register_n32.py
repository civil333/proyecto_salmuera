#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n32.py
Actualiza el Master Deliverable Register a TM N32 (ENTREGA 75, submittal
25007-0075, 7 documentos). Modelado en update_register_n29.py.

Idempotencia: el backup _pre-N32.xlsx conserva el estado LIMPIO N31
(51/29/5/0 + 1 sin codigo, 110 items / 86 delivered). Al re-correr, RESTAURA
SRC desde ese backup antes de aplicar.

Veredicto N32: 3 - To be revised. Tally 1 Code 1 + 3 Code 3 + 3 SIN CODIGO.

Decision del usuario: no se codifica 3 un documento que ADASA ya habia dispuesto
Codigo 2 y que el proveedor ya emitio a Rev 0 para construccion. Los tres que no
cerraron su condicion vuelven SIN CODIGO, como la Plant Control Philosophy del
N31. Los tres procedimientos de END no estan alcanzados: son primera emision.

  UPDATES (4 re-revisiones de filas existentes):
    #101 PMI Procedure                  P22-BA-09-000-006 (Rev A->0, 2-AN -> 1)
    #103 Visual Inspection Procedure    P22-BA-09-000-008 (Rev A->0, 2-AN -> 1)
    #105 HP and LP Pressure Test Proc.  P22-BA-09-000-010 (Rev D->0, 2-AN -> sin codigo)
    #106 Painting Procedure             P22-BA-09-000-011 (Rev B->0, 2-AN -> sin codigo)

  ITEMS NUEVOS (3 primeras emisiones, no existian en el registro):
    #115 Liquid Penetrant Examination Procedure  P22-BA-09-000-014 Rev A -> 3
    #116 Radiography Examination Procedure       P22-BA-09-000-015 Rev A -> 3
    #117 Ultrasonic Thickness Procedure          P22-BA-09-000-016 Rev A -> 3

Las tres nuevas pertenecen a la seccion 3 (FABRICATION & FAT), que sube de
12/9 a 15/12. Se agregan al final del Master Register, que es como el archivo
ya incorporo los items 113 y 114.

Tally esperado tras N32: 53 Code 1 / 25 Code 2 / 8 Code 3 / 0 Code 4 + 3 sin
codigo; 113 items / 89 delivered; 32 TMs / 75 entregas.

Nota de conteo de entregas: el submittal 25007-0073 (Alarm & Interlock List
Rev 0 y Control and Sequence Chart Rev 0, recibido el 11-Ago-2026) SI cuenta
como entrega recibida aunque quede fuera del alcance de este transmittal. Por
eso el contador pasa de 73 a 75 y no a 74.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N32.xlsx")

TM = "N32"
TM_DATE = "12-Aug-2026"

MR_UPDATES = {
    "P22-BA-09-000-006": dict(
        rev="0", delivery="E75", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 re-issued (E75, 11-Aug-2026). Code 1 - Approved (TM N32). BW Water "
            "answered both points ADASA raised: the project-applicability statement asked "
            "for at TM N20 is now in clause 2.0 of the cover section (10% of the super "
            "duplex HP piping components tested and witnessed by ADASA), and the acceptance "
            "basis asked for on 6 August is in the new clause 13.4, with the two refinery "
            "acceptance clauses deleted; the bolt and nut sampling of Appendix 1 rose from "
            "5% to 10% per lot for piping. Housekeeping tracked in Section 3 of the TM for "
            "the next natural issue: reconcile clauses 13.1 and 13.2 with 13.4, write the "
            "designation as UNS S32750, and align clause 8.1 and the heading of Appendix 1 "
            "with the extent the cover section already declares. Issue at IFC Rev 0."),
    ),
    "P22-BA-09-000-008": dict(
        rev="0", delivery="E75", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 re-issued (E75, 11-Aug-2026). Code 1 - Approved (TM N32). Closes the "
            "point raised on 6 August: clause 5.8.1 identifies form AQ-QAM-F020 Piping "
            "Fabrication Inspection Report (Steel) Rev. 0 and the form is now included in "
            "the procedure, which satisfies the visual report required at the witness point "
            "of row 3.2 of the ITP. Issue directly at IFC Rev 0."),
    ),
    "P22-BA-09-000-010": dict(
        rev="0", delivery="E75", tm=TM, verdict="No code issued",
        action=(
            "Rev 0 re-issued (E75, 11-Aug-2026) under the same revision letter as the Rev 0 "
            "of E71. Returned WITHOUT a response code (TM N32): approved as noted at TM N29 and issued at Rev 0 for construction. Of the two points raised on 6 August, "
            "the edition closed and the record form did not. Closed: clauses 5.5.2 and 5.6.3 "
            "now test to the ASME B31.3 2024 edition instead of to the latest edition. Open: "
            "clause 5.8.1 names a Pressure Test Report that is not part of the submittal and "
            "that no controlled form in the procedure produces, while row 5.2 of the ITP Rev "
            "0 requires a Pressure Test report with a pressure against time graphic as the "
            "certificate of a Hold Point, with the test on 13-14 August. Re-issue as Rev 1 "
            "identifying and attaching that form. No addenda exist for the editions cited - "
            "ASME Section V and ASME B31.3 publish complete editions on a two-year cycle - "
            "but errata are in force against both and take effect on the date posted, so the "
            "applicable errata are to be stated."),
    ),
    "P22-BA-09-000-011": dict(
        rev="0", delivery="E75", tm=TM, verdict="No code issued",
        action=(
            "Rev 0 re-issued (E75, 11-Aug-2026) under the same revision letter as the Rev 0 "
            "of E71. Returned WITHOUT a response code (TM N32): approved as noted at TM N27 and issued at Rev 0 for construction. The inspection form of Appendix A was "
            "completed with the product for each coat, which matches the body, and with the "
            "Colour row reading RAL 5010 Gentian Blue against RAL 5012 Luminous Blue in page "
            "9 of the same procedure and in the approved Painting Specification "
            "P22-ET-09-006-002 Rev C (item 4, frame support inside the container). Re-issue "
            "as Rev 1 with RAL 5012 on the form, and state which revision governs the "
            "painting preparation inspection of 13-14 August, since the third-party "
            "inspection package holds an earlier copy."),
    ),
}

# Items nuevos: primera emision de los tres procedimientos de ensayos no
# destructivos que el TM N30 pidio someter antes de iniciar la soldadura.
MR_NEW = [
    (115, "Liquid Penetrant Examination Procedure (PT)", "P22-BA-09-000-014", "A", "E75",
     TM, "3-To be revised", "Delivered",
     "Rev A delivered (E75, submittal 25007-0075, IFA), first issue in response to the "
     "request of TM N30 on the Dossier Index. Code 3 - To be revised (TM N32). Acceptance "
     "criteria are those of the pressure vessel code and the document states two different "
     "ones: clause 13.0 cites ASME Section VIII Div.1 Appendix 6, which is the MAGNETIC "
     "PARTICLE appendix and not the penetrant one, and the report form cites Appendix 8, "
     "which is the penetrant appendix of the same vessel code. The ET Section 8 and the "
     "approved NDE Plan Rev C both set ASME B31.3 para. 341.3.2. Also: cover purpose and "
     "document number describe a PMI procedure; the attached procedure alternates Rev.00 "
     "and Rev.01; the report form carries the job number, batch numbers and result of a "
     "different contract. Technique and personnel qualification are sound.",
     "ET Sec.8: records produced under an unapproved procedure are not admissible into the "
     "fabrication dossier"),
    (116, "Radiography Examination Procedure (RT)", "P22-BA-09-000-015", "A", "E75",
     TM, "3-To be revised", "Delivered",
     "Rev A delivered (E75, submittal 25007-0075, IFA), first issue in response to the "
     "request of TM N30 on the Dossier Index. Code 3 - To be revised (TM N32). Clause 23.0 "
     "gives a list of five codes without stating which governs, where the approved NDE Plan "
     "Rev C sets ASME B31.3 para. 341.3.2. Clause 12.1 fixes geometric unsharpness at 1.8 mm, "
     "which is NOT a row of T-274 but the dispensation of para. PW-51.1 of ASME Section I "
     "for PP (power piping, B31.1) stamped items; B31.3 grants no such dispensation, its "
     "para. 344.5.1 referring radiography wholly to Section V Article 2, where T-274 "
     "requires 0.020 in. for a wall under 2 in. The radiographed lines are DN65, DN80 and "
     "DN100 of the approved Line List, 6.02 to 8.56 mm of wall. Also: generic scope "
     "without the project material and thickness; cover purpose describes a PMI procedure "
     "and cites Article 9 where Article 2 applies; section numbering does not run. "
     "Technique, identification system, film densities and radiographer qualification "
     "(AELB) are adequate.",
     "ET Sec.8: records produced under an unapproved procedure are not admissible into the "
     "fabrication dossier"),
    (117, "Ultrasonic Thickness Procedure (UT)", "P22-BA-09-000-016", "A", "E75",
     TM, "3-To be revised", "Delivered",
     "Rev A delivered (E75, submittal 25007-0075, IFA), first issue in response to the "
     "request of TM N30 on the Dossier Index. Code 3 - To be revised (TM N32). The procedure "
     "has NO acceptance criterion: clause 9.0 leaves acceptance and rejection to the "
     "discretion of the client, where the approved NDE Plan Rev C sets measured thickness "
     "equal to or greater than the minimum required thickness of the design code and the "
     "engineering calculation. The technique sheet is written for carbon steel while the "
     "scope is UNS S32750; no measurement point drawing accompanies it, which row 7.8 of the "
     "ITP requires; the attached procedure cites the 2023 edition of ASME Section V against "
     "the 2025 of the cover and the in-service codes API 510/570/653; the report form "
     "belongs to a different contract (AIR RECEIVER VERTICAL, job XIYIN-UG230601).",
     "ET Sec.8: baseline thickness measurement is a witness point of row 7.8 of the ITP"),
]

RH_NEW = [
    (None, "PMI Procedure", "P22-BA-09-000-006", "0", "E75", "25007-0075",
     "1-Approved",
     "Rev 0 re-issued under the same revision letter. Code 1. Both points answered: project "
     "applicability in clause 2.0 of the cover section and acceptance basis in the new "
     "clause 13.4, with the refinery acceptance clauses deleted; bolt and nut sampling for "
     "piping raised from 5% to 10% per lot. Housekeeping to Section 3."),
    (None, "Visual Inspection Procedure (VT)", "P22-BA-09-000-008", "0", "E75",
     "25007-0075", "1-Approved",
     "Rev 0 re-issued. Code 1. Form AQ-QAM-F020 identified in clause 5.8.1 and included in "
     "the procedure, which satisfies the visual report of ITP row 3.2."),
    (None, "HP and LP Pressure Test Procedure", "P22-BA-09-000-010", "0", "E75",
     "25007-0075", "No code issued",
     "Rev 0 re-issued under the same revision letter. Returned without a response code: "
     "approved as noted at TM N29 and issued at Rev 0 for construction. Clauses 5.5.2 and "
     "5.6.3 now fix the ASME B31.3 2024 edition, which closes that point. Clause 5.8.1 "
     "still names a "
     "Pressure Test Report that no controlled form produces, against row 5.2 of the ITP, "
     "which requires a pressure against time graphic at a Hold Point. No addenda exist for "
     "the editions cited, but errata do and are to be stated."),
    (None, "Painting Procedure", "P22-BA-09-000-011", "0", "E75", "25007-0075",
     "No code issued",
     "Rev 0 re-issued under the same revision letter. Returned without a response code: "
     "approved as noted at TM N27 and issued at Rev 0 for construction. The inspection form "
     "was completed with RAL 5010 Gentian Blue against the RAL 5012 Luminous Blue of the "
     "body and of the approved Painting Specification Rev C, and still carries no nominal "
     "thickness per coat. Product per coat correct."),
    (None, "Liquid Penetrant Examination Procedure (PT)", "P22-BA-09-000-014", "A", "E75",
     "25007-0075", "3-To be revised",
     "First issue, in response to the TM N30 request. Code 3. Acceptance by pressure vessel "
     "code (Appendix 6 in the body, Appendix 8 on the form) instead of ASME B31.3 para. "
     "341.3.2; cover purpose and article wrong; revision index of the annex inconsistent; "
     "report form from another contract."),
    (None, "Radiography Examination Procedure (RT)", "P22-BA-09-000-015", "A", "E75",
     "25007-0075", "3-To be revised",
     "First issue, in response to the TM N30 request. Code 3. Acceptance given as a list of "
     "five codes; geometric unsharpness fixed at 1.8 mm, the ASME Section V limit for "
     "material over 4 in., against a wall of 3.7 to 11 mm that requires 0.020 in."),
    (None, "Ultrasonic Thickness Procedure (UT)", "P22-BA-09-000-016", "A", "E75",
     "25007-0075", "3-To be revised",
     "First issue, in response to the TM N30 request. Code 3. No acceptance criterion "
     "(left to the discretion of the client); technique sheet for carbon steel; no "
     "measurement point drawing per ITP row 7.8; report form from another contract."),
]


def style_row(ws, dst_row, ref_row, ncols):
    for c in range(1, ncols + 1):
        s = ws.cell(ref_row, c)
        d = ws.cell(dst_row, c)
        d._style = copy(s._style)


def main():
    if os.path.exists(BAK):
        shutil.copyfile(BAK, SRC)
        print(f"Restaurado SRC desde baseline limpio: {BAK}")
    else:
        shutil.copyfile(SRC, BAK)
        print(f"Baseline creado: {BAK}")

    wb = openpyxl.load_workbook(SRC)
    mr = wb["Master Register"]
    rh = wb["Revision History"]
    sm = wb["Summary"]

    ncols_mr = mr.max_column
    hdr = {mr.cell(1, c).value: c for c in range(1, ncols_mr + 1)}
    C_NUM = hdr["#"]; C_DOC = hdr["Document"]; C_CODE = hdr["Code / ET Reference"]
    C_REV = hdr["Rev"]; C_DEL = hdr["Delivery"]; C_TM = hdr["TM"]
    C_VER = hdr["Verdict"]; C_STA = hdr["Status"]; C_ACT = hdr["Action Required"]
    C_DDL = hdr.get("ET Deadline")

    # 1) updates (4 re-revisiones)
    seen = set()
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code in MR_UPDATES:
            u = MR_UPDATES[code]
            mr.cell(r, C_REV).value = u["rev"]
            mr.cell(r, C_DEL).value = u["delivery"]
            mr.cell(r, C_TM).value = u["tm"]
            mr.cell(r, C_VER).value = u["verdict"]
            mr.cell(r, C_STA).value = "Delivered"
            mr.cell(r, C_ACT).value = u["action"]
            seen.add(code)
            print(f"  MR update row {r}: {code} -> {u['verdict']} / {u['tm']} (Rev {u['rev']})")
    missing = set(MR_UPDATES) - seen
    if missing:
        raise SystemExit(f"ERROR: codigos N32 no encontrados en Master Register: {missing}")

    # 2) filas NUEVAS (3 primeras emisiones) al final, como los items 113 y 114
    existing = {str(mr.cell(r, C_CODE).value or "").strip()
                for r in range(2, mr.max_row + 1)}
    ref_row = mr.max_row
    for i, row in enumerate(MR_NEW, start=1):
        num, doc, code, rev, dele, tm, ver, sta, act, ddl = row
        if code in existing:
            raise SystemExit(f"ERROR: {code} ya existe en el Master Register; no se duplica.")
        dst = ref_row + i
        style_row(mr, dst, ref_row, ncols_mr)
        mr.cell(dst, C_NUM).value = num
        mr.cell(dst, C_DOC).value = doc
        mr.cell(dst, C_CODE).value = code
        mr.cell(dst, C_REV).value = rev
        mr.cell(dst, C_DEL).value = dele
        mr.cell(dst, C_TM).value = tm
        mr.cell(dst, C_VER).value = ver
        mr.cell(dst, C_STA).value = sta
        mr.cell(dst, C_ACT).value = act
        if C_DDL:
            mr.cell(dst, C_DDL).value = ddl
        print(f"  MR new row {dst}: #{num} {code} Rev {rev} -> {ver}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 3) Revision History (7 filas nuevas)
    rcols = rh.max_column
    rhh = {rh.cell(1, c).value: c for c in range(1, rcols + 1)}
    prior = collections.Counter(); rh_last = 1
    for r in range(2, rh.max_row + 1):
        cd = rh.cell(r, rhh["Code / ET Reference"]).value
        if cd:
            prior[str(cd).strip()] += 1; rh_last = r
    for i, row in enumerate(RH_NEW, start=1):
        dst = rh_last + i
        _num, doc, code, rev, dele, sub, ver, keyobs = row
        num = reg_num.get(code, "")
        cycle = prior[code] + 1; prior[code] += 1
        style_row(rh, dst, rh_last, rcols)
        rh.cell(dst, rhh["#"]).value = num
        rh.cell(dst, rhh["Document"]).value = doc
        rh.cell(dst, rhh["Code / ET Reference"]).value = code
        rh.cell(dst, rhh["Rev"]).value = rev
        rh.cell(dst, rhh["Delivery"]).value = dele
        rh.cell(dst, rhh["Submittal"]).value = sub
        rh.cell(dst, rhh["TM"]).value = TM
        rh.cell(dst, rhh["TM Date"]).value = TM_DATE
        rh.cell(dst, rhh["Verdict"]).value = ver
        rh.cell(dst, rhh["Cycle"]).value = cycle
        rh.cell(dst, rhh["Key Observations"]).value = keyobs
        print(f"  RH new row {dst}: #{num} {code} cycle {cycle} -> {ver}")

    # 4) Summary: recomputar total/delivered + verdicts desde MR
    stat = collections.Counter(); vd = collections.Counter(); total = 0
    for r in range(2, mr.max_row + 1):
        code = mr.cell(r, C_CODE).value
        if code and str(code).strip():
            total += 1
            su = str(mr.cell(r, C_STA).value or "").strip().upper()
            stat[su] += 1
            if su == "DELIVERED":
                vd[str(mr.cell(r, C_VER).value or "").strip()] += 1
    delivered = stat.get("DELIVERED", 0)
    not_delivered = stat.get("NOT DELIVERED", 0)
    partial = stat.get("PARTIAL", 0)
    print(f"  Summary recompute: total={total} delivered={delivered} "
          f"not_delivered={not_delivered} partial={partial} verdicts={dict(vd)}")

    sm["B4"].value = total
    sm["B5"].value = delivered
    sm["B7"].value = partial
    sm["B8"].value = not_delivered
    sm["B9"].value = "32 (N1 through N32 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "75 (E1 through E75)"
    sm["B12"].value = "12-Aug-2026 (E75)"
    sm["B13"].value = "12-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 5) ITEMS BY SECTION: los 3 items nuevos son de fabricacion y calidad,
    # misma familia que el PMI, el Visual y el ITP -> seccion 3 (fila 20).
    sm["B20"].value = 15
    sm["C20"].value = 12
    print("  ITEMS BY SECTION: seccion 3 FABRICATION & FAT 12/9 -> 15/12")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    scratch_dir = ("C:/Users/luisr/AppData/Local/Temp/claude/"
                   "C--SynologyDrive-SynologyDrive-DESAROLLO-PROYECTOS-CLAUDE-"
                   "MODULO-DE-SALMUERA-TALTAL/"
                   "d1666198-dddd-4b76-960f-85b08007e0c5/scratchpad")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n32_build.xlsx")
    wb.save(tmp)
    if zipfile.ZipFile(tmp).testzip() is not None:
        raise SystemExit("ERROR: el build en scratchpad salio corrupto.")
    openpyxl.load_workbook(tmp).close()
    print(f"Build verificado en scratchpad: {tmp}")
    for intento in range(1, 6):
        shutil.copyfile(tmp, dst)
        try:
            if zipfile.ZipFile(dst).testzip() is None:
                openpyxl.load_workbook(dst).close()
                print(f"Guardado y verificado en destino (intento {intento}): {dst}")
                return
        except Exception as e:
            print(f"  intento {intento}: destino aun corrupto ({e}); recopiando...")
    raise SystemExit(f"ERROR: no se pudo dejar copia integra. Build en {tmp}.")


if __name__ == "__main__":
    main()
