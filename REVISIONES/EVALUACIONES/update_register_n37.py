#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n37.py

Actualiza el Master Deliverable Register con el Transmittal N37
(P22-TM-09-000-037-0), emitido el 31-Ago-2026, submittals 25007-0086, 25007-0087 y 25007-0088
(ENTREGAS 86, 87 y 88), recibidas el 27 y el 28 de agosto de 2026.

Idempotente: si existe el backup _pre-N37.xlsx, restaura SRC desde ese backup
antes de aplicar. Re-correr el script es seguro.

VEREDICTO GLOBAL: 3 - To be revised. Recuento del transmittal: 2 Codigo 1,
4 Codigo 2 y 1 Codigo 3 sobre los SIETE documentos dispuestos. Siete
re-revisiones con veredicto, ningun item nuevo.

Filas que se tocan, todas ya existentes en el register:
    #115  Liquid Penetrant Examination Proc.  P22-BA-09-000-014  (Rev B -> C, 3 -> 2)
    #116  Radiography Examination Procedure   P22-BA-09-000-015  (Rev B -> C, 3 -> 2)
    #99   PLC/LCP Schematic Diagram           P22-CD-09-008-002  (Rev A -> B, 2 -> 2)
    #35   Instrument Location Layout          P22-DWG-09-008-001 (Rev C -> D, 3 -> 2)
    #31   I/O List                            P22-LI-09-008-001  (Rev 5 -> 6, 2 -> 1)
    #41   Tie-In Point Layout                 P22-DWG-09-005-005 (Rev B -> 0, 2 -> 1)
    #110  PLC/LCP FAT Procedure - Hardware    P22-PP-09-000-001  (Rev A -> B, 2 -> 3)

EFECTO SOBRE EL TALLY, declarado ANTES de correr. Partiendo del cierre del N36
(62 Codigo 1 / 21 Codigo 2 / 6 Codigo 3 / 0 Codigo 4), suben dos a Codigo 1 —la
I/O List y el Tie-In Point Layout, los dos emitidos para construccion—, tres
suben de Codigo 3 a Codigo 2 —los dos procedimientos de ensayos no destructivos
y el Instrument Location Layout— y uno baja de Codigo 2 a Codigo 3 —el registro
del FAT del tablero—. El tally esperado tras el N37 es 64 / 21 / 4 / 0.
Los cuatro Codigo 3 que quedan abiertos son el procedimiento de espesor por
ultrasonido, el O&M Manual, el indice del dossier y este registro del FAT.
El Summary se recomputa desde el Master Register y no se hardcodea: contrastar
contra ese numero al correr.

REGLA DE ALCANCE del N37. Los siete documentos responden a comentarios previos,
de modo que cada uno se revisa solo contra la instruccion escrita del transmittal
anterior. La columna de emision del Submittal Form decide el codigo: un documento
sometido para aprobacion reitera la condicion en Codigo 2, y uno emitido para
construccion queda en Codigo 1 o en Codigo 3, porque sobre un Rev 0 el Codigo 2
no tiene mecanismo.

EXCEPCION QUE HAY QUE ENTENDER, y por eso el FAT baja a Codigo 3 estando sometido
para aprobacion: la regla del Codigo 2 reiterado supone que la condicion vence al
emitir Rev 0. El TM N27 amarro la condicion de ESE documento a un hito distinto y
anterior, "before witnessing", y ese hito ocurrio: el ensayo corrio del 3 al 5 de
agosto sin incorporarlas.

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
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N37.xlsx")

TM = "N37"
TM_DATE = "31-Aug-2026"

# Tally esperado, declarado antes de correr (ver cabecera).
TALLY_ESPERADO = {"1-Approved": 64, "2-AN": 21, "3-To be revised": 4, "4-Rejected": 0}

