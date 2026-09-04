#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n33.py
Actualiza el Master Deliverable Register a TM N33 (submittals 25007-0076,
25007-0078 y 25007-0079; cinco documentos). Modelado en update_register_n32.py.

Idempotencia: el backup _pre-N33.xlsx conserva el estado LIMPIO N32
(53/25/8/0 + 3 sin codigo, 113 items / 89 delivered). Al re-correr, RESTAURA
SRC desde ese backup antes de aplicar.

Veredicto N33: 2 - Approved as noted. Tally 4 Code 1 + 1 Code 2.

REGLA DE ALCANCE (criterio del usuario, 17-Ago-2026). La revision de un
documento que responde a comentarios previos se limita a SI ESOS COMENTARIOS
ESTAN CERRADOS; no se introducen observaciones nuevas. El alcance lo fija la
columna de comentario del cliente de la Consolidated Comment Sheet, que trae el
texto literal del pedido original. Aplicarlo cambio tres veredictos respecto de
la primera version de este script y corrigio un error propio sobre el alcance de
la NOTE-01 del TM N16, que SI nombra el marco del skid.

  UPDATES (5 re-revisiones de filas existentes; NO hay items nuevos):
    #90  Civil and Loading Drawing   P22-DWG-09-005-001 (Rev A->B, 2-AN -> 2-AN)
    #56  GA CIP/Flushing Pump        P22-DWG-09-005-010 (Rev A->B, 2-AN -> 1)
    #82  Equipment Layout            P22-DWG-09-005-003 (Rev C->D, 3   -> 1)
    #1   PFD                         P22-DWG-09-009-001 (Rev B->0, 1   -> 1)
    #67  Control Philosophy          P22-BT-09-009-001  (Rev 0->1, sin codigo -> 1)

CORRECCION DE CLAVE DEL REGISTRO. El PFD se identifica a si mismo como
P22-DWG-09-009-01 desde su Rev A, y el registro lo llevaba como
P22-DWG-09-009-001. El transmittal declara que ADASA alinea su propio registro
al codigo del documento, y este script hace esa alineacion tambien en las filas
historicas del Revision History, para que el historial no quede partido en dos
grafias.

Tally esperado tras N33: 56 Code 1 / 24 Code 2 / 7 Code 3 / 0 Code 4 + 2 sin
codigo; 113 items / 89 delivered; 33 TMs / 78 entregas.

Nota de conteo de entregas: no existe el submittal 25007-0077. La serie del
proveedor salta del 0076 al 0078, de modo que el contador pasa de 75 a 78 y no
a 79. El transmittal lo pregunta.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N33.xlsx")

TM = "N33"
TM_DATE = "17-Aug-2026"

# El PFD cambia de clave en el registro: se alinea al codigo del documento.
CODE_FIX = {"P22-DWG-09-009-001": "P22-DWG-09-009-01"}

