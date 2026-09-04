The CIP pump BH-09-002 circulates cleaning solution from the CIP tank through the RO membrane system and
back to the tank. The pump is equipped with a variable speed drive (VFD), allowing the pump speed to be adjusted
to meet the hydraulic requirements of different CIP operating phases.
Pump start and stop commands are issued from the control system when the CIP mode is active and required
interlocks are satisfied. Pump speed is set manually by the operator or automatically by the CIP sequence logic
according to the active CIP phase. The VFD is used for speed adjustment and soft starting; during CIP circulation
step, the flow is verified using FIT-09-005. For each CIP phase (Stage 1 or Stage 2), the sequence applies a
predefined VFD speed setpoint for BH-09-002 and confirms that the measured circulation flow is above the
minimum required value for the selected stage. If the measured flow is below the minimum criterion after a
stabilization delay, the CIP sequence generates a low-flow alarm and holds progression until flow is restored by
operator adjustment or by automatic speed trim (if enabled). This function is implemented as a permissive
sequence and not as closed-loop flow control.
46 of 48
© BW Water

============================================================
--- PAGE 47 ---
============================================================
Pump operation is interlocked with the minimum tank level as measured by LIT-09-002. If tank level falls to low-
low level or if a motor or VFD fault occurs, the running pump trips automatically to protect the equipment.
CIP Cartridge Filter - FIL-09-002
Filter condition is monitored indirectly using local pressure indicators PI-09-004 and PI-09-005.
CIP Solution pH Monitoring
Prior to initiating the CIP circulation and soak phase, the CIP sequence verifies that the measured solution pH from
AE-09-001 / AIT-09-001 is within the acceptance range corresponding to the selected CIP chemical recipe. If the
pH is outside the defined range, the sequence is placed on hold, and an operator action/alarm is generated until
the solution is corrected and pH is confirmed.
CIP Interface Valve
The CIP feed, return, and make-up valves (VE-09-005, VE-09-012, VE-09-013,VE-09-007, VE-09-009, and VE-
09-010) are provided to establish or isolate the CIP circulation path between the CIP tank and the RO system
during a single CIP operation. These valves support CIP circulation only and do not determine or control the
selection of RO stage(s) to be cleaned.
Selection of the RO stage(s) under CIP is completed prior to initiation of the CIP operation. The CIP interface
valves operate in accordance with the CIP control sequence to enable the required CIP flow paths for the selected
RO stage(s).
• VE-09-005 is used for CIP solution preparation by allowing make-up water or cleaning chemicals to enter
the CIP tank and is closed once the required solution volume and concentration are achieved.
• VE-09-007 is used to isolate stages during CIP
• VE-09-012 or VE-09-013 is used to establish the CIP feed path from the CIP pump toward the selected
RO stage(s),
• VE-09-012 or VE-09-013 is used to establish the CIP feed path from the CIP pump toward the selected
RO stage(s),
• VE-09-009 or VE-09-010 is used to establish the CIP return path back to the CIP tank, depending on the
configured CIP routing.
These valves are operated automatically by the CIP sequence.
The CIP tank drain valve (manual) remains normally closed during CIP operation and is opened manually by the
Operator only after completion of CIP for draining, disposal of spent solution, or CIP tank maintenance (shall be
part of SOP).
Detailed valve operations, timing, and interlocks are defined in the CIP sequence control charts.
47 of 48
© BW Water

============================================================
--- PAGE 48 ---
============================================================
3.6.5 CIP / FLUSHING SYSTEM READY PERMISSIVES
The CIP / Flushing System shall be permitted to operate when the following conditions are satisfied:
• RO system CIP Mode / Isolated status is TRUE, and
• No active fault or trip is present within the CIP / Flushing System, and
• CIP tank level is above the minimum required level as indicated by LIT-09-002 and NOT FAULT, and
• No Low-Low Level (LALL) condition is present in CIP tank TK-09-001 as indicated by LIT-09-002, and
• CIP solution temperature measurement (TE-09-002 / TIT-09-001) is AVAILABLE and NOT FAULT, and
• CIP circulation flow measurement (FIT-09-005) is AVAILABLE and NOT FAULT, and
• CIP solution pH measurement (AE-09-001 / AIT-09-001) is AVAILABLE and NOT FAULT, and
• CIP pump BH-09-002 and its VFD are AVAILABLE and not faulted, and
• CIP interface valves (VE-09-005, VE-09-007, VE-09-009, VE-09-010 and VE-09-012, and VE-09-013 )
are AVAILABLE and NOT FAULT, and
• System is selected in REMOTE and AUTO.
IF the above conditions are satisfied, THEN CIP / Flushing System is considered AVAILABLE for operation.
Instrument availability refers to signal health and communication status only and not to measured process
values. Manual valve alignment and routing verification are performed via operating procedures and the CIP
sequence and are not enforced as PLC permissives.
3.6.6 CIP START/STOP Automatic Sequence
Detailed logic, valve sequencing, and timing are defined in the RO Flushing Sequence Chart and CIP Sequence
Chart.
48 of 48
© BW Water