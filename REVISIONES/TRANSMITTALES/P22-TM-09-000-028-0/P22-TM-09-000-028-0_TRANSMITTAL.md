---
second_brain: capture
type: transmittal
project: salmuera-taltal
date: 2026-07-20
---

# Technical Review Transmittal N28 — Second Stage RO Brine Module

**Code:** P22-TM-09-000-028-0 | **Date:** 20-Jul-2026 | **Submittals:** 25007-0065 (E65) and 25007-0066 (E66)

## 1. Executive Summary

**TRANSMITTAL VERDICT: 2 — Approved as Noted.** Four documents (submittals 25007-0065 and 25007-0066), the Plant Control family. Tally: 4 Code 2.

**Disposition at a glance:**

- **Plant Control Philosophy Rev E — Code 2.** Mirror the winding and bearing sensor tags and the motor and vibration setpoints to the Alarm and Interlock List and the Instrument List at Rev 0.
- **Alarm and Interlock List Rev C — Code 2.** Bring the HP pump vibration high-high trip within the transmitter range at Rev 0.
- **Control and Sequence Chart Rev A — Code 2.** Align the sequence setpoints and the bypass note to the Alarm and Interlock List and the Control Philosophy at Rev 0.
- **IO List Rev 5 — Code 2.** Add the CIP heater output, or confirm the heater is controlled outside the module PLC (in which case this list is correct as issued).

