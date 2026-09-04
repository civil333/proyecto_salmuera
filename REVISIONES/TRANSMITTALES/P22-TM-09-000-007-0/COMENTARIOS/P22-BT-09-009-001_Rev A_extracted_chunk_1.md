
============================================================
--- PAGE 1 ---
============================================================

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |
| A | 2026/03/06 | JON | DS/YFV | AS/GHY/NHH | JR | |
| Rev | Date | Prepared By | Reviewed<br>By | Checked By | Approved<br>By | Customer |

Document Title ADASACode:P22-BT-09-009-001
Date: 06/23/2026
Revision No.: A
Second Stage RO Module for Brine – PD Taltal
Page: 1of 48
Control Philosophy
Second Stage RO Module for Brine – PD Taltal
ADASA Code : P22-BT-09-009-001

============================================================
--- PAGE 2 ---
============================================================
Con
tents
1.1
PLC PLATFORM..............................................................................................................................................6
1.2
OPERATOR INTERFACE PLATFORM.............................................................................................................6
1.3
POWER INTERRUPTION / POWER UP ...........................................................................................................6
1.4
OPERATOR INTERFACE.................................................................................................................................6
1.4.1
PASSWORD ACCESS & PRIVILEGES ............................................................................................................6
1.4.2
GUEST PRIVILEGES .......................................................................................................................................6
1.4.3
OPERATOR PRIVILEGES................................................................................................................................7
1.4.4
SUPERVISOR PRIVILEGES.............................................................................................................................7
1.4.5
ADMINISTRATOR PRIVILEGES ......................................................................................................................7
1.5
HMI DISPLAY COLOR CODING ......................................................................................................................7
1.5.1
UNITS/DRIVE MOTORS ...................................................................................................................................7
1.5.2
MEASURED VALUES ......................................................................................................................................8
1.5.3
SCREEN NAVIGATION ....................................................................................................................................8
1.5.4
ALARMS ..........................................................................................................................................................9
1.5.5
SEQUENCERS ..............................................................................................................................................10
1.5.6
HMI SEQUENCER OBJECT...........................................................................................................................10
2.1
MOTOR CONTROL FUNCTION .....................................................................................................................11
2.1.1
MOTOR CONTROL - DIRECT ONLINE (DOL) ................................................................................................11
2.1.2
MOTOR CONTROL - SOFT START ...............................................................................................................11
2.1.3
MOTOR CONTROL - VSD ..............................................................................................................................13
2.1.4
EQUIPMENT DUTY / STANDBY ....................................................................................................................15
2.1.5
PUMP FAILURE TO START / STOP LOGIC ...................................................................................................15
2.2
INSTRUMENTATION AND CONTROL FUNCTIONS ......................................................................................16
2.2.1
ANALOG TRANSMITTER/ANALYZER (LIT, FIT, AIT) ....................................................................................16
2.2.2
SWITCHES (LS) .............................................................................................................................................18
2.3
VALVE CONTROL - MOTOR OPERATED ON/OFF........................................................................................18
2 of 48
$$©$$ BW W
ater

============================================================
--- PAGE 3 ---
============================================================
2.4
PROPORTIONAL INTEGRAL DERIVATIVE (PID) CLOSED LOOP CONTROL ..............................................21
2.5
CHEMICAL DOSING CONTROL RATIO CONTROL (OPEN LOOP CONTROL) .............................................23
3.1
FEED PREPARATION SYSTEM( GROUP 1) ..................................................................................................26
3.1.1
FEED PREPARATION SYSTEM EQUIPMENT.........................................................................................26
3.1.2
FEED PREPARATION SYSTEM INSTRUMENTS....................................................................................26
3.1.3
FEED PREPARATION SYSTEM PROCESS DESCRIPTION ..................................................................26
3.1.3
FEED PREPARATION SYSTEM CONTROL & OPERATION ..................................................................28
3.1.4
FEED PREPARATION SYSTEM OPERATION X READY PERMISSIVE ...............................................30
3.2
HIGH-PRESSURE PUMPING SYSTEM (GROUP 2) .......................................................................................31
3.2.1
HIGH-PRESSURE PUMPING SYSTEM EQUIPMENT.............................................................................31
3.2.2
HIGH-PRESSURE PUMPING SYSTEM INSTRUMENTS ........................................................................31
3.2.1
HIGH-PRESSURE PUMPING SYSTEM PROCESS DESCRIPTION ......................................................32
3.2.2
HIGH-PRESSURE PUMPING SYSTEM CONTROL AND OPERATION ................................................33
3.2.2
HIGH-PRESSURE PUMPING SYSTEM PERMISSIVE ............................................................................37
3.3
RO / MEMBRANE SYSTEM (GROUP 3).........................................................................................................38
3.3.1
RO / MEMBRANE SYSTEM EQUIPMENT (X=A/B/C) ..............................................................................38
3.3.2
RO FEED AND PRE-FILTRATION INSTRUMENTATION........................................................................38
3.3.3
RO / MEMBRANE SYSTEM PROCESS DESCRIPTION .........................................................................38
3.3.4
RO / MEMBRANE SYSTEM OPERATIONS AND CONTROL .................................................................39
3.3.4
RO / MEMBRANE SYSTEM READY PERMISSIVES ...............................................................................43
3.6
CIP/FLUSHING SYSTEM (GROUP 6).............................................................................................................44
3.6.1
CIP STORAGE TANK & INSTRUMENTATION .........................................................................................44
3.6.2
CIP PUMPS, FILTER & INSTRUMENTATION (X=A/B)............................................................................44
3.6.3
CIP PROCESS DESCRIPTION ..................................................................................................................44
3.6.4
CIP OPERATION AND CONTROL.............................................................................................................46
3.6.5
CIP READY PERMISSIVES........................................................................................................................48
3 of 48
$$©$$ BW W
ater

============================================================
--- PAGE 4 ---
============================================================
3.6.6 CIP START/STOP AUTOMATIC SEQUENCE ..........................................................................................48
4 of 48
© BW Water

============================================================
--- PAGE 5 ---
============================================================

| P&IDs | P22-DWG-09-009-0002 |
| --- | --- |
| PFD | P22-DWG-09-009-0001 |
| Controls & Sequence Chart | SEPARATE DOCUMENT |
| Alarm and Control Setpoint List | SEPARATE DOCUMENT |
| Control System Architecture | P22-CD-09-004-0001 |

GENERAL INFORMATION
The reader should refer to the Piping and Instrumentation Diagrams (P&ID’s), and the documents described below
for a complete understanding of the plant control. This document is only providing an overview of the Treatment
Plant controls, the details are described in the Operating Sequence Chart and Alarm and Control Setpoint List.
The PLC follows specific steps to automatically control valves, pumps, etc. during the operating states for the
treatment plant. These steps are listed and described in the Operating Sequence Charts.
Also, the details of the control actions, setpoints, etc. that are required to operate the plant are given in the Alarm
and Control Setpoint List.
Equipment and Train modes, such as AUTO and OFF are shown in full capital letters.
Table of Reference Documents:
5 of 48
© BW Water

============================================================
--- PAGE 6 ---
============================================================
1.1 PLC PLATFORM
In the documentation the Programmable Logic Controller is referred to as the PLC. The PLC provides automated
control of the equipment. All the programming for the control of the system is stored in the PLC.
All PLCs and Remote Inputs and Outputs (RIO) associated with this plant share the same network and use it to
communicate with the HMI system. The network is configured in a ring for reliability.
1.2 OPERATOR INTERFACE PLATFORM
To accommodate equipment operation and all other control, display, and monitoring requirements, this plant
employs a local Human Machine Interface (HMI) for access to system controls and archived operating data.
1.3 POWER INTERRUPTION / POWER UP
When a loss of power occurs, all pumps are immediately stopped, all actuated valves are in their fail state (fail
open/close/last state). When power is lost, the system is in OFFLINE state.
When power is restored, the plant does not restart automatically. To restart the System, press the “SYSTEM
START” button to restart the system.
System Controls and Instrumentation are backed up by an Uninterruptible Power Supply system (UPS) (refer to
Control System Architecture drawing). The UPS will provide 30 minutes of power to ensure the controls and
instrumentation do not shutdown. This ensures that the system will go to a safe OFFLINE state and be ready for
restart.
1.4 OPERATOR INTERFACE
1.4.1 Password Access & Privileges
The local HMI includes four levels of password protection: Guest, Operator, Supervisor, and Administrator. The
Guest user type does not require a password.
1.4.2 Guest Privileges
Navigate through the graphic screens and monitor plant and equipment status.
6 of 48
© BW Water

============================================================
--- PAGE 7 ---
============================================================

| Motors | Motor Stop and no FAULT | RED |
| --- | --- | --- |
| | Motor Run and no FAULT | GREEN |
| | FAULT not acknowledged | AMBER AND BLINKING |
| | FAULT acknowledged and still existing | AMBER |
| Valves | OPEN and no fault | GREEN |

1.4.3 Operator Privileges
Operator user type shall have the Guest privileges and the following:
• Monitor pre-sets and setpoints, and to adjust some process control setpoints (not process alarm setpoints)
as specified in the Control Matrix.
• Access process train control buttons such as START Sequence and reset alarms.
• Acknowledge alarms.
• Place devices such as pumps and valves in AUTO, MANUAL ON or OFF, and designate
DUTY/STANDBY operation.
• Access PID controller popup screens, change PID control selections, and adjust PID control parameters
(except PID tuning parameters).
1.4.4 Supervisor Privileges
The Supervisor user type shall have the Operator privileges and the following:
• Adjust all setpoints, including alarm and control, as described in the Control Matrix.
• Adjust PID tuning parameters.
• Substitute (simulate) Values for Instruments.
• Set instruments to MAINTENANCE where the instrument is removed from equipment interlocks.
1.4.5 Administrator Privileges
The Administrator user type shall have the Supervisor privileges and the following privileges:
• Security configuration, including adding users and changing passwords.
• HMI , and application configuration and modification.
The HMI is configured to log out the current user after one hour of inactivity and/or four hours after logging in.
1.5 HMI DISPLAY COLOR CODING
The displays uses the color-coding shown below:
1.5.1 Units/Drive Motors
7 of 48
© BW Water