MR_UPDATES = {
    "P22-BA-09-000-014": dict(
        rev="C", delivery="E86", tm=TM, verdict="2-AN",
        action=(
            "Rev C submitted for approval (E86, 27-Aug-2026, submittal 25007-0086). "
            "Code 2 - Approved as noted (TM N37), up from the Code 3 of TM N35. The "
            "determinant closed: clause 13.0 now offers a single acceptance criterion, "
            "ASME B31.3 para. 341.3.2 with its thresholds, the Section VIII Division 1 "
            "Appendix 6 block is gone, and the form the examiner signs declares that "
            "same criterion with its paragraph number, so the examiner no longer "
            "chooses. Open at Rev 0, on the document itself: the report form is "
            "unchanged from Rev B and still carries the report number and job number of "
            "another contract, three consumable batch numbers and an observations column "
            "pre-written with the result; the Procedure field inside that form still "
            "reads Rev.00; and page 2 still carries the document number of a positive "
            "material identification procedure. The report form is the second time it is "
            "raised, and the comment sheet answers Revised as per comment against a "
            "block that names it. Annotated PDF issued (OBS-01 to OBS-03, NOTE-01)."),
    ),
    "P22-BA-09-000-015": dict(
        rev="C", delivery="E86", tm=TM, verdict="2-AN",
        action=(
            "Rev C submitted for approval (E86, 27-Aug-2026, submittal 25007-0086). "
            "Code 2 - Approved as noted (TM N37), up from the Code 3 of TM N35. The "
            "determinant closed in both halves: the list of five acceptance codes in "
            "clause 23.0 came down to one, and the geometric unsharpness limit of 1.8 mm "
            "-the ASME Section I dispensation for PP-stamped power piping, which B31.3 "
            "does not grant- was replaced by the 0.020 in. of Table T-274 with its text "
            "reproduced in full in a new clause 13.0. Open at Rev 0, on the document "
            "itself: clause 1.0 still reads generically and names neither ASTM A790 UNS "
            "S32750 nor the 6.02 to 8.56 mm wall range radiographed on this module; the "
            "cover still carries the document number of a positive material "
            "identification procedure; and two internal cross-references were left "
            "behind by the renumbering. The comment sheet carries rows for OBS-01 and "
            "OBS-02 only, none for NOTE-01. Annotated PDF issued (OBS-01, NOTE-01 to "
            "NOTE-03)."),
    ),
    "P22-CD-09-008-002": dict(
        rev="B", delivery="E86", tm=TM, verdict="2-AN",
        action=(
            "Rev B submitted for approval (E86, 27-Aug-2026, submittal 25007-0086). "
            "Code 2 - Approved as noted (TM N37), second cycle on the single condition "
            "of TM N20. The reconciliation against the approved I/O List is nearly "
            "complete and was verified on the sheets, not on the declaration: the CIP "
            "heater output is wired on sheet 39 through relay KA8 on module -A4 output "
            "7, inputs 1 to 4 of sheet 35 are shown as spare consistent with the three "
            "rows deleted at Rev 6, and the air conditioning signals are on sheets 37 "
            "and 38. Open at Rev 0: CIP HEATER RUNNING, item 109 of the I/O List Rev 6, "
            "has no terminal on any of the four digital input sheets, nineteen inputs "
            "assigned against twenty active with thirteen free terminals; and the bill "
            "of material on sheet 28 still lists the operator terminal as "
            "2711P-T10C21D8S, which TM N30 named among the documents to correct after "
            "ADASA declared the 2711P-T10C22D9P binding. The comment sheet cites an I/O "
            "List Rev B that does not exist. Annotated PDF issued (OBS-01 to OBS-02, "
            "NOTE-01)."),
    ),
    "P22-DWG-09-008-001": dict(
        rev="D", delivery="E86", tm=TM, verdict="2-AN",
        action=(
            "Rev D submitted for approval (E86, 27-Aug-2026, submittal 25007-0086). "
            "Code 2 - Approved as noted (TM N37), up from the Code 3 carried since TM "
            "N23. The determinant closed: the geometry is now drawn against the "
            "Equipment Layout Rev D, which reached Code 1 at TM N33, and the title block "
            "code and the issue date are correct. Open at Rev 0, on the drawing itself "
            "and verified by render of the title block: the revision block carries four "
            "rows, D, C, B and A, all repeating the same description ISSUED FOR "
            "APPROVAL, so no row states what changed at its issue; the row of Rev C "
            "reads JUN.16.26 here and APR.17.26 on the drawing issued at Rev C, so the "
            "April issue was overwritten instead of a row being added and the two Rev C "
            "issues are still not distinguishable; and the declaration that the drawing "
            "follows the Equipment Layout Rev D lives only on the reply sheet, with the "
            "notes box of both sheets empty and no reference document list. The change "
            "notice column is not required: it is blank on the Equipment Layout as well. "
            "Annotated PDF issued (OBS-01 to OBS-02)."),
    ),
    "P22-LI-09-008-001": dict(
        rev="6", delivery="E86", tm=TM, verdict="1-Approved",
        action=(
            "Rev 6 delivered for construction (E86, 27-Aug-2026, submittal 25007-0086). "
            "Code 1 - Approved (TM N37). The single action of TM N28 closed and was "
            "verified on the list, not on the declaration: row 108 carries REL-09-001, "
            "HS001, CIP HEATER ON/OFF COMMAND as a dry contact output and row 109 "
            "carries REL-09-001, XB002, CIP HEATER RUNNING as the input in the opposite "
            "direction, both at revision 6. The list is issued for construction, so the "
            "condition fell due at this issue and there is no substantive defect against "
            "it. Related deliverable tracked in Section 3 of the transmittal, on other "
            "documents and not on this one: the running feedback this list now defines "
            "has no terminal on the schematic diagram, and the four digital inputs "
            "signed off on the panel test record are not the four this revision carries. "
            "No annotated PDF (Code 1)."),
    ),
    "P22-DWG-09-005-005": dict(
        rev="0", delivery="E87", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered for construction (E87, 27-Aug-2026, submittal 25007-0087). "
            "Code 1 - Approved (TM N37). The substantive point of TM N31 closed and was "
            "verified against the source: the tie-in schedule now carries a complete "
            "DESIGN PRESSURE column and the brine feed point TP-DA P8-001, 4 inch, class "
            "150 to ASME B16.5, is declared at 5 barG, which matches line "
            "DA-PVC-DN100-09-001 of the Line List Rev 0 approved at Code 1 in TM N29, so "
            "the ADASA acceptance of the ANSI 150 class is satisfied. The drawing is "
            "issued for construction and is not held. Two notes for the next natural "
            "issue, neither of which holds it: the reply states that TP-AS P11-001 is "
            "not a flanged connection and that the termination is the valve itself, and "
            "the sheet still shows two dashes and does not say it; and the DRAWING "
            "STATUS field reads ISSUED FOR APPROVAL while the revision row and the "
            "submittal form both read ISSUED FOR CONSTRUCTION. No annotated PDF "
            "(Code 1)."),
    ),
    "P22-PP-09-000-001": dict(
        rev="B", delivery="E88", tm=TM, verdict="3-To be revised",
        action=(
            "Rev B submitted for approval (E88, 28-Aug-2026, submittal 25007-0088). "
            "Code 3 - To be revised (TM N37). This revision is not a procedure: it is "
            "the completed record of the panel hardware test run on 3 to 5 August 2026 "
            "at the panel builder in Ningbo, submitted twenty-three days later. ADASA "
            "received no notice, against row 6.2 of the Inspection and Test Plan "
            "P22-BA-09-000-004 Rev 0 approved at Code 1, which assigns ADASA a witness "
            "point on the electrical test of panels and whose legend defines that point "
            "as requiring notification, and against row 7.1, a hold point on ADASA "
            "approval of the detailed test procedure. The Witnessed by (Client / "
            "Third-Party Inspector) box is signed by BW Water personnel and the Accepted "
            "by (BW Water) box by the panel supplier. Ten items are marked category A; "
            "eight of them, all raised by the BW Water engineer, carry target date, "
            "actual date and status blank, the closing block is empty, and an attached "
            "rectification report declares them done with photographs, unsigned, undated "
            "and unwitnessed. The reference document table cites two revisions that do "
            "not exist. Four digital inputs and the output relay map are stated three "
            "different ways across this record, the I/O List Rev 6 and the schematic "
            "Rev B. Five of six test instruments carry no model or serial number and "
            "none a calibration certificate, against safety requirement 3 of the "
            "document itself. Annotated PDF issued (OBS-01 to OBS-05, NOTE-01 to "
            "NOTE-02). Re-issue as Rev C."),
    ),
}

