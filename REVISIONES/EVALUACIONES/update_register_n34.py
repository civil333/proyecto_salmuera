#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n34.py
Actualiza el Master Deliverable Register a TM N34 (submittals 25007-0073,
25007-0077 y 25007-0080; cinco documentos). Modelado en update_register_n33.py.

Idempotencia: el backup _pre-N34.xlsx conserva el estado LIMPIO N33
(56/24/7/0 + 2 sin codigo, 113 items / 89 delivered). Al re-correr, RESTAURA
SRC desde ese backup antes de aplicar.

Veredicto N34: 3 - To be revised. Tally 2 Code 1 + 2 Code 2 + 1 Code 3.
El codigo global lo fija UN solo documento, el Quality Dossier Index.

REGLA DE ALCANCE. La revision de un documento que responde a comentarios previos
se limita a SI ESOS COMENTARIOS SE LEVANTARON EN FORMA. Universo por documento:
TM N28 para los dos de la E73, TM N30 para el dossier, TM N26 para los dos
planos. El Quality Dossier Index es la excepcion aprobada por el usuario y se
reviso a fondo, porque su funcion es ser el checklist del dossier.

CORRECCION DE VEREDICTO ANTES DE EMITIR. La primera version dispuso la Alarm and
Interlock List Rev 0 en Code 3 y era over-reach: ante un Rev 0 la pregunta es si
el defecto es INTRINSECO al documento o VIVE EN OTRO. El rango de vibracion vive
en la Instrument List (Seccion 3) y los dos TAG sin guion son housekeeping.

  UPDATES (5 re-revisiones de filas existentes; NO hay items nuevos):
    #93  Alarm and Interlock List   P22-LI-09-008-015 (Rev C->0, 2-AN -> 1)
    #112 Control and Sequence Chart P22-LI-09-008-017 (Rev A->0, 2-AN -> 1)
    #113 Quality Dossier Index      P22-BA-09-000-013 (Rev A->B, 3   -> 3)
    #57  GA Antiscalant Pump Skid   P22-DWG-09-005-011 (Rev B->C, 2-AN -> 2-AN)
    #109 GA CIP/Flushing Tank       P22-DWG-09-005-014 (Rev A->B, 2-AN -> 2-AN)

EL ITEM 65 NO SE TOCA. El Dossier de Fabricacion y Pruebas como entregable de la
ET Seccion 7 sigue en NOT DELIVERED: el indice no es el dossier.

CORRECCION DE CONTEO DE ENTREGAS. El N33 declaro que no existian las submittals
25007-0073 ni 25007-0077. Las dos existen: la 0073 llego el 11-Ago con dos
documentos y la 0077 el 18-Ago. La serie del proveedor NO tiene numeros ausentes
y el contador pasa de 78 a 80 (80 carpetas de entrega en disco).

Tally esperado tras N34: 58 Code 1 / 22 Code 2 / 7 Code 3 / 0 Code 4 + 2 sin
codigo; 113 items / 89 delivered; 34 TMs / 80 entregas.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N34.xlsx")

TM = "N34"
TM_DATE = "18-Aug-2026"

