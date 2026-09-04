#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_register_n38.py — aplica el Transmittal N38 al Master Deliverable Register.

TM N38 (P22-TM-09-000-038-0), emitido el 3 de septiembre de 2026, sobre los
submittals 25007-0089 (ENTREGA 89, recibida el 1-Sep) y 25007-0090 (ENTREGA 90,
recibida el 3-Sep). ONCE documentos, todos re-revisiones.

IDEMPOTENCIA. Si existe el backup _pre-N38.xlsx, restaura SRC desde ese backup
antes de aplicar. Re-correr el script es seguro.

VEREDICTO GLOBAL: 2 — Approved as noted. 8 Codigo 1, 3 Codigo 2, CERO Codigo 3.

Filas que se tocan, todas ya existentes en el register:

  #2    P&ID                                  P22-DWG-09-009-002  (Rev D -> 0,  1 -> 1)
  #5    DS HP Pump                            P22-ET-09-009-002   (Rev E -> 0,  1 -> 1)
  #11   DS Feed Turbocharger                  P22-ET-09-009-007   (Rev E -> 0,  2 -> 1)
  #12   DS Interstage Turbocharger            P22-ET-09-009-008   (Rev E -> 0,  2 -> 1)
  #32   Instrument List                       P22-LI-09-008-003   (Rev E -> F,  1 -> 1)
  #34   Equipment List                        P22-LI-09-005-001   (Rev B -> 0,  2 -> 1)
  #38   Line List                             P22-LI-09-009-003   (Rev 0 -> 1,  1 -> 1)
  #68   HMI Display Screenshot                P22-LI-09-008-016   (Rev B -> C,  2 -> 2)
  #110  PLC/LCP FAT Procedure - Hardware      P22-PP-09-000-001   (Rev B -> C,  3 -> 2)
  #115  Liquid Penetrant Examination Proc.    P22-BA-09-000-014   (Rev C -> 0,  2 -> 1)
  #117  Ultrasonic Thickness Procedure        P22-BA-09-000-016   (Rev B -> C,  3 -> 2)

EFECTO SOBRE EL TALLY, declarado ANTES de correr.

Se parte del cierre del TM N37: 64 / 21 / 4 / 0.

  Suben de Codigo 2 a Codigo 1 (cuatro):
    - Liquid Penetrant: el formulario se emitio en blanco, que era la condicion.
    - Feed Turbocharger e Interstage Turbocharger: STYLE 77 borrado de las cuatro
      llamadas de conexion de cada uno, verificado sobre la lamina de contorno.
    - Equipment List: el desglose individual de recipientes que estaba comprometido.
  Suben de Codigo 3 a Codigo 2 (dos):
    - Ultrasonic Thickness: la clausula 9.0 ya remite al NDE Plan aprobado.
    - PLC/LCP FAT Procedure: dejo de ser el registro de un ensayo corrido y es un
      procedimiento en blanco.
  Sin cambio de codigo (cinco): P&ID, DS HP Pump, Line List e Instrument List se
    mantienen en 1; el HMI se mantiene en 2.

  El tally esperado tras el N38 es 68 / 19 / 2 / 0.

  Los DOS unicos Codigo 3 que quedan son el O&M Manual (P22-BA-09-000-012, desde
  el N27) y el Dossier Index (P22-BA-09-000-013, desde el N34), que son dos de los
  cinco documentos que NO llegaron en la entrega consolidada del 3 de septiembre.

  El Summary se recomputa desde el Master Register y no se hardcodea.

REGLA DE ALCANCE. Ningun item nuevo: los once son re-revisiones de items ya
entregados. El total de items y el de entregados no se mueven.

🔴 CORRER DESPUES DE ENVIAR el transmittal, no antes.

