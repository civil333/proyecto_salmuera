#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n35.py

Actualiza el Master Deliverable Register con el Transmittal N35
(P22-TM-09-000-035-0), submittal 25007-0081 (ENTREGA 81), recibido el jueves
20-Ago-2026.

Idempotente: si existe el backup _pre-N35.xlsx, restaura SRC desde ese backup
antes de aplicar. Re-correr el script es seguro.

VEREDICTO GLOBAL: 3 - To be revised. Recuento del transmittal: 2 Codigo 1, 3
Codigo 3. Cinco re-revisiones, ningun item nuevo.

Filas que se tocan, todas ya existentes en el register:
    #105  HP and LP Pressure Test Procedure   P22-BA-09-000-010  (Rev 0 -> 1, sin codigo -> 1-Approved)
    #106  Painting Procedure                  P22-BA-09-000-011  (Rev 0 -> 1, sin codigo -> 1-Approved)
    #115  Liquid Penetrant Examination Proc.  P22-BA-09-000-014  (Rev A -> B, 3 -> 3)
    #116  Radiography Examination Procedure   P22-BA-09-000-015  (Rev A -> B, 3 -> 3)
    #117  Ultrasonic Thickness Procedure      P22-BA-09-000-016  (Rev A -> B, 3 -> 3)

EFECTO SOBRE EL TALLY: los dos documentos que estaban SIN CODIGO pasan a Codigo 1
y los tres Codigo 3 se mantienen. Partiendo del cierre del N34 (58 Codigo 1 / 22
Codigo 2 / 7 Codigo 3 / 0 Codigo 4 mas dos sin codigo), el tally esperado tras el
N35 es 60 / 22 / 7 / 0 y CERO sin codigo. El Summary se recomputa desde el Master
Register y no se hardcodea: contrastar contra ese numero al correr.

REGLA DE ALCANCE del N35, fijada por el usuario: los documentos que llegan por
sobre la Rev 0 ya estan emitidos para construccion, de modo que la revision
verifica si los comentarios previos cerraron y no introduce observaciones nuevas.
El mismo alcance se extendio a los tres procedimientos en Rev B.

CORRER DESPUES DE ENVIAR el transmittal, no antes.

El bloque ITEMS BY SECTION arrastra un descuadre heredado de un entregado de mas.
El updater lo reporta en cada corrida y no lo agranda.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N35.xlsx")

TM = "N35"
TM_DATE = "20-Aug-2026"