RH_NEW = [
    (None, "Liquid Penetrant Examination Procedure", "P22-BA-09-000-014", "C", "E86",
     "25007-0086", "2-AN",
     "Submitted for approval. The determinant closed: clause 13.0 and the examiner form "
     "now state ASME B31.3 para. 341.3.2 as the single criterion. Open: the report form "
     "is unchanged and still carries another contract, its Procedure field reads Rev.00, "
     "and page 2 keeps a PMI document number. Second cycle on the form."),
    (None, "Radiography Examination Procedure", "P22-BA-09-000-015", "C", "E86",
     "25007-0086", "2-AN",
     "Submitted for approval. The determinant closed in both halves: one acceptance "
     "criterion, and the 1.8 mm unsharpness limit replaced by the 0.020 in. of Table "
     "T-274. Open: the scope names neither the super duplex material nor the 6.02 to "
     "8.56 mm wall of this module, the cover keeps a PMI document number, and two "
     "cross-references were left behind by the renumbering."),
    (None, "PLC/LCP Schematic Diagram", "P22-CD-09-008-002", "B", "E86",
     "25007-0086", "2-AN",
     "Submitted for approval. Second cycle on the single condition of TM N20. The I/O "
     "reconciliation is nearly complete, verified on the sheets. Open: CIP HEATER "
     "RUNNING, item 109 of the I/O List Rev 6, has no terminal on any digital input "
     "sheet; and the bill of material still lists the operator terminal as the -D8S "
     "that TM N30 required corrected."),
    (None, "Instrument Location Layout", "P22-DWG-09-008-001", "D", "E86",
     "25007-0086", "2-AN",
     "Submitted for approval. Clears the Code 3 carried since TM N23: the geometry now "
     "follows the Equipment Layout Rev D, approved at Code 1 in TM N33. Open, verified "
     "by render: four revision rows all reading ISSUED FOR APPROVAL, the Rev C row "
     "rewritten from April to June, and the empty notes box that leaves the layout "
     "revision declared only on the reply sheet."),
    (None, "I/O List", "P22-LI-09-008-001", "6", "E86",
     "25007-0086", "1-Approved",
     "Issued for construction. The single action of TM N28 closed and was verified on "
     "the list: rows 108 and 109 carry the CIP heater command and its running feedback "
     "in both directions at revision 6. No substantive defect. What stays open lives on "
     "other documents and is tracked in Section 3."),
    (None, "Tie-In Point Layout", "P22-DWG-09-005-005", "0", "E87",
     "25007-0087", "1-Approved",
     "Issued for construction. The oldest open drawing of the package closes its "
     "substantive point: the brine feed tie-in is declared at 5 barG, matching the Line "
     "List Rev 0 approved at Code 1, so the ANSI 150 class acceptance is satisfied. Two "
     "notes for the next natural issue: the unflanged termination is answered on the "
     "reply and not on the sheet, and the title block still reads ISSUED FOR APPROVAL."),
    (None, "PLC/LCP FAT Procedure - Hardware", "P22-PP-09-000-001", "B", "E88",
     "25007-0088", "3-To be revised",
     "Submitted for approval and returned to revision. It is not a procedure but the "
     "completed record of the panel test run on 3 to 5 August in Ningbo without notice "
     "to ADASA, against the witness point of row 6.2 and the hold point of row 7.1 of "
     "the approved Inspection and Test Plan. Witnessed and accepted inside the supply "
     "chain. Eight category A punch items closed by nobody, two reference revisions "
     "that do not exist, and four digital inputs stated three different ways."),
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

    # 1) updates (7 re-revisiones)
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
        raise SystemExit(f"ERROR: codigos N37 no encontrados en Master Register: {missing}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 2) Revision History (7 filas nuevas)
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
        if mr.cell(r, C_CODE).value:
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

    # Gate: el tally se declara antes de correr y se contrasta aqui.
    real = {k: vd.get(k, 0) for k in TALLY_ESPERADO}
    if real != TALLY_ESPERADO:
        print(f"  🔴 TALLY DISTINTO DEL ESPERADO: esperado {TALLY_ESPERADO}, real {real}")
    else:
        print(f"  Tally coincide con lo declarado: {real}")

    sm["B4"].value = total
    sm["B5"].value = delivered
    sm["B7"].value = partial
    sm["B8"].value = not_delivered
    sm["B9"].value = "37 (N1 through N37 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "88 (E1 through E88; the submittal series has no missing numbers)"
    sm["B12"].value = "28-Aug-2026 (E88)"
    sm["B13"].value = "31-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 4) ITEMS BY SECTION: el N37 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N37 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n37_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n37_build.xlsx")
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