MR_UPDATES = {
    "P22-LI-09-008-015": dict(
        rev="0", delivery="E73", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered (E73, 11-Aug-2026, submittal 25007-0073). Code 1 - Approved "
            "(TM N34). Reviewed ONLY against the four points TM N28 set for this issue. "
            "All four are answered in the body: the incoming-breaker alarm resolves as "
            "P22-PLC01-XA001 on the breaker open contact; the vibration tag is unified to "
            "VT-09-001 and the four fault alarms are added for VE-09-014, VE-09-016 and "
            "the two dosing pumps; the turbocharger boost-failure differential is stated "
            "numerically at 10 bar (items 13.5/13.6); the FIT-09-005 sub-tags follow the "
            ".AHH/.AH pattern; the duplicate item numbers 5.7 and 13.4 are unique; and "
            "TIT-09-006 ranges 0 to 100 C. On the vibration trip the list is internally "
            "coherent: item 6.0 ranges VT-09-001 at 0 to 12 mm/s rms and item 6.1 sets "
            "the high-high trip at 10, inside that range. What remains lives in ANOTHER "
            "document and therefore does not degrade this one: ADASA declares the binding "
            "range to be 0 to 12 mm/s rms and requires the Instrument List "
            "(P22-LI-09-008-003) Rev E, still at 0 to 8.9 mm/s rms, to be re-issued to "
            "it, so that the vibration stop of the 93 kW pump can act. Tracked in Section "
            "3 of the transmittal. Housekeeping for the next natural issue: two of the "
            "added fault tags read VE09-014 and VE09-016, without the hyphen the IO List "
            "Rev 5 and the thirteen other valve rows both use; affects no setpoint. No "
            "annotated PDF (Code 1)."),
    ),
    "P22-LI-09-008-017": dict(
        rev="0", delivery="E73", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered (E73, 11-Aug-2026, submittal 25007-0073). Code 1 - Approved "
            "(TM N34). Reviewed ONLY against the seven points TM N28 set for this issue, "
            "all closed and each verified against the document that governs it. Note 5 "
            "assigns the turbocharger bypass VE-09-002 to the pressure control loop on "
            "PIT-09-005 with TDS selecting only the setpoint; the Stage-2 over-pressure "
            "abort reads 93 bar; the high-pressure pump ramps read 0.1 to 0.3 Hz/s; the "
            "new Note 9 states the flushing setpoints per stage, 48 and 36 m3/h under "
            "FIT-09-005; VE-09-009 is Stage 2 and VE-09-010 Stage 1 per the IO List Rev "
            "5; the setpoint and formula corrections are in place (suction permissive "
            "1.75 bar, step 7 against a setpoint, brine flow formula without the spurious "
            "/100), which the comment sheet does not claim; and the housekeeping items "
            "including the cover page count are corrected. NOT raised, per the "
            "anti-invention rule: the two 1 Hz/s ramps remaining in the CIP operation "
            "sequence belong to the CIP and flushing pumps, and the Control Philosophy "
            "sets no ramp limit for BH-09-002 - the 0.1 to 0.3 Hz/s range is written in "
            "the BH-09-001 section. No annotated PDF (Code 1)."),
    ),
    "P22-BA-09-000-013": dict(
        rev="B", delivery="E77", tm=TM, verdict="3-To be revised",
        action=(
            "Rev B delivered (E77, 14-Aug-2026, submittal 25007-0077, received 18-Aug). "
            "Code 3 - To be revised (TM N34). The index grows from 27 chapters to 49 and "
            "closes five of the ten TM N30 points: the dispatch chapters C9 and C10 "
            "against ITP rows 8.1 and 8.2, the RO pressure vessel package at D6, the "
            "equipment-by-equipment vendor records across Sections D and E, plus two the "
            "comment sheet does not claim - inspection personnel qualifications folded "
            "into B3 to B6 with the calibration certificate at C18, and the "
            "non-conformance and weld repair chapters at C19 and C20. THE DRIVER: OBS-03 "
            "is declared closed without being closed. The comment sheet reports the FAT "
            "Approval Certificate as incorporated at C21, but C21 is titled Certificate "
            "Release ADASA and points to ITP row 8.4, the Release for Dispatch. The FAT "
            "Approval Certificate is ITP row 7.9, a hold point, and the Technical "
            "Specification (P22-ET-09-000-001-0) Section 8 makes it an integral and "
            "indispensable part of the final quality dossier; it has no chapter. OBS-01 "
            "is only cosmetically closed: the two new columns are largely empty and no "
            "line carries an inclusion status, so the index still cannot serve as the "
            "checklist the PIE Base assigns to ADASA at item 7.6. And NOTE-01 remains "
            "open and decides the disposition: the ITP names two indices, the preliminary "
            "PROV-LIST-DOSS-PRE-001 of row 7.6 and the final PROV-LIST-DOSS-FIN-001 of "
            "row 8.3, a hold point for both parties, and Rev B does not state which it "
            "is. Also open: the packing list in the dispatch chapter, and the spool-by-"
            "spool identification of the super duplex mill certificates in C1 per ITP row "
            "2.1. Re-issue as Rev C. Annotated PDF with OBS-01 to OBS-03 and NOTE-01 to "
            "NOTE-02. THE INDEX IS NOT THE DOSSIER: item 65 remains NOT DELIVERED and "
            "this code does not reach it."),
    ),
    "P22-DWG-09-005-011": dict(
        rev="C", delivery="E80", tm=TM, verdict="2-AN",
        action=(
            "Rev C delivered (E80, 18-Aug-2026, submittal 25007-0080). Code 2 - Approved "
            "as noted (TM N34). Intermediate revision that ADASA had not required: the TM "
            "N26 action read 'to issue at IFC Rev 0, no new revision required'. The "
            "labelling half of TM N26 OBS-01 closes - each block is now identified as a "
            "group total or a per-bolt value. The reconciliation half does NOT, for the "
            "second consecutive issue, against a comment sheet that reports the reaction "
            "forces as updated. Verified by 300 dpi render with the 10 bolts of note 7.2: "
            "Fx 1.0242/10 = 0.102 and Fy 1.4632/10 = 0.146 both match the per-bolt block, "
            "but Fz 1.0242/10 = 0.102 against a per-bolt 0.205, twice the quotient, where "
            "at Rev B the same pair differed by a factor of ten. To be reconciled at IFC "
            "Rev 0 with no new drawing revision. TM N26 NOTE-01 stays cross-document: "
            "note 5 of the sheet still reads BOLTING DETAILS TO BE FINALIZED AND "
            "ENDORSED and note 7.9 calls the forces 'as per calculation report'; the "
            "endorsed structural calculation report is tracked in Section 3 and addressed "
            "in ADASA's letter of 18-Aug-2026. Annotated PDF with OBS-01."),
    ),
    "P22-DWG-09-005-014": dict(
        rev="B", delivery="E80", tm=TM, verdict="2-AN",
        action=(
            "Rev B delivered (E80, 18-Aug-2026, submittal 25007-0080). Code 2 - Approved "
            "as noted (TM N34). Intermediate revision that ADASA had not required. Of the "
            "two TM N26 items, OBS-01 CLOSES: Rev A carried TK-09-001 nowhere on the "
            "sheet and Rev B carries it in the title block. OBS-02 does NOT. The comment "
            "sheet reports the nozzle schedule reconciled with the datasheet, and the "
            "three entries in dispute are byte-identical to Rev A: the top opening reads "
            "MH Manhole ID 533 mm where the approved Datasheet of the CIP Tank "
            "(P22-ET-09-009-009) Rev B, Code 1 at TM N3, lists HH Handhole DN300, and N42 "
            "Spare and N97 Temperature Sensor have no counterpart in that schedule. "
            "Neither document was re-issued; the twelve remaining nozzles agree. The "
            "datasheet is not self-consistent either, since its tank construction "
            "description calls for a welded conical cover with a manhole cover. BW Water "
            "is to state in writing which document governs and align the other, "
            "re-issuing the datasheet if that is the one that changes, at IFC Rev 0 with "
            "no new drawing revision. NOT raised, per the scope rule: the cover declares "
            "two pages against the three issued - a new observation outside the TM N26 "
            "universe, recorded in the internal analysis only. Annotated PDF with "
            "OBS-01."),
    ),
}