AVISO. El bloque ITEMS BY SECTION arrastra un descuadre heredado de un entregado
de mas; el updater lo reporta en cada corrida y no lo agranda.
"""
import os
import shutil
import collections
from copy import copy
import openpyxl

EV = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register.xlsx")
BAK = os.path.join(EV, "P22-IT-06-000-002-0_Master-Deliverable-Register_pre-N38.xlsx")

TM = "N38"
TM_DATE = "03-Sep-2026"

# Tally esperado, declarado antes de correr (ver cabecera).
TALLY_ESPERADO = {"1-Approved": 68, "2-AN": 19, "3-To be revised": 2, "4-Rejected": 0}

MR_UPDATES = {
    "P22-DWG-09-009-002": dict(
        rev="Rev 0", delivery="E89", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E89, 01-Sep-2026, submittal 25007-0089). "
                "Code 1 - Approved (TM N38). The drawing carried no open condition since "
                "the Code 1 of TM N18. Five changes declared by BW Water on the comment "
                "sheet, including the cartridge filter orientation corrected to vertical "
                "and the CIP pump suction changed from PVC to 316L stainless steel, which "
                "ADASA accepts as a minor substitution. This drawing carries the correct "
                "sizes for lines 09-048 and 09-049; the Line List Rev 1 has them "
                "inverted, and ADASA declares the binding sizes in Section 3 of TM N38. "
                "The unified line numbering deliverable also requires the shop "
                "fabrication drawings."),
    ),
    "P22-BA-09-000-014": dict(
        rev="Rev 0", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38), up from the Code 2 of TM N37. The three "
                "actions of the condition are verified as done: the report form of "
                "Appendix 1 is issued blank in every field, so the identifiers of another "
                "contract, the three consumable batch numbers and the pre-written result "
                "are gone. Closes a point raised at TM N32 and again at N35. Residual, "
                "outside the condition and tracked in Section 3: the cover page still "
                "carries the provisional document number, and two of fifteen body pages "
                "carry the previous revision index."),
    ),
    "P22-BA-09-000-016": dict(
        rev="Rev C", delivery="E90", tm=TM, verdict="2-AN",
        action=("Rev C submitted for approval (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 2 - Approved as noted (TM N38), up from the Code 3 of TM N35. The "
                "point that governed the Code 3 closed: clause 9.0 now refers acceptance "
                "to the NDE Plan (P22-BA-09-000-005) Rev C and the material is written "
                "UNS S32750 throughout. To incorporate at Rev 0: cite Article 5 of ASME "
                "Section V instead of Article 9, correct the SA790 and SA79M "
                "designations, state the sound velocity as a value, and write the "
                "acceptance criterion rather than referring to it. The Article 9 citation "
                "is the second revision declared aligned without being so."),
    ),
    "P22-ET-09-009-002": dict(
        rev="Rev 0", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38). TM N36 accepted the content and required only "
                "the issue at Rev 0 for construction, with no intermediate approval "
                "revision. Condition met. Nothing outstanding on this datasheet."),
    ),
    "P22-LI-09-009-003": dict(
        rev="Rev 1", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 1 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38). The list carried no open condition since the "
                "Code 1 of TM N29. Rev 1 adds eight lines, six of which give the "
                "low-pressure super duplex spools their own line numbers and hydrotest "
                "pressure of 7.5 barG. The hydrotest column of every line common to Rev 0 "
                "is unchanged, so the test pressures ADASA has been requiring remain the "
                "approved ones. CIP pump suction changed from PVC to 316L stainless steel, "
                "accepted as a minor substitution; to be reflected in the Valve List and "
                "the fabrication drawings. Two line sizes are inverted: the list gives the "
                "first-stage CIP reject 54 cubic metres per hour and the second-stage "
                "36, and its own approved Rev 0 sizes those services DN80 and DN65, so "
                "ADASA declares CP-SSD-DN80-09-049 and CP-SSD-DN65-09-048 as binding "
                "and requires the two rows corrected before fabrication."),
    ),
    "P22-ET-09-009-007": dict(
        rev="Rev 0", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38), up from the Code 2 of TM N36. Condition "
                "verified on the outline sheet: the four connection callouts now read the "
                "cut groove designation and PIEDMONT STYLE S alone, and STYLE 77 has been "
                "removed from all four. Closes an item first raised at TM N11. The only "
                "remaining occurrence of STYLE 77 in the file is inside the comment sheet, "
                "quoting the ADASA instruction."),
    ),
    "P22-ET-09-009-008": dict(
        rev="Rev 0", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38), up from the Code 2 of TM N36. Same as the "
                "Feed Turbocharger: the four connection callouts are clean. With the high "
                "pressure pump datasheet, the three Fedco datasheets are now all at Rev 0 "
                "for construction with no intermediate approval revision, which is what "
                "ADASA required for equipment already bought and built."),
    ),
    "P22-LI-09-005-001": dict(
        rev="Rev 0", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev 0 issued for construction (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38), up from the Code 2 of TM N11. The re-issue "
                "undertaken in writing on the 3D model comment sheet has been made: the "
                "reverse osmosis vessels are broken out individually, six in the first "
                "stage and four in the second, consistent with the membrane counts of "
                "forty-two and twenty-eight at seven per vessel. The 3D model at Rev A "
                "showed five first-stage vessels and has to follow the approved list; "
                "tracked in Section 3. The Valve List P22-LI-09-005-002, undertaken in the "
                "same pair, was not issued."),
    ),
    "P22-LI-09-008-003": dict(
        rev="Rev F", delivery="E90", tm=TM, verdict="1-Approved",
        action=("Rev F submitted for approval (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 1 - Approved (TM N38). VT-09-001 is re-ranged to 0 to 12 mm/s rms, "
                "which is the binding value ADASA declared at TM N34, so the "
                "high-pressure pump vibration trip of 10 mm/s carried by the Alarm and "
                "Interlock List Rev 0 now falls inside the range of the approved "
                "instrument and the interlock can act. Issue at Rev 0 for construction. "
                "VT-09-002 and VT-09-003 remain at 0 to 8.9 mm/s rms; ADASA declared only "
                "VT-09-001 binding and asks for written confirmation that the difference "
                "is intended."),
    ),
    "P22-LI-09-008-016": dict(
        rev="Rev C", delivery="E90", tm=TM, verdict="2-AN",
        action=("Rev C submitted for approval (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 2 - Approved as noted (TM N38), same code as TM N31. Six of the "
                "seven observations closed, verified by render because the tags live "
                "inside the screen images: a new Digital Power Meter screen carries "
                "voltage, current, active power in kilowatts and energy, meeting the "
                "Technical Specification Section 5.4; and the antiscalant level switches, "
                "the high-pressure pump, its two temperature elements, the CIP make-up "
                "valve and the reject flow transmitter are correctly tagged. Open and "
                "inverted: the first-stage screen still shows PIT-09-005 and the "
                "second-stage screen was changed to PIT-09-003, so the two are crossed. "
                "Swap them at Rev 0. Also closes the temperature element mapping."),
    ),
    "P22-PP-09-000-001": dict(
        rev="Rev C", delivery="E90", tm=TM, verdict="2-AN",
        action=("Rev C submitted for approval (E90, 03-Sep-2026, submittal 25007-0090). "
                "Code 2 - Approved as noted (TM N38), up from the Code 3 of TM N37. The "
                "determinant closed: Rev B was the record of a test already run, in 16 "
                "photographed pages; Rev C is a native 23-page procedure with the test "
                "location and date blank, the results columns empty and a blank punch "
                "list. It cites the schematic diagrams and the I/O List by issued "
                "revision, and declares the four input channels as spare, reconciling "
                "with the I/O List Rev 6 and the schematic Rev B. BW Water undertakes in "
                "writing to hold a further FAT at Penang witnessed by ADASA and a third "
                "party. Open: the KA8 output row contradicts itself, and ADASA declares "
                "that the I/O List Rev 6 governs, where item 108 REL-09-001-HS001 is "
                "the CIP heater command and KA8 is not a spare; the tag repeated on "
                "five output rows is only the suffix. The signed closure of the eight category A "
                "punch list items belongs to the Rev B record and is tracked in Section 3."),
    ),
}

RH_NEW = [
    (None, "P&ID", "P22-DWG-09-009-002", "Rev 0", "E89", "25007-0089", "1-Approved",
     "Issued for construction. No open condition since TM N18. Five self-declared "
     "changes: cartridge filter to vertical, instrument drain line added, orifice plate "
     "at CIT-09-004 to a pressure reducing valve, line tagging for the low-pressure "
     "super duplex spools, and the CIP suction to 316L stainless steel. This drawing "
     "carries the correct sizes for 09-048 and 09-049; the Line List Rev 1 has them "
     "inverted."),
    (None, "Liquid Penetrant Examination Procedure (PT)", "P22-BA-09-000-014", "Rev 0",
     "E90", "25007-0090", "1-Approved",
     "Issued for construction. The three actions of the TM N37 condition verified as "
     "done: the report form is blank in every field. Closes a point open since TM N32. "
     "Residual outside the condition: provisional document number on the cover page and "
     "two body pages with the previous revision index."),
    (None, "Ultrasonic Thickness Procedure (UT)", "P22-BA-09-000-016", "Rev C", "E90",
     "25007-0090", "2-AN",
     "The determinant of the Code 3 closed: clause 9.0 refers acceptance to the NDE Plan "
     "Rev C and the material reads UNS S32750. Couplant, ASME E 797 and the in-service "
     "inspection codes are gone. Open: Article 9 still cited instead of Article 5, second "
     "revision declared aligned without being so; SA790 and SA79M; sound velocity."),
    (None, "DS HP Pump", "P22-ET-09-009-002", "Rev 0", "E90", "25007-0090", "1-Approved",
     "Issued for construction as TM N36 required, with no intermediate approval "
     "revision. Content accepted at TM N36 and unchanged. Nothing outstanding."),
    (None, "Line List", "P22-LI-09-009-003", "Rev 1", "E90", "25007-0090", "1-Approved",
     "Issued for construction. No open condition since TM N29. Eight lines added, six of "
     "them the low-pressure super duplex spools with hydrotest at 7.5 barG. The hydrotest "
     "column of every common line is unchanged, so the test pressures ADASA requires "
     "remain the approved ones. CIP suction to 316L accepted as a minor substitution. "
     "Two line sizes are inverted against the flow column and the approved Rev 0; ADASA "
     "declares CP-SSD-DN80-09-049 and CP-SSD-DN65-09-048 as binding."),
    (None, "DS Feed Turbocharger", "P22-ET-09-009-007", "Rev 0", "E90", "25007-0090",
     "1-Approved",
     "Issued for construction. Condition of TM N36 verified on the outline sheet: STYLE "
     "77 removed from the four connection callouts, leaving the cut groove designation "
     "and PIEDMONT STYLE S. Closes an item first raised at TM N11."),
    (None, "DS Interstage Turbocharger", "P22-ET-09-009-008", "Rev 0", "E90",
     "25007-0090", "1-Approved",
     "Issued for construction. Same as the Feed Turbocharger: the four connection "
     "callouts are clean. The three Fedco datasheets are now all at Rev 0 for "
     "construction."),
    (None, "Equipment List", "P22-LI-09-005-001", "Rev 0", "E90", "25007-0090",
     "1-Approved",
     "Issued for construction. The re-issue undertaken on the 3D model comment sheet has "
     "been made: six first-stage and four second-stage vessels broken out individually, "
     "consistent with forty-two and twenty-eight membranes at seven per vessel. The 3D "
     "model has to follow. The Valve List of the same pair was not issued."),
    (None, "Instrument List", "P22-LI-09-008-003", "Rev F", "E90", "25007-0090",
     "1-Approved",
     "VT-09-001 re-ranged to 0 to 12 mm/s rms, the binding value declared at TM N34, so "
     "the 10 mm/s vibration trip of the Alarm and Interlock List Rev 0 falls inside the "
     "instrument range and the interlock can act. Issue at Rev 0. VT-09-002 and VT-09-003 "
     "remain at 8.9; written confirmation requested."),
    (None, "HMI Display Screenshot (Screen Design)", "P22-LI-09-008-016", "Rev C", "E90",
     "25007-0090", "2-AN",
     "Six of the seven observations of TM N31 closed, verified by render. A new Digital "
     "Power Meter screen carries voltage, current and active power in kilowatts. Open and "
     "inverted: PIT-09-005 stays on the first-stage screen and PIT-09-003 was moved onto "
     "the second-stage screen, so the two are crossed. Closes the temperature element "
     "mapping."),
    (None, "PLC/LCP FAT Procedure - Hardware", "P22-PP-09-000-001", "Rev C", "E90",
     "25007-0090", "2-AN",
     "The determinant of the Code 3 closed: Rev C is a native blank procedure, not the "
     "record of a test already run. Cites the schematic and I/O List by issued revision "
     "and declares the four input channels as spare. BW Water undertakes a further FAT at "
     "Penang witnessed by ADASA and a third party. Open: the KA8 output row contradicts "
     "itself against the I/O List Rev 6 item 108, which governs, and the tag repeated on "
     "five output rows is only the suffix."),
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

    # 1) updates (11 re-revisiones)
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
            print(f"  MR update row {r}: {code} -> {u['verdict']} / {u['tm']} ({u['rev']})")
    missing = set(MR_UPDATES) - seen
    if missing:
        raise SystemExit(f"ERROR: codigos N38 no encontrados en Master Register: {missing}")

    reg_num = {}
    for r in range(2, mr.max_row + 1):
        code = str(mr.cell(r, C_CODE).value or "").strip()
        if code:
            try:
                reg_num[code] = int(mr.cell(r, C_NUM).value)
            except (TypeError, ValueError):
                pass

    # 2) Revision History (11 filas nuevas)
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
    sm["B9"].value = "38 (N1 through N38 - TM N5 issued in Rev 0 and Rev 1)"
    sm["B10"].value = "90 (E1 through E90; the submittal series has no missing numbers)"
    sm["B12"].value = "03-Sep-2026 (E90)"
    sm["B13"].value = "03-Sep-2026"

    def pct(n):
        return f"{round(100 * n / delivered)}%" if delivered else "0%"
    sm["B27"].value = vd.get("1-Approved", 0); sm["C27"].value = pct(vd.get("1-Approved", 0))
    sm["B28"].value = vd.get("2-AN", 0); sm["C28"].value = pct(vd.get("2-AN", 0))
    sm["B29"].value = vd.get("3-To be revised", 0); sm["C29"].value = pct(vd.get("3-To be revised", 0))
    sm["B30"].value = vd.get("4-Rejected", 0); sm["C30"].value = pct(vd.get("4-Rejected", 0))
    sm["B31"].value = vd.get("No code issued", 0); sm["C31"].value = pct(vd.get("No code issued", 0))

    # 4) ITEMS BY SECTION: el N38 no agrega items, solo re-revisiones.
    print("  ITEMS BY SECTION: sin cambios (N38 no agrega items)")

    _guardar_robusto(wb, SRC)


def _guardar_robusto(wb, dst):
    import zipfile
    import tempfile
    scratch_dir = os.environ.get("CLAUDE_SCRATCH") or tempfile.mkdtemp(prefix="register_n38_")
    os.makedirs(scratch_dir, exist_ok=True)
    tmp = os.path.join(scratch_dir, "register_n38_build.xlsx")
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
