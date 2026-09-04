# TECHNICAL REVIEW TRANSMITTAL N21 — SECOND STAGE RO BRINE MODULE

**ADASA Code:** P22-TM-09-000-021-0
**Date:** 11-Jun-2026
**From:** ADASA — Luis Rivera
**To:** BW Water Americas Inc.
**Submittal:** 25007-0048

---

## 1. EXECUTIVE SUMMARY

This transmittal reviews the two documents of submittal 25007-0048: the Grounding Point & Power Panel Location Layout Rev F, returned ahead of its 17-Jun commitment with the grounding schedule now embedded, and the Datasheet of PLC and HMI Panel Component Rev B, which fixes the panel hardware selection.

**TRANSMITTAL VERDICT: 3 — TO BE REVISED.** Submittal 25007-0048. Tally: 1 Code 1, 1 Code 3. The verdict is driven by the PLC and HMI Panel Component Datasheet: the panel provides no path to acquire the HART signal that the Technical Specification requires of the field instrumentation.

**Disposition at a glance:**

- **Grounding Point & Power Panel Location Layout Rev F — Code 1.** The grounding schedule (open since Transmittal N11, about 88 days, the longest-standing item of the electrical package) is embedded and complete; approved as-is — issue directly at IFC Rev 0, completing the revision-history descriptions as part of that issuance.
- **Datasheet of PLC and HMI Panel Component Rev B — Code 3.** The Allen-Bradley CompactLogix 5380 and PanelView Plus 7 selection is sound, but the panel carries no HART acquisition for the 4-20 mA + HART instrumentation the specification mandates, and the module list omits the RTD modules that serve the motor Pt-100 protection.

**Why Code 3 — Datasheet of PLC and HMI Panel Component Rev B:**

- The committed analog input module (5069-IF8) reads 4-20 mA only; it does not acquire the HART digital signal, and the panel rack carries no HART-capable analog input and no HART multiplexer. The Technical Specification — Instrumentation Specification requires the instrumentation signal protocol to be 4-20 mA + HART, so the HART capability of the field instruments cannot be used by the control system. A HART acquisition path, or the engineering justification for its omission, must be provided.
- The datasheet lists the controller and the discrete and analog I/O but omits the two 5069-IY4 universal analog modules that provide the eight motor Pt-100 RTD channels declared in the Local Control Panel Datasheet Rev B and the PLC/LCP Schematic Diagram — the module population shown does not match the project rack.

Open observations from previous transmittals are inventoried in Section 3.

---

## 2. OBSERVATIONS BY DOCUMENT

### 2.1 Grounding Point & Power Panel Location Layout Rev F — P22-DWG-09-007-003

**Response Code: 1 — Approved**

Resubmittal of Rev E (Code 3 in Transmittal N19), returned ahead of the 17-Jun commitment set in the clarification exchange of 03-Jun. The revision closes the review. The grounding schedule is now embedded on the drawing as a 48-conductor table with PE conductor identifiers, cross-section per load, ring-main topology and equipotential bonding declared on every row, per NCh Elect. 4/2003 Section 10.0 — closing the schedule item carried open since Transmittal N11, the longest-standing item of the electrical package. The Cu-bare versus insulated distinction requested is addressed (tray-to-tray bonding shown as tinned flexible braided copper, with the Material Take-Off listing copper earth link, Cu/PVC and tinned braided copper as separate items). Note 5 ("panel locations are indicative only and subject to relocation based on site condition") has been removed and the main panel is fixed in the approved Equipment Layout position. The conductor-sizing basis is unified to IEC 60364-5-54 across the drawing, with the NEC Table 250.122 reference removed. The Consolidated Comment Sheet is legible. The drawing is approved as-is.

**Action: none requiring a new revision — approved; issue directly at IFC Rev 0.** When the drawing is issued at Rev 0, complete the revision-history block with a one-line change description and the ECN reference per revision from Rev B to Rev F — the documentation item carried from Transmittal N19; the substantive content, including the embedded grounding schedule, is accepted.

---

### 2.2 Datasheet of PLC and HMI Panel Component Rev B — P22-ET-09-008-001

**Response Code: 3 — To be revised**

Resubmittal of Rev A (Code 2 in Transmittal N1). Rev B fixes the panel hardware by marking the committed values: the controller is an Allen-Bradley CompactLogix 5380 5069-L320ER (2 MB, dual EtherNet/IP), the discrete I/O are 5069-IB16 and 5069-OB16, the analog I/O are 5069-IF8 and 5069-OF4/OF8, and the operator interface is a PanelView Plus 7 Performance 2711P-T10C22D9P 10-inch touch panel. The Transmittal N1 query on Modbus is satisfactorily answered: the Consolidated Comment Sheet refers to the Control System Architecture Rev B, which carries the ProSoft PLX32-EIP-MBTCP gateway providing the Modbus TCP/IP interface to the plant — no further action on that point. Two matters require revision. Detailed annotations on `P22-ET-09-008-001_B_PLC_HMI_Datasheet_CC_ADASA.pdf`.