============================================================
--- PAGE 8 ---
============================================================

| | CLOSED and no fault | RED |
| --- | --- | --- |
| | FAULT not acknowledged | AMBER AND BLINKING |
| | FAULT acknowledged and still existing | AMBER |
| | Valve Transition | BLINKING GREEN AND RED |
| Other | | same basic colors as motors |


| Analogue measured value<br>as digital display | measured value within service range | background colour or equivalent |
| --- | --- | --- |
| | measured value within alarm range, not<br>acknowledged | red background, flashing or<br>equivalent |
| | measured value within alarm range,<br>acknowledged | red background or equivalent |
| Binary limit value/signal | within service range | green, e.g., point on process<br>line/symbol |
| From monitor or systems | outside service range (within alarm range) | Red AND flashing or steady,<br>depending on state of<br>acknowledgement |

1.5.2 Measured Values
1.5.3 Screen Navigation
There are several ways to navigate through the system.
• Screen navigation can be performed from equipment buttons at the top or each display.
• Click on equipment object in System Overview.
• Click on any navigation arrow.
Select the symbol for a device such as a blower, or pump to display the MANUAL/OFF/AUTO switch for that device.
Select a button labelled PID, which is found above the equipment with PID controls, to display the PID loop screen.
8 of 48
© BW Water

============================================================
--- PAGE 9 ---
============================================================
1.5.4 Alarms
The purpose of an alarm is to communicate that an operator is expected to take action to rectify or prevent an
abnormal situation.
Depending on the nature of the problem, the alarm may be a shutdown alarm (interlock) or an advisory alarm
(warning). A shutdown alarm will be generated when the PLC has determined that operation is unsafe or
undesirable. Shutdown alarms are typically reset by pressing an Alarm Reset button.
Advisory (warning) alarms are to notify the operator of an abnormal condition. The operator is expected to
acknowledge an advisory alarm by pressing the Acknowledge All button and correct the abnormal situation. If the
problem is not corrected, production quality and quantity may drop off quickly.
An alarm that is activated by an instrument such as a pressure transmitter or a flow transmitter typically requires a
pump or other device to generate the required pressure or flow. This is referred to “condition active” in this
document and the Alarm and Control Setpoint List. The alarm is not generated if the device to be protected is off
or with other specified conditions.
All alarms are indicated with a message on an alarm banner. All alarms and the time they occurred are recorded
on an alarm summary screen and archived for further reference.
The Alarms are divided in to 3 categories:
• Severity 1 - High Priority Alarm (red)
These alarms are normally associated with a complete plant shutdown or critical equipment failure, and
a partial shutdown or failure of a section of the plant that requires immediate operator attention.
• Severity 2 - Low Priority Alarm (yellow)
These alarms are normally associated with an abnormal process condition not requiring shutdown. This
alarm requires non-urgent operator attention, since no plant capacity has been lost, however the process
requires attention to avoid plant capacity loss in case the abnormal process condition is not corrected.
• Severity 3 - Notification (light blue)
These alarms are considered notifications. They are normally associated with personnel or controller-
initiated events such as placing an instrument in MAINTENANCE or SIMULATE modes, and certain
changes in operating scenarios/configurations.
Alarms can be displayed in chronological order or sorted under categories.
9 of 48
© BW Water

============================================================
--- PAGE 10 ---
============================================================

| AUTO | Completes sequence automatically without operator input. |
| --- | --- |
| SEMI AUTO | ALLOWS the Operator to use the buttons below. |
| START | Operator initiated sequence. Sequence completes automatically if none of the other buttons<br>below are pressed. |
| PAUSE | Remain in the current step with valves CLOSED and equipment STOPPED. Stop the timer and<br>retain the elapsed time |
| HOLD | Remain in current step with valves OPEN equipment RUNNING. Continue timing. |
| RESUME | 1. Step in PAUSE- reopen valves restart equipment and continue timing, continues sequence to<br>the end (as if AUTO) |
| | 2. Step in HOLD- continue timing, continues sequence to the end (as if AUTO) |
| ADVANCE | Move to next Step. |
| ABORT | CLOSE valves, stop equipment return to initial state |

1.5.5 Sequencers
A control sequencer is the order in which a set of executions are carried out to perform a specific function. The
PLC program and associated HMI object that execute instructions is called a Sequencer.
Sequencers are used throughout the control program to START/STOP equipment, systems, and processes in
specific logically ordered steps. Steps begin from a known process or equipment state and are triggered when
certain conditions are met, such as filter high DP, as required by a process, or operator initiation.
A sequencer advances when step complete/advance criteria are met. Typical criteria include timers, monitored
endpoints such as pH or concentration, equipment states such as valves open, motors running, etc.
1.5.6 HMI Sequencer Object
Sequencer Functionality
10 of 48
© BW Water

============================================================
--- PAGE 11 ---
============================================================

| REMOTE | PLC control selected at LCP |
| --- | --- |
| LOCAL | Not selected REMOTE at LCP |
| Run Time | Total run hours (from PLC resettable) |
| Alarms | Fail to Start/Stop |
| AUTO | Status |
| MANUAL | Status |
| RUN REQUEST | Status |
| RUNNING | Status |
| FAULT | Status |

1.0 STANDARIZED EQUIPMENT CONTROL FUNCTIONS
2.1 MOTOR CONTROL FUNCTION
2.1.1 Motor Control - Direct Online (DOL)
Each motor with Direct Online (DOL) drive has the following control signals and functionality (Some mixers do not
use AUTO mode, except for interlocks, and are started manually at the HMI):
PLC- Input and Outputs to and from the MCC/LCP
START / STOP Digital Output (DO) Motor start/stop command
REMOTE Digital Input (DI) PLC operation feedback
RUNNING Digital Input (DI) Run feedback
FAULT Digital Input (DI) Common Fault Signal (i.e. OLR)
Soft IO to the PLC from HMI
AUTO Complete PLC control, operator-selected
MANUAL Operator selected and controlled the Motor Equipment operation
START Starts Motor Equipment in MANUAL, operator-initiated
STOP Stops Motor Equipment in MANUAL, operator-initiated
DUTY Chooses the motor for operation in AUTO mode, operator selected,
motor selected AUTO, and not DUTY is considered STANDBY
RESET Clears Motor Equipment FAIL TO START/STOP alarm, operator initiated
Setpoints Fail to START/STOP delay (sec)
Soft IO from MCC and PLC to HMI
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch
between the system's command and its actual feedback. If the system fails to reach the commanded state within
a set time or tolerance, it is considered a fault, indicating a possible malfunction or failure.
2.1.2 Motor Control - Soft Start
Each motor with Soft Starter drive has the following control signals and functionality: A FAULT is generated by
drive or controller/monitor. TRIP is breaker status. Both may not be AVAILABLE in all circumstances.
11 of 48
© BW Water

============================================================
--- PAGE 12 ---
============================================================
PLC- Output to Soft Starter
START / STOP Digital Output (DO) Motor start/stop command
PLC- inputs from Soft Starter
REMOTE Digital Input (DI) PLC control
RUNNING Digital Input (DI) Run feedback
STOP Digital Input (DI) Stop status
FAULT Digital Input (DI) Common Fault Signal (SS Common Fault
Signal)
Soft IO to the PLC from HMI
AUTO Complete PLC control, operator-selected
MANUAL Operator selected and controlled the motor equipment operation
START Starts motor equipment in MANUAL, operator-initiated
STOP Stops motor equipment in MANUAL, operator-initiated
DUTY Chooses the motor equipment for operation in AUTO mode, operator
selected, motor selected AUTO, and not DUTY is considered STANDBY
RESET Clears motor equipment FAIL TO START/STOP alarm, operator initiated
Setpoints Fail to START/STOP delay (sec)
Soft IO from MCC and PLC to HMI
REMOTE PLC control selected at LCP
LOCAL Not selected REMOTE at LCP
Run Time Total run hours (from PLC resettable)
Alarms Fail to Start/Stop
AUTO Status
MANUAL Status
RUN REQUEST Status
RUNNING Status
FAULT status
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch
between the system's command and its actual feedback. If the system fails to reach the commanded state within
a set time or tolerance, it is considered a fault, indicating a possible malfunction or failure.
12 of 48
© BW Water

============================================================
--- PAGE 13 ---
============================================================
2.1.3 Motor Control - VSD
Each motor with a Variable Speed Drive (VSD) control signals consist
of the following (the Flocculation mixers do
not have AUTO mode for START/STOP or speed control and are star
ted manually and speed set at the HMI):
Each motor with a Variable Frequency Drive (VSD) control signal cons
ists of the following :
PLC- Outputs to the VSD
START / STOP Digital Output (DO)
Motor start / stop command
SPEED REFERENCE Analog Output (AO)
Motor speed command
PLC- Inputs from the VSD
REMOTE Digital Input (DI)
PLC control
SPEED FEEDBACK Analog Input (AI)
Current operating speed
STOP Digital Input (DI)
Stop status
FAULT Digital Input (DI)
Common Fault Signal (SS
Common Fault Signal)
Soft IO from HMI to the PLC

| AUTO | Complete PLC control, operator-selected |
| --- | --- |
| MANUAL (motor) | Operator selected and controlled the motor equipment operation |
| START | Starts motor equipment in MANUAL, operator-initiated |
| STOP | Stops motor equipment in MANUAL, operator-initiated |
| DUTY | Chooses the motor equipment for operation in AUTO mode, operator<br>selected, motor selected AUTO, and not DUTY is considered<br>STANDBY |
| RESET | Clears motor equipment FAIL TO START/STOP alarm, operator<br>initiated |
| Setpoints | Fail to START/STOP delay (sec) |
| AUTO (speed) | Complete PLC PID control, operator-selected |
| MANUAL (speed) | Allows operator speed input while motor START/STOP remains in<br>AUTO PLC control |
| MANUAL SPEED<br>REFERENCE | Allows operator input of speed (0%-100% = 4- 20mA) |

13 of 48
© BW Water