MR_UPDATES = {
    "P22-DWG-09-005-001": dict(
        rev="B", delivery="E76", tm=TM, verdict="2-AN",
        action=(
            "Rev B delivered (E76, 13-Aug-2026). Code 2 - Approved as noted (TM N33). "
            "Reviewed only against TM N16 NOTE-01, whose verbatim text is on the comment "
            "sheet, and NEITHER of its two parts is closed. Part 1 asked for the total "
            "weight of the modified 40 ft container: Note 2 gives 13,300 kg labelled "
            "container plus contents, and that figure is the dry sum of the contents "
            "EXCLUDING the container and all fluid inventory (rows 1-16 operating plus "
            "rows 17-23 dry give 30,529.5 kg). Part 2 asked to confirm the RO Skid "
            "operating weight accounts for the interior piping 'together with skid frame, "
            "pressure vessels and wet membranes': the two new notes and the six new rows "
            "close what is counted separately, but rows 6 and 7 were reclassified to RO "
            "PRESSURE VESSELS and Note 4 limits that weight to membranes and hydraulic "
            "contents, so the skid frame is in no row. Both to be incorporated at IFC "
            "Rev 0, no new drawing revision required. Everything else the Rev B changed "
            "(rewritten plinth sheet, five new anchor details) is new content that ADASA "
            "never requested and is NOT commented here: it is handled with L&A, who "
            "execute the civil engineering. Annotated PDF with OBS-01 and OBS-02."),
    ),
    "P22-DWG-09-005-010": dict(
        rev="B", delivery="E76", tm=TM, verdict="1-Approved",
        action=(
            "Rev B delivered (E76, 13-Aug-2026). Code 1 - Approved (TM N33). The three "
            "parts of TM N11 NOTE-05 are CLOSED, and the drawing delivers more than its "
            "own written reply claims: the reply lists two items and the third is also "
            "present. Bolting arrangement with diameter, spacing, 120 mm minimum "
            "embedment and 150 mm edge distance in two dedicated views; seismic base "
            "reactions Fx, Fy and Fz stated; equipment mass of 180 kg in Note 3 with the "
            "centre of gravity in Note 8.1, which is the item the reply omits. The "
            "document governs over the reply column. Internal consistency items of those "
            "figures are NOT commented: they are new observations, not closure of "
            "NOTE-05. Issue at IFC Rev 0. No annotated PDF."),
    ),
    "P22-DWG-09-005-003": dict(
        rev="D", delivery="E78", tm=TM, verdict="1-Approved",
        action=(
            "Rev D delivered (E78, 17-Aug-2026). Code 1 - Approved (TM N33), resolving the "
            "Code 3 of TM N22. The three observations CLOSE. OBS-01: the RO cartridge "
            "filter FIL-09-001 is drawn vertical, verified on a 500 dpi rendering "
            "(circular footprint on a square support base in plan), which closes an item "
            "open since TM N22 and aligns the drawing with Datasheet Rev E and with NT "
            "P22-NT-09-000-001-0. OBS-02: the Operating Weight table is embedded on the "
            "sheet. OBS-03: the main panel is labelled LCP, the same identifier the "
            "Grounding Layout P22-DWG-09-007-003 Rev F carries on its sheet, and the title "
            "block revision field is legible. The weight figures of the embedded table and "
            "the equipment tags are NOT commented: they are new observations and the "
            "foundation matters are handled with L&A. Issue at IFC Rev 0. No annotated "
            "PDF."),
    ),
    "P22-DWG-09-009-001": dict(
        rev="0", delivery="E78", tm=TM, verdict="1-Approved",
        action=(
            "Rev 0 delivered (E78, 17-Aug-2026). Code 1 - Approved (TM N33). Rev B was "
            "approved at TM N3 with no open comments, so the Rev 0 issue was reviewed "
            "against what was approved and against nothing else, with no new comments "
            "introduced. Every process figure is unchanged: CIP tank 6.1 m3, antiscalant "
            "tank 0.25 m3, dosing pumps 2.3 LPH, CIP pump 57 m3/h, first and second stage "
            "13 and 8 m3/h, heater 20 kW, equipment tags and materials of construction. "
            "One figure changed and the change is a CORRECTION: the HP pump duty reads 49 "
            "m3/h at 46.9 bar where Rev B read 49.4 bar, and 46.9 bar is the differential "
            "head of the governing Datasheet P22-ET-09-009-002 Rev D. Not raised, because "
            "both were already in the approved Rev B: the two-digit sequential of the "
            "document code and the PD Tattal typo on the cover. ADASA aligned its own "
            "register key to the document code, which has read P22-DWG-09-009-01 since "
            "Rev A. No annotated PDF."),
    ),
    "P22-BT-09-009-001": dict(
        rev="1", delivery="E79", tm=TM, verdict="1-Approved",
        action=(
            "Rev 1 delivered (E79, 17-Aug-2026). Code 1 - Approved (TM N33). Reviewed ONLY "
            "against the four points TM N31 left open, each verified against the governing "
            "document and not against the comment sheet, and the four are CLOSED. (1) The "
            "CIP pump sensors read TE-09-003 winding and TE-09-004 bearing, consistent "
            "with the Instrument List Rev E and the Alarm and Interlock List Rev C. (2) The "
            "vibration alarm and trip pairs match the Alarm and Interlock List Rev C "
            "exactly on all three machines: 7.0 and 10 mm/s on the HP pump, 4.5 and 6.0 on "
            "each turbocharger. (3) The winding trip is supported: Class F insulation with "
            "Class B temperature rise matches Insulation Class F of the governing Datasheet "
            "P22-ET-09-009-002 Rev D, so the 140 C trip sits inside the class limit. (4) "
            "The reference table pins both child documents by code; adding their revision "
            "(P22-LI-09-008-017 Rev A and P22-LI-09-008-015 Rev C) is housekeeping for the "
            "next natural issue and holds nothing. A document at Rev 1, issued because "
            "ADASA observed that a Rev 0 comment had not been properly closed, cannot "
            "carry new comments: nothing outside those four points is raised. No annotated "
            "PDF."),
    ),
}