MR_NEW = []

RH_NEW = [
    (None, "Alarm and Interlock List", "P22-LI-09-008-015", "0", "E73",
     "25007-0073", "1-Approved",
     "The four TM N28 points are answered in the body. The list is internally coherent on "
     "the vibration trip (range 0 to 12, trip 10); what remains is the re-issue of the "
     "Instrument List at the binding range ADASA declares, tracked in Section 3. Two "
     "added fault tags lack the hyphen: housekeeping for the next natural issue."),
    (None, "Control and Sequence Chart", "P22-LI-09-008-017", "0", "E73",
     "25007-0073", "1-Approved",
     "The seven TM N28 points are closed, each verified against the governing document, "
     "including one the comment sheet does not claim. The two 1 Hz/s ramps left in the "
     "CIP sequence belong to pumps for which the Control Philosophy sets no limit."),
    (None, "Quality Dossier Index", "P22-BA-09-000-013", "B", "E77",
     "25007-0077", "3-To be revised",
     "Five of ten TM N30 points close. The driver is OBS-03 declared closed without being "
     "closed: C21 is the release for dispatch of ITP row 8.4, and the FAT Approval "
     "Certificate of row 7.9 has no chapter. OBS-01 is only cosmetically closed and "
     "NOTE-01, which of the two dossier indices this is, remains open."),
    (None, "GA Antiscalant Dosing Pump Skid", "P22-DWG-09-005-011", "C", "E80",
     "25007-0080", "2-AN",
     "The labelling half of TM N26 OBS-01 closes; the reconciliation does not, for the "
     "second consecutive issue. Per-bolt Fz 0.205 against a total of 1.0242 kN over ten "
     "bolts is twice the quotient, where Rev B differed by a factor of ten."),
    (None, "GA CIP/Flushing Tank", "P22-DWG-09-005-014", "B", "E80",
     "25007-0080", "2-AN",
     "TM N26 OBS-01 closes with TK-09-001 now on the sheet. OBS-02 does not: the three "
     "nozzle entries in dispute are unchanged from Rev A and neither document was "
     "re-issued, while the comment sheet reports them reconciled."),
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
    sm["B9"].value = "34 (N1 through N34 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "80 (E1 through E80; the submittal series has no missing numbers)"
    sm["B12"].value = "18-Aug-2026 (E80)"
    sm["B13"].value = "18-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 4) ITEMS BY SECTION: el N34 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N34 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    # El scratchpad es por equipo. En macOS se usa el temporal del sistema;
    # lo que importa es construir FUERA del volumen de red y verificar el zip
    # antes de copiar al destino, porque un guardado directo sobre SMB puede
    # dejar el .xlsx a medias.
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n34_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n34_build.xlsx")
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