| ID | Severity | Topic |
|----|----------|-------|
| OBS-01 | MAJOR | No HART acquisition path in the panel. The committed analog input module 5069-IF8 reads 4-20 mA but does not acquire the HART digital signal (the datasheet note adds a 250 ohm resistor only to allow an external HART device on the loop), and the rack carries no HART-capable analog input and no HART multiplexer. The Technical Specification — Instrumentation Specification requires the instrumentation signal protocol to be 4-20 mA + HART; as configured, the HART capability of the field instruments cannot be used by the control system. Provide a HART acquisition path (HART-capable analog input or HART multiplexer) or submit the engineering justification for its omission |
| OBS-02 | MINOR | Module population does not match the project rack: the datasheet lists the controller, 5069-IB16, 5069-OB16, 5069-IF8 and 5069-OF4/OF8 but omits the two 5069-IY4 universal analog modules that provide the eight motor Pt-100 RTD channels declared in the Local Control Panel Datasheet Rev B and the PLC/LCP Schematic Diagram. Incorporate the 5069-IY4 modules, or reference the Local Control Panel Datasheet for the project-specific configuration, so the component datasheet is consistent with the rack |
| NOTE-01 | MINOR | Cover title block: project name typo "PD Tattal" — correct to "PD Taltal" (the same typo was noted on the Outline Panel Drawing in Transmittal N20) |

**Action — re-issue as Rev C:** provide the HART acquisition path for the 4-20 mA + HART instrumentation, or the engineering justification for its omission; incorporate the two 5069-IY4 RTD modules so the module list reflects the project rack consistently with the Local Control Panel Datasheet Rev B; and correct the cover title block. The controller, HMI and discrete/analog I/O selections are otherwise accepted. The per-module power dissipation given in this datasheet supports the total panel power consumption tracked on the Local Control Panel Datasheet.

---

## 3. PENDING OBSERVATIONS FROM PREVIOUS TRANSMITTALS

Items open as of 11-Jun-2026.

| Origin TM | Document | Observation | Outstanding | Status |
|-----------|----------|-------------|-------------|--------|
| TM N18 Section 2.1 | Plant Control Philosophy Rev C (P22-BT-09-009-001) | HP Pump start permissive; Sequence Charts / Setpoint List / Control Matrix; salt-rejection formula | **Fifth consecutive cycle.** The fourteen-day window of Transmittal N19 expired 08-Jun-2026 | OPEN — Rev D not delivered. As recorded in Transmittal N20, the I/O List acceptance has reverted to Code 3 and the instrumentation cabling and alarm documents remain gated. ADASA's reservation of remedies under Contract C-4300 stands |
| TM N20 Section 2.6 | PLC-LCP Outline Panel Drawing Rev A (P22-CD-09-008-001) | Enclosure contradiction (sheet steel / IP55 versus SS316L / NEMA 4X-IP66) — fabrication gate | Since 10-Jun | OPEN — Outline Rev B with the aligned Panel Specification Sheet, actual panel weight and reconciled cooling awaited; the expedited release path stated in the response of 10-Jun applies |
| TM N4 NOTE-05 | HMI Screenshots (P22-BREAD-09-008-001) | Committed at Transmittal N4 — never submitted | ~127 days — oldest open commitment | OPEN — the HMI hardware is now fixed in the datasheet of Section 2.2 (PanelView Plus 7), but the HMI screen design remains outstanding |
| TM N19 Section 2.10 | ITP Offsite (P22-BA-09-000-004) and vessel test procedures | ASME certification scope; Hydrostatic, Preservation and FAT procedures; RO pressure-vessel test scope | Since 25-May | OPEN — ITP Rev C with the certification basis of the 02-Jun waiver, the vessel test scope and the named procedures remain outstanding (Transmittal N20 Section 2.17) |
| TM N19 Sections 2.12/2.13 | Cartridge Filters (P22-ET-09-009-005/006) | Rev E / Rev D pending the Technical Note P22-NT-09-000-001-0 cycle | Due 15-Jun | OPEN — FAT/SAT table and remaining clarifications due 15-Jun-2026 |

**Addressed in this transmittal:**

- TM N11 OBS-03 / TM N15 NOTE-03 / TM N19 OBS-01 — Grounding schedule completeness (about 88 days open across three cycles): the complete 48-conductor schedule is now embedded on the Grounding Layout Rev F (Section 2.1). The grounding SEC compliance hold point is no longer gated on the schedule; only the revision-history administrative item remains.
- TM N1 — Datasheet of PLC and HMI Panel Component Modbus query: answered by reference to the Control System Architecture Rev B Modbus TCP/IP gateway (Section 2.2).

---

## 4. ATTACHMENTS

| Document | Verdict | Annotated File | Annotations |
|----------|---------|---------------|-------------|
| Datasheet of PLC and HMI Panel Component Rev B | Code 3 | P22-ET-09-008-001_B_PLC_HMI_Datasheet_CC_ADASA.pdf | OBS-01, OBS-02, NOTE-01 |

The Code 3 document carries an annotated PDF. The Grounding Point & Power Panel Location Layout Rev F is Code 1 — Approved and carries no annotated PDF.

---

## 5. RESPONSE SUMMARY

| Document Code | Title | Rev | Response Code |
|---------------|-------|-----|---------------|
| P22-DWG-09-007-003 | Grounding Point & Power Panel Location Layout | F | 1 — Approved |
| P22-ET-09-008-001 | Datasheet of PLC and HMI Panel Component | B | 3 — To Be Revised |

**Overall Transmittal Verdict: 3 — TO BE REVISED.** The Grounding Layout Rev F is approved: it closes the longest-standing electrical item, the grounding schedule, and issues directly at IFC Rev 0 (completing the revision-history descriptions as part of that issuance). The PLC and HMI Panel Component Datasheet drives the verdict: the committed hardware is sound and the Modbus question is answered, but the panel provides no means to acquire the HART signal that the Technical Specification requires of the instrumentation, and the module list omits the RTD modules of the project rack. Both points are document actions resolved at Rev C.