============================================================
--- PAGE 14 ---
============================================================

| REMOTE | PLC control selected at LCP |
| --- | --- |
| LOCAL | PLC control selected at LCP |
| Run Time | Total run hours (from PLC resettable) |
| Alarms | Fail to Start/Stop |
| AUTO | Status |
| MANUAL | Status |
| RUN REQUEST | Status |
| RUNNING | Status |
| FAULT | Status |
| | |

Soft IO from PLC to HMI
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch
between the system's command and its actual feedback. If the system fails to reach the commanded state within
a set time or tolerance, it is considered a fault, indicating a possible malfunction or failure
14 of 48
© BW Water

============================================================
--- PAGE 15 ---
============================================================
2.1.4 Equipment DUTY / STANDBY
2 pump, N+1 example
Each pump of a pair can meet the specified volume and pressure required by the process. This is expressed as
2x100% or N+1 (N=required number, in this case 1, +1 is a spare).
One pump selected AUTO will be selected for DUTY. The pump selected for DUTY will be the only operating
pump controlled by the PLC in AUTO operation unless it fails (FAULT or TRIP). The pump selected AUTO and
STANDBY is a hot spare that will operate in AUTO if the duty pump fails for some reason.
The switch over to the operation of the standby pump is automatically controlled by the PLC.
A motor in a TRIP/FAULT state is automatically placed and MANUAL and OFF by the PLC. The motor must be
reset by the operator before it can be selected AUTO and DUTY or STANDBY.
3 pump, N+1 example
Each pump of a set of three (3) can meet half the specified volume and pressure required by the process. This is
expressed as 3x50% or N+1 (N=required number, in this case 2, +1 is spare). Only N can be selected DUTY.
Two pumps selected AUTO will be selected for DUTY and the third is STANDBY if in AUTO. The pumps selected
for DUTY will be the operating pumps controlled by the PLC in AUTO operation. The STANDBY pump is a hot
spare that will operate in AUTO if one of the duty pumps TRIP/FAULT for some reason. A maximum two (2) pumps
can be selected for DUTY.
2.1.5 Pump Failure to Start / Stop Logic
When a pump is commanded to START in AUTO or MANUAL at the HMI, the RUN signal must be received within
a specified duration, or the pump will FAIL TO START. A latched alarm is generated. Operator RESET is required
to clear and unlatch the alarm.
The STANDBY pump will start when in AUTO. Its mode will be changed to DUTY.
Note: A pump that fails to start will go to MANUAL and STOP to prevent immediate restart when RESET.
To prevent pump deadheading, the associated motorized valve (auto-valve) must be confirmed fully open before
the pump is allowed to operate. The valve open status shall serve as a permissive signal for pump startup.
15 of 48
© BW Water

============================================================
--- PAGE 16 ---
============================================================
2.2 INSTRUMENTATION AND CONTROL FUNCTIONS
2.2.1 Analog Transmitter/Analyzer (LIT, FIT, AIT)
Analog instruments, have four (4) AVAILABLE alarm states (it is not required to use all states):
High High (HH) only used with interlocks and control actions such as switching valves and stopping
pumps in abnormal operating conditions
High (H) information/warning/permissive
SP-1 Readily AVAILABLE soft output provision for command (Admin shall be able to
activate this whenever necessary).
SP-2 Readily AVAILABLE soft output provision for command (Admin shall be able to
activate this whenever necessary).
SP-3 Readily AVAILABLE soft output provision for command (Admin shall be able to
activate this whenever necessary).
SP-4 Readily AVAILABLE soft output provision for command (Admin shall be able to
activate this whenever necessary).
Low (L) information/warning/permissive
Low Low (LL) only used with interlocks and control actions such as stopping pumps, switching
valves, in abnormal operating conditions
Analog Transmitters may also have operational setpoints that fall between the High and Low alarm setpoints. For
example, a level transmitter may have pump start and stop setpoints for level control. Analog Transmitters also
are used as the Process Variable (PV) for Proportional Integral Derivative (PID) or Ratio control where the
Manipulated Variable (MV), such as pump speed, is adjusted to maintain a tank level, flow, etc. Setpoint (SP).
All Flow Transmitters must have totalizers at the HMI. Totalized flow is calculated either of two ways, from pulses
from the transmitter or, calculated real time from the flow process variable.
Note: All analog values must be archived and AVAILABLE for trending.
16 of 48
© BW Water

============================================================
--- PAGE 17 ---
============================================================

| High High Alarm Setpoint | Alarm generated at greater than or equal to this value |
| --- | --- |
| High Alarm Setpoint | Alarm generated at greater than or equal to this value |
| SP-1 Setpoint | A soft output will be triggered once the set value matches the<br>actual process value or reaches an equivalent condition. |
| SP-2 Setpoint | A soft output will be triggered once the set value matches the<br>actual process value or reaches an equivalent condition. |
| SP-3 Setpoint | A soft output will be triggered once the set value matches the<br>actual process value or reaches an equivalent condition. |
| SP-4 Setpoint | A soft output will be triggered once the set value matches the<br>actual process value or reaches an equivalent condition. |
| Low Alarm Setpoint | Alarm generated at less than or equal to this value |
| Low Low Alarm Setpoint | Alarm generated at less than or equal to this value |
| Alarm Value Dead-band | The amount in engineering units that the current value must drop<br>below either the High High or High limits, or increase above either<br>the Low Low or Low limits before an alarm can be retriggered |
| Alarm Time Delay | The time, in seconds, that must elapse after the current value<br>exceeds an alarm limit before the alarm is triggered |
| Maintenance Mode | Removes the instrument from the interlock logic.<br>4-20mA derived scaled value is valid (still displayed). |
| Simulate Mode | The PV is entered by the operator, remains as an interlock |

Analog Instrument Control:
PLC - IO from the instrument to the PLC
4-20mA Analog Input (AI) process variable, converted and scaled in the PLC
HMI - Soft IO to PLC
NOTE: An instrument used as the PV for a PID controller can only be placed in SIMULATE Mode
when the PID controller is in MANUAL Mode.
17 of 48
© BW Water

============================================================
--- PAGE 18 ---
============================================================

| FAULT | The 4-20mA signal is outside its range |
| --- | --- |
| EU Scale Minimum | In appropriate engineering units, Lower Range Value (LRV) |
| EU Scale Maximum | In appropriate engineering units, Upper Range Value (URV) |
| Alarm | Status |

Soft IO from PLC to HMI
Process Variable (PV) Scaled process value
2.2.2 Switches (LS)
Switches are usually provided as a backup for the transmitters. They provide warnings and initiate control actions
as required. They provide alarms and initiate interlocking with other equipment and processes.
High High and Low Low switches typically function as an interlock by stopping equipment such as pumps, mixers
closing an isolation valve.
The discrete signal (either energized or de-energized) from the LS to the PLC is fail-safe, that is, energized until
the alarm condition is present. In the case of low level (LSL) / Level Low Low (LSLL), pressure (PSL/PSLL), and
Flow (FSL/FSLL), the switches are wired normally-open (NO). When liquid or pressure is present above the alarm
level, the circuit is energized. When the liquid drops below the alarm level, the switch opens, generating an alarm.
High Level (LSH)/ Level High High (LSHH) and pressure (PSH/PSHH) switches High / High High are wired normally
closed and energized when the liquid or pressure is below the alarm level. When they go above the alarm level,
the switches open and generate an alarm.
Level Switch Control is as follows:
PLC - IO from the instrument to the PLC
Current State Digital Input (DI) energized or de-energized
HMI - Soft IO to PLC
ON Delay Setpoint The time, in seconds, that must elapse after the alarm condition
occurs before generating an alarm
Disable/Enable Disables or enables LS interlock functions
HMI - Soft IO from PLC
Switches Interlock Status Active, Inactive
2.3 Valve Control - Motor Operated ON/OFF
A valve must be selected AUTO for automatic control according to the PLC logic. A valve cannot be selected
AUTO if the valve has FAILED TO OPEN or FAILED TO CLOSE alarm active. To deactivate an alarm, it must be
RESET.
18 of 48
© BW Water

============================================================
--- PAGE 19 ---
============================================================
Valve Position Switches are used to dete
rmine when valve is either open (ZSO) or closed (ZSC). Valve position
switches can provide alarm and interlock
functions.
Alarms are generated when a valve con
trolled by the PLC is not in its commanded position or takes too long to
transition, or when a manual valve is not
in the required position. When a valve fail alarm is generated, the valve
is put into MANUAL and CLOSE.
Valve Position Switches act as interlocks
by stopping, or preventing the starting, of pumps and processes.
Position Switches are wired normally ope
n and go closed when the valve is in its commanded position.
A FAILED valve interlocks the process a
nd is commanded to its FAIL-SAFE position.
PLC- Input and Outputs to an
d from the MCC
OPEN
Digital Output (DO) OPEN command
CLOSE
Digital Output (DO) CLOSE command
OPENED
Digital Input (DI) OPEN feedback
CLOSED
Digital Input (DI) CLOSED feedback
REMOTE/LOCAL
Digital Input (DI) REMOTE/LOCAL feedback
HMI - Soft IO from MCC/PLC
AUTO
Complete PLC control, operator-selected
MANUAL
Operation without interlocks activated, operator selected
MANUAL OPEN
Opens valve in MANUAL, operator-initiated
MANUAL CLOSE
Closes valve in MANUAL, operator-initiated
FAIL RESET
Reset Fail to Open/Close alarm
Fail to Open Setpoint
Alarm time delay in seconds
Fail to Close Setpoint
Alarm time delay in seconds
HMI - Soft IO to the PLC
AUTO
Complete PLC control, operator-selected
MANUAL
Operation without interlocks activated, operator selected
MANUAL OPEN
Opens valve in MANUAL, operator-initiated
MANUAL CLOSE
Closes valve in MANUAL, operator-initiated
FAIL RESET
Reset Fail to Open/Close alarm
Fail to Open Setpoint
Alarm time delay in seconds
Fail to Close Setpoint
Alarm time delay in seconds
HMI - Soft IO from MCC/PLC
AUTO
Status
REMOTE / LOCAL
Status
OPEN REQUEST
Status
CLOSE REQUEST
Status
FAIL ALARM
Status
2.3.2 Modulating Control Valve
19 of 48
© BW Water