MR_UPDATES = {
    "P22-BA-09-000-010": dict(
        rev="1", delivery="E81", tm=TM, verdict="1-Approved",
        action=(
            "Rev 1 delivered (E81, 20-Aug-2026, submittal 25007-0081). Code 1 - Approved "
            "(TM N35). Reviewed ONLY against the single point TM N32 raised on the Rev 0, "
            "which had been returned without a response code. That point is closed on "
            "this document: form AQ-QAM-F018, Pressure and Leak Test Report, Rev 4 is now "
            "attached as page 11 of the procedure, blank and identified, restoring the "
            "form present in Rev C and absent since Rev D. The hydrostatic inspection of "
            "20 August confirms it in use: both test records of that day were raised on "
            "this form. One element of the certificate lives in ANOTHER document and "
            "therefore does not degrade this one: rows 5.1 and 5.2 of the ITP "
            "(P22-BA-09-000-004) Rev 0 require a pressure against time graphic as the "
            "certificate of a hold point, and AQ-QAM-F018 records point values. The "
            "graphic IS produced, on a Pressure Test Record Chart that carries no "
            "document number and no revision and that this procedure neither identifies "
            "nor incorporates. Tracked in Section 3 of the transmittal and pursued "
            "through the inspection channel. No annotated PDF (Code 1)."),
    ),
    "P22-BA-09-000-011": dict(
        rev="1", delivery="E81", tm=TM, verdict="1-Approved",
        action=(
            "Rev 1 delivered (E81, 20-Aug-2026, submittal 25007-0081). Code 1 - Approved "
            "(TM N35). Reviewed ONLY against the condition TM N32 set on the Rev 0, which "
            "had been returned without a response code. The condition is met: the Colour "
            "row of the inspection form now reads RAL 5012 Luminous Blue for the third "
            "coat, consistent with page 9 of the procedure and with the Painting "
            "Specification (P22-ET-09-006-002) Rev C approved at Code 1. The anchor "
            "profile remains 50 to 80 micrometres in both rows and the product of each "
            "coat is stated. The nominal thickness per coat is still not printed on the "
            "blank form; TM N32 recorded expressly that this is NOT a condition, and "
            "ADASA does not reopen it. ADASA action, not a supplier observation: the "
            "third-party inspection package needs this Rev 1 in place of the superseded "
            "copy. No annotated PDF (Code 1)."),
    ),
    "P22-BA-09-000-014": dict(
        rev="B", delivery="E81", tm=TM, verdict="3-To be revised",
        action=(
            "Rev B delivered (E81, 20-Aug-2026, submittal 25007-0081). Code 3 - To be "
            "revised (TM N35). Re-issued WITHOUT a consolidated comment sheet, so closure "
            "was verified by comparing the text of Rev A against Rev B: eleven lines "
            "changed in the whole document. OBS-01 of TM N32 closes only in part - ASME "
            "B31.3 was added to clause 13.0 but Appendix 6 of ASME Section VIII Div. 1 "
            "was left in place beside it, so the clause offers two criteria and names "
            "neither as governing, and para. 341.3.2 is not cited by number. OBS-02 is "
            "UNCHANGED: the report form still declares Appendix 8. None of the three "
            "tidying items was attended. ADASA states expressly that the thresholds of "
            "the added B31.3 text match those of Appendix 6 digit for digit, so no "
            "examination result turns on the choice; what turns on it is the code the "
            "record cites when it enters the fabrication dossier. Re-issue as Rev C with "
            "the comment sheet. Annotated PDF issued."),
    ),
    "P22-BA-09-000-015": dict(
        rev="B", delivery="E81", tm=TM, verdict="3-To be revised",
        action=(
            "Rev B delivered (E81, 20-Aug-2026, submittal 25007-0081). Code 3 - To be "
            "revised (TM N35). Re-issued WITHOUT a consolidated comment sheet; two "
            "changes of content in the whole document. OBS-01 of TM N32 closes in part: "
            "Table 341.3.2-1 of ASME B31.3 2024 IS now attached in full as a new page of "
            "the annex, verified by render at 200 dpi because it enters as an image and "
            "does not appear in the text extraction. Clause 23.0 nonetheless keeps the "
            "list of five codes and only adds a parenthesis pointing to that page. OBS-02 "
            "is UNCHANGED and governs the code: clause 12.1 still states 1.8 mm, which is "
            "the PW-51.1 dispensation of ASME Section I for PP-stamped power piping. This "
            "module is process piping to B31.3, whose para. 344.5.1 refers radiography "
            "wholly to Section V, Article 2; for the DN65, DN80 and DN100 lines of ASTM "
            "A790 UNS S32750 that carry 10 per cent RT, 6.02 to 8.56 mm of wall, T-274 "
            "requires 0.020 in. Re-issue as Rev C with the comment sheet. Annotated PDF "
            "issued."),
    ),
    "P22-BA-09-000-016": dict(
        rev="B", delivery="E81", tm=TM, verdict="3-To be revised",
        action=(
            "Rev B delivered (E81, 20-Aug-2026, submittal 25007-0081). Code 3 - To be "
            "revised (TM N35). Re-issued WITHOUT a consolidated comment sheet. This is "
            "the document that changed most of the three, with nine changes of content, "
            "and OBS-02 of TM N32 CLOSES: the scope, the calibration block of clause 4.1 "
            "and Appendix 1 all declare UNS S32750, where Rev A was written for carbon "
            "steel. OBS-01 does not close and governs the code: clause 9.0 moved from "
            "acceptance at the discretion of the client to acceptance per ASME Section "
            "II, SA-790, which is the MATERIAL specification of the pipe and not a "
            "thickness criterion. The NDE Plan (P22-BA-09-000-005) Rev C, approved at "
            "Code 1, requires the measured thickness to be equal to or greater than the "
            "minimum required thickness of the design code and the engineering "
            "calculation, and that comparison is absent. Residuals that do not hold the "
            "re-issue: the sound velocity is not stated as a value, S32250 is not a UNS "
            "designation, and the report form still declares Wallpaper Paste. OBS-03, the "
            "measurement point drawing of ITP row 7.8, carries its own date and was never "
            "a condition of Rev B. Re-issue as Rev C with the comment sheet. Annotated "
            "PDF issued."),
    ),
}