**Why Approved as Noted, and the reconciliation these four require:** the Control-family documents outstanding for six to seven review cycles are now delivered in full, and each is correct in the content it governs. The Control Philosophy's logic (the turbocharger bypass is governed by the pressure control loop, closing the contradiction that held the Operating and Maintenance Manual), the Alarm and Interlock List's closed unit and sensor comments, the Sequence Chart's operating steps and the IO List's I/O and motor channels are all sound. What remains is a cross-document reconciliation to incorporate at Rev 0: the four disagree on tags and setpoints that must align to the governing document, namely the winding and bearing sensor mapping (winding TE-09-001, bearing TE-09-002, as the Alarm and Interlock List, IO List and Instrument List already hold, but the Control Philosophy still reverses) and a single achievable RO HP pump vibration trip (the Alarm and Interlock List sets 10.0 above the transmitter's 8.9 range, so the trip cannot fire). ADASA asks BW Water to re-issue the four as a coordinated set at Rev 0 with these two definitions fixed; no new revision cycle is required.

Section 3 lists the pending observations from previous transmittals.

## 2. Observations by Document

### 2.1 Plant Control Philosophy Rev E — P22-BT-09-009-001

**Response Code: 2 — Approved as Noted**

**Status.** Rev E delivers the parent document with its long-outstanding children now issued alongside it (the Control and Sequence Chart and the Alarm and Interlock List). Its own control logic is correct and verified: the turbocharger bypass valve VE-09-002 is governed by the pressure control loop and not by a TDS setpoint, closing the contradiction that held the Operating and Maintenance Manual; the HP pump permissive is clean, and the specific energy, salt-rejection and six-by-four array are right. What remains is a cross-document reconciliation, not a logic error: the instrument tables still tag the RO HP pump and CIP pump temperature sensors the reverse of the Alarm and Interlock List, the IO List and the Instrument List (winding and bearing swapped, a safety-sensor mapping), and the motor-temperature, vibration and discharge low-pressure setpoints must be aligned to the Alarm and Interlock List. Itemised in P22-BT-09-009-001_E_Plant_Control_Philosophy_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** mirror the RO HP pump and CIP pump winding and bearing sensor tags to the Instrument List (winding TE-09-001 and TE-09-003, bearing TE-09-002 and TE-09-004) and reconcile the motor-temperature, vibration and discharge low-pressure protection setpoints to the Alarm and Interlock List (OBS-01 to OBS-04 and NOTE-01 on the annotated PDF). The winding trip stated at 155 degrees Celsius against a Class B insulation citation is not consistent; confirm the winding trip against the motor insulation class. Issue as part of the coordinated Control-family reconciliation described in the Executive Summary.

### 2.2 Alarm and Interlock List Rev C — P22-LI-09-008-015

**Response Code: 2 — Approved as Noted**

**Status.** Rev C closes the comments carried since Transmittal N17 and N20: the permeate-conductivity setpoints now read in microsiemens per centimetre (the two-order-of-magnitude unit error is gone), the RO HP pump winding and bearing sensors are correctly tagged and set (winding TE-09-001 at 140 and 120, bearing TE-09-002 at 95 and 90 degrees Celsius, resolving the swap rejected at Rev B), the turbocharger vibration alarms are symmetric, and its six comment-sheet replies are all implemented in the body. One functional item remains on the list itself: the RO HP pump vibration high-high trip is set at 10.0 millimetres per second on a transmitter ranged 0 to 8.9, so the high-high trip the Control Philosophy requires can never fire. Itemised in P22-LI-09-008-015_C_Alarm_Interlock_List_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** bring the RO HP pump vibration high-high trip within the transmitter range, or re-range the transmitter in the Instrument List and confirm the trip value; and reconcile the incoming-breaker alarm tag to the IO List (OBS-01, OBS-02 and NOTE-01 to NOTE-02 on the annotated PDF). This list governs the reconciled setpoints for the Control-family Rev 0.

### 2.3 Control and Sequence Chart Rev A — P22-LI-09-008-017

**Response Code: 2 — Approved as Noted**

**Status.** This first-issue chart is the document that had been outstanding for six to seven review cycles, and its operating sequence is complete and correct in structure: group control, service start-up, normal and emergency shutdown, cleaning and flushing, with permissives that match the Plant Control Philosophy one to one. What it does not yet hold is numerical consistency with the documents that govern each value: Note 5 states the turbocharger bypass by a TDS value, where the Control Philosophy governs it by pressure; and several sequence setpoints differ from the Alarm and Interlock List (the Stage-2 over-pressure abort, the flushing flow, the suction permissive) and from the Control Philosophy (the VFD ramp rate). Itemised in P22-LI-09-008-017_A_Control_Sequence_Chart_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** reword the Note-5 bypass trigger to the pressure control loop per the Control Philosophy, align the sequence setpoints (over-pressure abort, flushing flow, suction permissive) to the Alarm and Interlock List and the VFD ramp rate to the Control Philosophy, correct the CIP-return valve stage description to the Valve List, and fix the brine-flow formula and the step-7 criterion (OBS-01 to OBS-06 and NOTE-01 on the annotated PDF). Issue as part of the coordinated Control-family reconciliation.

### 2.4 IO List Rev 5 — P22-LI-09-008-001

**Response Code: 2 — Approved as Noted**

**Status.** Rev 5, issued for construction, closes the Transmittal N25 note: the dosing-pump remote and running feedback are counted as BOOL, the running feedback is now sourced from the local control panel rather than the HMI, the four relay-contact coordination signals to the plant control system are present, and both motors carry Pt-100 winding and bearing channels per the Technical Specification (P22-ET-09-000-001-0), Section 5.3 - Electrical Motors, with no placeholders. One consistency item remains: the Alarm and Interlock List commands a Stop-heater interlock on the CIP tank heater (REL-09-001), but this list carries no output channel for it. Itemised in P22-LI-09-008-001_5_IO_List_CC_ADASA.pdf.

**Action to issue at IFC Rev 0 — no new revision required:** add the CIP tank heater start/stop output (and run/fault feedback if applicable) so the Alarm and Interlock List Stop-heater interlock can be executed, or confirm in writing that the CIP heater is controlled outside the module PLC (OBS-01 on the annotated PDF). On that written confirmation this list is correct as issued and the item transfers to the Alarm and Interlock List. The instrument-tag alignments (Section 3) do not affect this list on their own.

## 3. Pending Observations from Previous Transmittals

**The three most serious open items:**

| Origin TM | Document | Observation | Status |
|---|---|---|---|
| TM N27 | HP and LP Pressure Test Procedure (P22-BA-09-000-010) | The attached Line List orders 75 bar of hydrostatic test on line DA-PVC-DN65-09-016 (RO Brine Discharge, PVC Schedule 80, operating at 1 bar), a value that would rupture the line, and is labelled as an untransmitted revision | OPEN: re-issue as Rev D; the high-pressure hydrostatic test remains a Hold Point |
| TM N27 | Operating and Maintenance Manual (P22-BA-09-000-012) | Its control sequence, setpoints and HMI content are governed by this Control family; it cannot issue until the four documents above close at Rev 0 and the HMI Screenshots (P22-LI-09-008-016 Rev A) issue | OPEN: re-issue as Rev B once the Control family closes |
| TM N26 | UHPRO Structural Calculation Report (P22-CD-09-005-001) | The base-bolt design omits the main process equipment (HP pump, turbochargers, RO cartridge filter, RO pressure vessels) carried as seismic mass; it also governs the anchor loads of the dosing skids and CIP tank | OPEN: re-issue as Rev B |

**Also open:** the GA of the Antiscalant Dosing Tank Rev C and the Equipment Layout Rev D (RO cartridge filter still drawn horizontal); the HMI Screenshots (P22-LI-09-008-016 Rev A, Code 3, still incomplete); and the FAT Procedure (P22-PP-09-000-001) RTD protection sign-off, held from Transmittal N27 until the Plant Control Philosophy Rev 0 restores the winding and bearing mapping the Alarm and Interlock List, IO List and FAT already hold.

**Status of the control children:** the Control and Sequence Chart was outstanding for six to seven cycles and is now delivered (Section 2.3); the HMI Screenshots remain the last undelivered control child.

**Cross-document deliverables:** the Line List reconciled and transmitted (it fixes the HP and LP test pressure); the Single Line Diagram re-issued to "SS316L Panel, NEMA 4X/IP66" (committed on the Outline comment sheet at Transmittal N27); the container base-bolt interface (input to the OOCC foundation); and the Module Seismic Calculation Report.

## 4. Attachments

| Document | Verdict | Annotated File | Annotations |
|---|---|---|---|
| Plant Control Philosophy Rev E | Code 2 | P22-BT-09-009-001_E_Plant_Control_Philosophy_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, NOTE-01 |
| Alarm and Interlock List Rev C | Code 2 | P22-LI-09-008-015_C_Alarm_Interlock_List_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01, NOTE-02 |
| Control and Sequence Chart Rev A | Code 2 | P22-LI-09-008-017_A_Control_Sequence_Chart_CC_ADASA.pdf | OBS-01, OBS-02, OBS-03, OBS-04, OBS-05, OBS-06, NOTE-01 |
| IO List Rev 5 | Code 2 | P22-LI-09-008-001_5_IO_List_CC_ADASA.pdf | OBS-01 |

All four documents carry annotated PDFs (4 Code 2). No document in these submittals is Code 1 — Approved; each issues at IFC Rev 0 with the noted corrections incorporated.

**Download — this transmittal and the four annotated PDFs:** https://lrg.synology.me:6501/d/s/196vffdOgHuhxkUIjBvvagziqyuR4aQr/ByGtK2Zyvp6HBEouqMYWxFJ0Lc-1c7oq-67dg5dMBXA0

## 5. Response Summary

| Document Code | Title | Rev | Response Code |
|---|---|---|---|
| P22-BT-09-009-001 | Plant Control Philosophy | E | 2 — Approved as Noted |
| P22-LI-09-008-015 | Alarm and Interlock List | C | 2 — Approved as Noted |
| P22-LI-09-008-017 | Control and Sequence Chart | A | 2 — Approved as Noted |
| P22-LI-09-008-001 | IO List | 5 | 2 — Approved as Noted |

**Overall Transmittal Verdict: 2 — APPROVED AS NOTED.** Tally: 4 Code 2. The Plant Control family is delivered complete for the first time; each document is correct in the content it governs, and the open items are a coordinated cross-document reconciliation of tags and setpoints to incorporate at IFC Rev 0 — no new revision cycle. ADASA asks that the four be re-issued as a coordinated set at Rev 0 with the winding and bearing mapping and the HP pump vibration trip fixed as described in the Executive Summary. Documents not appearing in this response are unaffected by this transmittal.