============================================================
--- PAGE 20 ---
============================================================

| AUTO | Status |
| --- | --- |
| MANUAL | Status |
| REMOTE / LOCAL | Status |
| % POSITION | Status |
| FAIL ALARM | Status |

Valve Position Switches are used to determine when valve is either open (ZSO) or closed (ZSC). Valve position
switches can provide alarm and interlock functions.
The valve positioner provides the actual valve position in (%). The valve can be commanded to OPEN or CLOSE
to a specific position (0% - 100%), either in MANUAL or AUTO mode.
Alarms are generated when a valve controlled by the PLC is not in its commanded position or takes too long to
transition, or when a manual valve is not in the required position. When a valve fail alarm is generated, the valve
is put into MANUAL and CLOSE.
Valve Position Switches act as interlocks by stopping, or preventing the starting, of pumps and processes.
Position Switches are wired normally open and go closed when the valve is in its commanded position
Manual Valve Control (with Position Switches) is as follows:
PLC- Input and Outputs to and from the MCC
OPENED Digital Input (DI) OPEN feedback
CLOSED Digital Input (DI) CLOSED feedback
REMOTE/LOCAL Digital Input (DI) REMOTE/LOCAL feedback
% POSITION SETPOINT Analog Output (AO) % POSITION command
% POSITION Analog Input (AI) % POSITION feedback
HMI- Soft IO to the PLC
AUTO Complete PLC control, operator selected
MANUAL Operation without interlocks activated, operator selected
% POSITION Setpoint Opening / Closing % Position Command
FAIL RESET Reset Fail to Open/Close alarm
FAIL Position Time Setpoint Alarm time delay in seconds
FAIL Position Difference Position Difference in (%)
Setpoint
HMI - Soft IO from MCC/PLC
20 of 48
© BW Water

============================================================
--- PAGE 21 ---
============================================================
2.4 Proportional Integral Derivative (PID) Closed Loop Control
The following use PID controllers:
• Variable Frequency Drive (VSD) motor speed control for flow and pressure,
• Level and flow Control Valves
• Various Chemical Dosing Pumps
Proportional, Integral, and Derivative (PID) control uses an algorithm that compares a Process Variable (PV) with
a specified Setpoint (SP). The error of the PV from SP is calculated. The algorithm produces a Control Variable
(CV) that is sent to a control device such as a VSD, control valve, and etcetera., that adjusts the process to bring
the error to zero. The PID CV is continually adjusted as the process changes.
The PID algorithm is composed of:
• Proportional (GAIN) - when the process is under a consistent load, the error is multiplied by the GAIN
to produce a control output value.
• Integral (RESET) - when the process is under a magnitude change, a reset of the gain factor based on
the duration the error from the setpoint remains. The control variable is adjusted to bring the process
value back to the setpoint.
• Derivative (RATE)- when there are rapid process oscillations around the setpoint in processes, the rate
of process change is determined to prevent a swing in the process value from fully developing.
When a block goes OFFLINE, or associated equipment is commanded to STOP, the PID controller retains the last
state (tracking). This allows the process to stabilize more quickly when restarted.
When there is a loss of the PV, the PID controller is placed in manual at the last state output and the device point
is alarmed.
PID Parameter Setting and Trending
The PID object must include a 30-minute trend of the CV, PV, and SP to assist in the tuning of the PID controller.
Only small, incremental, changes should be made to the PID setpoints.
CAUTION: The operator must use caution when manipulating all values to avoid process upsets.
PID Control Object
PLC - PLC- Input and Outputs
Process Value (PV) Analog Input (AI), 4-20mA converted and scaled to engineering
units in PLC
Control Output (CV) Analog Output (AO), 4-20mA generally displayed as 0-100%
21 of 48
© BW Water

============================================================
--- PAGE 22 ---
============================================================
HMI - HMI To PLC
SP Process setpoint
P-SP Proportional setpoint
I-SP Integral setpoint
D-SP Derivative setpoint
AUTO mode PLC PID adjustment of the CV
MANUAL mode Operator entered CV generally 0-100% corresponding to 4-20mA
output
CASCADE Mode PID Setpoint comes from calculation or from other controller
HMI -PLC to HMI
Process Value (PV) current value
Control Output (CV) current value
22 of 48
© BW Water

============================================================
--- PAGE 23 ---
============================================================

| AUTO | PLC adjustment of output to pump |
| --- | --- |
| MANUAL | Operator Entered output (0-100%) |
| Concentration | Concentration of the chemical to be dosed |
| Density | Density of chemical to be dosed |
| Capacity | pump rated capacity at 100% stroke and speed |
| Stroke | Stroke setting of pump if manually set |
| Target Concentration | Operator entered |
| Manual Speed | Operator entered in PLC manual mode |

2.5 Chemical Dosing Control Ratio Control (open loop control)
Controlling dosing for chemicals not provided with analytical instrument feedback require a ratio controller based
on flow or another measured parameter.
Ratio Controller Object
In this control strategy, the system operates solely based on the preset parameter, relying on the assumption
that the input-out relation remains stable over time.
Controlling dosing for chemicals not provided with analytical instrument feedback requires a ratio controller based
on flow or another measured parameter.
This control loop is usually utilized in the chemical dosing application.
Ratio Controller Object
PLC- Input and Outputs to and from the MCC
Process Value (PV) The measured value being controlled,
Analog Input (AI), 4-20mA converted and scaled, or Digital Signal
(DI), or
A defined set of data.
Control Output (CV) Analog Output (AO), 4-20mA, generally displayed as 0-100%
HMI to PLC
PLC to HMI
Process Value (PV) Current value
Control Output (CV) Current value
23 of 48
© BW Water

============================================================
--- PAGE 24 ---
============================================================
Ratio Controller HMI Object (example)
24 of 48
© BW Water

============================================================
--- PAGE 25 ---
============================================================

| Group | | |
| --- | --- | --- |
| - | Feed to UHPRO system<br>(SWRO brine) | (BY CLIENT) |
| 1 | Feed Preparation System | Brine feed from SWRO (battery limit), chemical dosing, static<br>mixing, RO cartridge filtration, associated piping and<br>instrumentation. |
| 2 | High-Pressure Pumping<br>System | RO HP PUMP, TURBOCHARGER (feed and interstage turbos),<br>pressure transfer from reject streams, associated piping and<br>instrumentation. |
| 3 | Membrane Treatment<br>System | RO 1ST AND 2ND Stage, pressure vessels, permeate collection,<br>reject discharge, interconnections and instrumentation. |
| 4 | Cleaning-in-Place (CIP)<br>System | CIP tank, CIP pumps, flushing connections to membrane system,<br>isolation valves, and instrumentation for cleaning and preservation. |
| - | Product and Waste<br>Interfaces | (BY CLIENT) |

3. Water Treatment Plant
EQUIPMENT GROUPS
An equipment group is various equipment and instrumentation that operate as a unit. The groups are included in
the System Overview Displays in HMI. A group’s Overview graphic object will indicate if a group is READY. The
READY status of all groups will be observable in the Overview Display for the operator to readily determine the
operating state of the Treatment System.
Group READY is an indication that the minimum required equipment is selected AUTO and there are no priority 1
alarms. A block not READY may be an interlock for other groups and equipment, but not necessarily.
For example, the Clean-in-Place (CIP) System group is NOT READY due to CIP Tank level Transmitter FAULT.
The FAULT interlocks the Coagulant pumps. They are prevented from starting or they are stopped when running.
List of Equipment Groups
25 of 48
© BW Water

============================================================
--- PAGE 26 ---
============================================================

| | Item | | | Equipment Description | | | Tag No. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | RO Cartridge Filter | | | FIL-09-001 | |
| 2 | | | Static Mixer | | | MZE-09-001 | |
| 3 | | | Antiscalant Dosing Tank | | | TK-09-002 | |
| 4 | | | Antiscalant Dosing Pump 1 | | | BDS-09-001 | |
| 5 | | | Antiscalant Dosing Pump 2 | | | BDS-09-002 | |


| | Item | | | Instrument Description | | | Tag No. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | RO Cartridge Filter Differential Pressure Switch | | | DPS-09-001 | |
| 2 | | | ORP Analyzer (Downstream RO Cartridge Filter) | | | ORPIT-09-001 | |
| 3 | | | Conductivity Analyzer (Downstream RO Cartridge Filter) | | | CIT-09-001 | |
| 4 | | | Flowmeter (Downstream RO Cartridge Filter) | | | FIT-09-001 | |
| 5 | | | Antiscalant Dosing Tank Level Switch - High | | | LSH-09-001 | |
| 6 | | | Antiscalant Dosing Tank Level Switch - Low | | | LSH-09-002 | |
| 7 | | | Antiscalant Dosing Tank Inlet Motorized Valve - Limit Switch | | | VE-07-014 | |
| 8 | | | Antiscalant Dosing Pump Downstream Motorized Valve - Limit Switch | | | VE-07-016 | |

3.1 FEED PREPARATION SYSTEM( GROUP 1)
Ref P&ID: P22-DWG-09-009-02-08 || P22-DWG-09-009-02-11
3.1.1 FEED PREPARATION SYSTEM EQUIPMENT
3.1.2 FEED PREPARATION SYSTEM INSTRUMENTS
3.1.3 FEED PREPARATION SYSTEM PROCESS DESCRIPTION
The Feed Preparation System receives SWRO brine at the battery limit and conditions it for entry into the high-
pressure pumping and UHPRO membrane system. The incoming brine is characterized by high salinity, with a
typical total dissolved solids concentration in the range of approximately 43,000 to 53,000 mg/L, and is already
pretreated upstream of this system. The role of the Feed Preparation System is to ensure that the brine is
26 of 48
© BW Water