MR_NEW = []

RH_NEW = [
    (None, "HP and LP Pressure Test Procedure", "P22-BA-09-000-010", "1", "E81",
     "25007-0081", "1-Approved",
     "The single TM N32 point closes on this document: form AQ-QAM-F018 Rev 4 is attached "
     "as page 11, restoring the form absent since Rev D, and the inspection of 20 August "
     "confirms it in use. What remains is the Pressure Test Record Chart, an unidentified "
     "form outside this document, tracked in Section 3."),
    (None, "Painting Procedure", "P22-BA-09-000-011", "1", "E81",
     "25007-0081", "1-Approved",
     "The condition of TM N32 is met: the Colour row of the inspection form reads RAL "
     "5012 Luminous Blue, consistent with the body and with the approved Painting "
     "Specification Rev C. The anchor profile stays unified at 50 to 80 micrometres. The "
     "nominal thickness per coat was expressly declared not a condition."),
    (None, "Liquid Penetrant Examination Procedure", "P22-BA-09-000-014", "B", "E81",
     "25007-0081", "3-To be revised",
     "Re-issued without a comment sheet; eleven lines changed. B31.3 was added to clause "
     "13.0 without removing Appendix 6, and the report form still declares Appendix 8, "
     "unchanged. The thresholds coincide digit for digit, so the defect is the code the "
     "dossier record will cite, not the examination result."),
    (None, "Radiography Examination Procedure", "P22-BA-09-000-015", "B", "E81",
     "25007-0081", "3-To be revised",
     "Re-issued without a comment sheet; two changes. Table 341.3.2-1 is now attached in "
     "full, verified by render. The driver is clause 12.1, untouched: 1.8 mm is the "
     "Section I dispensation for PP-stamped power piping, where T-274 requires 0.020 in. "
     "for the 6.02 to 8.56 mm wall radiographed here."),
    (None, "Ultrasonic Thickness Procedure", "P22-BA-09-000-016", "B", "E81",
     "25007-0081", "3-To be revised",
     "The document that changed most of the three, and its technique sheet closes: scope, "
     "calibration block and Appendix 1 now read UNS S32750. The driver is clause 9.0, "
     "which moved to SA-790, the material specification of the pipe, where the approved "
     "NDE Plan requires measured thickness against minimum required thickness."),
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
    C_NUM = hdr["#"]; C_CODE = hdr["Code / ET Reference"]
    C_REV = hdr["Rev"]; C_DEL = hdr["Delivery"]; C_TM = hdr["TM"]
    C_VER = hdr["Verdict"]; C_STA = hdr["Status"]; C_ACT = hdr["Action Required"]

    # 1) updates (5 re-revisiones)
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
        raise SystemExit(f"ERROR: codigos N34 no encontrados en Master Register: {missing}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 2) Revision History (5 filas nuevas)
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

    # 3) Summary: recomputar total/delivered + verdicts desde MR
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
    sm["B9"].value = "35 (N1 through N35 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "81 (E1 through E81; the submittal series has no missing numbers)"
    sm["B12"].value = "20-Aug-2026 (E81)"
    sm["B13"].value = "20-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 4) ITEMS BY SECTION: el N35 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N35 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    # El scratchpad es por equipo. En macOS se usa el temporal del sistema;
    # lo que importa es construir FUERA del volumen de red y verificar el zip
    # antes de copiar al destino, porque un guardado directo sobre SMB puede
    # dejar el .xlsx a medias.
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n35_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n35_build.xlsx")
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