MR_NEW = []

RH_NEW = [
    (None, "Civil and Loading Drawing", "P22-DWG-09-005-001", "B", "E76",
     "25007-0076", "2-AN",
     "TM N16 NOTE-01 reviewed part by part: neither closed. The container weight is not "
     "declared and its Note 2 figure is mislabelled; the skid frame, named in the "
     "original request, is in no row after the reclassification to RO Pressure Vessels."),
    (None, "GA CIP/Flushing Pump", "P22-DWG-09-005-010", "B", "E76",
     "25007-0076", "1-Approved",
     "TM N11 NOTE-05 closed in its three parts. The written reply claims two; the "
     "equipment mass and centre of gravity are also on the sheet. The document governs "
     "over the reply column."),
    (None, "Equipment Layout", "P22-DWG-09-005-003", "D", "E78",
     "25007-0078", "1-Approved",
     "Resolves the Code 3 of TM N22 with its three observations closed: cartridge filter "
     "vertical (verified by render), weight table embedded, main panel labelled LCP "
     "consistent with the Grounding Layout Rev F."),
    (None, "PFD", "P22-DWG-09-009-01", "0", "E78",
     "25007-0078", "1-Approved",
     "Rev 0 reviewed only by difference against the approved Rev B. One figure changed "
     "and it corrects the HP pump duty to the 46.9 bar of the governing datasheet. "
     "Register key aligned to the document code."),
    (None, "Control Philosophy", "P22-BT-09-009-001", "1", "E79",
     "25007-0079", "1-Approved",
     "The four points TM N31 left open are closed and verified against the governing "
     "documents. Pinning the revision of the two child documents is housekeeping for the "
     "next natural issue."),
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
        raise SystemExit(f"ERROR: codigos N33 no encontrados en Master Register: {missing}")

    # 1b) alineacion de la clave del registro al codigo del documento (PFD)
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code in CODE_FIX:
            mr.cell(r, C_CODE).value = CODE_FIX[code]
            print(f"  MR code fix row {r}: {code} -> {CODE_FIX[code]}")

    # 1c) la misma alineacion en el Revision History, o el historial del
    # documento queda partido en dos grafias y el contador de ciclo se reinicia.
    _rhh0 = {rh.cell(1, c).value: c for c in range(1, rh.max_column + 1)}
    _c_code_rh = _rhh0["Code / ET Reference"]
    _n = 0
    for r in range(2, rh.max_row + 1):
        code = str(rh.cell(r, _c_code_rh).value or "").strip()
        if code in CODE_FIX:
            rh.cell(r, _c_code_rh).value = CODE_FIX[code]
            _n += 1
    if _n:
        print(f"  RH code fix: {_n} fila(s) historicas realineadas al codigo del documento")

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
    sm["B9"].value = "33 (N1 through N33 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "78 (E1 through E79; no submittal 25007-0077 was received)"
    sm["B12"].value = "17-Aug-2026 (E78 and E79)"
    sm["B13"].value = "17-Aug-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 5) ITEMS BY SECTION: el N33 no agrega items nuevos al registro, solo
    # re-revisiones de filas existentes, de modo que el bloque no se toca.
    print("  ITEMS BY SECTION: sin cambios (N33 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    scratch_dir = ("C:/Users/luisr/AppData/Local/Temp/claude/"
                   "C--SynologyDrive-SynologyDrive-DESAROLLO-PROYECTOS-CLAUDE-"
                   "MODULO-DE-SALMUERA-TALTAL/"
                   "a80560e4-55d0-4cbb-be60-12a034652756/scratchpad")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n33_build.xlsx")
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