============================================================
--- PAGE 27 ---
============================================================
chemically conditioned, uniformly mixed, and free of fine particulates that could adversely affect downstream high-
pressure equipment and membranes.
Chemical conditioning is achieved through antiscalant dosing. Antiscalant is stored in a dedicated dosing tank and
injected into the brine feed via duty and standby dosing pumps. The chemical is introduced via injection port of a
static mixer to ensure homogeneous distribution across the pipe cross-section before further processing. This
arrangement ensures consistent chemical availability and avoids localized under-dosing or over-dosing prior to
pressurization.
Following chemical injection and mixing, the brine passes through a cartridge filter that provides final mechanical
protection within the Feed Preparation System. The cartridge filter removes fine suspended solids remaining in the
brine stream, protecting the downstream high-pressure pump, energy recovery devices, and membrane elements
from particulate fouling, erosion, or blockage. The filtration stage does not alter the dissolved constituents of the
brine and operates solely as a physical barrier to solids.
Instrumentation installed downstream of the cartridge filter provides confirmation of feed readiness prior to high-
pressure pumping. Conductivity and ORP analyzers monitor feed quality to detect abnormal salinity or chemical
conditions, while a flow transmitter confirms the presence and stability of feed flow to the high-pressure pump.
These measurements support monitoring and protection functions and do not perform active control within the
Feed Preparation System.
Overall, the Feed Preparation System establishes the necessary boundary conditions for stable and reliable
operation of the downstream High-Pressure Pumping System. By ensuring continuous chemical conditioning,
uniform mixing, and effective particulate removal, the system protects critical equipment and supports efficient
UHPRO membrane operation without performing flow control, pressure generation, or desalination.
27 of 48
© BW Water

============================================================
--- PAGE 28 ---
============================================================
3.1.3 FEED PREPARATION SYSTEM CONTROL & OPERATION
The Feed Preparation System is enabled when the RO system is in operation and feed flow to the RO is required.
While enabled, the system operates continuously to provide stable chemical dosing, mixing, and filtration to
condition the feed water prior to further treatment.
System reliability is achieved through duty/standby arrangements for rotating chemical dosing equipment, while
passive conditioning and filtration components. Alarms provide indication of loss of chemical dosing capability, low
chemical inventory, or excessive filter fouling. Internal interlocks inhibit operation under conditions that could result
in ineffective chemical conditioning or mechanical damage, ensuring that only adequately conditioned feed is
passed forward for downstream processes.
• Static Mixer and Cartridge Filter (MZE-09-001 / FIL-09-001)
The static mixer requires no control or actuation and is considered AVAILABLE when the feed line is open and
flowing. The cartridge filter operates continuously during normal operation. Differential pressure across the filter is
monitored to assess cartridge condition. A high differential pressure alarm indicates fouling and maintenance
requirement.
Protective interlocks associated with excessive differential pressure may (operator-initiated) inhibit continued
operation to prevent equipment damage. No active control functions are applied to either the static mixer or the
cartridge filter.
Instrumentation installed downstream of the cartridge filter confirms feed condition before high-pressure pumping.
Conductivity and ORP analyzers provide continuous monitoring of feed quality to detect abnormal salinity or
chemical condition (CIT-09-001, ORPIT-09-001). A flow transmitter confirms the presence and stability of feed flow
to the high-pressure pump (FIT-09-001). These instruments are used for monitoring, and validation of feed
readiness and do not perform active control within the Feed Preparation System.
• Antiscalant Dosing Tank (TK-09-002) and Pump (BDS-09-001 / BDS-09-002),
The antiscalant dosing system is controlled to ensure reliable and continuous chemical injection into the brine feed
whenever the Feed Preparation System is in operation. The system comprises the antiscalant dosing tank (TK-09-
002), duty/standby dosing pumps (BDS-09-001 / BDS-09-002), and the motorized isolation valves (VE-09-
014/010);
The antiscalant dosing tank inlet motorized valve ( VE-09-014) is provided to automatically control tank filling based
on tank level. The valve opens when the tank level reaches a low-level condition and closes when the high-level
setpoint is reached to prevent overfilling. The valve is interlocked with tank level and system status such that it
28 of 48
© BW Water

============================================================
--- PAGE 29 ---
============================================================
remains closed during fault conditions (this shall be a separate loop such that filling is not stalled even during
shutdown for preparation purposes).
The dosing pumps are arranged in a duty and standby configuration and are normally operated in automatic mode.
One pump is selected as duty, with the standby pump AVAILABLE to maintain dosing continuity in the event of
pump fault or maintenance. Pump run status and fault feedback are monitored to confirm availability and correct
operation.
Antiscalant injection to the brine feed is enabled through the motorized valve (VE-09-016) installed upstream of
the static mixer (MZE-09-001). The valve is controlled to open when antiscalant dosing is enabled and to close
when dosing is inhibited or intentionally isolated, providing positive control of chemical injection into the process.
The antiscalant dosing tank level is continuously monitored by a level indicator (LI-09-002) with associated level
switches. A high-level switch (LSH-09-001) provides overfill indication, while a low-level switch (LSL-09-002)
provides alarms and protective inhibition of dosing pump operation. Low tank level also prevents opening of the
motorized injection valve to avoid ineffective dosing and protect the pumps.
Local pressure indication on the dosing discharge header (PI-09-006) provides visibility of dosing line pressure. A
pressure safety valve (PSV-09-002) is installed to protect the dosing system against overpressure conditions.
Valve positions, pump status, and instrument signals are monitored to provide clear operational feedback and
alarm indication to operators.
Antiscalant Dosing Strategy
Ratio Control: Flow-paced Open Loop
In Ratio Control mode, the antiscalant dosing rate is calculated directly from the RO inlet flow and the configured
antiscalant dosage requirement. The calculated dosing rate is converted to a corresponding pump stroke frequency
and applied directly to the duty dosing pump without closed-loop correction.
Antiscalant Flow (L/h) = [FIT-09-001, (m³/h) × Antiscalant dosage (g/m³)] ÷ [Chemical concentration ((g/L) ]
If RO feed flow signal FIT-09-001 is unAVAILABLE, the antiscalant dosing system shall be operated in “Manual
Stroke Mode” as fallback, where the duty pump BDS-09-001 / BDS-09-002 runs at a fixed operator-set stroke
frequency. This mode provides minimum chemical protection and is intended for temporary operation only until
flow measurement is restored.
29 of 48
© BW Water

============================================================
--- PAGE 30 ---
============================================================
3.1.4 FEED PREPARATION SYSTEM OPERATION X READY PERMISSIVE
The Feed Preparation System shall be considered AVAILABLE when the following conditions are satisfied:
• Cartridge filter differential pressure within acceptable range, and
• No active fault within the Feed Preparation System, and
• Feed Preparation System Group selected in REMOTE and AUTO.
• RO system in RUN / FEED REQUEST active.:
• Antiscalant dosing tank level above low (LSL-09-002 not active), and
• At least one antiscalant dosing pump NOT FAULT and AUTO (BDS-09-001 / BDS-09-002), and
• Motorized valves VE-09-014/016 are AVAILABLE, NOT FAULT and AUTO
30 of 48
© BW Water

============================================================
--- PAGE 31 ---
============================================================

| | Item | | | Equipment Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | RO High Pressure Pump – RO HP Pump (VSD Driven) | | | BH-09-001 | | |
| 2 | | | Feed Turbocharger | | | SIP-09-001 | | |
| 3 | | | Interstage Turbocharger | | | SIP-09-002 | | |


| | Item | | | Instrument Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | Pressure Transmitter (upstream RO HP PUMP) | | | PIT-09-001 | | |
| 2 | | | Pressure Transmitter (downstream RO HP PUMP) | | | PIT-09-002 | | |
| 3 | | | Pressure Transmitter (Feed Turbocharger Outlet - RO Stage 1 Feed) | | | PIT-09-003 | | |
| 4 | | | Pressure Transmitter (RO Stage 1 Reject - Interstage Turbocharger Feed) | | | PIT-09-004 | | |
| 5 | | | Pressure Transmitter (Interstage Turbocharger Outlet - RO Stage 2 Feed) | | | PIT-09-005 | | |
| 6 | | | Pressure Transmitter (RO Stage 2 Reject - Interstage Turbocharger Feed) | | | PIT-09-006 | | |
| 7 | | | Pressure Transmitter (Interstage Turbocharger Reject - Feed Turbocharger<br>Inlet) | | | PIT-09-007 | | |
| 8 | | | Pressure Transmitter (Feed Turbocharger Reject) | | | PIT-09-008 | | |
| 8 | | | Common Permeate Flow Indicator (RO Interface) | | | FIT-09-003 | | |
| 9 | | | Common Reject / Brine Flow Indicator (RO Interface) | | | FIT-09-004 | | |
| 10 | | | Brine Bypass Valve - Feed Turbocharger Bypass with Limit Switches | | | VE-09-002 | | |
| 11 | | | Turbocharger Isolation Valve with Limit Switches | | | VE-09-007 | | |

3.2 HIGH-PRESSURE PUMPING SYSTEM (Group 2)
Ref P&ID: P22-DWG-09-009-02-09
3.2.1 HIGH-PRESSURE PUMPING SYSTEM Equipment
3.2.2 HIGH-PRESSURE PUMPING SYSTEM Instruments
31 of 48
© BW Water

============================================================
--- PAGE 32 ---
============================================================
3.2.1 HIGH-PRESSURE PUMPING SYSTEM PROCESS DESCRIPTION
The High-Pressure Pumping System enables operation of a two-stage RO process by establishing and
redistributing hydraulic pressure within the membrane train. The system combines mechanical pressure generation
and hydraulic pressure recovery so that pressure energy is reused across both RO stages rather than dissipated.
In a two-stage RO configuration, the feed entering the first RO stage must be raised to a pressure sufficient to
overcome osmotic pressure and hydraulic losses. This initial pressure rise is provided by the high-pressure feed
pump (BH-09-001), which establishes the baseline pressure level for the membrane system. The pump supplies
only the portion of pressure that cannot be recovered internally.
As feed passes through the first RO stage, pressure is partially consumed to drive permeation. The first-stage
reject exits the membranes at a reduced but still significant pressure. This reject stream is routed through the
interstage turbocharger (SIP-09-002), where its pressure energy is hydraulically transferred to the feed entering
the second RO stage. Within the interstage turbocharger, pressure from the reject stream is exchanged with the
lower-pressure feed stream, resulting in a pressure boost without additional mechanical input.
Following the second RO stage, the final reject stream retains additional recoverable pressure energy. This stream
is directed to the feed turbocharger (SIP-09-001), where pressure energy from the second-stage reject is
transferred back to the incoming feed upstream of the RO system. This recovered pressure increases the inlet
pressure to the membrane train and correspondingly reduces the pressure rise required from the high-pressure
feed pump (BH-09-001).
From a theoretical standpoint, both turbochargers (SIP-09-001 and SIP-09-002) function as hydraulic pressure
transfer devices, not pressure-generating machines. They do not create pressure independently; instead, they
redistribute pressure energy already present in the reject streams. The magnitude of pressure boosting achieved
depends on AVAILABLE reject pressure, feed-to-reject flow balance, and device efficiency, rather than on active
control or external power input.
The combined action of the high-pressure feed pump (BH-09-001), interstage turbocharger (SIP-09-002), and feed
turbocharger (SIP-09-001) produces a distributed pressure profile across the two-stage RO system. Mechanical
energy input is concentrated at the pump, while recovered hydraulic energy is reused between and downstream
of the RO stages. This arrangement minimizes pressure dissipation, reduces overall power demand, and limits
mechanical loading on the high-pressure pump.
In essence, the High-Pressure Pumping System enables stable two-stage RO operation by converting reject
pressure from each stage into useful driving force for the next stage, forming an internal hydraulic energy-recovery
loop within the membrane process.
32 of 48
© BW Water

============================================================
--- PAGE 33 ---
============================================================
3.2.2 HIGH-PRESSURE PUMPING SYSTEM CONTROL AND OPERATION
The High-Pressure Pumping System is controlled to deliver stable and adequate pressure to the two-stage RO
membrane system while maximizing pressure recovery from reject streams. Operation focuses on coordinated
control of the high-pressure feed pump and monitoring pressure transfer across the feed and interstage
turbochargers. The system does not perform flow or quality control and operates in response to upstream feed
availability and downstream membrane hydraulic demand.
Automatic control actions are limited to pressure generation via pump speed control, valve actuation for isolation
and protection, and continuous monitoring of pressures, flows, and equipment condition. All control and protection
functions described herein are internal to the High-Pressure Pumping System, with upstream reference to Group
1 limited to feed availability only.
High-Pressure Feed Pump (BH-09-001)
The high-pressure feed pump (BH-09-001) is the only actively controlled equipment within the High-Pressure
Pumping System. The pump is driven by a variable speed drive and regulated by a discharge pressure control
loop (PID) to maintain the required feed pressure to the first-stage RO membranes.
Pump start-up is initiated in automatic or remote mode once all upstream permissive conditions are satisfied.
Suction conditions are verified prior to start by monitoring pump suction pressure using PIT-09-001, ensuring
adequate inlet pressure is AVAILABLE to prevent cavitation.
Upon receipt of a start command, the pump is started at minimum VSD speed to establish initial flow and stabilize
hydraulic conditions within the discharge piping and RO feed header.
Following a successful start, pump speed is ramped up gradually by the VSD to increase discharge pressure in a
controlled manner. The ramp-up rate is limited to avoid hydraulic shock, membrane stress, and excessive transient
loading on downstream equipment.
During ramp-up, pump discharge pressure measured at PIT-09-002 is continuously monitored. If abnormal
conditions occur; such as low suction pressure detected by PIT-09-001 or excessive discharge pressure at PIT-
09-002; the ramp-up sequence is halted and alarms or pump shutdown actions are initiated in accordance with the
protection logic.
Once the required discharge pressure is reached and stabilized, the pump transitions into normal closed-loop
pressure control.
The process variable (PV) for the control loop is the pump discharge pressure measured at PIT-09-002. The
manipulated variable (MV) is the pump speed command to the VSD. The controlled variable (CV) is the first-stage
RO feed pressure. Pump speed is adjusted automatically to maintain discharge pressure within the normal
33 of 48
© BW Water

============================================================
--- PAGE 34 ---
============================================================
operating range defined by the process design; the high-pressure pump discharge pressure setpoint shall be
established to meet the RO Stage 1 feed pressure requirement under worst-case operating conditions, including
start-up and scenarios where turbocharger energy recovery is unAVAILABLE. Turbochargers operate as passive
hydraulic devices and do not impose independent pressure requirements or participate in control. Any pressure
recovered by the turbochargers is treated as a hydraulic offset that reduces pump duty without altering the pressure
control setpoint (ensures stable RO operation while inherently accommodating turbocharger performance across
the full operating envelope).
RO system hydraulic continuity is confirmed by permeate and reject flow indication measured on the common
permeate and reject headers using FIT-09-003 and FIT-09-004. These signals are used for indication and
protection only to confirm that flow is established through the RO membrane system and do not participate in
closed-loop control of the high-pressure pump.
Feed Turbocharger (SIP-09-001)
The feed turbocharger (SIP-09-001) is a passive hydraulic energy recovery device that transfers pressure energy
from the second-stage RO reject stream to the incoming RO feed upstream of the high-pressure pump. The unit
does not generate pressure independently and does not participate in any closed-loop control or regulation.
Under normal design operating conditions, the second-stage reject stream exits at approximately 59-60 barg. The
feed turbocharger hydraulically recovers a portion of this residual pressure and transfers it to the feed stream,
providing an effective pressure boost depending on operating flow and recovery conditions. This reduces the net
pressure rise required from the high-pressure feed pump to achieve the required Stage 1 RO feed pressure.
The feed turbocharger operates automatically whenever sufficient reject pressure and flow are AVAILABLE.
Pressure recovery varies naturally with reject-side hydraulic conditions and requires no operator intervention.
Pressure at the reject inlet is monitored by PIT-09-007, installed on the second-stage RO reject (brine) line
immediately upstream of the feed turbocharger inlet, to confirm AVAILABLE reject pressure and detect abnormal
hydraulic conditions. The boosted feed pressure downstream of the feed turbocharger is monitored by PIT-09-003,
installed on the RO Stage 1 feed line downstream of SIP-09-001, to indicate recovered pressure contribution and
support alarm functions. PIT-09-008 at the feed turbocharger reject outlet indicates reject (brine) discharge
pressure downstream of the feed turbocharger to monitor AVAILABLE energy recovery pressure and detect
abnormal hydraulic conditions. These PITs are for indication and alarm only and do not participate in control.
34 of 48
© BW Water

============================================================
--- PAGE 35 ---
============================================================
Interstage Turbocharger (SIP-09-002)
The interstage turbocharger (SIP-09-002) transfers hydraulic pressure energy from the RO Stage 1 reject stream
to the RO Stage 2 feed stream, enabling pressure reuse between RO stages without additional mechanical energy
input.
Based on design conditions, the RO Stage 2 feed stream downstream of the interstage turbocharger is
approximately 77 barg, with a corresponding Stage 2 brine outlet pressure of approximately 46 barg. The interstage
turbocharger recovers a portion of the Stage 1 reject pressure and transfers it hydraulically to the Stage 2 feed,
increasing the AVAILABLE feed pressure to the second-stage RO membranes while reducing the pressure duty
required from upstream pumping.
The interstage turbocharger operates passively through hydraulic coupling and does not participate in pressure,
flow, or recovery control loops. Pressure transfer varies naturally with reject pressure, feed flow, and system
recovery.
Interstage pressures are monitored for indication and alarm purposes only using the following instruments:
• PIT-09-004, installed on the RO Stage 1 reject line immediately upstream of the interstage turbocharger
inlet, to confirm AVAILABLE reject pressure for energy transfer.
• PIT-09-005, installed on the RO Stage 2 feed line immediately downstream of the interstage turbocharger
outlet, to indicate boosted feed pressure entering RO Stage 2.
• PIT-09-006, installed on the RO Stage 2 feed line upstream of the interstage turbocharger, to provide a
reference pressure for evaluating pressure gain across SIP-09-002.
These instruments do not participate in closed-loop control and are provided solely to indicate interstage hydraulic
conditions and generate alarms under abnormal operation.
*** See alarm and setpoint lists for specific details.
Second-Stage Brine Bypass Control
Under normal seawater operating conditions (approximately 53,000 ppm TDS), the second-stage RO brine stream
exits the membrane system at sufficiently high pressure, typically in the range of 75-83 barg. Under these
conditions, adequate hydraulic energy is AVAILABLE for stable operation of the feed turbocharger, and the brine
bypass valve VE-09-002 remains closed, allowing the full second-stage brine flow to pass through the turbocharger
for maximum energy recovery with no bypass flow.
At reduced salinity conditions (approximately 43,000 ppm TDS), second-stage brine pressure decreases to
approximately 59-61 barg, reducing the amount of recoverable hydraulic energy AVAILABLE to the feed
turbocharger. To maintain stable turbocharger operation and prevent operation outside vendor-defined limits, a
portion of the second-stage brine flow is diverted through the bypass line. Typical bypass flow under these
conditions is approximately 3.2-3.3 m³/h, with the remaining brine continuing through the turbocharger for partial
energy recovery.
35 of 48
© BW Water

============================================================
--- PAGE 36 ---
============================================================
The control system continuously evaluates feed turbocharger operating conditions using pressure measurements
on both sides of the device. Second-stage RO brine pressure upstream of the feed turbocharger, measured by
PIT-09-007, represents the AVAILABLE reject-side hydraulic energy and is used to identify a low reject pressure
condition when it falls below a threshold. The recovered pressure delivered to the RO Stage 1 feed downstream
of the feed turbocharger, measured by PIT-09-003, represents the effectiveness of pressure transfer across the
turbocharger. Degradation of effective pressure gain is evaluated from the relationship between PIT-09-007 (reject-
side pressure) and PIT-09-003 (recovered feed pressure).
When either a low reject pressure condition is identified by PIT-09-007, OR the effective pressure gain inferred
from PIT-09-007 and PIT-09-003 degrades below the minimum criterion, the control system progressively opens
the brine bypass valve VE-09-002 to unload the turbocharger by diverting a portion of the second-stage brine flow.
As operating conditions recover, the bypass valve is correspondingly closed to restore energy recovery. Valve
modulation is performed gradually to maintain hydraulic stability and avoid oscillation.
The reject pressure threshold and minimum effective pressure gain criteria used in this logic define the lower
boundary of stable turbocharger operation. These parameters are established, validated, and tuned during testing
and commissioning (T&C) in coordination with the turbocharger vendor based on observed site operating
conditions and vendor performance characteristics. Following commissioning, the logic operates using the
configured parameters, with any subsequent changes made only through authorized configuration adjustments.
During start-up and shutdown, hydraulic conditions are inherently transient and unstable. VE-09-002 is therefore
commanded open to unload the feed turbocharger and prevent unstable operation. Closing VE-09-002 during start-
up would force 100% of the Stage 2 brine flow through the feed turbocharger immediately, which can create
operational issues if reject pressure and flow are not yet within a “NOT FAULT” and stable range (e.g., low reject
pressure, fluctuating flow, or incomplete hydraulic stabilization). Once steady-state RO operation is established
and stable reject-side conditions are confirmed, VE-09-002 is progressively closed to restore maximum energy
recovery.
Turbocharger Isolation Valves
Motorized valve VE-09-007 is provided as on/off isolation valves to allow positive hydraulic isolation of the feed
and interstage turbochargers during maintenance, CIP preparation, or abnormal operating conditions. This valve
is normally open during RO operation. When closed, the associated turbocharger is isolated, and its energy
recovery function is disabled.
36 of 48
© BW Water

============================================================
--- PAGE 37 ---
============================================================
3.2.2 HIGH-PRESSURE PUMPING SYSTEM PERMISSIVE
The High-Pressure Pumping System shall be permitted to operate when the following conditions are satisfied:
• RO/Membrane System READY, and
• High-pressure feed pump BH-09-001 AVAILABLE and NOT FAULT, and
• Pump suction pressure NOT FAULT as indicated by PIT-09-001, and
• Pump discharge pressure NOT FAULT as indicated by PIT-09-002, and
• Turbocharger isolation valve VE-09-007 and VE-09-007 AVAILABLE and NOT FAULT, and
• Feed turbocharger (SIP-09-001) pressure transmitters PIT-09-007 and PIT-09-003 AVAILABLE and NOT
FAULT, and
• Interstage turbocharger (SIP-09-002) pressure transmitters PIT-09-004, PIT-09-005, and PIT-09-006
AVAILABLE and NOT FAULT, and
• Permeate and reject flow indication FIT-09-003 and FIT-09-004 AVAILABLE and NOT FAULT,
• System selected in REMOTE and AUTO, and
• No active trip or protection within the High-Pressure Pumping System.
• VE-09-002 is in AUTO and NOT FAULT, and
• VE-09-006 is in AUTO and NOT FAULT, and
• VE-09-013 is Fully closed, and
• VE-09-014 is fully CLOSED.
IF the above conditions are satisfied, THEN high-pressure feed pump is permitted to start and continue operation,
and the feed and interstage turbochargers are permitted to operate passively based on hydraulic conditions.
37 of 48
© BW Water

============================================================
--- PAGE 38 ---
============================================================

| | Item | | | Equipment Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | RO Stage 1 Membrane Train | | | BOI-09-001 | | |
| 2 | | | RO Stage 2 Membrane Train | | | BOI-09-002 | | |


| | Item | | | Instrument Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | RO Membrane System Differential Pressure Transmitter (Overall Membrane<br>Resistance) | | | PDIT-09-003 | | |
| 2 | | | Permeate Conductivity Analyzer (Common Permeate Header) | | | AIT-09-002 | | |
| 3 | | | Stage-Level Permeate Conductivity Analyzer | | | AIT-09-003 | | |
| 4 | | | RO Stage 2 Permeate Flow Transmitter (Stage-Level Permeate Production<br>Prior To Mixing) | | | FIT-09-001 | | |
| 5 | | | Common Permeate Flow Transmitter (Total RO Permeate Production) | | | FIT-09-003 | | |
| 6 | | | RO Reject / Brine Flow Transmitter (Common Reject Header) | | | FIT-09-004 | | |
| 7 | | | Permeate Conductivity Analyzer (Stage-Level Permeate Line Upstream of<br>Common Header) | | | AIT-09-003 | | |
| 8 | | | RO Stage 1 Reject / Interstage Conductivity Analyzer | | | AIT-09-004 | | |
| 9 | | | RO Stage 2 Reject Conductivity Analyzer | | | AIT-09-005 | | |
| 10 | | | Motorized Valve (Permeate to Product) with Limit Switches | | | VE-09-003 | | |
| 10 | | | Motorized Valve (Permeate to Off-Spec Diversion) with Limit Switches | | | VE-09-004 | | |

3.3 RO / MEMBRANE SYSTEM (Group 3)
Ref P&ID: P22-DWG-09-009-02-09
3.3.1 RO / MEMBRANE SYSTEM EQUIPMENT
3.3.2 RO / MEMBRANE SYSTEM INSTRUMENTATION
3.3.3 RO / MEMBRANE SYSTEM PROCESS DESCRIPTION
The RO / Membrane System performs the core desalination function of the plant by separating dissolved salts from
the pressurized feed stream through a two-stage reverse osmosis (RO) configuration. Pressurized feed supplied
by the High-Pressure Pumping System enters the RO membrane system at the required operating pressure and
is distributed to the membrane vessels, where separation into permeate and reject streams occurs across semi-
permeable RO membranes. The system is designed to maximize overall water recovery while maintaining stable
membrane operation and acceptable hydraulic conditions across both RO stages.
The RO system is configured as a single (1 × 100%) two-stage RO train, with a total feed flow of approximately 49
m³/h and a total design permeate capacity of approximately 21 m³/h. The membrane arrangement consists of six
38 of 48
© BW Water

============================================================
--- PAGE 39 ---
============================================================
(6) pressure vessels in RO Stage 1 and four (4) pressure vessels in RO Stage 2, with seven (7) membrane
elements per vessel.
In RO Stage 1, the incoming pressurized feed is introduced to the Stage 1 membrane vessels. A portion of the
feed passes through the membranes as permeate and is discharged at near-atmospheric pressure to the permeate
collection header. The remaining concentrated stream exits the Stage 1 membrane vessels as reject and is routed
onward to RO Stage 2 through the interstage connection.
In RO Stage 2, the partially desalinated feed from Stage 1 is further processed through the Stage 2 membrane
vessels. Additional permeate is extracted and routed to the same permeate collection header as Stage 1 permeate.
The reject stream from RO Stage 2 exits the membrane system and is routed downstream (RO Reject stream by
client)
Permeate streams from RO Stage 1 and RO Stage 2 are combined in a common permeate header. Final permeate
quality is represented by a conductivity analyzer installed upstream of the common permeate header, providing
indication of blended permeate quality from the complete RO system.
Stage-level and system-level hydraulic conditions within the RO membrane system are represented by differential
pressure measurements across the RO membrane. Differential pressure indicators installed across RO Stage 1
and RO Stage 2 provide indication of membrane resistance and fouling tendencies. These instruments represent
membrane hydraulic characteristics only and do not alter process flow or participate in control.
The RO / Membrane System is limited to the physical separation of feed into permeate and reject streams within
the membrane vessels. Pressure generation, pressure recovery, hydraulic control, and pump operation are
handled by the High-Pressure Pumping System, while downstream permeate handling, diversion, and disposal
functions are addressed in other system groups.
3.3.4 RO / MEMBRANE SYSTEM OPERATIONS AND CONTROL
The RO / Membrane System is controlled to monitor membrane hydraulic performance, assess permeate quality,
and determine off-spec conditions. Control actions within this group are limited to monitoring, quality evaluation,
and permeate routing commands. The system does not regulate pressure or flow and does not modulate upstream
equipment.
The detailed operational logic for RO startup, shutdown, flushing, transition between operating states, and
interaction with the CIP system shall be defined in a dedicated RO Control / Sequence Chart, issued as a separate
document. This section describes control intent and functionality only.
39 of 48
© BW Water

============================================================
--- PAGE 40 ---
============================================================
RO Membrane Trains (Stage 1 and Stage 2)
The RO membrane trains comprise Stage 1 and Stage 2 membrane vessels operating in series. Membrane
hydraulic condition across the combined RO membrane system is monitored using differential pressure
transmitter PDIT-09-003, installed across the membrane train as shown on the P&ID.
The signal from PDIT-09-003 provides indication of overall membrane resistance and is used for monitoring,
alarming, and performance trending. Increasing or abnormal differential pressure indicates membrane fouling,
scaling, or blockage. This instrument does not initiate any hydraulic control actions and does not influence feed
pressure, flow, or recovery.
Permeate Outlet - Flow & Quality Monitoring
The combined permeate outlet from the RO membrane system is equipped with a conductivity analyzer consisting
of AIT-09-002, installed upstream of the common permeate system header. The conductivity signal represents the
final blended permeate quality from all RO stages and is evaluated to determine overall permeate acceptability.
A flow meter (FIT-09-003) installed at the common permeate header measures the total permeate production rate
from the RO system. This measurement provides operators with real-time indication of RO output and supports
performance monitoring, trending, and mass balance calculations such as RO recovery. The permeate flow signal
is used primarily for indication, reporting, and performance assessment rather than direct control.
In addition to combined permeate monitoring, stage-level performance is monitored upstream of the common
permeate header. A flow transmitter (FIT-09-001) installed at the RO Stage 2 permeate outlet indicates second-
stage permeate production prior to mixing. This measurement is used to monitor stage-level hydraulic performance
and recovery distribution between RO stages.
A conductivity analyzer (AIT-09-003) provides stage-specific permeate quality indication. This measurement
supports early detection of membrane performance degradation or integrity issues at the stage level before effects
are observed on the combined permeate stream.
RO Reject, Off spec and Intermediate Streams
Conductivity analyzers AE-09-004 / AIT-09-004 and AE-09-005 / AIT-09-005, installed on RO reject and
intermediate streams as shown on the P&ID, provide supplementary indication of membrane stage performance
and salt balance.
These analyzers are used for monitoring and diagnostic purposes only.
An off-spec condition is determined within the RO / Membrane System based on permeate quality. Permeate
conductivity measured by AE-09-002 / AIT-09-002 is evaluated against the defined acceptable quality limit.
When the measured permeate conductivity exceeds the allowable limit for a validated duration, the RO / Membrane
System declares an off-spec condition. This declaration represents a quality-based status used to initiate permeate
routing actions.
Permeate routing downstream of the RO membrane system is executed using motorized valves installed on the
permeate outlet piping.
40 of 48
© BW Water

============================================================
--- PAGE 41 ---
============================================================
• VE-09-003 - Permeate to product
• VE-09-004 - Permeate to off-spec
Under normal operating conditions, VE-09-003 is open and VE-09-004 is closed. Upon declaration of an off-spec
condition, VE-09-003 is closed and VE-09-004 is opened to divert permeate away from the product system. Valve
position feedback is monitored to confirm correct routing.
From Client side, two (2) Digital Output (DO), dry free contact signals shall be provided to the RO plant control
system:
(1) Permissive to fill Permeate Tank, and
(2) Permissive to fill Off Spec Tank.
The logic of the Client DO signals (received as DI in the RO plant control system) is: TRUE (1) means permissive
to fill the tank, and FALSE (0) means not allowed to fill the tank. These permissive signals shall be used as
interlocks to enable the respective filling/diverting valves. Loss of signal shall default to FALSE (0) (not allowed to
fill the tank) as fail-safe.
RO Performance Monitoring Indicators
RO system performance is monitored using calculated indicators derived from existing flow and conductivity
measurements to provide visibility of hydraulic balance and membrane separation efficiency. These indicators are
intended to support operational awareness, performance trending, and diagnostic assessment during normal RO
operation.
Overall RO recovery is calculated using a mass balance across the membrane system based on permeate and
reject flow measurements. RO recovery is determined as the ratio of common permeate flow measured by FIT-09-
003 to the sum of permeate flow (FIT-09-003) and reject (brine) flow measured by FIT-09-004, expressed as a
percentage. This calculated value provides indication of the fraction of pressurized feed converted to permeate
and supports monitoring of recovery trends and operating stability.
RO Recovery (%) = FIT-09-003 / (FIT-09-003 + FIT-09-004) × 100
This calculation assumes steady-state operation and is intended for trending rather than instantaneous control.
Membrane salt separation performance is represented by an indicative salt rejection calculation derived from
conductivity measurements on the permeate and reject streams. Salt rejection is calculated by comparing
permeate conductivity measured by AIT-09-002 against reject conductivity measured by AIT-09-005, expressed
as a percentage. Where applicable, an interstage salt rejection indicator may also be derived using conductivity
measured on the Stage 1 reject (interstage) line upstream of the interstage turbocharger. These calculated values
provide visibility of membrane separation behavior and support trending and diagnostic evaluation of membrane
performance over time.
41 of 48
© BW Water

============================================================
--- PAGE 42 ---
============================================================
Overall Salt Rejection (%) = [1 − (AIT-09-002 / AIT-09-005)] × 100
Interstage Salt Rejection Indicator (%) = [1 − (AIT-09-002 / AIT-09-004)] × 100
Stage-2 Salt Rejection (%)= [1 − (AIT-09-003 / AIT-09-004)] × 100
CIP Trigger Indication
The RO membrane system provides performance indications that may prompt evaluation for Cleaning-in-Place
(CIP). These indications include sustained or increasing differential pressure indicated by PDIT-09-003 and
persistent degradation of permeate quality indicated by AE-09-002 / AIT-09-002.
These indications support maintenance decision-making only. CIP execution is handled within the CIP system and
documented separately. More details provided in the CIP Group Section.
42 of 48
© BW Water

============================================================
--- PAGE 43 ---
============================================================
3.3.4 RO / MEMBRANE SYSTEM READY PERMISSIVES
The RO / Membrane System shall be permitted to operate when the following conditions are satisfied:
• No active fault or trip is present within the RO / Membrane System, and
• Differential pressure indication across the RO membrane system (PDIT-09-003) is AVAILABLE and NOT
FAULT, and
• Permeate conductivity analyzer (AE-09-002 / AIT-09-002) is AVAILABLE and NOT FAULT, and
• Permeate routing valve VE-09-003 (permeate to product) is AVAILABLE and able to operate, and
• Off-spec diversion valve VE-09-004 (permeate to off-spec) is AVAILABLE and able to operate, and
• Client Permeate Tank permissive signal is AVAILABLE and NOT FAULT, and
• Client Off-Spec Tank permissive signal is AVAILABLE and NOT FAULT, and
• System is selected in REMOTE and AUTO.
IF the above conditions are satisfied, THEN RO / Membrane System is considered AVAILABLE for operation.
43 of 48
© BW Water

============================================================
--- PAGE 44 ---
============================================================

| | Item | | | Equipment Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | CIP Tank | | | TK-09-001 | | |
| 2 | | | CIP Pump | | | BH-09-002 | | |
| 3 | | | CIP Heater | | | REL-09-001 | | |
| 4 | | | CIP Cartridge Filter | | | FIL-09-002 | | |


| | Item | | | Instrument Description | | | Tag No. | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | CIP Tank Level Transmitter | | | LIT-09-002 | | |
| 2 | | | CIP Solution Temperature Element | | | TE-09-002 | | |
| 3 | | | CIP Solution Temperature | | | TIT-09-001 | | |
| 4 | | | CIP Solution pH Analyzer | | | AIT-09-001 | | |
| 5 | | | CIP Circulation Flow Transmitter | | | FIT-09-005 | | |
| 6 | | | Motorized Valve - CIP Make-up / Chemical Fill with Limit Switches | | | VE-09-005 | | |
| 7 | | | Motorized Valve – Interstage Isolation Valve with Limit Switches | | | VE-09-007 | | |
| 8 | | | Motorized Valve - CIP Return from RO Stage 1 with Limit Switches | | | VE-09-009 | | |
| 9 | | | Motorized Valve - CIP Return from RO Stage 2 with Limit Switches | | | VE-09-010 | | |
| 10 | | | Motorized Valve - CIP Feed to RO Stage 1 with Limit Switches | | | VE-09-012 | | |
| 11 | | | Motorized Valve - CIP Feed to RO Stage 2 Path with Limit Switches | | | VE-09-013 | | |

3.6 CIP/FLUSHING SYSTEM (GROUP 4)
Ref P&ID: P22-DWG-09-009-02-10
3.6.1 CIP/FLUSHING SYSTEM EQUIPMENT
3.6.2 CIP/FLUSHING SYSTEM INSTRUMENTATION
3.6.3 CIP PROCESS DESCRIPTION
The CIP / Flushing System is provided to prepare, store, heat, circulate, and return cleaning solutions for periodic
chemical cleaning of the RO membrane system. The system operates independently of normal RO production and
is used only when the RO membrane system is isolated and placed in CIP mode.
Cleaning solution is prepared and stored in the CIP tank TK-09-001, which provides sufficient volume for circulation
through the RO membrane stages. The tank is equipped with level indication to allow monitoring of AVAILABLE
solution volume during preparation and circulation.
44 of 48
© BW Water

============================================================
--- PAGE 45 ---
============================================================
Heating of the CIP solution is provided by the CIP heater REL-09-001, enabling the solution to reach and maintain
the required cleaning temperature prior to and during circulation. The heated solution is circulated from the CIP
tank through the RO membrane system and returned to the tank, forming a closed-loop circulation path.
Circulation of the CIP solution is achieved using the CIP pump BH-09-002, which draws solution from the CIP tank
and delivers it through the CIP piping, cartridge filter, and RO membranes before returning to the tank. A cartridge
filter FIL-09-002 is installed in the CIP circulation line to remove suspended solids and protect the RO membranes
during cleaning.
The chemical condition of the CIP solution is monitored to verify solution suitability during cleaning. Flow,
temperature, pressure, level, and pH measurements provide visibility of CIP operating conditions but do not alter
the hydraulic configuration of the RO system.
CIP solution routing to and from the RO membrane system is achieved through dedicated CIP feed and return
piping equipped with motorized isolation valves. These valves allow individual or collective cleaning of RO
membrane stages as required. Upon completion of circulation, the CIP solution is either retained in the tank or
drained for disposal.
45 of 48
© BW Water

============================================================
--- PAGE 46 ---
============================================================
3.6.4 CIP OPERATION AND CONTROL
The CIP / Flushing System operates in a dedicated CIP mode and is enabled only when the RO membrane system
is confirmed isolated via an RO system status signal. Control actions are supervisory and sequence-based, with
interlocks and alarms provided to ensure safe and effective cleaning.
Detailed execution of CIP steps is defined in the CIP sequence charts.
CIP Tank - TK-09-001
The CIP tank TK-09-001 stores the cleaning solution required for membrane cleaning. Tank level is monitored
using LI-09-001 and LIT-09-002. These signals are used for indication, alarming, and pump protection only. No
automatic level control is implemented.
High-level and low-level alarms alert operators to abnormal filling or depletion. Low-Low level (LALL) conditions
are used to inhibit or trip the CIP pump to prevent dry running.
The CIP heater REL-09-001 is provided to heat the CIP cleaning solution in TK-09-001 prior to and during
circulation. CIP solution temperature is monitored using TE-09-002 / TIT-09-001. Heater operation is controlled in
ON/OFF mode based on the measured CIP solution temperature and a configured temperature setpoint for the
selected CIP phase. When the measured temperature is below the setpoint (minus deadband), the heater is
energized; when the measured temperature reaches the setpoint (plus deadband), the heater is de-energized.
Heater operation is enabled only when the CIP system is in CIP mode and sufficient tank level is confirmed. High
temperature alarms are provided to protect equipment and maintain chemical stability.
CIP Pump - BH-09-002
