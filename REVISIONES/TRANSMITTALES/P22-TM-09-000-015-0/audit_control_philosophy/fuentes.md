# FUENTES CONSOLIDADAS — Auditoria Multi-Audit Plant Control Philosophy Rev B
================================================================================

## 1. CONTROL PHILOSOPHY REV A (ENTREGA 14, 06-Mar-2026) — TEXTO COMPLETO
================================================================================

============================================================
--- PAGE 1 ---
============================================================
 
 
                                                                                                                                                                
 
 
  
Document Title  
 
Second Stage RO Module for Brine – PD Ta ltal 
 
  
ADASACode: P22-BT-09-009-001 
Date: 06/23/2026 
Revision No.: A  
Page: 1of 48 
 
 
 
 
  
  
 
 
 
Control Philo sophy  
Second Stage RO Module for Brine – PD Taltal  
ADASA C ode : P22-BT-09-009-001 
 
 
 
 
 
 
 
  
       
       
A 2026/03/06  JON DS/YFV  AS/GHY/NHH  JR  
Rev Date  Prepared By  Reviewed 
By Checked  By Approved 
By Customer  


============================================================
--- PAGE 2 ---
============================================================
 
 2 of 48 
© BW Water  
 
Contents  
1.1 PLC PLATFORM ................................ ................................ ................................ ................................ .............. 6 
1.2 OPERATOR INTERFACE PLATFORM ................................ ................................ ................................ ............. 6 
1.3 POWER INTERRUPTION / POWER UP  ................................ ................................ ................................ ........... 6 
1.4 OPERATOR INTERFACE ................................ ................................ ................................ ................................ .6 
1.4.1 PASSWORD ACCESS & PRIVILEGES  ................................ ................................ ................................ ............ 6 
1.4.2 GUEST PRIVILEGES  ................................ ................................ ................................ ................................ .......6 
1.4.3 OPERATOR PRIVILEGES ................................ ................................ ................................ ................................ 7 
1.4.4 SUPERVISOR PRIVILEGES ................................ ................................ ................................ ............................. 7 
1.4.5 ADMINISTRATOR PRIVILEGES  ................................ ................................ ................................ ...................... 7 
1.5 HMI DISPLAY COLOR CODING  ................................ ................................ ................................ ...................... 7 
1.5.1 UNITS/DRIVE MOTORS  ................................ ................................ ................................ ................................ ...7 
1.5.2 MEASURED VALUES  ................................ ................................ ................................ ................................ ......8 
1.5.3 SCREEN NAVIGATION  ................................ ................................ ................................ ................................ ....8 
1.5.4 ALARMS  ................................ ................................ ................................ ................................ .......................... 9 
1.5.5 SEQUENCERS  ................................ ................................ ................................ ................................ .............. 10 
1.5.6 HMI SEQUENCER OBJECT ................................ ................................ ................................ ........................... 10 
 
  
2.1 MOTOR CONTROL FUNCTION  ................................ ................................ ................................ ..................... 11 
2.1.1 MOTOR CONTROL - DIRECT ONLINE (DOL)  ................................ ................................ ................................ 11 
2.1.2 MOTOR CONTROL - SOFT START  ................................ ................................ ................................ ............... 11 
2.1.3 MOTOR CONTROL - VSD ................................ ................................ ................................ .............................. 13 
2.1.4 EQUIPMENT DUTY / STANDBY  ................................ ................................ ................................ .................... 15 
2.1.5 PUMP FAILURE TO START / STOP LOGIC  ................................ ................................ ................................ ...15 
2.2 INSTRUMENTATION AND CONTROL FUNCTIONS  ................................ ................................ ...................... 16 
2.2.1 ANALOG TRANSMITTER/ANALYZER (LIT, FIT, AIT)  ................................ ................................ .................... 16 
2.2.2 SWITCHES (LS)  ................................ ................................ ................................ ................................ ............. 18 
2.3 VALVE CONTROL - MOTOR OPERATED ON/OFF ................................ ................................ ........................ 18 

============================================================
--- PAGE 3 ---
============================================================
 
 3 of 48 
© BW Water  
 
2.4 PROPORTIONAL INTEGRAL DERIVATIVE (PID) CLOSED LOOP CONTROL  ................................ .............. 21 
2.5 CHEMICAL DOSING CONTROL RATIO CONTROL (OPEN LOOP CONTROL)  ................................ ............. 23 
 
3.1 FEED PREPARATION SYSTEM( GROUP 1)  ................................ ................................ ................................ ..26 
3.1.1 FEED PREPARATION SYSTEM EQUIPMENT ................................ ................................ ......................... 26 
3.1.2 FEED PREPARATION SYSTEM INSTRUMENTS ................................ ................................ .................... 26 
3.1.3 FEED PREPARATION SYSTEM PROCESS DESCRIPTION  ................................ ................................ ..26 
3.1.3 FEED PREPARATION SYSTEM CONTROL & OPERATION  ................................ ................................ ..28 
3.1.4 FEED PREPARATION SYSTEM OPERATION X READY PERMISSIVE  ................................ ............... 30 
3.2 HIGH -PRESSURE PUMPING SYSTEM (GROUP 2)  ................................ ................................ ....................... 31 
3.2.1 HIGH -PRESSURE PUMPING SYSTEM EQUIPMENT ................................ ................................ ............. 31 
3.2.2 HIGH -PRESSURE PUMPING SYSTEM INSTRUMENTS  ................................ ................................ ........ 31 
3.2.1 HIGH -PRESSURE PUMPING SYSTEM PROCESS DESCRIPTION  ................................ ...................... 32 
3.2.2 HIGH -PRESSURE PUMPING SYSTEM CONTROL AND OPERATION  ................................ ................ 33 
3.2.2 HIGH -PRESSURE PUMPING SYSTEM PERMISSIVE  ................................ ................................ ............ 37 
3.3 RO / MEMBRANE SYSTEM (GROUP 3) ................................ ................................ ................................ ......... 38 
3.3.1 RO / MEMBRANE SYSTEM EQUIPMENT (X=A/B/C)  ................................ ................................ .............. 38 
3.3.2 RO FEED AND PRE -FILTRATION INSTRUMENTATION ................................ ................................ ........ 38 
3.3.3 RO / MEMBRANE SYSTEM PROCESS DESCRIPTION  ................................ ................................ ......... 38 
3.3.4 RO / MEMBRANE SYSTEM OPERATIONS AND CONTROL  ................................ ................................ .39 
3.3.4 RO / MEMBRANE SYSTEM READY PERMISSIVES  ................................ ................................ ............... 43 
3.6 CIP/FLUSHING SYSTEM (GROUP 6) ................................ ................................ ................................ ............. 44 
3.6.1 CIP STORAGE TANK & INSTRUMENTATION  ................................ ................................ ......................... 44 
3.6.2 CIP PUMPS, FILTER & INSTRUMENTATION (X=A/B) ................................ ................................ ............ 44 
3.6.3 CIP PROCESS DESCRIPTION  ................................ ................................ ................................ .................. 44 
3.6.4 CIP OPERATION AND CONTROL ................................ ................................ ................................ ............. 46 
3.6.5 CIP READY PERMISSIVES ................................ ................................ ................................ ........................ 48 

============================================================
--- PAGE 4 ---
============================================================
 
 4 of 48 
© BW Water  
 
3.6.6 CIP START/STOP AUTOMATIC SEQUENCE  ................................ ................................ .......................... 48 
 
  

============================================================
--- PAGE 5 ---
============================================================
 
 5 of 48 
© BW Water  
 
 
GENERAL INFORMATION  
The reader should refer to the Piping and Instrumentation Diagrams (P&ID’s) , and the documents described below 
for a complete understanding of the plant control.  This document is only providing an overview of the Treatment 
Plant controls, the details are described in the Operati ng Sequence Chart and Alarm and Control Setpoint List . 
The PLC follows specific steps to automatically control valves, pumps, etc. during the operating states for the 
treatment plant.  These steps are listed and described in the Operating S equence Charts.  
Also, the details of the control actions , setpoints, etc. that are required to operate the plant are given in the Alarm 
and Control Setpoint List . 
Equipment and Train modes, such as AUTO and OFF are shown in full capital letters.  
Table of Reference Documents:  
P&IDs  P22-DWG -09-009-0002  
PFD P22-DWG -09-009-0001 
Controls & Sequence Chart  SEPARATE DOCUMENT  
Alarm and Control Setpoint List  SEPARATE DOCUMENT  
Control System Architecture  P22-CD-09-004-0001 
 
  

============================================================
--- PAGE 6 ---
============================================================
 
 6 of 48 
© BW Water  
 
1.1 PLC PLATFORM  
In the documentation the Programmable Logic Controller is referred to as the PLC.  The PLC provides automated 
control of the equipment.  All the programming for the control of the system is stored in the PLC.  
All PLCs and Remote Input s and Outputs (RIO) associated with this plant share the same network and use it to 
communicate with the HMI system.  The network is configured in a ring for reliability.  
1.2 OPERATOR INTERFACE PLATFORM  
To accommodate equipment operation and all other control, display, and monitoring requirements, this plant 
employs a local Human Machine Interface  (HMI) for access to system controls and archived operating data.   
1.3 POWER INTERRUPTION / POWER UP  
When a loss of power occurs, all pumps are immediately stopped, all actuated valve s are in their fail state (fail 
open/close/last state) .  When power is lost, the system is in OFFLINE state.  
When power is restored, the plant does not restart automatically. To restart the System, press the “SYSTEM 
START” button to restart the  system . 
System Controls and Instrumentation are backed up by an Uninterruptible  Power Supply system (UPS) (refer to 
Control System Architecture drawing).  The UPS will provide 30 minutes of power to ensure the controls and 
instrumentation do not shutdown.  This ensures that the system  will go to a safe OFFLINE state and be ready for 
restart.  
1.4 OPERATOR INTERFACE  
1.4.1 Password Access & Privileges  
The local HMI includes four levels of password protection:  Guest, Operator, Supervisor, and Administrator.  The 
Guest user type does not require a password.  
1.4.2 Guest Privileges  
Navigate through the graphic screens and monitor plant and equipment status . 
  

============================================================
--- PAGE 7 ---
============================================================
 
 7 of 48 
© BW Water  
 
1.4.3 Operator Privileges  
Operator user type shall have the Guest privileges and the following:  
• Monitor pre -sets and setpoints, and to adjust some process control setpoints (not process alarm setpoints) 
as specified in the Control Matrix.  
• Access process train control buttons such as START Sequence and reset alarms . 
• Acknowledge alarms . 
• Place devices such as pumps and valves in AUTO, MANUAL ON or OFF, and designate 
DUTY/STANDBY operation . 
• Access PID controller popup screens, change PID control selections, and adjust PID control parameters 
(except PID tuning parameters) . 
1.4.4 Supervisor Privileges  
The Supervisor user type shall have the Operator privileges and the following:  
• Adjust all setpoints, including alarm and control, as described in the Control Matrix.  
• Adjust PID tuning parameters . 
• Substitute (simulate) Values for Instruments . 
• Set instruments to MAINTENANCE where the instrument is removed from equipment interlocks . 
1.4.5 Administrator Privileges  
The Administrator user type shall have the Supervisor privileges and the following privileges:  
• Security configuration, including adding users and changing passwords . 
• HMI , and application configuration and modification . 
The HMI is configured to log out the current user after one hour of inactivity and/or four hours after logging in.  
1.5 HMI DISPLAY COLOR CODING  
The displays uses the color -coding shown below:  
1.5.1 Units/Drive Motors  
Motors  Motor Stop and no FAULT  RED  
 Motor Run and no FAULT  GREEN  
 FAULT not acknowledged  AMBER AND BLINKING  
 FAULT acknowledged and still existing  AMBER  
Valves  OPEN and no fault  GREEN  

============================================================
--- PAGE 8 ---
============================================================
 
 8 of 48 
© BW Water  
 
 CLOSED and no fault  RED  
 FAULT not acknowledged  AMBER AND BLINKING  
 FAULT acknowledged and still existing  AMBER  
 Valve Transition  BLINKING GREEN AND RED  
Other   same basic colors as motors  
1.5.2 Measured Values  
Analogue measured value 
as digital display  measured value within service range  background colour or equivalent  
 measured value within alarm range, not 
acknowledged  red background, flashing or 
equivalent  
 measured value within alarm range, 
acknowledged  red background or equivalent  
Binary limit value/signal  within service range  green, e.g., point on process 
line/symbol  
From monitor or systems  outside service range (within alarm range)  Red AND flashing or steady, 
depending on state of 
acknowledgement  
1.5.3 Screen Navigation  
There are several ways to navigate through the system.  
• Screen navigation can be performed from equipment buttons at the top or each display . 
• Click on equipment object in System Overview . 
• Click on any navigation arrow.  
Select the symbol for a device such as a blower, or pump to display the MANUAL/OFF/AUTO switch for that device.  
Select a button labelled PID, which is found above the equipment with PID controls, to display the PID loop screen.  
  

============================================================
--- PAGE 9 ---
============================================================
 
 9 of 48 
© BW Water  
 
1.5.4 Alarms  
The purpose of an alarm is to communicate that an operator is expected to take action to rectify or prevent an 
abnormal situation.  
Depending on the nature of the problem, the alarm may be a shutdown alarm (interlock) or an advisory alarm 
(warning).  A shutdown alarm will be generated when the PLC has determined that operation is unsafe or 
undesirable.  Shutdown alarms are typically re set by pressing an Alarm Reset button.  
Advisory (warning) alarms are to notify the operator of an abnormal condition.  The operator is expected to 
acknowledge an advisory alarm by pressing the Acknowledge All button and correct the abnormal situation.  If the 
problem is not corrected, productio n quality and quantity may drop off quickly.  
An alarm that is activated by an instrument such as a pressure transmitter or a flow transmitter typically requires a 
pump or other device to generate the required pressure or flow.  This is referred to “condition active” in this 
document and the Alarm and Control Setpoint List . The alarm is not generated if the device to be protected is off  
or with other specified conditions .   
All alarms are indicated with a message on an alarm banner.  All alarms and the time they occurred are recorded 
on an alarm summary screen  and archived for further reference .  
The Alarms are divided in to 3 categories:  
• Severity 1 - High Priority Alarm (red)  
These alarms are normally associated with a complete plant shutdown or critical equipment failure, and 
a partial shutdown or failure of a section of the plant that requires immediate operator attention.  
• Severity 2 - Low Priority Alarm (yellow)  
These alarms are normally associated with an abnormal process condition not requiring shutdown. This 
alarm requires non -urgent operator attention, since no plant capacity has been lost, however the process 
requires attention to avoid plant capacity loss in case the abnormal process condition is not corrected.  
• Severity 3 - Notification (light blue)  
These alarms are considered notifications. They are normally associated with personnel or controller -
initiated events such as placing an instrument in MAINTENANCE or SIMULATE modes, and certain 
changes in operating scenarios/configurations.  
Alarms can be displayed in chronological order or sorted under categories.  
  

============================================================
--- PAGE 10 ---
============================================================
 
 10 of 48 
© BW Water  
 
1.5.5 Sequencers  
A control sequencer is the  order  in which  a set of executions  are carried  out to  perform  a specific function. The 
PLC program and associated HMI object that execute instructions is called a Sequencer.  
Sequencers are used throughout the control program to START/STOP equipment, systems, and processes in 
specific logically ordered steps.  Steps begin from a known process or equipment state and are triggered when 
certain conditions are met, such as filter h igh DP, as required by a process, or operator initiat ion. 
A sequencer advances when step complete/advance criteria are met.  Typical criteria include timers, monitored 
endpoints such as pH or concentration, equipment states such as valves open, motors running, etc . 
1.5.6 HMI Sequencer Object  
Sequencer Functionality  
AUTO  Completes sequence automatically without operator input.  
SEMI AUTO  ALLOWS the Operator to use the buttons below.  
START  Operator initiated sequence. Sequence completes automatically if none of the other buttons 
below are pressed.  
PAUSE  Remain in the current step with valves CLOSED and equipment STOPPED.  Stop the timer and 
retain the elapsed time  
HOLD  Remain in current step with valves OPEN equipment RUNNING.  Continue timing.  
RESUME  1. Step in PAUSE - reopen valves restart equipment and continue timing, continues sequence to 
the end (as if AUTO)  
 2. Step in HOLD - continue timing, continues sequence to the end (as if AUTO)  
ADVANCE  Move to next Step.  
ABORT  CLOSE valves, stop equipment return to initial state  
 
  

============================================================
--- PAGE 11 ---
============================================================
 
 11 of 48 
© BW Water  
 
1.0 STANDARIZED EQUIPMENT CONTROL FUNCTIONS  
2.1 MOTOR CONTROL FUNCTION  
2.1.1 Motor Control - Direct Online (DOL)  
Each motor with Direct Online (DOL) drive has the following control signals and functionality (Some mixers do not 
use AUTO mode, except for interlocks, and are started manually at the HMI): 
PLC- Input and Outputs to and from the MCC/LCP  
START / STOP  Digital Output (DO)  Motor start/stop command  
REMOTE  Digital Input (DI)  PLC operation feedback  
RUNNING  Digital Input (DI)  Run feedback  
FAULT  Digital Input (DI)  Common Fault Signal (i.e. OLR)  
 
Soft IO to the PLC from HMI 
AUTO  Complete PLC control, operator -selected  
MANUAL  Operator selected and controlled the Motor Equipment operation  
START  Starts Motor Equipment in MANUAL, operator -initiated  
STOP  Stops Motor Equipment in MANUAL, operator -initiated  
DUTY  Chooses the motor for operation in AUTO mode, operator selected, 
motor selected AUTO, and not DUTY is considered STANDBY  
RESET  Clears Motor Equipment FAIL TO START/STOP alarm, operator initiated  
Setpoints  Fail to START/STOP delay (sec)  
 
Soft IO from MCC and PLC to HMI 
REMOTE  PLC control selected at LCP  
LOCAL  Not selected REMOTE at LCP  
Run Time  Total run hours (from PLC resettable)  
Alarms  Fail to Start/Stop  
AUTO  Status  
MANUAL  Status  
RUN REQUEST  Status  
RUNNING  Status  
FAULT  Status  
 
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch 
between the system's command and its actual feedback. If the system fails to reach the commanded state within 
a set time or tolerance, it is  considered a fault, indicating a possible malfunction or failure.  
 
2.1.2 Motor Control - Soft Start  
Each motor with Soft Starter drive has the following control signals and functionality:   A FAULT is generated by 
drive or controller/monitor.  TRIP is breaker status.  Both may not be AVAILABLE  in all circumstances.  

============================================================
--- PAGE 12 ---
============================================================
 
 12 of 48 
© BW Water  
 
PLC- Output to Soft Starter  
START / STOP  Digital Output (DO)  Motor start/stop command  
 
PLC- inputs from Soft Starter  
REMOTE  Digital Input (DI)  PLC control  
RUNNING  Digital Input (DI)  Run feedback  
STOP  Digital Input (DI)  Stop status  
FAULT  Digital  Input (DI)  Common Fault Signal (SS Common Fault 
Signal)  
 
Soft IO to the PLC from  HMI 
AUTO  Complete PLC control, operator -selected  
MANUAL  Operator selected and controlled the motor equipment operation  
START  Starts motor equipment in MANUAL, operator -initiated  
STOP  Stops motor equipment in MANUAL, operator -initiated  
DUTY  Chooses the motor equipment for operation in AUTO mode, operator 
selected, motor selected AUTO, and not DUTY is considered STANDBY  
RESET  Clears motor equipment FAIL TO START/STOP alarm, operator initiated  
Setpoints  Fail to START/STOP delay (sec)  
 
Soft IO from MCC and PLC to HMI 
REMOTE  PLC control selected at LCP  
LOCAL  Not selected REMOTE at LCP  
Run Time  Total run hours (from PLC resettable)  
Alarms  Fail to Start/Stop  
AUTO  Status  
MANUAL  Status  
RUN REQUEST  Status  
RUNNING  Status  
FAULT  status  
 
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch 
between the system's command and its actual feedback. If the system fails to reach the commanded state within 
a set time or tolerance, it is  considered a fault, indicating a possible malfunction or failure.  
  

============================================================
--- PAGE 13 ---
============================================================
 
 13 of 48 
© BW Water  
 
2.1.3 Motor Control - VSD 
Each motor with a Variable Speed  Drive ( VSD ) control signals consist of the following (the Flocculation mixers do 
not have AUTO mode for START/STOP or speed control and are started manually and speed set at the HMI): 
Each motor with a Variable Frequency Drive (VSD) control signal consists of the following :  
PLC- Outputs to the VSD  
START / STOP  Digital Output (DO)  Motor start / stop command  
SPEED REFERENCE  Analog Output (AO)  Motor speed command  
 
PLC- Inputs from the VSD  
REMOTE  Digital Input (DI)  PLC control  
SPEED FEEDBACK  Analog Input (AI)  Current operating speed  
STOP  Digital Input (DI)  Stop status  
FAULT  Digital Input (DI)  Common Fault Signal (SS 
Common Fault Signal)  
 
Soft IO from HMI to the PLC  
AUTO  Complete PLC control, operator -selected  
MANUAL (motor)  Operator selected and controlled the motor equipment operation  
START  Starts motor equipment in MANUAL, operator -initiated  
STOP  Stops motor equipment in MANUAL, operator -initiated  
DUTY  Chooses the motor equipment for operation in AUTO mode, operator 
selected, motor selected AUTO, and not DUTY is considered 
STANDBY  
RESET  Clears motor equipment FAIL TO START/STOP alarm, operator 
initiated  
Setpoints  Fail to START/STOP delay (sec)  
AUTO (speed)  Complete PLC PID control, operator -selected  
MANUAL (speed)  Allows operator speed input while motor START/STOP remains in 
AUTO PLC control  
MANUAL SPEED 
REFERENCE  Allows operator input of speed (0% -100% = 4 - 20mA)  
 
  

============================================================
--- PAGE 14 ---
============================================================
 
 14 of 48 
© BW Water  
 
Soft IO from PLC to HMI 
REMOTE  PLC control selected at LCP  
LOCAL  PLC control selected at LCP  
Run Time  Total run hours (from PLC resettable)  
Alarms  Fail to Start/Stop  
AUTO  Status  
MANUAL  Status  
RUN REQUEST  Status  
RUNNING  Status  
FAULT  Status  
  
The FAULT Alarm Status is triggered either by a fault signal from an external controller or when there’s a mismatch 
between the system's command and its actual feedback. If the system fails to reach the commanded state within 
a set time or tolerance, it is  considered a fault, indicating a possible malfunction or failure  
  

============================================================
--- PAGE 15 ---
============================================================
 
 15 of 48 
© BW Water  
 
2.1.4 Equipment D UTY / STANDBY   
2 pump, N+1 example  
Each pump of a pair can meet the specified volume and pressure required by the process. This is expressed as 
2x100% or N+1 (N=required number, in this case 1, +1 is a spare).  
One pump selected AUTO will be selected for DUTY.  The pump selected for DUTY will be the only operating 
pump controlled by the PLC in AUTO operation unless it fails  (FAULT or TRIP) .  The pump selected AUTO and 
STANDBY is a hot spare that will operate in AUTO if the duty pump fails for some reason.  
The switch over to the operation of the standby pump is automatically controlled by the PLC.  
A motor in a TRIP/ FAULT state is automatically placed and MANUAL and OFF  by the PLC .  The motor must be 
reset by the operator before it can be selected AUTO and DUTY  or STANDBY . 
3 pump, N+1 example  
Each pump of a set of three (3) can meet half the specified volume and pressure required by the process. This is 
expressed as 3x50% or N+1 (N=required number, in this case 2, +1 is spare). Only N can be selected DUTY.  
Two pumps selected AUTO will be selected for DUTY and the third is STANDBY if in AUTO.  The pumps selected 
for DUTY will be the operating pumps controlled by the PLC in AUTO operation.  The STANDBY pump is a hot 
spare that will operate in AUTO if one of th e duty pumps TRIP /FAULT for some reason.  A maximum two (2) pumps 
can be selected for DUTY.  
2.1.5 Pump Failure to Start / Stop Logic  
When a pump is commanded to START in AUTO or MANUAL at the HMI, the RUN signal must be received within 
a specified duration, or the pump will FAIL TO START. A latched alarm is generated. Operator RESET is required 
to clear and unlatch the alarm.  
The STANDBY pump will start when in AUTO.  Its mode will be changed to DUTY.  
Note: A pump that fails to start will go to MANUAL and STOP to prevent immediate restart when RESET.  
To prevent pump deadheading, the associated motorized valve (auto -valve) must be confirmed fully open before 
the pump is allowed to operate. The valve open status shall serve as a permissive signal for pump startup.  
  

============================================================
--- PAGE 16 ---
============================================================
 
 16 of 48 
© BW Water  
 
2.2 INSTRUMENTATION AND CONTROL FUNCTIONS  
2.2.1 Analog Transmitter/Analyzer (LIT, FIT, AIT) 
Analog instruments, have four (4) AVAILABLE  alarm states (it is not required to use all states):  
High High (HH)  only used with interlocks and control actions such as switching valves and stopping 
pumps in abnormal operating conditions  
High (H)  information/warning/permissive  
SP-1 Readily AVAILABLE  soft output provision for command (Admin shall be able to 
activate this whenever necessary).  
SP-2 Readily AVAILABLE  soft output provision for command (Admin shall be able to 
activate this whenever necessary).  
SP-3 Readily AVAILABLE  soft output provision for command (Admin shall be able to 
activate this whenever necessary).  
SP-4 Readily AVAILABLE  soft output provision for command (Admin shall be able to 
activate this whenever necessary).  
Low (L)  information/warning/permissive  
Low Low (LL)  only used with interlocks and control actions such as stopping pumps, switching 
valves, in abnormal operating conditions  
Analog Transmitters may also have operational setpoints that fall between the High and Low alarm setpoints.  For 
example, a level transmitter may have pump start and stop setpoints for level control.  Analog Transmitters also 
are used as the Process Variab le (PV) for Proportional Integral Derivative (PID) or Ratio control where the 
Manipulated Variable (MV), such as pump speed, is adjusted to maintain a tank level, flow, etc. Setpoint (SP).  
All Flow Transmitters must have totalizers at the HMI.  Totalized flow is calculated either of two ways, from pulses 
from the transmitter or, calculated real time from the flow process variable.  
Note: All analog values must be archived and AVAILABLE  for trending.  
  

============================================================
--- PAGE 17 ---
============================================================
 
 17 of 48 
© BW Water  
 
Analog Instrument Control:  
PLC - IO from the instrument to the PLC  
4-20mA   Analog Input (AI)  process variable, converted and scaled in  the PLC  
HMI - Soft IO to PLC  
High High Alarm Setpoint  Alarm generated at greater than or equal to this value  
High Alarm Setpoint  Alarm generated at greater than or equal to this value  
SP-1 Setpoint  A soft output will be triggered once the set value matches the 
actual process value or reaches an equivalent condition.  
SP-2 Setpoint  A soft output will be triggered once the set value matches the 
actual process value or reaches an equivalent condition.  
SP-3 Setpoint  A soft output will be triggered once the set value matches the 
actual process value or reaches an equivalent condition.  
SP-4 Setpoint  A soft output will be triggered once the set value matches the 
actual process value or reaches an equivalent condition.  
Low Alarm Setpoint  Alarm generated at less than or equal to this value  
Low Low Alarm Setpoint  Alarm generated at less than or equal to this value  
Alarm Value Dead -band  The amount in engineering units that the current value must drop 
below either the High High or High limits, or increase above either 
the Low Low or Low limits before an alarm can be retriggered  
 
 
Alarm Time Delay  The time, in seconds, that must elapse after the current value 
exceeds an alarm limit before the alarm is triggered  
Maintenance Mode  Removes the instrument from the interlock logic.  
4-20mA derived scaled value is valid (still displayed).  
Simulate Mode  The PV is entered by the operator, remains as an interlock  
 
NOTE:  An instrument used as the PV for a PID controller can only be placed in S IMULATE  Mode 
when the PID controller is in MANUAL  Mode.  
  

============================================================
--- PAGE 18 ---
============================================================
 
 18 of 48 
© BW Water  
 
Soft IO from PLC to HMI 
Process V ariable  (PV) Scaled process value  
FAULT  The 4 -20mA signal is outside its range  
EU Scale Minimum  In appropriate engineering units, Lower Range Value (LRV)  
EU Scale Maximum  In appropriate engineering units, Upper Range Value (URV)  
Alarm  Status  
2.2.2 Switch es (LS) 
Switches are usually provided as a backup for the transmitters. They provide warnings and initiate control actions 
as required. They provide alarms and initiate interlocking with other equipment and processes.  
High High and Low Low switches typically function as an interlock by stopping equipment such as pumps, mixers 
closing an isolation valve.  
The discrete signal (either energized or de -energized) from the LS to the PLC is fail -safe, that is, energized until 
the alarm condition is present. In the case of low level (LSL) / Level Low Low (LSLL), pressure (PSL/PSLL), and 
Flow (FSL/FSLL), the switches are wired normally -open (NO). When liquid or pressure is present above the alarm 
level, the circuit is energized. When the liquid drops below the alarm level, the switch opens, generating an alarm.  
High Level (LSH)/ Level High High (LSHH) and pressure (PSH/PSHH) switches High / High High are wired normally 
closed and energized when the liquid or pressure is below the alarm level. When they go above the alarm level, 
the switches open and generate an a larm.  
Level Switch Control is as follows:  
PLC - IO from the instrument to the PLC  
Current State   Digital  Input (DI) energized or de -energized  
HMI - Soft IO to PLC  
ON Delay Setpoint  The time, in seconds, that must elapse after the alarm condition 
occurs before generating an alarm  
Disable/Enable  Disables or enables LS interlock functions  
 
HMI - Soft IO from PLC  
Switches Interlock Status  Active, Inactive  
 
2.3 Valve Control  - Motor Operated  ON/OFF  
A valve must be selected AUTO for automatic control according to the PLC logic.  A valve cannot be selected 
AUTO if the valve has FAILED TO OPEN or FAILED TO CLOSE alarm active. To deactivate an alarm, it must be 
RESET.  

============================================================
--- PAGE 19 ---
============================================================
 
 19 of 48 
© BW Water  
 
Valve Position Switches are used to determine when valve is either open (ZSO) or closed (ZSC). Valve position 
switches can provide alarm and interlock functions.  
Alarms are generated when a valve controlled by the PLC is not in its commanded position or takes too long to 
transition, or when a manual valve is not in the required position. When a valve fail alarm is generated, the valve 
is put into MANUAL and CLOSE.  
Valve Position Switches act as interlocks by stopping, or preventing the starting, of pumps and processes.  
Position Switches are wired normally open and go closed when the valve is in its commanded position.  
A FAILED valve interlocks the process and is commanded to its FAIL -SAFE position.  
PLC- Input and Outputs to and from the MCC  
OPEN  Digital Output (DO)  OPEN command  
CLOSE  Digital Output (DO)  CLOSE command  
OPENED  Digital Input (DI)  OPEN feedback  
CLOSED  
REMOTE/LOCAL  Digital Input (DI)  
Digital Input (DI)  CLOSED feedback  
REMOTE/LOCAL feedback  
HMI - Soft IO from MCC/PLC  
AUTO  Complete PLC control, operator -selected  
MANUAL  Operation without interlocks activated, operator selected  
MANUAL OPEN  Opens valve in MANUAL, operator -initiated  
MANUAL CLOSE  Closes valve in MANUAL, operator -initiated  
FAIL RESET  Reset Fail to Open/Close alarm  
Fail to Open Setpoint  Alarm time delay in seconds  
Fail to Close Setpoint  Alarm time delay in seconds  
 
HMI - Soft IO to the PLC  
AUTO  Complete PLC control, operator -selected  
MANUAL  Operation without interlocks activated, operator selected  
MANUAL OPEN  Opens valve in MANUAL, operator -initiated  
MANUAL CLOSE  Closes valve in MANUAL, operator -initiated  
FAIL RESET  Reset Fail to Open/Close alarm  
Fail to Open Setpoint  Alarm time delay in seconds  
Fail to Close Setpoint  Alarm time delay in seconds  
 
HMI - Soft IO from MCC/PLC  
AUTO  Status  
REMOTE / LOCAL  Status  
OPEN REQUEST  Status  
CLOSE REQUEST  Status  
FAIL ALARM  Status  
 
2.3.2  Modulating Control Valve  

============================================================
--- PAGE 20 ---
============================================================
 
 20 of 48 
© BW Water  
 
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
OPENED  Digital Input (DI)  OPEN feedback  
CLOSED  Digital Input (DI)  CLOSED feedback  
REMOTE/LOCAL  Digital Input (DI)  REMOTE/LOCAL feedback  
% POSITION SETPOINT  Analog Output (AO)  % POSITION command  
% POSITION  Analog Input (AI)  % POSITION feedback  
 
HMI- Soft IO to the PLC  
AUTO  Complete PLC control, operator selected  
MANUAL  Operation without interlocks activated, operator selected  
% POSITION Setpoint  Opening / Closing % Position Command  
FAIL RESET  Reset Fail to Open/Close alarm  
FAIL Position Time Setpoint  Alarm time delay in seconds  
FAIL Position Difference 
Setpoint  Position Difference in (%)  
 
HMI - Soft IO from MCC/PLC  
AUTO  Status  
MANUAL  Status  
REMOTE / LOCAL  Status  
% POSITION  Status  
FAIL ALARM  Status  
  

============================================================
--- PAGE 21 ---
============================================================
 
 21 of 48 
© BW Water  
 
2.4 Proportional Integral Derivative (PID) Closed Loop Control  
The following use PID controllers:  
• Variable Frequency Drive ( VSD ) motor speed control for flow and pressure,  
• Level and flow Control Valves  
• Various Chemical Dosing Pumps  
Proportional, Integral, and Derivative (PID) control uses an algorithm that compares a Process Variable (PV) with 
a specified Setpoint (SP).  The error of the PV from SP is calculated.  The algorithm produces a Control Variable 
(CV) that is sent to a contr ol device such as a VSD , control valve, and etcetera., that adjusts the process to bring 
the error to zero.  The PID CV is continually adjusted as the process changes.  
The PID algorithm is composed of:  
• Proportional (GAIN)  - when the process is under a consistent load, the error is multiplied by the GAIN 
to produce a control output value.  
• Integral (RESET)  - when the process is under a magnitude change, a reset of the gain factor based on 
the duration the error from the setpoint remains. The control variable is adjusted to bring the process 
value back to the setpoint.  
• Derivative (RATE) - when there are rapid process oscillations around the setpoint in processes, the rate 
of process change is determined to prevent a swing in the process value from fully developing.  
When a block goes OFFLINE, or associated equipment is commanded to STOP, the PID controller retains the last 
state (tracking).  This allows the process to stabilize more quickly when restarted.  
When there is a loss of the PV, the PID controller is placed in manual at the last state output and the device point 
is alarmed.  
PID Parameter Setting and Trending  
The PID object must include a 30-minute trend of the CV, PV, and SP to assist in the tuning of the PID controller. 
Only small, incremental, changes should be made to the PID setpoints.  
CAUTION:    The operator must use caution when manipulating all values to avoid process upsets.  
 
PID Control Object  
PLC - PLC- Input and Outputs  
Process Value (PV)  Analog Input (AI), 4 -20mA converted and scaled to engineering 
units in PLC  
Control Output (CV)  Analog Output (AO), 4 -20mA generally displayed as 0 -100%  
 
  

============================================================
--- PAGE 22 ---
============================================================
 
 22 of 48 
© BW Water  
 
HMI - HMI To PLC  
SP Process setpoint  
P-SP Proportional setpoint  
I-SP Integral setpoint  
D-SP Derivative setpoint  
AUTO mode  PLC PID adjustment of the CV  
MANUAL mode  Operator entered CV generally 0 -100% corresponding to 4 -20mA 
output  
CASCADE Mode  PID Setpoint comes from calculation or from other controller  
 
HMI -PLC to HMI 
Process Value (PV)  current value  
Control Output (CV)  current value  
 
  

============================================================
--- PAGE 23 ---
============================================================
 
 23 of 48 
© BW Water  
 
2.5 Chemical Dosing Control Ratio Control (open loop control)  
Controlling dosing for chemicals not provided with analytical instrument feedback require a ratio controller based 
on flow or another measured parameter.  
Ratio Controller Object  
In this control strategy, the system operates solely based on the preset parameter, relying on the assumption 
that the input -out relation remains stable over time.  
 
Controlling dosing for chemicals not provided with analytical instrument feedback requires a ratio controller based 
on flow or another measured parameter.  
This control loop is usually utilized in the chemical dosing application.  
Ratio Controller Object  
PLC- Input and Outputs to and from the MCC  
Process Value (PV)  The measured value being controlled,  
Analog Input (AI), 4 -20mA converted and scaled, or Digital Signal 
(DI), or  
A defined set of data.  
Control Output (CV)  Analog Output (AO), 4 -20mA, generally displayed as 0 -100%  
 
HMI to PLC  
AUTO  PLC adjustment of output to pump  
MANUAL  Operator Entered output (0 -100%)  
Concentration  Concentration of the chemical to be dosed  
Density  Density of chemical to be dosed  
Capacity  pump rated capacity at 100% stroke and speed  
Stroke  Stroke setting of pump if manually set  
Target Concentration  Operator entered  
Manual Speed  Operator entered in PLC manual mode  
 
PLC to HMI 
Process Value (PV)  Current value  
Control Output (CV)  Current value  
 
  

============================================================
--- PAGE 24 ---
============================================================
 
 24 of 48 
© BW Water  
 
Ratio Controller HMI Object (example)  
 
  


============================================================
--- PAGE 25 ---
============================================================
 
 25 of 48 
© BW Water  
 
3. Water Treatment Plant  
EQUIPMENT GROUPS  
An equipment group is various equipment and instrumentation that operate as a unit. The groups are included in 
the System Overview Displays in HMI. A group’s Overview graphic object will indicate if a group is READY. The 
READY status of all groups will be observable in the Overview Display for the operator to readily determine the 
operating state of the Treatment System.  
Group READY is an indication that the minimum required equipment is selected AUTO and there are no priority 1 
alarms.  A block not READY may be an interlock for other groups and equipment, but not necessarily.  
For example, the Clean -in-Place (CIP) System  group is NOT READY due to CIP Tank level Transmitter FAULT.  
The FAULT interlocks the Coagulant  pumps. They are prevented from starting or they are stopped when running. 
List of Equipment Groups  
Group    
- Feed to UHPRO system 
(SWRO brine)  (BY CLIENT)  
1 Feed Preparation System  Brine feed from SWRO (battery limit), chemical dosing, static 
mixing, RO cartridge filtrat ion, associated piping and 
instrumentation.  
2 High-Pressure Pumping 
System  RO HP PUMP,  TURBOCHARGER  (feed and interstage turbos), 
pressure transfer from reject streams, associated piping and 
instrumentation.  
3 Membrane Treatment 
System  RO 1ST AND 2ND Stage , pressure vessels, permeate collection, 
reject discharge, interconnections and instrumentation.  
4 Cleaning -in-Place (CIP) 
System  CIP tank, CIP pumps, flushing connections to membrane system, 
isolation valves, and instrumentation for cleaning and preservation.  
- Product and Waste 
Interfaces  (BY CLIENT)  
 
  

============================================================
--- PAGE 26 ---
============================================================
 
 26 of 48 
© BW Water  
 
 
3.1 FEED PREPARATION SYSTEM( GROUP 1)  
Ref P&ID: P22-DWG -09-009-02-08 || P22-DWG -09-009-02-11  
3.1.1 FEED PREPARATION SYSTEM EQUIPMENT  
 
3.1.2 FEED PREPARATION SYSTEM INSTRUMENTS  
Item Instrument Description  Tag No.  
1 RO Cartridge Filter Differential Pressure Switch  DPS -09-001 
2 ORP Analyzer (Downstream RO Cartridge Filter)  ORP IT-09-001 
3 Conductivity Analyzer (Downstream RO Cartridge Filter)  CIT-09-001 
4 Flowmeter (Downstream RO Cartridge Filter)  FIT-09-001 
5 Antiscalant Dosing Tank Level Switch - High LSH-09-001 
6 Antiscalant Dosing Tank Level Switch - Low LSH-09-002 
7 Antiscalant Dosing Tank Inlet Motorized Valve - Limit Switch  VE-07-014 
8 Antiscalant Dosing  Pump Downstream Motorized Valve - Limit Switch  VE-07-016 
3.1.3 FEED PREPARATION SYSTEM PROCESS DESCRIPTION  
The Feed Preparation System receives SWRO brine at the battery limit and conditions it for entry into the high -
pressure pumping and UHPRO membrane system. The incoming brine is characterized by high salinity, with a 
typical total dissolved solids concentration in the range of approximately 43,000 to 53,000 mg/L, and is already 
pretreated upstream of this system. Th e role of the Feed Preparation System is to ensure that the brine is Item Equipment Description  Tag No.  
1 RO Cartridge Filter  FIL-09-001 
2 Static Mixer  MZE -09-001 
3 Antiscalant Dosing Tank  TK-09-002 
4 Antiscalant Dosing Pump  1 BDS -09-001 
5 Antiscalant Dosing Pump 2  BDS -09-002 

============================================================
--- PAGE 27 ---
============================================================
 
 27 of 48 
© BW Water  
 
chemically conditioned, uniformly mixed, and free of fine particulates that could adversely affect downstream high -
pressure equipment and membranes.  
Chemical conditioning is achieved through antiscalant dosing. Antiscalant is stored in a dedicated dosing tank and 
injected into the brine feed via duty and standby dosing pumps. The chemical is introduced via injection port of a 
static mixer to ensure homogeneous distribution across the pipe cross -section before further processing. This 
arrangement ensures consistent chemical availability and avoids localized under -dosing or over -dosing prior to 
pressurization.  
Following chemical injection and mixing, the brine passes through a cartridge filter that provides final mechanical 
protection within the Feed Preparation System. The cartridge filter removes fine suspended solids remaining in the 
brine stream, protecting the downstream high -pressure pump, energy recovery devices, and membrane elements 
from particulate fouling, erosion, or blockage. The filtration stage does not alter the dissolved constituents of the 
brine and operates solely as a physical barrier to solid s. 
Instrumentation installed downstream of the cartridge filter provides confirmation of feed readiness prior to high -
pressure pumping. Conductivity and ORP analyzers monitor feed quality to detect abnormal salinity or chemical 
conditions, while a flow transmitter confirms the presence and stability of feed flow to the high -pressure pump. 
These measurements support monitoring and protection functions and do not perform active control within the 
Feed Preparation System.  
Overall, the Feed Preparation System establishes the necessary boundary conditions for stable and reliable 
operation of the downstream High -Pressure Pumping System. By ensuring continuous chemical conditioning, 
uniform mixing, and effective particulate removal, the system protects critical equipment and supports efficient 
UHPRO membrane operation without performing flow control, pressure gener ation, or desalination.   

============================================================
--- PAGE 28 ---
============================================================
 
 28 of 48 
© BW Water  
 
 
3.1.3 FEED PREPARATION SYSTEM CONTROL & OPERATION  
The Feed Preparation System is enabled when the RO system is in operation and feed flow to the RO is required. 
While enabled, the system operates continuously to provide stable chemical dosing, mixing, and filtration to 
condition the feed water prior to fu rther treatment.  
System reliability is achieved through duty/standby arrangements for rotating  chemical dosing equipment, while 
passive conditioning and filtration  compo nents. Alarms provide indication of loss of chemical dosing capability, low 
chemical inventory, or excessive filter fouling. Internal interlocks inhibit operation under conditions that could result 
in ineffective chemical conditioning or mechanical damage, ensuri ng that only adequately conditioned feed is 
passed forward for downstream processes.  
• Static Mixer and Cartridge Filter (MZE -09-001 / FIL -09-001) 
The static mixer requires no control or actuation and is considered AVAILABLE  when the feed line is open and 
flowing.  The cartridge filter operates continuously during normal operation. Differential pressure across the filter is 
monitored to assess cartridge condition. A high differential pressure alarm indicates fouling and maintenance 
requirement . 
Protective interlocks associated with excessive differential pressure may  (operator -initiated ) inhibit continued 
operation to prevent equipment damage. No active control functions are applied to either the static mixer or the 
cartridge filter.  
Instrumentation installed downstream of the cartridge filter confirms  feed condition before  high-pressure pumping. 
Conductivity and ORP analyzers provide continuous monitoring of feed quality to detect abnormal salinity or 
chemical condition (CIT -09-001, ORPIT -09-001). A flow transmitter confirms the presence and stability of feed flow 
to the high -pressure pump (FIT -09-001). These instruments are used for monitoring , and validation of feed 
readiness and do not perform active control within the Feed Preparation System.  
• Antiscalant Dosing Tank  (TK-09-002) and Pump  (BDS -09-001 / BDS -09-002),  
The antiscalant dosing system is controlled to ensure reliable and continuous chemical injection into the brine feed 
whenever the Feed Preparation System is in operation. The system comprises the antiscalant dosing tank (TK -09-
002), duty/standby dosing pumps (BDS -09-001 / BDS -09-002), and the motorized isolation valve s (VE-09-
014/010);  
The antiscalant dosing tank inlet motorized valve ( VE -09-014) is provided to automatically control tank filling based 
on tank level. The valve opens when the tank level reaches a low -level condition and closes when the high -level 
setpoint is reached to prevent overfilling. The valve is interlocked with tank level and system status such that it 

============================================================
--- PAGE 29 ---
============================================================
 
 29 of 48 
© BW Water  
 
remains closed during fault conditions  (this shall be a separate loop  such that filling is not stalled  even during 
shutdown for prep aration  purposes ). 
The dosing pumps are arranged in a duty and standby configuration and are normally operated in automatic mode. 
One pump is selected as duty, with the standby pump AVAILABLE  to maintain dosing continuity in the event of 
pump fault or maintenance. Pump run status and fault feedback are monitored to confirm availability and correct 
operation.  
Antiscalant injection to the brine feed is enabled through the motorized valve (VE -09-016) installed upstream of 
the static mixer (MZE -09-001). The valve is controlled to open when antiscalant dosing is enabled and to close 
when dosing is inhibited or intentionally isolated, providing positive control of chemical injection into the process.  
The antiscalant dosing tank level is continuously monitored by a level indicator (LI -09-002) with associated level 
switches. A high -level switch (LSH -09-001) provides overfill indication, while a low -level switch (LSL -09-002) 
provide s alarms and protective inhibition of dosing pump operation. Low tank level also prevents opening of the 
motorized injection valve to avoid ineffective dosing and protect the pumps.  
Local pressure indication on the dosing discharge header (PI -09-006) provides visibility of dosing line pressure. A 
pressure safety valve (PSV -09-002) is installed to protect the dosing system against overpressure conditions. 
Valve positions, pump status, and instrument signals are monitored to provide clear operational feedback and 
alarm indication to operators.  
Antiscalant Dosing Strategy  
Ratio  Cont rol: Flow -paced Open Loop  
In Ratio  Control  mode, the antiscalant dosing rate is calculated directly from the RO inlet flow and the configured 
antiscalant dosage requirement. The calculated dosing rate is converted to a corresponding pump stroke frequency 
and applied directly to the duty dosing pum p without closed -loop correction.  
Antiscalant Flow (L/h) = [ FIT-09-001, (m³/h) × Antiscalant dosage (g/m³)] ÷ [Chemical concentration ( (g/L)  ]  
If RO feed flow signal FIT -09-001 is un AVAILABLE , the antiscalant dosing system shall be operated in “Manual 
Stroke Mode” as fallback , where the duty pump BDS -09-001 / BDS -09-002 runs at a fixed operator -set stroke 
frequency. This mode provides minimum chemical protection and is intended for temporary operation only until 
flow measurement is restored.  
  

============================================================
--- PAGE 30 ---
============================================================
 
 30 of 48 
© BW Water  
 
 3
.1.4 FEED PREPARATION SYSTEM OPERATION X READY PERMISSIVE
The Feed Preparation System shall be considered AVAILABLE  when the following conditions are satisfied:
• Cartridge filter differential pressure within acceptable range, and
• No active fault within the Feed Preparation System, and
• Feed Preparation System Group selected in REMOTE and AUTO.
• RO system in RUN / FEED REQUEST active.:
• Antiscalant dosing tank level above low (LSL-09-002 not active), and
• At least one antiscalant dosing pump NOT FAULT and AUTO (BDS-09-001 / BDS-09-002), and 
• Motorized valves VE-09-014/016 are AVAILABLE, NOT FAULT and AUTO

============================================================
--- PAGE 31 ---
============================================================
 
 31 of 48 
© BW Water  
 
3.2 HIGH -PRESSURE PUMPING SYSTEM (Group 2) 
Ref P&ID: P22 -DWG -09-009-02-09  
3.2.1 HIGH -PRESSURE PUMPING SYSTEM Equipment   
 
3.2.2 HIGH -PRESSURE PUMPING SYSTEM Instruments  
Item Instrument Description  Tag No.  
1 Pressure Transmitter ( upstream RO HP PUMP ) PIT-09-001 
2 Pressure Transmitter ( down stream RO HP PUMP ) PIT-09-002 
3 Pressure Transmitter (Feed Turbocharger  Outlet - RO Stage 1 Feed ) PIT-09-003 
4 Pressure Transmitter ( RO Stage 1 Reject - Interstage Turbocharger Feed ) PIT-09-004 
5 Pressure Transmitter (Interstage Turbocharger Outlet - RO Stage 2 Feed ) PIT-09-005 
6 Pressure Transmitter (RO Stage 2 Reject - Interstage Turbocharger  Feed ) PIT-09-006 
7 Pressure Transmitter (Interstage Turbocharger Reject - Feed Turbocharger 
Inlet)  PIT-09-007 
8 Pressure Transmitter (Feed Turbocharger Reject)  PIT-09-008 
8 Common Permeate Flow Indicator (RO Interface)  FIT-09-003 
9 Common Reject / Brine Flow Indicator (RO Interface)  FIT-09-004 
10 Brine Bypass Valve - Feed Turbocharger Bypass with Limit Switches  VE-09-002 
11 Turbocharger Isolation Valve with Limit Switches  VE-09-007 
 Item Equipment Description  Tag No.  
1 RO H igh Pressure  Pump  – RO HP Pump   (VSD Driven)   BH-09-001 
2 Feed Turbocharger  SIP-09-001 
3 Interstage Turbocharger  SIP-09-002 

============================================================
--- PAGE 32 ---
============================================================
 
 32 of 48 
© BW Water  
 
3.2.1 HIGH -PRESSURE PUMPING SYSTEM PROCESS DESCRIPTION  
The High -Pressure Pumping System enables operation of a two -stage RO process by establishing and 
redistributing hydraulic pressure within the membrane train. The system combines mechanical pressure generation 
and hydraulic pressure recovery so that pressure energy is reused across both RO stages rather than dissipa ted. 
In a two -stage RO configuration, the feed entering the first RO stage must be raised to a pressure sufficient to 
overcome osmotic pressure and hydraulic losses. This initial pressure rise is provided by the high -pressure feed 
pump (BH -09-001), which establishes the baseline pressure level for the membrane system. The pump supplies 
only the portion of pressure that cannot be recovered internally.  
As feed passes through the first RO stage, pressure is partially consumed to drive permeation. The first -stage 
reject exits the membranes at a reduced but still significant pressure. This reject stream is routed through the 
interstage turbocharger (SIP -09-002), where its pressure energy is hydraulically transferred to the feed entering 
the second RO stage. Within the interstage turbocharger, pressure from the reject stream is exchanged with the 
lower -pressure feed stream, resulting in a pressure boost witho ut additional mechanical input.  
Following the second RO stage, the final reject stream retains additional recoverable pressure energy. This stream 
is directed to the feed turbocharger (SIP -09-001), where pressure energy from the second -stage reject is 
transferred back to the incoming feed upstream of the RO system. This recovered pressure increases the inlet 
pressure to the membrane train and correspondingly reduces the pressure rise required from the high -pressure 
feed pump (BH -09-001).  
From a theoretical standpoint, both turbochargers (SIP -09-001 and SIP -09-002) function as hydraulic pressure 
transfer devices, not pressure -generating machines. They do not create pressure independently; instead, they 
redistribute pressure energy already present in the reject streams. The magnitude of pressure boosting achieved 
depends on AVAILABLE  reject pressure, feed -to-reject flow balance, and device efficiency, rather than on active 
control or external power input.  
The combined action of the high -pressure feed pump (BH -09-001), interstage turbocharger (SIP -09-002), and feed 
turbocharger (SIP -09-001) produces a distributed pressure profile across the two -stage RO system. Mechanical 
energy input is concentrated at the pump, while recovered hydraulic energy is reused between and downstream 
of the RO stages. This arrangement minimizes pressure dissipation, reduces overall power demand, and limits 
mechanical l oading on the high -pressure pump.  
In essence, the High -Pressure Pumping System enables stable two -stage RO operation by converting reject 
pressure from each stage into useful driving force for the next stage, forming an internal hydraulic energy -recovery 
loop within the membrane process.  
  

============================================================
--- PAGE 33 ---
============================================================
 
 33 of 48 
© BW Water  
 
 
3.2.2 HIGH -PRESSURE PUMPING SYSTEM CONTROL AND OPERATION  
The High -Pressure Pumping System is controlled to deliver stable and adequate pressure to the two -stage RO 
membrane system while maximizing pressure recovery from reject streams. Operation focuses on coordinated 
control of the high -pressure feed pump and monitoring  pressure transfer across the feed and interstage 
turbochargers. The system does not perform flow or quality control and operates in response to upstream feed 
availability and downstream membrane hydraulic demand.  
Automatic control actions are limited to pressure generation via pump speed control, valve actuation for isolation 
and protection, and continuous monitoring of pressures, flows, and equipment condition. All control and protection 
functions described herein  are internal to the High -Pressure Pumping System, with upstream reference to Group 
1 limited to feed availability only.  
High-Pressure Feed Pump (BH -09-001) 
The high -pressure feed pump (BH -09-001) is the only actively controlled equipment within the High -Pressure 
Pumping System. The pump is driven by a variable speed drive and regulated by a discharge pressure control 
loop (PID)  to maintain the required feed pressure to the first -stage RO membranes.  
Pump start -up is initiated in automatic or remote mode once all upstream permissive conditions are satisfied. 
Suction conditions are verified prior to start by monitoring pump suction pressure using PIT -09-001, ensuring 
adequate inlet pressure is AVAILABLE  to prevent cavitation.   
Upon receipt of a start command, the pump is started at minimum VSD speed to establish initial flow and stabilize 
hydraulic conditions within the discharge piping and RO feed header.  
Following a successful start, pump speed is ramped up gradually by the VSD to increase discharge pressure in a 
controlled manner. The ramp -up rate is limited to avoid hydraulic shock, membrane stress, and excessive transient 
loading on downstream equipment.  
During ramp -up, pump discharge pressure measured at PIT -09-002 is continuously monitored. If abnormal 
conditions occur ; such as low suction pressure detected by PIT -09-001 or excessive discharge pressure at PIT -
09-002; the ramp -up sequence is halted and alarms or pump shutdown actions are initiated in accordance with the 
protection logic.  
Once the required discharge pressure is reached and stabilized, the pump transitions into normal closed -loop 
pressure control.  
The process variable (PV) for the control loop is the pump discharge pressure measured at PIT -09-002. The 
manipulated variable (MV) is the pump speed command to the VSD. The controlled variable (CV) is the first -stage 
RO feed pressure. Pump speed is adjusted automatically to maintain discharge pressure within the normal 

============================================================
--- PAGE 34 ---
============================================================
 
 34 of 48 
© BW Water  
 
operating range defined by the process desig n; the high -pressure pump discharge pressure setpoint shall be 
established to meet the RO Stage 1 feed pressure requirement under worst -case operating conditions, including 
start-up and scenarios where turbocharger energy recovery is un AVAILABLE . Turbochargers operate as passive 
hydraulic devices and do not impose independent pressure requirements or participate in control. Any pressure 
recovered by the turbochargers is treated as a hydraulic offset that reduces pump duty without altering the pre ssure 
control setpoint  (ensures stable RO operation while inherently accommodating turbocharger performance across 
the full operating envelope ). 
RO system hydraulic continuity is confirmed by permeate and reject flow indication measured on the common 
permeate and reject headers using FIT -09-003 and FIT -09-004. These signals are used for indication and 
protection only to confirm that flow is established through the RO membrane system and do not participate in 
closed -loop control of the high -pressure pump.  
Feed Turbocharger (SIP -09-001) 
The feed turbocharger (SIP -09-001) is a passive hydraulic energy recovery device that transfers pressure energy 
from the second -stage RO reject stream to the incoming RO feed upstream of the high -pressure pump. The unit 
does not generate pressure independently and does not participate in any closed -loop control or regulation.  
Under normal design operating conditions, the second -stage reject stream exits at approximately 59 -60 barg. The 
feed turbocharger hydraulically recovers a portion of this residual pressure and transfers it to the feed stream, 
providing an effective pressure boost depending on operating flow and recovery conditions. This reduces the net 
pressure rise req uired from the high -pressure feed pump to achieve the required Stage 1 RO feed pressure.  
The feed turbocharger operates automatically whenever sufficient reject pressure and flow are AVAILABLE . 
Pressure recovery varies naturally with reject -side hydraulic conditions and requires no operator intervention. 
Pressure at the reject inlet is monitored by PIT -09-007, installed on the second -stage RO reject (brine) line 
immediately upstream of the feed turbocharger inlet, to confirm AVAILABLE  reject pressure and detect abnormal 
hydraulic conditions. The boosted feed pressure downstream of the feed turb ocharger is monitored by PIT -09-003, 
installed on the RO Stage 1 feed line downstream of SIP -09-001, to indicate recovered pressure contribution and 
support alarm functions. PIT-09-008 at the feed turbocharger reject outlet  indicates  reject (brine) discharge 
pressure downstream of the feed turbocharger to monitor AVAILABLE  energy recovery pressure and detect 
abnormal hydraulic conditions. These PITs are for indication and alarm only and do not participate in control.  
  

============================================================
--- PAGE 35 ---
============================================================
 
 35 of 48 
© BW Water  
 
Interstage Turbocharger (SIP -09-002) 
The interstage turbocharger (SIP -09-002) transfers hydraulic pressure energy from the RO Stage 1 reject stream 
to the RO Stage 2 feed stream, enabling pressure reuse between RO stages without additional mechanical energy 
input.  
Based on design conditions, the RO Stage 2 feed stream downstream of the interstage turbocharger is 
approximately 77 barg, with a corresponding Stage 2 brine outlet pressure of approximately 46 barg. The interstage 
turbocharger recovers a portion of the St age 1 reject pressure and transfers it hydraulically to the Stage 2 feed, 
increasing the AVAILABLE  feed pressure to the second -stage RO membranes while reducing the pressure duty 
required from upstream pumping.  
The interstage turbocharger operates passively through hydraulic coupling and does not participate in pressure, 
flow, or recovery control loops. Pressure transfer varies naturally with reject pressure, feed flow, and system 
recovery.  
Interstage pressures are monitored for indication and alarm purposes only using the following instruments:  
• PIT-09-004, installed on the RO Stage 1 reject line immediately upstream of the interstage turbocharger 
inlet, to confirm AVAILABLE  reject pressure for energy transfer.  
• PIT-09-005, installed on the RO Stage 2 feed line immediately downstream of the interstage turbocharger 
outlet, to indicate boosted feed pressure entering RO Stage 2.  
• PIT-09-006, installed on the RO Stage 2 feed line upstream of the interstage turbocharger, to provide a 
reference pressure for evaluating pressure gain across SIP -09-002. 
These instruments do not participate in closed -loop control and are provided solely to indicate interstage hydraulic 
conditions and generate alarms under abnormal operation.  
*** See alarm and setpoint lists for specific details.  
Second -Stage Brine Bypass Control  
Under normal seawater operating conditions (approximately 53,000 ppm TDS), the second -stage RO brine stream 
exits the membrane system at sufficiently high pressure, typically in the range of 75 -83 barg. Under these 
conditions, adequate hydraulic energy is AVAILABLE  for stable operation of the feed turbocharger, and the brine 
bypass valve VE -09-002 remains closed, allowing the full second -stage brine flow to pass through the turbocharger 
for maximum energy recovery with no bypass flow.  
At reduced salinity conditions (approximately 43,000 ppm TDS), second -stage brine pressure decreases to 
approximately 59 -61 barg, reducing the amount of recoverable hydraulic energy AVAILABLE  to the feed 
turbocharger. To maintain stable turbocharger operation and prevent operation outside vendor -defined limits, a 
portion of the second -stage brine flow is diverted through the bypass line. Typical bypass flow under these 
conditions is approximately 3.2 -3.3 m³/h, with the remaining brine continuing through the  turbocharger for partial 
energy recovery.  

============================================================
--- PAGE 36 ---
============================================================
 
 36 of 48 
© BW Water  
 
 
The control system continuously evaluates feed turbocharger operating conditions using pressure measurements 
on both sides of the device. Second -stage RO brine pressure upstream of the feed turbocharger, measured by 
PIT-09-007, represents the AVAILABLE  reject -side hydraulic energy and is used to identify a low reject pressure 
condition when it falls below a threshold. The recovered pressure delivered to the RO Stage 1 feed downstream 
of the feed turbocharger, measured by PIT -09-003, represents the effective ness of pressure transfer across the 
turbocharger. Degradation of effective pressure gain is evaluated from the relationship between PIT -09-007 (reject -
side pressure) and PIT -09-003 (recovered feed pressure).  
When either a low reject pressure condition is identified by PIT -09-007, OR  the effective pressure gain inferred 
from PIT -09-007 and PIT -09-003 degrades below the minimum criterion, the control system progressively opens 
the brine bypass valve VE -09-002 to unload the turbocharger by diverting a portion of the second -stage brine flow. 
As operating conditions recover, the bypass valve is correspondingly closed to restore energy recovery. Valve 
modulation is performed gradually to maintain hydraulic stability and avoid oscillation.  
The reject pressure threshold and minimum effective pressure gain criteria used in this logic define the lower 
boundary of stable turbocharger operation. These parameters are established, validated, and tuned during testing 
and commissioning (T&C) in coord ination with the turbocharger vendor based on observed site operating 
conditions and vendor performance characteristics. Following commissioning, the logic operates using the 
configured parameters, with any subsequent changes made only through authorized c onfiguration adjustments.  
During start -up and shutdown, hydraulic conditions are inherently transient and unstable. VE -09-002 is therefore 
commanded open to unload the feed turbocharger and prevent unstable operation. Closing VE -09-002 during start -
up would force 100% of the Stage 2 brine flow through the feed turbocharger immediately, which can create 
operational issues if reject pressure and flow are not yet within a “ NOT FAULT ” and stable range (e.g., low reject 
pressure, fluctuating flow, or incomplete hydraulic stabilization). Once steady -state RO operation is established 
and stable reject -side conditions are confirmed, VE -09-002 is progressively closed to restore maximum ene rgy 
recovery.  
Turbocharger Isolation Valves  
Motorized valve VE -09-007 is provided as on/off isolation valves to allow positive hydraulic isolation of the feed 
and interstage turbochargers during maintenance, CIP preparation, or abnormal operating conditions. This valve 
is normally open during RO operation. When closed, t he associated turbocharger is isolated, and its energy 
recovery function is disabled.  
  

============================================================
--- PAGE 37 ---
============================================================
 
 37 of 48 
© BW Water  
 
 3
.2.2 HIGH-PRESSURE PUMPING SYSTEM PERMISSIVE
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

============================================================
--- PAGE 38 ---
============================================================
 
 38 of 48 
© BW Water  
 
3.3 RO / MEMBRANE SYSTEM  (Group 3)  
Ref P&ID: P22 -DWG -09-009-02-09 
3.3.1 RO / MEMBRANE SYSTEM EQUIPMENT  
Item Equipment Description  Tag No.  
1 RO Stage 1 Membrane Train  BOI-09-001 
2 RO Stage 2  Membrane Train  BOI-09-002 
3.3.2 RO / MEMBRANE SYSTEM INSTRUMENTATION  
Item Instrument Description  Tag No.  
1 RO Membrane System Differential Pressure Transmitter (Overall Membrane 
Resistance)  PDIT -09-003 
2 Permeate Conductivity Analyzer  (Common Permeate Header )  AIT-09-002 
3 Stage -Level Permeate Conductivity Analyzer  AIT-09-003 
4 RO Stage 2 Permeate Flow Transmitter (Stage -Level Permeate Production 
Prior To Mixing)  FIT-09-001 
5 Common Permeate Flow Transmitter (Total RO Permeate Production)  FIT-09-003 
6 RO Reject / Brine Flow Transmitter (Common Reject Header)  FIT-09-004 
7 Permeate Conductivity Analyzer ( Stage -Level Permeate Line Upstream of 
Common Header)   AIT-09-003 
8 RO Stage 1 Reject / Interstage Conductivity Analyzer  AIT-09-004 
9 RO Stage 2 Reject Conductivity Analyzer  AIT-09-005 
10 Motorized Valve ( Permeate to Product) with  Limit Switches  VE-09-003 
10 Motorized Valve ( Permeate to Off -Spec Diversion) with Limit Switches  VE-09-004 
3.3.3 RO / MEMBRANE SYSTEM PROCESS DESCRIPTION  
The RO / Membrane System performs the core desalination function of the plant by separating dissolved salts from 
the pressurized feed stream through a two -stage reverse osmosis (RO) configuration. Pressurized feed supplied 
by the High -Pressure Pumping System enters the RO membrane system at the required operating pressure and 
is distributed to the membrane vessels, where separation into permeate and reject streams occurs across semi -
permeable RO membranes. The system is designed to maximize overall water re covery while maintaining stable 
membrane operation and acceptable hydraulic conditions across both RO stages.  
The RO system is configured as a single (1 × 100%) two -stage RO train, with a total feed flow of approximately 49 
m³/h and a total design permeate capacity of approximately 21 m³/h. The membrane arrangement consists of six 

============================================================
--- PAGE 39 ---
============================================================
 
 39 of 48 
© BW Water  
 
(6) pressure vessels in RO Stage 1 and four (4) pressure vessels in RO Stage 2, with seven (7) membrane 
elements per vessel.  
In RO Stage 1, the incoming pressurized feed is introduced to the Stage 1 membrane vessels. A portion of the 
feed passes through the membranes as permeate and is discharged at near -atmospheric pressure to the permeate 
collection header. The remaining concentrated stream exits the Stage 1 membrane vessels as reject and is routed 
onward to RO Stage 2 through the interstage connection.  
In RO Stage 2, the partially desalinated feed from Stage 1 is further processed through the Stage 2 membrane 
vessels. Additional permeate is extracted and routed to the same permeate collection header as Stage 1 permeate. 
The reject stream from RO Stage 2 exits the membrane system and is routed downstream  (RO Reject stream by 
client)  
Permeate streams from RO Stage 1 and RO Stage 2 are combined in a common permeate header. Final permeate 
quality is represented by a conductivity analyzer installed upstream of the common permeate header, providing 
indication of blended permeate quality fr om the complete RO system.  
Stage -level and system -level hydraulic conditions within the RO membrane system are represented by differential 
pressure measurements across the RO membrane . Differential pressure indicators installed across RO Stage 1 
and RO Stage 2 provide indication of membrane resistance and fouling tendencies. These instruments represent 
membrane hydraulic characteristics only and do not alter process flow or participate  in control.  
The RO / Membrane System is limited to the physical separation of feed into permeate and reject streams within 
the membrane vessels. Pressure generation, pressure recovery, hydraulic control, and pump operation are 
handled by the High -Pressure Pumping System, while downstream permeate handling, diversion, and disposal 
functions are addressed in other system groups.  
3.3.4 RO / MEMBRANE SYSTEM OPERATIONS AND CONTROL  
The RO / Membrane System is controlled to monitor membrane hydraulic performance, assess permeate quality, 
and determine off -spec conditions. Control actions within this group are limited to monitoring, quality evaluation, 
and permeate routing commands. The system does not regulate pressure or flow and does not modulate upstream 
equipment.  
The detailed operational logic for RO startup, shutdown, flushing, transition between operating states, and 
interaction with the CIP system shall be defined in a dedicated RO Control / Sequence Chart, issued as a separate 
document. This section describes c ontrol intent and functional ity only. 
  

============================================================
--- PAGE 40 ---
============================================================
 
 40 of 48 
© BW Water  
 
RO Membrane Trains (Stage 1 and Stage 2)  
The RO membrane trains comprise Stage 1 and Stage 2 membrane vessels operating in series. Membrane 
hydraulic condition across the combined RO membrane system is monitored using differential pressure 
transmitter PDIT -09-003, installed across the membrane train as shown on the P&ID.  
The signal from PDIT -09-003 provides indication of overall membrane resistance and is used for monitoring, 
alarming, and performance trending. Increasing or abnormal differential pressure indicates membrane fouling, 
scaling, or blockage. This instrument does not initiate any hydr aulic control actions and does not influence feed 
pressure, flow, or recovery . 
Permeate Outlet - Flow & Quality Monitoring  
The combined permeate outlet from the RO membrane system is equipped with a conductivity analyzer consisting 
of AIT -09-002, installed upstream of the common permeate system header. The conductivity signal represents the 
final blended permeate quality from all RO stages and is evaluated to determine overall permeate acceptability.  
A flow meter  (FIT-09-003) installed  at the common permeate header measures the total permeate production rate 
from the RO system. This measurement provides operators with real -time indication of RO output and supports 
performance monitoring, trending, and mass balance calculations such as RO recovery. The permeate flow signal 
is used primarily for indication, reporting, and performance assessment rather than direct control.  
In addition to combined permeate monitoring, stage -level performance is monitored upstream of the common 
permeate header. A flow transmitter (FIT -09-001) installed at the RO Stage 2 permeate outlet indicates  second -
stage permeate production prior to mixing. This measurement is used to monitor stage -level hydraulic performance 
and recovery distribution between RO stages.  
A conductivity analyzer (AIT -09-003) provides stage -specific permeate quality indication. This measurement 
supports early detection of membrane performance degradation or integrity issues at the stage level before effects 
are observed on the combined permeate stream.  
RO Reject , Off spec  and Intermediate Streams  
Conductivity analyzers AE -09-004 / AIT -09-004 and AE -09-005 / AIT -09-005, installed on RO reject and 
intermediate streams as shown on the P&ID, provide supplementary indication of membrane stage performance 
and salt balance.  
These analyzers are used for monitoring and diagnostic purposes only.  
An off -spec condition is determined within the RO / Membrane System based on permeate quality. Permeate 
conductivity measured by AE -09-002 / AIT -09-002 is evaluated against the defined acceptable quality limit.  
When the measured permeate conductivity exceeds the allowable limit for a validated duration, the RO / Membrane 
System declares an off -spec condition. This declaration represents a quality -based status used to initiate permeate 
routing actions.  
Permeate routing downstream of the RO membrane system is executed using motorized valves installed on the 
permeate outlet piping.  

============================================================
--- PAGE 41 ---
============================================================
 
 41 of 48 
© BW Water  
 
• VE-09-003 - Permeate to product  
• VE-09-004 - Permeate to off -spec 
Under normal operating conditions, VE -09-003 is open and VE -09-004 is closed. Upon declaration of an off -spec 
condition, VE -09-003 is closed and VE -09-004 is opened to divert permeate away from the product system. Valve 
position feedback is monitored to confirm correct routing.  
From Client side, two (2) Digital Output (DO), dry free contact signals shall be provided to the RO plant control 
system:  
 (1) Permissive to fill Permeate Tank, and  
(2) Permissive to fill Off Spec Tank.  
The logic of the Client DO signals (received as DI in the RO plant control system) is: TRUE (1) means permissive 
to fill the tank, and FALSE (0) means not allowed to fill the tank. These permissive signals shall be used as 
interlocks to enable the respecti ve filling/diverting valves. Loss of signal shall default to FALSE (0) (not allowed to 
fill the tank) as fail -safe.  
RO Performance Monitoring Indicators  
RO system performance is monitored using calculated indicators derived from existing flow and conductivity 
measurements to provide visibility of hydraulic balance and membrane separation efficiency. These indicators are 
intended to support operational awar eness, performance trending, and diagnostic assessment during normal RO 
operation.  
Overall RO recovery is calculated using a mass balance across the membrane system based on permeate and 
reject flow measurements. RO recovery is determined as the ratio of common permeate flow measured by FIT -09-
003 to the sum of permeate flow (FIT -09-003) and reject (brine) flow measured by FIT -09-004, expressed as a 
percentage. This calculated value provides indication of the fraction of pressurized feed converted to permeate 
and supports monitoring of recovery trends and operating stability.  
RO Recovery (%) = FIT -09-003 / (FIT -09-003 + FIT -09-004) × 100  
This calculation assumes steady -state operation and is intended for trending rather than instantaneous control.  
Membrane salt separation performance is represented by an indicative salt rejection calculation derived from 
conductivity measurements on the permeate and reject streams. Salt rejection is calculated by comparing 
permeate conductivity measured by AIT -09-002 against reject conductivity measured by AIT -09-005, expressed 
as a percentage. Where applicable, an interstage salt rejection indicator may also be derived using conductivity 
measured on the Stage 1 reject (interstage) line upstream of the interstage tur bocharger. These calculated values 
provide visibility of membrane separation behavior and support trending and diagnostic evaluation of membrane 
performance over time.  
  

============================================================
--- PAGE 42 ---
============================================================
 
 42 of 48 
© BW Water  
 
Overall Salt Rejection (%) = [1 − (AIT -09-002 / AIT -09-005)] × 100  
Interstage Salt Rejection Indicator (%) = [1 − (AIT -09-002 / AIT -09-004)] × 100  
Stage -2 Salt Rejection (%) = [1 − (AIT -09-003 / AIT -09-004)] × 100  
CIP Trigger Indication  
The RO membrane system provides performance indications that may prompt evaluation for Cleaning -in-Place 
(CIP). These indications include sustained or increasing differential pressure indicated by PDIT -09-003 and 
persistent degradation of permeate quality indicated by AE -09-002 / AIT -09-002. 
These indications support maintenance decision -making only. CIP execution is handled within the CIP system and 
documented separately.  More details provided in the CIP Group Section.   

============================================================
--- PAGE 43 ---
============================================================
 
 43 of 48 
© BW Water  
 
 
3.3.4 RO / MEMBRANE SYSTEM READY PERMISSIVES  
The RO / Membrane System shall be permitted to operate when the following conditions are satisfied:  
• No active fault or trip is present within the RO / Membrane System, and  
• Differential pressure indication across the RO membrane system (PDIT -09-003) is AVAILABLE  and NOT 
FAULT , and  
• Permeate conductivity analyzer (AE -09-002 / AIT -09-002) is AVAILABLE  and NOT FAULT , and  
• Permeate routing valve VE -09-003 (permeate to product) is AVAILABLE  and able to operate, and  
• Off-spec diversion valve VE -09-004 (permeate to off -spec) is AVAILABLE  and able to operate, and  
• Client Permeate Tank permissive signal is AVAILABLE and NOT FAULT , and  
• Client Off -Spec Tank permissive  signal is AVAILABLE and NOT FAULT , and  
• System is selected in REMOTE and AUTO.  
IF the above conditions are satisfied, THEN  RO / Membrane System is considered AVAILABLE  for operation.   

============================================================
--- PAGE 44 ---
============================================================
 
 44 of 48 
© BW Water  
 
 
3.6 CIP/FLUSHING SYSTEM (GROUP 4)  
Ref P&ID: P22 -DWG -09-009-02-10  
3.6.1  CIP/FLUSHING SYSTEM  EQUIPMENT  
Item Equipment Description  Tag No.  
1 CIP Tank  TK-09-001 
2 CIP Pump  BH-09-002 
3 CIP Heater  REL-09-001 
4 CIP Cartridge Filter  FIL-09-002 
3.6.2  CIP/FLUSHING SYSTEM INSTRUMENTATION  
Item Instrument Description  Tag No.  
1 CIP Tank Level Transmitter  LIT-09-002 
2 CIP Solution Temperature Element  TE-09-002 
3 CIP Solution Temperature  TIT-09-001 
4 CIP Solution pH Analyzer  AIT-09-001 
5 CIP Circulation Flow Transmitter  FIT-09-005 
6 Motorized Valve - CIP Make -up / Chemical Fill with Limit Switches  VE-09-005 
7 Motorized Valve – Interstage Isolation Valve  with Limit Switches  VE-09-007 
8 Motorized Valve - CIP Return from RO  Stage 1  with Limit Switches  VE-09-009 
9 Motorized Valve - CIP Return from RO Stage 2  with Limit Switches  VE-09-010 
10 Motorized Valve - CIP Feed to RO  Stage 1  with Limit Switches  VE-09-012 
11 Motorized Valve - CIP Feed to RO Stage 2  Path with Limit Switches  VE-09-013 
3.6.3  CIP PROCESS DESCRIPTION  
The CIP / Flushing System is provided to prepare, store, heat, circulate, and return cleaning solutions for periodic 
chemical cleaning of the RO membrane system. The system operates independently of normal RO production and 
is used only when the RO membran e system is isolated and placed in CIP mode.  
Cleaning solution is prepared and stored in the CIP tank TK -09-001, which provides sufficient volume for circulation 
through the RO membrane stages. The tank is equipped with level indication to allow monitoring of AVAILABLE  
solution volume during preparation and circulation.  
 

============================================================
--- PAGE 45 ---
============================================================
 
 45 of 48 
© BW Water  
 
Heating of the CIP solution is provided by the CIP heater REL -09-001, enabling the solution to reach and maintain 
the required cleaning temperature prior to and during circulation. The heated solution is circulated from the CIP 
tank through the RO membrane  system and returned to the tank, forming a closed -loop circulation path.  
Circulation of the CIP solution is achieved using the CIP pump BH -09-002, which draws solution from the CIP tank 
and delivers it through the CIP piping, cartridge filter, and RO membranes before returning to the tank. A cartridge 
filter FIL -09-002 is insta lled in the CIP circulation line to remove suspended solids and protect the RO membranes 
during cleaning.  
The chemical condition of the CIP solution is monitored to verify solution suitability during cleaning. Flow, 
temperature, pressure, level, and pH measurements provide visibility of CIP operating conditions but do not alter 
the hydraulic configuration of t he RO system.  
CIP solution routing to and from the RO membrane system is achieved through dedicated CIP feed and return 
piping equipped with motorized isolation valves. These valves allow individual or collective cleaning of RO 
membrane stages as required. Upon completi on of circulation, the CIP solution is either retained in the tank or 
drained for disposal.  
  

============================================================
--- PAGE 46 ---
============================================================
 
 46 of 48 
© BW Water  
 
3.6.4 CIP OPERATION AND CONTROL  
The CIP / Flushing System operates in a dedicated CIP mode and is enabled only when the RO membrane system 
is confirmed isolated via an RO system status signal. Control actions are supervisory and sequence -based, with 
interlocks and alarms provided to ensu re safe and effective cleaning.  
Detailed execution of CIP steps is defined in the CIP sequence charts.  
CIP Tank - TK-09-001 
The CIP tank TK -09-001 stores the cleaning solution required for membrane cleaning. Tank level is monitored 
using LI -09-001 and LIT -09-002. These signals are used for indication, alarming, and pump protection only. No 
automatic level control is implemented.  
High-level and low -level alarms alert operators to abnormal filling or depletion. Low -Low level (LALL) conditions 
are used to inhibit or trip the CIP pump to prevent dry running.  
The CIP heater REL -09-001 is provided to heat the CIP cleaning solution in TK -09-001 prior to and during 
circulation. CIP solution temperature is monitored using TE -09-002 / TIT -09-001. Heater operation is controlled in 
ON/OFF mode based on the measured CI P solution temperature and a configured temperature setpoint for the 
selected CIP phase. When the measured temperature is below the setpoint (minus deadband), the heater is 
energized; when the measured temperature reaches the setpoint (plus deadband), the heater is de -energized.  
Heater operation is enabled only when the CIP system is in CIP mode and sufficient tank level is confirmed. High 
temperature alarms are provided to protect equipment and maintain chemical stability.  
CIP Pump - BH-09-002 
The CIP pump BH -09-002 circulates cleaning solution from the CIP tank through the RO membrane system and 
back to the tank. The pump is equipped with a variable speed drive (VFD), allowing the pump speed to be adjusted 
to meet the hydraulic requirements of different CIP opera ting phases.  
Pump start and stop commands are issued from the control system when the CIP mode is active and required 
interlocks are satisfied. Pump speed is set manually by the operator or automatically by the CIP sequence logic 
according to the active CIP phase. The VFD is used for speed adjustment and soft starting ; during CIP circulation  
step, the  flow is verified using FIT -09-005. For each CIP phase (Stage 1 or Stage 2), the sequence applies a 
predefined VFD speed setpoint for BH -09-002 and confirms that the measur ed circulation flow is above the 
minimum required value for the selected stage. If the measured flow is below the minimum criterion after a 
stabilization delay, the CIP sequence generates a low -flow alarm and holds progression until flow is restored by 
operator adjustment or by automatic speed trim (if enabled). This function is implemented as a permissive 
sequence  and not as closed -loop flow control.  

============================================================
--- PAGE 47 ---
============================================================
 
 47 of 48 
© BW Water  
 
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

============================================================
--- PAGE 48 ---
============================================================
 
 48 of 48 
© BW Water  
 
3.6.5  CIP / FLUSHING SYSTEM  READY PERMISSIVES  
The CIP / Flushing System shall be permitted to operate when the following conditions are satisfied:  
• RO system CIP Mode / Isolated status is TRUE, and  
• No active fault or trip is present within the CIP / Flushing System, and  
• CIP tank level is above the minimum required level as indicated by LIT -09-002 and NOT FAULT , and  
• No Low -Low Level (LALL) condition is present in CIP tank TK -09-001 as indicated by LIT -09-002, and  
• CIP solution temperature measurement (TE -09-002 / TIT -09-001) is AVAILABLE  and NOT FAULT , and  
• CIP circulation flow measurement (FIT -09-005) is AVAILABLE  and NOT FAULT , and  
• CIP solution pH measurement (AE -09-001 / AIT -09-001) is AVAILABLE  and NOT FAULT , and  
• CIP pump BH -09-002 and its VFD are AVAILABLE  and not faulted, and  
• CIP interface valves ( VE-09-005, VE-09-007, VE-09-009, VE-09-010 and VE-09-012, and VE-09-013 ) 
are AVAILABLE  and NOT FAULT, and  
• System is selected in REMOTE and AUTO.  
IF the above conditions are satisfied, THEN  CIP / Flushing System is considered AVAILABLE  for operation.  
Instrument availability refers to signal health and communication status only and not to measured process 
values. Manual valve alignment and routing verification are performed via operating procedures and the CIP 
sequence and are not enforced as PLC permis sives.  
3.6.6 CIP START/STOP Automatic Sequence  
Detailed logic, valve sequencing, and timing are defined in the RO Flushing Sequence Chart  and CIP Sequence 
Chart . 
 

## 2. CONTROL PHILOSOPHY REV A — ESTRUCTURA/METADATA (md resumen)
================================================================================
# P22-BT-09-009-001 — Control Philosophy Rev A

**Tipo:** "BT" — Código no catalogado en sistema P22
**Título:** Control Philosophy — Second Stage RO Module for Brine – PD Taltal
**Código ADASA:** P22-BT-09-009-001
**Revisión:** A | **Fecha Rev A:** 2026/03/06
**Preparado por:** JON | **Revisado:** DS/YFV | **Aprobado:** AS/GHY/NHH, JR
**Páginas:** 48

---

## Estructura del Documento

| Sección | Contenido |
|---------|-----------|
| 1.1 | PLC Platform |
| 1.2 | Operator Interface Platform (HMI) |
| 1.3 | Power Interruption / Power Up |
| 1.4 | Operator Interface (4 niveles de acceso) |
| 1.5 | HMI Display Color Coding |
| 2.1 | Motor Control Functions (DOL, Soft Start, VSD) |
| 2.2 | Instrumentation and Control Functions |
| 2.3 | Valve Control (Motor Operated ON/OFF) |
| 2.4 | PID Closed Loop Control |
| 2.5 | Chemical Dosing Ratio Control |
| 3.1 | Feed Preparation System (Group 1) |
| 3.2 | High-Pressure Pumping System (Group 2) |
| 3.3 | RO / Membrane System (Group 3) |
| 3.6 | CIP/Flushing System (Group 6) |

## Documentos de Referencia en el Documento

| Tipo | Código |
|------|--------|
| P&ID | P22-DWG-09-009-0002 (portada) / P22-DWG-09-009-02-08 y -02-11 (sección 3.1) |
| PFD | P22-DWG-09-009-0001 |
| Controls & Sequence Chart | SEPARATE DOCUMENT (no submitado) |
| Alarm & Control Setpoint List | SEPARATE DOCUMENT (no submitado) |
| Control System Architecture | P22-CD-09-004-0001 |

## Puntos Clave del Contenido

### Plataforma de Control
- PLC en red ring para redundancia
- HMI con 4 niveles de acceso: Guest / Operator / Supervisor / Administrator
- Color coding estándar (Verde=OK, Rojo=Falla, Ámbar=Fault)

### UPS (Sección 1.3)
- "The UPS will provide **30 minutes** of power to ensure the controls and instrumentation do not shutdown."
- Tras pérdida de poder: sistema pasa a OFFLINE state, NO reinicia automáticamente.

### Control de Motores
- DOL, Soft Start, VSD — todos documentados con IOs al PLC y HMI
- Configuración Duty/Standby con switchover automático por PLC

### Instrumentación
- Señal estándar: 4-20mA
- Alarmas: HH / H / L / LL con deadband y time delay
- Modos: AUTO / MANUAL / MAINTENANCE / SIMULATE

### Grupos de Equipos Identificados
- Group 1: Feed Preparation (cartridge filter, static mixer, antiscalant dosing)
- Group 2: High-Pressure Pumping (HP Pump, Feed TC, Interstage TC)
- Group 3: RO/Membrane System (1st + 2nd stage vessels)
- Group 4 (numerado 3.6): CIP/Flushing System

### Tags Identificados en Sección 3.1
| Item | Tag | Descripción |
|------|-----|-------------|
| FIL-09-001 | FIL-09-001 | RO Cartridge Filter |
| MZE-09-001 | MZE-09-001 | Static Mixer |
| TK-09-002 | TK-09-002 | Antiscalant Dosing Tank |
| BDS-09-001 | BDS-09-001 | Antiscalant Dosing Pump 1 |
| BDS-09-002 | BDS-09-002 | Antiscalant Dosing Pump 2 |
| DPS-09-001 | DPS-09-001 | RO CF DP Switch |
| ORP-IT-09-001 | ORPIT-09-001 | ORP Analyzer |
| CIT-09-001 | CIT-09-001 | Conductivity Analyzer |
| FIT-09-001 | FIT-09-001 | Flowmeter downstream CF |
| LSH-09-001 | LSH-09-001 | Antiscalant Tank LS High |
| **VE-07-014** | VE-07-014 | Antiscalant Tank Inlet MV (Instrument table) |
| **VE-07-016** | VE-07-016 | Antiscalant Pump DS MV (Instrument table) |
| **VE-09-014** | VE-09-014 | Same valve referenced in section 3.1.3 as VE-09-014 |
| **VE-09-016** | VE-09-016 | Same valve referenced in section 3.1.3 as VE-09-016 |

**DISCREPANCIA DE TAGS:** La tabla de instrumentos usa VE-07-014 y VE-07-016, pero el texto descriptivo de la misma sección usa VE-09-014 y VE-09-016.

---

## Observaciones ADASA (Revisión E14)

### OBS-A: Código "BT" no definido en sistema de codificación P22
El tipo "BT" no existe en el sistema de codificación del proyecto (P22-TT-AA-DDD-NNN-R). Los tipos válidos son: ET, DWG, LI, CD, TM, CT, IT. BW Water debe definir qué significa "BT" en el registro de documentos del proyecto, o reclasificar el documento con un código type válido.

### OBS-B: UPS 30 minutos vs requerimiento ET 8 horas (CRÍTICO)
El documento establece: "The UPS will provide 30 minutes of power."
El ET (sección de Control y Automatización) requiere: "Para el control debe suministrarse una UPS con la capacidad suficiente para mantener el sistema de control activo por al menos **8 horas**."
30 minutos es insuficiente. Requiere corrección urgente y actualización del cálculo de capacidad de UPS.

### OBS-C: Discrepancia de tags de válvulas antiscalante
La tabla de instrumentos Section 3.1.2 usa VE-07-014 y VE-07-016, mientras que la descripción operacional Section 3.1.3 usa VE-09-014 y VE-09-016 para los mismos equipos. Resolver y alinear con Valve List Rev C y P&ID.

### OBS-D: Inconsistencia en referencias al P&ID
- Introducción: referencia P22-DWG-09-009-0002
- Sección 3.1: referencia P22-DWG-09-009-02-08 y P22-DWG-09-009-02-11
Formatos de código distintos para el mismo P&ID o diferentes planos. Aclarar qué documentos son los P&IDs vigentes del sistema.

### OBS-E: Modbus TCP Memory Map — no abordado
El documento NO contiene referencia a la interface Modbus TCP/IP requerida para integración con el SCADA de la planta principal. El ET requiere comunicación Modbus TCP/IP. La Control Philosophy debería al menos definir qué variables se exponen vía Modbus. El Memory Map sigue pendiente desde TM N2 (65 días a la fecha de este transmittal).

### OBS-F: Documentos complementarios no submitados
La Control Philosophy referencia explícitamente:
- Operating Sequence Chart: "SEPARATE DOCUMENT" — no submitado
- Alarm and Control Setpoint List: "SEPARATE DOCUMENT" — no submitado
Estos documentos son necesarios para una comprensión completa del sistema de control. BW Water debe comprometerse a una fecha de entrega.

**Veredicto ADASA: 3 — To be Revised**
Crítico: OBS-B (UPS 30 min vs 8 h), OBS-C (tags discrepantes), OBS-D (P&ID inconsistente), OBS-E (Modbus TCP no abordado).


## 3. CONSOLIDATED COMMENT SHEET EN REV B
================================================================================

**OBSERVACION CRITICA:** Se verifico el contenido completo de Rev B (ENTREGA 33)
con grep por patrones 'CONSOLIDATED', 'Comment Sheet', 'Reply from', 'Comment from Client'.
**Rev B NO incluye Consolidated Comment Sheet.** BW Water no documento como respondieron
a los comentarios previos de Rev A en la entrega de Rev B. Este es en si un finding de audit.


## 4. DOCUMENTOS DE CONTROL APROBADOS EN TM N14 (cross-reference)
================================================================================

Los siguientes documentos fueron aprobados Code 1 o 2 en TM N14 (15-Apr-2026) y deben
ser consistentes con Control Philosophy Rev B:

- **IO List Rev C** (P22-LI-09-008-001) — Code 2 TM N14, 141 items. TE-09-001/002 (HP Pump),
  TE-09-003/004 (CIP Pump), TIT-09-006 (CIP Tank). Conductivities CIT-09-001B/004/005 a 0-200 mS/cm.
- **Valve List Rev D** (P22-LI-09-005-002) — Code 2 TM N14, 111 items. VE-09-002 modulating ON/OFF DN25 SDSS.
- **Instrument List Rev C** (P22-LI-09-008-003) — Code 2 TM N14, 39 items. Wilcoxon PCH420V-M12 vibration (0-127 mm/s, HART 7.0).
- **Data Transfer List Rev B** (P22-LI-09-008-004) — Code 2 TM N14, 189 Modbus entries.
- **P&ID Rev C** (P22-DWG-09-009-002) — Code 2 TM N13.
- **Control System Architecture Rev D** (P22-CD-09-004-001) — Code 1 TM N14. UPS 8h runtime confirmed.

**Dato clave Instrument List Rev C:** Motor RTDs son TE (no TIT) — modulo 5069-IY4 lee RTD directo sin loop 4-20mA.
TIT-09-006 es CIP Tank process temp con Rosemount 644 transmitter.

**Dato clave Oferta Tecnica Rev1 (performance):**
- SEC garantizada: 4.71 kWh/m3 +/- 5%
- SEC limite contractual: <= 5.0 kWh/m3 at TDS 53,000 ppm


## 5. BAE 12803 PLANTA MODULAR — TEXTO COMPLETO
================================================================================
# BAE 12803 - Bases Administrativas Especiales - Planta Modular

## Metadatos
- **Archivo origen**: BAE 12803 PLANTA MODULAR - VF (Parte 1 y 2)
- **Paginas totales**: 94
- **Fecha extraccion**: 2025-11-25

---

## PARTE 1 - Bases Administrativas Especiales (Paginas 1-50)



---

### Pagina 1
---
BASES  ADMINISTRATIVAS  ESPECIALES   
Licitación 12 803  
Módulo RO Segunda Etapa para  Salmuera  
PD Taltal   
AGUAS  DE ANTOFAGASTA  S.A. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Antofagasta,  Junio  2025  

---

### Pagina 2
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
2/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 INDICE  
I. GENERALIDADES  ................................ ................................ ................................ ................................ ... 5 
1. NOMBRE  DE LA LICITACIÓN  ................................ ................................ ................................ .................  5 
2. PROPOSITO  Y ALCANCE  ................................ ................................ ................................ .......................  5 
3. DESCRIPCIÓN  Y ALCANCE  GENERAL  DEL PROYECTO  ................................ ................................ .... 5 
4. LEY APLICABLE  ................................ ................................ ................................ ................................ ...... 6 
5. DOMICILIO  ................................ ................................ ................................ ................................ ...............  7 
6. IDIOMA  OFICIAL  ................................ ................................ ................................ ................................ ...... 7 
7. ADMINISTRACIÓN  DEL CONTRATO ................................ ................................ ................................ .. 7 
8. DEFINICIONES  ................................ ................................ ................................ ................................ ........  8 
II. DE LA LICITACIÓN  ................................ ................................ ................................ ................................ .. 9 
9. LLAMADO  DE LICITACIÓN  ................................ ................................ ................................ .....................  9 
10. TIPO DE LICITACIÓN, TIPO DE CONTRATO, REAJUSTE.  ................................ ................................  11 
11. DOCUMENTOS QUE CONFORMAN LAS BASES DE LICITACIÓN  ................................ ...................  11 
12. DOCUMENTOS  INTEGRANTES  DEL CONTRATO  Y SU ORDEN DE PRELACIÓN  ..........................  13 
13. PROGRAMA  DE LA LICITACIÓN. (Hora de Chile).  ................................ ................................ ..............  14 
14. CONSULTAS Y ACLARACIONES SOBRE LAS BASES DE LICITACIÓN  ................................ ..........  14 
15. ANTECEDENTES  PREVIOS  ................................ ................................ ................................ .................  15 
15.1.  ANTECEDENTES COMERCIALES, FINANCIEROS Y LABORALES  ................................ ..................  15 
15.2.  ANTECEDENTES DE EXPERIENCIA Y RECURSOS  ................................ ................................ .........  16 
15.3.  ANTECEDENTES GENERALES Y LEGALES DEL PROVEEDOR.  ................................ ....................  17 
16. HABILITACIÓN  ................................ ................................ ................................ ................................ ...... 20 
17. PRESENTACIÓN  DE LAS OFERTAS  ................................ ................................ ................................ ... 21 
18. COSTO  DE LA OFERTA.  ................................ ................................ ................................ .......................  23 
19. MONEDA  DE LA OFERTA  ................................ ................................ ................................ .....................  23 
20. ENTREGA  DE OFERTAS TÉCNICAS  ................................ ................................ ................................ ... 23 
20.1.  DOCUMENTOS  OFERTA TÉCNICA ................................ ................................ ................................ ..... 23 
21. ENTREGA DE OFERTAS ECONÓMICAS  ................................ ................................ ............................  25 
21.1.  DOCUMENTOS QUE SE DEBEN INCLUIR EN LAS OFERTAS.  ................................ ........................  25 
22. VALIDEZ  DE LAS OFERTAS  ................................ ................................ ................................ .................  28 

---

### Pagina 3
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
3/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 23. GARANTÍA  DE SERIEDAD  DE LA OFERTA  ................................ ................................ .........................  28 
24. DERECHO A DEJAR SIN EFECTO LICITACIÓN Y OTROS. APERTURA, EVALUACIÓN, 
ADJUDICACIÓN Y CELEBRACION DEL CONTRATO.  ................................ ................................ ....... 30 
24.1.  APERTURA OFERTAS TÉCNICAS  ................................ ................................ ................................ ...... 30 
24.2.  EVALUACIÓN DE OFERTAS TÉCNICAS.  ................................ ................................ ...........................  31 
24.3.  APERTURA DE OFERTAS ECONÓMICAS.  ................................ ................................ .........................  32 
24.4.  EVALUACIÓN  DE LA OFERTA  ECONÓMICA.  ................................ ................................ .....................  33 
24.5.  ADJUDICACIÓN DEL CONTRATO  ................................ ................................ ................................ ....... 34 
24.6.  SUSCRIPCIÓN DEL CONTRATO  ................................ ................................ ................................ .........  35 
III. CONDICIONES  DE EJECUCIÓN  DEL CONTRATO  ................................ ................................ .............  36 
25. MODALIDAD  Y PRECIO  DEL CONTRATO  ................................ ................................ ...........................  36 
26. ALCANCE  Y DESARROLLO  DEL PEDIDO  ................................ ................................ ...........................  37 
27. PLAZO S DE EJECUCIÓN DEL PEDIDO  ................................ ................................ ................................  37 
28. GARANTÍAS  TÉCNICAS  DEL PEDIDO  ................................ ................................ ................................ . 38 
29. BOLETAS  DE GARANTÍAS  ................................ ................................ ................................ ...................  41 
29.1  BOLETA DE GARANTÍA BANCARIA POR ENTREGA DE ANTICIPO.  ................................ ...............  41 
29.2  BOLETA DE GARANTÍA BANCARIA POR FIEL CUMPLIMIENTO DEL CONTRATO  ........................  42 
29.3  BOLETA DE GARANTÍA BANCARIA POR GARANTÍA TÉCNICA O DE DESEMPEÑO DEL EQUIPO.
 ................................ ................................ ................................ ................................ ...............................  43 
29.4  NORMAS COMUNES A LAS BOLETAS BANCARIAS DE GARANTÍA  ................................ ...............  44 
29.5 ALTERNATIVA PARA PROVEEDOR EXTRANJERO  ................................ ................................ ............  45 
29.6 POLIZAS DE SEGURO PARA CUBRIR GARANTIAS.  ................................ ................................ ...........  45 
30. SEGUROS,  ACCIDENTES  E INDEMNIZACIONES  ................................ ................................ ..............  46 
31. FACTURACIÓN  Y CONDICIONES  DE PAGO  ................................ ................................ ......................  49 
32. CONDICIONES DE ANTICIPO ................................ ................................ ................................ ..............  52 
33. ENTREGA  DEL PEDIDO  ................................ ................................ ................................ .......................  53 
34. DOCUMENTACIÓN  TÉCNICA  ................................ ................................ ................................ ..............  53 
35. MATERIALES  Y EQUIPOS  ................................ ................................ ................................ ....................  55 
36. FABRICACIÓN  ................................ ................................ ................................ ................................ ....... 55 
37. CALIDAD,  INSPECCIÓN  Y PRUEBAS  ................................ ................................ ................................ .. 56 
37.1  INTERVENCIÓN DE TERCERO INSPECTOR  ................................ ................................ .....................  60 
37.2  PLAZOS DE REVISIÓN, APROBACIÓN Y COORDINACIÓN POR ADASA DURANTE LA 

---

### Pagina 4
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
4/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 EJECUCIÓN  ................................ ................................ ................................ ................................ ..........  61 
38. EMBALAJE  Y MARCADO  ................................ ................................ ................................ ......................  62 
39. EXPEDICIÓN  Y ENTREGA  ................................ ................................ ................................ ...................  63 
40. COMISIONAMIENTO  Y PUESTA  EN MARCHA  ................................ ................................ ...................  66 
41. RECEPCIÓN  PROVISIONAL  ................................ ................................ ................................ .................  69 
42. RECEPCIÓN  DEFINITVA  ................................ ................................ ................................ ......................  70 
43. MULTAS  ................................ ................................ ................................ ................................ .................  70 
43.1  MULTAS POR ATRASOS  ................................ ................................ ................................ .....................  70 
43.2  MULTAS POR INCUMPLIMIENTO DE GARANTÍAS DE DESEMPEÑO (APLICABLES SEGÚN 
RESULTADOS PRUEBAS ET SEC. 10.2):  ................................ ................................ ...........................  72 
43.3 OTROS INCUMPLIMIENTOS ................................ ................................ ................................ ................  74 
43.4  LÍMITE Y APLICACIÓN DE MULTAS:  ................................ ................................ ................................ .. 74 
44. FUERZA  MAYOR  ................................ ................................ ................................ ................................ ... 74 
45. CUMPLIMIENTO  DE LAS LEYES  ................................ ................................ ................................ .........  76 
46. CESIÓN  Y SUBCONTRATACIÓN  ................................ ................................ ................................ .........  77 
47. PATENTES  Y ROYALTIES  ................................ ................................ ................................ ....................  79 
48. SUSPENSIÓN  TEMPORAL  ................................ ................................ ................................ ...................  79 
49. INCUMPLIMIENTO  POR  EL PROVEEDOR  ................................ ................................ ..........................  80 
50. CANCELACIÓN  Y RESOLUCIÓN  DEL PEDIDO  ................................ ................................ ...................  82 
51. CONFIDENCIALIDAD  ................................ ................................ ................................ ............................  84 
52. PUBLICIDAD  ................................ ................................ ................................ ................................ ..........  85 
53. TRANSFERENCIA  DE TITULARIDAD  Y RIESGOS  ................................ ................................ ..............  85 
54. DECLARACION  DEL PROVEEDOR  ................................ ................................ ................................ ..... 86 
55. SOLUCIÓN DE CONTROVERSIAS  ................................ ................................ ................................ ...... 86 
55.1  SOLICITUDES Y RECLAMOS  ................................ ................................ ................................ ..............  86 
55.2  SOLICITUD DE COMPENSACIÓN  ................................ ................................ ................................ ....... 87 
55.3  RECLAMOS Y ARBITRAJE ................................ ................................ ................................ ...................  87 
56. MEDIO  AMBIENTE  ................................ ................................ ................................ ................................  91 
57. LÍMITE DE RESPONSABILIDAD  ................................ ................................ ................................ ..........  92 
58. RESPONSABILIDAD PENAL EMPRESARIAL  ................................ ................................ .....................  93 
 

---

### Pagina 5
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
5/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 I. GENERALIDADES  
1. NOMBRE  DE LA LICITACIÓN  
“12803 Módulo RO Segunda Etapa para  Salmuera - PD Taltal ”. 
 
2. PROPOSITO  Y ALCANCE  
 
Las presentes Bases Administrativas Especiales (en adelante también “BAE”), establecen 
las disposiciones aplicables al proceso de Licitación y al posterior Contrato de Suministro 
de Módulo RO segunda etapa para salmuera - PD Taltal , para Aguas de Antofagasta S.A. 
(en adelante indistintamente ADASA , el Comprador  o el Comprador ), en el marco del 
proyecto de tratamiento de salmuera desde la infraestructura existente  (en adelante 
indistintamente el “Proyecto”).  
 
En dicho contexto, el presente instrumento contiene las definiciones, condiciones y demás 
cláusulas que regirán las relaciones de ADASA con los participantes de la Licitación 
(Licitantes) y con el eventual Licitante Adjudicado , en adelante, el Proveedor . 
 
 
3. DESCRIPCIÓN  Y ALCANCE  GENERAL  DEL PROYECTO  
ADASA es una sociedad anónima cerrada regida por las normas de las sociedades 
anónimas abiertas, e inscrita en el Registro de Entidades Informantes y en el Registro de 
Emisores de Valores de Oferta Pública de la Comisión para el Mercado Financiero, y 
sometida a su fiscalización, con objeto único y exclusivo de prestación de servicios 
sanitarios,  que adquirió  de la Empresa  de Servicios  Sanitarios  de Antofagasta  S.A.,  hoy 
denominada  Econssa  Chile  S.A.,  el derecho  de explotación  de las concesiones  sanitarias  de 
los servicios públicos sanitarios de producción y distribución de agua potable, y de 
recolección y disposición de aguas servidas que esta última posee en la Región de 
Antofagasta, excluida la concesión de disposición de aguas servidas de las ciudades de 

---

### Pagina 6
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
6/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Calama y Antofagasta.  
 
Como titular del derecho de explotación de las concesiones sanitarias de producción y 
distribución  de agua  potable  para el consumo  humano  en la ciudad  de Antofagasta,  ADASA 
requiere aumentar la capacidad de producción de agua potable para el consumo humano, 
para lo que proyecta implementar el Proyecto “ Módulo  RO Segunda Etapa para Salmuera  - 
PD Taltal ”. 
 
Se requiere  contar  con una empresa  proveedora  de Suministro  de planta modular, como 
integrador global del encargo . La licitación abarca Suministro  y Servicio  de Asistencia, de 
acuerdo  con las Especificaciones  Técnicas  P22-ET-09-000-001-0. 
 
Para el proyecto se requiere la compra e instalación de una planta modular de 2 0 m3/hora 
de producción de permeado en la localidad de Taltal con el objetivo de aumentar la 
producción de agua desalinizada para satisfacer el aumento de demanda del suministro en 
períodos estivales. La nueva planta toma la salmuera de rechazo del módulo RO N°3 
existente y la trata nuevamente con el fin de producir permeado adicional , sin aumentar la 
cantidad de agua bruta que se deba extraer desde los pozos de captación.  
 
4. LEY APLICABLE  
El Contrato y su ejecución se regirán por la Ley Chilena. En este sentido, la expresión “ley” 
incluye cualquier ley, decreto ley, decretos, reglamentos, resoluciones u otras normas 
emanadas de la autoridad gubernamental central, regional o municipal y demás que 
correspondan  al ordenamiento  jurídico  institucional  de la República  de Chile.  El adjudicatario 
deberá cumplir con la ley vigente a la fecha de adjudicación y con todas aquellas que se 
dicten  durante  la vigencia  del Contrato  en lo que a la ejecución  del mismo  se refiere,  siendo 
de su riesgo cualquier cambio en la legislación que afecte el Contrato.  
 
En todo caso, ante cualquier discrepancia en la interpretación de los documentos que 

---

### Pagina 7
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
7/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 conforman el Contrato y la normativa vigente aplicable al mismo, primará lo dispuesto en 
dicha normativa.  
 
5. DOMICILIO  
Para todos los efectos legales, el domicilio especial de ADASA, los Licitantes y las 
posteriores Partes será la ciudad y comuna de Antofagasta de Chile y se someten a la 
jurisdicción de los tribunales ordinarios de justicia  de Chile . 
 
 
6. IDIOMA  OFICIAL  
El idioma oficial será el CASTELLANO  para todo documento de la Licitación y/o integrante 
del Contrato,  así como  los informes  y productos  materia  de los mismos.  En el caso de 
los licitantes extranjeros, y exclusivamente para los documentos requeridos en la oferta 
técnica y antecedentes previos, se admitirá su presentación en idioma Inglés . 
 
 
7. ADMINISTRACIÓN  DEL CONTRATO   
La Administración del Contrato será realizad a por Aguas de Antofagasta S.A., a  través  de 
un Gestor  Administrativo  y a un Administrador de Contrato , quienes  tendrán  a su cargo,  
durante  toda la duración  de la prestación  de los servicios y la vigencia del presente contrato 
(s), el seguimiento técnico, administrativo, financiero, contractual y de control.   
 
La administración podrá nombrar Ayudantes Técnicos como Prevencionistas de Riesgos, 
asesores jurídicos, financieros, de control interno o Inspectores Técnicos, si así  lo estimare 
conveniente, quienes podrán actuar en su representación dejando observaciones del 
desarrollo y cumplimiento del o los contratos.  
 
El Administrador del Contrato por ADASA durante la vigencia de este Contrato será la 
persona que ADASA designe y comunique. Los cambios del Administrador del Contrato por 

---

### Pagina 8
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
8/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 ADASA serán informados al Representante el Proveedor . 
  
El Representante del Proveedor  durante la vigencia de este Contrato será la persona que 
el Proveedor  designe y comunique  formalmente a ADASA . Cualquier cambio del 
Representante del Proveedor  deberá ser comunicado por el Proveedor  y aprobado por 
ADASA formalmente y por escrito.  
 
8. DEFINICIONES  
Los siguientes términos empleados en estas Bases Administrativas Especiales y en los 
restantes documentos que integren el Contrato, tendrán el significado y alcance que a 
continuación se indica:  
 
− Adjudicatario : el Licitante  que se adjudique  el Contrato  y que pasará  a ser el 
Proveedor , Oferente o EPS . 
− EPS: Empresa prestadora de Servicio.  
− Comprador : ADASA  o Aguas de Antofagasta S.A.  
− Día: Significa  días corridos  y completos,  comprendiendo  los días sábado,  domingo  y 
festivos, a menos que se utilice explícitamente una definición distinta.  
− Día Hábil : Cada  día calendario,  excluidos  los sábados , domingos  y festivos.  
− Oferta : Propuesta de los términos técnicos y económicos a través de la cual el 
licitante ofrece en forma irrevocable ejecutar el Pedido.  
− Licitantes u Oferente : Empresas nacionales o extranjeras participantes de la 
presente Licitación.  
− Partes : Se refiere  al Comprador  (ADASA)  y Proveedor.  
− Pedido  o Encargo : Es todo aquello que deberá ser diseñado, edificado, construido, 
proporcionado, suministrado, realizado, instalado, removido, excavado, 
transportado, extraído, procesado, montado o hecho por el Proveedor, de acuerdo 
con las Especificaciones Técnicas y el Contrato.  

---

### Pagina 9
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
9/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 − Proveedor : Adjudicatario de la presente Licitación. Persona  jurídica  que como  
fabricante,  contratista,  almacenista, representante o distribuidor que contrata con el 
Comprador y adquiere la responsabilidad  de entregar  los materiales,  equipos  y/o 
servicios  objeto  del Contrato en las condiciones pactadas.  
− Suministro : Materiales  y equipos,  así como el  conjunto  de actividades incluyendo 
la mano de obra directa e indirecta, equipos, organización, instalaciones 
temporales, servicios, etc. necesario para la ejecución completa del Pedido.  
 
II. DE LA LICITACIÓN  
9. LLAMADO  DE LICITACIÓN  
Sólo podrán participar en este proceso, Empresas Jurídicas nacionales o 
internacionales  que sean fabricantes  o representantes  oficiales  del fabricante  o 
integradores  del Pedido  en licitación  (en adelante también nombrados indistintamente 
como el Licitante , Proveedor , EPS u Oferente , según corresponda), y que cumplan a 
satisfacción con las exigencias establecidas en las presentes Bases  Administrativas 
Especiales, Bases técnicas, especificaciones técnicas, hojas de datos y Circulares 
Aclaratorias emitidas por ADASA  durante la Licitación, si las hubiere . 
 
Las Empresas deberán  cumplir con las siguientes condiciones  de participación :   
 
a) Acreditar, mediante certificados otorgados por los Comprador es o documentos 
tales como Órdenes de Compra, Contratos o Facturas , la experiencia relevante y 
comprobable  en la elaboración, venta, integración y/o puesta en marcha de 
sistemas de desalinización por ósmosis inversa, demostrando capacidad técnica 
y experiencia combinada  en los siguientes ámbitos clave (la cual puede ser 
evidenciada a través de uno o más proyectos de referencia ): 
 

---

### Pagina 10
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
10/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 i. Suministro  de al menos  5 (cinco)  plantas desaladoras modulares o 
contenerizadas para desalinización de agua de mar , con capacidad 
individual igual o superior a 480 m³/h. Las cuales deben encontrarse 
actualmente en operación.  
ii. Suministro  de al menos un a Planta Modular que incorpore tecnología de 
segunda etapa de Ósmosis Inversa y/o tratamiento/recuperación de 
salmuera/concentrado de OI , preferentemente utilizando membranas de 
alta o ultra -alta presión  (UHPRO) . La cual debe n encontrarse actualmente 
en operación.  
 
La documentación presentada deberá permitir a ADASA evaluar 
satisfactoriamente la idoneidad técnica del licitante para el alcance específico de 
este proyecto.  
 
Esta experiencia se acreditará mediante documentos que especificados en la 
cláusula 15 de las presentes bases. certificados otorgados por los Comprador es 
correspondientes o mediante documentos contractuales.  
 
b) Acrediten certificación ISO 9001  para el sistema de gestión del fabricante  de 
plantas modulares RO  a ofertar . 
c) Para las EPS Nacionales, Certificado de la Tesorería sin observaciones, otorgado 
por la Tesorería General de la República de Chile.  Para EPS Internacionales 
Certificado sin observaciones otorgado por el Departamento, ente fiscal, según 
corresponda al País de la EPS Oferente.  
d) Empresas y sus socios que no tengan obligaciones impagas con Aguas de 
Antofagasta S.A., sean estas de cualquier naturaleza, civiles, comerciales, 
laborales, contractuales o extracontractuales, etc.  
e) No haber recibido una inhabilitación expresa por parte de Aguas de Antofagasta 
S.A.,  para participar  en procesos  de Licitación  y que esta se encuentre  vigente  a 
la fecha.   

---

### Pagina 11
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
11/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 f) Evaluación desempeño de proveedores. (solo si aplica).  
g) Realizar debida diligencia a todas las EPS que están en etapa de habilitación. 
(Compliance).  
h) Haberse inscrito y haber bajado las bases en el periodo indicado en el programa 
de licitación de las BAE.  
 
10. TIPO DE LICITACIÓN , TIPO DE CONTRATO , REAJUSTE.  
La modalidad  de licitaci ón es PUBLICA  y el tipo de Contrato  “A SUMA  ALZADA ”. 
Para esta licitación no se considera ningún tipo de Reajuste.  
 
11. DOCUMENTOS  QUE  CONFORMAN  LAS BASES  DE 
LICITACIÓN  
Los documentos  que conforman las Bases de Licitación, con el objeto de  que los Licitantes 
preparen y presenten su Oferta son:  
 
a) Las Circulares  Aclaratorias  emitidas  por ADASA  (si las hubiere) . 
b) Las presentes  Bases  Administrativas  Especiales  (BAE).  
c) Las Especificaciones  Técnicas  (ET) del módulo  P22-ET-09-000-001-0. 
d) Bases Administrativas Generales (BAG) para contratos de servicios.  
e) Ensayos  técnicos  del suministro  (si los hubiere) . 
f) Oferta Económica de la EPS y cualquier otro documento técnico que forme parte de ésta.  
g) Bases Administrativas Generales, Seguridad y Salud Ocupacional para Empresas 
Colaboradoras y sus respectivos anexos.  
h) Programa Seguridad y Salud Ocupacional Empresas Colaboradoras de Aguas de 
Antofagasta S.A. (PSEC).  
i) Programa Ambiental de Empresas Prestadora De Servicios GPC -DMA -PL-007. 

---

### Pagina 12
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
12/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 j) Ley 16.744 que establece el seguro social contra riesgos de accidentes de trabajo y 
enfermedades profesionales, por lo tanto, deberá estar adherido a un organismo 
administrador establecido por Ley.  
k) Ley 20.123 que regula trabajo en régimen de subcontratación, el funcionamiento de las 
empresas de servicios transitorios y el contrato de trabajo de servicios transitorios.  
l) Bases para inscripción en el Registro de Empresas Prestadoras de Servicios de Aguas de 
Antofagasta S.A. (Rubro Servicios Generales).  
m) Ley 20.393: que establece la Responsabilidad penal de las personas jurídicas.  
n) Políticas de DD.HH. ADASA  
o) Código de Conducta Ética para Contratistas y Proveedores (CCEPS).  
p) Manual de Prevención del delito de Aguas de Antofagasta S.A.  
q) Todas las Normas Chilenas Oficiales relacionadas (INN).  
r) Políticas de Evaluación Económica, Garantías de Contratos y pagos por compras, servicios 
y contratos de Aguas de Antofagasta S.A.  
s) Manual de Identidad Corporativa de Aguas de Antofagasta S.A.  
t) Reglamento de Prevención de Riesgos para las Empresas Contratistas de Aguas de 
Antofagasta S.A.  
u) Anexo 7: Protocolo para EE.CC. (Plan contingencia en relación con el riesgo de contagio de 
coronavirus COVID -19). 
 
En caso  de existir  discrepancias,  prevalecerán  en el orden  señalado.  
 
Estos  documentos  serán  descargados  por los postulantes  mediante  la plataforma  Web de 
licitaciones de Aguas de Antofagasta  
http://www.aguasantofagasta.cl/idempiere/licitaciones/  todo de acuerdo con el  punto 13 
programa de la licitación.  

---

### Pagina 13
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
13/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 12. DOCUMENTOS  INTEGRANTES  DEL CONTRATO  Y SU 
ORDEN DE PRELACIÓN  
En el Contrato  quedarán  señalados  los documentos  que forman  parte  integrante  del mismo. 
En caso de que  dicho documento no los señale  o en el caso de existir discrepancias, se 
entenderán que son los siguientes y en el orden de prelación que se indica a continuación.  
 
a) El Contrato   
b) Las modificaciones al Contrato . 
c) La Carta  de Adjudicación  y Notificación  
d) Las Circulares Aclaratorias emitidas por ADASA, con precedencia de acuerdo con  su 
fecha de emisión . 
e) Las Bases  Administrativas  Especiales  (BAE) . 
f) Las Especificaciones  Técnicas  (ET), Bases técnicas (BT) , Hojas de datos (HD)  y/o 
Términos  de referencia (TR) . 
g) La Oferta  Técnica  del Licitante.  
h) La Oferta  Económica  del Licitante.  
  

---

### Pagina 14
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
14/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
13. PROGRAMA  DE LA LICITACIÓN . (Hora de Chile) . 
 
 
Actividad  Fecha  
Desde  Hasta  
Visita a Terreno  NO APLICA  
Reunión Aclaratoria Virtual  NO APLICA  
Inscripción y bajada de Bases  (vía sistema de licitaciones)  
Obligatoria.  Hasta las  23:00 horas del 15 -06-2025  11-06-2025  15-06-2025  
Recepcion  de correo para oferentes internacionales, solicitando 
código interno, hasta las 12:00 horas del 13 -06-2025  11-06-2025  13-06-2025  
Ronda Consultas 1  12-06-2025  16-06-2025  
Respuestas Ronda 1  17-06-2025  19-06-2025  
Ronda Consultas 2  21-06-2025  26-06-2025  
Respuestas Ronda 2  27-06-2025  01-07-2025  
Entrega Antecedentes Previos  hasta las 23:00 horas   11-07-2025  
Habilitación de Oferentes   17-07-2025  
Recepción de Ofertas Técnicas,  hasta las 10:30   22-07-2025  
Apertura de Ofertas Técnicas,  a las 11:00 horas    22-07-2025  
Notificación Evaluación Técnica  a las 18:00 horas    29-07-2025  
Recepción Boleta de Garantía Seriedad de la Oferta  14:00 horas    05-08-2025  
Recepción de Ofertas Económicas 14:30 horas  
(Sistema licitaciones)   05-08-2025  
Apertura de Ofertas  Económicas  15:00 horas  
(Vía plataforma Teams )  05-08-2025  
Notificación de Adjudicación      25-08-2025  
 
Aguas  de Antofagasta  S.A.,  podrá  modificar  las fechas  del Programa  de Licitación,  mediante 
un Documento de Aclaratoria. En tal caso, todos los derechos y obligaciones de Aguas de 
Antofagasta S.A.,  y de los Licitantes se entenderán prorrogados conforme a las nuevas 
fechas que se estipulen.  
14. CONSULTAS Y ACLARACIONES SOBRE LAS BASES DE 
LICITACIÓN  

---

### Pagina 15
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
15/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Los Licitantes  podrán  hacer  consultas  o solicitar  aclaraciones  sobre  las Bases  de Licitación, 
mediante correo electrónico dirigido a licitacion2@aguasantofagasta.cl . De acuerdo con el  
programa de licitación.  
 
Tanto, las respuestas a las consultas formuladas por los Licitantes, como las aclaraciones, 
rectificaciones, enmiendas o adiciones que ADASA estime necesario hacer a las Bases de 
Licitación,  serán  incluidas  en comunicaciones  denominadas  Circulares  Aclaratorias,  dirigidas 
a todos los Licitantes.  
 
15. ANTECEDENTES  PREVIOS  
El proponente deberá adjuntar los Antecedentes  con tal que permitan evaluar su 
continuidad en el proceso de Licitación sólo hasta la fecha y horarios establecidos en el 
Programa de la Licitación. Estos antecedentes serán los siguientes y se deben adjuntar en 
la plataforma Web de licitaciones de Aguas de Antofagasta 
http://www.aguasantofagasta.cl/idempiere/licitaciones/  
 
Estos  antecedentes  serán  los siguientes:  
 
Licitación  Pública  ANTECEDENTES  PREVIOS:  “12803 Módulo RO Segunda Etapa 
para Salmuera - PD Taltal”  
 
15.1.  ANTECEDENTES  COMERCIALES,  FINANCIEROS  Y 
LABORALES  
 
a) Estado  Financiero  a Diciembre - 2024 bajo normativa  NIIF auditado  (IFRS  Financial  
Statements with Audit Report), para proveedores Internacionales. Este 
documento debe adjuntarlo  en la casilla  de la plataforma  “Estado  de resultado  y 
cartera  de clientes”.   

---

### Pagina 16
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
16/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 b) Balance de 8 columnas al 31 de diciembre del año 2023  (auditado o certificado) con 
firma y timbre de representante legal y contador.  Proveedores nacionales.  Cargar en 
PDF en la casilla correspondiente . 
c) Balance clasificado con su respectivo Estado de Resultado al 31 de diciembre del 
año 2023 (Auditado y certificado), con firma y timbre representante Legal y Contador.  
Proveedores nacionales. Cargar en PDF en la casilla correspondiente . 
d) Declaración  renta  Año Tributario 2025.  Para proveedores nacionales.  
e) Certificado  de DICOM,  para proveedores  Nacionales.  
f)    Para las EPS Nacionales, Certificado de la Tesorería sin observaciones, 
otorgado por la Tesorería General de la República de Chile.  Para EPS 
Internacionales Certificado sin observaciones otorgado por el Departamento, 
ente fiscal, según corresponda al País de la EPS Oferente.  
g) Declaración  de IVA de los últimos  6 meses,  para proveedores  Nacionales.  
h) Certificado de la Inspección del Trabajo F -30 Cumplimiento de obligaciones 
laborales y previsionales, para proveedores Nacionales.  
 
15.2.  ANTECEDENTES  DE EXPERIENCIA  Y RECURSOS  
 
a) Listado de servicios ejecutados debidamente  firmado por el representante legal, 
SÓLO  DE LA ESPECIALIDAD  REQUERIDA  SEGÚN  EXIGENCIA  EN EL 
PUNTO 9 LLAM ADO A LICITACION  DE LAS PRESENTES BAE.  La omisión 
de esta información, o la entrega deficiente, que no permita validar la 
experiencia del proponente,  podrá  determinar  su eliminación  del proceso  de 
licitación  sin derecho a indemnización de ningún tipo. Para este ítem se deberá 
utilizar el formato adjunto a las presentes bases “ AC10EXP OBRAS O 
SERVICIOS EJECUTADOS ”. 
 

---

### Pagina 17
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
17/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 b) Listado de obras, servicios y/o suministros EN EJECUCIÓN y/o 
RECIENTEMENTE ADJUDICADAS , debidamente firmado por el representante 
legal (independiente de la naturaleza que sean o el estatus en que se 
encuentren), con indicación de montos y avances financieros a la fecha, relación 
de contratos vigentes con Aguas de Antofagasta S.A. o cualquier otra institución 
pública o privada. Para este ítem se deberá utilizar el formato adjunto a las 
presentes bases “AC10OEJ OBRAS, SERVICIOS, SUMINISTROS EN 
EJECUCIÓN (EN CURSO)” . La omisión de cualquier obra de reciente 
adjudicación o que esté ejecutando el proponente  podrá  determinar  su 
eliminación  del proceso  de licitación  sin derecho a indemnización de ningún tipo.  
c) Contratos , Órdenes  de Compra  o certificados otorgados por los Comprador es 
correspondientes que acrediten  servicios ejecutados (Ver punto a).  
d) Certificaciones ISO 9001. Adjuntar documentos en la casilla de la plataforma 
“contrato que acrediten ”. 
 
15.3.  ANTECEDENTES  GENERALES Y LEGALES DEL 
PROVEEDOR . 
 
a) Copia de la escritura pública de constitución de la Empresa y sus modificaciones. 
Para proveedores nacionales y Documento que lo reemplace para proveedores 
internacionales.  
b) Publicaciones en el Diario Oficial.  Para el caso de las Empresas por un 1 día, debe 
estar protocolizado a través de notaria con firma electrónica simple.  Para 
proveedores nacionales y Documento que lo reemplace para proveedores 
internacionales.  
c) Certificado de Inscripción con vigencia del Registro de Comercio que  corresponda,  
emitido  en un plazo  no superior  en los últimos  3 meses.  Para proveedores nacionales 
y Documento que lo reemplace para proveedores internacionales.  
d) Certificado de Vigencia de Sociedad del Registro de Comercio, emitido en un plazo 
no superior en los últimos 3 meses. Para proveedores nacionales y Documento que 
lo reemplace para proveedores internacionales.  

---

### Pagina 18
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
18/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 e) e) Certificado de Vigencia de Poder del Registro de Comercio, emitido en un plazo no 
superior en los últimos 3 meses. Para proveedores nacionales y Documento que lo 
reemplace para proveedores internacionales.  
 
Estos documentos se deben adjuntar en la plataforma de licitaciones de Aguas de 
Antofagasta S.A. ( http://www.aguasantofagasta.cl/idempiere/licitaciones/ ), solo hasta el 
horario indicado en el Programa de la presente Licitación. En caso de no presentar en su 
totalidad los antecedentes , el PROVEEDOR quedará inhabilitada automáticamente para 
presentar oferta.  
 
La omisión  de esta información,  o la entrega  deficiente,  que no permita  validar  la experiencia 
del proponente  u otra información solicitada , podr ía determinar la NO HABILITACIÓN para 
la continuidad en el proceso de la licitación sin derecho a indemnización de ningún tipo.  
 
Los antecedentes se deberán adjuntar en el formato solicitado  en plataforma de 
licitaciones  de Aguas Antofagasta , generalmente PDF. tamaño máximo 5 MB o en Excel 
versión 5.0  / 97 / 2010 con extensión ( XLS). 
 
Para efectos de respaldo de presentación de Antecedentes  de la EPS, el sistema de 
licitaciones  de Aguas de Antofagasta , una vez subidos todos los antecedentes 
solicitados, permite la emisión de un certificado de antecedentes Previos 
presentados,  el cual la EPS deberá tener a su resguardo como comprobante de 
presentación de los antecedentes.  
 
Las empresas  participantes se  obligan  a cumplir  con los requisitos,  forma  y entrega  de toda 
la documentación  requerida.  Toda  información  falsa,  errónea,  con omisión,  entrega  fuera  de 
plazo, será de absoluta y total responsabilidad de la empresa oferente.  Esta será 
inhabilita da para continuar en el presente proceso de licitación.  
 
Sin perjuicio  de que las empresas  participantes  cumplan  con la documentación  requerida  en 

---

### Pagina 19
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
19/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 este artículo, Aguas de Antofagasta S.A. se reserva el derecho de:  
 
a) Solicitar  aclaraciones  o complementos  de los Antecedentes  entregados,  a todas las 
empresas o en forma particular. Para responder de esta solicitud, la(s) empresa(s) 
participante(s) dispondrá(n) hasta de un plazo máximo de 48 hrs. para presentar los 
referidos  antecedentes  (sean  éstos  mediante  documentación  física  o digital  enviada  por 
correo electrónico) en las oficinas del Departamento Cadena de Suministros de Aguas 
de Antofagasta  S.A. ó a través  de la casilla  licitacion2@aguasantofagasta.cl  según  sea 
el caso.  
b) Eliminar, en  esta etapa del  proceso  de licitación,  a cualquiera de  los participantes en  el 
caso que, a juicio de Aguas de Antofagasta S.A., existan antecedentes que puedan 
afectar sus intereses por cualquiera de las causales señaladas en el Artículo 16. 
c) De anular  o postergar  el proceso  en esta etapa,  en el caso  de existir  la concurrencia  de 
un solo participante.  
 
Como el Sistema de Licitaciones de Aguas Antofagasta es un sistema estándar, puede que 
solicite subir más antecedentes previos de los solicitados en el punto 15 Antecedentes Previos 
de la presente  BAE, para este caso, se debe adjuntar un archivo en formato  libre, que indique 
NO APLICA PARA ESTA LICITACIÓN.   
 
En caso de generarse problemas con las cargas de documentos en la plataforma, podrá 
comunicarse a la siguiente dirección electrónica licitacion2@aguasantofagasta.cl , señalando 
detalles del problema.  
 
En caso de que el oferente no present e los antecedentes previos en plataforma de licitaciones 
dentro del plazo indicado en el programa de licitación  de la presente  BAE, la EPS quedará 
inhabilitada automáticamente para continuar en el proceso de licitación.  
 
 

---

### Pagina 20
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
20/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 16. HABILITACIÓN  
 
Para  esta licitación,  solamente  las empresas  que habiendo  cumplido  con la entrega  de los 
Antecedentes  Previos  y cumplido  cabalmente  con los requisitos  solicitados en las presentes 
bases, podrán ser declaradas como “Participantes Habilitados” para  presentar  ofertas,  de 
acuerdo  con resultado  de su evaluación.  
 
La nómina de Participantes Habilitados no  será de conocimiento público y su conocimiento 
será reservado a ADASA.  
 
Con todo, ADASA se reserva el derecho de HABILITAR o NO HABILITAR a las empresas 
que, habiendo cumplido con la entrega de los Antecedentes , a su juicio existan 
antecedentes que afecten en todo o parte sus intereses, no siendo esta enumeración 
taxativa, y sólo a modo ilustrativo tales como:  
 
a) Juicios, demandas, querellas, denuncias u otras acciones legales interpuestas por 
la EPS, en contra de Aguas de Antofagasta S.A., o interpuestas por Aguas de 
Antofagasta S.A., en contra de la EPS, y/o en contra de sus representantes 
legales o relacionados, terminados o vigentes. Juicios, demandas o acciones 
legales con entidades de gobierno, empresas privadas o terceros y que 
comprometan en parte o todo el patrimonio de la empresa proponente.  
b) Juicios, demandas, querellas, denuncias u otras acciones legales con entidades 
públicas, empresas privadas o terceros y que impliquen situaciones graves, como 
delitos, falta de probidad o vulneración de garantías constitucionales, que 
comprometan en parte o todo el patrimonio de la empresa proponente, y/o la 
imagen de Aguas de Antofagasta S.A., y/o de sus socios o representantes.  
c) Acciones  legales  o juicios  por incumplimientos  laborales  o previsionales.  
d) Se incluyen también aquellas consideraciones, notas de demérito o calificaciones 
deficientes que la empresa pueda haber obtenido en su ejecución de contratos o 

---

### Pagina 21
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
21/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 servicios con cualquier entidad pública o privada.  
e) Empresas que habiendo pertenecido al Registro de Empresas Prestadores de 
Servicios  de ADASA  hayan  sido suspendidas,  sancionadas  o eliminadas  del mismo 
a razón  de incumplimientos  definidos  en las Bases  del Registro,  Contratos  de Obras 
o Servicios y que hayan incurrido en alguno de los aspectos señalados en los 
literales anteriores.  
f) Comportamiento deficiente o incumplimientos graves en contratos de obras o 
servicios vigentes con ADASA, realizados en los últimos 3 años.  
g) Falta de probidad, falseamiento u ocultamiento de información  que no permita una 
objetiva  evaluación  del estatus  del proponente  con motivo  de su participación  en la 
presente licitación.  
h) Insolvencia  económica  o quiebra.  
i) Haber recibido  una inhabilitación  expresa  por parte  de ADASA  para participar  en 
procesos de Licitación y que esta se encuentre vigente a la fecha.  
j) Cuando la EPS haya incurrido en manifiestas negligencia o indebida 
administración, durante la ejecución de algún contrato con Aguas de Antofagasta. 
S.A.  
k) Indicadores  asociados  a temas  de seguridad  y salud  ocupacional,  con valores  que, 
a juicio  de ADASA,  demuestren  una acción  ineficiente  que no propicie  la seguridad 
y salud de las personas.  
 
 
17. PRESENTACIÓN  DE LAS OFERTAS  
Para la preparación de las Ofertas, los Licitantes serán responsables estudiar todos los 
documentos entregados por ADASA y de recabar toda la información complementaria 
necesaria  de forma  de lograr  un completo  y acabado  conocimiento  de las características  del 
suministro , sus dificultades, normativas aplicables, permisos exigidos y costos asociados. 
En virtud de lo anterior, el Proveedor no podrá aducir ignorancia, desconocimiento o falta 
de información acerca de las condiciones necesarias para confeccionar adecuadamente su 

---

### Pagina 22
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
22/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Oferta.  
La obligación  de presentar  las ofertas  con los antecedentes  que se indican  a continuación    . se 
entenderá cumplida con la entrega de copias autorizadas de los documentos, con  
certificación de vigencia no superior a 30 días anteriores a la fecha establecida para la  
entrega de  las ofertas.  
Las ofertas deberán ser íntegras, considerando todos los componentes solicitados por 
Aguas  de Antofagasta, en las bases técnicas, hoja de datos y/o aclaraci ones . Las ofertas 
que omitan alguno de los componentes solicitados no serán  tomadas  en consideración  en 
la evaluación  final.  
No se aceptará la presentación de ningún otro formato distinto de presentación de oferta 
económica del proporcionado por Aguas de Antofagasta S.A.  
 
De esta manera,  al presentar  su Oferta  cada  Licitante  declara  y acepta:  
 
 
• Que será el  único  responsable  de la interpretación  y comprobación  de la documentación 
entregada por ADASA, no siendo esta última responsable de ningún error, inexactitud, 
suficiencia  u omisión  de cualquier  naturaleza  en los documentos  entregados  por ADASA.  
• Que ha obtenido toda la información necesaria y suficiente relacionada a los riesgos, 
contingencias y otras circunstancias que puedan influir o afectar el Pedido.  
• Que todas las aprehensiones, incertidumbres, vacíos y ambigüedades fueron suficiente 
y favorablemente aclaradas.  
• La responsabilidad total de haber previsto cualquier dificultad y costo en la correcta 
ejecución y terminación del Contrato.  
• Que el precio ofertado cubrirá todas las obligaciones del Proveedor y cualquier otra 
necesaria para la ejecución y terminación adecuada del Contrato y reparación de 
cualquier defecto.  
• Que el precio  ofertado  no se ajustará  debido  a dificultades  o costos  imprevistos,  e incluye 
todos  los estudios,  diseños,  evaluaciones  y verificaciones  que considere  necesarios  para 
formular la Oferta.  
• Que la obligación del Proveedor es una obligación de resultado, no una  mera obligación 

---

### Pagina 23
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
23/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 de medios.  
 
Lo anteriormente  señalado  prevalecerá  por sobre  lo indicado  en cualquier  otro documento.  
 
18. COSTO  DE LA OFERTA.  
Serán de cargo de cada Licitante todos los costos directos e indirectos asociados a la 
preparación y presentación de su Oferta, no siendo ADASA, en ningún caso, responsable 
de estos costos.  
 
19. MONEDA  DE LA OFERTA  
Los valores  monetarios  señalados  en los documentos  que forman  parte  de la Oferta  deberán 
venir expresados en dólares de los Estados Unidos de América.   
 
 
20. ENTREGA  DE OFERTAS  TÉCNICAS  
La obligación de presentar las ofertas con los antecedentes que se indican a continuación 
se entenderá cumplida con la entrega digital de los documentos al correo 
licitacion2@aguasantofagasta.cl  sólo hasta la fecha y horarios establecidos en el Programa 
de la Licitación. La empresa oferente deberá verificar que el medio digital que se adjunta 
en la plataforma de licitaciones sea legible y contenga todos y cada uno de los documentos 
solicitados para esta propuesta. Estos antecedentes serán los siguientes:  
 
20.1.  DOCUMENTOS  OFERTA TÉCNICA  
 
En la oferta técnica se deberá incluir todos los requerimientos definidos en las Especificaciones 
Técnicas  P22-ET-09-000-001-0: 
 

---

### Pagina 24
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
24/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
Documento  1: Descripción técnica de " Módulo RO Segunda Etapa para Salmuera  - 
PD Taltal”, de acuerdo con lo solicitado en la Sección 6 de las 
Especificaciones Técnicas (P22 -ET-09-000-001-0). Este documento 
deberá indicar la oferta técnica general, plazos de entrega, listados de 
repuestos y la demás información detallada requerida en ET Sec. 6 . 
 
 
Documento  2: Plan de ejecución de actividades  de comisionamiento y puesta en 
marcha . Este plan debe incluir como mínimo:  
• Identificación del  personal propuesto  para liderar  las actividades 
de Comisionamiento y Puesta en Marcha , con sus respectivos 
currículums vitae (CVs) . Se validará lo establecido en sección 9 
de las Especificaciones Técnicas.    
• Cronograma preliminar para asegurar el cumplimiento exitoso 
de la puesta en marcha, las pruebas de desempeño en sitio 
(PIE Item 11.5) y la posterior obtención de la Recepción 
Provisional (PIE Item 12.3) .  
• Detalle de recursos  y dotación de especialistas a utilizar .  
 
Documento  3: Declaración de Consumo Específico de Energía Eléctrica 
Garantizado (CEE Garantizado) . Documento oficial, firmado por el 
Representante Legal del Oferente, donde se declare explícitamente el 
valor del Consumo Específico de Energía Eléctrica (expresado en 
kWh/m³) que el Oferente garantiza para la planta modular, conforme a 
los requerimientos y rangos de TDS establecidos en la Sección 10.1.3 
de la Especificación Técnica (P22 -ET-09-000-001-0). Este valor será 
utilizado en la evaluación económica de la oferta (se gún Cláusula 24.4) 
y será exigible durante las Pruebas de Desempeño . 
  
ADASA  se reserva  el derecho  de solicitar  aclaraciones , correc ciones  o complementos  de los 
antecedentes o  documentación  entregada.  Para  responder  esta solicitud,  el Licitante  
dispondrá  de un plazo máximo de 72 hrs. hábiles. Para presentar los referidos 
antecedentes.  
 

---

### Pagina 25
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
25/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 21. ENTREGA  DE OFERTAS  ECONÓMICAS  
La obligación de presentar las ofertas con los antecedentes que se indican a continuación 
se entenderá cumplida con la entrega digital de los documentos en la plataforma de 
licitaciones de ADASA  http://www.aguasantofagasta.cl/idempiere/licitaciones/,  sólo hasta 
la fecha y horarios establecidos en el Programa de la Licitación. La empresa oferente 
deberá verificar que el medio digital que se adjunta en la plataforma de licitaciones sea 
legible y contenga todos y cada uno de los documentos solicitados para esta propuesta. 
Estos antecedentes serán los siguientes:  
 
21.1.  DOCUMENTOS  QUE  SE DEBEN  INCLUIR  EN LAS OFERTAS.  
 
PROPUESTA ECONÓMICA (Sobre 1)  
 
Documento  1: Formulario de Cotización de Oferta  Economica , según formato 
adjunto , señalando el monto total Suma Alzada ( Valor Exw y Valor  
DDP ) de su oferta base, debidamente firmado por el representante 
legal . En PDF. 
 
Documento  2: Declaración  Jurada  1 de la oferta  según  formato  adjunto.  No se 
aceptará otro archivo distinto y éste NO DEBERÁ ser modificado. Se 
deberá cumplir  estrictamente  la entrega  firmada  tanto  de la oferta  
como  de la Declaración Jurada en formato (PDF), esta última bajo 
poder notarial para proveedores Nacionales y para proveedores 
Internacionales debidamente firmada por el representante legal . 
Documento  3: Presupuesto por partidas o itemizado ( en archivo  PDF y EXCEL), 
según formulario adjunt o. Los valores de las partidas a subir al 
sistema de licitación corresponderán  a su oferta Exw. 
IMPORTANTE: La EPS deberá utilizar sólo el Archivo  
"PRESUPUESTO ITEMIZADO LICITACIÓN", que se entrega con los 
antecedentes de la propuesta, para generar su Oferta. Éste debe venir  
DEBIDAMENTE FIRMADO por el representante legal.  
La presentación de su oferta debe corresponder al 100% de las 
partidas, es decir no se acepará la omisión de ninguna partida.  

---

### Pagina 26
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
26/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 No se aceptará otro archivo distinto y éste  NO DEBERÁ  ser modificado. 
La EPS deberá ingresar los precios unitarios, en este formato de 
presupuesto.  
El documento en formato PDF deberá ser cargado en el portal de 
licitaciones en la casilla “ PRESUPUESTO ITEMIZADO FIRMADO POR 
REPRESENTANTE LEGAL” .   
El documento en formato EXCEL deberá ser cargado en el portal de 
licitaciones en la casilla “Listado detallado de Recursos para la obra ”. 
 
Documento  4: Opcional: “Cotización Repuestos para 2 años", con el detalle de precios 
unitarios y totales para el listado recomendado según ET Sec. 6. ( En 
PDF y xlsx.  Cargar en Casilla:  Formato de Gastos Generale s. 
 
Documento 5  Formulario de Cotización de Oferta  Económica detallada, según 
formato libre de oferente. Cargar en casilla Metodología . 
 
La empresa oferente deberá verificar que el medio digital que se adjunta en la 
plataforma de licitaciones sea legible y contenga todos y cada uno de los 
documentos solicitados para esta propuesta.  
 
DOCUMENTOS ANEXOS (Sobre 2) 
 
Documentos, debidamente firmados y separados según los antecedentes que se 
detallan a continuación: (Cap.  máxima  de cada  uno de los documentos  requeridos  5 
megas):  
Documento  1: Boleta de Garantía  de Seriedad de la Oferta (BAE clausula 23), 
adjuntar en casilla correspondiente.  
Documento 2  Aclaraciones  (si las hubiere) debidamente firmadas por el 
representante legal . adjuntar en casilla correspondiente  
Documento  3: Declaración Jurad a 2, de Toma de conocimiento y conformidad firmada 
por el  representante legal . Según formato adjunto . adjuntar en casilla 
correspondiente.  

---

### Pagina 27
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
27/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Documento  4: Declaración  Jurada 3 , de Conflictos  de Intereses  para Proveedores,  
firmada  por el representante legal . Según formato adjunto . adjuntar en 
casilla correspondiente.  
Documento  5: Declaración Jurada 4 , de confidencialidad,  firmada  por el 
representante  legal . Según formato adjunto . 
Documento  6: DECLARACIÓN JURADA 5  PSEC Seguridad y Salud Ocupacional . Según 
formato adjunto . Cargar la declaración en la casilla de nombre 
declaración jurada N°5 . adjuntar en casilla correspondiente.  
Documento  7: DECLARACIÓN JURADA 7 de Subcontratación , según formato  adjunto 
(.PDF).  Cargar la declaración en la casilla de nombre declaración jurada 
N°7 
Documento  8: DECLARACIÓN JURADA 8 de uso apropiado de Ciberactivos  Según 
formato adjunto . (Cargar excepcionalmente junto con declaración 
jurada 7, en un solo archivo ) 
Documento  9 DECLARACION JURADA 9, Carta de compromiso exponiendo la 
obligación de cumplir con el Programa de Seguridad de  Aguas de 
Antofagasta S.A. Según formato adjunto . (Cargar excepcionalmente 
junto con declaración jurada 7, en un solo archivo ) 
Documento  10 DECLARACIÓN JURADA 10, VÍNCULO CON PERSONAS 
EXPUESTAS POLÍTICAMENTE (PEP ), según formato adjunto.  (Cargar 
excepcionalmente junto con declaración jurada 7, en un solo archivo ) 
Documento  11 DECLARACIÓN JURADA 11, POLITICA DE DD HH ADASA , según 
formato adjunto.  (Cargar excepcionalmente junto con declaración 
jurada 7, en un solo archivo ) 
 
Está prohibido a las EPS, enviar la OFERTA COMERCIAL  (con Valores) al correo 
licitacion2@aguasantofagasta.cl  
 
ADASA  se reserva  el derecho  de solicitar  aclaraciones  o complementos  de los antecedentes 
o documentación  entregada.  Para  responder  esta solicitud,  el Licitante  dispondrá  de un plazo 
máximo de 48 hrs. hábiles. Para presentar los referidos antecedentes.  
 
 
 

---

### Pagina 28
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
28/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 22. VALIDEZ  DE LAS OFERTAS  
Las Ofertas  presentadas  por los Licitantes  deberán  ser válidas  e irrevocables  por un plazo  
de 90 días  desde su recepción. ADASA podrá solicitar la extensión de dicho período.  
23. GARANTÍA  DE SERIEDAD  DE LA OFERTA  
Los Licitantes deberán garantizar la seriedad de su Oferta, entregando en la Oficina de 
Partes de ADASA, Avda. Pedro Aguirre Cerda N° 6496, hasta el horario indicado en el 
Programa  de Licitación,  una Boleta  de Garantía  Bancaria  en favor  de ADASA.  Los Licitantes 
extranjeros  tienen  la posibilidad  alternativa  de reemplazar  la entrega  de la Boleta  de Garantía 
Bancaria de Seriedad de la Oferta emitida a la Vista o una póliza de Segur o de garantía a 
la Vista , siempre que cumpla con los mismos requisitos de dicho documento, que sea 
ejecutable en Chile y que su ejecución  fuere  sustancialmente  equivalente  a la ejecución  de 
una Boleta  Garantía  Bancaria a la vista.  
 
El texto  de la garantía  deberá  ser previamente  sometido  a aprobación  de ADASA.  
 
Estas  garantías deberán ser tomadas por el  Licitante a su costo,  en dólares de los Estados 
Unidos de América, pagaderas a la vista, incondicionales, irrevocables y emitidas por un 
banco nacional con domicilio en Santiago de Chile o un banco extranjero con oficina en 
Chile.  
La vigencia  de la garantía  debe  ser de 180 días a partir de su fecha de emisión  y por 
un monto  de CLP $ 25.000.000 .- (Veinticinco millones de pesos  chilenos ). 
 
La boleta deberá adjuntarse en un sobre cerrado  en la Oficina de Partes de Aguas de 
Antofagasta S.A., Avda. Pedro Aguirre Cerda N° 6496, hasta el horario indicado en el 
Programa de Licitación, con la siguiente leyenda:  
 
Licitación Pública: GARANTIZAR LA SERIEDAD DE LA OFERTA LICITACIÓN 12 803 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA - PD TALTAL  

---

### Pagina 29
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
29/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Razón social empresa postulante 
Correo  electrónico  empresa  postulante  
Nombre y fono de la persona de contacto en la empresa postulante 
Contiene: BOLETA  DE GARANTÍA  POR  SERIEDAD  DE LA OFERTA  
 
Esta boleta deberá adjuntarse en fotocopia e n los Documentos  de la Oferta Económica  y 
en original según programación de licitación. Esta boleta será devuelta  a todos los 
Licitantes una vez presentada la Boleta por Fiel Cumplimiento por parte del  PROVEEDOR 
que se adjudique el contrato , dentro de los 30 días posteriores a dicho hito .  
 
Sin perjuicio de lo indicado en el párrafo anterior, queda establecido que la omisión de la 
boleta  de garantía  por Seriedad  de la Oferta  o equivalente  para empresas  extranjeras 
constituirá  un impedimento  para abrir la oferta  económica  del proponente . Así mismo si 
existe algún error de emisión de la Boleta de Garantía o Carta de Garantía.  
 
Queda  establecido  que las Boletas  de Garantías  que requieran  ser enviadas  a alguna  región 
del país, Aguas de Antofagasta S.A. se exime de cualquier tipo de carga, gravamen, 
obligación  o responsabilidad  derivada  del envío  y/o extravío  de la BG solicitada.  En caso  de 
extraviarse  y aparecer  el documento,  Aguas  de Antofagasta  S.A.,  se exime  de cualquier  tipo 
de responsabilidad relativa a su devolución u otros similares, ante el tomador, el banco 
emisor, y/o cualquier tercero.  
 
Por lo anterior, la PROVEEDOR que requiera solicitar dicho documento, debe completar el 
formulario que se adjunta para ser enviado por ADASA a otra región de Chile o caso 
contrario, el PROVEEDOR debe solicitar y retirar en forma presencial en las instalaciones 
de Aguas Antofagasta. Este formulario debe ser llenado a mano y firmado por el 
representante legal, el cual debe entregarse en la presentación de ofertas (ya sean éstas 
solicitadas  digitales,  por correo  o plataforma,  o físicas,  según  cada  Licitación)  establecido  en 
el artículo 17, 20 y 21  de las presente BAE, o  en un  sobre  cerrado en la  Oficina de  Partes  
de Aguas de  Antofagasta  S.A.,  Avda.  Pedro  Aguirre  Cerda  N° 6496,  según  sea el caso.  No 

---

### Pagina 30
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
30/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 se aceptará la presentación de ningún otro documento o formato distinto.  
 
Aguas Antofagasta S.A. verificará y revisará que el formulario de solicitud esté 
confeccionado  correctamente  y que todos  los campos  estén  completos.  Si la documentación 
presentada está incompleta, será causal de rechazo, quedando sin acción.  
 
Cumpliendo con toda información, Aguas Antofagasta tendrá un plazo  adicional  de 10 días 
hábiles para la devolución del documento . 
 
La garantía será devuelta al Licitante Adjudicatario una vez presentada la Garantía de Fiel 
Cumplimiento de Contrato. En dicho sentido, se deberá mantener siempre vigente la 
Garantía de Seriedad de la Oferta hasta que sea sustituida por la Garantía de Fiel 
Cumplimiento de Contrato.  Mientras no opere dicha sustitución, ADASA podrá hacer 
efectiva total o parcialmente, la Garantía de Seriedad de la Oferta en los casos de 
incumplimiento de las obligaciones del Licitante y/o Proveedor, en su caso.  
 
24. DERECHO A DEJAR SIN EFECTO LICITACIÓN Y OTROS. 
APERTURA, EVALUACIÓN, ADJUDICACIÓN Y 
CELEBRACION DEL CONTRATO.  
ADASA se reserva el derecho a desestimar todas las Ofertas, dejar sin efecto, declarar 
desierta o terminada la licitación, postergar la licitación, en cualquier momento previo a la 
celebración del Contrato, sin expresión de causa y sin que ello genere obligación de 
compensación alguna a los Licitantes.  
 
24.1.  APERTURA OFERTAS TÉCNICAS  
 
ADASA invita a las Empresas Participantes a participar en la apertura de las Ofertas 
Técnicas, que se realizará el día señalado en el Programa de la Licitación  o en la fecha  
reprogramada  según  corresponda.  Se enviará  por correo  el link para que  se conecten  

---

### Pagina 31
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
31/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 virtualmente,  el PROVEEDOR  debe  confirmar  la participación  por correo  a través de 
licitacion2@aguasantofagasta.cl  y la participación es un representante por empresa.  
 
Se procederá  a la apertura  de documentos  hasta la fecha señalada en el programa de licitación 
y recepcionados al correo licitacion2@aguasantofagasta.cl   
 
24.2.  EVALUACIÓN DE OFERTAS TÉCNICAS .  
 
Las ofertas  serán  declaradas  técnicamente  aceptables  si cumplen a cabalidad  con los 
aspectos técnicos requeridos en las especificaciones técnicas del presente encargo  
(Dimensionamiento de equipos , Materiales , Diseño de Procesos, Calidad de Agua 
Producto,  Plan de Comisionamiento y Puesta en Marcha y experiencia del personal que 
liderará dichas actividades , entre otros) . Dicha  declaración  constará  en un Acta de 
Evaluación  que será firmada por ADASA.  
Sólo aquellas ofertas técnicamente aceptables podrán participar en las etapas siguientes 
de la Licitación . 
ADASA, podrá requerir de los oferentes, hasta antes de la apertura de las Ofertas 
Económicas, aclaraciones, rectificaciones por errores de  forma u omisiones y  la entrega  de 
antecedentes,  con el objeto  de clarificar  y precisar  el correcto  sentido  y alcance  de la Oferta, 
evitando que alguna sea descalificada por aspectos formales en su evaluación técnica, y 
velando siempre por los principios de transparencia del proceso y de igualdad de los 
Licitantes.  
 
ADASA podrá prescindir de antecedentes que, aun cuando no hubieren sido presentados 
por algún Licitante, no resulten relevantes para la evaluación de la idoneidad jurídico - 
financiera -técnica para la suscripción del Contrato y no afecten la adecuada inteligencia de 
la Oferta  presentada.  Asimismo,  durante  la evaluación  de las ofertas,  ADASA  podrá  solicitar 
los antecedentes complementarios que estime necesarios a efectos de una adecuada 
evaluación de las Ofertas.  

---

### Pagina 32
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
32/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
A los Licitantes que se les soliciten aclaraciones, modificaciones o información adicional 
deberán presentarla el día, hora, lugar y condiciones que se señale en la comunicación 
escrita correspondiente de ADASA.  
 
24.3.  APERTURA DE OFERTAS ECONÓMICAS . 
 
ADASA  invita  a las Empresas  Participantes  a participar en la apertura de las Ofertas 
Económicas, que se realizará el día señalado en el Programa de  la Licitación  o en la fecha  
reprogramada  según  corresponda.  Se enviará  por correo  el link para que se conecten 
virtualmente, el PROVEEDOR debe confirmar la participación por correo a través de 
licitacion2@aguasantofagasta.cl   y la participación es un representante por empresa.  
 
Queda establecido que la no presentación de la Garantía de Seriedad de la Oferta en la 
fecha y horario definido en el programa de licitación o cualquier error u omisión en la 
conformación de ésta de acuerdo a lo exigido en estas Bases podría ser motivo para 
declararla inadmisible y constituirá un impedimento para abrir la oferta económica del 
proponente dejando constancia de dicha situación en el Acta de Apertura.  
ADASA  dará a conocer  el resultado  de la evaluación  de las Ofertas  Técnicas,  y procederá  a 
abrir la Oferta Económica de los Licitantes cuyas ofertas fueron declaradas técnicamente 
aceptables. La apertura de los documentos se hará desde la plataforma de Licitaciones de 
ADASA.  
 
La Oferta Económica de los Licitantes cuyas ofertas no fueron aceptadas en la etapa de 
evaluación técnica, serán bajados de la plataforma, sin abrir, dejándose constancia de ello 
en el acta correspondiente.  
 
Tras el  término  de la apertura, se  procederá  a levantar un  acta en que se dejará constancia 
de quienes presentaron Ofertas, de los antecedentes recibidos y las demás circunstancias 
que se estimen necesarias, la que será suscrita por todos los asistentes.  

---

### Pagina 33
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
33/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
Las Ofertas Económicas que no presenten todos los antecedentes requeridos en las 
presentes Bases de Licitación o en su defecto que presenten enmiendas, tachaduras o 
condicionamientos  serán  rechazados  en el acto,  dejándose  constancia  de ello en el acta de 
apertura.  
 
No se aceptará, bajo ninguna circunstancia, que los Licitantes entreguen 
antecedentes faltantes o canjeen o rectifiquen los rechazados.  
 
24.4.  EVALUACIÓN  DE LA OFERTA  ECONÓMICA.  
 
La evaluación económica (EEC) de la oferta de cada proveedor se realizará en pesos 
chilenos (CLP), considerando tanto la inversión inicial como el impacto del consumo 
energético proyectado durante un período definido, según la siguiente fórmula:  
 
EEC= P0+(Costo_Energ ia_Eval×Produccion_Anual_Eval×N_A ños_Eval)⋅CEp 
 
Donde los términos se definen como:  
• EEC:  Resultado de la Evaluación Económica total, expresado en  Dólares 
Estadounidenses . Se adjudicará al oferente con el menor valor de EEC que cumpla 
con todos los requisitos.  
• P0: Monto  ofertad o por el Proveedor  en Formulario de Cotización de la Oferta . En 
Dólares Estadounidenses.   
• Costo_Energıa_Eval:  Costo unitario promedio de la energía eléctrica considerado 
por ADASA para esta evaluación, definido en 0,1 USD /kWh.  
• Produccion_Anual_Eval:  Producción anual de permeado considerada como base 
para la evaluación del costo energético, establecida en 175.200  m³/año 
(equivalente a 480 m³/día  * 365 días/año, consistente con lo indicado en Cláusula 
43.2.c). 
• N_Años_Eval:  Período (en años) durante el cual se proyecta el costo energético 

---

### Pagina 34
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
34/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 para la evaluación, establecido en 3 años (consistente con el período usado para el 
cálculo de multas por CEE en Cláusula 43.2.c). 
• CEp: Consumo específico de energía declarado por el  proveedor  en Documento 3 
de Oferta Técnica , expresado en kWh/m³, correspondiente a la garantía ofrecida 
para la condición de operación con TDS en el rango 48.000 – 53.000 mg/L, según 
lo requerido en la ET Cláusula 10.1.3 . 
 
Una vez evaluadas las propuestas, Aguas de Antofagasta S.A. podrá reservarse el  derecho 
de: 
a) Desechar todas las propuestas o aceptar cualquiera de ellas sin necesidad de expresión 
de causa.  
b) Descalificar las ofertas que contengan omisiones, exclusiones o condicionantes que se 
aparten de lo establecido en las presentes bases de licitación.  
c) Requerir las aclaraciones, respaldos, certificados y antecedentes complementarios que 
estime necesarios para realizar la evaluación. Con todo, estas aclaraciones no podrán 
alterar el monto de la propuesta económica ofertada.  
d) Descalificar las ofertas que, habiendo sido requeridas según el punto anterior, no 
presentan la respuesta al requerimiento en el plazo definido para ello.  
e) Requerir documentos actualizados, previo a la adjudicación de un contrato, para 
verificar la capacidad económica, financiera y cumplimiento de leyes laborales por parte 
del proponente.  
f) Solicitar una reconsideración de ofertas a todos y sin excepción de ningún proponente 
que haya presentado ofertas y dejado registro de dicho acontecimiento en acta de 
apertura de ofertas del proceso.  
 
Aguas de Antofagasta S.A. no aceptará de los oferentes  envío de regalos u obsequios, 
tendientes a influir en la resolución de la propuesta, lo que en cualquier caso podrá dar 
motivo para la descalificación de la empresa oferente.  
 
24.5.  ADJUDICACIÓN DEL CONTRATO  
 

---

### Pagina 35
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
35/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 La adjudicación de las propuestas es derecho exclusivo de ADASA, de acuerdo con  sus 
propios procedimientos de evaluación, incluido los plazos para que ello  ocurra, así como la 
disposición de firmas para autorizar la adjudicación. Por lo anterior, la fecha establecida en 
el Programa de la Licitación tendrá sólo carácter de referencial.  
 
El criterio que considerará Aguas de Antofagasta S.A. para decidir la adjudicación será el 
siguiente: Se adjudicará el Contrato a la empresa que obtenga el menor valor de 
Evaluación Económica  (EEC), siempre que no existan motivos para inhabilitar dicha oferta 
en virtud de los requisitos establecidos en estas Bases.  
 
Para el caso de existir dos o más Ofertas Económicas cuya diferencia de Evaluación  
Económica (EEC)  sea menor a un  5% respecto a la Oferta con menor valor  de Evaluación  
Económica (EEC) , se considerará un empate técnico las Ofertas, pudiendo ADASA adjudicar la 
Licitación a la Oferta que estime conveniente . 
 
Así, cualquiera sea el resultado de la Licitación, no existirá ninguna indemnización ni 
compensación para los proponentes, sea por reembolso de gastos u otro concepto 
relacionado con el costo del estudio y presentación de la propuesta, así como tampoco 
existirá devolución de documentos, a excepción de la Garantía de Seriedad de la Oferta.  
 
Dentro del periodo de validez de las Ofertas, ADASA comunicará por escrito la 
adjudicación del Contrato mediante la correspondiente Carta de Adjudicación.  
 
24.6.  SUSCRIPCIÓN DEL CONTRATO  
 
El Contrato  deberá  suscribirse  según  el formato  que se adjunta como Anexo N°6 a las 
presentes Bases Administrativas, en tres ejemplares dentro del plazo máximo de 15 días 
hábiles contados desde la fecha en que se notifique la adjudicación, quedando dos 
ejemplares en poder de ADASA y uno del Proveedor. Será de responsabilidad del Licitante 
Adjudicado suscribir el documento en que conste el Contrato.  

---

### Pagina 36
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
36/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
Si el Licitante  adjudicado  no suscribiere  el Contrato  dentro  del plazo  antes  señalado,  ADASA 
podrá  dejar  sin efecto  la adjudicación  mediante  una notificación  por parte  de ADASA.  Como 
consecuencia el Licitante perderá a favor de ADASA, la Garantía de Seriedad de la Oferta. 
En este caso, ADASA podrá adjudicar el Contrato a otro de los Licitantes.  
 
Sin perjuicio de la Fecha de firma del contrato, el Plazo Contractual se establece de acuerdo a 
lo señalado en la Cl áusula 27 de las presentes base . 
 
III. CONDICIONES  DE EJECUCIÓN  DEL CONTRATO  
25. MODALIDAD  Y PRECIO  DEL CONTRATO  
El Pedido  se contratará  bajo la modalidad  a “SUMA  ALZADA”.  
 
El Precio incluye la provisión de los Materiales y Equipos necesarios para la ejecución del 
Encargo, las  herramientas, energía eléctrica, fletes, el valor de la mano de obra, con sus 
cotizaciones e imposiciones  de seguridad social, leyes sociales, impuestos (incluido el Impuesto 
al Valor Agregado, “IVA”), gastos  generales, utilidades, subcontratos y cualquier otro gasto 
necesario para la correcta y total ejecución del  Pedido . 
El Contrato está afecto a IVA, el que será de cargo de ADASA, por lo cual el Proveedor  lo 
deberá detallar  separadamente en las facturas que emita. Todos los demás impuestos que por 
cualquier causa graven o  sean originados por el Contrato, serán de exclusivo cargo del 
Proveedor  y estarán incluidos en el Precio.  En caso de modificaciones de las leyes tributarias 
que afecten al Contrato, el impacto de estas  modificaciones será asumido por el Proveedor , a 
excepción del IVA.  
Se considerará que el precio del Contrato es correcto y suficiente, cubriendo todas las 
obligaciones del  Proveedor , cualquier otra cosa necesaria para la ejecución y terminación 
adecuada del Encargo, la  reparación de cualquier defecto y las utilidades del Proveedor . 
 
ADASA no admitirá reclamación alguna del Proveedor en relación con el alcance, 

---

### Pagina 37
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
37/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 condiciones y requisitos de cualquier naturaleza incluidos en el Pedido o Encargo.  
 
ADASA  no admitirá  modificación  de los precios  indicados  en el Pedido,  salvo  que haya  sido 
ordenada una modificación al Pedido cuyo precio haya sido autorizado por escrito por el 
ADASA.  
 
Cualquier gasto que ADASA se vea obligado a realizar por incumplimiento del Proveedor 
será repercutido a este.  
 
26. ALCANCE  Y DESARROLLO  DEL PEDIDO  
Cualquier  incidencia  o circunstancia  que pudiera  surgir  durante  la ejecución  del Pedido,  que 
deba  solucionarse  con la participación  de ADASA  o que pueda  afectar  de forma  desfavorable 
a la fabricación, montaje o garantías del Pedido, deberá ser puesta en conocimiento al 
Comprador por escrito y sin dilación alguna por parte del Proveedor.  
 
El Proveedor se obliga a ejecutar las modificaciones del Pedido con suministros o trabajos 
adicionales que eventualmente pueda encomendarle a ADASA mediante revisiones de 
Pedido, en las que se definirá el alcance de dichas modificaciones y/o trabajos adicionales 
en la misma  forma que en el pedido inicial, así como su repercusión en precio y/o plazo de 
entrega  cuando  proceda.  La obligación  de ejecutar  será inmediata,  aunque  no exista  acuerdo 
de las Partes sobre las posibles repercusiones de las modificaciones ordenadas, 
comprometiéndose en este caso las Partes a negociar las citadas repercusiones de buena 
fe. 
 
27. PLAZO S DE EJECUCIÓN DEL PEDIDO  
El Plazo  de Entrega  para el módulo RO de segunda etapa para salmuera , en las condiciones 
descritas en las Bases de Licitación,  será de máximo 300 días corridos  contados desde  la 
emisión de la Notificación de Adjudicación por parte de ADASA.  

---

### Pagina 38
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
38/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 El Plazo de Entrega será firme y constituye una condición esencial para el cumplimiento del 
Contrato. La entrega cabal y correcta de la documentación requerida también se considera 
a efectos de cumplimiento de plazos.  
 
No se admitirán modificaciones en dicho plazo, a menos que el Comprador lo acepte 
expresamente por escrito mediante la correspondiente revisión del Pedido.  
 
Si se produjesen retrasos imputables al Proveedor, este deberá poner los medios a su 
alcance para recuperar los mencionados retrasos, a su costa y sin cargo alguno para el 
Comprador.  
 
El Plazo Contractual  se extenderá desde la Notificación de Adjudicación por parte de 
ADASA hasta la obtención por parte del Proveedor de la Recepción Provisional del Pedido , y 
no deberá superar los 510 días corridos . 
 
Dentro de los 180 días corridos posteriores  a la recepción por parte del Comprador del módulo 
RO de segunda etapa para salmuera , el Comprador convocará al Proveedor para que ejecute las 
labores de Comisionamiento y Puesta en Marcha . La convocatoria se realizará con al menos 30 
días de anticipación respecto de la fecha en la cual debe apersonarse el Proveedor en el Sitio  (En 
Planta Desaladora Taltal, Chile) , de acuerdo a las condiciones y dotación de personal que indica en 
la sección 9 de las Especificaciones técnicas P22-ET-09-000-001. 
   
El Proveedor tendrá un máximo de 21 días corridos  para Completar el Alcance del Pedido 
correspondiente al Comisionamiento y Puesta en Marcha  del módulo RO de segunda etapa para 
salmuera , en las condiciones que se especifican en la sección 9 de las Especificaciones técnicas 
P22-ET-09-000-001. Una vez completadas dichas actividades, el Proveedor tendrá un máximo de 
30 días corridos  para presentar toda la documentación y cerrar todos los requisitos establecidos 
para la Recepción Provisional del Pedido .  
 
28. GARANTÍAS  TÉCNICAS  DEL PEDIDO  

---

### Pagina 39
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
39/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 El Proveedor garantiza a la empresa ADASA que la totalidad de los equipos y sus 
componentes, suministrados por él y/o sus proveedores y subcontratistas, están libres de 
defectos  o fallos  de diseño,  de materiales,  de mano  de obra,  de fabricación  o funcionamiento 
que pudieran surgir bajo uso normal, que se han fabricado de conformidad con las 
especificaciones,  muestras,  planos,  normas  y demás  documentos  técnicos  aplicables  y que 
dichos equipos y sus  componentes son nuevos, de primera calidad y adecuados para el  fin 
a que se destinan. Los vicios ocultos estarán cubiertos por dicha garantía. El Proveedor 
garantiza el diseño de su suministro, para una vida operativa esperada de veint icinco  (25) 
años, teniendo en cuenta el  mantenimiento periódico del mismo y una correcta operación y 
mantenimiento según los manuales proporcionados para tales efectos por el Proveedor.  
 
Las garantías  de funcionamiento  se determinarán  en las Especificaciones  Técnicas  P22-ET-
09-000-001-0, en su punto 10.  
 
El Proveedor  garantiza  además  que los equipos  suministrados  están  libres  de gravámenes, 
cargas y reclamaciones  de titularidad en  favor de terceros, debiendo eximir e indemnizar al 
Comprador  de cualquier  gasto,  carga  o gravamen  que resulte  de la falta de cumplimiento  de 
sus obligaciones contractuales con los subcontratistas, empleados, agentes o cualquier 
persona con quien haya contraído compromiso.  
 
El período de la presente garantía técnica y de desempeño, que cubre todos los aspectos 
definidos en esta cláusula, incluyendo la conformidad con las especificaciones, la ausencia 
de defectos (de diseño, materiales, mano de obra, fabricación o funcionamiento bajo uso 
normal) y el cumplimiento de los parámetros de desempeño garantizados según las 
Especificaciones Técnicas P22 -ET-09-000-001-0 (Punto 10), comenzará a regir única y 
exclusivamente a partir de la fecha de emisión del Acta de Recepción Provisional del 
Pedido por parte de ADASA, según se define en la Cláusula 41 de estas BAE.  
 
Dicho período de garantía tendrá una duración total e ininterrumpida (salvo suspensiones 
por reparaciones según se indica más adelante) de veinticuatro (24) meses corridos, 

---

### Pagina 40
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
40/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 contados desde la mencionada fecha de Recepción Provisional.  
 
Se establece explícitamente que la fecha de puesta a disposición de la mercancía bajo la 
modalidad de entrega EXW (Cláusula 33) o cualquier otra fecha anterior a la Recepción 
Provisional, no constituirá el inicio del período de esta garantía técnica y de desempeño. 
Esta garantía estará a disposición del Comprador en su total extensión y términos durante 
los veinticuatro (24) meses siguientes a la Recepción Provisional.  
 
Durante el período de garantía el Proveedor, a su cargo y dentro de los quince (15) días 
siguientes  a la fecha en  que el Comprador  le hubiera comunicado los  defectos  observados, 
procederá  a reponer  o corregir  cualquier  defecto  de diseño,  de materiales,  de mano  de obra, 
de fabricación y de funcionamiento (incluyendo todo el trabajo de desmontaje, compra y 
reinstalación  que pudiera  ser necesario).  Una vez subsanados  los defectos  por el Proveedor, 
se aplicará la misma garantía indicada en el párrafo anterior a aquellas partes reparadas o 
reemplazadas, con validez hasta veinticuatro (24) meses a partir de la última fecha en que 
tales reparaciones fueran satisfactoriamente realizadas. El plazo de garantía del equipo se 
suspenderá hasta que sea repuesta o reparada la parte averiada.  
 
Si el equipo,  tras las modificaciones  y/o reparaciones  requeridas  realizadas  por el Proveedor, 
no cumpliera  todavía  con las características  requeridas,  deberá  ser totalmente  reemplazado 
por otro nuevo que el Proveedor entregará en el lugar indicado por el Comprador, libre de 
todo gasto, en el menor plazo posible y sujeto a las condiciones del Pedido.  
 
En el caso de no efectuar en un plazo fijado de común acuerdo las reposiciones o 
correcciones necesarias, o si ello no fuese posible para el Proveedor por razones de 
capacidad técnica o de cualquier otra índole, el Comprador se  reserva el  derecho de poder 
optar  por efectuar  por sí mismo  o mediante  la contratación  de un tercero  las reposiciones  y/o 
correcciones necesarias, repercutiendo el Comprador al Proveedor todos los gastos 
soportados  por dichos  conceptos  como  consecuencia  de las reparaciones  o reposiciones  así 
efectuadas.  

---

### Pagina 41
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
41/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
Cuando se efectúen reparaciones, modificaciones y/o sustituciones de equipos, si las 
mismas han sido realizadas para cumplir con los valores garantizados a cuenta del 
Proveedor, los plazos de garantía comenzarán a contar a partir de la puesta en servicio 
satisfactoria del equipo.  
 
No excusarán al Proveedor de las obligaciones de la garantía cualquier revisión de planos, 
inspección de equipos o participación de los representantes del Comprador en las 
discusiones  con el Proveedor  y/o sub-proveedores  o subcontratistas  de éste.  Ni la aceptación 
de los equipos  por parte  del Comprador,  ni el pago  de cualquier  factura,  eximirá  al Proveedor 
de las responsabilidades por él contraídas al aceptar el Pedido.  
 
29. BOLETAS  DE GARANTÍAS  
 
 
29.1  BOLETA DE GARANTÍA BANCARIA POR ENTREGA DE 
ANTICIPO.  
 
 
El Proveedor podrá solicitar un Anticipo según lo estipulado en la Cláusula 32, como 
requisito previo a la liberación del pago de  dicho anticipo , el Proveedor deberá presentar 
una Boleta de Garantía Bancaria a la vista  o su alternativa para Proveedor Extranjero que 
cumpla con las siguientes especificaciones:  
 
• A favor de: “AGUAS DE ANTOFAGASTA S.A.”.  
• RUT: 76.418.976 -0 
• Glosa:  Para garantizar el correcto uso y amortización del anticipo otorgado según 
contrato para la Licitación Pública “MÓDULO RO SEGUNDA ETAPA PARA  
SALMUERA - PD TALTAL”.  
• Monto:  Equivalente al cien por ciento (100%) del valor del anticipo otorgado 
(máximo  el 25% del monto total neto del Contrato u Orden de Compra).  
• Vigencia:  La boleta deberá mantenerse vigente hasta el término del Plazo 

---

### Pagina 42
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
42/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Contractual o hasta la amortización total del anticipo, lo que ocurra primero. El 
Proveedor estará obligado a prorrogar esta garantía si fuese necesario para 
mantenerla vigente hasta se cumplan los hitos antes mencionados.  
• Condiciones:  Pagadera a la vista, incondicional, irrevocable y emitida por un banco 
según las condiciones generales estipuladas en la sección "Normas comunes a las 
Boletas Bancarias de Garantía" de esta cláusula . 
 
29.2  BOLETA DE GARANTÍA BANCARIA POR FIEL 
CUMPLIMIENTO DEL CONTRATO  
 
El Proveedor  deberá  presentar  una Boleta de Garantía Bancaria a la vista  o su alternativa 
para Proveedor Extranjero , según las siguientes especificaciones:  
 
A favor  de: “AGUAS  DE ANTOFAGASTA  S.A.”. 
RUT: 76.418.976 -0 
Glosa:  garantizar el fiel cumplimiento de los parámetros solicitados en las BAE y garantías 
según Especificaciones Técnicas, de Licitación Pública “12803  MÓDULO RO SEGUNDA 
ETAPA PARA  SALMUERA - PD TALTAL”  
Monto:  15% del monto  total  neto  del Contrato  u Orden  de Compra.  
 
Vigencia:  La boleta deberá tener vigencia durante todo el Plazo Contractual aumentado en 
180 días corridos. El Proveedor será responsable de mantener la vigencia de las boletas 
durante toda la duración del Contrato, debiendo reemplazarlas toda vez que el plazo de 
esta se extienda. El no cumplimiento de lo anterior dará lugar al inmediato cobro de la 
boleta por parte de ADASA.  
Además, esta Boleta cubrirá la obligación que pudiera corresponder al Proveedor por 
incumplimientos con motivo de la prestación del contrato u orden de compra.  
 
Además, esta Boleta cubrirá la obligación que pudiera corresponder al Proveedor por 
incumplimientos con motivo de la prestación del contrato u orden de compra.  
 

---

### Pagina 43
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
43/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Esta Boleta será Devuelta al Proveedor una vez que se complete la Recepción Provisional 
del Pedido y haga entrega de la Boleta de Garantía Técnico o de Desempeño del Equipo.  
 
29.3  BOLETA DE GARANTÍA BANCARIA POR GARANTÍA TÉCNICA 
O DE DESEMPEÑO DEL EQUIPO.  
 
 
Como condición para el otorgamiento de la Recepción Provisional, el Proveedor deberá 
presentar  una Boleta  de Garantía  Bancaria  a la Vista o su alternativa para Proveedor 
Extranjero , para asegurar  al Comprador  la calidad  técnica  y de funcionamiento del 
suministro, conforme a lo descrito en la cláusula 31.  
 
Esta Boleta de Garantía Bancaria deberá tener vigencia desde su fecha de emisión (como 
condición para la Recepción Provisional) y deberá mantenerse válida hasta la fecha de 
emisión del Acta de Recepción Definitiva  del Pedido, la cual se otorgará una vez 
transcurrido satisfactoriamente el período de garantía técnica estipulado en la Cláusula  28. 
El importe  de esta Boleta  de Garantía  Bancaria  será de un diez por ciento  (10%)  del Monto 
Total Neto del Contrato u Orden de Compra.  
 
La Boleta de Garantía Bancaria por Garantía Técnica o de Desempeño del Equipo deberá 
asegurar el cumplimiento de los parámetros de desempeño especificados en la Sección 
10.1 de la Especificación Técnica P22-ET-09-000-001-0, incluyendo, pero no limitado a, la 
Capacidad Nominal detallada en el punto 10.1.1 y la Calidad del Agua Producto a 
Garantizar según el punto 10.1.2. El cumplimiento de estas garantías se verificará 
mediante las Pruebas de Desempeño descritas en la Sección 10.2 de la misma 
Especificación Técnica, específicamente la Prueba de la Capacidad Nominal de 
Producción y las Pruebas de calidad del agua producto . 
 
El cobro total o parcial de la Boleta de Garantía Bancaria por Garantía Técnica o de 
Desempeño del Equipo podrá ser efectuado por ADASA , sin perjuicio de la aplicación 

---

### Pagina 44
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
44/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 de multas según Cláusula 43.2 u otras acciones contractuales o legales a las que tenga 
derecho, en caso de que el Proveedor no cumpla con los Parámetros de Desempeño 
Garantizados especificados en la Especificación Técnica (ET Sec. 10.1) , verificados 
mediante las Pruebas de Desempeño en Sitio (ET Sec. 10.2) , o no subsane dicho 
incumplimiento a satisfacción de ADASA en el plazo que se determine . Dicha 
ejecución podrá cubrir, entre otros, el monto de las multas aplicadas bajo la Cláusula 43.2 y 
la compensación por los perjuicios derivados de la operación con desempeño inferior al 
garantizado, incluyendo costos energéticos adicionales, menor producción de agua, etc.  
 
29.4  NORMAS COMUNES A LAS BOLETAS BANCARIAS DE 
GARANTÍA  
 
 
Entrega de Garantías Post -Adjudicación:  Salvo instrucción escrita contraria por parte de 
ADASA, el Proveedor deberá presentar los documentos originales físicos de las Boletas de 
Garantía Bancaria requeridas en las cláusulas 29.1, 29.2 y 29.3 precedentes, en la Oficina 
de Partes de ADASA ubicada en Avda. Pedro Aguirre Cerda N° 6496, Antofagasta, dentro 
de los plazos estipulados para cada una. La entrega deberá realizarse en sobre cerrado, 
dirigido al Administrador del Contrato designado por ADASA, indicando claramente el 
nombre de la licitación y el tipo de garantía que contiene.  
 
El Proveedor deberá proceder a la prórroga de cualquiera de las Boletas de Garantía 
Bancaria citadas en esta cláusula en caso de que existieran obligaciones garantizadas por 
dichos instrumentos que estuvieran pendientes de cumplimiento o respecto de las que 
existiera cualquier tipo de controversia en cuanto a su correcto cumplimiento. Si dicha 
prorroga no se produjera ante de los 15 días anteriores a la finalización de su periodo de 
vigencia, el Comprador podrá ejecutar los mismos, sin perjuicio de su derecho a resolver o 
terminar anticipadamente el Contrato  
 
A su vez, en caso  de que cualquieras  de las Boletas  de Garantía  Bancaria  citadas  no 
fueran presentada dentro del plazo prescrito, el Comprador tendrá derecho a resolver o 

---

### Pagina 45
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
45/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 terminar anticipada y automáticamente el Contrato, sin que requiera su previa notificación 
al Proveedor, y pudiendo hacer efectiva la Boleta Bancaria de Garantía que estuviere en su 
poder.  
 
Todas las Boletas de Garantías Bancarias a cargo del Proveedor, incluyendo la Boleta de 
Garantía  de Seriedad  de la Oferta,  deberán  ser pagaderas  a la vista,  emitidas  por entidades 
bancarias de reconocida solvencia y presencia en Chile, siendo los costos y gastos 
originados por su emisión de cuenta del Proveedor.  
 
29.5 ALTERNATIVA PARA PROVEEDOR EXTRANJERO  
 
 
Los Proveedores  Extranjeros  tienen  la posibilidad  alternativa  de reemplazar  la entrega  de la 
Boletas de Garantías Bancarias antes indicadas por Carta s de Crédito para proveedores 
internacionales, cuyo banco emisor tenga sucursal en Chile, o por Pólizas de Seguro 
de Garant ía, siempre  que aquellas  cumplan  con los mismos  requisitos  de las Boletas  de 
Garantías  Bancarias, que sean ejecutables en Chile y que su ejecución fuere 
sustancialmente equivalente a la ejecución de una Boleta Garantía Bancaria a la vista.  
 
29.6 POLIZAS DE SEGURO PARA CUBRIR GARANTIAS.  
 
Este proceso licitatorio considera la posibilidad de reemplazar la Boleta de Garantía de 
Fiel Cumplimiento y correcta Ejecución del Contrato.  
Para ello, el oferente deberá solicitar el reemplazo de la o las Boletas de Garantía por 
Pólizas de Seguros, Aguas de Antofagasta S.A. solo se admite el reemplazo por Pólizas 
obtenidas a través de la gestión de la empresa Corredora de Seguros MARSH S.A. 
única empresa aprobada por Aguas Antofagasta S.A. para tal efecto.  
El correo de consulta o solicitud deberá ser dirigido a licitacion2@aguasantofagasta.cl 
quien indicará el proceder y entregará los contactos referidos.  
a) El oferente deberá tomar contacto con MARSH S.A. quienes le solicitarán un conjunto de 
documentos para la evaluación financiera y de riesgo a través de tres Compañías 

---

### Pagina 46
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
46/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Aseguradoras quienes prepararán la oferta de póliza para el oferente.  
b) La evaluación y respuesta tarda aproximadamente 3 a 7 días hábiles por lo que el oferente 
deberá tomar la decisión una vez recepcionada la o las cotizaciones respectivas.  
c) Una vez que el oferente cuente con la o las pólizas respectivas, deberá enterarla en Aguas 
Antofagasta S.A. en los mismos plazos establecidos en las presentes BAE, los cuales no 
pueden ser modificados por este motivo.  
 
30. SEGUROS,  ACCIDENTES  E INDEMNIZACIONES  
 
El Proveedor será responsable del daño o pérdida de los bienes, equipos y materiales 
objeto del Pedido hasta el momento en que los ponga a disposición de ADASA en el 
lugar de entrega convenido (sus instalaciones), conforme a la regla Incoterms® 2020 
EXW.  El Proveedor deberá mantener asegurados los bienes objeto del Pedido contra todo 
riesgo hasta dicho momento de puesta a disposición.  
Será responsabilidad exclusiva de ADASA contratar y mantener vigente, a su costo, 
el seguro de transporte de los materiales y equipos que cubra todos los riesgos 
asociados desde el momento en que el Proveedor pone la mercancía a su 
disposición en el lugar convenido (EXW), incluyendo la carga, el transporte principal, 
la descarga en el sitio del Proyecto y los almacenamientos intermedios.  
Nota Clasificatoria  sobre Seguros bajo EXW : Se reitera y clarifica que, en estricta 
conformidad con la regla EXW Incoterms® 2020 acordada, la responsabilidad de contratar 
y mantener la cobertura de seguro adecuada para la mercancía, que cubra todos los 
riesgos asociados al transporte (incluyendo, pero no limitado a, daños durante la carga si 
es realizada por ADASA o su transportista, transporte principal marítimo/terrestre, 
almacenamientos intermedios, descarga en sitio, etc.), recae exclusivamente en ADASA 
desde el instante en que el Proveedor notifica y pone efectivamente la mercancía a 
disposición en el lugar convenido (instalaciones del Proveedor). El seguro del Proveedor 
cesa su cobertura en ese preciso momento.  

---

### Pagina 47
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
47/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 El Proveedor exonerará, defenderá e indemnizará al Comprador de las reclamaciones por 
perdidas, gastos y perjuicios que puedan derivarse de daños a la propiedad y daños 
personales o muerte, tanto de sus empleados como de terceros, que sean ocasionados 
directa o indirectamente como consecuencia de la ejecución de los trabajos objeto del 
Pedido bajo su responsabilidad . 
El Proveedor deberá contratar a sus expensas las correspondientes pólizas de seguro para 
cubrir sus propias responsabilidades, incluyendo, pero no limitándose a:  
• Seguro de vida y accidentes de su personal conforme a la legislación aplicable.  
• Seguro de Automóviles frente a Terceros, que cubra los daños ocasionados 
por los vehículos utilizados por el Proveedor.  
• Cualesquiera otras que se requieran para la adecuada cobertura de las 
responsabilidades contraídas por el Proveedor en virtud del Contrato y que no 
correspondan a ADASA según la regla EXW.  
 
El Proveedor deberá  entregar, si  es solicitado por ADASA, prueba  certificada  de las pólizas 
contratadas.  
 
Si el Proveedor, bien directamente o por medio de alguno de sus agentes o empleados, 
hubiese  de entrar  en la zona  de trabajo  de ADASA  con cualquier  fin, formalizará  previamente 
los seguros oportunos, deberá comprometerse a utilizar, proveer y tomar las precauciones, 
salvaguardias  y protecciones  adecuadas,  necesarias  y suficientes  contra  accidentes  y daños 
personales o materiales que puedan afectar a cualquier persona y propiedad, durante el 
proceso del trabajo objeto del Pedido, e indemnizará y eximirá al Comprador y a sus 
representantes de toda pérdida o responsabilidad económica que se deriven directa o 
indirectamente  de los accidentes  que puedan  ocurrir  por actos  u omisiones  del Proveedor  o 
de sus empleados, agentes y subcontratistas.  
 
El Proveedor mantendrá al Comprador al margen de cualquier reclamación por parte de 

---

### Pagina 48
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
48/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 terceros, relacionado directa o indirectamente con el Pedido. Si en cualquier momento se 
probara  la existencia  de alguna  reclamación  imputable  al Proveedor  que pudiera  afectar  los 
intereses de ADASA, este tendrá derecho a resarcirse o ser compensado  por el Proveedor 
en el importe equivalente a la reclamación.  
 
En el caso de que el Proveedor incorpore en los equipos que ha de suministrar, material o 
equipo que el Comprador le facilite directa o indirectamente, el Proveedor será totalmente 
responsable de cualquier pérdida o daño que pueda producirse en dicho material o equipo 
hasta  que pase  a poder  del Comprador  o de cualquier  persona  autorizada  por el Comprador 
a recibir los equipos.  
 
El Comprador no será responsable en ningún momento ante el Proveedor por pérdidas de 
beneficios, lucro cesante, daño emergente o por ningún otro daño resultante, directo o 
indirecto, previsto o imprevisto o especial, que pudiera derivarse como consecuencia del 
cumplimiento del Pedido.  
El Comprador podrá exigir al Proveedor la indemnización por los daños y perjuicios que se 
le produzcan, excluyéndose el lucro cesante y/o daños indirectos y consecuenciales, salvo 
si se derivaran de dolo o culpa grave del Proveedor.  
 
El Proveedor será, asimismo, responsable del costeo de cuantos encargos haga el 
Comprador  a terceros  en aquellos  supuestos  en que el Proveedor  no cumpla  oportunamente 
con sus obligaciones contractuales.  
 
El Comprador podrá ejecutar las garantías bancarias que le entregue el Proveedor, o bien 
compensar con las cantidades que adeude el primero al segundo, para resarcirse de 
aquellas cantidades que deba abonar como consecuencia de lo previsto en los apartados 
anteriores.  
 
El Proveedor se obliga a contestar, efectuando todos los trámites oportunos con la mayor 
diligencia, todas las reclamaciones que pudieran derivar en las responsabilidades aquí 

---

### Pagina 49
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
49/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 previstas. Asimismo, interpondrá cuantas acciones sean precisas en defensa de las 
responsabilidades que se le pudieran reclamar.  
 
El Comprador colaborará, en la medida de lo posible, en la interposición y tramitación de 
tales reclamaciones, pudiendo incluso participar en la defensa de sus intereses a costa del 
Proveedor.  
31. FACTURACIÓN  Y CONDICIONES  DE PAGO  
 
El pago del precio del suministro y asistencia del Pedido se efectuará mediante cinco  (5) 
Estados de Pago según el avance del Pedido.  
 
• Estado de Pago por Aprobación de Ingeniería (1 0% del Precio): Este pago se 
devengará una vez que ADASA haya revisado y aprobado formalmente por escrito 
la totalidad de la documentación de ingeniería de detalle requerida en la Sección 7 
de la Especificación Técnica (P22 -ET-09-000-001-0), y emitida la comunicación 
correspondiente indicando dicha aprobación sin comentarios pendientes o con la 
resolución satisfactoria de los mismos. El Proveedor está obligado a presentar dicha 
documentación dentro del plazo estipulado de 90 días desde la notificación de 
adjudicación . Se entiende que la aprobación formal por parte de ADASA se emitirá 
tras su revisión, para la cual dispone de 7 días hábiles según lo indicado en la ET 
(Sec. 7), contados desde la recepción conforme de la documentación completa. El 
Proveedor podrá presentar el Estado de Pago correspondiente dentro de los 
primeros 3 días hábiles siguientes a la recepción de la notificación de aprobación 
formal por parte de ADASA.  
 
• Estado de Pago  Contra  OC de Equipos Principales  (15% del Precio):  Este pago 
se devengará una vez que se cumplan acumulativamente las siguientes 
condiciones:  
a) ADASA haya emitido la aprobación formal por escrito de la totalidad de la 
documentación de ingeniería de detalle (cumplimiento del primer hito de 

---

### Pagina 50
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
50/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 pago).  
b) El Proveedor haya presentado a ADASA copias de las Órdenes de Compra 
(OCs) confirmadas y aceptadas por los sub -proveedores para todos los 
equipos principales listados en esta cláusula : Bomba Alta Presión, Sistema 
Recuperación Energía, Filtros Cartucho, Tubos Presión, Membranas OI, 
Sistema Dosificación, Sistema CIP.  
 
El Proveedor podrá presentar el Estado de Pago correspondiente dentro de los 
primeros 3 días hábiles siguientes a la notificación formal por parte de ADASA de 
haber verificado el cumplimiento de todas estas condiciones (a, b y c)."  
 
• Estado de Pago  Pruebas FAT  (40% del Precio):  Lo presentará el Proveedor 
dentro de los primeros 3 días hábiles siguientes a la recepción por parte del 
Proveedor del Acta de Aprobación FAT  emitida formalmente por ADASA, la cual 
confirma la realización satisfactoria de dichas pruebas según el PIE  detallado 
(Desarrollado desde el PIE Base) , lo que se destaca a continuación:  
a) Aprobación del Procedimiento FAT: Antes de iniciar las pruebas, el 
Proveedor debe presentar un procedimiento detallado de FAT, el cual debe 
ser revisado y aprobado formalmente por ADASA. Este es un Punto de 
Espera (H) según el PIE  Detallado  (PIE Item 7.1).    
b) Revisión de Registros y Protocolos: El Proveedor debe generar registros 
detallados de todas las pruebas realizadas durante las FAT. ADASA revisa 
estos registros (como checklists específicos, reportes de pruebas eléctricas, 
resultados de simulación de control, etc., indicados en la columna "Registro 
Requerido" del PIE) para verificar que los resultados cumplen con los 
criterios de aceptación definidos en los procedimientos y especificaciones 
aprobadas.    
c) Protocolo Final FAT: La ejecución satisfactoria de todas las etapas de las 
FAT se documenta en un protocolo o informe final de FAT. (BAE Cl. 39).  
 

---

## PARTE 2 - Continuacion (Paginas 51-94)



---

### Pagina 51
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
51/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 • Estado de Pago  liberación del Encargo  (20% del Precio):  Lo presentará el 
Proveedor dentro de los primeros 3 días hábiles siguientes a la fecha en que 
ADASA haya emitido por escrito la autorización de envío (Certificado de 
Liberación)  del módulo, de acuerdo con  lo estipulado en la Cláusula 39 de estas 
Bases.  
• Estado de Pago  Recepción Provisional (15% del Precio):  El último Estado de 
Pago lo presentará el Proveedor dentro de los primeros 3 días del mes siguiente al 
que el Comprador haya aprobado la Recepción Provisional del Pedido . 
 
Para  proceder  con el pago,  el Proveedor  deberá  presentar  un Estado  de Pago  que contenga 
el detalle con los suministros entregados y/o servicios ejecutados, así como cualquier otra 
prestación del Pedido ejecutada, que serán sometidas a proceso de pago y que hayan 
cumplido íntegramente las condiciones de satisfacción definidas en las presentes Bases.  
Es responsabilidad del Proveedor presentar los respaldos suficientes para la revisión por 
parte de ADASA (ej: planos  aprobados,  bill of lading,  guía de despacho,  Órdenes de 
compra de componentes, certificados emitidos por ADASA , etc.)  
 
Sólo una vez aprobado el detalle ante mencionado, ADASA cursará la emisión del recibo 
correspondiente  (HES)  de aprobación del pago , representado por un documento con un 
número único . El Proveedor deberá incluir el número de Recibo  en la glosa de la Factura 
correspondiente.  La unidad contable de ADASA rechazará toda factura  que no cumpla las 
condiciones anteriores . 
 
Las facturas  que no se ajusten  a lo requerido  en las presentes  instrucciones  serán  devueltas 
al Proveedor para su corrección, con el consiguiente retraso en los pagos.  
 
No se abonará ninguna factura hasta que ADASA haya recibido y dado su conformidad a 
toda la documentación requerida en el Pedido y en los documentos anexos al mismo.  
 
Las facturas se enviarán ADASA para su conformación y pago. El envío constará de todos 

---

### Pagina 52
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
52/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 los ejemplares exigidos por la ley.  
 
No se realizarán  retenciones  a modo  de garantía.  
 
El pago  se realizará , como máximo  dentro de los 30 días corridos contados desde la aprobación 
de la factura  por ADASA.  
 
 
ADASA estará  facultada  para descontar de los Estados de Pago, administrativamente y  sin 
forma alguna de juicio, cualquier suma que le adeude el Proveedor o sus Subcontratistas, 
sea por multas,  suministros  o servicios  prestados,  o rechazados,  o por daños  causados  a su 
propiedad. De la misma manera ADASA podrá retener de los Estados de Pago toda suma 
de dinero  que judicialmente  le fuese  requerida  o demandada,  mientras  no se dicte  sentencia 
definitiva ejecutoriada.  
 
En el caso de existir reclamos o requerimientos de los ya señalados, cuyo valor exceda al 
monto  disponible  del Estado  de Pago  sumado  a las retenciones  que ya existan  en poder  de 
ADASA, ésta tendrá derecho a hacer efectiva cualquier garantía del Proveedor que tenga 
en su poder.  
32. CONDICIONES DE ANTICIPO  
 
Se considera, en el caso de que el Proveedor lo requiera, un anticipo máximo  equivalente 
al veinticinco por ciento (25%)  del monto total neto del contrato u Orden de Compra. El 
pago de este anticipo se entregará únicamente después de que ADASA haya recibido y 
aprobado la Boleta de Garantía Bancaria descrita en la Cláusula 29.1. 
 
El Anticipo no se considera un avance en la ejecución del Pedido, por lo cual, ADASA 
recuperará el Anticipo de la siguiente forma:  
 
• ADASA descontará del monto de cada Estado de Pago aprobado al Proveedor el 

---

### Pagina 53
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
53/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 porcentaje del anticipo entregado al Proveedor.  
• El monto total del Anticipo entregado se completará con el Último Estado de Pago.  
 
33. ENTREGA  DEL PEDIDO  
La entrega del Pedido por parte del Proveedor se realizará bajo la modalidad “EXW – Ex 
Works (Lugar convenido: instalaciones del Proveedor)” Incoterms® 2020 . 
Esto significa que el Proveedor cumple con su obligación de entrega cuando pone la 
mercancía (el Módulo embalado y listo para el transporte según lo acordado y verificado en 
la Inspección Pre -Embarque) a disposición del Comprador (ADASA) o de su transportista 
designado, en las instalaciones del Proveedor (fábrica o almacén) en la fecha o dentro del 
plazo acordado.  
A partir de ese momento de puesta a disposición, todos los riesgos de pérdida o 
daño de la mercancía, así como todos los costos asociados (incluyendo, pero no 
limitado a, carga en el vehículo de transporte, transporte principal, seguros, trámites 
de exportación e importación, descarga en destino) son asumidos por el Comprador 
(ADASA) , salvo acuerdo explícito en contrario por escrito. El Proveedor deberá notificar a 
ADASA con antelación suficiente la fecha exacta en que la mercancía estará disponible 
para su recogida.  
34. DOCUMENTACIÓN  TÉCNICA  
Todos los planos, diseños y especificaciones facilitados por el Comprador al Proveedor 
deben ser considerados como confidenciales y de propiedad exclusiva de aquel. No deben 
ser prestados ni entregados a terceros, copiados ni usados sin previo consentimiento por 
escrito del Comprador.  
El Proveedor deberá entregar sin gasto alguno para ADASA toda la documentación 
requerida para la ejecución del Contrato, ya sea para información, para aprobación o para 

---

### Pagina 54
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
54/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 archivo definitivo, en los tiempos y cantidades establecidas. En el caso particular de planos 
y documentos para aprobación, el Proveedor repetirá el envío cuantas veces sea necesario 
hasta su aprobación final, sin que esto suponga costo adicional alguno para el Comprador , 
como se describe en el punto  7 de la Especificación técnica P22-ET-09-000-001-0 
 
El Pedido no se considerará finalizado hasta que  se haya entregado no sólo el material y/o 
equipos, sino también los planos, protocolos de ensayo, listas de piezas, manuales de 
utilización, libros de instrucciones, listas de piezas de recambio recomendadas y cuantos 
documentos y obligaciones se hayan solicitado con el Pedido.  
 
El Proveedor se compromete, durante un periodo de cinco (5) años desde la fecha de 
entrega del suministro, o  de la prestación de los servicios del Pedido, a guardar y  custodiar 
una copia de la totalidad de la documentación requerida en el mismo. (Certificados de 
calidad, homologaciones, planos finales, registros de END’s, actas de pruebas y ensayos, 
etc.).  
Adicionalmente a la documentación listada en la Especificación Técnica (ET Sección 7), el 
Proveedor deberá desarrollar y entregar para aprobación de ADASA un Plan de 
Inspección y Ensayos Detallado (PIE Detallado) , completando la plantilla PIE Base 
(P22 -IT-09-000-001-0) proporcionada por ADASA. Este PIE Detallado deberá incluir 
referencias cruzadas específicas a los criterios de aceptación contenidos en los 
documentos contractuales y en los propios entregables técnicos aprobados del Proveedor, 
según se detalla en la ET Sección 7.  
 
La aprobación de este PIE Detallado es un requisito para la liberación de fases 
subsecuentes del proyecto, según determine ADASA . Además de su completitud general, 
a la verificación de que cada criterio de aceptación incluido por el Proveedor cumpla con el 
nivel de especificidad detallado en el propio documento PIE Base (P22 -IT-09-000-001-0), 
asegurando que sean inequívocos y trazables a documentos fuente aprobados."    
 

---

### Pagina 55
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
55/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 35. MATERIALES  Y EQUIPOS  
El Proveedor será responsable de que  todos los materiales a suministrar o que utilice en la 
fabricación  de equipos  objeto  del Pedido  sean  nuevos  y libres  de defecto,  de primera  calidad 
y de primer  uso, libres  de defectos  de mano  de obra,  adecuados  para el fin a que se destinan 
y libres de cargas y gravámenes. No se admitirán prototipos, cualquier otra alternativa 
deberá ser aprobada por el Comprador.  
 
El Proveedor deberá realizar el acopio de los equipos y materiales del suministro con la 
suficiente antelación para que se puedan efectuar los Suministros en los plazos previstos, 
siendo de su entera responsabilidad los retrasos que se produzcan.  
 
La lista de repuestos  deberá  incluir  los siguientes  conceptos:  Cantidad,  nombre  y número  de 
identificación, descripción, precio unitario y manuales.  
 
ADASA se reserva el derecho de adquirir los repuestos del Proveedor del equipo total o 
parcialmente, o de un tercero, si lo estima oportuno.  
 
El Proveedor de material a granel (tubos, válvulas, accesorios de tuberías, cables, etc.) 
deberá negociar con ADASA la recompra del sobrante del material suministrado por él a 
precios de mercado.  
36. FABRICACIÓN  
El Proveedor deberá enviar, en un plazo máximo de treinta días  (30) días desde la 
Notificación de Adjudicación , el programa de fabricación de los equipos (en adelante 
también Programa de Trabajo),  detallando  las fases  o hitos  principales  según  la naturaleza  
del Pedido,  tales  como diseño, aprobación de planos, acopios, fabricación, ensamblaje, 
pruebas y entrega de los equipos  al Comprador.  Dicho  programa  debe  incluir  los 
tiempos  necesarios  para la aprobación por el Comprador de los planos y documentos 
sujetos a su aprobación que se indiquen en las Especificaciones Técnicas P22-ET-09-000-

---

### Pagina 56
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
56/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 001-0. 
 
El Proveedor se obliga a mantener informado al  Comprador en todo momento acerca de la 
ejecución del Pedido y de cuantas incidencias surjan durante ella facilitándole diagramas e 
informes de progreso mensuales, para un seguimiento correcto del proceso de diseño, 
acopio, fabricación, inspección y pruebas de los equipos.  
 
El Proveedor se obliga a tomar inmediatamente y a su cargo las medidas necesarias para 
corregir  cuantas  desviaciones  sean  detectadas  tanto  en plazo  de entrega  como  en la calidad 
de los materiales y equipos.  
 
 
37. CALIDAD,  INSPECCIÓN  Y PRUEBAS  
Sin perjuicio del derecho de ADASA a realizar inspecciones y atestiguar pruebas mediante 
su personal propio o representantes designados, ADASA se reserva el derecho, a su 
entera discreción y costo, de designar y utilizar los servicios de una agencia de inspección 
independiente y calificada (Tercero Inspector) para realizar o atestiguar cualquiera de las 
inspecciones y pruebas requeridas en las Especificaciones Técnicas (P22 -ET-09-000-001-
0) y/o el Plan de Inspección y Ensayos (PIE) asociado, incluyendo, pero no limitado a, las 
Pruebas de Aceptación en Fábrica (FAT).  En caso de que ADASA opte por utilizar un 
Tercero Inspector, el Proveedor se obliga a otorgarle el mismo nivel de acceso a las 
instalaciones, documentación y facilidades que se otorgan a los representantes directos de 
ADASA, según lo estipulado en estas Bases y documentos asociados. ADASA comunicará 
oportunamente al Proveedor la identidad de la agencia de inspección seleccionada, si 
aplica.  
Para asegurar el cumplimiento de los requisitos de calidad y especificaciones, el Proveedor 
deberá desarrollar, basado en la plantilla PIE Base (P22 -IT-09-000-001-0) proporcionada 
por ADASA, un Plan de Inspección y Ensayos Detallado (PIE Detallado) . Este 
documento, que detallará las referencias específicas a los criterios de aceptación según se 

---

### Pagina 57
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
57/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 exige en la Especificación Técnica (ET Sección 7), será un entregable contractual clave 
sujeto a la aprobación de ADASA antes del inicio de la fabricación. Las inspecciones y 
pruebas mencionadas en esta cláusula se regirán por el PIE Detallado aprobado.  
Se establece explícitamente que ninguna actividad de fabricación, ensamblaje o ensayo 
que esté sujeta a un Punto de Espera (H) o Punto de Testimonio (W) según el PIE 
Detallado, podrá dar inicio antes de que dicho PIE Detallado, incluyendo la definición 
específica y verificable de todos sus criterios de aceptación conforme a la Cláusula 34, 
haya sido formalmente aprobado por escrito por ADASA."    
El Proveedor  garantiza  la perfecta  calidad  de los suministros,  con el máximo  nivel de calidad 
y competencia  profesional,  conforme  a las Especificaciones  Técnicas  P22-ET-09-000-001-
0, la normativa aplicable y las normas de buena construcción.  
 
El Proveedor  será responsable  y abonará  los gastos  derivados  de corregir,  demoler,  rehacer 
cuantos trabajos hayan sido realizados con los materiales suministrados defectuosamente, 
incluyendo  las paralizaciones  de obra y cualquier  otro gasto  que hubiere  como  consecuencia 
de la calidad de los materiales suministrados.  
 
El Comprador podrá seguir el proceso completo de fabricación de los equipos, mediante 
visitas  a los talleres  y dependencias  del Proveedor  y sus sub proveedores  y subcontratistas, 
en horas normales de trabajo. El Proveedor estará obligado a facilitar a los inspectores y/o 
los representantes  del Comprador,  los medios  e instrumentos  necesarios  para su cometido, 
sin cargo alguno.  
 
El Proveedor queda obligado a  facilitar a los inspectores  y/o representantes del Comprador 
los informes, programas de trabajo, controles de avance de fabricación, y cuantos docu - 
mentos sean necesarios para vigilar y controlar el cumplimiento del Pedido en el tiempo 
previsto y en la calidad requerida.  
 

---

### Pagina 58
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
58/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 El Comprador, si  lo considera oportuno, podrá exigir  a su cargo  la realización de ensayos o 
pruebas adicionales. El Proveedor acepta que, si tales comprobaciones pusieran de 
manifiesto fallos debidos a incumplimiento de especificaciones, defectos de calidad, de 
fabricación,  por cualquier  motivo  no imputable  al Comprador,  los importes  de dichas  pruebas 
y ensayos pasarán a ser por cuenta del Proveedor.  
 
Las correcciones  a las  que hubiere lugar por incumplimiento de  lo expresado en los  puntos 
anteriores se realizarán a juicio exclusivo del Comprador.  
 
El Proveedor autoriza al Comprador a recuperar los gastos de las reparaciones, así como 
los gastos de las pruebas y ensayos a que hubiere lugar mediante su deducción en las 
facturas correspondientes o bien con cargo a las retenciones si se las hubiese practicado.  
 
Si durante la inspección en taller o posteriormente en obra el Comprador detecta que los 
equipos no cumplen con cualquier requisito de las normas aplicables, especificaciones 
técnicas,  códigos,  características,  etc. requeridas,  podrá  libremente  rechazar  los equipos  sin 
incurrir en gasto o cargo alguno.  
 
Es responsabilidad  del Proveedor  realizar  satisfactoriamente  y a su cargo  todas  las pruebas 
requeridas en las leyes, reglamentos, ordenanzas o normas dictadas por las autoridades y 
organismos  oficiales,  así como  la obtención  de las aprobaciones  de las entidades  colabora - 
doras  de la administración  que sean  reglamentarias  para demostrar  que los equipos  cumplen 
con dichas disposiciones.  
Las pruebas  de los equipos  deberán  realizarse  en presencia  de los inspectores  y/o represen - 
tantes del Comprador, cuando así se requiera, quienes recibirán del Proveedor, sub - 
proveedores o subcontratistas las facilidades necesarias.  
 
Serán a cargo del Proveedor todos los gastos relacionados con los servicios prestados por 
su personal  para la ejecución  de las inspecciones  y pruebas,  la confección  de los certificados 
de inspección y los informes de ensayos realizados, la emisión de certificados de análisis 

---

### Pagina 59
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
59/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 por laboratorios calificados, la ejecución de las pruebas de acuerdo con los requerimientos 
del Pedido  y sus anexos  y la redacción  de protocolos  e informes  de las pruebas  finales,  todo 
ello en el número de ejemplares que se establezca en el Pedido.  
 
La fecha prevista por el Proveedor para la realización de las pruebas y ensayos será 
confirmada  por escrito  al Comprador  con un mínimo  de diez (10) días de antelación,  tanto  si 
van a llevarse  a cabo  en sus propios  talleres  o laboratorios  como  si se realizan  fuera  de ellos. 
El hecho de que el Comprador renuncie a presenciar y/o realizar la inspección no releva al 
Proveedor  de su responsabilidad  y garantías.  De igual  modo  la realización  de las mismas  no 
supone causa de modificación del plazo de entrega.  
 
En aquellos  equipos  para los que pudiera  existir  una inspección  de terceros,  la fecha  prevista 
por el Proveedor para la realización de las pruebas o ensayos deberá ser comunicada por 
escrito con  un mínimo de Treinta  (30) días de antelación para suministros  internacionales y 
diez (10) días de antelación para suministros a nivel nacional.  
 
Cualquier omisión o error en la aceptación de los equipos por parte de los inspectores y/o 
representantes del Comprador, no exime al Proveedor de la responsabilidad que implica la 
garantía ni de suministrar los equipos de conformidad con las especificaciones.  
El Proveedor deberá someter al personal  asignado a los trabajos objeto  del Pedido a  todas 
las pruebas  de calificación  que sean  necesarias.  El importe  de dichas  pruebas  será a cargo 
del Proveedor.  
 
En caso de que el Proveedor autorice que los equipos sean enviados a la obra sin 
inspeccionar, la inspección será efectuada en destino por el  Comprador, quien informará al 
Proveedor  del resultado  de la inspección,  comunicando  cuando  proceda  la existencia  de los 
errores y/o defectos que deban ser corregidos por el Proveedor. El Proveedor deberá 
personarse  en la obra dentro  de los tres (3) días siguientes  a la recepción  de la notificación, 
o en el plazo más corto  que razonablemente le sea posible, para comprobar los errores y/o 
defectos aludidos, y proceder sin demora a la reparación. Si el Proveedor no actúa en la 

---

### Pagina 60
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
60/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 forma indicada, el Comprador estará facultado para rechazar el equipo defectuoso o bien 
proceder a la reparación en la obra, todo ello siendo por cuenta y riesgo del Proveedor y a 
su cargo todos los gastos, y sin menoscabo de las garantías.  
 
Si fueran  precisas  nuevas  pruebas  o inspecciones  por causa  del Proveedor  todos  los gastos 
incurridos  (gastos  de viaje,  dietas  y horas  utilizadas)  por el Comprador  serán  por cuenta  del 
Proveedor.  
 
Los anteriores  puntos  serán  también  de aplicación  cuando  un material,  equipo  y/o suministro 
deba ser terminado y/o montado en obra por parte del Proveedor.  
 
37.1  INTERVENCIÓN DE TERCERO INSPECTOR  
 
ADASA se reserva el derecho, a su entera discreción y costo, de designar y contratar los 
servicios de una agencia de inspección independiente y calificada (en adelante, el "Tercero 
Inspector") para realizar o atestiguar, en nombre de ADASA, cualquiera de las 
inspecciones, verificaciones y pruebas definidas en el Plan de Inspección y Ensayos (PIE) 
del Pedido (P22 -IT-09-000-001-0) y/o requeridas por las Especificaciones Técnicas (P22 -
ET-09-000-001-0) y demás documentos contractuales.    
El Proveedor deberá brindar al Tercero Inspector, sin cargo adicional para ADASA, acceso 
irrestricto y oportuno a sus instalaciones y las de sus subcontratistas relevantes, así como 
a toda la documentación, registros, equipos y personal necesarios para llevar a cabo las 
actividades de inspección y prueba encomendadas.    
ADASA notificará por escrito al Proveedor la designación de un Tercero Inspector, 
indicando su identidad y el alcance general de su intervención.  
La participación o ausencia de un Tercero Inspector en cualquier etapa no libera al 
Proveedor de ninguna de sus obligaciones contractuales, incluyendo, pero no limitado a, el 
aseguramiento de la calidad, el cumplimiento de las especificaciones y las garantías 
aplicables al Pedido.  
 

---

### Pagina 61
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
61/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 37.2  PLAZOS DE REVISIÓN, APROBACIÓN Y COORDINACIÓN POR 
ADASA DURANTE LA EJECUCIÓN  
 
• Plazo Estándar de Revisión Documental:  ADASA se compromete a realizar los 
esfuerzos razonables para revisar y emitir comentarios y/o la aprobación (según 
corresponda al flujo definido para cada entregable) de la documentación técnica y 
administrativa sometida por el Proveedor durante la ejecución del Contrato 
(incluyendo ingeniería de detalle, procedimientos, planes, informes, etc.) dentro de 
un plazo máximo de siete (7) días hábiles . Este plazo se contará a partir del día 
hábil siguiente a la recepción formal y completa de la documentación por parte del 
Gestor Técnico/Administrativo designado por ADASA. Este plazo estándar es 
consistente con lo indicado en la ET Sección 7 y el estándar P00 -IT-00-000-101. La 
conformidad de la recepción será comunicada al Proveedor si la documentación se 
considera completa para iniciar la revisión.    
• Coordinación y Asistencia a Puntos de Intervención del PIE (H/W):   
a) El Proveedor deberá notificar formalmente al Gestor Técnico de ADASA las 
fechas programadas para los Puntos de Espera (H - Hold Point) y Puntos de 
Testimonio (W - Witness Point) definidos en el PIE Detallado aprobado, 
cumpliendo estrictamente los plazos mínimos de antelación establecidos en 
la Cláusula 37 de estas BAE (o los plazos específicos que se acuerden y 
documenten en el PIE Detallado aprobado).  
b) ADASA, a través de su Gestor Técnico, confirmará la recepción de la 
notificación y comunicará al Proveedor su intención de asistir (directamente o 
mediante representante/Tercero Inspector) o de renunciar a la asistencia 
para el punto notificado, dentro de los tres (3) días hábiles  siguientes a la 
recepción de la notificación.  
c) Para Puntos de Espera (H):  El Proveedor no podrá continuar con la 
actividad subsiguiente sin la presencia y/o la autorización escrita explícita de 
ADASA o su representante. ADASA es consciente de que su presencia o 
autorización es mandatoria para el avance y coordinará los recursos 

---

### Pagina 62
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
62/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 necesarios para cumplir con la fecha notificada y acordada.  
d) Para Puntos de Testimonio (W):  Si ADASA confirma su no asistencia, o si 
no responde a la notificación del Proveedor dentro del plazo de tres (3) días 
hábiles indicado en el punto (b), el Proveedor estará autorizado a proceder 
con la actividad en la fecha programada. El Proveedor deberá dejar 
constancia documentada (ej. en el registro de la actividad) de la notificación 
enviada y de la confirmación de no asistencia o ausencia de respuesta por 
parte de ADASA.    
• Gestión de Potenciales Retrasos de Revisión por ADASA:  En el evento 
excepcional de que ADASA anticipe que no podrá cumplir con el plazo estándar de 
revisión documental (XX.1) o asistir a un Punto de Espera (H) en la fecha 
coordinada, el Gestor del Contrato de ADASA lo comunicará formalmente al 
Proveedor tan pronto como sea posible, exponiendo las razones y la nueva fecha 
estimada de respuesta o asistencia. Ambas Partes se reunirán para evaluar el 
posible impacto en el cronograma del Proveedor y acordarán, de buena fe y por 
escrito, las medidas de mitigación o los ajustes necesarios, si correspondiera, 
conforme a las demás cláusulas contractuales (ej. Cl. 44 Fuerza Mayor, Cl. 48 
Suspensión Temporal por causas imputables al Comprador)."    
 
38. EMBALAJE  Y MARCADO  
El Proveedor está obligado a cuidar que el embalaje, marcado, carga y estiba de la 
mercancía  que comprende  el Pedido  se haga  en las mejores  condiciones  para su protección, 
manejo y siempre de acuerdo con la especificación general de embalaje, marcado y envío 
adjunto con el Pedido.  
 
El Comprador se reserva el derecho a inspeccionar todos los Suministros en las 
instalaciones del Proveedor o en la de los subcontratistas antes del embarque y a requerir 
embalaje en la forma apropiada con cargo al Proveedor de cualquier Suministro que se 
juzgue mal preparado para el envío.  

---

### Pagina 63
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
63/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
El Proveedor deberá desarrollar y someter a aprobación de ADASA un "Procedimiento 
Detallado de Preservación, Embalaje y Preparación para Transporte Marítimo 
Internacional", según lo requerido en la Especificación Técnica (ET Sec. 7). El 
cumplimiento estricto de dicho procedimiento aprobado es obligatorio y será verificado 
durante la Inspección Pre -Embarque.  
 
Dado que la entrega del Pedido se rige por la regla Incoterms® 2020 EXW en las 
instalaciones del Proveedor, la responsabilidad y el riesgo de pérdida o daño durante el 
transporte recaen en ADASA a partir del momento en que la mercancía es puesta a su 
disposición. Para mitigar este riesgo de daño durante el tránsito internacional, el Proveedor 
deberá desarrollar y someter a la aprobación rigurosa de ADASA un Procedimiento 
Detallado de Preservación, Embalaje y Preparación para Transporte Marítimo 
Internacional , según lo exigido en la Sección 7 de la Especificación Técnica (ET P22 -ET-
09-000-001-0). Este procedimiento detallará, entre otros, los métodos específicos de 
preservación, aseguramiento interno, materiales de embalaje y marcado.  
 
ADASA se reserva el derecho de inspeccionar y atestiguar (Punto W en el Plan de 
Inspección y Ensayos - PIE) la correcta y estricta aplicación de dicho procedimiento 
aprobado durante la Inspección Pre -Embarque en las instalaciones del Proveedor, según 
se detalla en la Sección 8 del PIE (P22 -IT-09-000-001-0), y conserva el derecho a requerir 
embalajes apropiados con cargo al Proveedor si juzga que el suministro está mal 
preparado para el envío. La verificación satisfactoria del cumplimiento del Procedimiento 
Detallado de Preservación, Embalaje y Preparación para Transporte Marítimo Internacional 
durante la Inspección Pre -Embarque es una condición obligatoria y un Punto de Espera 
(H) para la emisión del Certificado de Liberación  (Dispatch Release), sin el cual los 
equipos no podrán ser despachados ni transportados . 
 
39. EXPEDICIÓN  Y ENTREGA  
 

---

### Pagina 64
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
64/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 La preparación para la expedición  del Módulo  RO de segunda etapa para Salmuera  por 
parte del Proveedor , deberá efectuarse única y exclusivamente una vez emitida el Acta de 
Aprobación FAT  por parte de ADASA (confirmando la realización y aprobación 
satisfactoria de todas las pruebas según PIE), verificada la conformidad de la preservación, 
embalaje y marcado  según el procedimiento aprobado durante la Inspección Pre -
Embarque, aceptado el Dossier Final de Calidad de Fabricación, y recibida la autorización 
de envío por escrito de ADASA ("Certificado de Liberación" según PIE), a no ser que las 
partes acuerden por escrito condiciones distintas . 
 
Si ADASA solicitase aplazar la recogida de la mercancía ya liberada, el Proveedor, a 
simple requerimiento de ADASA, estará obligado a mantener depositados en sus 
almacenes, sin costo alguno para el Comprador por un plazo máximo acordado (o seis (6) 
meses por defecto según BAE), el material y/o equipos objeto del Pedido a partir de la 
fecha de disponibilidad notificada. Este almacenaje se realizará de forma tal que los 
materiales y/o equipos se conserven en perfecto estado, adquiriendo el Proveedor las 
responsabilidades como depositario y debiendo entregar un Certificado de depósito. 
ADASA podrá proceder a la retirada en cualquier momento, prestando el Proveedor su 
colaboración.    
 
El Proveedor facilitará oportunamente al Comprador toda la documentación de la 
mercancía (listas de empaque, certificados, manuales, datos técnicos, información de 
origen, etc.) que sea razonablemente necesaria y requerida por ADASA para que este 
último pueda gestionar y realizar el transporte, y los trámites de aduanas 
(exportación/importación) hasta la obra. En el caso de suministros que se consideran de 
doble uso, civil y militar, el Proveedor deberá notificarlo al Comprador y aportar la 
documentación pertinente para que ADASA gestione su envío. Se deja constancia que, 
bajo la modalidad EXW Incoterms® 2020, la organización, contratación y costo del 
transporte y seguros desde las instalaciones del Proveedor hasta la obra son 
responsabilidad exclusiva de ADASA.    
 

---

### Pagina 65
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
65/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 La puesta a disposición de los equipos y/o materiales deberá efectuarse en la fecha o 
dentro del plazo establecido, acompañando la documentación pertinente (copia del 
Certificado de Liberación , Packing List detallado). El Proveedor identificará todos los 
paquetes y bultos según lo especificado y la normativa vigente.    
 
El Proveedor deberá proporcionar al Comprador las instrucciones de almacenamiento en el 
Sitio para la buena conservación de los equipos hasta su montaje, entregando junto con 
estos los productos o útiles específicos requeridos para dicha conservación. El Proveedor 
será responsable de los desperfectos si se han seguido sus instrucciones.    
 
Aun existiendo aceptación previa (Liberación para Despacho), la aceptación final sólo 
tendrá lugar en la obra, tras el montaje y pruebas correspondientes. Cualquier equipo 
recibido en obra que no cumpla especificaciones podrá ser devuelto al Proveedor (a costo 
y riesgo del Proveedor) o reparado por el Proveedor en obra, según elección de ADASA. El 
Proveedor deberá acudir a obra en los plazos indicados para verificar y/o reparar, 
asumiendo todos los costos y responsabilidades asociados a la no conformidad.    
 
Además de la Inspección Pre -Embarque realizada en las instalaciones del Proveedor, a la 
llegada del Módulo y sus componentes al Sitio del Proyecto en Taltal, ADASA o su 
representante designado realizará una Inspección a la Recepción en Sitio  formal y 
detallada. Esta inspección, que se llevará a cabo conforme al Plan de Inspección y 
Ensayos (PIE), incluirá, pero no se limitará a, la verificación exhaustiva de los embalajes, la 
apertura de los bultos críticos para inspeccionar detalladamente el estado físico y la 
integridad de los equipos principales y componentes sensibles, y la comprobación 
minuciosa de la concordancia con la lista de embalaje (packing list) detallad a.  
 
El Proveedor deberá colaborar plenamente con ADASA en la ejecución de esta inspección. 
Cualquier daño o no conformidad detectada durante esta Inspección a la Recepción en 
Sitio, así como las que puedan identificarse posteriormente durante las actividades de 
montaje y comisionamiento en sitio (según se detalla en la Sección 10 del PIE y los puntos 

---

### Pagina 66
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
66/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 de intervención definidos - H/W), deberá ser notificado por el Proveedor a ADASA sin 
demora y será objeto de corrección, reparación o reemplazo por parte del Proveedor a su 
entero costo y riesgo, conforme a lo estipulado en la Cláusula 28 y 49 de estas Bases y en 
el PIE. La detección temprana de tales anomalías en sitio, facilitada por esta inspección 
detallada a la recepción y el seguimiento riguroso de los puntos de intervención en el PIE 
durante el montaje y puesta en marcha, es crítica para asegurar el cumplimiento de los 
requisitos técnicos y minimizar el impacto en el cronograma general del Pedido.  
 
40. COMISIONAMIENTO  Y PUESTA  EN MARCHA  
Las actividades de Comisionamiento y Puesta en Marcha estipuladas en las 
Especificaciones Técnicas P22-ET-09-000-001-0, punto 9 , son alcance del Proveedor , y 
serán de cuenta del Proveedor los gastos derivados de su personal, equipos y materiales 
necesarios  para ejecutar dichas actividades .  
Los Aportes que son alcance de ADASA para que el Proveedor pueda ejecutar las labores 
de Comisionamiento y Puesta en Marcha se listan a continuación:  
- Conexiones Físicas o Tie In establecidos en sección 5.6 de las Especificaciones 
Técnicas.  
- Energía Eléctrica en 380 V y 50 Hz , suficiente para el consumo establecido por el 
Proveedor en su Oferta Técnica  
- Salmuera para alimentación del Módulo RO de Segunda Etapa , en las condiciones 
establecidas en las especificaciones técnicas , y con la presión mínima requerida por el 
Proveedor en uso Oferta Técnica.  
- Químicos para Comisionamiento y Puesta en Marcha requeridos por el Proveedor en 
su Oferta Técnica.  

---

### Pagina 67
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
67/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 El Proveedor  acepta  la plena  responsabilidad  de la manipulación  y montaje  de los materiales 
y equipos y de los daños ocasionados a estos o a las instalaciones del Proveedor y/o 
terceros.  
 
El Proveedor será responsable de todos los accidentes de trabajo de su personal que 
pudieran producirse y deberá por consiguiente cubrir los seguros necesarios en forma 
oportuna . 
 
El Proveedor está obligado por sí mismo y de manera exclusiva respecto a su personal a 
cumplir con cuantas obligaciones se deriven de la legislación laboral y de seguridad social 
vigente  en Chile , debiendo estar al corriente tanto de los haberes debidos a su personal 
como del pago de las cuotas y contribuciones debidas al régimen general de la Seguridad 
Social, formación profesional, desempleo, accidentes de trabajo, etc.  
 
El Proveedor está asimismo obligado al cumplimiento de las disposiciones legales que 
afecten a su actividad y deberán atenerse a las normas de régimen propio del Proveedor 
incluidas las de materia en Seguridad e Higiene y Medio Ambiental.  
 
El Proveedor, a petición de ADASA, acreditará documentalmente el cumplimiento de las 
obligaciones legales o reglamentarias aquí referidas siendo el incumplimiento de dicha 
petición  causa  de resolución  o terminación  anticipada  del Pedido.  En todo caso  el Proveedor 
deberá suministrar al comprador previo a cualquier pago  que éste último le efectúe  durante 
el montaje y puesta en marcha y/o supervisión, certificado emitido por la Inspección del 
Trabajo competente en la Obra o de una entidad acreditadora autorizada, que acredite la 
inexistencia de reclamos pendientes ni de cotizaciones previsionales y/o de salud impagas 
respecto del personal del Proveedor que se desempeñe en la Obra. En caso de que  el 
Proveedor  no acredite  oportunamente  el cumplimiento  íntegro  de las obligaciones  laborales 
y previsionales y de seguridad por medio de los certificados que establece la ley, así como 
también  cuando  sea informado  el Comprador de  este hecho por  la Dirección del  Trabajo, el 
Comprador  podrá  retener  de los pagos  pendientes  los montos  correspondientes  a 

---

### Pagina 68
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
68/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 remuneraciones, cotizaciones previsionales y otros pagos que establezca la ley a favor de 
los trabajadores de modo tal que el Comprador pague por subrogación las cantidades 
adeudadas a los trabajadores del Proveedor. Las obligaciones enunciadas son extensivas 
respecto de la obligación laboral, provisional y de seguridad que tengan a su vez los 
trabajadores del Proveedor, todo lo anterior según lo establece el artículo 183 -C de la Ley 
20.013, de fecha 16 de octubre de 2006, y su Reglamento. Asimismo,  el Proveedor deberá 
presentar previa petición del Comprador Certificado emitido por la autoridad tributaria 
competente de estar al día en el pago y cumplimiento de sus obligaciones fiscales.  
 
El Comprador  se reserva  el derecho  de rechazar  al personal  de obra cuando  estime  que no 
es apto para el trabajo o por conducta inadecuada.  
 
El Comprador no se hará responsable por la pérdida, hurto, desperfecto producido por 
cualquier motivo en los utensilios, herramientas o maquinaria del Proveedor.  
 
Los supervisores de montaje y/o puesta en marcha del Proveedor actuarán como 
interlocutores de este frente al Comprador y tendrán la responsabilidad de la instalación y 
puesta en marcha de los equipos.  
 
Según se indique en las especificaciones técnicas  y en este documento , el 
comisionamiento y  puesta en marcha del módulo  deberá realizarse dentro del plazo 
indicado  en la cláusula 27 de este documento.  Si se produjeran retrasos, sus causas 
deberán estar documentadas por el supervisor del Comprador quien determinará si dichos 
retrasos son imputables o no a causas ajenas al Proveedor, siendo responsabilidad del 
Proveedor  la obtención  de los visados  y resto  de permisos  requeridos  para acceder  a la obra.  
Para el cómputo de los días trabajados por el personal del Proveedor no se incluirán los 
tiempos  dedicados  a reparaciones  o terminación  de trabajos  que el Proveedor  debería  haber 
realizado  en sus instalaciones,  ni los tiempos  de inactividad  derivados  de la indisponibilidad 
de equipos, materiales, consumibles o documentación dentro del alcance y 
responsabilidades del Proveedor.  

---

### Pagina 69
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
69/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 41. RECEPCIÓN  PROVISIONAL  
El Acta de Recepción Provisional se rá emiti da por ADASA  una vez que el Proveedor 
cumpla los siguientes requisitos:  
 
1) Entrega Completa:  Haber entregado todos los equipos y materiales del Pedido.  
2) El Proveedor  ha completado los servicios de Comisionamiento y Puesta en 
Marcha.  
3) Pruebas de Desempeño Superadas:  Haber ejecutado y aprobado las Pruebas de 
Desempeño en sitio (capacidad, calidad, consumo energético) según la ET Sec. 
10.2. La aprobación del informe final de estas pruebas es un Punto de Espera (H) 
de acuerdo con el PIE definitivo  (PIE Item 11.5).  
4) Documentación Final Aprobada:  Haber entregado y obtenido la aprobación de 
ADASA para toda la documentación técnica final (Manuales O&M, Planos As -Built 
verificados en sitio, software, licencias, etc.) según BAE Cl. 34, ET Sec. 7 y de 
acuerdo con el PIE definitivo. ( PIE Item 12.1a, 12.1b, 12.1c).  
5) Garantía Técnica Entregada : Haber presentado la Boleta de Garantía Bancaria 
por Garantía Técnica o de Desempeño según BAE Cl. 29.3.  
6) Cierre de Pendientes:  Haber cerrado todas las no conformidades o puntos 
pendientes registrados , de acuerdo con el  PIE definitivo  (PIE Item 12.2).  
7) Entrega de Repuest os: Haber entregado los repuestos Mandatorios para Puesta 
en Marcha.  
 
Adicionalmente, en caso de que las Especificaciones Técnicas lo requieran, el Acta de 
Recepción Provisional se emitirá una vez que se verifique el correcto montaje de todos los 
componentes del suministro y se realicen las pruebas de puesta en marcha a plena 
satisfacción del Comprador.  
 
En todo caso, el Acta de Recepción Provisional no supondrá un reconocimiento del 

---

### Pagina 70
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
70/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Comprador  respecto  del cumplimiento  de las garantías  técnicas  respectivas,  sino hasta  que 
no haya transcurrido dicho período de garantía.  
 
42. RECEPCIÓN  DEFINITVA  
Transcurrido el periodo de garantía de la cláusula 28 de forma satisfactoria, el Proveedor 
podrá solicitar por escrito del Comprador que le extienda el Acta de Recepción Definitiva. 
Con la formalización del Acta, el Comprador devolverá al Proveedor las correspondientes 
Boletas de Garantías, según lo indicado en la cláusula 29. 
 
La recepción definitiva de lo contratado no liberará al Proveedor de su eventual 
responsabilidad por vicios ocultos o cualquier otra responsabilidad que le fuera exigible en 
derecho y a lo que el Comprador no hubiera renunciado expresamente.  
 
Únicamente se emitirá el Acta de Recepción Definitiva si se han cumplido los siguientes 
requisitos:  
 
• Que todas las posibles reclamaciones del Comprador relacionadas con las Boletas de 
Garantías se hayan atendido satisfactoriamente, o en su caso exista acuerdo entre las 
Partes en cuanto a la aplicación de estas . 
 
• Que haya  transcurrido  el plazo  de garantía  referido  en la cláusula  28, desde  la Recepción 
Provisional.  
43. MULTAS  
 
43.1  MULTAS POR ATRASOS  
 
a) Atraso en la entrega de la ingeniería  y Documentos : El atraso en la entrega de la 
ingeniería según lo indicado en las Especificaciones Técnicas P22-ET-09-000-001-0 
sección 7 , aplicará una multa diaria equivalente al 0,05 %  del valor neto total del 

---

### Pagina 71
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
71/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Contrato  u Orden de Compra , por cada día calendario de atraso . 
 
b) Por atraso en la entrega del suministro (EXW):  Se aplicará una multa diaria 
equivalente al 0,2 % del valor neto total del Contrato  u Orden de Compra , por cada día 
calendario en que se exceda el Plazo de Entrega  del Módulo RO Segunda Etapa 
establecido en la Cláusula 27.   
 
c) Atraso en Finalización de Comisionamiento y Puesta en Marcha:  Se aplicará una 
multa diaria equivalente al 0,1 % del valor neto total del Contrato  u Orden de Compra , 
por cada día calendario en que se exceda  el plazo estipulado en Cláusula 27 para 
completar las actividades de Comisionamiento y Puesta en Marcha . 
 
d) Por la no entrega de documentación requerida:  Por cada día calendario de atraso en 
la entrega de la documentación final requerida para la Recepción Provisional o 
Definitiva según corresponda, Aguas de Antofagasta aplicará una multa  diaria 
equivalente al  0,05%  del valor neto del Contrato  u Orden de Compra . 
 
A efectos de esta cláusula, se consideran 'documentos principales' cuya falta 
impide la recepción correspondiente, los siguientes entregables finales:   
• Plan de Inspección y Ensayos detallado.  
• Filosofía de Control.  
• Manual de puesta en marcha de la planta y sus equipos.  
• Manual de operación y mantenimiento de la planta y sus equipos (completo, 
incluyendo pantallas PLC, TAGs, procedimientos detallados según ET Sec. 7 y 
requerimientos de BAE Cl. 34).  
• Planos As -Built finales (verificados en sitio según BAE Cl. 34 y 41  y PIE Item 
12.1b).  
• Manual de montaje de la planta (incluyendo memoria de cálculo para izaje, planos 
de izaje y diseño de yugo).   
• Dossier de Calidad Final de Fabricación aprobado (según BAE Cl. 39 y PIE Item 
8.3).  

---

### Pagina 72
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
72/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 • Paquete Final de Software y Licencias perpetuas (según ET Sec. 7 y PIE Item 
12.1c).  
• Informe Final de Pruebas de Desempeño aprobado (según PIE Item 11.5).  
 
El Proveedor  quedará constituido en mora del cumplimiento de sus obligaciones por el solo 
hecho de  exceder los plazo s estipulado s, sin necesidad de requerimiento, intimación o 
notificación alguna.  
Estas multa s tendrá n el carácter de moratorias y es sin perjuicio del cumplimiento de su 
obligación principal  por parte del Proveedor  y de la respectiva compensación de aquellos 
perjuicios que excedieran el importe  de la multa.  
 
 
43.2  MULTAS POR INCUMPLIMIENTO DE GARANTÍAS DE 
DESEMPEÑO (APLICABLES SEGÚN RESULTADOS PRUEBAS 
ET SEC. 10.2):  
 
Las siguientes multas se aplicarán basadas en los resultados promedio obtenidos durante 
la Prueba de Desempeño de 2 días consecutivos descrita en la ET Sec. 10.2 . 
 
a) Incumplimiento de la Capacidad Nominal Garantizada (ET Sec. 10.1.1 y 10.2.1):  Si 
la capacidad promedio de producción de permeado durante la prueba de 2 días es 
inferior a los 480 m³/día s garantizados  (20 m³/h ), se aplicará una multa calculada 
como:  
Multa_Capacidad = ( (Capacidad Garantizada - Capacidad Real Promedio) / 
Capacidad Garantizada ) * K_Cap * Valor Neto Contrato   
Donde:  
• Capacidad Garantizada = 480 m³/día  
• Capacidad Real Promedio = Valor promedio medido en m³/día durante la 
prueba.  
• K_Cap = Factor de penalización por capacidad definido como 0.5 . 

---

### Pagina 73
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
73/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
b) Incumplimiento de la Calidad del Agua Producto Garantizada (ET Sec. 10.1.2 y 
10.2.2):  Si durante la prueba de 2 días, alguna muestra diaria analizada (in situ o 
laboratorio) excede los límites garantizados (TDS > 500 mg/l o Cloruros > 400 mg/l), 
se aplicará:  
i. Una multa fija de (2.000 Dólares  Estadounidenses)  por cada día en que al 
menos uno de los parámetros no cumpla.  
ii. Adicionalmente, el Proveedor estará obligado a identificar y corregir la causa 
del incumplimiento a su entero costo en un plazo máximo acordado con 
ADASA. La persistencia del incumplimiento tras dicho plazo podrá ser causal 
de ejecución de la s Garantías de las cuales disponga ADASA y/o término 
anticipado de contrato.  
 
c) Incumplimiento del Consumo Específico de Energía Eléctrica Garantizado (ET 
Sec. 10.1.3 y 10.2.3): Si el Consumo Específico de Energía Eléctrica (CEE) promedio 
medido durante la Prueba de Desempeño de 2 días (en kWh/m³) supera el valor 
garantizado por el Proveedor en su oferta (CEE_Garantizado), se aplicará una multa 
única calculada como la valorización del sobrecosto energético proyectado durante el 
período de evaluación de la multa, según la siguiente fórmula:  
Multa_CEE = (CEE_Medido - CEE_Garantizado) * Producción_Anual_Proyectada 
* Costo_Energía_Multa * N_Años  
Donde:  
• CEE_Medido  = Valor promedio medido en kWh/m³ durante la prueba de 
desempeño.  
• CEE_Garantizado  = Valor garantizado por el Licitante en su oferta, en kWh/m³ 
(para el rango de TDS correspondiente según ET Sec. 10.1.3).  
• Producción_Anual_Proyectada  = 480 m³/día  * 365 días/año = 175.200  
m³/año.  
• Costo_Energía_Eval  = Corresponde al costo unitario promedio de la 
energía eléctrica fijo y definido para la evaluación económica  en la 

---

### Pagina 74
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
74/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Cláusula 2 4.4 de estas BAE (establecido en 0,1 USD /kWh ). Este valor se 
utilizará como base contractual fija para el cálculo de esta multa, 
independientemente del costo real de la energía al momento de las pruebas.  
• N_Años  = Número de años para proyectar el sobrecosto, establecido en 3 
años   
 
43.3 OTROS INCUMPLIMIENTOS  
 
Cualquier otro incumplimiento de las obligaciones establecidas en estas Bases 
Administrativas y/o en las Especificaciones Técnicas, que no esté específicamente 
sancionado en los puntos 43.1 o 4 3.2, aplicará una multa diaria equivalente al 0,05 % del 
valor neto total del Contrato  u Orden de Compra , por cada día que persista el incumplimiento 
y por cada evento, hasta que el incumplimiento sea subsanado a satisfacción de ADASA.  
 
43.4  LÍMITE Y APLICACIÓN DE MULTAS:  
 
• El monto acumulado de multas  cursadas al Proveedor , por cualquier concepto (atrasos, 
desempeño, otros) , tendrá como límite 15% del monto  neto del Contrato u Orden de Compra.  
• Las multas serán descontadas por ADASA de los estados de pago pendientes o, en su 
defecto, se podrán hacer efectivas contra las boletas de garantía correspondientes (Fiel 
Cumplimiento o Garantía Técnica/Desempeño).  
44. FUERZA  MAYOR  
No serán admitidos por el Comprador los retrasos originados por acontecimientos o 
condiciones  especiales  desfavorables,  de cualquier  naturaleza  que estas  sean,  a menos  que 
las mismas tengan su origen en causas de Fuerza Mayor.  
 
Se considera que los retrasos o falta de cumplimiento de una de las partes no constituyen 
incumplimiento del pedido ni darán lugar a reclamaciones de la otra Parte, siempre que tal 
circunstancia  sea debida  a causas  de Fuerza  Mayor,  que impidan  realmente  el cumplimiento 

---

### Pagina 75
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
75/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 de los compromisos derivados del Pedido.  
 
Se entenderá por Fuerza Mayor todos aquellos sucesos o circunstancias que impidan 
cualquiera de las partes  el cumplimiento de las obligaciones derivadas del Pedido, siempre 
y cuando estos sucesos o circunstancias fueren imprevistas e imposibles de resistir, de 
acuerdo con lo establecido en el artículo 45 del Código Civil  de Chile . 
 
Para que el Comprador pueda reconocer y admitir la existencia de Fuerza Mayor, el 
Proveedor  deberá  en cada  caso,  poner  en conocimiento  del Comprador  tan pronto  como  sea 
posible  y no más tarde  de cuarenta  y ocho  (48) horas  siguientes  al momento  en que aquellas 
aparezcan, el comienzo y posible duración del supuesto de Fuerza Mayor, explicando los 
detalles  completos  y los motivos,  y tratando  de llegar  a un acuerdo  con el Comprador  sobre 
las consecuencias de esta.  
 
El cumplimiento  por el Proveedor  de las obligaciones  afectadas  por causas  de Fuerza  Mayor, 
se suspenderá durante el periodo de duración de dicha causa y los plazos de ejecución se 
entenderán  prorrogados  como  máximo  por un periodo  equivalente  al del tiempo  perdido  por 
causa de la Fuerza Mayor. A estos efectos se tendrá en cuenta la adopción de medidas y 
precauciones que razonablemente haya adoptado el Proveedor para prevenir y evitar en lo 
posible que los trabajos ejecutados y los materiales y equipos acopiados y/o entregados 
pudieran sufrir daños en tales casos.  
 
Todos los efectos causados por la Fuerza Mayor serán remediados tan pronto como sea 
posible y  se mitigarán  en la medida  de lo posible  por el  Proveedor, estando obligado este  a 
poner todos los medios a su alcance para conseguirlo.  
 
El Proveedor no podrá pretender indemnización alguna por la eventual aplicación de 
cualquiera de las causas de Fuerza Mayor.  
 
Si las causas de Fuerza Mayor se prolongasen por más de 100 días, las Partes tendrán 

---

### Pagina 76
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
76/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 derecho  a resolver  o terminar  anticipadamente  el Pedido.  Teniendo  derecho el  Proveedor  a 
recibir el importe correspondiente a todos los Suministros realizados a la fecha de 
terminación.  
 
En el caso  de la terminación  contemplada  en el punto  anterior,  el Proveedor  interrumpirá  los 
Suministros, no emitirá nuevas órdenes de equipo, material o servicios, proveerá un listado 
de todas las órdenes de Proveedores o compromisos y, a menos que el Comprador le 
indique lo contrario, cancelará en la medida de lo posible todas las órdenes emitidas y 
compromisos adquiridos. El Proveedor entregará al Comprador todos los Suministros 
realizados con anterioridad a la terminación y tomará además todas las otras medidas 
necesarias para completar el traspaso al Comprador del título sobre los Suministros.  
45. CUMPLIMIENTO  DE LAS LEYES  
En todo lo relacionado  con el Pedido, el  Proveedor  actúa  con personalidad  jurídica  propia  e 
independiente del Comprador. Tampoco podrá considerarse, en ninguna circunstancia, al 
personal del Proveedor como dependiente del Comprador.  
 
El Proveedor garantiza que cumplirá con todas las disposiciones legales, reglamentarias, 
administrativas  y contractuales  aplicables,  y, especialmente,  las que estén  referidas  a medio 
ambiente, seguridad en el trabajo y defensa de los usuarios y consumidores.  
 
Si se produjeran  cambios  en la legislación  o en los códigos  nacionales  o internacionales  que 
fuesen de aplicación al Pedido, con posterioridad a la fecha de este, el Proveedor deberá 
igualmente cumplir con dichas modificaciones.  
 
Todos los permisos, licencias y certificados que sean necesarios para el cumplimiento del 
Pedido,  en virtud  de las leyes,  reglamentos,  ordenanzas,  normas,  etc., aplicables  deben  ser 
procurados por el Proveedor a su cargo y expensas, debiendo eximir al Comprador de 
cualquier responsabilidad y/o penalidad que pudiera serle impuesta a causa de cualquier 
violación a tales leyes, reglamentos, ordenanzas, etc. en que incurriese por si mismo, sus 

---

### Pagina 77
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
77/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 empleados, agentes, subproveedores y/o subcontratistas en todo lo relacionado con el 
Pedido.  
 
Antes  de la entrega  de los equipos,  el Proveedor  proporcionará  al Comprador  las necesarias 
autorizaciones gubernamentales o de otras autoridades que dichos equipos requieran, 
debiendo responsabilizarse de obtener de las mismas las pruebas de aceptación de los 
equipos,  incluyendo  la prueba  final,  así como  todos  los certificados,  planos  de construcción, 
análisis e informes de todas las pruebas que se requieran, incluyendo la colocación en el 
equipo de la marca de aprobación final del mismo para su puesta en funcionamiento.  
 
El Proveedor facilitará al Comprador la información técnica necesaria, en cantidad y plazo 
que precise  para obtener  permisos  y autorizaciones  de las instalaciones,  cuando  éstas  sean 
competencia del Comprador.  
 
46. CESIÓN  Y SUBCONTRATACIÓN  
El Proveedor  no podrá  ceder,  transferir  o traspasar  en forma  alguna,  total ni parcialmente  los 
derechos y obligaciones establecidos en el Contrato; ni tampoco constituir sobre ellas 
garantías, prendas u otros gravámenes que lo afecten, ni otorgar mandatos de cobro 
irrevocables a un tercero, sin la aprobación escrita y previa del Comprador.  
Asimismo, el Proveedor no podrá subcontratar la totalidad o parte del Pedido, sin la 
aprobación escrita y previa del Comprador.  
 
Esta aprobación no eximirá al Proveedor de su responsabilidad siendo totalmente 
responsable  de cualquier  fallo o negligencia  por parte  de sus Proveedores  o subcontratistas, 
considerándose  a todos  los efectos  como  si el trabajo  se hubiera  realizado  directamente  por 
el propio Proveedor.  
 
En todo caso, la autorización de ADASA siempre deberá entenderse que no afecta en lo 
absoluto a los derechos que ADASA tiene en el Contrato de que se trata y que por motivo 

---

### Pagina 78
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
78/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 alguno, ADASA podrá verse impedido en su ejercicio.  
 
Salvo instrucciones en contra, la compra de materias primas y elementos estándar o 
comerciales incorporados a los equipos objeto del pedido, no se considerará como 
subcontrato. El Comprador se reserva el derecho de exigir si lo considera oportuno, que el 
Proveedor le someta a aprobación la lista de sub proveedores de los que intenta 
aprovisionarse para realizar los acopios necesarios para el pedido. Asimismo a 
requerimiento  del Comprador, el  Proveedor deberá enviarle copia de todos los sub pedidos 
incluyendo los de materias primas y elementos “estándar” o comerciales.  
 
El Comprador podrá en todo momento inspeccionar y vigilar los trabajos del subcontratista 
y el cumplimiento  de sus obligaciones  y el subcontratista  queda  obligado  a facilitarle  toda la 
documentación que para ello pueda ser necesaria.  
 
El Comprador está expresamente facultado, sin necesidad de consentimiento previo del 
Proveedor, para ceder, total o parcialmente el Pedido en las condiciones pactadas a 
cualquier empresa.  
 
Se estipula expresamente a favor de la “Empresa Concesionaria de Servicios Sanitarios 
S.A.”, persona  jurídica del giro  de su  razón social, Rol Único  Tributario N°  96.579.410 -7, en 
su calidad de sucesora y continuadora legal de la Empresa de Servicios Sanitarios de 
Antofagasta  S.A. (ESSAN  S.A.),  Rol Único  Tributario  N° 96.579.410 -7, la facultad  de sustituir 
y reemplazar a Aguas de Antofagasta S.A. en su posición contractual en el contrato objeto 
de la presente licitación. La facultad de sustitución estipulada a favor de  la “Empresa 
Concesionaria de Servicios Sanitarios S.A.” quedará sujeta a la condición suspensiva de 
producirse la terminación del contrato de transferencia del derecho de explotación de las 
concesiones sanitarias celebrado entre Aguas de Antofagasta S.A. y la Empresa de 
Servicios Sanitarios de Antofagasta S.A. con fecha 29 de diciembre de 2003, respecto del 
cual la “Empresa  Concesionaria  de Servicios  Sanitarios  S.A.”  ha adquirido  la posición  jurídica 
de ESSAN S.A. Para hacer efectiva la sustitución referid a, la “Empresa Concesionaria de 

---

### Pagina 79
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
79/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Servicios Sanitarios S.A.” deberá notificar por escrito, al proveedor que se adjudique este 
contrato, su decisión de sustituir a Aguas de Antofagasta S.A. en este contrato con una 
anticipación mínima de treinta días. Por lo cual, la empresa proponente que participa de la 
presente licitación, acepta desde ya el ejercicio por parte de la “Empresa Concesionaria de 
Servicios Sanitarios S.A.” la  facultad  de sustituir a Aguas de  Antofagasta S.A., renunciando 
a cualquier derecho, acción o indemnización que pudiere corresponderle.  
 
El proveedor bajo ningún motivo o circunstancia, podrá ceder total o parcialmente los 
derechos  y obligaciones  que emanan  del presente  contrato  a un tercero  sin el consentimiento 
expreso de Aguas de Antofagasta S.A. o de su sucesora.  
 
En caso de que el Comprador recibiera alguna reclamación de algún subcontratista o sub 
proveedor, el Comprador estará  facultado para retener al Proveedor de los pagos vencidos 
las cantidades reclamadas.  
47. PATENTES  Y ROYALTIES  
El Proveedor mantendrá indemne y defenderá libre de todo gasto al Comprador o terceros 
que utilicen o vendan los equipos objeto del Pedido, frente a toda demanda o acción por 
infracción  de patentes,  derechos  de invención,  "copyright"  o marcas  comerciales,  derivadas 
del empleo o venta de dichos equipos.  
 
El Proveedor  mantendrá  asimismo  al Comprador  libre de responsabilidades  o perjuicios  y le 
indemnizará  por toda pérdida, garantía  económica,  costo,  daño  o gastos  en que incurra  por 
causa de cualquier demanda o acción contra ellos o contra terceros que utilicen o vendan 
los equipos y/o materiales objeto del Pedido. El Comprador se reserva el derecho de 
participar en la defensa contra estas demandas o acciones, o bien asumir por si solo la 
defensa, utilizando sus propios abogados.  
48. SUSPENSIÓN  TEMPORAL  
El Comprador  podrá  suspender  el Pedido  o parte  de este  en cualquier  momento  mediante 

---

### Pagina 80
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
80/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 notificación  escrita  al Proveedor,  se estará lo dispuesto en la cláusula  49, indicando los 
motivos de la Suspensión Temporal. las Partes  suscribirán  un acta en la que quedará  
constancia  de las unidades  realizadas,  situación de  los Suministros  y cuantos  datos  se 
consideren  necesarios  para fijar la posición  respectiva de las Partes en el momento de la 
suspensión.  
El Proveedor  reanudará  su ejecución  en el más breve  plazo  posible y  no más tarde  de los 
diez (10) días siguientes  a la fecha  fijada  para su reanudación, según notificación escrita 
del Comprador.  Resueltas las causas que motivaron la suspensión temporal, se suscribirá 
igualmente  un acta de reanudación . 
 
El Proveedor tendrá derecho a que le sean abonados aquellos gastos directos que 
efectivamente se le hayan producido, necesarios para tomar las medidas precautorias 
anteriormente descritas . 
 
49. INCUMPLIMIENTO  POR  EL PROVEEDOR  
Se considerará  incumplimiento  del Proveedor:  
 
• Cualquier incumplimiento de sus obligaciones susceptible de afectar tanto a la calidad 
como a la conformidad del Pedido.  
• Cuando  no dé comienzo  a los trabajos  de acuerdo  con el programa  de fabricación.  
• Cuando  no asigne  a la ejecución  de los trabajos  a personal  con el grado  de 
especialización necesario o no  utilice materiales  y componentes  de la  calidad requerida.  
• La falta de cumplimiento  de la legislación  vigente.  
• La falta de cumplimiento  reiterado  de las instrucciones  del Comprador.  
• La negligencia  o abandono  en la ejecución  del Pedido.  
• El retraso  en la ejecución  del Pedido  que dé lugar  a un aplazamiento  inevitable  e 
injustificado del plazo de entrega.  

---

### Pagina 81
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
81/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 • La no entrega  de cualquiera  de las Boletas  de Garantías  requeridas.  
• La cesión  o subcontratación  de las obligaciones  del Pedido  sin la respectiva  autorización 
previa.  
 
El incumplimiento  será formalmente  manifestado  por el Proveedor,  instándole  a cumplir  con 
sus obligaciones  en un plazo  de 10 días.  El Proveedor  deberá  acusar  recibo  de la notificación 
e informar sin dilación alguna al Comprador sobre los efectos de su incumplimiento y las 
medidas de corrección que tenga intención de llevar a cabo para remediar dicho 
incumplimiento a la mayor brevedad.  
 
Si una vez recibida la notificación de incumplimiento del Comprador y transcurrido el plazo 
que se establece en la misma, el Proveedor no  pusiera remedio a dicho  incumplimiento, se 
entenderá que éste ha incurrido en incumplimiento contractual. En dicho supuesto, y sin 
perjuicio de la posibilidad de resolver o terminar anticipadamente el Pedido, el Comprador 
podrá:  
 
• Imponer su asistencia técnica al Proveedor, sin que ello suponga una exoneración 
de sus obligaciones y responsabilidades.  
 
• Sustituir al Proveedor, en la totalidad o en parte del Pedido, siendo dicha sustitución 
por cuenta  y riesgo  del Proveedor,  sin que el Pedido  pierda  validez.  En este caso  el 
Comprador podrá utilizar sus propios recursos para completar el indicado Pedido o 
subcontratar a un tercero para dicho fin.  
 
Todos los gastos en que incurra el Comprador a consecuencia del incumplimiento del 
Proveedor serán asumidos por éste, y podrán incrementarse en un 15% para cubrir los 
gastos generales administrativos que se generen. Las cantidades que procedan se 
descontarán de los importes que todavía pueda adeudar el Comprador al Proveedor 
correspondientes a la parte del Suministro que haya sido concluida de conformidad con el 
Pedido. También podrán recuperarse ejecutando las respectivas Boletas de Garantía.  

---

### Pagina 82
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
82/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 50. CANCELACIÓN  Y RESOLUCIÓN  DEL PEDIDO  
El Pedido  podrá  ser cancelado  total o parcialmente  por el Comprador  en cualquier  momento, 
mediante  notificación  escrita  al Proveedor.  Al recibir  esta notificación  el Proveedor  detendrá 
todo trabajo  relacionado  con el pedido  o con la parte  cancelada  y dará orden  inmediatamente 
a sub proveedores  y subcontratistas para cancelar los suministros y trabajos 
correspondientes. A partir de este momento, el Proveedor se limitará a hacer lo necesario 
para preservar y proteger los trabajos ya realizados.  
 
En un plazo de cinco (5) días desde la notificación de cancelación, el Proveedor deberá 
enviar al Comprador una relación detallada y completa de todos los Trabajos realizados y 
Suministros recibidos hasta el momento de la cancelación,  con evidencia y soporte  
documenta l detall ado, debiendo permitir la toma de posesión inmediata al Comprador de 
dichos Trabajos y Suministros.  
 
La cancelación por decisión unilateral del Comprador no dará derecho alguno al Proveedor 
a exigir indemnización alguna por daños y perjuicios; sin embargo, el Comprador estará 
obligado a abonar al Proveedor las facturas correspondientes a los trabajos realizados y 
suministros recibidos hasta el momento de producirse la cancelación, en la medida en que 
estos  trabajos  y suministros  se hayan  efectuado  de acuerdo  con el Pedido , y por lo tanto , las 
facturas  hayan  sido aprobadas.  De dicho  importe  se descontarán  los pagos  anticipados  y se 
abonarán las retenciones recibidas.  
El Comprador podrá resolver o terminar anticipadamente el Pedido, sin incurrir en ningún 
gasto  adicional,  cuando  el Proveedor  incumpla  cualquier  disposición  del Pedido  y/o anexos, 
o se produzca  alguna  de las circunstancias  que, a título  de ejemplo  y no de modo  limitativo, 
se relacionan a continuación:  
 
• En el supuesto  de un incumplimiento  contractual  del Proveedor  conforme  a lo establecido 
en la cláusula 49. 
 

---

### Pagina 83
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
83/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 • Cuando  el atraso respecto del P lazo de Entrega  del Suministro  exceda  de 30 días.  
 
• Cuando el monto previsible de multas acumuladas por parte del Proveedor exceda el 
15% del Monto Neto del Contrato u Orden de Compra.  
 
• Cuando  a juicio  del Comprador  y como  consecuencia  de las inspecciones  realizadas  por 
sus inspectores,  sea manifiesta  la incapacidad  del Proveedor  para suministrar  los equipos 
de acuerdo con las especificaciones del Pedido y en el plazo de entrega establecido.  
 
• El incumplimiento reiterado de sus obligaciones frente a terceros, que puedan estar 
relacionadas  con la fabricación  o suministro  de los equipos  o materiales  objeto  el Pedido.  
 
• Cuando  el Proveedor,  salvo  por condiciones  de Fuerza  Mayor , interrumpiera  la ejecución 
del encargo  durante más de quince (15) días  hábiles , incluso en periodos de tiempo no 
consecutivos.  
 
• La solicitud de liquidación del Proveedor a instancia de uno o más acreedores, la 
presentación por el Proveedor de solicitud de liquidación o si el Proveedor o uno o más 
de sus acreedores  formulan  proposiciones  de convenio  judicial  o extrajudicial  preventivo, 
o en caso de  dificultad  financiera  manifiesta  que impidan al  Proveedor atender el  normal 
cumplimiento de las obligaciones derivadas del Pedido.  
 
Una vez recibida la notificación de resolución de  Pedido por incumplimiento del Proveedor, 
este deberá cesar inmediatamente toda su actividad relacionada con el Pedido, o con la 
parte cancelada, y no realizará ningún otro pedido para la ejecución de Pedido.  
 
En el momento  que se  reciba por el Proveedor la notificación de la resolución del Pedido el 
Comprador quedará facultado para adoptar las medidas que sean precisas para prohibir el 
acceso a la Obra del Proveedor o sus empleados o representantes. El Proveedor no podrá 
sacar  ningún  material,  producto  terminado  ni equipo  sin autorización  expresa  del Comprador.  

---

### Pagina 84
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
84/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
La facultad de resolver el Pedido se entenderá sin perjuicio de cuantas otras acciones 
legales  puedan  corresponder  al Comprador,  quien  en todo caso  estará  facultado  para exigir 
la correspondiente indemnización por daños y perjuicios . La resolución de Pedido se 
producirá sin perjuicio del pago de las penalidades por retrasos en la entrega.  
 
El Comprador tiene el derecho, pero no la obligación de adquirir todos o algunos de los 
materiales que el Proveedor tuviese subcontratados, acopiados, fabricados en parte o 
entregados, fijándose el precio y las demás condiciones de esta adquisición de mutuo 
acuerdo o, si esto no se lograra mediante tasación pericial que se realizará en el plazo de 
sesenta  (60) días corridos  desde  la resolución  del Pedido.  En todos  los casos  de cancelación 
o resolución del Pedido, el Comprador queda eximido de cualquier reclamación que pueda 
hacer el Proveedor en relación con la parte del Pedido sin completar. No obstante, las 
estipulaciones del Pedido continuarán en pleno vigor y efecto en lo que se refiere al 
Suministro ejecutado con anterioridad a la fecha de cancelación o resolución, así como en 
relación a las restantes obligaciones señaladas en el Pedido que no dependan de la 
terminación completa de los Suministros.  
 
El Proveedor, en el plazo de 10 días desde la notificación entregará en todos los casos de 
resolución al Comprador toda la documentación, manuales, dibujos, planos, datos e 
información  específicos,  etc. que hubiera  preparado  en relación  al Pedido  hasta  la fecha  de 
cancelación.  El Proveedor  a petición  del Comprador  cederá  todos  los derechos  derivados  de 
los subpedidos que hubiera realizado en la relación con el Pedido resuelto.  
 
 
51. CONFIDENCIALIDAD  
Todos los documentos, planos, especificaciones, diseños, manuales, informes  y demás 
entregables  que entregue el Comprador al Proveedor en virtud de la petición de oferta y/o 
Pedido y cualquier documentación transmitida, e incluso el mismo Pedido, deben ser 
considerados confidenciales.  Por lo tanto,  el Proveedor  no deberá cederlos,  prestarlos  ni 

---

### Pagina 85
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
85/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 revelarlos  a terceros,  copiarlos,  ni darles  otro uso que el que se deriva del objeto para el que 
se le han facilitado, sin la previa autorización escrita del Comprador.  
 
 
52. PUBLICIDAD  
El Proveedor no tendrá derecho a hacer referencia al Pedido y lo acepta bajo la condición 
de no citarlo, anunciarlo ni utilizarlo con fines publicitarios sin la autorización previa de l 
Comprador.  
 
 
53. TRANSFERENCIA  DE TITULARIDAD  Y RIESGOS  
 
La propiedad (titularidad) de los equipos pasará al Comprador al momento de su 
Recepción Provisional, salvo acuerdo distinto por escrito entre las Partes.  
 
Sin perjuicio de lo anterior respecto a la transferencia de titularidad, la transferencia 
del riesgo de pérdida o daño de los materiales y/o equipos objeto del Pedido se 
regirá estrictamente por la regla Incoterms® 2020 EXW (Lugar convenido: 
instalaciones del Proveedor), definida en la Cláusula 3 3. Por lo tanto, el Proveedor 
asumirá dicho riesgo únicamente hasta el momento en que ponga los bienes a 
disposición de ADASA en el lugar convenido, momento a partir del cual el riesgo es 
asumido íntegramente por ADASA.  
 
En los subpedidos que curse el Proveedor como consecuencia del Pedido, deberá hacer 
constar que los materiales, componentes o equipos a entregar por los subproveedores o 
subcontratistas, no podrán ser sometidos a reserva de dominio, embargos u otros 
gravámenes, ni quedar vinculados al cumplimiento de cualesquiera garantías que obliguen 
al Comprador. Esta misma obligación la asume el Proveedor respecto a los Suministros por 
él realizados.  
 

---

### Pagina 86
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
86/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Si el Pedido tiene por objeto materiales o equipos cuyo montaje no haya sido confiado al 
Proveedor  pero éste haya  de supervisar,  la entrega  que el Proveedor  efectúe  en su momento 
se entenderá realizada a reserva de la Recepción Provisional por el Comprador, quedando 
ésta aplazada  hasta  que se haya  concluido  el montaje  de los materiales  o equipos  y puedan 
realizarse las pruebas definitivas en obra.  
 
 
54. DECLARACION  DEL PROVEEDOR  
Cuando el Comprador así  lo exija, el Proveedor entregará una declaración que  garantice  al 
Comprador que los equipos que conforman el Pedido están libres de cualquier posible 
reclamación o derecho de retención, procedente del Proveedor o de terceros, consignando 
especialmente que los equipos y/o materiales están libres de cargas o gravámenes por 
impuestos, tasas y demás cargas reales y/o sociales exigibles, y exentos de cualquier 
responsabilidad derivada de obligaciones laborales que afecten al Proveedor o a sus 
subcontratistas con sus trabajadores.  
 
Cuando así lo requiera el Comprador, el Proveedor deberá enviar con la factura final una 
declaración de finiquito, con excepción de las garantías, en términos aceptables para el 
Comprador.  
 
55. SOLUCIÓN DE CONTROVERSIAS  
 
55.1  SOLICITUDES Y RECLAMOS  
En caso que el Proveedor  considere que una orden o instrucción, acción, hecho o 
circunstancia que se aparte de las condiciones que establece el Contrato, le produce 
perjuicio o le da derecho al cobro de gastos adicionales, o al pago de alguna indemnización, 
o a variación de plazo, debe dar un aviso por escrito al Administrador del Contrato de 
ADASA de su intención de solicitar la correspondiente compensación, dentro de los 5 días 
siguientes, plazo que podrá prorrogarse por igual número de días corridos si lo solicita el 

---

### Pagina 87
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
87/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 Proveedor . Cumplido lo anterior, si persisten las condiciones que el Proveedo r considera que 
le afectan, éste deberá solicitar las compensaciones del caso, ciñéndose al siguiente 
procedimiento.  
 
55.2  SOLICITUD DE COMPENSACIÓN   
Una vez manifestada la voluntad de solicitar una compensación, el Representante del 
Proveedo r presentará al Administrador del Contrato dicha solicitud de compensación por 
escrito, con la descripción y fundamentos de los hechos o circunstancias que lo afectan. La 
presentación se debe hacer en un plazo máximo de 20 días, contados desde la ocurrencia 
de la acción, hecho o circunstancia que le afecta. Pasado este plazo, caducará el derecho 
para solicitar las compensaciones.  
 
55.3  RECLAMOS Y ARBITRAJE  
Se entenderá por “reclamo” la solicitud formal de compensación económica y/o aumento de 
plazos, presentada por el Proveedor  a ADASA frente a una acción, hecho o circunstancia 
que, a juicio del afectado, se aparta de lo previsto en el Contrato, tiene consecuencias 
desfavorables para él y no ha podido ser resuelta entre el Administrador de Contrato y el 
Representante del Proveedor , procediéndose a su formalización mediante una modificación 
del Contrato de acuerdo al procedimiento descrito en las presentes Bases Administrativas.  
El tratamiento de los reclamos estará sujeto a las reglas que se indican en los literales 
siguientes,  
a.  Todo reclamo debe ser presentado por escrito, esto es, en soporte papel, al 
Administrador del Contrato de ADASA, firmado tanto por el Representante del 
Proveedor  como por su representante legal, o adjuntando la autorización por escrito de 
este último, cuando ocurra cualquiera de las siguientes circunstancias, en los plazos 

---

### Pagina 88
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
88/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 que se indican a continuación:  
• Dentro de 20 días, contados desde la fecha en que el Administrador de Contrato 
de ADASA comunica por escrito al Proveedor  una respuesta a una solicitud de 
compensación, que a este último no le satisface.  
• A partir de los 31 días, y hasta los 50 días, contados desde la fecha en que el 
Proveedor  presenta por escrito una solicitud de compensación al Administrador de 
Contrato de ADASA, sin que éste último haya entregado su respuesta por escrito 
al Proveedor .  
 
El hecho que el Proveedor  no presente formalmente sus reclamos, en los términos y 
dentro del plazo indicado, caducará su derecho  e implicará que el Proveedor  otorga 
su plena conformidad en la forma en que se ha administrado el Contrato y de la 
suficiencia de los pagos.  
 
b.  La presentación del reclamo debe incluir todos los antecedentes del caso, 
incluyendo, a lo menos:  
• La información necesaria para conocer de manera completa y objetiva los 
fundamentos y alcances del reclamo, en particular, si se trata de un hecho 
puntual o que persiste en el tiempo  
• Las disposiciones contractuales en que se apoya y las circunstancias que 
originan el reclamo  
• La documentación de respaldo probatoria que justifique la procedencia y 
magnitud de lo reclamado y  
• La designación de hasta 3 personas, incluyendo al Representante del 
Proveedor , o quien el representante legal del Proveedor  designe en su 

---

### Pagina 89
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
89/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 reemplazo, que en forma conjunta representarán a dicho Proveedor  en esta 
instancia.  
c.  Dentro de los siguientes 10 días, contados desde la recepción del reclamo por el 
Administrador del Contrato ADASA, éste citará por escrito al Representante del 
Proveedor  para que concurra con las personas previamente designadas a una 
primera reunión, que deberá efectuarse dentro de los primeros 30 días de recibido el 
reclamo, con el fin de constituir una Mesa de Resolución de Reclamos (MRR) en que 
se aborde el tema.  
 
En esta primera reunión, la MRR deberá acordar, a lo menos, su metodología de 
trabajo, el representante líder de cada parte, la periodicidad y lugar de sus reuniones 
y sus quórum de funcionamiento, acuerdos que deberán además constar en actas 
suscritas por los miembros de la Mesa, las que serán obligatoriamente respaldadas 
por vía electrónica y cargadas en un repositorio ad -hoc definido por ADASA.  
 
Por su parte, a lo menos 7 días antes de la reunión referida, el Administrador de 
Contrato de ADASA informará por escrito al Representante del Proveedor , la nómina 
de personas, de hasta 3, incluyendo al mismo Administrador de Contrato o quien 
ADASA designe en su reemplazo, que representarán a ADASA en esta instancia.  
 
d.  La MRR tendrá la misión de elaborar dentro de un plazo máximo de 60 días a contar 
de la fecha de su constitución, una propuesta común de acuerdo, la que quedará 
sujeta a la ratificación de los representantes legales de cada parte. Dicho plazo podrá 
ser prorrogado de común acuerdo hasta por una vez, por 30 días adicionales.  
e.  Si la MRR lo estima conveniente, podrá acordar la designación de un perito 
especialista, para participar como moderador en las reuniones de la Mesa y hacer 
recomendaciones, o bien, para presentar un informe no obligatorio para las partes, 
sobre la base de lo observado durante el funcionamiento de la MRR.  

---

### Pagina 90
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
90/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 f.  La ratificación del acuerdo, cuando se produzca, se formalizará mediante una 
modificación del Contrato suscrito entre las partes, para lo cual se dispondrá de un 
plazo adicional de 30 días, periodo que constituirá una obligación contractual para 
ambas partes.  
g.  Sólo si se vence el plazo de que dispone la MRR sin que ésta logre una propuesta de 
acuerdo, o si se vence el plazo para elaborar la correspondiente modificación de 
Contrato, según lo indicado en el punto anterior, la parte interesada estará liberada 
para ejercer, si lo estima conveniente, su derecho a recurrir al arbitraje.  
 
h.  Durante el transcurso del proceso de reclamo, el Proveedor  deberá seguir 
ejecutando los trabajos o prestando los servicios objeto del contrato en forma normal. 
Además, deberá entregar al Administrador del Contrato de ADASA, un informe 
detallado de los recursos (mano de obra, equipos, maquinarias, etc.) utilizado en las 
actividades que está llevando a cabo el Proveedor  y que han dado origen a dicho 
reclamo. El Administrador de Contrato de ADASA podrá liberar al Proveedor  de dicha 
obligación, si por la naturaleza del reclamo no es aplicable el control diario de 
recursos utilizados.  
 
i.  Los costos de especialistas, peritos o asesores, entre otros, asumidos por ADASA 
para la defensa de un reclamo infundado o que no cumple los requisitos básicos 
indicados en la letra b. de este numeral, serán de exclusiva responsabilidad del 
Proveedor . Por su parte, ADASA será responsable en los mismos términos recién 
indicados, en caso que  rechace un reclamo sin causa justificada o si, en definitiva, 
acoge la totalidad del reclamo.  
 
Sólo después de agotados todos los recursos previstos para el tratamiento de solicitudes y 
reclamos, las controversias que puedan subsistir entre las Partes con motivo de la validez, 
aplicación, cumplimiento, interpretación o terminación del Contrato, o por cualquier causa, 

---

### Pagina 91
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
91/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 sin limitación, podrán ser sometidas al procedimiento de solución de controversias por la 
vía judicial que se describe a continuación:  
 
Cualquier dificultad o controversia que se produzca entre los contratantes respecto de la 
aplicación, interpretación, duración, validez o ejecución del Contrato o cualquier otro motivo 
será sometida a arbitraje, conforme al Reglamento Procesal de Arbitraje del Centro de 
Arbitraje y Mediación de Santiago, vigente al momento de solicitarlo.  
 
Las partes confieren poder especial irrevocable a la Cámara de Comercio de Santiago 
A.G., para que, a petición escrita de cualquiera de ellas, designe a un árbitro arbitrador en 
cuanto al procedimiento y de derecho en cuanto al fallo, de entre los integrantes del cuerpo 
arbitral del Centro de Arbitraje y Mediación de Santiago.  
 
En contra de las resoluciones del árbitro no procederá recurso alguno. El árbitro queda 
especialmente facultado para resolver todo asunto relacionado con su competencia y/o 
jurisdicción.  
 
El lugar del proceso será la ciudad de Santiago de Chile, área de jurisdicción de la Corte 
de Apelaciones de Santiago, Chile.  
 
Las partes renuncian desde ya a las tachas contempladas en los números 4 y 5 del artículo 
358 del Código de Procedimiento Civil, relativas a la inhabilidad del testigo por su 
dependencia laboral de la parte que lo presenta.  
 
56. MEDIO  AMBIENTE  
El Proveedor  cumplirá  con la legislación  medioambiental  vigente,  siendo  responsable  directo 
de las repercusiones medioambientales perjudiciales que pueda originar con su trabajo, a 
través  de sus residuos,  emisiones  a la atmósfera  por sus equipos  o vertidos,  y manteniendo 
al Comprador indemne de cualquier posible responsabilidad que contra ellos pueda 

---

### Pagina 92
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
92/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 derivarse por las acciones u omisiones del Proveedor.  
 
El Proveedor estará obligado a presentar al Comprador todas las evidencias del 
cumplimiento legal de los requisitos de aplicación que le sean solicitados.  
 
El Proveedor  está obligado  a cumplir  todos  los requisitos  y disposiciones  legales  en materia 
de Medio Ambiente, siendo responsable de la puesta en práctica de estas, así  como de las 
consecuencias  que se deriven  de su incumplimiento,  tanto  en lo que se refiere  a la actividad 
por él subcontratada como a la que, a su vez subcontrate con terceros.  
 
El Proveedor  deberá  cumplir  los procedimientos  y los protocolos  del Comprador  que le sean 
aplicables, para lo cual se les hará llegar copia de los documentos oportunos.  
 
El Comprador no aceptará ninguna reclamación del Proveedor por pérdidas de tiempo 
debidas  a posibles  interrupciones  del trabajo,  como  consecuencia  del cumplimiento  por parte 
del mismo, de la Legislación Ambiental.  
 
El incumplimiento por parte del Proveedor de sus obligaciones en materia ambiental, 
facultará  al Comprador  a la imposición  de una penalización  hasta  un límite  máximo  del 110% 
de la Sanción impuesta por Organismos Oficiales y/o Autoridad Ambiental Competente. En 
caso  de reiteración,  se podrán  retener  los pagos  y certificaciones  en curso  e incluso  resolver 
el contrato  sin que el Proveedor  tenga  derecho  a indemnización  alguna,  independientemente 
de los daños y perjuicios que el Comprador pudiese reclamar.  
 
57. LÍMITE DE RESPONSABILIDAD  
 
 
El límite de responsabilidad del Proveedor para con ADASA, emanad o del Contrato, por 
todas y cualquiera causa y/o naturaleza, sea que se devenguen a título de multas, 
compensaciones, indemnizaciones, penas, o sanciones, se fija en un monto equivalente al 

---

### Pagina 93
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
93/94 BASES  ADMINISTRATIVAS  ESPECIALES   
 25% del valor neto del Contrato u Orden de Compra,  más sus modificaciones, si las 
hubiere . Se exceptúan de este límite de responsabilidad los siguientes conceptos:  
 
- Los costos de rehacer los servicios  y/o trabajos deficientes y la Garantía Técnica o de 
Desempeño del Equipo .  
- Pago a las instituciones de previsión social que se cobren a ADASA por deudas del 
Proveedor , sus subcontratistas y/o proveedores.  
- Deudas del Proveedor  y/o de sus subcontratistas, con terceros, que se pretendan 
cobrar mediante demanda judicial.  
- Daños a terceros causados por el Proveedor  y/o sus subcontratistas, que se pretendan 
cobrar mediante demanda judicial.  
- Deudas del Proveedor  y/o de sus subcontratistas en que exista responsabilidad 
subsidiaria de ADASA.  
Ninguna parte ser á́ responsable ante la otra por daños indirectos o consecuenciales, como 
la pérdida de beneficios o lucro cesante.  
 
El límite de responsabilidad y la exclusión de responsabilidad por daños indirectos o 
consecuenciales, no se aplicarán en caso de fraude, culpa grave o dolo del Proveedor  y/o 
sus dependientes.  
 
58. RESPONSABILIDAD  PENAL  EMPRESARIAL  
 
El Comprador  deberá  respetar  las disposiciones legales vigentes aplicables a la  realización 
de sus labores.  En especial,  todo trabajador  o dependiente  deberá  abstenerse  de cometer  o 
participar, de cualquier manera,  en la comisión de alguno de los siguientes delitos:  
 
• Lavado  de activos,  contemplado  en el artículo  27 de la Ley N° 19.913;  
• Financiamiento  del terrorismo,  establecido  en el artículo  8 de la Ley N° 18.314;  y 
• Delitos  de cohecho  previstos  en los artículos  250 y 251 bis del Código  Penal.  
 

---

### Pagina 94
---
12803 SUMINISTRO  Módulo  RO Segunda Etapa para  Salmuera  - PD Taltal” 
94/94 BASES  ADMINISTRATIVAS  ESPECIALES   
  
Las jefaturas  y los trabajadores  o dependientes  deberán  ejercer  el control  sobre  el personal 
bajo su subordinación, procurando evitar que quienes estén bajo su supervisión cometan o 
participen de  cualquier  modo en  la comisión de los delitos  mencionados  en la letra  anterior.  
 
Todo trabajador o dependiente del Comprador tendrá la obligación de informar a ADASA 
respecto de cualquier acto o conducta que pueda ser constitutiva de alguno de los delitos 
antes mencionados.  
 
Adicionalmente, el Comprador y sus dependientes deben respetar la Ley N°  20.393. Y 
cumplir con el Manual de Prevención del delito de Aguas de Antofagasta S.A.  
 


================================================================================
## 6. ET MODULO (P22-ET-09-000-001-0) — TEXTO COMPLETO
================================================================================
# P22-ET-09-000-001-0 - Especificacion Tecnica Modulo RO Segunda Etapa

## Metadatos
- **Archivo origen**: P22-ET-09-000-001-0 (ET Módulo).pdf
- **Paginas**: 41
- **Fecha extraccion**: 2025-11-25

---

## Contenido Extraido


---

### Pagina 1
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  1 de 41 
 
 
  
  
 
 
 
Especificación técnica  
Módulo RO Segunda Etapa para Salmuera – PD Taltal  
P22-ET-09-000-001 
 
 
Antofagasta, abril  2025 
 
 
 
 
 
 
 
0 24/04/2025  F. Salato  L. Hughes  L. Hughes   
B 17/04/2025  F. Salato  L. Hughes  L. Hughes   
A 31/03/2025  F. Salato  L. Hughes  L. Hughes   
Rev.  Fecha  Preparado Por  Revisado Por  Aprobado Por  Cliente  
 
 


---

### Pagina 2
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  2 de 41 
 
 
  
 TABLA DE CONTENIDOS  
1 INTRODUCCIÓN  ................................ ................................ ................................ ........................  5 
1.1 OBJETIVO  ................................ ................................ ................................ ...........................  5 
1.2 ALCANCE  ................................ ................................ ................................ ............................  5 
2 DESCRIPCIÓN DEL PROYECTO  ................................ ................................ .............................  5 
3 ALCANCE DEL ENCARGO  ................................ ................................ ................................ ...... 7 
4 CALIDAD AGUA DE MAR, CANTIDAD Y CALIDAD DE PERMEADO  ................................ .. 7 
4.1 Calidad de la salmuera de alimentación  ................................ ................................ .............  7 
4.2 Requerimientos de Cantidad Permeado  ................................ ................................ .............  8 
4.3 Requerimientos de Calidad del Permeado  ................................ ................................ .........  8 
4.4 Condiciones Sísmicas  ................................ ................................ ................................ .........  9 
5 CARÁCTERISTICAS DE LA PLANTA MODULAR  ................................ ................................ . 9 
5.1 Especificación de los equipos electromecánicos principales  ................................ ...........  10 
5.1.1  Bomba de Alta Presión  ................................ ................................ ................................ . 10 
5.1.2  Turbo 1°Etapa  ................................ ................................ ................................ ...............  10 
5.1.3  Turbo 2°Etapa  ................................ ................................ ................................ ...............  11 
5.1.4  Bomba de lavado CIP  ................................ ................................ ................................ ... 11 
5.1.5  Filtros cartucho  ................................ ................................ ................................ .............  12 
5.1.6  Tubos de Presión ................................ ................................ ................................ ..........  12 
5.1.7  Membranas de osmosis inversa ................................ ................................ ...................  13 
5.1.8  Bomba dosificadora  ................................ ................................ ................................ ...... 13 
5.1.9  Bastidor Soporte  ................................ ................................ ................................ ...........  13 
5.1.10  Contenedor  ................................ ................................ ................................ .................  14 
5.1.11  Servicios Auxiliares  ................................ ................................ ................................ .... 15 
5.2 Especificación de materiales de cañerías y válvulas  ................................ .......................  16 
5.2.1  Cañerías de baja presión  ................................ ................................ .............................  16 
5.2.2  Cañerías de alta presión  ................................ ................................ ..............................  16 
5.2.3  Actuadores  ................................ ................................ ................................ ....................  17 
5.3 Especificación de motores eléctricos  ................................ ................................ ................  18 
5.4 Especificación de tableros de fuerza y control  ................................ ................................ . 18 
5.4.1  Características constructivas  ................................ ................................ .......................  20 

---

### Pagina 3
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  3 de 41 
 
 
  
 5.4.2  Características eléctricas  ................................ ................................ .............................  20 
5.4.3  Terminaciones  ................................ ................................ ................................ ..............  21 
5.4.4  Protecciones eléctricas  ................................ ................................ ................................ . 21 
5.4.5  Alambrado y regletas  ................................ ................................ ................................ .... 21 
5.4.6  VDF’s  ................................ ................................ ................................ ............................  22 
5.4.7  Voltajes y frecuencia que considerar  ................................ ................................ ...........  23 
5.5 Especificación de instrumentación  ................................ ................................ ....................  23 
5.5.1  Caudalímetros  ................................ ................................ ................................ ..............  23 
5.5.2  Manómetros  ................................ ................................ ................................ ..................  24 
5.5.3  Transmisores de presión  ................................ ................................ ..............................  24 
5.5.4  Sensores de nivel  ................................ ................................ ................................ .........  24 
5.5.5  Conductímetro  ................................ ................................ ................................ ..............  24 
5.5.6  Transmisores de Vibración:  ................................ ................................ ..........................  25 
5.6 Límites de suministro  ................................ ................................ ................................ ........  25 
6 DOCUMENTACIÓN QUE PRESENTAR EN LA PROPUESTA  ................................ .............  26 
7 INGENIERÍA Y DOCUMENTACIÓN QUE DESARROLLAR DURANTE EL ENCARGO  ..... 27 
8 INSPECCIONES DURANTE LA FABRICACIÓN  ................................ ................................ ... 30 
8.1 Alcance Mínimo de Pruebas de Aceptación en Fábrica (FAT)  ................................ ........  31 
9 COMISIONAMIENTO Y PUESTA EN MARCHA  ................................ ................................ .... 33 
10 GARANTÍAS  ................................ ................................ ................................ ............................  34 
10.1  Parámetros de desempeño a garantizar  ................................ ................................ ..........  34 
10.1.1  Capacidad Nominal  ................................ ................................ ................................ .... 34 
10.1.2  Calidad del Agua Producto Que Garantizar  ................................ ..............................  34 
10.1.3  Consumo Específico de Energía Eléctrica Garantizado  ................................ ...........  35 
10.2  Pruebas de Desempeño  ................................ ................................ ................................ ... 35 
10.2.1  Prueba de la Capacidad Nominal de Producción  ................................ ......................  35 
10.2.2  Pruebas de calidad del agua producto  ................................ ................................ ...... 35 
10.2.3  Prueba del Consumo Específico de Energía Eléctrica ................................ ..............  36 
11 ANEXO I – Caracterización de salmuera  ................................ ................................ .............  37 
12 ANEXO II – PFD Proyecto Base  ................................ ................................ ............................  38 
13 ANEXO III – P&ID´s proyecto base  ................................ ................................ .......................  39 

---

### Pagina 4
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  4 de 41 
 
 
  
 14 ANEXO IV – Planos de arreglo mecánico/cañerías del proyecto base  ............................  40 
15 ANEXO V – 3D proyecto base  ................................ ................................ ...............................  41 
 
ÍNDICE DE FIGURAS  
Figura 2 -1 UBICACIÓN DEL PROYECTO  ................................ ................................ .....................  6 
 
ÍNDICE DE TABLAS  
Tabla 4 -1 CALIDAD DE LA SAMUERA DE ALIMENTACIÓN  ................................ .......................  8 
Tabla 4 -2 REQUERIMIENTOS  DE CALIDAD  DEL PERMEADO  ................................ ..................  8 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 5
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  5 de 41 
 
 
  
 1 INTRODUCCIÓN  
La localidad de Taltal cuenta con tres plantas desaladoras de tipo modular instaladas en las 
inmediaciones de su agencia zonal, las cuales utilizan agua de mar captada a través de pozos 
para producir hasta 1 4 L/s d e agua potable.  
Aguas de Antofagasta (ADASA) requiere  aumentar la capacidad instalada en la localidad, para 
lo cual planea incorporar una nueva planta modular que tratará la salmuera del último de los tres 
módulos instalados (módulo 3), que actualmente genera como subproducto 49 m3/h de salmuera.  
Esta nueva planta modular de tratamiento de salmuera tratar á los 49 m3/h de salmuera residual 
de manera tal de lograr un incremento de producción de agua  permeada de 20 m3/ h adicionales  
para su posterior  Re-mineralización  y potabilización en la infraestructura existente . El nuevo 
módulo requiere diseñar las instalaciones de interconexiones de tuberías, bombas intermedias y 
estanques para la integración de este  dentro del espacio disponible de manera tal de cumplir con 
los requerimientos de producción de agua potable en cantidad y calidad.  
1.1 OBJETIVO  
El objetivo del presente documento es especificar técnicamente  para compra  la nueva planta 
modular de tratamiento de salmuera que tratará los 49 m3/h de salmuera residual de l módulo 3 
actualmente en operación, de  manera tal de lograr un incremento de producción de permeado 
de 20 m3/ h adicionales . 
1.2 ALCANCE  
El alcance de este documento comprende la especificación de los componentes de la planta 
modular de tratamiento de salmuera  que se encontrarán dentro de  un contenedor , comprendidos 
entre el flange de alimentación de agua salmuera  a tratar , hasta los flanges de entrega de 
permeado y de rechazo incluyendo filtros cartucho, bomba de alta presión, sistema de 
recuperación de energía, tubos de presión, membranas, cañerías e instrumentos, sistema de 
control  junto con su lógica de control , tableros de fuerza y control  para la interconexión con la 
alimentación en sitio , incluyendo además el sistema de lavado CIP.  
También se especifican actividades como la ingeniería asociada a la planta modular como así 
también la construcción del propio módulo, la supervisión d el montaje y la puesta en marcha de 
la instalación.  
2 DESCRIPCIÓN DEL PROYECTO  
El Módulo RO Segunda Etapa para Salmuera – PD Taltal , con templa el diseño e instalación de 
una nueva planta desaladora modular de tratamiento de salmuera para reaprovechar salmuera 
residual  disponible  e incrementar la capacidad de producción de agua desalada de la ciudad de 
Taltal en 20 m3/h . En la figura 2-1 se puede observar la ubicación del proyecto.  

---

### Pagina 6
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  6 de 41 
 
 
  
  
FIGURA 2-1 UBICACIÓN DEL PROYECTO  
 
La salmuera para desalar  se obtendrá del módulo 3 actualmente en operación, el cual abastecerá 
un estanque de salmuera con 49 m3/h. Luego una bomba de alimentación de salmuera enviará 
el agua desde el estanque de salmuera hacia la planta modular de tratamiento de salmuera . 
La planta modular de tratamiento de salmuera tendrá dos etapas de desalación de ultra alta 
presión y se instalará sobre una s bases de concreto construida s para tal fin, dentro de un 
contenedor  el cual deberá caber en el espacio reservado para tal fin  siendo este de 1 3 metros  
de largo por 2,5 metros ancho . 
La misma contará con un sistema de filtrado a través de filtros cartucho para protección de las 
membranas de osmosis inversa. Antes del arribo de la salmuera al filtro cartucho, se efectuará 
la inyección de anti -incrustante para evitar la precipitación de sales dentro de las membranas de 
osmosis inversa.  
Luego, la salmuera filtrada se irá hacia una bomba de alta presión, que elevará la presión de la 
salmuera pretratada, alimentando posteriormente a la unidad turbocharger de la primera etapa, 
que elevará la presión hasta aquella requerida por el proceso de desalación de la primera etapa, 
para alimentar las membranas de ósmosis inversa, que se alojarán en tubos de presión de PRFV 
de 8 pulgadas y 7 elementos.  El permeado producido en la primera etapa se enviará hacia el 
sistema de postratamiento existente con la presión residual del mismo , donde  se le dosificará 
hipoclorito de sodio y fluorsilicato de sodio para acondicionamiento final. El agua producto se 
enviará presurizada hacia los estanques de agua producto a partir de los cuales se bombeará el 
fluido al sistema de distribución de agua de la ciudad de Taltal  
PROYECTO  

---

### Pagina 7
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  7 de 41 
 
 
  
 El rechazo generado en la primera etapa se enviará al turbocharger de la segunda etapa el cual 
elevará la presión hasta aquella requerida por el proceso de desalación de la primera etapa para 
alimentar las membranas de osmosis inversa que se alojarán en tubos de presión de PRFV de 8 
pulgadas y 7 elementos de  la segun da etapa . El permeado producido en la segunda etapa se 
enviará hacia el sistema de postratamiento existente junto con el permeado de la primera.  
La otra corriente de rechazo generada en la segunda etapa que posee una alta presión residual 
será enviada al sistema de recuperación de energía compuesto por dos turbocharger  ubicados 
en la alimentación de la primera y segunda etapa. Estas unidades tomará n la presión residual de 
del rechazo y se la transferirá n a la corriente parcial de las salmueras de alimentación de cada 
una de las dos etapa s. 
Para efectuar los lavados periódicos de las membranas, la planta modular de tratamiento de 
salmuera constará con un sistema de lavado CIP provisto de una bomba de lavado y un estaque 
de agua de lavado , un filtro cartucho, con sus correspondientes cañerías, válvulas e 
instrumentación.   
3 ALCANCE DEL ENCARGO  
El Encargo para ejecutar  por el Proveedor , corresponde a entregar ADASA una planta modular 
de tratamiento de salmuera a suma alzada.  
Dentro de las actividades generales que comprende el Encargo, se encuentran todas aquellas 
necesarias para el desarrollo de la ingeniería de detalles, la adquisición y suministro de los 
equipos, materiales y herramientas, construcción de la planta  y entrega Ex Works.  
Respecto a las tareas de montaje en sitio , estas serán ejecutadas por ADASA  y el 
comisionamiento y  puesta en marcha  serán de acuerdo al punto 9 de este documento y la BAE 
Clausula 40.  
Además, el Proveedor  deberá considerar el entrenamiento del personal de ADASA que operará 
la planta  en sitio durante un  periodo de tres semanas.  
4 CALIDAD AGUA DE MAR, CANTIDAD Y CALIDAD DE PERMEADO  
4.1 Calidad de  la salmuera de alimentación  
Se presentan en el Anexo I los datos de calidad de  la salmuera de alimentación obtenidos en 
dos muestreos puntuales realizados para establecer las características de la salmuera  del 
módulo 3 , tanto en su contenido de sales como materia en suspensión y temperatura.  
El diseño del sistema deberá considerar dichos parámetros como base para la selección de 
materiales, configuración hidráulica y condiciones operativas.  
El diseño de l a planta modular de tratamiento de salmuera deberá permitir al menos la variación 
de los parámetros de calidad de la salmuera de alimentación que se indican a continuación , en 
los rangos que se señalan:  

---

### Pagina 8
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  8 de 41 
 
 
  
 Concepto  Unidad  Mínimo  Máximo  
Sólidos  Totales  Disueltos  (TDS)  mg/l  43.000  53.000  
Temperatura  °C 19 24 
Sólidos  Suspendidos  (SS) mg/l  0,4 1 
Turbiedad  NTU  0,4 1 
TABLA 4-1 CALIDAD DE  LA SAMUERA DE ALIMENTACIÓN  
 
El diseño del Proveedor  deberá incorporar instrumentación en la línea de alimentación del 
módulo, incluyendo al menos un caudalímetro y un conductímetro, para validar las condiciones 
de calidad y cantidad de la salmuera de ingreso. La relación entre conductividad y TDS será 
acordada con el Comprador  durante la etapa de revisión de ingeniería. Esta información deberá 
almacenarse de forma continua y trazable, de manera de permitir su revisión posterior y respaldar 
el cumplimiento de las garantías operativas establecidas en el Apart ado 10 de este documento.  
4.2 Requerimientos de Cantidad Permeado  
La planta modular de tratamiento de salmuera deberá entregar una producción diaria mínima de 
permeado de 480 m3/día  correspondiente a un caudal de 20 m3/h  de permeado. Por tratarse de 
una planta modular se aceptan capacidades mayores si es que los oferentes poseen soluciones 
estandarizadas de mayor caudal de hasta un 5% superior del caudal definido en la presente 
especificación.  
Por otro lado, no se aceptarán plantas de capacidades menores a las que haya que llevarlas 
sobre su capacidad nominal para lograr el objetivo de producció n. 
La producción de permeado se deberá lograr con la alimentación de 1.176 m3/día de salmuera 
de alimentación.  
4.3 Requerimientos de Calidad del Permeado  
Los requerimientos de calidad para el permeado de la planta modular de tratamiento de salmuera 
se indican en el cuadro siguiente:  
Parámetro  Unidad  Valor  
Sólidos  Totales  Disueltos  mg/l  < 500 
Cloruros  mg/l  < 400 
TABLA 4-2 REQUERIMIENTOS  DE CALIDAD  DEL PERMEADO  
 
 

---

### Pagina 9
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  9 de 41 
 
 
  
 4.4 Condiciones Sísmicas  
Todos los componentes internos y la envolvente del módulo serán diseñadas y construidas para 
resistir de forma continuada la máxima carga que pueda ocurrir bajo todas las condiciones de 
operación, incluido el sismo. Las estructuras del módulo (bastidor/con tenedor) y los anclajes de 
los equipos principales internos deberán ser diseñadas y construidas para soportar sismos según 
la Norma Sísmica de Chile NCh 2369, para Zona 3.  
Las fuerzas se aplicarán al centro de gravedad de los equipos y el peso considerado será el peso 
en funcionamiento. (El cumplimiento de este requisito deberá ser verificado mediante una 
memoria de cálculo específica, detallada en la Sección 7 de este documento ). 
 
5 CARÁCTERISTICAS DE LA PLANTA MODULAR  
ADASA ha desarrollado un proyecto base referencial para la  instalación de la planta modular  de 
tratamiento  de salmuera cuyo P&ID se puede apreciar en el anexo de la presente especificación , 
compuesto de:  
• Diagrama PFD . 
• Diagramas P&ID´s . 
• Planos de arreglo mecánico y cañerías . 
La planta modular de tratamiento de salmuera tendrá dos etapas de desalación de ultra alta 
presión dentro de un contenedor hasta 13 metros  de largo , con una capacidad de producción de 
permeado mínima de 20 m3/h , trabajando con una conversión mínima del 50 % por lo que la 
planta será alimentada con un flujo máximo de 49 m3/h de salmuera obtenida a través de una 
bomba de alimentación de salmuera.  
Dentro del contendedor se encontrarán instalados todos sus componentes siendo estos: bomba 
de alta presión, sistema de recuperación de energía, tubos de presión, membranas de osmosis 
inversa, sistema de limpieza CIP, sistema de dosificación de cañerías, válvulas e 
instrumentación. Todos estos elementos pueden observarse en el P&ID en anexo.  
En el proyecto base, el sistema de recuperación de energía adoptado consiste dos recuperadores 
de energía del tipo turbocharge r instalados en cada una de las  dos etapas . Con respecto a esta 
solución en particular , se aceptan también soluciones alternativas si el proponente así lo 
considera con su debida justificación  técnica en la propuesta , siempre y cuando se cumpla con 
las limitaciones de producción de caudal de permeado mínimo, eficiencia energética y 
dimensiones máximas de la planta indicadas en esta e specificación técnica.  La metodología para 
la evaluación técnica y económica de dichas alternativas por parte de ADASA se detalla en las 
Bases Administrativas Especiales (BAE).  

---

### Pagina 10
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  10 de 41 
 
 
  
 A continuación, se entregan las especificaciones de los componentes principales de la planta 
desaladora modular.  
5.1 Especificación de los equipos electromecánicos  principales  
5.1.1  Bomba de Alta Presión  
Tipo  Desplazamiento  positivo  o centrífuga  multietapa  
Fluido  Salmuera  filtrada  a temperatura  Ambiente  
Caudal  49 m3/h 
TDH Por proveedor  
Material  voluta  Acero  inoxidable  Super  Duplex  PREN  > 40 
Material  impulsor  Acero  inoxidable  Super  Duplex  PREN  > 40 
Tensión/frecuencia  3 x 380 V/50  Hz 
Potencia  estimada  Por proveedor  
Protección/aislación  IP55/clase  B 
Tipo  de Arranque  Variador  de Frecuencia  
Instrumentación  RTDs a 3 hilos para temperatura de rodamientos  
 
5.1.2  Turbo 1°Etapa  
Tipo  Turbocargador  
Fluido  Salmuera  filtrada  a temperatura  Ambiente / Rechazo 2° etapa  
Caudal  1 49 m3/h 
Caudal 2  Por proveedor  
TDH Por proveedor  
Material  voluta  Acero  inoxidable  Super  Duplex  PREN  > 40 
Material  impulsor  Acero  inoxidable  Super  Duplex  PREN  > 40 
Tensión/frecuencia  - 

---

### Pagina 11
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  11 de 41 
 
 
  
 Potencia  estimada  - 
Protección/aislación  - 
Tipo  de Arranque  - 
 
5.1.3  Turbo 2°Etapa  
Tipo  Turbocargador  
Fluido  Salmuera  filtrada  a temperatura  Ambiente / Rechazo 2° etapa  
Caudal 1   Por proveedor  
Caudal 2  Por proveedor  
TDH Por proveedor  
Material  voluta  Acero  inoxidable  Super  Duplex  PREN  > 40 
Material  impulsor  Acero  inoxidable  Super  Duplex  PREN  > 40 
Tensión/frecuencia  - 
Potencia  estimada  - 
Protección/aislación  - 
Tipo  de Arranque  - 
 
5.1.4  Bomba de lavado  CIP 
Tipo  Centrífuga  Vertical  
Fluido  Soluciones  básicas  y ácidas  para  limpieza  CIP de membranas  
Caudal  Por proveedor  
TDH Por proveedor  
Material  voluta  AISI 316 
Material  impulsor  AISI 316 
Tensión/frecuencia  3 x 380 V/50  Hz 

---

### Pagina 12
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  12 de 41 
 
 
  
 Potencia  estimada  Por Proveedor  
Protección/aislación  IP55/clase  B 
Tipo  de Arranque  Partida  directa  
Instrumentación  RTDs a 3 hilos para rodamientos  
 
5.1.5  Filtros cartucho  
Tipo  Cartuchos  descartables  
Cantidad  de carcasas  1 
Caudal  de operación  Por Proveedor  
Material  Plástico  
Presión  de trabajo  máxima  10 bar 
Tipo  de cierre  Rápido  
Conexiones  proceso  Flangeadas  Tipo  ANSI  B 16.5  Cl 150 
Retención  1 micr ón 
Longitud  de cada  Cartucho  40” 
Diámetro  2,5” 
 
5.1.6  Tubos de Presión  
Marca  PROTEC  o similar  
Material  PRFV  
Dimensiones  Para  alojar  7 membranas  de 8”  
Cantidad  1° Etapa   Por proveedor  
Cantidad 2° Etapa   Por proveedor  
 Presión  1800 psi para UHPRO  
Puertos   Single Port y/o Multi Port  
 

---

### Pagina 13
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  13 de 41 
 
 
  
 5.1.7  Membranas de osmosis inversa  
Marca  DUPONT , HYDRANAUTICS,  LG 
Modelo  Por proveedor  
Tipo  Poliamida,  espiral  
Diámetro  8” 
Longitud  40” 
Cantidad  Por proveedor  
5.1.8  Bomba dosificadora  
Marca  Grundfos, Milton Roy  
Modelo  Por proveedor  
Tipo  Membrana  
 
5.1.9  Bastidor Soporte  
El sistema de filtración, sistema de bombeo de alta presión, sistema de recuperación de energía 
y el banco de membranas, se deberán montar integrados en un solo Skid soporte construido en 
acero al carbono con terminación protegido según se especifica más adelante en este apartado.  
El bastidor debe incluir placas de identificación de equipos, válvulas e instrumentos con sus 
correspondientes TAG s. 
Con respecto a los materiales del bastidor los perfiles, chapas y placas base  deberán ser de 
acero estructural, ASTM A -36. 
El revestimiento para el bastidor de acero estructural (ASTM A -36) deberá cumplir con los 
siguientes requisitos para garantizar una alta durabilidad en un ambiente marino corrosivo:  
1. Preparación de Superficie:  
o Limpieza mediante chorreado abrasivo hasta grado SSPC -SP10 (Metal Casi 
Blanco) / Sa 2½ (ISO 8501 -1). 
o Perfil de anclaje según recomendaciones del fabricante de la imprimación (50  
micras).  
2. Sistema de Pintura (Ejemplo con productos Sherwin Williams especificados, sujeto 
a verificación de compatibilidad y recomendaciones del fabricante):  
o Capa de Imprimación (Primer):  

---

### Pagina 14
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  14 de 41 
 
 
  
 ▪ Producto: Zinc Clad II (Epóxico Rico en Zinc) SHERWIN WILLIAMS, o 
similar técnicamente equivalente aprobado por ADASA.  
▪ Espesor de Película Seca (EPS/DFT): 80 micras.  
o Capa Intermedia:  
▪ Producto: Macropoxy 646 (Epóxico de Alto Espesor) SHERWIN 
WILLIAMS, o similar técnicamente equivalente aprobado por ADASA.  
▪ Espesor de Película Seca (EPS/DFT): 200 micras.  
o Capa de Acabado (Topcoat):  
▪ Producto: Acrolon 218 HS (Poliuretano Alifático Acrílico) SHERWIN 
WILLIAMS, o similar técnicamente equivalente aprobado por ADASA.  
▪ Espesor de Película Seca (EPS/DFT): 75 micras.  
▪ Color: RAL 5012 (Azul Luminoso),  
3. Espesor Total del Sistema:  
o El espesor total de película seca del sistema de pintura no deberá ser inferior a 
355 micras (o 380 micras si se incluye el mist -coat).  
4. Aplicación y Control de Calidad:  
o La aplicación de la pintura deberá realizarse de acuerdo con las recomendaciones 
del fabricante, las condiciones ambientales permisibles (temperatura, humedad, 
punto de rocío) y por personal calificado.  
o Se realizarán inspecciones de calidad en cada etapa (preparación de superficie, 
aplicación de cada capa, medición de EPS) conforme al Plan de Inspección y 
Ensayos (PIE) Detallado.  
o Se deberá asegurar la continuidad del sistema de pintura, prestando especial 
atención a bordes, soldaduras y áreas de difícil acceso.  
El diseño del bastidor y la soportación interna de las tuberías, especialmente las de alta presión, 
deberá considerar explícitamente las cargas estáticas y dinámicas derivadas de la operación y 
posibles transientes (identificadas en el análisis de flexibil idad requerido en Sección 7), 
asegurando la adecuada restricción de movimientos y la integridad estructural bajo todas las 
condiciones.  
5.1.10  Contenedor  
Las dimensiones máximas del contenedor serán de 1 3 metros de largo por 2,5 metros de ancho, 
y 2.8 metros de altura . 

---

### Pagina 15
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  15 de 41 
 
 
  
 El contenedor deberá considerar puerta de acceso peatonal, puerta para acceso de equipos y 
puerta de emergencia. Las puertas de acceso de personas deben tener un ancho de 900 mm 
por 2.200 mm de alto.  
Las puertas de acceso para equipos deberán tener dimensiones adecuadas que permitan la 
entrada o el retiro del equipo de mayor tamaño instalado en su interior. Estas puertas contarán 
con un ángulo de apertura de 110° y se abrirán siempre hacia el exterior.  Adicionalmente, el 
contenedor deberá garantizar el acceso lateral mediante una puerta corrediza.  
El piso por donde caminarán los operarios deberá constar de una rejilla de PRFV antideslizante.  
5.1.11  Servicios Auxiliares  
El alumbrado interior del contendor deberá ser del tipo fluorescente industrial LED, luz blanco 
frío, hermético, luminarias de 2 x 18 W, 220 V, 50 Hz, con un interruptor de encendido localizado 
en cada acceso.  
La instalación eléctrica propia de la sala incluirá dos enchufes de 16 A, 2 20 VAC, con 2 polos + 
tierra de protección.  
Para la iluminación exterior de los accesos a la sala eléctrica, debe considerarse la instalación 
de luminarias de 150 W de potencia nominal o su equivalente LED , tipo hermético, fabricados en 
policarbonato, con refractor de vidrio templado y cubierta de protección tipo anti -golpes, ubicados 
sobre las puertas de acceso  y paredes laterales . Estas luminarias exteriores serán comandadas 
por una fotocelda y un switch selector de modos Manual -Off-Automático.  Toda iluminación 
externa deberá estar homologada con el DS 43  en la versión más reciente , según Decreto 
Supremo N°1, del año 2022 . 
El proveedor deberá considerar la cantidad y necesidad de unidades de aire acondicionado para  
trabajo 24  horas por día los siete días de la semana en cantidad n+1, para que la temperatura 
se mantenga por debajo de los 25º C al interior del contenedor. Este equipamiento deberá 
cotizarse en ítem por separado.  
Para los cálculos el Proveedor  deberá considerar las siguientes condiciones del sitio:  
• Temperaturas:  
o Máxima: 28°C  
o Mínima: 8°C  
• Humedad relativa promedio: 48%  
• Presión atmosférica promedio: 93,3 KPa  
Durante la ingeniería de detalles se deberá entregar una memoria de cálculo térmica para 
determinar la cantidad del sistema de aire acondicionado, en base a la información de la carga 
térmica de los equipos a instalar en ella y las condiciones ambientales especificadas por ADASA.  

---

### Pagina 16
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  16 de 41 
 
 
  
 5.2 Especificación de materiales de cañerías y válvulas  
5.2.1  Cañerías de baja presión  
Para las cañerías de baja presión se utilizará PVC siguiendo las siguientes características:  
 
 
ITEM  TAMAÑO   
DESCRIPCIÓN   
SCH  
CLASE   
END 
DESDE  HASTA  
TUBERÍA  40 mm 100 mm POLYVINYL  CHLORIDE  (PVC)  SEGÚN  ASTM  D1784. 
FABRICACIÓN SIGUIENDO ASTM D1785  80 - - 
 
FLANGE   
2"  
4" FLANGE  LOCO  EN ACERO  CARBONO  CUBIERTO  DE 
RILSAN/FIBRA  DE VIDRIO  O PP RECUBIERTO  CON  FIBRA DE  
VIDRIO,  PERFORACIONES  CONFORME  A ASME  B 16.5  
-  
150  
- 
FITTINGS  40 mm 100 mm POLYVINYL CHLORIDE (PVC) SEGÚN ASTM D1784. PARA  
SOLDAR  DIMENSIONES  SEGÚN  ASTM  D2467.  80 - - 
EMPAQUETADURA  2" 4" EMPAQUETADURA  NO METALICA,  CAUCHO NEOPRENO 
(CR), 1/16”  SEGUN ASME 16.21  - 150 - 
ESPARRAGOS  Y  
TUERCAS Y  
ARANDELAS   
-  
- ESPÁRRAGOS  DE INOXIDABLE,  ASTM  A193  Gr.B8M,  HILO 
CORRIDO,  TUERCAS  Y ARANDELAS,  ASTM  A194  Gr.8M  
(1.4401)   
-  
-  
- 
 
 
TIPO  VÁLVULA  TAMAÑO   
DESCRIPCIÓN   
CLASE   
CONEXIÓN  
DESDE  HASTA  
BOLA  1/2" 2" CUERPO  Y BOLA  EN PVC,  PASO  TOTAL,  ASIENTOS Y SELLOS 
EN PTFE, TUERCA UNIÓN DOBLE.   
150  
SW 
 
MARIPOSA   
3"  
4" DISCO ACERO INOXIDABLE SÚPER DUPLEX, ASTM A995 Gr. 
5A UNS J93404, PREN>40, EJE Y RESORTE  UNS32760,  
ASIENTO  PTFE,  CUERPO  FUNDICIÓN  GRIS.   
150  
WAFER  
RETENCIÓN  2” 4” CUERPO  Y BOLA  EN PVC 150 SW 
 
5.2.2  Cañerías de alta presión  
Para las cañerías de alta presión (hasta 120 bar) se utilizará acero inoxidable super  duplex 
siguiendo las siguientes características:  
 
ITEM  TAMAÑO   
DESCRIPCIÓN   
SCH.   
CLASE   
END 
DESDE  HASTA  
CAÑERÍA  1/2" 4" ACERO  INOXIDABLE  SÚPER  DUPLEX,  SIN COSTURA,  ASTM 
A790 UNS S32750, PREN>40, ASME B36.19M  80S - BE 
 
FLANGE   
1/2"  
4" FLANGE  CON  CUELLO  PARA  SOLDAR,  ACERO  INOXIDABLE 
SÚPER  DUPLEX,  ASTM  A182  F53 UNS  S32750,  PREN>40,  
ASME  B16.5   
80S  
900  
RF 
 
VICTAULIC   
1 1/2"   
4" ACOPLE RIGIDO, CUERPO EN ASTM A -890 Gr. CE8MN, 
SELLO GRADO EW, EPDM, TIPO VICTAULIC .  
-  
-  
- 
 
 1/2" 4" TEE, ACERO INOXIDABLE SÚPER DUPLEX, SIN COSTURA NOTA 2 - BW 

---

### Pagina 17
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  17 de 41 
 
 
  
  
ITEM  TAMAÑO   
DESCRIPCIÓN   
SCH.   
CLASE   
END 
DESDE  HASTA  
 
 
 
 
 
 
 
 
FITTINGS  ASTM A815 Gr. S32750, PREN>40, ASME B16.9  
 
1/2"  
4" TEE REDUCCIÓN,  ACERO  INOXIDABLE  SÚPER  DUPLEX,  
SIN COSTURA  ASTM  A815  Gr. S32750,  PREN>40,  ASME 
B16.9  NOTA 2  
-  
BW 
1/2" 4" CODO  90º, ACERO  INOXIDABLE  SÚPER  DUPLEX,  LR, SIN 
COSTURA ASTM A815 Gr. S32750, PREN>40, ASME B16.9  NOTA 2 - BW 
 
1/2"  
4" CODO  90º, ACERO  INOXIDABLE  SÚPER  DUPLEX,  RADIO 
CORTO,  SIN COSTURA  ASTM  A815  Gr. S32750,  PREN>40,  
ASME  B16.28  NOTA 2  
-  
BW 
1/2" 4" CODO  45º, ACERO  INOXIDABLE  SÚPER  DUPLEX,  LR, SIN 
COSTURA ASTM A815 Gr. S32750, PREN>40, ASME B16.9  NOTA 2 - BW 
 
1/2"  
4" REDUCCION CONCENTRICA, ACERO INOXIDABLE SÚPER 
DUPLEX, LR, SIN COSTURA ASTM A815 Gr. S32750, 
PREN>40, ASME B16.9  NOTA 2  
-  
BW 
 
1/2"  
4" REDUCCION  EXCENTRICA,  ACERO  INOXIDABLE  SÚPER  
DUPLEX,  LR, SIN COSTURA  ASTM  A815  Gr. S32750, 
PREN>40, ASME B16.9  NOTA 2  
-  
BW 
1/2" 4" WELDOLET,  ACERO  INOXIDABLE  SÚPER  DUPLEX,  ASTM 
A182 F53 UNS S32750, PREN>40, POR MSS SP 97  NOTA 2 - BW 
 
 
EMPAQUETADURAS   
 
1/2"  
 
4" ESPIROMETALICA, RELLENO PTFE, ANILLO INTERNO Y 
EXTERNO EN ACERO INOXIDABLE SUPER DÚPLEX, ESPESOR 
DE 3 MM, POR ASME 16.20.  
OPCIONAL: TIPO KLINGER EN AISI 316 CON RELLENO DE 
GRAFITO.   
 
-  
 
900  
 
RF 
ESPARRAGOS  Y 
TUERCAS   
-  
- ESPÁRRAGOS  DE ACERO  INOXIDABLE,  ASTM  A193  Gr.B8M, 
GOLILLA DE FIBRA, HILO CORRIDO, TUERCA HEXAGONAL 
PESADA, ASTM A194 Gr.8M (1.4401)   
-  
-  
- 
NOTAS:  
1- El espesor  de cañería  deberá  ser verificado,  basado  en las condiciones  reales  de diseño  por ASME  B31.3.  
2. Espesor  igual  a cañería.  
 
 
TIPO  VÁLVULA  TAMAÑO  DESCRIPCIÓN      CLASE   CONEXIÓN  DESDE  HASTA  
 
SEGURIDAD   
1”  
2”  
CUERPO  Y OBTURADOR  EN SUPERDUPLEX   
900 FLG 
ASME  
B16.5 F 
 
BOLA   
1/2"  
4" ACERO INOXIDABLE SÚPER DUPLEX, COMPLETAMENTE  
FABRICADA  EN ASTM  A 182 Gr. F53 UNS S32750 
(PREN>40), PASO TOTAL.  DISEÑO DE 3 CUERPOS.   
900  
Para  
Soldar  
 
5.2.3  Actuadores  
Todas las válvulas de proceso relevantes, tanto en sistemas de alta como baja presión, deberán 
contar con actuación eléctrica y ser completamente integrables al sistema de control del módulo 
(PLC), permitiendo su operación automática, así como la configuración de pe rmisos e interlocks 
de seguridad. Asimismo, las válvulas manuales consideradas críticas para el proceso deberán 
contar con finales de carrera que permitan monitorear su estado (abierto/cerrado) desde el PLC 
y condicionar lógicas de operación.  

---

### Pagina 18
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  18 de 41 
 
 
  
 La topología de comunicación entre el PLC y los actuadores deberá ser tipo estrella, con 
protocolo preferentemente ethernet a nivel de capa física.  
5.3 Especificación de motores eléctricos  
Todos los motores deberán ser trifásicos, de inducción tipo jaula de ardilla, diseñados para operar 
con una tensión de 400 V, 50 Hz y cumplir con la norma IEC 60034. En caso de que en el 
mercado existan motores de otro tipo que entreguen una mayor eficienc ia, se deberá hacer un 
trade -off para determinar la mejor alternativa.   
Los motores deberán poseer una alta eficiencia según las categorías explicitadas en la norma 
IEC 60034 -30 o equivalente. Deberán poseer una clase térmica  tipo H de acuerdo con las normas 
IEC 60085 / UL 1446.  
Todos los componentes y materiales deben ser nuevos y estar fabricados por empresas 
reconocidas en el sector. Los motores deberán estar diseñados para trabajos en ambiente 
altamente corrosivo, a una altitud menor de 1000 m.s.n.m. El grado de protección IP6 6. 
Los motores principales deberán ser diseñados para un régimen de operación tipo S1 de acuerdo 
con la norma IEC 60034 -1, con un Factor de Servicio FS=1.  
Los motores que sean alimentados a través de variadores de frecuencia deberán contemplar en 
su dimensionamiento los lineamientos especificados en la norma IEC 60034 -25. 
Los motores deberán contar con sensores de temperatura tipo Pt -100 para devanados y 
rodamientos.  
 
5.4 Especificación de tableros de fuerza y control  
El tablero de fuerza y control  contará con su estructura soportante  de tipo armario ; la operación, 
habilitación, inhabilitación y todas las maniobras de funcionamiento se realizarán desde el frente 
del tablero.  
El control de los equipos se realizará mediante un PLC  (Allen Bradley)  que comandará toda la 
secuencia de funcionamiento automático permitiendo también que esta sea ejecutada en forma 
manual por el operador sin afectar el correcto funcionamiento del sistema.  
El equipamiento del tablero tendrá funcionamiento: Automático - 0 - Manual. En Automático, el 
PLC realizará el control y comando de la planta.  
En 0, el tablero completo no tendrá posibilidad de funcionamiento ni por PLC ni manual (para 
realizar mantenimiento del equipo).  
En Manual, el PLC estará desvinculado del comando. Esto implica que aun estando el PLC 
apagado la planta podrá operar a través de los comandos manuales, por lo que la planta deberá 
poder funcionar sin inconvenientes de manera manual.  

---

### Pagina 19
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  19 de 41 
 
 
  
 El sistema de control deberá incorporar un HMI con pantalla táctil de 10”  color . Deber contar con 
la posibilidad comunicación vía OPC como estándar para disponer de una interfaz común para 
comunicar, interactuar y compartir datos con otros componentes de software.  
Se debe considerar el suministro de todo el licenciamiento y el hardware y software necesario 
para poder interactuar con el sistema de control, tanto para configuración como para 
mantenimiento.  
También se deberá considerar un sistema de comunicación vía Ethernet, con protocolo  Modbus  
TCP/IP, que permita controlar y/o extraer datos en forma remota. Para la conexión se debe 
proveer un Switch Ethernet industrial , no administrable,  de al menos 5 bocas.  
El tablero de fuerza debe incluir un equipo MVE (Medidor de Variables Eléctricas)  con capacidad 
de historización q ue entregue al menos Voltaje, Corriente y Potencias, conectado al PLC. Estas 
variables eléctricas deben estar presentes en una pantalla del HMI  junto con el Consumo 
Específico de Energía Eléctrica (C.E.E.) o Consumo Unitario, expresado en kWh/m3, que 
corresponderá al total de consumo eléctrico registrado, dividido por el volumen real de agua 
producto producida en el mismo período.  
El sistema de control debe tener la posibilidad de almacenar históricos y mostrar tendencias de 
las variables más importantes del proceso.  
El HMI debe diseñarse de modo tal que permita parametrizar el sistema según la necesidad del 
proceso, poniendo como limites, valores seguros para la operación.  
Para el control debe suministrarse una UPS con la capacidad suficiente para mantener el sistema 
de control activo por al menos 8 horas.  
Lo planos del sistema deben suministrarse en forma separada para la parte eléctrica y para el 
control.  Los planos as Built deberán entregarse en formato CAD de acuerdo con los 
requerimientos d el pliego técnico RIC N°18.  
Asimismo, debe entregarse, como parte del suministro, el respaldo de los softwares y programas 
de PLC y HMI y, los softwares y hardware necesarios para interactuar con ambos sistemas (PLC 
y HMI).  En definitiva,  todo el licenciamiento perpetuo necesario para poder interactuar con la 
lógica de control programada.  
Como parte integral del suministro del sistema de control, el Proveedor deberá entregar:  
• El código fuente completo, editable y no compilado, tanto para el PLC (incluyendo 
comentarios detallados) como para la HMI.  
• Toda la documentación necesaria para entender y modificar dicho código fuente.  
• Identificación clara (y preferiblemente entrega si no es software comercial 
estándar) de las herramientas de software (versiones específicas) necesarias para 
programar, configurar y mantener el PLC y la HMI.  

---

### Pagina 20
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  20 de 41 
 
 
  
 • Licencias de usuario final de tipo perpetuo e intransferible a ADASA para todos 
los componentes de software suministrados que lo requieran (PLC runtime, HMI 
runtime, software de desarrollo si es propietario, etc.)  
El HMI debe cumplir norma ISA 101 como estándar para diseño de pantallas . 
5.4.1  Características constructivas  
El tablero estará compuesto por un (1) gabinete  que contendrá los interruptores termomagnéticos 
y accesorios para los servicios auxiliares, fuerza, alumbrado e instrumentación. El mismo 
gabinete debe tener un área específica  para control, en la cual, estará el PLC con sus respectivas 
I/O y los equipos de comunicación y, un área para electricidad donde alojaran equipos, VDF’s , 
Etc.. 
El tablero será del tipo sobrepuesto o a piso acondicionado . La base superior e inferior de los 
paneles, deberá tener una plancha metálica empernada con empaquetadura para realizar las 
perforaciones para la prensa  cables  de los cables de entrada y salida.  
Deberá construirse con un índice de protección NEMA 4X o su equivalente IP.  
Además, deberá contar con una cubierta cubre equipos y con una puerta exterior. La puerta 
exterior será totalmente cerrada permitiéndose sobre ella sólo luces piloto de indicación de 
tablero energizado y una pantalla HMI. Todos los otros controles, selectores y comandos 
necesarios para la operación estarán en la bandeja inte rior del gabinete. Su fijación se hará 
mediante bisagras en disposición vertical u horizontal. Se pueden montar equipos de medida u 
otro elemento de maniobra o control siempre que se mantenga el grado de protección no inferior 
a NEMA 4X.  
De acuerdo con su tamaño el tablero deberá tener una o dos puertas delanteras abisagradas 
provistas de chapa o manilla con picaporte con llave. Para un ancho superior a 900 mm, deben 
llevar dos (2) puertas. Las bisagras deberán ser diseñadas de manera tal que aseguren el sello 
del tablero.  Este tablero  debe estar fuera del  contendor , permitiendo la operación desde el HMI 
del PLC sin acceder  físicamente a la planta modular . 
5.4.2  Características eléctricas  
Las barras estarán montadas en material aislante, ignifugo, que no absorba humedad, y tendrán 
un grado de aislamiento de 600 V entre fases. Las partes vivas de las barras deberán tener una 
cubierta aislante transparente de manera de evitar el contacto accidental con el personal que 
deba realizar labores de mantenimiento e n el mismo.  
La barra de neutro cumplirá con las mismas exigencias de las barras de fases.  
El tablero deberá ser provisto de una barra de cobre para las conexiones de tierra, conectada 
eléctricamente a la caja metálica del tablero y a todos los elementos metálicos constituyentes del 
mismo. La barra de tierra será de 1” × ¼” (25 x 6 mm) como míni mo y deberá tener las 

---

### Pagina 21
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  21 de 41 
 
 
  
 dimensiones adecuadas para la conexión de los conductores de tierra. Tendrá pernos de ¼” Ø 
en cantidad suficiente para el aterramiento de todos los circuitos.  
El gabinete deberá ser diseñado con amplitud suficiente para permitir el holgado ordenamiento 
de los equipos, conductores y el acoplamiento de cañerías rígidas (tipo Conduit ), o conectores 
prensa cables , por su parte inferior y superior para lo cual dispondrá de placas empernadas . 
Los gabinetes deben cumplir con todos los aspectos de la norma RIC.  
 
5.4.3  Terminaciones  
La caja exterior del tablero deberá ser completamente rígida, las uniones soldadas no deben 
presentar salientes hacia el exterior. Sus puertas y cubiertas deben ser completamente planas, 
sin ondulaciones.  
El tablero será de acero inoxidable. De lo contrario, se entregará pintado con 3 capas de pintura, 
una con propiedades anticorrosivas y las restantes de terminación color de terminación estándar 
del fabricante para interior. Previo a estas capas se realiza rá un proceso de granallado en acero 
o arenado a metal blanco. El espesor total de las capas no será menor a 100 micrones (100 μm).  
5.4.4  Protecciones eléctricas  
Los interruptores automáticos generales instalados en los tableros serán del tipo “Molded Case” , 
con capacidad de corte omnipolar  y tendrán la siguiente capacidad de ruptura 25 kA, para 
circuitos de  380 V. Para los interruptores monofásicos a utilizar en sistemas de 220 V y 120 V la 
capacidad de ruptura será 10 kA en 2 20 V. Todos los interruptores deberán ser aprobados por 
SEC y cumpliendo norma RIC.  
Los interruptores automáticos tetrapolares o tripolares  deberán tener una clase de aislamiento 
de 600 V y los monopolares de 250 V.  
Todos circuitos de enchufe s y alumbrado deberán  contar con  protección diferencial, de 
capacidad de corriente igual o superior al interruptor de protección correspondiente, y 
sensibilidad de 30 mA.  
Los circuitos de alimentación de motores trifásicos deberán contar con protección de 
sobrecorriente residual , incluyendo los instrumentos de medición necesarios.  
5.4.5  Alambrado y regletas  
El alambrado interno de los tableros y las barras para uso eléctrico deberán ser marcadas de 
acuerdo con el código de colores vigentes, y normalizado por SEC.  
Los tableros deberán contar con barras rígidas de cobre con capacidad de corriente en estado 
permanente y de cortocircuito  acorde a las características del sistema. L as barras deberán contar 
con señalización y protección ante contactos involuntarios.  

---

### Pagina 22
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  22 de 41 
 
 
  
 El cableado interno será instalado en bandejas plásticas ranuradas. Para el caso de 
instrumentación, se considera alambrar la salida de los interruptores que alimentan las cargas 
externas a una regleta, esta deberá considerar un terminal desde cada interru ptor con un terminal 
neutro contiguo.  
Todos los extremos de circuitos y cables deberán tener marcas impresas e indelebles. Las 
marcas serán del tipo manguito, termo contraíbles , y el esquema de marcado deberá incluir el 
identificador del dispositivo y el número de borne, en ambos extremos del conductor.  
 
5.4.6  VDF’s  
Deberán ser aptos para funcionar en forma continua 24 horas por día, 7 días por semana y 365 
días al año, con una vida útil esperada de al menos 10 años.  
Los variadores de frecuencia de baja tensión deberán funcionar con caídas de tensión de hasta 
30% con limitación de potencia (para una caída de tensión entre 5% y 30%, el inversor deberá 
seguir funcionando normalmente, reduciendo la potencia máxima disponi ble proporcionalmente 
al porcentual de la caída de tensión, con caídas de tensión total con duración de hasta 100 
milisegundos  (5 ciclos de red) sin que se provoque detención del proceso.  
El variador de frecuencia deberá tener un ciclo de trabajo continuo del 100% de la corriente 
nominal con una sobrecarga del 110% por un minuto cada 10 minutos si la carga es de torque 
variable. Si la carga es de torque constante, se requerirá un ciclo de t rabajo pesado con 
capacidad de manejar el 100% de la corriente nominal de forma continua con una sobrecarga 
del 150% por un minuto cada 10 minutos. El variador de frecuencia deberá ser capaz de 
suministrar hasta el 100% de torque de arranque sin retroalime ntación de velocidad. El torque 
de arranque con retroalimentación de velocidad deberá ser del 150% del nominal. Estos ciclos y 
cargas de trabajo serán los básicos que deberá soportar el variador de frecuencia. En el caso 
que el ciclo y carga de trabajo del  motor exceda los requerimientos básicos será indicado su ciclo 
y carga de trabajo en la hoja de datos.  
Con el objeto de evitar posibles deterioros en las tarjetas electrónicas que componen el variador, 
el proveedor deberá considerar que ellas sean barnizadas, por tanto, protegidas contra corrosión  
de acuerdo con la Norma IEC 721 -3-3, para partículas sólidas clase 3S 2 y gases químicos clase 
3C 3.  
La utilización del variador de frecuencia no deberá ocasionar que los motores requieran de 
disminución de su potencia efectiva (de -rating) ni de aislación mejorada ni de factor de servicio 
adicional al demandado por la carga.  
El sistema de aislación del motor a energizar no deberá ser comprometido térmicamente ni sujeto 
a esfuerzo adicional, ni comprometido debido a excesivos peaks de voltaje en la onda de salida.  

---

### Pagina 23
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  23 de 41 
 
 
  
 Los variadores deben satisfacer las exigencias de la última edición en relación con las  
recomendaciones de la norma IEEE 519  y considerar filtros dV/dt , e inyectar a la red un muy bajo 
nivel de armónicos . 
El variador debe ser capaz de mantener un mínimo de factor de potencia de 0,97 del 30% al 
100% de la potencia. Si el variador no cumple con este requerimiento, entonces una unidad de 
corrección del factor de potencia debe cotizarse como alternativa opcional.  
El variador de frecuencia deberá tener una eficiencia mínima del 97% al 100% de velocidad y al 
100% de la carga. La eficiencia del sistema deberá incluir el variador, transformador de aislación 
y/o reactor de línea según corresponda, filtro de armónica, Un idad de corrección de factor de 
potencia (si aplica) y filtros de salida.  
En los cálculos de pérdidas deberán incluirse las fuentes de poder, circuitos de control, 
ventiladores de enfriamiento y bombas.  
La programación de los Variadores de Frecuencia (VDF) y la lógica de control del PLC deberán 
implementar obligatoriamente rampas de aceleración y desaceleración controladas (soft 
start/stop) para la bomba de alta presión, con el fin de minimizar los efecto s de golpes de ariete 
durante las secuencias de arranque y parada. Los parámetros de estas rampas deberán ser 
configurables y justificados en la filosofía de control.  
5.4.7  Voltajes y frecuencia que considerar  
Para todos los equipos eléctricos se debe considerar una alimentación eléctrica de operación en 
380 VAC/220 VAC, 50 Hz. No se aceptarán equipos principales que operen en otros voltajes y 
frecuencias . 
5.5 Especificación de instrumentación  
Se detallan a continuación la instrumentación mínima con la cual deberá contar la planta . El 
protocolo de la instrumentación deberá ser 4 -20 mA + HART y los equipos de marcas 
reconocidas en el mercado con presencia demostrada de venta y servicio técnico en Chile.  
5.5.1  Caudalímetros  
La planta tendrá caudalímetros de tipo electromagnético con indicación local y transmisión a PLC 
ubicados en los siguientes puntos:  
• Un caudalímetro en la alimentación al módulo  
• Un caudalímetro en la salida permeado del rack 2°Etapa  
• Un caudalímetro en la salida de permeado  
• Un caudalímetro en la salida de rechazo  
• Un caudalímetro en la s alida filtro cartucho  CIP 

---

### Pagina 24
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  24 de 41 
 
 
  
 5.5.2  Manómetros  
Los manómetros se ubicarán en los siguientes puntos:  
• Descarga bomba de alta presión  
• Salida de rechazo  
• Descarga bomba CIP  
• Alimentación filtro cartucho  CIP 
• Salida filtro cartucho  CIP 
• Descarga bomba dosificadora dispersante  
5.5.3  Transmisores de presión  
Se instalará n los siguientes transmisores de presión con transmisión al PLC : 
• Succión bomba de alta presión  
• Descarga bomba de alta presión  
• Alimentación rack  1°Etapa  
• Rechazo rack  1°Etapa  
• Succión Turbo 1°Etapa  
• Alimentación rack 2°Etapa  
• Rechazo rack 2°Etapa  
• Salida de permeado  
• Salida de rechazo  
5.5.4  Sensores de nivel  
Se incluirá un transmisor de nivel en el estanque de agua de lavado CIP de tipo Dpcell con 
transmisión al PLC.  
5.5.5  Conductímetro  
Será de tipo celda/electrodo de conductividad transmisión a PLC y se ubicará en:  
• En la alimentación al módulo  
• Salida de p ermeado  

---

### Pagina 25
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  25 de 41 
 
 
  
 • Salida de permeado  de segunda etapa  
• Salida de rechazo de primera etapa  
• Salida de rechazo  
5.5.6  Transmisores de Vibración:  
Se deberá incluir la instalación de transmisores de vibración en la bomba de alta presión (Ítem 
5.1.1) y en las unidades del sistema de recuperación de energía (ej. Turbos, Ítems 5.1.2 y 5.1.3). 
Estos transmisores deberán ser compatibles con el PLC suministrado y permitir el monitoreo 
continuo y la configuración de alarmas  y posibles interlocks por alta vibración.  
5.6 Límites de suministro  
Los límites de batería mecánicos pueden apreciarse en detalle en el P&ID referencial encontrado 
en el anexo , siendo estos:  
• Tie-in 1: Corresponde a la entra da de salmuera de alimentación en el flange ubicado 
aguas arriba de la válvula de corte para los filtros de cartucho. La presión que deberá 
entregar ADASA en este punto deberá ser informada por el Oferente en su oferta.  
• Tie-in 2: Corresponde a la salida de permeado en el flange ubicado aguas debajo de las 
conexiones para lavado. La presión por considerar  en este punto será desde atmosférica 
hasta 1 bar de manera tal que el agua producida lleque al punto de entrega.  
• Tie-in 3: Corresponde a la salida de rechazo  en el flange ubicado aguas debajo de la 
medición de caudal y válvula de retención. La presión por considerar  en este punto será 
desde atmosférica hasta 1 bar de manera tal que el agua producida lleque al punto de 
entrega.  
• Tie-in 4: Corresponde al vaciado del estanque de lavado ubicado aguas debajo de la 
válvula esfera. La descarga se hará en forma gravitacional.  
• Tie-in 5: Corresponde al suministro de dispersante.  
• Para los tie -in 1, 2 y 3 deben entregarse los flanges con sus juntas, espárragos y tuercas 
para conexión.  
Para los flanges deberá considerarse la norma ANSI B16.5 clase 150.  
Como límite del servicio de la disciplina eléctrica debe considerarse los bornes para la acometida 
eléctrica a los tableros de fuerza y control, siendo todos los cableados, interconexinado de 
equipos y canalizaciones internas del módulo, alcance de la entr ega del Proveedor .  

---

### Pagina 26
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  26 de 41 
 
 
  
 6 DOCUMENTACIÓN QUE PRESENTAR  EN LA PROPUESTA  
En la presentación de su oferta los oferentes deberán presentar la siguiente documentación 
técnica:  
• Descripción de la Planta  
• Diagrama de flujo con presiones y balances de masas  
• Layout  con las dimensiones del módulo  
• P&ID  
• Modelaciones con las membranas seleccionadas  paras membranas nuevas y cinco años 
de uso  
• Especificación de equipos electromecánicos con marcas y modelos  
• Especificación de equipos eléctricos con marcas y modelos  
• Especificación de instrumentos y PLC con marcas y modelos  
• Protocolos a utilizar  
• Filosofía de control  
• Listado con licencias de hardware y software  
• Listado de entregables de ingeniería  
• Programa del encargo  
• PIE de equipos principales  según 5.1 
• Garantías (ver ítem 10)  
• Justificación de Tipos de Junta en Alta Presión:  En caso de proponerse el uso 
extensivo de acoples mecánicos (tipo Victaulic) en reemplazo de uniones soldadas o 
bridadas (Clase 900) en el circuito principal de alta presión, se deberá incluir una 
justificación técnica detallada que analice la idoneidad y  fiabilidad a largo plazo de dicha 
solución bajo las condiciones de presión (~120 bar), temperatura, fluido y potencial fatiga 
por ciclos operativos, junto con las referencias de aplicación correspondientes.  
• Suministro de Repuestos Mandatorios para Puesta en Marcha:  El Proveedor deberá 
incluir, **como parte integral del alcance y precio base del suministro (Suma Alzada)**, 
un lote mínimo de repuestos críticos para las fases de comisionamiento y puesta en 
marcha. Este lote deberá incluir, como mínimo:  

---

### Pagina 27
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  27 de 41 
 
 
  
 o Un (1) juego completo de cartuchos para el filtro de seguridad (Ítem 5.1.5).  
o Un (1) set de fusibles de recambio para todos los tipos utilizados en los tableros 
de fuerza y control (Ítem 5.4).  
o Un (1) transmisor de presión de repuesto, del tipo más crítico utilizado en el 
sistema de alta presión (Ítem 5.5.3).  
o Un (1) sensor/electrodo de conductividad de repuesto, del tipo utilizado en la línea 
de permeado final (Ítem 5.5.5).  
o Un (1) kit de sellos/juntas de repuesto para una conexión bridada o acople 
Victaulic (según diseño final) en el sistema de alta presión (Ítem 5.2.2).  
o Estos repuestos mandatorios deberán ser entregados junto con el módulo 
principal.  
• Listado y Cotización Opcional de Repuestos para Dos Años : Adicionalmente, el 
oferente deberá presentar en su propuesta técnica un listado detallado y recomendado 
de repuestos para dos (2) años de operación normal de la planta. Esta lista deberá incluir 
descripción, número de parte del fabricante, cantidad recom endada y será cotizada como 
un ítem opcional y separado del precio base del módulo.  
Los consumos específicos, presiones y balances de masas a entregar en la documentación 
solicitada, deberán ser consecuentes con  la capacidad de producción mínima que solicita 
ADASA . 
7 INGENIERÍA Y DOCUMENTACIÓN QUE DESARROLLAR  DURANTE EL 
ENCARGO  
El Proveedor  deberá desarrollar la ingeniería para construcción del módulo considerando que 
deberá enviar máximo a los 90 días de la adjudicación del encargo la siguiente documentación 
para aprobación por parte de ADASA , salvo en los casos que se indique un plazo menor : 
• Programa del encargo detallado incluyendo ingeniería, adquisiciones, construcción, 
transporte, montaje y puesta en marcha . (Se debe enviar máximo a los 15 desde la 
Notificación de Adjudicación).  
• P&ID  
• PFD 
• Memoria de cálculo de procesos con modelaciones con las membranas seleccionadas 
para 53.000 mg/l de TDS  
• Layout s 

---

### Pagina 28
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  28 de 41 
 
 
  
 • Planos de arreglo de equipos y cañerías en planta y elevación  
• Memoria de Cálculo Sísmico del Módulo Informe detallado que demuestre, mediante 
cálculos estructurales, la integridad del bastidor/contenedor del módulo y el adecuado 
diseño y dimensionamiento de los anclajes de todos los equipos principales (bombas, 
turbos, filtros,  tubos de presión, tableros, estanque CIP, etc.) instalados en su interior, 
bajo las condiciones sísmicas especificadas en la Sección 4.4 (NCh 2369, Zona 3). Esta 
memoria deberá ser aprobada por ADASA.  
• Análisis de flexibilidad de líneas de alta presión.  
• Plano con necesidades civiles incluyendo dimensiones, cargas y pernos  
• Diagramas Unifilares  
• Hojas de datos de equipos principales (definidos en 5.1). 
• Dossier de fabricación y pruebas de todos los equipos  eléctricos y electromecánicos  con 
sus certificados de fabricación de aceros especiales para los equipos en superduplex . 
• Especificación de, válvulas, instrumentos con marcas y modelos  
• Filosofía de control  con mención a los TAGs de los P&ID´s : La filosofía de control deberá 
detallar explícitamente, y el sistema de control deberá implementar, interlocks de 
seguridad avanzados, incluyendo, pero no limitándose a, paradas automáticas seguras 
por: muy alta presión, muy baja presión sostenida (indicat ivo de posible ruptura), alta 
vibración (si aplica según 5.5.6), y otros parámetros críticos que defina el proveedor y 
apruebe ADASA. La respuesta del sistema ante fallos de instrumentación principal 
también deberá ser definida y probada  
• Diseño de p antallas de control, HMI.  
• Listado de entregables  detallado con marca y modelo de todo el suministro  
• Maqueta 3D en software a definir por el oferente. El desarrollo del modelo  debe incluir 
toda la metada y tags de equipos e instrumentos y la plataforma de software queda 
abierta,  pero debe asegurar la interoperabilidad completa con la suite AEC de Autodesk, 
por ejemplo,  Autodesk inventor u similar.   
• Isométricas de líneas en alta presión.  
• Propuesta de vigas carrileras y puntos de izaje internos dentro del módulo , para extraer 
equipos mecánicos (Bombas y Turbos).  
• Plan de Inspección y Ensayos Detallado (PIE Detallado):  El Proveedor deberá tomar 
como base la estructura y los requerimientos mínimos definidos en el Plan de Inspección 
y Ensayos Base de ADASA, documento P22 -IT-09-000-001-0. Es obligación del 

---

### Pagina 29
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  29 de 41 
 
 
  
 Proveedor completar y detallar exhaustivamente la matriz de inspección y ensayos 
(Sección 13 del PIE Base), así como cualquier otra sección pertinente, para generar el 
"PIE Detallado" específico para este suministro.  El PIE Detallado deberá incluir, para cada 
ítem de inspección o ensayo:  
o La referencia cruzada específica y unívoca al documento y 
sección/cláusula/valor/plano que contiene el criterio de aceptación cuantitativo o 
cualitativo aplicable. Los documentos referenciados incluirán la presente 
Especificación Técnica (ET), las Bases Ad ministrativas Especiales (BAE), Normas 
aplicables, y de forma primordial, los propios documentos técnicos generados por 
el Proveedor (tales como Hojas de Datos, Planos de Fabricación aprobados, 
Procedimientos de Soldadura/END/Pruebas/Pintura/FAT/Montaje/PE M 
aprobados, Planes de Fabricación/Montaje aprobados, etc.).  
o La definición precisa de la frecuencia y/o alcance de la inspección/ensayo, 
referenciando el Plan o Procedimiento específico aprobado donde se detallen 
estos aspectos cuando la frecuencia no sea "100%" o única.  
o La identificación clara del registro específico que evidenciará la realización y el 
resultado de la inspección/ensayo.  
o El PIE Detallado es un entregable fundamental de la fase de ingeniería y deberá 
ser presentado a ADASA para su revisión y aprobación formal junto con los 
principales procedimientos y planes que referencia, dentro de los plazos 
establecidos para la entrega de ingeniería.  
o La aprobación por escrito del PIE Detallado por parte de ADASA es un requisito 
indispensable para autorizar el inicio de la fabricación de componentes mayores 
y/o el ensamblaje principal del módulo. ADASA no aprobará el PIE Detallado si 
este carece de la e specificidad, trazabilidad o referencias adecuadas a los 
criterios de aceptación en los documentos de soporte aprobados.  
 
Un mes antes de la finalización del encargo el Proveedor  deberá entregar para aprobación la 
siguiente documentación:  
• Manual de montaje de la planta , que incluya:  
- Memoria de Calculo para el izaje del módulo.  
- Plano de izaje del módulo indicando los puntos de izaje, indicando claramente pesos.  
- Plano y diseño del yugo de Izaje para el módulo  
• Manual de puesta en marcha de la planta y sus equipos.  

---

### Pagina 30
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  30 de 41 
 
 
  
 • Manual de operación y mantenimiento de la planta y sus equipos (incluyendo todas las 
pantallas del PLC con los respectivos TAG, además de como operar la planta en 
automático y manual), detallando procedimientos específicos para el manejo seguro de 
transientes operativos (arranques, paradas normales y de emergencia), d iagnóstico de 
fallas comunes, respuesta a alarmas críticas (especialmente las de alta presión), y 
recomendaciones para inspecciones periódicas de integridad (ej. revisión de torque de 
pernos bridados, inspección de acoples, pruebas funcionales de válvulas de seguridad).  
• Paquete Final de Software y Licencias:  Incluyendo medios físicos o enlace de descarga 
seguro con el código fuente editable (PLC/HMI), documentación asociada, 
identificación/entrega de herramientas de desarrollo, y certificados de licencias perpetuas  
• Procedimiento Detallado de Preservación, Embalaje y Preparación para Transporte 
Marítimo Internacional: Documento detallado para aprobación de ADASA, escribiendo 
como mínimo:   
o Métodos específicos de preservación a corto y largo plazo para todos los 
componentes sensibles (membranas RO, bombas, turbos, tuberías de Super 
Duplex, instrumentación, tableros eléctricos, etc.), considerando el ambiente 
salino y posibles cambios de tempe ratura durante el tránsito y almacenamiento.  
Plan de limpieza final interna y externa del módulo.  
o Métodos de aseguramiento y sujeción interna de equipos y componentes para 
resistir vibraciones y movimientos del transporte marítimo.  
o Especificación de materiales de embalaje, protección y desecantes a utilizar.  
o Método de sellado y verificación de estanqueidad del contenedor (si aplica).  
o Plan detallado de marcado externo de bultos y contenedor según normativa 
internacional y requisitos específicos de ADASA (ref. BAE Cl. 41).  
o Instrucciones especiales de manejo y estiba recomendadas para el transportista.  
ADASA se tomará siete días hábiles para la emisión de los comentarios una vez recibida la 
documentación. Sin la aprobación de toda la documentación por parte de ADASA el Proveedor  
no podrá liberar los equipos para trasporte a terreno.  
La generación de documentos y la codificación del proyecto deberá seguir los lineamientos de 
ADASA en  el documento  P00-IT-00-000-101-0 (CODIFICACION GENERAL), donde se describe 
entre otros la metodología de tagueo  de instrumentos, líneas  y equipos . 
8 INSPECCIONES  DURANTE LA FABRICACIÓN  
Todos los equipos comprendidos en esta especificación estarán sujetos a inspección por parte 
de ADASA, con anterioridad al despacho, quien será notificado, al menos con un mes de 
anticipación, de la fecha de las inspecciones.  

---

### Pagina 31
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  31 de 41 
 
 
  
 La inspección abarcará cualquier aspecto que tenga relación con la calidad y funcionamiento de 
los equipos adquiridos, su avance de fabricación, ensayos, pruebas, inspección de pinturas y 
embalajes. El inspector tendrá un acceso fácil y expedito a la fábri ca, documentos y planos, 
durante el período de fabricación y pruebas. Cualquier deficiencia encontrada durante las 
pruebas será documentada y corregida, por cargo del proveedor, antes de ser liberados los 
equipos por parte de la inspección de ADASA. Los re querimientos de inspección y control de 
calidad de los equipos serán establecidos en el documento “ Plan de Inspección y Ensayos ”, que 
se entregará al oferente  adjudicado.  
Verificación de Materiales Críticos (PMI):  Como parte del aseguramiento de calidad, el 
Proveedor deberá realizar una Identificación Positiva de Materiales (PMI) mediante un método 
espectrográfico adecuado en, al menos, un 10% (o un número mínimo de piezas a acordar) de 
los componentes suministrado s de Acero Inoxidable Super Duplex destinados al circuito de alta 
presión (tuberías, accesorios, cuerpos de válvula, bridas). Los resultados deberán confirmar la 
conformidad con la especificación UNS S32750 y serán parte del Dossier de Calidad. ADASA se 
reserva el derecho de testificar estas pruebas (Punto W).  
Plan de Ensayos No Destructivos (NDE):  El Proveedor deberá someter a aprobación de 
ADASA un Plan de NDE detallado para todas las soldaduras del sistema de alta presión (Acero 
Super Duplex). Este plan especificará, como mínimo, el tipo de ensayo (RT, UT, PT, etc.), el 
porcentaje de cobertura pa ra cada tipo de junta (circunferencial, derivación, etc.) y los criterios 
de aceptación aplicables según ASME B31.3 y/o normativa más exigente acordada. Como 
mínimo, se requerirá la siguiente cobertura de ensayos no de structivos para todas las soldaduras 
a tope en el circuito de alta presión (Acero Super Duplex): 100% de Inspección Visual (VT), 100% 
de Líquidos Penetrantes (PT) en la pasada de raíz y en la soldadura final, y un 10% de 
Radiografiado (RT) o Ultrasonido (U T) en soldaduras circunferenciales y de derivación críticas, 
distribuidas aleatoriamente. El alcance y detalle final, incluyendo la posible extensión de estos 
mínimos, se formalizará en el Plan de NDE y el PIE Detallado, los cuales estarán sujetos a la 
revisión y aprobación final de ADASA.  
 
8.1 Alcance Mínimo de Pruebas de Aceptación en Fábrica (FAT)  
Adicionalmente a las inspecciones generales durante la fabricación mencionadas, y como 
requisito previo a la autorización de envío del módulo y como soporte al hito de pago definido en 
las BAE (Cláusula 3 1), el Proveedor deberá ejecutar y documentar satisfactoriamente las 
Pruebas de Aceptación en Fábrica (FAT). ADASA o sus representantes tendrán derecho a 
presenciar dichas pruebas, notificándose la fecha con la antelación indicada. Se requiere que las 
prueb as hidrostáticas de los sistemas de baja y alta pre sión (detalladas en el PIE, Sección 5) 
hayan sido completadas y aprobadas satisfactoriamente antes del inicio formal de las FAT. El 
alcance mínimo de las FAT incluirá, pero no se limitará a, la verificación y/o atestiguamiento de 
lo siguiente:  
• Aprobación del Procedimiento FAT:  Revisión y aprobación del procedimiento detallado 
de FAT propuesto por el Proveedor . 

---

### Pagina 32
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  32 de 41 
 
 
  
 • Inspección Visual, de Completitud y Verificación Dimensional:  Comprobación del 
correcto montaje de todos los equipos y componentes dentro del contenedor/skid 
conforme al Layout y P&ID aprobados. Verificación de dimensiones generales, ubicación 
y tipo de las conexiones de interfaz (Tie -ins definidos en Sección 5.6) y  puntos de izaje.  
• Verificación de Integridad del Montaje Mecánico:  Verificación visual de la correcta 
instalación e identificación de tuberías, soportes y equipos.  
• Pruebas Funcionales (en seco):  Chequeo de giro libre y correcta dirección de rotación 
de equipos rotativos principales (Bombas). Verificación de actuación de válvulas 
automáticas y señalización de válvulas manuales críticas con finales de carrera.  
• Verificación del Sistema de Instrumentación y Control:  Comprobación de la correcta 
instalación e identificación (TAGs) de todos los instrumentos. Chequeo de continuidad 
eléctrica y lazos ("loop checks") para señales de instrumentos hacia el PLC. Verificación 
de la correcta energización del tablero de control y PLC. Revisión de las pantallas HMI 
(según ISA 101) y ejecución de una simulación avanzada y dinámica del control.  Esta 
simulación deberá realizarse utilizando señales de entrada forzadas o un simulado r de 
proceso, que representen los rangos operativos y transitorios clave del proceso (ej. 
variaciones de flujo, presión, conductividad según ET Sec. 4), e incluirá 
obligatoriamente escenarios de fallo simulados (ej. pérdida de señal de transmisor 
de presión crítico, disparo de bomba bajo carga, actuación de válvula de seguridad) 
para verificar la correcta ejecución de las secuencias de parada segura, la ge stión 
de alarmas críticas y la lógica de interlocks bajo condiciones anormales . El objetivo 
es verifica r no solo la lógica de interlocks básicos, sino también la respuesta dinámica de 
lazos de control importantes, la correcta ejecución de secuencias complejas (arranque, 
parada normal/emergencia, CIP), la gestión de alarmas críticas y la funcionalidad 
comple ta de las pantallas HMI bajo condiciones simuladas representativas. Las 
comunicaciones con sistemas externos (si aplica) también serán verificadas  
• Revisión Documental Preliminar:  Verificación de la disponibilidad y conformidad 
preliminar de la documentación clave (Manuales O&M preliminares, certificados de 
materiales para componentes críticos como Super Duplex, registros de pruebas previas 
incluyendo hidrostáticas, dossier de cali dad de fabricación según lo requerido en Sección 
7). 
• Verificación de Conformidad con Normativa Eléctrica Chilena (SEC):  Comprobación 
documental y/o visual (marcado) de que los componentes eléctricos principales (ej. 
interruptores, protecciones, VDFs, cableado principal, tableros) y el ensamblaje general 
cumplen con los requisitos esenciales de la normativa SEC chilena apli cables al 
equipamiento suministrado. Revisión de la disponibilidad y conformidad de certificados o 
declaraciones de cumplimiento necesarios para la posterior certificación/inscripción en 
Chile. (Esta verificación será un punto de detención (Hold Point) y su conformidad es 
requisito previo a la autorización de embarque ). 

---

### Pagina 33
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  33 de 41 
 
 
  
  
El Proveedor deberá registrar detalladamente los resultados de todas las pruebas y 
verificaciones ejecutadas durante las FAT, conforme al alcance mínimo definido en esta sección 
y según el Procedimiento de FAT aprobado, en un protocolo específico. La confo rmidad técnica 
final de las FAT, basada en la revisión de dicho protocolo y el atestiguamiento de las pruebas 
clave según los criterios de aceptación definidos, será formalmente validada y confirmada por 
ADASA. Esta validación se materializará mediante la emisión de un Acta de Aprobación FAT por 
parte de ADASA, cuya emisión constituye un hito de control definido en el Plan de Inspección y 
Ensayos (PIE) Detallado y Aprobado (PIE Base Ítem 7.9). Tanto el protocolo de pruebas FAT 
generado por el Proveedor como  el Acta de Aprobación FAT emitida por ADASA formarán parte 
integral e indispensable del dossier final de calidad del módulo.  
Se deja constancia que la aprobación de las FAT no exime al Proveedor de su responsabilidad 
respecto al correcto funcionamiento del módulo una vez instalado en sitio, ni reemplaza las 
Pruebas de Desempeño en sitio descritas en la Sección 10 de esta especif icación, las cuales 
son mandatorios  para la Recepción Provisional.  
 
9 COMISIONAMIENTO  Y PUESTA EN MARCHA  
Se establece que el período efectivo para las actividades de comisionamiento y puesta en 
marcha , comprendido desde el inicio formal del comisionamiento en sitio y hasta que la planta 
sea declarada por el Proveedor como lista para iniciar las Pruebas de Desempeño descritas en 
la Sección 10.2, no deberá exceder de 21 días corridos . El Proveedor deberá planificar  y 
coordinar  sus recursos y actividades, incluyendo la coordinación con los Vendors especialistas, 
para cumplir con dicho  plazo  y completar las activi dades de Comisionamiento y Puesta en 
Marcha en cumplimiento de las Bases de l encargo  y sus Especificaciones . 
El Provedor  debe considerar en el periodo de puesta en marcha, como personal mínimo  el 
responsable de la integración del módulo  con un procesista que  conozca en detalle el diseño del 
módulo y  tenga la capacidad técnica de realizar los ajustes pertinentes en la programación del 
PLC, adicional a los Vendors  que el Proveedor  estime convenientes.  
Para asegurar una ejecución eficiente y experta de estas etapas críticas, el personal clave del 
Proveedor deberá  con una experiencia adecuada, e specíficamente, tanto el Responsable de la 
Integración del Módulo  como el Procesista deberán contar, cada uno, con un mínimo de diez 
(10) años de experiencia demostrable en el diseño, implementación y/o puesta en marcha de 
plantas de tratamiento de agua, y haber participado activamente en la implementación y puesta 
en marcha de, al menos, dos (2) plantas desaladoras modulares por ósmosis inversa de 
capacidad y complejidad comparables a la del presente Encargo.  
La interconexión  del módulo con  la línea de salmuera de alimentación , línea de drenaje de 
rechazo  y línea de permeado,  así como el anclaje a base del contenedor, incluyendo los equipos 

---

### Pagina 34
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  34 de 41 
 
 
  
 de izamiento requeridos para ese fin como grúas  serán alcance  de ADASA , de acuerdo con  los 
límites  establecidos en el punto 5.6 
El Comisionamiento y Puesta en Marcha se realizarán en el sitio de ubicación de la Planta 
Modular,  dentro del predio que posee ADASA en su agencia zonal ubicada en Guillermo Matta 
221, Ciudad de Taltal, Región de Antofagasta.  
El Proveedor , estará a cargo de l comisionamiento,  puesta en marcha y capacitación del personal 
de ADASA a cargo de la operación. La puesta en marcha incluye la supervisión del sistema hasta 
la entrada en régimen de este , incluyendo las pruebas de desempeño que corroboren el correcto 
funcionamiento de las instalaciones.  
Cada actividad deberá ser documentada, registrada y concentrada en un informe final separado 
por comisionamiento, capacitación y puesta en marcha . 
Con respecto a la  capacitación del personal de ADASA será un entrenamiento diseñado para 
identificar oportunidades de optimización energética y mejorar las ratios  de producción de agua, 
elementos clave para conseguir una operación más eficiente y sostenible. El temario mínimo que 
considerar  será el siguiente:  
• Diseños avanzados de sistemas de ósmosis inversa.  
• Cuantificación de beneficios como reducción de la huella de carbono, mejora en la tasa 
de retorno, ahorro en el consumo de energía, ahorro en el consumo de agua.  
• Diseño y modelación de membranas de Ultra alta presión (UHPRO), como las que utiliza 
el modulo  
• Características y detalles del software de proyección de membranas para tener un mejor 
control de la normalización de datos y optimizaciones.  
• Análisis  de datos para proyección  de CIP de membranas  de UHPRO . 
10 GARANTÍAS  
10.1 Parámetros de desempeño a garantizar  
10.1.1  Capacidad Nominal  
La Capacidad Nominal Que Garantizar  para la planta objeto de esta licitación será de  480 m3/día , 
equivalentes a 20 m3/h . Esta capacidad de producción corresponde al volumen de agua producto 
entregada por la planta y medida en el caudalímetro de permeado.  
10.1.2  Calidad del Agua Producto Que Garantizar  
La calidad del agua producida por la Planta debe cumplir con las condiciones mínimas de calidad 
definidas en el punto 4.3 de esta especificación.  

---

### Pagina 35
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  35 de 41 
 
 
  
 10.1.3  Consumo Específico de Energía Eléctrica Garantizado  
El Consumo Específico de Energía Eléctrica (C.E. E.) o Consumo Unitario, expresado en 
kWh/m3, corresponderá al consumo eléctrico registrado por todos los equipos e instalaciones de 
la planta en el período de las pruebas de desempeño, dividido por el volumen real de agua 
producto producida en el mismo período.  
El Consumo Específico de Energía Eléctrica Garantizado será el que el Licitante asegure en su 
Oferta Técnica para los rangos de TDS especificados teniendo en cuenta que los mismos deben 
ser inferiores a los siguientes consumos máximos establecidos en funci ón del contenido de 
sólidos disueltos del agua filtrada:  
TDS (mg/l)  Consumo  específico  requerido  (kWh/m3)  
43.000  a 48.000  < 4,8 
48.000  a 53.000  < 5,0 
 
10.2 Pruebas de Desempeño  
Alcanzados los parámetros de calidad y cantidad de agua durante el proceso de Puesta en 
Marcha, se dará paso al período de Pruebas de Desempeño. Si las pruebas no resultan 
satisfactorias, se aplicarán las penalizaciones establecidas en las Bases Administra tivas 
Especiales para este incumplimiento.  
10.2.1  Prueba de la Capacidad Nominal de Producción  
Durante esta Prueba de Desempeño la planta debe funcionar durante un período de 2 días 
consecutivos, de forma continua y al 100% de la capacidad nominal de producción. Esta prueba 
también servirá para comprobar los parámetros garantizados de calidad del agua producto y 
consumo específico de energía eléctrica.  
Esta prueba se considerará positiva y aprobada si se cumplen, satisfactoriamente, los 2 días de 
funcionamiento en forma continua y se logra una producción mínima del período de 960 m3. 
10.2.2  Pruebas de calidad del agua producto  
Para comprobar la calidad del agua producto de la planta, se tomará  una muestra diaria a la 
salida del permeado durante el período de 2 días de prueba para determinar mediante medición 
in situ y análisis de laboratorio los parámetros de calidad exigidos en esta licitación y garantizados 
por el Proveedor . Estos análisis y determinaciones son:  
• Contenido de Cloruros  
• Sólidos Totales Disueltos  

---

### Pagina 36
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  36 de 41 
 
 
  
 10.2.3  Prueba del Consumo Específico de Energía Eléctrica  
La prueba se considerará positiva y aprobada si el coeficiente entre los consumos totales de 
energía registrados en el período, en kWh, y los metros cúbicos producidos durante la prueba, 
es menor al valor garantizado por el Licitante adjudicado.  
El consumo total de energía para el período respectivo corresponderá al registrado en el medidor 
del panel de fuerza de la planta desaladora modular.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 37
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  37 de 41 
 
 
  
 11 ANEXO I – Caracterización de salmuera  
https://www.dropbox.com/t/MHIH96wxPLzwFjEX   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 38
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  38 de 41 
 
 
  
 12 ANEXO II – PFD Proyecto Base  
https://www.dropbox.com/t/1mwTnrOM618nGTOe   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 39
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  39 de 41 
 
 
  
 13 ANEXO III – P&ID ´s proyecto base  
https://www.dropbox.com/t/Er6BNQOXtfTevmwI   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 40
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  40 de 41 
 
 
  
 14 ANEXO I V – Planos de arreglo mecánico/cañerías del proyecto base  
https://www.dropbox.com/t/neQmyLZn3L5SKmYK   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

---

### Pagina 41
---
 
                                                                                                                                 
 
  
ESPECIFICACIÓN TÉCNICA  
 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA – PD TALTAL  
  
Código: P 22-ET-09-000-001 
Fecha: 24/04/25   
Revisión N°: 0 
Página:  41 de 41 
 
 
  
 15 ANEXO V – 3D proyecto base  
https://www.dropbox.com/t/Fyct85LrUBDAhbNZ   
 
 
 


================================================================================
## 7. OFERTA TECNICA BW WATER REV1 (vigente) — TEXTO COMPLETO
================================================================================

============================================================
--- PAGE 1 ---
============================================================
 
 
4520 Oak Fair Blvd, Suite 200 
Tampa, FL 33610 - USA 
www.bw-water.com.com   
 
 
 
To: Aguas Antofagasta S.A. (ADASA) Technical Proposal for ADASA’s 
Taltal Desalination Plant – Brine 
Recovery Project  
- UHPRO System 
 
Client Ref.: Proceso de Licitación 12803 SUMINISTRO 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA - 
PLANTA DESALADORA TALTAL (ex 12783) 
BW Water Americas Inc. 
 
BWWA Ref. No: 20.24.6501.F - Rev.1  
August 19, 2025 | Confidential  

============================================================
--- PAGE 2 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.2 
 
PROPRIETARY , PATENT NOTICE & CONFIDENTIALITY AGREEMENT  
 
This proposal and the concept of the system are the intellectual property of BW Water and its 
Affiliates and are subject to legal copyright. The contents of this proposal shall not be disclosed 
by the Recipient to any third party without the expressed written consent of BW Water groups. 
National and International patents protect core parts of our systems. 
BW Water group reserves the right to alter the proposed system to incorporate technical 
advances realized after the date of this proposal.   
 
BW Water’s information and the recommendations presented in this proposal (hereinafter 
referred to as "Confidential Information") are the work product of BW Water Gorup and are 
provided solely with the understanding and agreement that the information contained in this 
document is submitted for evaluation only. The recipient agrees not to reveal its contents 
except to those in Recipient’s organization necessary for evaluation and copies of this 
document may not be distributed outside of the Recipient organization. 
 
By receiving and accepting this proposal, the recipient agrees to the stated terms and 
conditions. 
 
  

============================================================
--- PAGE 3 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.3 
 
Contents 
EXECUTIVE SUMMARY ................................................................................................. 5  
1. TECNICAL OFFER – COVER LETTER  ................................................................... 6  
DOCUMENT No. 1 – TECHNICAL DESCRIPTION ........................................................ 7  
2. PLANT DESCRIPTION  ............................................................................................. 8  
2.1 PROJECT & SYSTEM OVERVIEW ......................................................................... 8  
2.1.1 Process Description ........................................................................................ 9  
2.2 DESIGN BASIS ...................................................................................................... 10  
 System Recovery ....................................................................................................... 10  
 System Production Water Volume .............................................................................. 10  
 Feed Water Quality And quantity ................................................................................ 11  
 Product Water Quality ................................................................................................ 11  
 Seismic Conditions ..................................................................................................... 11  
 Others conditions, requirements, and/or assumptions ................................................ 11  
3. PERFORMANCE GUARANTEES  .......................................................................... 12  
3.1 PERFORMANCE PARAMETERS .......................................................................... 12  
 Nominal Production (permeate) Capacity ................................................................... 12  
 Product Water Quality ................................................................................................ 12  
 Specific Energy Consumption (SEC) .......................................................................... 12  
3.2 PERFORMANCE TESTS ....................................................................................... 13  
 Nominal Permeate (Product) Capacity Test ................................................................ 13  
 Product Water Quality Test ......................................................................................... 13  
 SEC (Specific Energy Consumption) Test .................................................................. 14  
4. SCOPE OF SUPPLY AND WORK  ......................................................................... 15  
4.1 Equipment List & Technical Details .................................................................... 16  
5. CLARIFICATION & DEVIATION LIST  ................................................................... 21  
6. DRAWINGS  ............................................................................................................ 24  
6.1 3D MODEL OF CONTAINERIZED SYSTEM ......................................................... 24  
6.2 GA / LAYOUT ......................................................................................................... 26  

============================================================
--- PAGE 4 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.4 
 
6.3 PROCESS FLOW DIAGRAM (PFD) ...................................................................... 28  
6.4 PIPING AND INSTRUMENTATION DRAWINGS (P&ID) ....................................... 30  
7. RO MEMBRANE PROJECTIONS  .......................................................................... 35  
7.1 TURBO CHARGER PROJECTION ........................................................................ 71  
8. PROTOCOLS  ......................................................................................................... 73  
9. CONTROL PHILOSOPHY  ...................................................................................... 74  
10. HARDWARE AND SOFTWARE LICENSES LIST  ................................................. 89  
11. PROJECT SCHEDULE  .......................................................................................... 90  
11.1 ENGINEERING SUBMITTALS & SCHEDULE .................................................. 91  
12. INSPECTION AND TESTING PLAN (ITP)  ............................................................. 97  
13. JUSTIFICATION OF MECHANICAL COUPLINGS/JOINTS (VICTAULIC TYPE) IN HIGH 
PRESSURE  ................................................................................................................. 105  
14. MANDATORY/CRITICAL SPARE PARTS LIST FOR COMMISSIONING AND START-
UP PHASES  ................................................................................................................ 108  
15. RECOMMENDED TWO-YEAR SPARE PARTS LIST .......................................... 109  
16. CHEMICALS CONSUMPTION  ............................................................................. 111  
17. POWER & LOAD CONSUMPTION LIST  ............................................................. 112  
DOCUMENT No. 2 – COMMISSIONING & START-UP PLAN ................................... 114  
18. COMMISSIONING AND START-UP ACTIVITIES EXECUTION PLAN  ............... 115  
18.1 KEY PERSONNEL ........................................................................................... 115  
18.2 PRELIMINARY ON SITE FIELD SERVICE PROGRAM .................................. 119  
18.3 RESOURCES AND ASSIGNED SPECIALISTS TO BE USED ....................... 120  
 Resources and Assigned Specialists Plan (Preliminary-Sample Plan) ...................... 120  
DOCUMENT No. 3 – GUARANTEED SEC VALUE .................................................... 122  
19. SIGNED DECLARATION OF THE SPECIFIC ENERGY CONSUMPTION (SEC) 
GUARANTEED VALUE  .............................................................................................. 123  
 
 

============================================================
--- PAGE 5 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.5 
 
 
 
 
 
 
 
EXECUTIVE SUMMARY 
 

============================================================
--- PAGE 6 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.6 
 
1. TECNICAL OFFER – COVER LETTER 
Following the approval of our company, BW Water Americas Inc. (BWWA),  as a qualified bidder for 
the public tender identified as “ Proceso de Licitación 12803 – SUMINISTRO MÓDULO RO 
SEGUNDA ETAPA PARA SALMUERA - PLANTA DESALADORA TALTAL (ex 12783)”,  and in 
consideration of the clarifications requested during the evaluation of our Technical Proposal Rev. 0, 
submitted on August 5, 2025, we are pleased to submit our Revised Technical Proposal (Rev. 1) . 
This proposal is for the supply of an Ultra-High-Pressure Reverse Osmosis (UHPRO) system  with 
ancillary components for Aguas Antofagasta SA (ADASA ), as part of the Brine Recovery Project  at 
the Taltal Seawater Desalination Treatment Plant  in Chile. 
Our revised submission reflects our commitment to becoming the selected vendor for the required 
system package and has been prepared in accordance with the instructions outlined in the “Bases 
Administrativas Especiales” (BAE), Sections 20 and 20.1. 
As part of our evaluation of the bidding documentation, we are proposing a containerized UHPRO 
system designed to treat 1,176 m³/day of brine  from the existing Taltal desalination plant. The system 
will produce desalinated water that meets the Client’s project requirements and supports the goal of 
increasing potable water production for human consumption without increasing raw water 
extraction from existing wells . 
With over 35 years of global experience  in the water and wastewater industry, BWWA offers a robust, 
reliable, and efficient RO solution tailored to meet ADASA’s water quality and production needs. Our 
proposed solution, branded as Brine Positive , incorporates components from internationally 
recognized manufacturers and complies with the technical specifications and design drawings provided 
by the Client. 
Our scope of supply includes a standalone, containerized second-stage UHPRO system  capable of 
producing 21 m³/hour  at a 42.85% recovery rate , along with all necessary ancillary components to 
ensure a comprehensive and integrated solution. BWWA brings proven engineering expertise, in-house 
fabrication capabilities, and a global network of qualified service providers to deliver a high-performance 
system aligned with the Client’s goals. 
We look forward to the opportunity to collaborate with ADASA and contribute to the successful delivery 
of this important infrastructure project. Should you require any further information or clarification, we are 
ready to assist. 
 
Best regards, 
BW Water Americas Inc.  

============================================================
--- PAGE 7 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.7 
 
 
 
 
 
 
 
DOCUMENT No. 1 – 
TECHNICAL DESCRIPTION 
 
 
 

============================================================
--- PAGE 8 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.8 
 
BW Water Americas Inc. (BWWA)  has prepared Document 1 – Technical Description  in accordance 
with the bidding instructions outlined in the Bases Administrativas Especiales (BAE), Section 20.1 – 
Document 1 . This document also considers the list of required documentation described in Technical  
Specification No. P22-ET-09-000-001-0, Section 6.  
Please note that the order in which the information is presented does not strictly follow the sequence 
outlined in Section 6 of the Technical Specifications. However, all required elements have been 
addressed. Additionally, where deemed necessary and applicable, we have included supplementary 
information to provide a comprehensive technical offer for our proposed UHPRO system. 
Furthermore, this proposal has been revised to incorporate the clarifications requested on August 12, 
2025, following the technical evaluation of our initial submission (Technical Proposal Rev. 0, submitted 
on August 5, 2025). 
2. PLANT DESCRIPTION  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Descripción de la Planta”) 
2.1 PROJECT & SYSTEM OVERVIEW 
ADASA, the entity responsible for operating sanitary concessions for potable water production and 
distribution in Antofagasta, is undertaking a strategic expansion of its desalination capabilities. This 
project involves the supply and installation of a modular second-stage Reverse Osmosis (RO) system 
at the Taltal Desalination Plant. The primary objective is to increase the production of desalinated water 
during peak summer demand periods—without increasing the volume of raw water extracted from 
existing wells. 
To achieve this, the required system should treat the brine (wastewater) discharged from the existing 
RO unit/module No3, recovering and producing a minimum of 20 m³/hour  of additional permeate. The 
system may accommodate up to 5% higher flow rates , if bidders offer standardized modular solutions 
capable of handling larger capacities in compliance with project specifications. 
BWWA proposes its Brine Positive Plant Solution , a brine treatment system featuring an Ultra High-
Pressure Reverse Osmosis (UHPRO) unit and associated components. This advanced system is 
designed to maximize water recovery from existing infrastructure while maintaining high energy 
efficiency and operational reliability. 
Our system  is designed to treat 49 m³/hour (~1,176 m³/day) of brine (the feed) and produce 21 
m³/hour (~504 m³/day) of permeate . It will include: 
o One (1) containerized UHPRO unit consists of Cartridge Filter, 2-stage UHPRO train, High 
Pressure RO Pump Energy Recovery Devices (Turbo type) 

============================================================
--- PAGE 9 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.9 
 
o A Lot of Ancillary equipment located outside the container, including Dosing System for 
high-salinity feed protection and CIP system. 
2.1.1 Process Description 
Brine from the existing RO module No3 at the Taltal Desalination Plant is fed into the proposed system 
at a flow rate of 49 m³/hour via a Brine Feed Pump (by others). The Ultra High-Pressure Reverse 
Osmosis (UHPRO) system operates at a recovery rate of 42.85%, producing high-quality permeate with 
a salinity of less than 500 ppm. 
The process flow includes the following key stages: 
1. Brine Feed Transfer : Brine supplied from the existing desalination plant (by others) is first 
treated with an anti-scalant to mitigate scaling risks due to high salinity. The treated feed passes 
through a cartridge filter before being delivered to the high-pressure RO feed pump. 
2. High-Pressure Pumping : The filtered brine is pressurized by a high-pressure pump and 
directed into the first stage of the UHPRO system 
3. Feed Turbo Exchange : An energy recovery device (Feed Turbo) boosts the pressure of the 
feed stream, optimizing energy efficiency and ensuring the required pressure for UHPRO 
operation is achieved. 
4. Pressure is boosted using the Feed Turbo to meet the required UHPRO feed pressure. 
5. Interstage Turbo Exchange : Concentrate from the first stage is further pressurized using an 
Interstage Turbo, which transfers energy from the second-stage concentrate to the first-stage 
concentrate, enabling efficient feed into the second UHPRO stage 
6. Permeate (Water Product) Transfer : The final permeate produced by the system is dosed with 
anti-scalant and routed to the existing post-treatment system (provided by others) for final 
conditioning and distribution 
7. Brine of UHPRO system : final Concentrate/brined produced by the system 
This modular and energy-efficient solution enhances water recovery from existing infrastructure, 
contributing to sustainable water resource management in the region. 
Here is a picture of the 2-stage concept mentioned above. Please refer to the preliminary GA/layout, 
PDF, P&ID and 3D drawings attached for addional details. 

============================================================
--- PAGE 10 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.10 
 
 
2.2 DESIGN BASIS 
The design of the proposed Brine Treatment System is based on the technical specifications package 
(Tender “Licitation” No. 12803) prepared and provided by the client, ADASA, via its online portal on June 
11, 2025. This package was supplemented by eight (8) formal clarifications (in Spanish “Aclaraciones”) 
received via email on the following dates: 
- Clarification No. 01 – June 19, 2025 
- Clarification No. 02 – July 1, 2025 
- Clarification No. 03 – July 7, 2025 
- Clarification No. 04 – July 8, 2025 
- Clarification No. 05 – July 7, 2025 
- Clarification No. 06 – July 28, 2025 
- Clarification No. 07 – August 1, 2025 
- Clarification No. 08 – August 12, 2025 
The main design conditions, requirements, and assumptions are outlined below: 
 System Recovery 
The system will have a minimum recovery of 42.85% 
 System Production Water Volume 
The system will produce 21 m³/hour of permeate  


============================================================
--- PAGE 11 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.11 
 
 Feed Water Quality And quantity 
As provided by client. 
Parameter Unit Value 
Total Dissolved Solids  mg/L 43,000 - 53,300 
Total Suspended Solids  mg/L 0.4 - 1 
Turbidity NTU 0.4 - 1 
Temperature °C 19 - 24 
 
 Product Water Quality  
Parameter Unit Value 
Total Dissolved Solids  mg/L < 500 
Chlorides  mg/L < 400 
  
 Seismic Conditions 
As applicable, the components and the system enclosure will be designed and built to continuously 
withstand the maximum load that may occur under all operating conditions, including earthquakes. The 
module structures (frame and container) and the anchors for the main internal equipment must be 
designed and built to withstand earthquakes in accordance with Chilean Seismic Standard NCh 2369, 
for Zone 3. 
 
 Others conditions, requirements, and/or assumptions 
The Client shall provide and guarantee the following: 
 Brine Feed Pressure  - a minimum of 45 psi (3 bar) is required   
 Feed Water Flow - 1,176m3/day of brine  
The proposed design and equipment selection is based solely upon design conditions and 
requirements and assumptions described thought this proposal as well as data provided by 
ADASA. BW Water Americas shall not be responsible for system performance issues, design 
and equipment changes caused by deviations to those mentioned design conditions, 
requirements, and/or assumptions.  Performance Guarantee will be provided based upon the 
water quality data provided by Client, ADASA. 
Also refer to Section 7 of this proposal  

============================================================
--- PAGE 12 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.12 
 
3. PERFORMANCE GUARANTEES  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Garantías”, (Section 10) 
In accordance with Technical Specifications (P22-ET-09-000-001-00, Section 10), the Bidder (Supplier) 
shall guarantee the following performance parameters and demonstrate compliance through on-site 
performance testing, as outlined below: 
3.1 PERFORMANCE PARAMETERS 
 Nominal Production (permeate) Capacity  
The guaranteed nominal minimal capacity for the Augas Antofagasta UHPRO Plant  is 20 m³/hr 
(480³/day). ADASA (the client), will accept up to maximum permeate flow of up 21m3/hr (504 m³/day). 
The production is based on a feed water capacity of 1,176 m3/h (provided by client)  
 Product Water Quality  
The UHPRO Plant will produce water that meets the minimum quality conditions defined below, 
contingent upon the feed water quantity and quality provided by ADASA meeting the requirements 
stated in Section 2.2 of this proposal: 
Parameter Unit Value 
Total Dissolved Solids  mg/L < 500 
Chlorides  mg/L < 400 
 Specific Energy Consumption (SEC) 
The Specific Energy Consumption (SEC)—referred to in Spanish as EEC—is defined as the total power 
consumption of the RO unit, including all plant equipment and auxiliary systems (such as the RO high-
pressure pump, chemical dosing pump, CIP/flushing pump, CIP heater, RO PLC power, air conditioning, 
and lighting) during the performance testing period. This value is then divided by the actual volume of 
product water produced (21 m³/h) at a feed TDS of 53,000 ppm. 
For further details, please refer to: 
▪ Section 3.2 – Performance Testing 
▪ Section 19 – Guaranteed SEC Value 
▪ Section 17 – Power Consumption Calculation 
▪ Section 5 – Clarifications and Deviations 

============================================================
--- PAGE 13 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.13 
 
3.2 PERFORMANCE TESTS 
The plant shall operate continuously for 2 consecutive days at 100% capacity. This test will validate the 
guaranteed parameters for: 
 Nominal Capacity  
 Product Water Quality  
 SEC (in Spanish EEC)  
 Nominal Permeate (Product) Capacity Test  
The permeate  capacity of 21  m³/hr will be delivered to the Client’s plant for reuse and measured via 
the permeate flowmete r to confirm compliance. 
 Product Water Quality Test  
Daily samples will be collected from the permeate side during the 2-day test period. 
 Chloride and TDS will be measured using an on-site conductivity analyzer instrument and 
laboratory analysis . See table above for minimum water quality conditions (Section 3.1) 
 Laboratory testing will be conducted by ADASA, with sampling performed by BWWA (subject to 
price adder). 
NOTE: BWWA only can warrant the water quality performance based on The UHP RO 
membrane manufacturer policy described below as updated by manufacturer on August 13, 
2025. 
Revised UHRO Membrane Performance Warranty : 
 Due to Membrane Manufacturing internal Policy, it only provides membrane warranty larger than 
15000m3/day  
 If end user (Client) provides data accumulated with LG UHPRO membrane, membrane 
manufacturing company will consider providing a system performance warranty upon future 
replacement.   
 Lifetime for LG UHPRO is about 1 year, thus 5 years projection value in RO projections will not 
apply into calculation of design TalTal Brine Positive plant. Thus 5 Years projections are provided 
by the request from Client in the specification(P22-ET-09-000-001), section 6, Thus 5 years 
Projected process parameters will not be guaranteed.   
Please refer to Section 5 and 7 of this proposal  

============================================================
--- PAGE 14 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.14 
 
 SEC (Specific Energy Consumption) Test  
Total energy consumption during the performance testing period will be recorded using the UHPRO 
Plant Power Panel Meter . As per project requirements, the guaranteed SEC value must remain 
below 5.0 kWh/m³  at a feed TDS of 53,000 ppm . 
Our guaranteed SEC (EEC)  value is calculated based on the total energy consumption of all equipment 
and systems associated with the RO unit, including the RO high-pressure pump, chemical dosing 
pump, CIP/flushing pump, CIP heater, RO PLC power, indoor and outdoor lighting, and air 
conditioning unit . This total is divided by the permeate capacity , at the maximum TDS level of 53,000 
ppm, and considers a CIP frequency of every 60 days . 
The guaranteed SEC (EEC)  value is 4.71 kWh/m³ ± 5% . 
This SEC value is the one to be considered for both the SEC performance guarantee  and 
the commercial evaluation  of the offer. For further details, please refer to: 
▪ Section 3.1 – Performance Paraments 
▪ Section 19 – Guaranteed SEC Value 
▪ Section 17 – Power Consumption Calculation 
▪ Section 5 – Clarifications and Deviations 
 
 
 
 

============================================================
--- PAGE 15 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.15 
 
4. SCOPE OF SUPPLY AND WORK 
BWWA will be responsible for the engineering design, procurement/fabrication, and supply of a modular 
second-stage Reverse Osmosis (RO) system, along with applicable ancillary equipment, to be installed 
at ADASA’s Taltal Desalination Plant (installation by others). The scope also includes related services 
such as installation supervision, commissioning and start-up, and operator training. 
The table below summarizes the major items / equipment included in our proposed solution. 
A more comprehensive list with some addional details is presented in the attached equipment lists 
(section 4.1.1 below) 
 
Quantity Major Items/ Equipment 
UHPRO Module -Inside of the container 
1 x 100% RO Feed Cartridge Filter package   
– Fiberglass housing with 15 polypropylene elements (2.5" x 40") per filter. Installed 
inside a 40 ft container with piping, valves, and instrumentation. 
1 x 100% RO High-Pressure Pump with VFD package 
 – Super Duplex casing and impeller, 49 m³/h (215.6 GPM) @ 723 psig (49.14 barg), 
115.3 hp (86 kW) motor.  
Installed inside a 40 ft container with piping, valves, and instrumentation. 
1 x 100% Double Stage Ultra High-Pressure RO (UHPRO) Train with ERD package   
– 21 m³/h (92.4 GPM) permeate capacity per train, designed for 42.85% recovery. 
Configuration: 6:4 array, 7-element vessels, 70 TFC RO membranes. Includes one 
Super Duplex Bi-Turbo Energy Recovery package (1 Feed Turbo and 1 Interstage 
Turbo), SDSS high-pressure piping, PVC low-pressure permeate piping, and all 
necessary valving/instrumentation tubed and wired to a junction box. Installed inside a 
40 ft container. 
1 Lot HVAC  for the container (a separate price will be provided in Commercial proposal) 
 2 A/C (1W + 1S) are provided inside container. Vent fan is not needed since CIP 
system and chemical dosing system are located in outside the container.  
Ancillary Equipment of the UHPRO Module - Out of the container 
1 x 100% CIP / Flushing Tank package 
– HDPE material, 5.1 m³ capacity. Includes CIP heater and is installed with piping, 
valves, and instrumentation. Located outside the 40 ft container. 
1 x 100% CIP / Flushing Pump package   
– SS316 casing and impeller, 57 m³/h (250 GPM) @ 61 psig (4.1 barg), 15 hp (11 kW) 
motor. Installed with piping, valves, and instrumentation. Located outside the 40 ft 
container. 

============================================================
--- PAGE 16 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.16 
 
Quantity Major Items/ Equipment 
1 x 100% CIP Cartridge Filter package 
– Fiberglass housing with 15 polypropylene elements (2.5" x 40") per filter. Installed 
with piping, valves, and instrumentation. Located outside the 40 ft container. 
1 x 100% Anti-Scalant Injection System package 
– Includes 1 HDPE drum, 1 pump skid, and plastic piping. Installed with piping, valves, 
and instrumentation. Located outside the 40 ft container. 
1 Lot Local Control Panel with HMI package   
– Installed outside the 40 ft container. 
 
Exclusions: 
The following items are excluded from the scope of supply and services for the proposed Brine 
Treatment System: 
 Civil and Foundation Design 
 Civil Works 
 Installation of Supplied Equipment/System and direct labor during commissioning and start-
up. BWWA will provide supervision for these on-site services, as detailed in Section 18 of 
this proposal. 
Also, please refer to Section 5 of this proposal 
4.1 Equipment List & Technical Details 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Especificación de equipos electromecánicos con marcas 
y modelos” | -Item “Especificación de equipos eléctricos con marcas y modelos” | -Item “Especificación 
de instrumentos y PLC con marcas y modelos”) 
The lists provided herein are preliminary. The complete and final equipment/component lists, as 
applicable, will be developed and submitted during the execution phase of the project. These will be 
included as part of the engineering submittals and will reflect the outcomes of technical 
discussions and mutual agreement on the final scope of work. It is understood that modifications may 
occur as the project progresses and requirements are refined. 
 Electromechanical equipment List (updated) 
 PLC & Instruments List (updated) 
 

============================================================
--- PAGE 17 ---
============================================================
Confidential
CUSTOMER: REV.:1
LOCATION: DATE: August 15, 2025
PROJECT No.: ORIG. BY:
Item Description /Service Qty Capacity Material Dimensions Details Manufacturers Notes
1 Static Mixer 1 x 100% 49 m3/hr FRP4'' (D) x 22'' (H)One Ports
 (1'' CL150 RFSO Flanged)
Connection : (CL 150 RFSO Flanged)
Triple Action Mixing ElementsKOMAX or Equal
2 RO Cartridge Filter 1 x 100% 49 m3/hrFRP Housing
Polypropylene filterShell(FRP) : 12 in (D) x 55in (H)
Filter : 2 1/2'' OD x 40'' # of filters in housing : 12 Filtrek or Equal
3 RO HP Feed Pump 1 x 100%51.45 m3/hr
@ 49.14 BargSDSS Shaft/Shell 123 in (L) x 34 in (W) x 28.9 in (H)Motor Rating : 86kW
IP66 / Class B (Protection)
VFD (Strater Type)Fedco or Equal
4 Feed Turbo 1 x 100%Feed : 49 m3/hr (Membrane 
Pressure : 57.0 barg)
Brine : 27.9 m3/hr  (Outlet Pressure 
:1 barg)SDSS 2507 11.51 in (L) x 11(W) x 9 in (H) Model : HPB - 60 Fedco or Equal
5 Interstage Turbo 1 x 100%Feed : 35.4 m3/hr (Membrane 
Pressure : 71.5 barg)
Brine : 27.9 m3/hr  (Outlet Pressure 
:1 barg)SDSS 2507 11.51 in (L) x 11(W) x 9 in (H) Model : HPB - 60 Fedco or Equal
6 Doble stage Brine Treatment RO Unit 1 x 100% See item 6.1 and 6.2
6.1 RO Memebrane 70Permeate Flow : 21 m3/hr
Recovery : 42.85%Composite Polyamide 8'' (D)  x 40'' (L)Membrane : LG SW 400 R G2 UHP;
42 Membranes for 1st stage and 28 membrend for 
2nd stageLG  (or Dupont)
6.2 RO Pressure Vessesl (PV)/ Tubes 10Array: (10PVs) 6:4 , 7 membrane 
elements per PVFRP/SDSS 13.92 '' (D) x  343.2 '' (L) To be provided later for details. Protec or Equal
7 CIP/Flushing Tank 1 x 100% 5.1 m3 (1350 GAL) HDPE 71in (D) x 88in (H) NTO Tank or Equal
8 CIP Heater 1 x 100% 20 kW 316 SS/316L SS Flange3'' Flanged 
7 1/2 in (D) x 47 1/2 in (L) .150 lb CHROMALOX or Equal
9 CIP/Flushing Pumps 1 x 100%54.5 m3/hr 
@ 4.13 barg316SS Shaft/Shell 30 in (L) x 13 in (W) x 14.4 in (H)150 lb ANSI Flange
Motor : 15kW (480V/50Hz/3Ph)
IP66 / Class B
VFD (Starter Type)Groundfos or Equal
10 CIP/Flushing Cartridge Filter 1 x 100% 54.5 m3/hrSS316 Housing
Polypropylene filterShell(FRP) : 14.50 in (D) x 55 in (H)
Filter : 2 1/2'' OD x 40'' # of filters in housing : 19 Filtrek or EqualMechnical Equipment List
Aguas Antofagasta
Chile
Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - August 19 2025 1

============================================================
--- PAGE 18 ---
============================================================
Confidential
CUSTOMER: REV.:1
LOCATION: DATE: August 15, 2025
PROJECT No.: ORIG. BY:
Item Description /Service Qty Capacity Material Dimensions Details Manufacturers NotesMechnical Equipment List
Aguas Antofagasta
Chile
Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System
11 Antiscalant Dosing Pumps (Skid) 2 x 100% 1 LPH @ 4 bargPVC wetted parts 
and piping
Skid : Duplex9.98 in (L) x 6.71 in (W) 
x 12.25 in (H)Solenoid, Positive Displacement
Internal Pressure Relief Valve
Control : Automatic
Seal Material : StandardGroundfos or Equal
12 Antiscalant Dosing Tank 1 x 100% 65 gal HDPE 23'' (D) x 26''(H) x 43''(L) Norwesco or Equal
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - August 19 2025 2

============================================================
--- PAGE 19 ---
============================================================
CUSTOMER: Aguas Antofagasta REV.: 1
LOCATION: Chile DATE: 15-Aug-25
PROJECT No.: Proposal 20.24. 6501  -ADASA Brine Recovery Project -UHPRO System [ Rev.1] ORIG. BY: Nicholaus Huta
Item Instrument Type / Description Media Manufacturer Location Qty Notes
1Analytical Transmitter - ORP Seawater Brine EMERSON / ABB / EQUAL RO CF DISCHARGE 1 4-20mA + HART (24VDC, 4-wire)
2Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO HP PUMP SUCTION 1 4-20mA + HART (24VDC, 2-wire)
3Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO HP PUMP DISCHARGE 1 4-20mA + HART (24VDC, 2-wire)
4Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO STAGE 1 FEED 1 4-20mA + HART (24VDC, 2-wire)
5Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO STAGE 1 REJECT 1 4-20mA + HART (24VDC, 2-wire)
6Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO STAGE 2 FEED 1 4-20mA + HART (24VDC, 2-wire)
7Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO STAGE 2 REJECT 1 4-20mA + HART (24VDC, 2-wire)
8Pressure Transmitter Seawater Brine FOXBORO / EQUAL INTERSTAGE TURBO TO FEED TURBO 1 4-20mA + HART (24VDC, 2-wire)
9Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO TRAIN COMBINED PERMEATE 1 4-20mA + HART (24VDC, 2-wire)
10 Pressure Transmitter Seawater Brine FOXBORO / EQUAL RO TRAIN REJECT 1 4-20mA + HART (24VDC, 2-wire)
11 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL RO HP PUMP DISCHARGE 1 Local Indication Only
12 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL RO TRAIN REJECT 1 Local Indication Only
13 Flow Transmitter Seawater Brine ROSEMOUNT / ABB / EQUAL RO TRAIN COMBINED PERMEATE 1 4-20mA + HART (24VDC, 4-wire)
14 Flow Transmitter Seawater Brine ROSEMOUNT / ABB / EQUAL RO TRAIN STAGE 2 PERMEATE 1 4-20mA + HART (24VDC, 4-wire)
15 Flow Transmitter Seawater Brine ROSEMOUNT / ABB / EQUAL RO TRAIN REJECT 1 4-20mA + HART (24VDC, 4-wire)
16 Analytical Transmitter - CONDUCTIVITY Seawater Brine EMERSON / ABB / EQUAL RO TRAIN COMBINED PERMEATE 1 4-20mA + HART (24VDC, 4-wire)
17 Motorized Valve Seawater Brine EMERSON / EQUAL RO TRAIN PERMEATE OUT 1 ETHERNET/IP
18 Motorized Valve Seawater Brine EMERSON / EQUAL OFF-SPEC PERMEATE DUMP 1 ETHERNET/IP
19 Motorized Valve Seawater Brine EMERSON / EQUAL CIP TO RO STAGE 1 1 ETHERNET/IP
20 Motorized Valve Seawater Brine EMERSON / EQUAL CIP TO RO STAGE 2 1 ETHERNET/IP
21 Motorized Valve Seawater Brine EMERSON / EQUAL FEED TURBO LP BYPASS 1 ETHERNET/IP
22 Motorized Valve Seawater Brine EMERSON / EQUAL INTERSTAGE TURBO LP BYPASS 1 ETHERNET/IP
23 Motorized Valve Seawater Brine EMERSON / EQUAL RO CIP PERM RETURN 1 ETHERNET/IP
24 Motorized Valve Seawater Brine EMERSON / EQUAL RO STAGE 1 CIP REJECT 1 ETHERNET/IP
25 Motorized Valve Seawater Brine EMERSON / EQUAL RO STAGE 2 CIP REJECT 1 ETHERNET/IP
26 Temperature Transmitter Seawater Brine ROSEMOUNT / SIEMENS / EQUAL CIP TANK 1 4-20mA + HART (24VDC, 2-wire)
27 Level Gauge Seawater Brine CIP TANK 1 Local Indication Only
28 Level Transmitter Seawater Brine IFM / VEGA / EQUAL CIP TANK 1 4-20mA + HART (24VDC, 2-wire)
29 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL CIP PUMP DISCHARGE 1 Local Indication Only
30 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL CIP CF INLET 1 Local Indication Only
31 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL CIP CF OUTLET 1 Local Indication Only
32 Analyzer Indicator - pH Seawater Brine EMERSON / ABB / EQUAL CIP PUMP DISCHARGE 1 4-20mA + HART (24VDC, 4-wire)
33 Flow Transmitter Seawater Brine ROSEMOUNT / ABB / EQUAL CIP TO RO TRAIN 1 4-20mA + HART (24VDC, 4-wire)
34 Motorized Valve Seawater Brine EMERSON / EQUAL ANTISCALANT TO DOSING TANK 1 ETHERNET/IP
35 Level Gauge Seawater Brine ANTISCALANT TANK 1 Local Indication Only
36 Level Switch Seawater Brine IFM / VEGA / EQUAL ANTISCALANT TANK 124VDC DISCRETE (x2, HIGH + 
LOW)
37 Pressure Gauge Seawater Brine ASHCROFT / WIKA / EQUAL ANTISCALANT PUMP DISCHARGE 1 Local Indication OnlyPLC and Intruments List 
PLC Major Parts BOMInstrument List
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - printed  Confidential

============================================================
--- PAGE 20 ---
============================================================
CUSTOMER: Aguas Antofagasta REV.: 1
LOCATION: Chile DATE: 15-Aug-25
PROJECT No.: Proposal 20.24. 6501  -ADASA Brine Recovery Project -UHPRO System [ Rev.1] ORIG. BY: Nicholaus HutaPLC and Intruments List 
Item Model Number / Description Type Manufacturer Location Qty Notes
15069-L320ER CPU Allen Bradley PLC PANEL 1
25069-IB16 DIGITAL INPUT Allen Bradley PLC PANEL A/R
35069-OB16 DIGITAL OUTPUT Allen Bradley PLC PANEL A/R
45069-IF8 ANALOG INPUT Allen Bradley PLC PANEL A/R
55069-OF4 ANALOG OUTPUT Allen Bradley PLC PANEL A/R
6Panelview Plus 7 HMI Allen Bradley PLC PANEL 1
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - printed  Confidential

============================================================
--- PAGE 21 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.21 
 
5. CLARIFICATION & DEVIATION LIST 
No.   Subjects Contents Reference 
1   Technical 
Bid 
Submittal 
Document   "Protocols to be used" will be submitted as 
detail in execution stage, BWWA will choose 
communication as Ethernet/IP  P22 -ET-09-000-001 
Page 26, 
6. DOCUMENTATION 
TO BE PRESENTED IN 
THE PROPOSAL  
2   Guarantee Total Energy consumption considering not 
only RO HP Pump but also the chemical 
dosing pump, CIP/Flushing Pump, CIP Heater, 
RO PLC Power, Lights (indoor and outdoor) 
and A/C unit is now 4.71kW/m3± 5% by 
considering CIP frequency as 60 days. P22 -ET-09-000-001 
Page 34, 
10. GUARANTEE  
 
REQUESTS FOR 
CLARIFICATION OF 
TECHNICAL OFFER  
3   Guarantee Product Water Quality Test through Laboratory 
analysis shall be conducted by ADASA and 
sampling will be conducted by BWWA, but this 
will be price adder P22 -ET-09-000-001 
Page 26, 
10. GUARANTEE 
4   Technical 
Bid 
Submittal 
Document  BWWA shall provide List of Hardware and 
Software License for HMI/PLC Programming, 
and this will be Hardware and Software 
License for HMI/PLC. 
 
Programming as a price adder. P22 -ET-09-000-001 
Page 26, 
6. DOCUMENTATION 
TO BE PRESENTED IN 
THE PROPOSAL 
5   Guarantee BWWA only offers design based on pressure 
data and other process data for Year 0 and 1 
RO projections under 19 - 24C. LG UHPRO 
Membrane has about 1-year lifetime 
membrane. Thus, year 5 projected values 
(attached with rev.1 Technical proposal 
submission) are provided to ADASA since 5Y 
were requested as one of item in '6. 
DOCUMENTATION TO BE PRESENTED IN 
THE PROPOSAL". However, these year 5 
projected process parameters will not be 
guaranteed.  P22 -ET-09-000-001 
Page 26, 
10. GUARANTEE  
5   Guarantee The Membrane manufacturer only provides 
warranty for 1-year Workmanship and 
Materials limited Warranty for UHPRO 
(maximum pressure: 120 bar) membrane. 
Here is the current warranty for product Water P22 -ET-09-000-001 
Page 26, 
6. DOCUMENTATION 
TO BE PRESENTED IN 
THE PROPOSAL 
 

============================================================
--- PAGE 22 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.22 
 
No.   Subjects Contents Reference 
Quality Revised Terms based on Membrane 
manufacturing company for UHPRO: 
 
1. Due to Membrane Manufacturing internal 
Policy, it only provides membrane warranty 
larger than 15000m3/day 
 
2. If end user provides data accumulated with 
LG UHPRO membrane, membrane 
manufacturing company will consider 
providing a system performance warranty 
upon future replacement.  
 
3. Lifetime for LG UHPRO is about 1 year, 
thus 5 years projection value in RO 
projections will not apply into calculation of 
design TalTal Brine Positive plant. Thus 5 
Years projections are provided by the 
request from Client in the 
specification(P22-ET-09-000-001), section 
6.  
Thus 5 years Projected process 
parameters will not be guaranteed.  P22 -ET-09-000-001 
Page 35, 
10. GUARANTEE 
6   Submission 
Due date ADASA has stated that the supplier must 
submit all required documentation for 
approval no later than 90 calendar 
days following the award notice. 
However, we are considering a maximum 
delivery time of 42 weeks from the date 
of purchase order (PO)/contract acceptance, 
most documentation related to the engineering 
phase is expected to be submitted within 15 
weeks of PO/contract acceptance—not from 
the award notice. 
It is estimated that there will be a 15 to 20-day 
gap between the award notice and the 
completion of  PO/contract acceptance.   P22 -ET-09-000-001 
Page 26, 
7. Engineering and 
Documentation to be 
developed during the 
charge 
7   Document 
submittal 
during 
execution 
stage Flexibility analysis of high-pressure lines is 
vague. BWWA can provide the class rating for 
the high-pressure line to show flexibility 
analysis.  P22 -ET-09-000-001 
Page 26, 
7. Engineering and 
Documentation to be 
developed during the 
charge 

============================================================
--- PAGE 23 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.23 
 
No.   Subjects Contents Reference 
8   CIP Line 
Valve 
Material CIP Line Butterfly Valve( Size 4'') shall have 
PVC (wetted part) material. P22 -ET-09-000-001 
Page 16, 
5.2 Specification of pipe 
and valve materials.  
9   
HP 
Pressure 
line Check 
Valve RO HP Pump discharge (3'') and Concentrate 
to Waste (2-1/2'') line has check valves and 
are not in the range HP line check valve size ( 
1'' - 2'') in the  P22 -ET-09-000-001 Page 16, 
5.2 Specification of pipe and valve materials. 
So BWWA clarify that these vales should be 
check valve even though they are not in the 
specified range of (1'' - 2'') regarding check 
valve.  P22 -ET-09-000-001 
Page 16, 
5.2 Specification of pipe 
and valve materials.  
 
 

============================================================
--- PAGE 24 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.24 
 
6. DRAWINGS 
The following preliminary diagrams and drawings are included as part of this proposal.  
6.1 3D MODEL OF CONTAINERIZED SYSTEM  
 
 
 
 


============================================================
--- PAGE 25 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.25 
 
 
 
 


============================================================
--- PAGE 26 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.26 
 
6.2 GA / LAYOUT  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Layout con las dimensiones del modulo”) 
 

============================================================
--- PAGE 27 ---
============================================================
FOR PROPOSAL


============================================================
--- PAGE 28 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.28 
 
6.3 PROCESS FLOW DIAGRAM (PFD)  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Diagrama de flujo con presiones y balances de masas”) 
 

============================================================
--- PAGE 29 ---
============================================================
PRELIMINARY

============================================================
--- PAGE 30 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.30 
 
6.4 PIPING AND INSTRUMENTATION DRAWINGS (P&ID) 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “P&ID’) 
Updated/revised document 
 

============================================================
--- PAGE 31 ---
============================================================
RO CARTRIDGE FILTERAIA
-HH
H
(PLC)
AIT
-
ORP-1
PRELIMINARY

============================================================
--- PAGE 32 ---
============================================================
PIT
-PI
-PIA
-H
L
PIT
-
RO HP FEED PUMP
PIA
-H
L
(PLC)
PIT
-VB
-PIA
-H
(PLC)
PIT
-PSV
-
AIT
-
CONDFIA
-H
L
(PLC)
FIT
-
XV
-
XV
-PDIA
-H
(PLC)
FIA
-H
L
(PLC)
FIT
-2 STG BRINE TREATMENT RO TRAIN
1X100%
FEED TURBO
INTERSTAGE TURBOPIT
-
PI
-PIT
-PIT
-
PIT
-FIA
-H
L
(PLC)
FIT
-
PIT
-
XV
-
XV
-
PRELIMINARY

============================================================
--- PAGE 33 ---
============================================================
ITE
-TA
-HH
H
L
(PLC)
LIT
-LIA
-HH
H
L
LL
(PLC)
AI
-
pH
LG
-
FLUSH/CIP TANKFLUSH/CIP PUMPSCIP/FLUSH  CARTRIDGE FILTERPI
-PI
-FIA
-H
L
(PLC)
FIT
-PI
-
CIP HEATERXV
-
XV
-
XV
-
PRELIMINARY

============================================================
--- PAGE 34 ---
============================================================
PSV
-PI
-
LA
-H
L
(PLC)
LS
-
LG
-
ANTISCALANT DOSING TANK ANTISCALANT DOSING PUMP
PRELIMINARY

============================================================
--- PAGE 35 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.35 
 
7. RO MEMBRANE PROJECTIONS 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Modelaciones con las membranas seleccionadas paras 
membranas nuevas y cinco años de uso”) 
The following RO membrane projections are included: 
Conditions: TDS 43,000 ppm | Temperature: 19°C  
 Year 0 
 Year 1 
 Year 5 
Conditions: TDS 43,000 ppm | Temperature: 24°C 
 Year 0 
 Year 1 
 Year 5 
Conditions: TDS 53,000 ppm | Temperature: 19°C 
 Year 0 
 Year 1 
 Year 5 
Conditions: TDS 53,000 ppm | Temperature: 24°C 
 Year 0 
 Year 1 
 Year 5  
Please note, our UHPRO system design  is based on Year 0 and Year 1 RO projections , with a 10% 
safety margin  applied. This results in a second-stage feed pressure of 83.9 bar , consistent with both 
turbocharger sizing and membrane specifications. Attached are the corresponding turbocharger 
projections. 
Year 5 RO projections for models 19 Co and 24 Co have been updated to reflect a 1 bar permeate 
back pressure . These projections are provided for reference only and are not guaranteed  beyond 
the membrane’s expected one-year operational life . 
Please also refer to Section 3.2 and Section 5 for notes related to the performance-limited 
warranty provided by the UHPRO membrane manufacturer. 
 

============================================================
--- PAGE 36 ---
============================================================
v3.3.0.1
Water type: 0
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 30.4 bar
42.86 % 53.15 bar
System - Pass1
21 m3/hr 8.5 lmh 19 °C
49 m3/hr 10.51 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.4 bar 48.57 bar
70 53.15 bar 193.73 mg/L
ERD type: None 80 % 1
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.07 35.93 48.57 47.48 1.09 0 1 0 8.81 166.96
Stage 2 4 7 35.93 7.95 27.98 61.48 60.13 1.35 14 1 0 8.04 237.73
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,445.30 13,445.30 18,314.73 23,494.76 23,494.76 59.85 85.26 69.46
Potassium 473.70 473.70 645.13 827.44 827.44 2.48 3.54 2.88
Magnesium 1,461.94 1,461.94 1,993.25 2,559.08 2,559.08 1.41 2.02 1.64
Calcium 505.56 505.56 689.30 884.97 884.97 0.48 0.69 0.56
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,704.79 23,704.79 32,292.67 41,429.29 41,429.29 97.79 139.31 113.50
Sulfate 3,362.28 3,362.28 4,584.93 5,887.21 5,887.21 1.37 1.96 1.59
Nitrate 0.16 0.16 0.22 0.28 0.28 0.00 0.01 0.01
Carbonate 2.11 2.11 2.88 3.69 3.69 0.00 0.00 0.00
Bicarbonate 221.40 221.40 301.13 385.79 385.79 2.24 3.18 2.60
Boron 7.48 7.48 9.72 11.98 11.98 1.32 1.76 1.49
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.86 3.67 3.67 0.01 0.01 0.01
CO2 6.36 6.36 6.36 6.36 6.36 6.36 6.36 6.36
TDS 43,186.82 43,186.82 58,836.83 75,488.18 75,488.18 166.96 237.73 193.73
pH 7.60 7.60 7.72 7.82 7.82 5.78 5.93 5.84
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.53 14.93 6.45 0.20 12.96 1.10 43,180.01 87.82
LG SW 400 R G2
UHP2 7.64 0.43 12.29 5.68 0.18 11.01 1.09 46,153.15 112.12
LG SW 400 R G2
UHP3 7.21 0.35 10.04 4.92 0.16 9.28 1.07 48,925.69 143.09
LG SW 400 R G2
UHP4 6.85 0.29 8.16 4.21 0.15 7.77 1.06 51,450.57 182.33
LG SW 400 R G2
UHP5 6.56 0.23 6.61 3.56 0.14 6.47 1.05 53,702.20 231.73
LG SW 400 R G2
UHP6 6.33 0.19 5.35 2.98 0.13 5.37 1.04 55,674.42 293.51
LG SW 400 R G2
UHP7 6.14 0.15 4.32 2.48 0.13 4.44 1.04 57,376.52 370.23
Stage 2
LG SW 400 R G2
UHP1 8.98 0.48 13.62 5.35 0.23 14.32 1.08 58,828.39 128.61
LG SW 400 R G2
UHP2 8.50 0.39 11.14 4.62 0.21 12.26 1.07 62,147.89 163.53
LG SW 400 R G2
UHP3 8.11 0.32 9.09 3.96 0.20 10.46 1.06 65,153.71 207.06
LG SW 400 R G2
UHP4 7.79 0.26 7.41 3.36 0.19 8.89 1.05 67,829.94 260.98
LG SW 400 R G2
UHP5 7.53 0.21 6.05 2.84 0.18 7.55 1.04 70,179.18 327.14
LG SW 400 R G2
UHP6 7.31 0.17 4.94 2.39 0.17 6.39 1.04 72,218.91 407.69
LG SW 400 R G2
UHP7 7.14 0.14 4.05 2.00 0.16 5.41 1.03 73,975.17 504.98Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 11:26:55
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 48.57 bar (1P)
Raw water flow: Raw water TDS: 43,186.82 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,186.82 mg/L Specific energy: 4.58 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 37 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.73 1.64
CaSO4 28.5 % 59.07 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.86 0.11
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,186.82 7.60
2 1P RO Feed 49.00 48.57 43,186.82 7.60
3 1P Brine 28.00 60.13 75,488.18 7.82
4 1P Product 21.00 1.00 193.73 5.84Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 38 ---
============================================================


============================================================
--- PAGE 39 ---
============================================================
v3.3.0.1
Water type: 1
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 30.4 bar
42.86 % 53.14 bar
System - Pass1
21 m3/hr 8.5 lmh 19 °C
49 m3/hr 11.13 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.4 bar 49.17 bar
70 53.14 bar 207.01 mg/L
ERD type: None 80 % 0.93
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.1 35.89 49.17 48.08 1.09 0 1 0 8.84 177.98
Stage 2 4 7 35.89 7.92 27.98 62.08 60.73 1.35 14 1 0 8.01 255.08
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,445.30 13,445.30 18,330.83 23,491.99 23,491.99 63.80 91.49 74.23
Potassium 473.70 473.70 645.69 827.32 827.32 2.65 3.80 3.08
Magnesium 1,461.94 1,461.94 1,995.13 2,559.08 2,559.08 1.51 2.16 1.76
Calcium 505.56 505.56 689.95 884.97 884.97 0.52 0.74 0.60
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,704.79 23,704.79 32,321.26 41,424.91 41,424.91 104.25 149.50 121.29
Sulfate 3,362.28 3,362.28 4,589.30 5,887.34 5,887.34 1.46 2.10 1.70
Nitrate 0.16 0.16 0.22 0.28 0.28 0.01 0.01 0.01
Carbonate 2.11 2.11 2.88 3.69 3.69 0.00 0.00 0.00
Bicarbonate 221.40 221.40 301.36 385.67 385.67 2.39 3.42 2.77
Boron 7.48 7.48 9.70 11.92 11.92 1.40 1.86 1.57
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.86 3.67 3.67 0.01 0.01 0.01
CO2 6.36 6.36 6.36 6.36 6.36 6.36 6.36 6.36
TDS 43,186.82 43,186.82 58,889.20 75,480.87 75,480.87 177.98 255.08 207.01
pH 7.60 7.60 7.72 7.82 7.82 5.81 5.96 5.86
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.52 14.63 6.32 0.20 13.65 1.10 43,180.01 95.61
LG SW 400 R G2
UHP2 7.65 0.43 12.17 5.62 0.18 11.71 1.09 46,088.94 120.80
LG SW 400 R G2
UHP3 7.22 0.35 10.05 4.91 0.16 9.97 1.07 48,824.09 152.64
LG SW 400 R G2
UHP4 6.87 0.29 8.25 4.24 0.15 8.43 1.06 51,339.18 192.64
LG SW 400 R G2
UHP5 6.57 0.24 6.75 3.63 0.14 7.09 1.05 53,606.09 242.59
LG SW 400 R G2
UHP6 6.34 0.19 5.51 3.07 0.13 5.94 1.04 55,614.32 304.57
LG SW 400 R G2
UHP7 6.14 0.16 4.50 2.59 0.13 4.97 1.04 57,367.65 380.93
Stage 2
LG SW 400 R G2
UHP1 8.97 0.47 13.27 5.22 0.23 15.01 1.08 58,880.80 140.28
LG SW 400 R G2
UHP2 8.50 0.39 10.96 4.55 0.21 12.97 1.07 62,115.38 176.53
LG SW 400 R G2
UHP3 8.12 0.32 9.03 3.93 0.20 11.16 1.06 65,067.67 221.38
LG SW 400 R G2
UHP4 7.80 0.26 7.44 3.37 0.19 9.58 1.05 67,719.13 276.41
LG SW 400 R G2
UHP5 7.54 0.22 6.13 2.87 0.18 8.20 1.04 70,068.97 343.42
LG SW 400 R G2
UHP6 7.32 0.18 5.06 2.44 0.17 7.01 1.04 72,129.43 424.32
LG SW 400 R G2
UHP7 7.14 0.15 4.18 2.07 0.16 5.99 1.03 73,921.52 521.22Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 11:26:02
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 49.17 bar (1P)
Raw water flow: Raw water TDS: 43,186.82 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,186.82 mg/L Specific energy: 4.63 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 40 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.73 1.64
CaSO4 28.5 % 59.08 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.86 0.11
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,186.82 7.60
2 1P RO Feed 49.00 49.17 43,186.82 7.60
3 1P Brine 28.00 60.73 75,480.87 7.82
4 1P Product 21.00 1.00 207.01 5.86Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 41 ---
============================================================


============================================================
--- PAGE 42 ---
============================================================
v3.3.0.5
Water type: 5
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 30.4 bar
42.86 % 53.11 bar
System - Pass1
21 m3/hr 8.07 lmh 19 °C
49 m3/hr 13.32 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.4 bar 51.12 bar
70 53.11 bar 270.29 mg/L
ERD type: None 80 % 0.7
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.19 35.81 51.12 50.02 1.1 0 1 0 8.45 230.9
Stage 2 4 7 35.81 7.83 27.98 64.02 62.67 1.36 14 1 0 7.53 336.65
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,446.93 13,446.93 18,369.44 23,476.84 23,476.84 83.23 121.44 97.46
Potassium 473.76 473.76 646.99 826.67 826.67 3.46 5.03 4.04
Magnesium 1,462.12 1,462.12 1,999.96 2,558.92 2,558.92 1.96 2.88 2.30
Calcium 505.62 505.62 691.62 884.92 884.92 0.67 0.97 0.78
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,701.90 23,701.90 32,382.51 41,390.44 41,390.44 135.66 197.92 158.85
Sulfate 3,361.87 3,361.87 4,599.51 5,886.06 5,886.06 1.90 2.78 2.23
Nitrate 0.16 0.16 0.22 0.27 0.27 0.01 0.01 0.01
Carbonate 7.52 7.52 10.29 13.16 13.16 0.00 0.01 0.00
Bicarbonate 221.40 221.40 302.11 385.74 385.74 2.28 3.32 2.67
Boron 7.48 7.48 9.60 11.65 11.65 1.72 2.28 1.93
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.87 3.67 3.67 0.01 0.01 0.01
CO2 3.72 3.72 3.72 3.72 3.72 3.72 3.72 3.72
TDS 43,190.87 43,190.87 59,015.13 75,438.38 75,438.38 230.90 336.65 270.29
pH 7.60 7.60 7.67 7.73 7.73 6.07 6.22 6.13
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.49 13.12 5.97 0.20 16.03 1.09 43,184.05 131.32
LG SW 400 R G2
UHP2 7.68 0.42 11.22 5.43 0.18 14.11 1.08 45,918.11 161.37
LG SW 400 R G2
UHP3 7.26 0.35 9.53 4.88 0.16 12.33 1.07 48,546.32 198.49
LG SW 400 R G2
UHP4 6.91 0.30 8.05 4.33 0.15 10.71 1.06 51,026.45 244.13
LG SW 400 R G2
UHP5 6.61 0.25 6.78 3.81 0.14 9.26 1.05 53,326.83 299.94
LG SW 400 R G2
UHP6 6.36 0.21 5.68 3.32 0.13 7.98 1.05 55,427.65 367.77
LG SW 400 R G2
UHP7 6.14 0.18 4.76 2.88 0.13 6.85 1.04 57,320.49 449.66
Stage 2
LG SW 400 R G2
UHP1 8.95 0.44 11.73 4.87 0.23 17.41 1.07 59,006.74 196.79
LG SW 400 R G2
UHP2 8.52 0.37 9.96 4.35 0.22 15.39 1.06 62,016.57 240.88
LG SW 400 R G2
UHP3 8.15 0.31 8.43 3.85 0.20 13.57 1.06 64,822.96 294.24
LG SW 400 R G2
UHP4 7.83 0.26 7.13 3.38 0.19 11.93 1.05 67,404.12 358.32
LG SW 400 R G2
UHP5 7.57 0.22 6.02 2.96 0.18 10.47 1.04 69,750.68 434.72
LG SW 400 R G2
UHP6 7.34 0.19 5.09 2.58 0.17 9.18 1.04 71,863.54 525.07
LG SW 400 R G2
UHP7 7.15 0.16 4.32 2.24 0.16 8.04 1.03 73,751.44 631.09Perm. TDS Polarization# of elements
PositionSpecies2025-08-15 15:36:16
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 51.12 bar (1P)
Raw water flow: Raw water TDS: 43,190.87 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure: Specific energy: 4.97 kwh/m3
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,190.87 mg/L Specific energy: 4.97 kwh/m3
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 43 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.74 1.61
CaSO4 28.5 % 59.07 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.85 0.08
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,190.87 7.60
2 1P RO Feed 49.00 51.12 43,190.87 7.60
3 1P Brine 28.00 62.67 75,438.38 7.73
4 1P Product 21.00 1.00 270.29 6.13Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 44 ---
============================================================


============================================================
--- PAGE 45 ---
============================================================
v3.3.0.1
Water type: 0
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr 47.9 bar (1P)
49 m3/hr
28 m3/hr 30.92 bar
42.86 % 54.01 bar
System - Pass1
21 m3/hr 8.5 lmh 24 °C
49 m3/hr 9.23 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.92 bar 47.9 bar
70 54.01 bar 282.42 mg/L
ERD type: None 80 % 1
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.07 35.93 47.9 46.82 1.08 0 1 0 8.81 243.61
Stage 2 4 7 35.93 7.95 27.98 60.82 59.48 1.34 14 1 0 8.05 346.17
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,445.45 13,445.45 18,302.57 23,470.59 23,470.59 87.39 124.26 101.34
Potassium 473.71 473.71 644.64 826.44 826.44 3.63 5.15 4.20
Magnesium 1,461.95 1,461.95 1,992.78 2,558.49 2,558.49 2.07 2.94 2.40
Calcium 505.56 505.56 689.14 884.77 884.77 0.71 1.01 0.82
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,704.52 23,704.52 32,271.79 41,388.97 41,388.97 142.80 203.05 165.60
Sulfate 3,362.24 3,362.24 4,584.06 5,886.50 5,886.50 2.00 2.85 2.32
Nitrate 0.16 0.16 0.22 0.27 0.27 0.01 0.01 0.01
Carbonate 2.37 2.37 3.23 4.15 4.15 0.00 0.00 0.00
Bicarbonate 221.40 221.40 300.72 384.89 384.89 3.27 4.64 3.79
Boron 7.48 7.48 9.57 11.65 11.65 1.73 2.25 1.93
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.86 3.67 3.67 0.01 0.01 0.01
CO2 5.87 5.87 5.87 5.87 5.87 5.87 5.87 5.87
TDS 43,186.96 43,186.96 58,801.58 75,420.40 75,420.40 243.61 346.17 282.42
pH 7.60 7.60 7.72 7.82 7.82 5.94 6.09 6.00
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.56 15.88 6.87 0.20 11.65 1.10 43,180.23 120.77
LG SW 400 R G2
UHP2 7.61 0.45 12.69 5.89 0.18 9.64 1.08 46,354.98 159.01
LG SW 400 R G2
UHP3 7.16 0.36 10.06 4.96 0.16 7.90 1.07 49,246.25 208.98
LG SW 400 R G2
UHP4 6.80 0.28 7.95 4.12 0.15 6.44 1.06 51,807.40 273.66
LG SW 400 R G2
UHP5 6.52 0.22 6.26 3.39 0.14 5.23 1.05 54,023.87 356.60
LG SW 400 R G2
UHP6 6.30 0.17 4.94 2.77 0.13 4.23 1.04 55,906.72 461.79
LG SW 400 R G2
UHP7 6.13 0.14 3.90 2.25 0.13 3.42 1.03 57,484.13 593.43
Stage 2
LG SW 400 R G2
UHP1 8.98 0.51 14.42 5.67 0.23 12.88 1.08 58,793.57 177.12
LG SW 400 R G2
UHP2 8.47 0.40 11.46 4.78 0.21 10.77 1.07 62,316.09 231.86
LG SW 400 R G2
UHP3 8.07 0.32 9.10 3.98 0.20 8.97 1.06 65,430.06 301.62
LG SW 400 R G2
UHP4 7.75 0.26 7.23 3.30 0.19 7.45 1.05 68,130.85 389.49
LG SW 400 R G2
UHP5 7.49 0.20 5.77 2.72 0.18 6.19 1.04 70,439.65 498.87
LG SW 400 R G2
UHP6 7.29 0.16 4.62 2.24 0.17 5.14 1.03 72,393.01 633.15
LG SW 400 R G2
UHP7 7.13 0.13 3.72 1.84 0.16 4.27 1.03 74,035.22 795.94Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 11:27:35
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure:
Raw water flow: Raw water TDS: 43,186.96 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,186.96 mg/L Specific energy: 4.53 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 46 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.81 1.72
CaSO4 28.5 % 59.08 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.8 0.17
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,186.96 7.60
2 1P RO Feed 49.00 47.90 43,186.96 7.60
3 1P Brine 28.00 59.48 75,420.40 7.82
4 1P Product 21.00 1.00 282.42 6.00Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 47 ---
============================================================


============================================================
--- PAGE 48 ---
============================================================
v3.3.0.1
Water type: 1
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 30.92 bar
42.86 % 54 bar
System - Pass1
21 m3/hr 8.5 lmh 24 °C
49 m3/hr 9.76 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.92 bar 48.39 bar
70 54 bar 301.69 mg/L
ERD type: None 80 % 0.93
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.1 35.9 48.39 47.3 1.09 0 1 0 8.83 259.64
Stage 2 4 7 35.9 7.92 27.98 61.3 59.96 1.34 14 1 0 8.01 371.22
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,445.45 13,445.45 18,316.97 23,466.22 23,466.22 93.15 133.27 108.27
Potassium 473.71 473.71 645.13 826.25 826.25 3.87 5.53 4.49
Magnesium 1,461.95 1,461.95 1,994.54 2,558.45 2,558.45 2.20 3.15 2.56
Calcium 505.56 505.56 689.74 884.76 884.76 0.75 1.08 0.88
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,704.52 23,704.52 32,297.45 41,381.96 41,381.96 152.21 217.77 176.92
Sulfate 3,362.24 3,362.24 4,588.16 5,886.59 5,886.59 2.13 3.06 2.48
Nitrate 0.16 0.16 0.22 0.27 0.27 0.01 0.01 0.01
Carbonate 2.37 2.37 3.23 4.15 4.15 0.00 0.00 0.00
Bicarbonate 221.40 221.40 300.91 384.71 384.71 3.48 4.97 4.04
Boron 7.48 7.48 9.55 11.58 11.58 1.82 2.37 2.03
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.86 3.67 3.67 0.01 0.01 0.01
CO2 5.87 5.87 5.87 5.87 5.87 5.87 5.87 5.87
TDS 43,186.96 43,186.96 58,848.76 75,408.63 75,408.63 259.64 371.22 301.69
pH 7.60 7.60 7.72 7.82 7.82 5.97 6.12 6.02
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.55 15.53 6.71 0.20 12.25 1.10 43,180.23 131.89
LG SW 400 R G2
UHP2 7.62 0.44 12.56 5.82 0.18 10.24 1.08 46,279.08 171.60
LG SW 400 R G2
UHP3 7.17 0.36 10.08 4.96 0.16 8.50 1.07 49,128.12 222.96
LG SW 400 R G2
UHP4 6.82 0.28 8.05 4.17 0.15 7.00 1.06 51,679.99 288.82
LG SW 400 R G2
UHP5 6.53 0.23 6.42 3.47 0.14 5.75 1.05 53,915.32 372.50
LG SW 400 R G2
UHP6 6.31 0.18 5.11 2.86 0.13 4.70 1.04 55,838.30 477.72
LG SW 400 R G2
UHP7 6.13 0.14 4.09 2.35 0.13 3.84 1.03 57,469.77 608.37
Stage 2
LG SW 400 R G2
UHP1 8.97 0.50 14.03 5.52 0.23 13.48 1.08 58,840.83 193.45
LG SW 400 R G2
UHP2 8.48 0.40 11.28 4.70 0.21 11.38 1.07 62,266.32 250.26
LG SW 400 R G2
UHP3 8.08 0.32 9.06 3.96 0.20 9.58 1.06 65,322.23 321.95
LG SW 400 R G2
UHP4 7.76 0.26 7.28 3.31 0.19 8.04 1.05 67,999.82 411.42
LG SW 400 R G2
UHP5 7.50 0.21 5.86 2.76 0.18 6.74 1.04 70,313.56 521.77
LG SW 400 R G2
UHP6 7.30 0.17 4.74 2.29 0.17 5.65 1.03 72,292.86 656.21
LG SW 400 R G2
UHP7 7.13 0.14 3.86 1.91 0.16 4.75 1.03 73,974.99 817.79Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 11:25:28
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 48.39 bar (1P)
Raw water flow: Raw water TDS: 43,186.96 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,186.96 mg/L Specific energy: 4.57 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 49 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.81 1.72
CaSO4 28.5 % 59.09 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.8 0.17
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,186.96 7.60
2 1P RO Feed 49.00 48.39 43,186.96 7.60
3 1P Brine 28.00 59.96 75,408.63 7.82
4 1P Product 21.00 1.00 301.69 6.02Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 50 ---
============================================================


============================================================
--- PAGE 51 ---
============================================================
v3.3.0.5
Water type: 5
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 30.92 bar
42.86 % 53.95 bar
System - Pass1
21 m3/hr 8.07 lmh 24 °C
49 m3/hr 11.6 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 30.92 bar 49.96 bar
70 53.95 bar 393.52 mg/L
ERD type: None 80 % 0.7
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.18 35.82 49.96 48.86 1.09 0 1 0 8.44 336.71
Stage 2 4 7 35.82 7.84 27.98 62.86 61.51 1.35 14 1 0 7.54 488.96
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 13,447.27 13,447.27 18,349.18 23,444.23 23,444.23 121.50 176.55 142.04
Potassium 473.77 473.77 646.19 825.31 825.31 5.04 7.32 5.89
Magnesium 1,462.15 1,462.15 1,998.96 2,558.23 2,558.23 2.87 4.18 3.36
Calcium 505.63 505.63 691.27 884.69 884.69 0.97 1.41 1.14
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 23,701.30 23,701.30 32,347.03 41,335.36 41,335.36 197.99 287.75 231.48
Sulfate 3,361.78 3,361.78 4,597.40 5,885.22 5,885.22 2.78 4.04 3.25
Nitrate 0.16 0.16 0.22 0.27 0.27 0.01 0.01 0.01
Carbonate 8.40 8.40 11.49 14.70 14.70 0.01 0.01 0.01
Bicarbonate 221.40 221.40 301.62 384.83 384.83 3.33 4.83 3.89
Boron 7.48 7.48 9.42 11.27 11.27 2.20 2.85 2.44
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.87 3.67 3.67 0.01 0.01 0.01
CO2 3.46 3.46 3.46 3.46 3.46 3.46 3.46 3.46
TDS 43,191.46 43,191.46 58,955.65 75,347.81 75,347.81 336.71 488.96 393.52
pH 7.60 7.60 7.67 7.73 7.73 6.22 6.37 6.28
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.51 13.84 6.30 0.20 14.29 1.09 43,184.74 182.02
LG SW 400 R G2
UHP2 7.65 0.43 11.56 5.61 0.18 12.31 1.08 46,075.84 229.34
LG SW 400 R G2
UHP3 7.22 0.36 9.58 4.93 0.16 10.52 1.07 48,802.25 288.95
LG SW 400 R G2
UHP4 6.87 0.29 7.90 4.28 0.15 8.94 1.06 51,317.81 363.49
LG SW 400 R G2
UHP5 6.57 0.24 6.50 3.67 0.14 7.56 1.05 53,594.22 455.94
LG SW 400 R G2
UHP6 6.33 0.20 5.34 3.13 0.13 6.38 1.04 55,620.42 569.49
LG SW 400 R G2
UHP7 6.13 0.16 4.39 2.66 0.13 5.37 1.03 57,400.08 707.38
Stage 2
LG SW 400 R G2
UHP1 8.96 0.46 12.34 5.12 0.23 15.55 1.07 58,947.71 272.21
LG SW 400 R G2
UHP2 8.50 0.38 10.24 4.48 0.21 13.49 1.06 62,115.75 341.10
LG SW 400 R G2
UHP3 8.12 0.32 8.48 3.88 0.20 11.66 1.05 65,013.39 426.05
LG SW 400 R G2
UHP4 7.80 0.26 7.02 3.34 0.19 10.07 1.04 67,621.81 529.32
LG SW 400 R G2
UHP5 7.54 0.22 5.82 2.87 0.18 8.68 1.04 69,942.10 653.66
LG SW 400 R G2
UHP6 7.32 0.18 4.83 2.45 0.17 7.48 1.03 71,986.97 801.68
LG SW 400 R G2
UHP7 7.14 0.15 4.04 2.10 0.16 6.45 1.03 73,777.41 975.72Perm. TDS Polarization# of elements
PositionSpecies2025-08-15 15:35:38
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: Antofagasta 43K Membrane age:
Flux loss per year: Safety factor:
Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 49.96 bar (1P)
Raw water flow: Raw water TDS: 43,191.46 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure: Specific energy: 4.88 kwh/m3
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 43,191.46 mg/L Specific energy: 4.88 kwh/m3
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 52 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 0.82 1.69
CaSO4 28.5 % 59.09 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.79 0.14
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 43,191.46 7.60
2 1P RO Feed 49.00 49.96 43,191.46 7.60
3 1P Brine 28.00 61.51 75,347.81 7.73
4 1P Product 21.00 1.00 393.52 6.28Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 53 ---
============================================================


============================================================
--- PAGE 54 ---
============================================================
v3.3.0.1
Water type: 0
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 37.49 bar
42.86 % 65.53 bar
System - Pass1
21 m3/hr 8.5 lmh 19 °C
49 m3/hr 12.67 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 37.49 bar 60.63 bar
70 65.53 bar 241.82 mg/L
ERD type: None 80 % 1
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.85 35.14 60.63 59.56 1.06 0 1 0 9.34 198.05
Stage 2 4 7 35.14 7.16 27.98 75.56 74.24 1.32 16 1 0 7.25 326.45
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,578.86 16,578.86 23,086.77 28,969.17 28,969.17 71.10 117.26 86.83
Potassium 584.09 584.09 813.19 1,020.20 1,020.20 2.95 4.86 3.60
Magnesium 1,802.66 1,802.66 2,512.66 3,155.44 3,155.44 1.68 2.77 2.05
Calcium 623.38 623.38 868.91 1,091.20 1,091.20 0.57 0.95 0.70
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,229.56 29,229.56 40,707.01 51,083.09 51,083.09 116.17 191.61 141.89
Sulfate 4,145.79 4,145.79 5,779.55 7,259.02 7,259.02 1.63 2.69 1.99
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.01 0.01
Carbonate 2.83 2.83 3.94 4.95 4.95 0.00 0.00 0.00
Bicarbonate 273.00 273.00 379.58 475.67 475.67 2.66 4.38 3.24
Boron 7.48 7.48 9.93 11.98 11.98 1.27 1.91 1.49
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.93 3.67 3.67 0.01 0.01 0.01
CO2 7.68 7.68 7.68 7.68 7.68 7.68 7.68 7.68
TDS 53,249.96 53,249.96 74,164.77 93,074.75 93,074.75 198.05 326.45 241.82
pH 7.60 7.60 7.73 7.82 7.82 5.77 5.98 5.84
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.59 16.65 7.20 0.20 16.28 1.11 53,243.20 98.40
LG SW 400 R G2
UHP2 7.58 0.47 13.34 6.21 0.18 13.73 1.10 57,365.25 129.51
LG SW 400 R G2
UHP3 7.11 0.38 10.63 5.28 0.16 11.52 1.08 61,157.99 169.85
LG SW 400 R G2
UHP4 6.73 0.30 8.45 4.43 0.15 9.62 1.07 64,557.57 221.55
LG SW 400 R G2
UHP5 6.43 0.24 6.71 3.68 0.14 8.01 1.05 67,539.86 287.03
LG SW 400 R G2
UHP6 6.20 0.19 5.35 3.05 0.13 6.66 1.04 70,112.50 368.97
LG SW 400 R G2
UHP7 6.01 0.15 4.28 2.51 0.12 5.53 1.04 72,304.43 470.27
Stage 2
LG SW 400 R G2
UHP1 8.79 0.45 12.61 5.07 0.23 16.74 1.08 74,156.32 173.53
LG SW 400 R G2
UHP2 8.34 0.36 10.11 4.28 0.21 14.48 1.07 78,105.63 224.08
LG SW 400 R G2
UHP3 7.98 0.29 8.13 3.60 0.20 12.53 1.05 81,588.48 286.87
LG SW 400 R G2
UHP4 7.70 0.23 6.57 3.01 0.18 10.86 1.05 84,620.48 363.71
LG SW 400 R G2
UHP5 7.46 0.19 5.34 2.52 0.18 9.43 1.04 87,237.40 456.33
LG SW 400 R G2
UHP6 7.28 0.15 4.37 2.12 0.17 8.21 1.03 89,485.07 566.34
LG SW 400 R G2
UHP7 7.12 0.13 3.61 1.79 0.16 7.16 1.03 91,412.04 695.09Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 09:54:13
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 53K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 60.63 bar (1P)
Raw water flow: Raw water TDS: 53,249.96 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,249.96 mg/L Specific energy: 5.65 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 55 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1 2.03
CaSO4 37.24 % 78.02 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.61 0.53
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,249.96 7.60
2 1P RO Feed 49.00 60.63 53,249.96 7.60
3 1P Brine 28.00 74.24 93,074.75 7.82
4 1P Product 21.00 1.00 241.82 5.84Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 56 ---
============================================================


============================================================
--- PAGE 57 ---
============================================================
v3.3.0.1
Water type: 1
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 37.49 bar
42.86 % 65.52 bar
System - Pass1
21 m3/hr 8.5 lmh 19 °C
49 m3/hr 13.44 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 37.49 bar 61.36 bar
70 65.52 bar 258.41 mg/L
ERD type: None 80 % 0.93
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.89 35.11 61.36 60.3 1.07 0 1 0 9.37 211.16
Stage 2 4 7 35.11 7.13 27.98 76.3 74.97 1.32 16 1 0 7.22 350.41
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,578.86 16,578.86 23,106.01 28,965.00 28,965.00 75.81 125.88 92.80
Potassium 584.09 584.09 813.86 1,020.03 1,020.03 3.15 5.22 3.85
Magnesium 1,802.66 1,802.66 2,514.92 3,155.37 3,155.37 1.79 2.98 2.19
Calcium 623.38 623.38 869.69 1,091.17 1,091.17 0.61 1.02 0.75
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,229.56 29,229.56 40,741.19 51,076.36 51,076.36 123.87 205.69 151.64
Sulfate 4,145.79 4,145.79 5,784.81 7,259.00 7,259.00 1.74 2.89 2.13
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.01 0.01
Carbonate 2.83 2.83 3.95 4.95 4.95 0.00 0.00 0.00
Bicarbonate 273.00 273.00 379.85 475.50 475.50 2.83 4.70 3.47
Boron 7.48 7.48 9.91 11.92 11.92 1.34 2.02 1.57
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.93 3.67 3.67 0.01 0.01 0.01
CO2 7.68 7.68 7.68 7.68 7.68 7.68 7.68 7.68
TDS 53,249.96 53,249.96 74,227.41 93,063.34 93,063.34 211.16 350.41 258.41
pH 7.60 7.60 7.73 7.82 7.82 5.80 6.01 5.87
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.58 16.31 7.05 0.20 17.15 1.11 53,243.20 107.33
LG SW 400 R G2
UHP2 7.59 0.47 13.22 6.15 0.18 14.61 1.09 57,275.17 139.72
LG SW 400 R G2
UHP3 7.12 0.38 10.65 5.28 0.16 12.37 1.08 61,017.75 181.37
LG SW 400 R G2
UHP4 6.75 0.30 8.55 4.47 0.15 10.43 1.07 64,406.35 234.32
LG SW 400 R G2
UHP5 6.45 0.24 6.86 3.76 0.14 8.77 1.06 67,411.32 300.90
LG SW 400 R G2
UHP6 6.20 0.19 5.52 3.14 0.13 7.37 1.05 70,032.51 383.64
LG SW 400 R G2
UHP7 6.01 0.16 4.45 2.62 0.12 6.18 1.04 72,290.58 485.23
Stage 2
LG SW 400 R G2
UHP1 8.78 0.43 12.30 4.95 0.23 17.58 1.08 74,219.02 189.33
LG SW 400 R G2
UHP2 8.34 0.35 9.97 4.22 0.21 15.33 1.06 78,073.05 242.00
LG SW 400 R G2
UHP3 7.99 0.29 8.09 3.57 0.20 13.37 1.05 81,499.71 306.93
LG SW 400 R G2
UHP4 7.71 0.23 6.59 3.02 0.18 11.68 1.05 84,508.56 385.85
LG SW 400 R G2
UHP5 7.47 0.19 5.40 2.55 0.18 10.23 1.04 87,128.10 480.39
LG SW 400 R G2
UHP6 7.28 0.16 4.46 2.16 0.17 8.97 1.03 89,397.20 592.04
LG SW 400 R G2
UHP7 7.13 0.13 3.71 1.84 0.16 7.89 1.03 91,358.44 722.09Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 09:54:47
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 53K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 61.36 bar (1P)
Raw water flow: Raw water TDS: 53,249.96 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,249.96 mg/L Specific energy: 5.71 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 58 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1 2.03
CaSO4 37.24 % 78.02 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.61 0.53
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,249.96 7.60
2 1P RO Feed 49.00 61.36 53,249.96 7.60
3 1P Brine 28.00 74.97 93,063.34 7.82
4 1P Product 21.00 1.00 258.41 5.87Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 59 ---
============================================================


============================================================
--- PAGE 60 ---
============================================================
v3.3.0.5
Water type: 5
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 37.49 bar
42.86 % 65.48 bar
System - Pass1
21 m3/hr 8.07 lmh 19 °C
49 m3/hr 16.13 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 37.49 bar 63.77 bar
70 65.48 bar 337.47 mg/L
ERD type: None 80 % 0.7
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.97 35.02 63.77 62.7 1.07 0 1 0 8.95 273.98
Stage 2 4 7 35.02 7.05 27.98 78.7 77.37 1.33 16 1 0 6.77 463.37
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,581.51 16,581.51 23,157.24 28,948.30 28,948.30 98.91 167.39 121.87
Potassium 584.18 584.18 815.61 1,019.31 1,019.31 4.10 6.95 5.05
Magnesium 1,802.95 1,802.95 2,521.30 3,155.41 3,155.41 2.34 3.96 2.88
Calcium 623.48 623.48 871.90 1,091.19 1,091.19 0.79 1.34 0.98
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,224.86 29,224.86 40,819.81 51,033.44 51,033.44 161.19 272.82 198.62
Sulfate 4,145.12 4,145.12 5,797.92 7,257.43 7,257.43 2.26 3.83 2.79
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.01 0.01
Carbonate 11.61 11.61 16.24 20.33 20.33 0.01 0.01 0.01
Bicarbonate 273.00 273.00 380.83 475.61 475.61 2.71 4.58 3.34
Boron 7.48 7.48 9.81 11.65 11.65 1.65 2.47 1.92
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.94 3.67 3.67 0.01 0.01 0.01
CO2 4.19 4.19 4.19 4.19 4.19 4.19 4.19 4.19
TDS 53,256.51 53,256.51 74,393.88 93,016.70 93,016.70 273.98 463.37 337.47
pH 7.60 7.60 7.67 7.72 7.72 6.09 6.30 6.17
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.54 14.64 6.66 0.20 20.15 1.10 53,249.75 147.22
LG SW 400 R G2
UHP2 7.62 0.45 12.22 5.96 0.18 17.62 1.09 57,039.66 186.10
LG SW 400 R G2
UHP3 7.17 0.38 10.14 5.25 0.16 15.32 1.08 60,641.40 235.00
LG SW 400 R G2
UHP4 6.79 0.31 8.37 4.58 0.15 13.26 1.06 63,991.80 295.97
LG SW 400 R G2
UHP5 6.48 0.26 6.90 3.96 0.14 11.45 1.06 67,050.48 371.22
LG SW 400 R G2
UHP6 6.22 0.21 5.69 3.40 0.13 9.87 1.05 69,799.44 463.08
LG SW 400 R G2
UHP7 6.01 0.17 4.70 2.91 0.12 8.50 1.04 72,239.53 573.95
Stage 2
LG SW 400 R G2
UHP1 8.76 0.41 10.92 4.64 0.23 20.49 1.07 74,385.47 264.30
LG SW 400 R G2
UHP2 8.35 0.34 9.09 4.04 0.21 18.26 1.06 77,988.09 328.82
LG SW 400 R G2
UHP3 8.01 0.28 7.57 3.51 0.20 16.27 1.05 81,261.74 406.88
LG SW 400 R G2
UHP4 7.73 0.23 6.32 3.04 0.19 14.52 1.04 84,202.30 499.94
LG SW 400 R G2
UHP5 7.50 0.20 5.29 2.62 0.18 12.99 1.04 86,822.73 609.75
LG SW 400 R G2
UHP6 7.30 0.17 4.45 2.27 0.17 11.64 1.03 89,144.70 737.50
LG SW 400 R G2
UHP7 7.13 0.14 3.77 1.97 0.16 10.46 1.03 91,196.11 884.05Perm. TDS Polarization# of elements
PositionSpecies2025-08-14 17:02:30
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: Antofagasta 53k Membrane age:
Flux loss per year: Safety factor:
Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 63.77 bar (1P)
Raw water flow: Raw water TDS: 53,256.51 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure: Specific energy: 6.09 kwh/m3
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,256.51 mg/L Specific energy: 6.09 kwh/m3
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 61 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1.01 2
CaSO4 37.23 % 78.02 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.6 0.5
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,256.51 7.60
2 1P RO Feed 49.00 63.77 53,256.51 7.60
3 1P Brine 28.00 77.37 93,016.70 7.72
4 1P Product 21.00 1.00 337.47 6.17Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 62 ---
============================================================


============================================================
--- PAGE 63 ---
============================================================
v3.3.0.1
Water type: 0
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 38.13 bar
42.86 % 66.59 bar
System - Pass1
21 m3/hr 8.5 lmh 24 °C
49 m3/hr 11.17 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 38.13 bar 59.89 bar
70 66.59 bar 352.6 mg/L
ERD type: None 80 % 1
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.88 35.12 59.89 58.84 1.06 0 1 0 9.36 288.64
Stage 2 4 7 35.12 7.14 27.98 74.84 73.52 1.32 16 1 0 7.23 476.82
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,579.05 16,579.05 23,088.29 28,940.92 28,940.92 103.69 171.39 126.70
Potassium 584.10 584.10 813.17 1,019.02 1,019.02 4.30 7.11 5.26
Magnesium 1,802.68 1,802.68 2,513.93 3,154.91 3,154.91 2.45 4.06 3.00
Calcium 623.39 623.39 869.35 1,091.02 1,091.02 0.84 1.39 1.02
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,229.23 29,229.23 40,710.45 51,036.18 51,036.18 169.43 280.08 207.04
Sulfate 4,145.74 4,145.74 5,782.74 7,258.62 7,258.62 2.38 3.93 2.91
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.01 0.01
Carbonate 3.18 3.18 4.43 5.56 5.56 0.00 0.00 0.00
Bicarbonate 273.00 273.00 379.33 474.57 474.57 3.88 6.39 4.73
Boron 7.48 7.48 9.78 11.66 11.66 1.66 2.44 1.92
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.93 3.67 3.67 0.01 0.01 0.01
CO2 7.08 7.08 7.08 7.08 7.08 7.08 7.08 7.08
TDS 53,250.15 53,250.15 74,174.70 92,996.50 92,996.50 288.64 476.82 352.60
pH 7.60 7.60 7.73 7.82 7.82 5.93 6.14 6.00
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.63 17.75 7.68 0.20 14.72 1.11 53,243.49 135.46
LG SW 400 R G2
UHP2 7.54 0.49 13.77 6.45 0.17 12.09 1.09 57,658.57 184.40
LG SW 400 R G2
UHP3 7.05 0.38 10.63 5.32 0.16 9.87 1.08 61,618.49 249.43
LG SW 400 R G2
UHP4 6.68 0.29 8.20 4.33 0.14 8.03 1.06 65,065.71 334.47
LG SW 400 R G2
UHP5 6.39 0.22 6.35 3.51 0.14 6.52 1.05 67,998.72 443.93
LG SW 400 R G2
UHP6 6.16 0.17 4.94 2.83 0.13 5.30 1.04 70,453.73 582.17
LG SW 400 R G2
UHP7 5.99 0.14 3.88 2.29 0.12 4.32 1.03 72,488.56 753.75
Stage 2
LG SW 400 R G2
UHP1 8.78 0.47 13.24 5.32 0.23 15.06 1.08 74,166.75 240.12
LG SW 400 R G2
UHP2 8.31 0.36 10.32 4.38 0.21 12.76 1.06 78,324.07 319.11
LG SW 400 R G2
UHP3 7.95 0.29 8.08 3.59 0.19 10.84 1.05 81,898.81 418.85
LG SW 400 R G2
UHP4 7.66 0.23 6.39 2.94 0.18 9.23 1.04 84,933.36 542.29
LG SW 400 R G2
UHP5 7.44 0.18 5.10 2.42 0.18 7.88 1.03 87,491.44 692.00
LG SW 400 R G2
UHP6 7.26 0.15 4.11 2.00 0.17 6.76 1.03 89,642.99 869.96
LG SW 400 R G2
UHP7 7.11 0.12 3.36 1.67 0.16 5.82 1.02 91,455.15 1,077.42Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 09:53:27
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 53K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 59.89 bar (1P)
Raw water flow: Raw water TDS: 53,250.15 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,250.15 mg/L Specific energy: 5.59 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 64 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1.08 2.11
CaSO4 37.24 % 78.04 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.55 0.59
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,250.15 7.60
2 1P RO Feed 49.00 59.89 53,250.15 7.60
3 1P Brine 28.00 73.52 92,996.50 7.82
4 1P Product 21.00 1.00 352.60 6.00Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 65 ---
============================================================


============================================================
--- PAGE 66 ---
============================================================
v3.3.0.1
Water type: 1
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr 60.5 bar (1P)
49 m3/hr
28 m3/hr 38.13 bar
42.86 % 66.58 bar
System - Pass1
21 m3/hr 8.5 lmh 24 °C
49 m3/hr 11.82 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 38.13 bar 60.5 bar
70 66.58 bar 376.7 mg/L
ERD type: None 80 % 0.93
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.91 35.09 60.5 59.44 1.06 0 1 0 9.38 307.69
Stage 2 4 7 35.09 7.11 27.98 75.44 74.12 1.32 16 1 0 7.2 511.62
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,579.05 16,579.05 23,105.76 28,933.99 28,933.99 110.54 183.92 135.37
Potassium 584.10 584.10 813.76 1,018.74 1,018.74 4.59 7.63 5.62
Magnesium 1,802.68 1,802.68 2,516.07 3,154.72 3,154.72 2.61 4.35 3.20
Calcium 623.39 623.39 870.09 1,090.95 1,090.95 0.89 1.49 1.09
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,229.23 29,229.23 40,741.62 51,024.85 51,024.85 180.62 300.55 221.21
Sulfate 4,145.74 4,145.74 5,787.76 7,258.38 7,258.38 2.53 4.22 3.10
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.02 0.01
Carbonate 3.18 3.18 4.44 5.56 5.56 0.00 0.00 0.00
Bicarbonate 273.00 273.00 379.56 474.32 474.32 4.13 6.86 5.06
Boron 7.48 7.48 9.75 11.58 11.58 1.74 2.56 2.02
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.93 3.67 3.67 0.01 0.01 0.01
CO2 7.08 7.08 7.08 7.08 7.08 7.08 7.08 7.08
TDS 53,250.15 53,250.15 74,232.04 92,977.12 92,977.12 307.69 511.62 376.70
pH 7.60 7.60 7.73 7.82 7.82 5.96 6.17 6.03
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.61 17.37 7.51 0.20 15.48 1.11 53,243.49 147.56
LG SW 400 R G2
UHP2 7.55 0.48 13.64 6.37 0.17 12.85 1.09 57,553.16 198.36
LG SW 400 R G2
UHP3 7.07 0.38 10.66 5.32 0.16 10.61 1.08 61,457.63 265.21
LG SW 400 R G2
UHP4 6.70 0.29 8.32 4.39 0.14 8.73 1.06 64,895.79 351.87
LG SW 400 R G2
UHP5 6.40 0.23 6.51 3.59 0.14 7.17 1.05 67,856.78 462.44
LG SW 400 R G2
UHP6 6.17 0.18 5.12 2.93 0.13 5.89 1.04 70,365.99 601.48
LG SW 400 R G2
UHP7 5.99 0.14 4.06 2.39 0.12 4.84 1.03 72,468.97 771.99
Stage 2
LG SW 400 R G2
UHP1 8.77 0.46 12.90 5.19 0.22 15.79 1.08 74,224.17 264.67
LG SW 400 R G2
UHP2 8.32 0.36 10.17 4.32 0.21 13.50 1.06 78,273.45 347.67
LG SW 400 R G2
UHP3 7.96 0.28 8.05 3.57 0.19 11.57 1.05 81,788.00 451.59
LG SW 400 R G2
UHP4 7.67 0.23 6.42 2.95 0.18 9.94 1.04 84,800.70 579.20
LG SW 400 R G2
UHP5 7.45 0.18 5.17 2.45 0.18 8.56 1.03 87,364.99 732.92
LG SW 400 R G2
UHP6 7.26 0.15 4.21 2.04 0.17 7.41 1.03 89,541.85 914.55
LG SW 400 R G2
UHP7 7.12 0.12 3.46 1.72 0.16 6.44 1.02 91,391.40 1,125.00Perm. TDS Polarization# of elements
PositionSpecies2025-06-19 09:57:39
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: AFT_53PPM_Chile Antofagasta 53K Membrane age:
Flux loss per year: Safety factor:
Jiyoung Rowley Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure:
Raw water flow: Raw water TDS: 53,250.15 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure:
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,250.15 mg/L Specific energy: 5.64 kWh/m³
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 67 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1.08 2.11
CaSO4 37.24 % 78.04 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.55 0.59
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,250.15 7.60
2 1P RO Feed 49.00 60.50 53,250.15 7.60
3 1P Brine 28.00 74.12 92,977.12 7.82
4 1P Product 21.00 1.00 376.70 6.03Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 68 ---
============================================================


============================================================
--- PAGE 69 ---
============================================================
v3.3.0.5
Water type: 5
Customer: 7.00% 1
Username: 7.00%
Overall System
21 m3/hr
49 m3/hr
28 m3/hr 38.13 bar
42.86 % 66.51 bar
System - Pass1
21 m3/hr 8.07 lmh 24 °C
49 m3/hr 14.12 bar
28 m3/hr Feed TDS:
Recovery: 42.86 % 38.13 bar 62.45 bar
70 66.51 bar 491.48 mg/L
ERD type: None 80 % 0.7
RO feed Permeate Conc. RO feed Conc. Vessel Boost Back Inter-stage Average
flow flow flow pressure pressure DP pressure pressurepressure
lossflux
m3/hr m3/hr m3/hr bar bar bar bar bar bar lmh mg/L
Stage 1 6 7 49 13.99 35.01 62.45 61.38 1.07 0 1 0 8.96 398.97
Stage 2 4 7 35.01 7.03 27.98 77.38 76.06 1.32 16 1 0 6.76 675.55
Stage1 Stage2 Composite Stage1 Stage2 Composite
Ammonium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Sodium 16,582.00 16,582.00 23,150.36 28,906.61 28,906.61 144.14 244.24 177.62
Potassium 584.20 584.20 815.25 1,017.57 1,017.57 5.98 10.13 7.37
Magnesium 1,803.00 1,803.00 2,522.10 3,154.44 3,154.44 3.41 5.78 4.20
Calcium 623.50 623.50 872.18 1,090.86 1,090.86 1.15 1.95 1.42
Strontium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Barium 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Fluoride 0.01 0.01 0.01 0.02 0.02 0.00 0.00 0.00
Chloride 29,223.99 29,223.99 40,807.64 50,962.52 50,962.52 234.91 398.06 289.48
Sulfate 4,145.00 4,145.00 5,799.97 7,256.09 7,256.09 3.29 5.59 4.06
Nitrate 0.20 0.20 0.28 0.34 0.34 0.01 0.02 0.01
Carbonate 12.98 12.98 18.16 22.72 22.72 0.01 0.02 0.01
Bicarbonate 273.00 273.00 380.51 474.45 474.45 3.95 6.68 4.86
Boron 7.48 7.48 9.62 11.27 11.27 2.11 3.06 2.43
Bromide 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Silica 2.10 2.10 2.94 3.67 3.67 0.01 0.01 0.01
CO2 3.89 3.89 3.89 3.89 3.89 3.89 3.89 3.89
TDS 53,257.46 53,257.46 74,379.01 92,900.58 92,900.58 398.97 675.55 491.48
pH 7.60 7.60 7.67 7.72 7.72 6.24 6.45 6.32
RO feed Permeate Element Element Net driving
flow flow recovery DP pressure
m3/hr m3/hr lmh % bar bar mg/L mg/L
Stage 1
LG SW 400 R G2
UHP1 8.17 0.58 15.49 7.05 0.20 18.08 1.10 53,250.80 203.33
LG SW 400 R G2
UHP2 7.59 0.47 12.59 6.16 0.18 15.46 1.08 57,274.78 264.26
LG SW 400 R G2
UHP3 7.12 0.38 10.17 5.31 0.16 13.15 1.07 61,020.07 342.44
LG SW 400 R G2
UHP4 6.74 0.30 8.20 4.52 0.15 11.14 1.06 64,421.14 441.47
LG SW 400 R G2
UHP5 6.44 0.25 6.61 3.81 0.14 9.42 1.05 67,447.44 565.12
LG SW 400 R G2
UHP6 6.19 0.20 5.34 3.20 0.13 7.96 1.04 70,098.48 717.19
LG SW 400 R G2
UHP7 6.00 0.16 4.34 2.69 0.12 6.74 1.03 72,395.04 901.08
Stage 2
LG SW 400 R G2
UHP1 8.75 0.42 11.40 4.84 0.22 18.31 1.07 74,371.09 369.14
LG SW 400 R G2
UHP2 8.33 0.34 9.26 4.13 0.21 16.04 1.06 78,133.66 470.15
LG SW 400 R G2
UHP3 7.98 0.28 7.55 3.51 0.20 14.08 1.05 81,482.07 593.76
LG SW 400 R G2
UHP4 7.70 0.23 6.19 2.98 0.18 12.39 1.04 84,428.15 742.49
LG SW 400 R G2
UHP5 7.47 0.19 5.10 2.54 0.18 10.93 1.03 87,001.72 918.34
LG SW 400 R G2
UHP6 7.28 0.16 4.24 2.16 0.17 9.68 1.03 89,242.05 1,122.51
LG SW 400 R G2
UHP7 7.13 0.13 3.56 1.86 0.16 8.61 1.02 91,191.71 1,355.43Perm. TDS Polarization# of elements
PositionSpecies2025-08-14 17:01:39
Raw waterPerm. TDS
Adjusted feed
Feed TDSPermeate Conc.# of vessels
FluxProject name: Antofagasta 53k Membrane age:
Flux loss per year: Safety factor:
Salt passage increase:
Total permeate flow: Water source: Seawater-Open Intake (SDI<5) Feed pressure: 62.45 bar (1P)
Raw water flow: Raw water TDS: 53,257.46 mg/L
Total concentrate flow: Feed osmotic pressure:
Overall recovery: Concentrate osmotic pressure: Specific energy: 5.99 kwh/m3
Permeate flow: Average flux: Temperature:
RO feed flow: Water source: Seawater-Open Intake (SDI<5) Average NDP:
Concentrate flow: 53,257.46 mg/L Specific energy: 5.99 kwh/m3
Feed osmotic pressure: Feed pressure:
Number of elements: Concentrate osmotic pressure: Permeate TDS:
Pump efficiency: Fouling factor:
Recirculation:
Water Analysis - Pass1
Within Vessels - Pass1


============================================================
--- PAGE 70 ---
============================================================
Solubility - Pass1
Feed Conc.
LSI 1.09 2.08
CaSO4 37.23 % 78.04 %
SrSO4 0 % 0 %
BaSO4 0 % 0 %
CaF2 0 % 0.01 %
SiO2 0 % 0 %
Stiff Davis Index -0.53 0.56
Warnings - Pass1
# Stream Flow (m3/hr)Pressure
(bar)TDS (mg/L) pH
1 Raw Feed 49.00 0.00 53,257.46 7.60
2 1P RO Feed 49.00 62.45 53,257.46 7.60
3 1P Brine 28.00 76.06 92,900.58 7.72
4 1P Product 21.00 1.00 491.48 6.32Solubility calculation
Disclaimer: LG Chem Design is intended to be used by persons having the requisite technical skill, at their own discretion and risk.
When using LG Chem Design, it is the user's responsibility to make provisions against fouling, scaling and chemical attacks, to account for piping and valve pressure losses, feed pump suction pressure and permeate backpressure.
LG Chem shall not be liable for any error or miscalculation in results obtained by using LG Chem Design.
Because use conditions and applicable laws may differ from one location to another and may change with time,users are responsible for determining whether products are appropriate for their use.


============================================================
--- PAGE 71 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.71 
 
7.1 TURBO CHARGER PROJECTION 
The Turbo Charger Projection is included after this page. 
Please note the projection calculation is based on 1Y, 0Y 19Co – 24Co and pressure Safety Margin 
applied into Projected Value (19Co cases) is 10%.   
 

============================================================
--- PAGE 72 ---
============================================================
Date:
Project #6/25/2025  -  4:12 PM BiTurbo™ Performance
71332_LG_R2
Version 2.29-D
NOTE: All data are based on reasonable engineering es Ɵmates. Not for design purposes.  Version 2.29-D1st STAGE 2nd STAGE
Feed TDS     Qf             Pf           Qr            Pr                 Qf           Pf           Qr             Pr           Pex         Time      Comments
   (ppm)     (m3/h)     (bar)      (m3/h)     (bar)            (m3/h)    (bar)     (m3/h)     (bar)        (bar)
1 53000 49.0 67.50 35.1 66.30 35.1 83.90 27.9 82.40 1.00 0.100 19C_Y1 x 10%
2 53000 49.0 66.70 35.1 65.50 35.1 83.10 27.9 81.60 1.00 0.100 19C_Y0 x 10%
3 53000 49.0 61.30 35.1 60.30 35.1 76.30 27.9 74.90 1.00 0.100 19C_Y1
4 53000 49.0 60.60 35.1 59.50 35.1 75.50 27.9 74.20 1.00 0.100 19C_Y0
5 53000 49.0 60.50 35.0 59.40 35.0 75.40 27.9 74.10 1.00 0.100 24C_Y1
6 53000 49.0 59.80 35.1 58.80 35.1 74.80 27.9 73.50 1.00 0.100 24C_Y0
7 43000 49.0 49.10 35.8 48.00 35.8 62.00 27.9 60.70 1.00 0.100 19C_Y1
8 43000 49.0 48.50 35.9 47.40 35.9 61.40 27.9 60.10 1.00 0.100 19C_Y0
9 43000 49.0 48.30 35.9 47.30 35.9 61.30 27.9 59.90 1.00 0.100 24C_Y1
10 43000 49.0 47.90 35.9 46.80 35.9 60.80 27.9 59.40 1.00 0.100 24C_Y0
TERMINOLOGYPf  =  Feed pressure to turbo
Qf  =  Feed ﬂow to membrane
Pf   =  membrane pressure
∆Pf  =  turbo feed pressure boost
Qr  =  brine from membrane
∆Pr  =  brine pressure drop through turbo
Pex  =  brine pressure at turbo outlet
Neﬀ  =  turbo transfer e ﬃciency
Kvt  =  brine ﬂow coeﬃcient through turbo
Aux  =  aux valve posi Ɵon
Qbyp  =  brine bypass ﬂow around turbo
CvByp  =  ﬂow coeﬀ. of brine bypass valve (if used)
HPP pressure o ﬀset: (bar) 0.00Pipe Pressure Losses
∆P1
∆P2
∆P3
∆P4
∆P5
∆P60.30
0.30
0.20
0.20
0.20
0.20Feed & pretreatment data
Pump eﬀ
Mot eﬀ
VFD eﬀ
Total ∆P0.00
0.00
0.00
00.00TURBO CASE ANALYSIS
Pﬁn∆Pf Qf ∆Pr Qt Pex Ne ﬀ Qbyp Aux
(bar) (bar) (m3/h) (bar) (m3/h) (bar) (m3/h)Kvt KvByp
Pt   Stg
1 1 47.8 20.0 49.0 49.9 27.9 1.0 0.704 4.11 Part 0.0 0.0
2 66.1 18.0 35.1 31.1 27.9 51.1 0.727 5.20 Part 0.0 0.0
2 1 47.3 19.7 49.0 49.1 27.9 1.0 0.703 4.14 Part 0.0 0.0
2 65.3 18.0 35.1 31.1 27.9 50.3 0.727 5.20 Part 0.0 0.0
3 1 43.7 17.9 49.0 44.9 27.9 1.0 0.699 4.33 Part 0.0 0.0
2 60.1 16.4 35.1 28.6 27.9 46.1 0.721 5.42 Part 0.0 0.0
4 1 43.3 17.6 49.0 44.2 27.9 1.0 0.699 4.36 Part 0.0 0.0
2 59.3 16.4 35.1 28.6 27.9 45.4 0.721 5.42 Part 0.0 0.0
5 1 43.2 17.6 49.0 44.1 27.9 1.0 0.699 4.37 Part 0.0 0.0
2 59.2 16.4 35.0 28.6 27.9 45.3 0.720 5.43 Part 0.0 0.0
6 1 42.8 17.3 49.0 43.5 27.9 1.0 0.698 4.40 Part 0.0 0.0
2 58.6 16.4 35.1 28.6 27.9 44.7 0.721 5.42 Part 0.0 0.0
7 1 36.8 12.6 49.0 33.6 26.8 1.0 0.687 4.77 Open 1.1 0.2
2 47.8 14.4 35.8 25.7 28.1 34.8 0.714 5.72 Open 0.0 0.0
8 1 36.7 12.1 49.0 32.8 26.4 1.0 0.686 4.77 Open 1.5 0.3
2 47.2 14.4 35.9 25.9 27.9 34.0 0.714 5.66 Part 0.0 0.0
9 1 36.6 12.0 49.0 32.6 26.4 1.0 0.685 4.77 Open 1.5 0.3
2 47.1 14.4 35.9 25.9 27.9 33.8 0.714 5.66 Part 0.0 0.0
10 1 36.5 11.7 49.0 32.1 26.2 1.0 0.684 4.77 Open 1.7 0.3
2 46.6 14.4 35.9 25.9 27.9 33.3 0.714 5.66 Part 0.0 0.0

============================================================
--- PAGE 73 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.73 
 
8. PROTOCOLS  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Protocolos a utilizar”) 
To ensure seamless integration and reliable data exchange within the Ultra High-Pressure Reverse 
Osmosis (UHPRO) system, the following communication protocols have been considered: 
 EtherNet/IP  – Facilitates high-speed, deterministic communication between the PLC and field 
devices, supporting real-time control and diagnostics. 
 Modbus TCP/IP  – Enables robust and standardized communication between the PLC and the 
Client’s main control system, ensuring interoperability across platforms. 
 4-20mA with HART Protocol  – Provides analog signal transmission with digital overlay for 
enhanced device diagnostics and configuration, particularly for pressure and flow transmitters. 
The final selection of protocols will be confirmed during the execution phase of the project. These 
decisions will be documented in the engineering submittals and will reflect the outcomes of technical 
discussions and mutual agreement on the finalized scope of work. 
 

============================================================
--- PAGE 74 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.74 
 
9. CONTROL PHILOSOPHY 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Filosofía de control”) 
 
CONTROL PHILOSOPHY (Preliminary Description) 
The Ultra High-Pressure Reverse Osmosis (UHPRO) train will have a PLC and operator interface that 
controls the on-skid valves and feed pump and monitors on-skid instrumentation. The UHPRO train will 
be designed to normally operate automatically.  
OPERATOR INTERFACE AND SCREENS 
The operator interface screens will be developed and provided by BW Water Americas (BWWA or BW 
Water) after system integration is carried out during the project execution phase.  
Some actual screens will be then taken from the design software showing all the screen elements.  
Overview (Primary) screen  
 Displays the operational status  of the UHPRO train. 
 Hosts the primary operator controls . 
 Displays  Valve status indicators : 
o Red icons : Valve closed 
o Green icons : Valve open 
A symbolic example from a non-UHPRO project is shown for reference; actual screens may differ after 
system integration. 

============================================================
--- PAGE 75 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.75 
 
Picture: Overview (primary)Screen - for reference only
 
Screen Navigation 
 Accessed via the Screen Navigation button on the Overview screen. 
 Provides access to: 
o Equipment Controls 
o Alarm Setpoints 
o Alarm History 
o Tech Support 
o Alarm Configuration 
o System Configuration 


============================================================
--- PAGE 76 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.76 
 
 Permeate Flush sequence can be toggled (enabled or disabled) from this screen, but only after 
entering the System Configuration Access Code (provided by BW Water). 
 The System Configuration Access Code allows to access the Alarm Config and System Config 
screens.  
 
Picture: Screen Navigation Sample - for reference only 
 
Equipment Controls 
 Accessed via the Equipment Controls button on the Screen Navigation (first picture below) or 
by touching component icons on the Overview screen of these component control pop-up 
window (second picture below). 
 Allows direct control of individual components. 
 Used for maintenance and troubleshooting. 
 


============================================================
--- PAGE 77 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.77 
 
Picture: Equipment Controls Button Screen Sample - for reference only
 
Component Control Pop-Up Windows 
 Accessed via the Component icon on the Overview Screen (second picture below)  
 During normal operation, all components should be set to Auto. 
 


============================================================
--- PAGE 78 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.78 
 
Picture: Component Control Pop-Up Windows Icon - for reference only
 
Alarm Setpoints 
 Accessed via the Alarm Setpoints button on the Screen Navigation screen (see picture below) 
 Used to configure alarm thresholds. 
 


============================================================
--- PAGE 79 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.79 
 
Picture: Alarm Setpoint Screen - for reference only  
 
Alarm History 
 Accessed via the Alarm History button. 
 Displays historical alarm data for diagnostics and review. 
 


============================================================
--- PAGE 80 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.80 
 
Picture: Alarm History Screen - for reference only
 
Tech Support 
 Accessed via the Tech Support button. 
 Requires a Hardware Configuration Access Code (provided by BW-Water). 
 
Picture: Tech Support Screen Sample - for reference only
 


============================================================
--- PAGE 81 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.81 
 
Alarm - Configuration 1 
 Accessed via the Alarm Config button. 
 Allows enabling/disabling alarms and adjusting delay times. 
 Requires the System Configuration Access Code (provided by BW-Water). 
 
Picture: Alarm Config.1 Screen - for reference only  
 
Alarm - Configuration 2 
 Accessed from the Alarm Config 1 screen by clicking Alarm Config 2 button 
 Displays spare alarms. 


============================================================
--- PAGE 82 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.82 
 
Picture: Alarm Config.2 Screen  - for reference only  
 
System Configuration 
 Accessed via the System Config button on the Screen Navigation 
 Allows adjustment of: 
o PID loop parameters 
o Analog instrument ranges 
o Operator interface date and time 
 Requires the System Configuration Access Code (provided by BW-Water) 


============================================================
--- PAGE 83 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.83 
 
Picture: System Configuration  Screen - for reference only  
 
Pre-Start-Up Review - – UHPRO Train 
If the UHPRO train remains offline for an extended period due to chemical cleaning, maintenance, or 
repairs, the operator must perform a pre-start-up review before initiating UHPRO Train/system  start-
up. 
The operator should conduct a thorough walk-through of the plant to verify that all equipment is ready 
for operation and that all manual valves and switches are correctly positioned. 
Pre-Start-Up Procedure: 


============================================================
--- PAGE 84 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.84 
 
- Cartridge Filters should contain clean filters, and the manual inlet isolation valve should be open. 
The vent valves should be open especially if the cartridge filters have been changed to bleed 
any entrapped air. The clean water and dirty water drain valves should be closed 
- Concentrate discharge valve must be in automatic  mode.   
 
- All manual valves off skid and downstream that could restrict the concentrate or permeate flow 
leaving the skid must be opened.  
- UHPRO train inlet valve must be in automatic  mode.  
 
- The high-pressure feedwater pump must be in automatic  mode.  
 Under low pressure flow from feedwater source, bleed air off from feedwater system, the 
cartridge filters, the UHPRO feed pump, Super Duplex stainless steel manifolds and 
permeate sample valves. If the skid is drained, the pre-flush timer needs to be extended, 
ensuring that all entrapped air is removed from the system.   
Pre-Flush, Normal Operation, Post-Flush, and Permeate Flush  
- When the UHPRO train is called to run from SCADA, the train inlet valve will open.  


============================================================
--- PAGE 85 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.85 
 
- Once the train inlet valve is fully open the pre-flush timer will start, and water will flush through 
the system for the length of time input in the pre-flush timer setting.   
- The pre-flush time can be monitored on the UHPRO train operator interface screen and 
measured in seconds remaining.   
- When the Pre-Flush sequence will time out the UHPRO high pressure feed pump will slowly 
ramp up.  
- The manual concentrate control valve will need to be adjusted if the correct concentrate flow is 
not displayed on the UHPRO train operator interface screen.  
- After start-up, the UHPRO train should reach stable operation in approximately 5-10 minutes.   
o Feed Pump Speed  – In Automatic mode, this speed should adjust automatically to meet the 
Total Permeate flow set-point. Changing feed pump speed will change flows throughout the 
system including total permeate and concentrate flow. Increasing the feed pump speed will 
increase flows while decreasing it will lower the flows.  
- The UHPRO system will continue operating until the UHPRO skid is commanded to stop by 
SCADA. At this time, the UHPRO train will go into a post-flush sequence.  
- During post-flush, the high-pressure feed pump will be de-energized. The concentrate discharge 
valve will fully open, and concentrated water will be flushed from the system under pressure. 
The system will flush for the length of time input in the post-flush timer setting. The post-flush 
time remaining can be monitored and changed on the UHPRO train operator interface screen. 
At the end of the post-flush sequence the train inlet valve will close.  
- The UHPRO train will remain shut down until it is called for by SCADA.  
Post-flush will be required to reduce the conductivity of the water that will remain in contact with the 
membranes until the system is restarted. If the concentrate is not flushed out of the system, salts will 
begin to precipitate out of this saturated solution and scales will form on the membrane surface. The 
goal of the post-flush is to remove the water left in the pressure vessels similar in quality to that of the 
feed water. Feed water is naturally balanced meaning no salts present exceed the saturation limit and 
therefore salts will not precipitate out of solution. Opening the concentrate valve will allow for a high 
volume of water to be flushed through the system at low pressure. This will reduce the required post-
flush length.  
Permeate post-flush  can be utilized to further reduce the conductivity of the water that will remain in 
contact with the membranes until the system is restarted. As soon as the UHPRO train is brought into 
operation and is producing permeate, it will fill the dual-purpose CIP tank with permeate. The tank will 

============================================================
--- PAGE 86 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.86 
 
fill using a float valve that will prevent further filling once the tank is at maximum capacity. Once the 
UHPRO train will fully complete the typical raw water post-flush the 1st stage cleaning feed valve will 
open. Once it is fully open, the UHPRO train will call for the CIP pump to run. The pump will run for a 
pre-determined amount of time before shutting down. The 1st stage cleaning feed valve will close.   
Operation without SCADA  – An operator can operate the UHPRO train without SCADA in an 
emergency situation under certain conditions. Sufficient feedwater must be available at the train inlet 
valve. When the UHPRO train control switch is placed into Manual the automatic operation sequence 
will commence without requiring communication with SCADA.   
When the UHPRO train control switch is placed into Off the UHPRO train valves and feed pump can 
also be operated manually. This will require the operator to operate the components in the correct order 
and should only be done in an emergency situation as there is greater risk of unintended operation.   
Note: When operating the UHPRO train manually, the train continues to run regardless of conditions, 
with most of the alarms non-functional. Each individual system component and valve in manual can 
only be stopped/started or opened/closed by the operator. This mode of operation disables all automatic 
control functions and interlocks. Only skilled technicians and/or operators with extensive knowledge of 
the process should operate the system manually.  
Extreme caution must be utilized when operating the system manually in order to avoid 
potentially catastrophic damage to pumps, piping, controls, membranes and all other system 
components.   
UHPRO Feed Pump Control  – As stated above, the UHPRO feed pump speed will typically be 
controlled automatically when the Speed Mode is set to Auto in order to maintain the total permeate 
flow rate setpoint. The Speed Mode can be set to Manual to run at a set speed (Hz) for troubleshooting 
or maintenance purposes.  
This functionality is useful for testing purposes when wanting to compare operational data versus start-
up data to determine if a cleaning is necessary. The flow from each vessel can be measured with the 
3-way permeate ball valves and volumetric measurement (calibrated bucket & stopwatch). Also, it will 
give the operator the ability to set the pump to a historical speed and run the system if a flow meter 
were to malfunction and need to be taken out of service.  

============================================================
--- PAGE 87 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.87 
 
 
UHPRO Skid: Alarm Conditions  – There will be several alarm conditions monitored by the UHPRO 
train PLC that will initiate either an immediate UHPRO train shutdown or a shutdown with post-flush 
and permeate flush if enabled. If the shutdown is from an alarm that results in an immediate shutdown, 
then the post-flush step will be skipped.   
UHPRO Train Initiated Some Possible Alarms: Shutdown with Post-Flush    
- High Recovery % Alarm (Operator Adjustable Setpoint)  
- RO Feed Pump VFD Fault  
- RO Feed Pump VFD Failed to Run  
UHPRO Train Initiated Some Possible Alarms: Immediate Shutdown without Post-Flush  
- Emergency Stop Switch  
- Low Feed Pump Suction Pressure (Mechanically Adjusted)  
- High Feed Pump Discharge Pressure (Mechanically Adjusted)  
- Rupture Disk Burst (Requires Rupture Disk Replacement)  
- Low Concentrate Flow (Operator Adjustable Setpoint)  
- High First Stage Feed Pressure (Operator Adjustable Setpoint)  
- High Second Stage Feed Pressure (Operator Adjustable Setpoint)  
- High 1st Stage Differential Pressure (Operator Adjustable Setpoint)  
- High 2nd Stage Differential Pressure (Operator Adjustable Setpoint)  
- Inlet Valve Failed to Open  
- Inlet Valve Failed to Close  
- Concentrate Discharge Valve Fail to Open  
- Concentrate Discharge Valve Fail to Close  
- 1st Stage Cleaning Feed Valve Fail to Open  
- 1st Stage Cleaning Feed Valve Fail to Close  
- Surge Arrestor Fail  
- Control Power Fail  


============================================================
--- PAGE 88 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.88 
 
In all cases, if the UHPRO train shuts down in an alarm condition, the alarm text will flash on the operator 
interface next to the related component icon.  
The UHPRO train will remain shut down until the operator has addressed the cause of the alarm and 
presses the alarm Reset button that appears on the operator interface. 
When the alarm condition has been addressed and the alarm Reset button pushed, the UHPRO skid 
will begin a new running sequence starting with pre-flush if the UHPRO train control is still in Auto and 
SCADA is still calling for the UHPRO train to run. If it is not desired, then the UHPRO train control can 
be switched to Off. 
If the alarm condition has not been cleared the alarm will not be able to be reset.  
Alarms can be viewed on the Alarm History screen.  
 

============================================================
--- PAGE 89 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.89 
 
10. HARDWARE AND SOFTWARE LICENSES LIST 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Listado con licencias de hardware y software”) 
 
Hardware / Software Licenses (Preliminary List) 
Item Description / Model 
Number  Type Manufacturer Location  Qty Notes 
1 Studio 5000 Logix 
Designer v37  Logic Editor Rockwell 
Automation  - 1  
2 FactoryTalk View 
Studio v15 HMI Editor Rockwell 
Automation - 1  
3 Dell 14" Latitude 3450 
(w/ Win 11)  Laptop Dell - 1  
 
 
 
 

============================================================
--- PAGE 90 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.90 
 
11. PROJECT SCHEDULE  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Programa del encargo”) 
The final project execution schedule will be established based on a mutually agreed timeline following 
contract finalization. However, the following preliminary milestones are proposed based on current 
requirements and conditions: 
 Issuance of Award Notice : September 29, 2025  
 Start Date of contract: will be 15 - 20 days after Award Notice . This is when the contract is 
expected to be fully executed, and the final agreed timeline shall be counted from this date    
 Contract Term : Shall not exceed 510 calendar days from start date until Provisional 
Acceptance  
 Delivery Period : Maximum of 300 calendar days  from start date  
 Engineering submittals for approval: overall maximum 90 calendar days after the start 
date, except in cases where difference period is defined. Please refer to Section 11.1 below of 
this proposal.  
 Fabrication, assembly and testing activities: start after selected/required documentation 
is approved  
 Shipment of system: after ADASA issued the release, which required all applicable 
engineering submittals to be approved. And agreed list to be defined  
 Installation supervision Commissioning and Start-Up Period : Maximum of 21 calendar 
days, initiated upon ADASA’s formal request. This request (advance notice to site) can be made 
by ADASA  within 180 calendar days  following receipt of the UHPRO system on site.  Note:  
 Advance Notice for On-Site Field Services : ADASA will notify the supplier 30 calendar days 
in advance  of the required site appearance date.  
 Final Documentation and Project Close-Out : Supplier will have a maximum of 30 calendar 
days after completion of commissioning and start-up activities to submit all required 
documentation and fulfill all conditions necessary for Provisional Acceptance  
 Review/approval Period: All submittals shall be reviewed and approved by ADASA within 7 
business days of submission  
 Warranty period: 24 months from the Provisional Acceptance date (as per client requirement). 
Note:  for RO Membranes, the warranty offered will be as per manufactures and is not part of 
this Equipment guarantee )  

============================================================
--- PAGE 91 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.91 
 
 Final Acceptance: after warranty period has satisfactorily elapsed. The Supplier may request 
the ADASA to issue the Final Acceptance Certificate in writing. Upon formalization of the 
Certificate, the ADASA Buyer will return the corresponding Warranty Certificates to the Supplier.  
A visual timeline (Gantt-style chart) for the Preliminary Project Execution Schedule is attached for further 
details. 
11.1 ENGINEERING SUBMITTALS & SCHEDULE  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Listado de entregables de ingeniería”) 
A final list of engineering submittals and timeline will be established based on a mutually agreed 
agreement following contract finalization. According to P22-ET-09-000-001-0 - Section7, the following 
has been considered at this stage. 
Engineering Submittals  
References: 
G = General        P = Process                M = Mechanical        E = Electrical        I&C = Instrumentation & Control 
Q =  Quality (Assurance / Control)         Doc. No.  
Discipline  
Document Name Submittal Due Notes 
# Unit Event 
TBA 
-1 G Detailed Project Schedule, 
including engineering, 
procurement, construction, 
transportation, assembly, and 
commissioning. 15 Days after the 
start date , after the start date , as 
defined above  
TBA 
-2 P Process and Instrument 
Diagrams (P&IDs) within 
90 Days after the 
start date    
TBA 
-3 P Process Flow Diagram (PFD) with 
Mass Balance  within 
90 Days after the 
start date    
TBA 
-4 P Process calculations reports with 
models using the selected 
membranes for 53,000 mg/L TDS 
o RO Projections 
o Turbo Charger Projections 
o Utility Consumption List  
o Chemical Consumption List within 
90 Days after the 
start date  
  
TBA 
-5   General arrangements 
(GAs)/Layouts Drawings within 
90 Days after the 
start date    
TBA 
-6   Plan and elevation drawings of 
equipment and piping within 
90 Days after the 
start date    
TBA 
-7   Module Seismic Calculation Report within 
90 Days after the 
start date    

============================================================
--- PAGE 92 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.92 
 
Engineering Submittals  
References: 
G = General        P = Process                M = Mechanical        E = Electrical        I&C = Instrumentation & Control 
Q =  Quality (Assurance / Control)         Doc. No.  
Discipline  
Document Name Submittal Due Notes 
# Unit Event 
TBA 
-8   Stress & flexibility analysis for high 
pressure pipes within 
90 Days after the 
start date    
TBA 
-9   Drawing with civil requirements, 
including dimensions, loads, and 
bolts within 
90 Days after the 
start date  Only GAs with Weight and 
Dimensions, Client shall 
obtain the require civil 
design  
TBA 
-10   Single-line diagrams within 
90 Days after the 
start date    
TBA 
-11   Main Equipment data sheets 
(defined in P22-ET-09-000-001, 
Section 5.1) 
o High Pressure Pump 
o 1st Stage Turbo 
o 2nd Stage Turbo 
o CIP Wash Pump 
o Cartridge Filters 
o RO Pressure Vessels 
o Reverse Osmosis Membranes 
o Dosing Pump 
o RO Support/skid Frame 
o Container 
o Auxiliary Services (container 
interior lighting, exterior 
lighting, A/C within 
90 Days after the 
start date  
  
TBA 
-12   Manufacturing and testing dossier 
for all electrical and 
electromechanical equipment with 
their special steel manufacturing 
certificates for super duplex 
equipment. within 
90 Days after the 
start date  
  
TBA 
-13   Piping, Valves and instruments 
data sheets/specs, with brands and 
models within 
90 Days after the 
start date  
 
TBA 
-14   Control philosophy with reference 
to the P&ID TAGs within 
90 Days after the 
start date  
 
TBA 
-15   Design of control screens and HMI. within 
90 Days after the 
start date  
 

============================================================
--- PAGE 93 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.93 
 
Engineering Submittals  
References: 
G = General        P = Process                M = Mechanical        E = Electrical        I&C = Instrumentation & Control 
Q =  Quality (Assurance / Control)         Doc. No.  
Discipline  
Document Name Submittal Due Notes 
# Unit Event 
TBA 
-16   Detailed Bill of Materials (BOL), 
with brands and models within 
90 Days after the 
start date  
 
TBA 
-17   3D Model   within 
90 Days after the 
start date  
 
TBA 
-18   Isometric views of high-pressure 
lines. within 
90 Days after the 
start date   
TBA 
-19   Proposal of rail beams and internal 
lifting points within the module for 
the removal of mechanical 
equipment (pumps and 
turbochargers). within 
90 Days after the 
start date  
 
TBA 
-20 Q  Detailed Inspection and Testing 
Plan (ITP) (in Spanish PIE), as per 
requirements defined in document 
P22-IT-09-000-001-0 (this is 
minimum basis) within 
90 Days after the 
start date  
 
TBA 
-21 G Spare Parts and Special Tool 
List  1  Month Before 
shipment 
 
TBA 
-22  Others: 
-) A/C report (a thermal calculation 
report to determine the volume of 
the air conditioning system)   within 
90 Days after the 
start date  
 
TBA 
-23  G Assembly/Installation Instruction 
Manual 1  Month Before 
shipment   
TBA 
-24 G  Start-up Manual of the System-
Plant /Equipment  1  Month Before 
shipment   
TBA 
-25 G  Operation and Maintenance (O&M) 
Manual of the System-Plant 
/Equipment 1  Month Before 
shipment   

============================================================
--- PAGE 94 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.94 
 
Engineering Submittals  
References: 
G = General        P = Process                M = Mechanical        E = Electrical        I&C = Instrumentation & Control 
Q =  Quality (Assurance / Control)         Doc. No.  
Discipline  
Document Name Submittal Due Notes 
# Unit Event 
TBA 
-26   Final Software and License 
Package 1  Month Before 
shipment   
TBA 
-27 G  Detailed Procedure for 
Preservation, Packaging, and 
Preparation for International 
Maritime Transport 1  Month Before 
shipment 
  
 
 
 
 

============================================================
--- PAGE 95 ---
============================================================
ID
 Task 
ModeTask Name Duration Start Finish Predecessors Resource Names
1 ( Business Days) 0 days Mon 9/29/25 Mon 9/29/25
2 Award Notice 0 days Mon 9/29/25 Mon 9/29/25
3 Contract Start Date 10 days Mon 9/29/25 Fri 10/10/25 2
4 Project 210 days Mon 10/13/25 Fri 7/31/26
5 1 Engineering 64 days Mon 10/13/25 Thu 1/8/26
6 Order entry 5 days Mon 10/13/25 Fri 10/17/25 3
7 P&ID 15 days Mon 10/20/25 Fri 11/7/25 6
8 General 
arrangement 10 days Mon 
11/10/25Fri 11/21/25 7
9 Wire Diagram 5 days Mon 11/24/25 Fri 11/28/25 8
10 Submitt Eng 
Package for 
approval5 days Mon 
12/1/25Fri 12/5/25 9
11 Approved Package 1 7 days Mon 12/8/25 Tue 12/16/25 10ADASA
12 Control Package
for Approval10 days Wed 
12/17/25Tue 
12/30/2511
13 Approved 
Control Package7 days Wed 
12/31/25Thu 1/8/26 12ADASA
14 2 Purchasing 100 days Mon 12/8/25 Fri 4/24/26
15 Long Lead Items
Order100 days Mon 
12/8/25Fri 4/24/26 10
16 Procurement 50 days Fri 1/9/26 Thu 3/19/26 13
17 3 Fabrication 70 days Mon 4/27/26 Fri 7/31/26
18 Mechanical 30 days Mon 4/27/26 Fri 6/5/26 15,16
19 electrical 15 days Mon 6/8/26 Fri 6/26/26 18
20 factory Testing 5 days Mon 6/29/26 Fri 7/3/26 19
21 Package 3 : 
Operation 
Manual, 15 days Mon 7/6/26 Fri 7/24/26 20
22 Ready to ship 5 days Mon 7/27/26 Fri 7/31/26 21
23
24 Shipping Ocean-Site 40 days Mon 8/3/26 Fri 9/25/26 22SHIPPING
25
26 Site Installation By Client 180 days Mon 2/2/26 Fri 10/9/26 24FF+10 days,13ADASA
27 ADISA Notification 
Start Up22 days Mon 
9/28/26Tue 
10/27/2626FF-22
days,24ADASA
28 Precheck- List to be 
filled by Customer0 days Tue 
10/27/26Tue 
10/27/2627
29 Installation Supervision 9 days Wed 10/28/26 Mon 11/9/26 27BW
30 Start Up 5 days Tue 11/10/26 Mon 11/16/26 29BW
9/29
9/29
ADASA
ADASA
SHIPPING
ADASA
ADASA
10/27
BW
BWJun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov DecQtr 3, 2025 Qtr 4, 2025 Qtr 1, 2026 Qtr 2, 2026 Qtr 3, 2026 Qtr 4, 2026
Task
Split
Milestone
Summary
Project Summary
Inactive Task
Inactive Milestone
Inactive Summary
Manual Task
Duration-only
Manual Summary Rollup
Manual Summary
Start-only
Finish-only
External Tasks
External Milestone
Deadline
Progress
Manual Progress
Page 1Project: 6501 TALTAL ANTOFAG
Date: Fri 8/1/25


============================================================
--- PAGE 96 ---
============================================================
ID
 Task 
ModeTask Name Duration Start Finish Predecessors Resource Names
31 Training 2 days Tue 11/17/26 Wed 11/18/26 30BW
32 Performance Test 5 days Thu 11/19/26 Wed 11/25/26 31BWBW
BWJun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov DecQtr 3, 2025 Qtr 4, 2025 Qtr 1, 2026 Qtr 2, 2026 Qtr 3, 2026 Qtr 4, 2026
Task
Split
Milestone
Summary
Project Summary
Inactive Task
Inactive Milestone
Inactive Summary
Manual Task
Duration-only
Manual Summary Rollup
Manual Summary
Start-only
Finish-only
External Tasks
External Milestone
Deadline
Progress
Manual Progress
Page 2Project: 6501 TALTAL ANTOFAG
Date: Fri 8/1/25


============================================================
--- PAGE 97 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.97 
 
12. INSPECTION AND TESTING PLAN (ITP) 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “ PIE (Plan de Inspección y Ensayos Detallado (PIE) de 
equipos principales según Section 5.1”) 
Inspection and Testing Plan (ITP) sample is attached for reference only. The final document for this 
project will be developed and submitted after the contract is awarded. 
 
 

============================================================
--- PAGE 98 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA Owner
Verification of Material
  - Material Test Report Review/Certificate
20 Non Destructive Examination (NDE) ASME VIII I R R Inspection Report
30 Visual & Dimensional Check Drawings / Prints I R R Inspection Report
40 Pickle / Passivation or Electropolish ASTM A967-05 I R R Manufacturer Procedure
50 Hydrostatic test ASME B31.3 I R R Test Report
Packing Inspection I R R
Marking Condition / Protection for shipment
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Packaging Inspection
Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Verification of Material
  - Material Test Report Review/Certificate
20 Visual & Dimension Inspection Approved Drawing(s) I R R Supplier's dimensional inspection report
Testing:
- Seat Leakage Test
-  Body  Pressure TestMetal Valves :
Solenoid, Manual & Pneumatic Spools
 - Stainless Steel  & Super DuplexItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test
 PVC, CPVCR RVerification
IManufacturer Standard Procedure
Manufacturer Standard ProcedureR
Factory certificate3
Mill Certs. or Test Report  
30 Manufacturer Standard Procedure  I R R- - Data Book
10 Material Spec according to ASTM Code R R R30 Drawings/ Print , Technical spec , and Specifications20 I R R Photos10 Compliance to requirements Manufacturer Standard Procedure R R R Purchase OrderNon-metal  Valves  2Mill Certs. or Test Report 10 Material Spec according to ASTM Code
Data BookPacking List  &Photos
70 Drawings/ Print , Technical spec , and Specifications I - -601
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 1
For Reference Only

============================================================
--- PAGE 99 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
40 Operation Test  Manufacturer Standard Procedure I R R Test Certificate
Painting Inspection  (if applicable):
- Color / Visual Condition Check
Packing Inspection
Marking Condition / Protection for shipment
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Material Verification :
 Material Test report Review
20 Motor Test & Inspection : Data Sheet I R R Test Report
30 Hydrostatic Test Manufacturer Standard Procedure I R R Test Procedure
40 Balance Test ( For Impeller or Rotor) Manufacturer Standard Procedure I R R Test Report
50 Dimensional and  visual inspection Approved drwg,  data sheet I R R Dim. Inspection
60 Performance & Running Test : Manufacturer Standard Procedure I R R Test Report
70 Painting  Inspection : Manufacturer Standard Procedure I R R Painting Report
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Compliance to requirements
        - Pump test certificate
20 Visual & Dimension Inspection Data Sheet  &  Manufacturer Standard Procedure I R R Data Sheet
Documentation  :
- Quality Record Book4
5
Metering, Unloading & Dispensing Pumps(COTS):     
                             Centrifugal Pumps and Motors 
- I -I - -IManufacturer Standard Procedure  
Manufacturer Standard Procedure 
30 Drawings/ Print , Technical spec , and SpecificationsPurchase Order 10 Per Manufacturer Standard Procedure  & Datasheet R R R
Data Book80 Drawings/ Print , Technical spec  and Specifications Data BookR R Mill Certs. or Report- - Data Book
10Material Spec according to ASTM code  &  Manufacturer 
Standard ProcedureR70 Drawings/ Print , Technical spec , and Specifications60 I R R Packing List  &Photos50 I R R Inspection Report
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 2
For Reference Only

============================================================
--- PAGE 100 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
- Certificate of Compliance
- Data Book Review / Quality Release
10    Testing Data sheets R R R Test Certificates
20 Dimensional and  visual inspection Approved drwg,  data sheet I R R Certificate of Conformance
Packing Inspection I R R
Marking Condition / Protection for shipment
Documentation  : I - -
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Material Verification I R R
- Material Test Report Review
20 Dimensional and  visual inspection Approved drwg and DHT MPS I R R Supplier's process
30 Nameplate/markings verification Approved DWG. and MPS I R R Supplier's dimensional inspection report
Test certification to ASME X.  Pressure rating: I R R
- 1000 PSI for SWRO,
- 300 PSI BWRO.
50 Painting  Inspection Manufacturer Standard Procedure I R R Painting Report
Packaging Inspection
- Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release6
7
10Energy Recovery DeviceRO Pressure Vessels (FRP)RO Elements
Manufacturer Standard Procedure R R I
Drawings/ Print , Technical spec , and Specifications - - I- I
R R R-
Test Report
60 Packing list and photos30 Drawings/ Print , Technical spec , and Specifications
30
Material certificates, test reports
40 Hydrostatic Test10 ASTM D 3299 / D4097Data BookPacking List  &Photos
40 Drawings/ Print , Technical spec ,  and SpecificationsManufacturer Standard Procedure
Data Book 70
10 Verification of Material Test Certificate Test CertificateData Book
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 3
For Reference Only

============================================================
--- PAGE 101 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
20 Dimensional and  visual inspection Approved drwg,  data sheet I R R Dim. Inspection
30 Factory or Performance Test Data Sheet  &  Manufacturer Standard Procedure I R R Test Report
Packing Inspection
- Marking Condition / Protection for shipment
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
10 Material Verification Material Spec according to ASTM code R R R Mill Certs. or Report according to EN 10204
20 Visual and Dimensional Inspection for Assembly Drawing I R R Dim. Inspection Report
30 Non-Destructive Examination (NDE) ( if applicable) ASME Section VIII I R R PT Report
Hydrostatic Test  -
- Full Water Filling Test
Tank Lining Verification: ( If applicable) I R R
- Cleaning Hardness I R R
- Thickness I R R
- Pinhole Test I R R
Painting Inspection (if applicable) I R R
- Dry Film Thickness I R R
- Color / Visual Condition Check I R R
Packaging Inspection I R R
- Marking , Quantity, Packing I R R
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release8Tanks -CIP
IManufacturer Standard ProcedureR R I
Manufacturer Standard ProcedureManufacturer Standard Procedure
80 Drawings/ Print , Technical spec and Specifications Data Book70Hydro Test Report
60 Painting ReportManufacturer Procedure
Packing List  &Photos5040
Manufacturer Standard Procedure
- -Manufacturer Standard Procedure
- - IR R I
Data Book 50 Drawings/ Print , Technical spec , and Specifications40 Photos
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 4
For Reference Only

============================================================
--- PAGE 102 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
10 Visual & Dimensional Check Approved drwg,  data sheet I R R Dim. Inspection
20 Hydro Test for all pipes Manufacturer Standard Procedure I R R Hydro Test Certificate
30 Assembly Inspection Approved drwg, BOM, Mfg Standard Procedure I R R 0
Painting Inspection (if applicable)
- Dry Film Thickness
- Color / Visual Condition Check
Packaging Inspection
- Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
10 Test Report Review R R R Data Sheet
I R R
30 Hydrostatic Test Manufacturer Standard Procedure I R R Test Report
Painting Inspection
- Color / Visual Condition Check on final coat only.
Packaging Inspection
- Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
10Dimension Inspection Drawing I R R Supplier's dimensional inspection report
20Hydrostatic Test Manufacturer Standard Procedure I R R Test Report9
10
11RO SkidsSkid / Steel Structure (CS)
R R I Manufacturer Standard Procedure 
RManufacturer Standard Procedure
Manufacturer Standard Procedure 
- - IR R IR R I
Data BookPainting Report
50 Packing List  &Photos Manufacturer Standard Procedure 
- -II RDimensional and  visual inspection Approved drwg,  data sheet 
60 Drawings/ Print , Technical spec , and Specifications
Chemical Dosing Systems70 Drawings/ Print , Technical spec  and Specifications Data BookPainting Report
60 Packing List  &Photos50
Dim. Inspection
4020
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 5
For Reference Only

============================================================
--- PAGE 103 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
30Painting Inspection ( If applicable)
- Color / Visual Condition
Check on final coat only.
40Packaging Inspection
- Marking , Quantity, Packing
50Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
Dimensional and  visual inspection
- Record actual dimensions on inspection report (for non-
COTS or Catalog items)
Testing (If applicable)   ;
- Calibration or Functional Test (for non-COTS or Catalog 
items)
Packaging Inspection
- Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
10 Visual and Dimensional Inspection for Assembly Drawing I R R Dim. Inspection Report
20 Function Test / Compliance to requirements Manufacturer Standard Procedure R R R Data Sheet
Packaging Inspection
- Marking , Quantity, Packing
Documentation  :
- Quality Record Book
- Certificate of Compliance ( if required)12
13& Electrical Raw MaterialData BookPacking List  &Photos
-R
-RPainting Report R R I Manufacturer Standard Procedure 
R R I
Data BookPacking List  &PhotosApproved drwg,  data sheet Manufacturer Standard Procedure 
- - III
Cut sheet R R I
R R
R R I20 Manufacturer Standard Procedure 10Drawings/ Print , Technical spec , and Specifications
Local Instrumentation
40 Drawings/ Print , Technical spec , and Specifications30Data BookPacking List  &Photos
40 Drawings/ Print , Technical spec , and Specifications - - I30 I Manufacturer Standard Procedure 
Electric Heaters:  Dim. Inspection
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 6
For Reference Only

============================================================
--- PAGE 104 ---
============================================================
Confidential
CUSTOMER: Aguas Antofagasta REV.:0
LOCATION: Chile DATE: 
PROJECT No.: Proposal 20.24. 6501 -ADASA Brine Recovery Project -UHPRO System ORIG. BY:
MFG BWWA OwnerItem NameINSPECTION & TESTING  PLAN - SAMPLE
Inspection Doc. Reference Document No. Description of Inspection & Test Verification
- Data Book Review / Quality Release
10 Visual & Dimensional Check Approved drwg,  data sheet I R R Dim. Inspection
20  Wiring and Assembling Drawing I R R Drawing
30  Insulation Resistance Test Manufacturer Standard Procedure I R R Manufacturer Procedure
40 Painting Inspection (if applicable) Manufacturer Standard Procedure 
- Dry Film Thickness
- Color / Visual Condition Check
50 Packaging Inspection Manufacturer Standard Procedure 
- Marking , Quantity, Packing
60 Documentation  : Drawings/ Print , Technical spec , and Specifications
- Quality Record Book
- Certificate of Compliance ( if required)
- Data Book Review / Quality Release
#10Xxxx xxx XX XX xx
20xxxx xxx xx14
Iteam name xxxControl Panel
R
R
- - Data Book IR Painting Report
I R Packing List  &PhotosI
BW Water Americas Inc. Bid Tender 12803 _Technical Offer - July 29 2025 7
For Reference Only

============================================================
--- PAGE 105 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.105 
 
13. JUSTIFICATION OF MECHANICAL COUPLINGS/JOINTS (VICTAULIC TYPE) IN 
HIGH PRESSURE 
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Justificación de Tipos de Junta en Alta Presión”) 
HIGH PRESSURE LINE JOINT LIST 
No. Service Process 
condition  Joint Types Process 
Pipe size  Pipe 
Material  Pipe 
Class Remark 
1 Discharge from RO HP 
Feed Pump (High 
Pressure Line) 49 m3/hr 
48.8 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 80, 
NPS 3'' SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 
2 Feed into UHPRO 
Train (Feed Turbo HP 
OUT), (High Pressure 
Line) 49 m3/hr 
67.5 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 80, 
NPS 3'' SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 
3 1st Stage Concentrate 
of UHPRO, (High 
Pressure Line) 35.1 m3/hr 
66.3 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 65, 
NPS 2.5'' SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 
4 Feed into 2nd Stage 
UHPRO Train 
(Interstage Turbo HP 
OUT) , (High Pressure 
Line) 35.1 m3/hr 
83.9 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 65, 
NPS 2.5'' SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 

============================================================
--- PAGE 106 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.106 
 
HIGH PRESSURE LINE JOINT LIST 
No. Service Process 
condition  Joint Types Process 
Pipe size  Pipe 
Material  Pipe 
Class Remark 
5 2nd Stage Concentrate 
of UHPRO or 
 Feed into Interstage 
Turbo (Interstage 
Turbo HP IN), (High 
Pressure Line) 27.9 m3/hr 
82.4 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 65, 
NPS 2.5'' SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 
6 Feed into Feed Turbo 
(Feed Turbo HP IN) or 
 Discharge from 
Interstage Turbo 
(Interstage LP 
DISCHARGE), (High 
Pressure Line) 27.9 m3/hr 
51.1 Barg 
pH 7.6 
19 - 24 °C Victaulic coupling or 
Welded or flanged 
Joints (CL900) DN 65, 
NPS 2.5''  SDSS 
SCH80 
ASME 
B31.3 
CL 900 ASME B 
16.5 
CL 900 For stability and durability of HP pipe  
1) Victaulic couplings: Rated as 2000PSI (138 
BAR). 
2) Flanged or Welded connection: Test can be 
done up to CL 900 (2220PSIG) for pipe spools 
in HP line 
Please see attached technical details of PIEDMONT Pacific Groove End Flexible Pipe Coupling 
 
 

============================================================
--- PAGE 107 ---
============================================================
PLAN VIEW261
12
23
34
4A AB B
REV CHKD APPVD ENG DATE
(DD/MM/YYYY)
REVISION:DRAWING REVISION
SCALE:PIEDMONT PACIFIC 
GROOVE END FLEXIBLE PIPE COUPLINGPROPRIETARY AND CONFIDENTIAL NOTE :
THE INFORMATION CONTAINED IN THIS DRAWING IS 
THE SOLE PROPERTY OF PIEDMONT PACIFIC.
ANY REPRODUCTION IN PART OR AS A WHOLE WITHOUT
THE WRITTEN PERMISSION OF PIEDMONT PACIFIC IS 
PROHIBITED.   ANSI Y14.5INTERPRETATION:UNLESS NOTED
OTHERWISE
DRAWN REVISION DESCRIPTION
DO NOT SCALE PRINTS  TITLE:
STYLE H COUPLING ASSEMBLY
UNIT: DRAWING NO. SHEET:
1.0 9 N/AINCH 
[MM]1.0
1 14-09-2015 GENERAL COUPLING ASSEMBLY OF STYLE D AH AH CZZTOLERANCES: 0.03" [0.75 MM]
ANGLES:       1
HOLE SIZES:      0.03" [0.75 MM]
HOLE CENTERS:    0.03" [0.75 MM]
 SURFACE FINISH ON PART:    125
SURFACE FINISH ON O-RING: 32
2 08-12-2015 D2.0 AND D3.0 WERE REVISED AH CZZ AHAH
AH
3 12-01-2016
D8.0 DESCRIPTION WAS ADDED AH CZZ AH AH5
618-07-2016 PRODUCT WEIGHTS ARE ADDED. DIMENSIONS REVISED. AH CZZ AH AH
08-09-2017
7TABLE UPDATED JF CZZ
802-11-2017 TABLE UPDATED JF CZZ
909-08-2018 TABLE UPDATED JF CZZITEM DESCRIPTION MATERIAL QTY
1 GROOVED END PIPE (AWWA C606 STANDARD) METALLIC/NON METALLIC 2
2 COUPLING HOUSINGCE8MN/CE3MN (DUPLEX/SUPERDUPLEX 
STAINLE
SS STEEL) 2
3 EPDM RUBBER 1
4GASKET
ROUND  HEAD , OVAL NE CK  TRACK BOLT / 
HEXAGONAL HEAD BOLT    316 S / 2205 DUPLEX 2
5 WASHER 2
6 HEAVY HEX NUT    SILICON BRONZE/316 SS / 2205 DUPLEX 2
PRESSURE RATIN
NOMINAL SIZES RATED PRESSURE PROOF TEST PRESSURE
1" - 4" 2000 PSI (138  B ) 3000 PSI (207 BAR)
NOTES :
          
  
            
          
   
          
         
      
    1. DIMENSIONS SHOWN IN THE DRAWING ARE INDICATIVE. FOR DETAILED INFORMATION ON
GD&T, CONTACT PIEDMONT
2. COUPLING IS RATED FOR SCH. 40 PIPE (OR THICKER) WITH CUT GROOVES ONLY
3. HOUSING MATERIAL IS DUPLEX (CE8MN) OR SUPER DUPLEX (CE8MN/CE3MN) STAINLESS STEEL,
CONFORM TO ASTM A995/A995M-13
4. BOLTS ARE ROUND HEAD, OVAL NECK 316SS /2205 DUPLEX TRACK BOLTS
5. NUTS ARE HEAVY HEX SILIC
ON BRONZE/316SS  / 2205 DUPLEX , CONFORM TO DIN-934.
6. WASHERS ARE 316SS / 2205 DUPLEX ,CONFORM TO DIN-125.
7. GASKETS ARE EPDM RUBBER (FLU
SH-FIT/C-SHAPE)NOMINAL SIZE 
INCHX 
INCH [MM]Y 
INCH [MM]Z 
INCH [MM]dk
 INCH [MM]R1
 INCH [MM]R2 
INCH [MM] Rk 
INCH [MM]APPROX. WT 
LB [KG]
1 2.4 [60.9] 3.8 [96.7] 1.68 [42.6] 1.37 [34.8] 1.00 [25.4] 0.67 [16.9] 0.60 [15.2] 0.97 [0.44]
1-1/2 2.94 [74.6] 4.3 [109.2] 1.71 [43.4] 1.35 [34.3] 1.23 [31.2] 0.98 [24.9] 0.90 [22.7] 1.21 [0.55]
2 3.5 [88.9] 4.02 [127.5] 1.78 [45.2] 1.35 [34.3] 1.47 [37.3] 1.21 [30.7] 1.13 [28.7] 1.92 [0.87]
3 4.84 [123.1] 6.7 [170.2] 1.85 [47.0] 1.35 [34.3] 2.03 [51.6] 1.78 [45.2] 1.68 [42.7] 2.64 [1.20]
4 6 [152.4] 7.8 [198.5] 2.02 [51.3] 1.50 [38.1] 2.64 [67.1] 2.28 [57.9] 2.17 [55.2] 4.54 [2.06]DIMENSIONS:
42
3
1
5
6
AA
SECTION A-A
dk
Z
XY
R1R2RkS
316 S / 2205 DUPLEX S
R A
2-1/2 4.04 [102.6 ] 5.8 [147.2 ] 1.85 [47.0] 1.35 [34.3] 1.72 [43.7] 1.46 [37.03 ] 1.367 [34.7]2.40 [1.09]
DTASASDJ TABLE UPDATED  / ADDED. 2-1/2 SIZE 08-05-2020

============================================================
--- PAGE 108 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.108 
 
14. MANDATORY/CRITICAL SPARE PARTS LIST FOR 
COMMISSIONING AND START-UP PHASES  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Suministro de Repuestos Mandatorios para Puesta en 
Marcha”) 
Preliminary list of Mandatory/Critical Spares is presented in table below:  
Manufacturer  Part # Description  Qty. Unit Notes 
Hardware 
 Fil-Trek or Equivalent  tba Cartridge Filter 1 set  
 tba tba Fuses used in the panels 1 set  
 Rosemount or 
Equivalent tba Pressure Transmitter 1 unit Used in the HP 
system 
Rosemount or 
Equivalent tba Conductivity sensor/electrode 1 set Used on the line of 
final permeate 
 Flexitallic or 
Equivalent tba Seal/gasket kit 1 set For HP Victaulic 
pipe 
ABB or Equivalent tba Flowmeter 1 unit  
Ashcroft or Equivalent  tba Pressure Gauges, SS304/316 3 unit  
IFM or Equivalent tba Level Transmitter 1 unit  
 
 

============================================================
--- PAGE 109 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.109 
 
15. RECOMMENDED TWO-YEAR SPARE PARTS LIST  
(Ref.: P22-ET-09-000-001-0, Section 6 -Item “Listado y Cotización Opcional de Repuestos para Dos 
Años”) 
A Preliminary list of recommended 2-year Spares is presented in the table below:  
Manufacturer  Part No.  Description  Qty. Unit Notes 
Hardware   
Tampa Rubber 
EPDM Gaskets 
or Equivalent Custom Part Set of Gaskets (Low Pressure – 
Plastic Pipe)  4 set   
Flexitallic or 
Equivalent Custom Part Set pf Gaskets (High Pressure)  2 set   
Protec Arisawa 2081006 RO Vessel Head Assembly  1 unit   
Protec Arisawa 4080474-1 RO Vessel Head Locking Ring  3 unit   
Protec Arisawa 6100442MK RO Vessel Seal Set  2 set   
Protec Arisawa 5080074 RO Membrane Adapters  4 unit   
Fedco or 
Equivalent MSD-130 
repair kit SWRO High Pressure Pump 
Service Kit  1 set   
Pulsafeeder or 
Equivalent LB02SA- XXXX 
(or equal) Chemical Dosing Pump Repair 
Kit  2 set   
Foxboro or 
Equivalent pH 10 (or 
equal) pH Sensor  1 unit   
Foxboro or 
Equivalent  ORP 10 (or 
equal) ORP Sensor  1 unit   
  
Conductivity Sensor  1 unit   
Bray or 
Equivalent Series 63, 
120VAC Solenoid Valve  2 unit   

============================================================
--- PAGE 110 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.110 
 
Manufacturer  Part No.  Description  Qty. Unit Notes 
Ashcroft or 
Equivalent Series 45, 
Monel Pressure Gauge, Monel  2 unit   
Ashcroft or 
Equivalent Series 45, SS  Pressure Gauge, SS304/316  2 unit   
Valves  
Bray or 
Equivalent S01-0200  3” Lined Butterfly Valve   1 unit    
Asahi/America or 
Equivalent Type 57L 2.5” Lined Butterfly Valve   1 unit    
Asahi/America or 
Equivalent Type 57L 2” Lined Ball Valve  1 unit   
Asahi/America or 
Equivalent Type 57P 4” Plastic Butterfly Valve  1 unit   
Asahi/America or 
Equivalent Type 57P 3” Plastic Butterfly Valve  1 unit   
Asahi/America or 
Equivalent Type 57P 2” Plastic Ball Valve  1 unit   
Hayward or 
Equivalent TB Series 1.5 Plastic Ball Valve  5 unit   
Hayward or 
Equivalent TB Series 1” Plastic Ball Valve  5 unit   
 

============================================================
--- PAGE 111 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.111 
 
16. CHEMICALS CONSUMPTION 
Please refer to preliminary Chemicals Consumption below 
Chemical Consumption Calculation             
1. Salinity Level (TDS): 43,000 - 53,000  mg/L       
2. Water Temperature: 19 - 24  °C       
3.UHPRO Feed Flowrate: 49  m3/hr = 1,176 m3/day = 215.6 gpm = 310464 gpd  
4. Total Product Flowrate: 21  m3/hr = 504 m3/day = 92.4 gpm =133056 gpd  
Item 
# Chemical For 
Use Operation 
Mode Dose kg/year kg/day S.G(kg/L)  Frequency  Notes 
1  Anti-Scalant 
(100% ) UHPRO for Scale 
Inhibitor 0.5 215 0.6 1.031 24hr/day   
2 Citric Acid 
Cleaning(30%)  UHPRO for UHPRO 
Acid CIP 20000ppm 152 0.4 1.01 1 time 
/3month   
3 NaOH Caustic 
Cleaning(50%)  UHPRO  for UHPRO 
Akali CIP 20000ppm 91 0.3 1.52 1 time 
/3month   
 
 

============================================================
--- PAGE 112 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.112 
 
17. POWER & LOAD CONSUMPTION LIST 
In alignment with Sections 3, 5, and 19 of this proposal, please find attached the revised calculation 
file detailing the power and load consumption for the proposed UHPRO plant . 
This calculation includes the energy consumption of the RO High-Pressure (HP) Pump, along with the 
following auxiliary equipment: 
 Chemical dosing pumps 
 CIP/flushing pumps 
 CIP heaters 
 RO PLC power 
 Air conditioning (A/C) 
 Internal and external lighting 
The calculations are based on a Total Dissolved Solids (TDS) level of 53,000 ppm  and assume a CIP 
frequency of every 60 days . 
This value will be used for the energy performance guarantee . 
 

============================================================
--- PAGE 113 ---
============================================================
Confidential
     
     
PROJECT TITLE: AGUAS ANTOFAGASTA BRINE RECOVERY SYSTEM CHECKED APPROVED DOC NO.: 6501-E-CL-0001
CLIENT: AGUAS ANTOFAGASTA Production 21.0 m3/hr ID DN Rev. No.: P2
DOC. TITLE: LOAD LIST & POWER CONSUMPTION DATE: 15-Aug-25
 
Equipment 
ID No:No. of Duty 
PumpsNo. of 
Standby 
PumpNo. in Intermittent 
Operation Equipment Description Flow Inlet PressureDischarge 
PressureFluid SGPump 
Effic.Motor ratingMotor 
Service 
FactorMotor VoltsFrequenc
yNumber of 
PhasesMotor 
Operating 
efficiencyVFD EfficiencyConsumed 
KilowattsOperating 
Power FactorkVA kVA AmpereOperation Time 
Hr/DayConsumed 
kWHrConnected    
kWStarterType
m3/h Bar(g) Bar(g) % in kW Volts Hz Rating S.F % %
1 1 0 0 RO HP Pump 49.0 2 48.8 1.0 80.8 83.0 1.15 380 50 3 OK OK 95.8 95.0 88.93 0.78 113.88 173.02 24 88.93 83.00 VFD
2 1 1 0 Antiscalant Dosing Pumps (UHPRO) 0.24 220 50 1 0.20 24 0.20 0.48 DOL
3 1 0 0 CIP/Flushing Pump 54.5 0.25 4.38 1.0 82 9.3 1.15 380 50 3 OK OK 95.8 95.0 88.93 0.85 104.74 159.14 0.02 0.07 9.3 VFD
4 1 0 0 CIP Heater 16 380 50 3 16.00 0.02 0.01 16.0
5 1 0 0 RO PLC + Instrumentation (UPS powered) 2.0 220 50 1 2.00 24 2.00 2.00 UPS Power
6 1 0 0 Lights (Indoor) 0.16 220 50 1 0.16 24 0.16 0.16
7 1 0 0 Lights (Outdoor) 0.16 220 50 1 0.16 24 0.16 0.16
8 1 1 0 A/C Unit 2.64 220 50 1 2.64 24 2.64 5.28
  
Notes: Total Consumed Power 99 kWHr
1. Final kW ratings of pump-motors shall be determined from vendor data sheets. Total Connected Power 122 kW
2. Power consumption values are indicative of maximum 'not to exceed' values.  Power Consumption 4.71 kW/m3
3. CIP Frequency is assumed as 60 days for this plant. PRELIMINARY LOAD LISTS & POWER CONSUMPTION  - SEC Guaranteed Value 
 SEC Guaranteed ValuePREPARED BY PROJECT NO.
JR 6501
 
Electrical Loads
Motor Status
BRINE RECOVERY SYSTEM - Ultra High Pressure  Reverse Osmosis Package 
BW Water Americas Inc Bid Tender 12803 _Technical Offer -  August 19 2025  [Page]

============================================================
--- PAGE 114 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.114 
 
 
 
 
 
 
 
DOCUMENT No. 2 – 
COMMISSIONING & START-
UP PLAN 
 
 

============================================================
--- PAGE 115 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.115 
 
18. COMMISSIONING AND START-UP ACTIVITIES EXECUTION 
PLAN 
(Ref.: Bases Administrativas Especiales (BAE), Section 20.1 – Document 2 “Plan de ejecución de 
actividades de comisionamiento y puesta en marcha)” 
18.1  KEY PERSONNEL 
All activities related to commissioning, start-up, on-site performance testing, and client personnel 
training will be led and directed by our Field Services Manager, Mr. Andrew L. Fuller.   
Mr. Fuller brings over 25 years of experience  and a proven track record as an effective Project and 
Field Service Manager. He has successfully delivered complex water and wastewater treatment projects 
under technically demanding and time-constrained conditions, ensuring systems perform in accordance 
with their design specifications. 
His extensive expertise in managing and executing on-site installation and commissioning of 
desalination and water/wastewater treatment systems will be a valuable asset throughout all phases of 
this project. Mr. Fuller will play a key role in guiding the project team toward selecting and implementing 
a technically sound and client-aligned solution. 
As requested, Mr. Fuller's resume (curriculum vitae) is attached. 
 
 

============================================================
--- PAGE 116 ---
============================================================
 Andrew  L.  
Fuller  
 
 
 
 
Personnel  Resume  BW Water Americas Inc.  | 1 
 
Mr. Fuller has over 25 years of experience in engineering design and 
project management, including start -up and commissioning of water 
projects. He possesses a solid theoretical and practical background, 
enabling him to handle various complex projects for municipal and 
industrial customers.  
 
Mr. Fuller successfully utilizes his professional knowledge and rich 
experience to drive projects to successful completion, consistently 
meeting and/or exceeding client expectations.  
 
D E T A I L E D  E X P E R I E N C E  
BW Water Americas Inc.(*), Tampa, FL – USA  
Since he joined the company , held a few positions  within the operation 
function  
Project and Field Service Manager  (Oct.2023 – Present)  
Director of Project Management Operations  (2012  – 2015 ) 
Field Service Manager  (Sept.2005  – 2012 ) 
Project Manager  (2000 -Sept. 2005)  
- Manages and supervises field service technicians/engineers, 
providing training, support, and guidance, while ensuring 
employees and clients' operators are aware of potential safety 
issues related to the operation of equipment/systems.  
- Oversees and ensures timely and high -quality service delivery, 
addressing customer issues and resolving complaints.  
- Builds and maintains strong relationships with clients, ensuring 
their satisfaction and loyalty.  
- During project execution, ensures project performance meets high 
standards, contract requirements, and stays within budget and on 
schedule. Manages the design, production, installation, and 
commissioning of membrane -based systems for public water 
supply and industrial process water  requirements.  
- Manages project budgets to maintain/improve profitability and 
efficiency.  
- Possesses vast experience/expertise in executing and 
commissioning a wide variety of projects,  that include seawater 
and brackish reverse osmosis systems, ultra -filtration systems, 
multimedia filters, granulated activated carbon treatment, and re -
mineralization systems. Project sizes range from 0.25 to 50 MGD 
and they’re located all over the world.  
 
Major Projects  
❖ Municipal Client  
o Brunswick County's NWTP Expansion and Upgrades (Phase 3) - 
RO System  41 MGD  - to be completed 2025  
o Water Treatment Plant (WTP) Improvements - North Springs  
 
Y E A R S  OF  
E X P E R I E N C E   
25+  
 
E D U C AT I O N   
- 1995/B. Eng. - Electrical 
Engineering  / Kingston, Jamaica  
 
M E M B E R S H I P S  &  
A F F I L I A T I O N S  
- S.M.E  - Society for Mining, 
Metallurgy and Exploration  
 
O T H E R  T R A I N I N G  
- Diploma / Supervisory 
Management  
 


============================================================
--- PAGE 117 ---
============================================================
 Andrew L.   
Fuller  
Cont’ . 
 
 
 
Personnel  Resume  BW Water Americas Inc.  | 2 
 
Improvement District (NSID)  - Florida  – 3 BWRO  x 2.25MGD . 1 
BWRO  x 2MGD  - Completed  2016 | 2023  
o Desalcott's Point Lisas Desalination Plant - Expansion Projects  -
Trinidad & Tobago - 2 SWRO  (1st pass)  trains total capacity of 
59,052 m3/day and 3 BWRO  (2nd pass)  trains total capacity of 
68,136 m3/day.  - Completed 2014 | 2016 | 2022  
o Fargo Membrane WTP and Improvements North Dakota  – RO 
systems 14  MGD  - Completed  2019  
o Doolittle Road WTP, Edinburg, Texas:  BWRO System 2.0 MGD. 
Completed 2007.  
o North Cameron County RO Plant, Texas: BWRO System 2.0 
MGD. Completed 2007.   
o La Sarah, Texas: BWRO System 1.0 MGD. Completed 2006  
o Owassa WTP, Texas: BWRO System 3.0 MGD. Completed 2008 .  
o Southmost Regional Desalination Plant, Texas: BWRO System  
6.0 MGD. Completed 2007.   
o La Junta, Colorado: BWRO System 4.5 MGD. Completed 
December  2004   
o Cooper City, Florida  BWRO expansion, 4 MGD.  Completed June 
2003   
o City of West Carrollton, Ohio: BWRO system, 2.0 MGD. 
Completed March 2005  
o Town of Moundsville, West Virginia : BWRO , System, 3.0 MGD . 
Completed October 2007  
o Village of Minster, Ohio : 2 MGD. Completed October 2007  
o Long Beach Prototype, CA: NF -RO/SWRO, 0.3.  Completed 
March  2005  
 
❖ Industrial Clients  
o PREPA_S an Juan Power Plant -AWTP - Service Contract  – 
Puerto Rico, 2.62MGD UF and 1.73MGD  BWRO System s - to be 
completed 2025  
o Absolics -Chip Facility  Project  Georgia  – WWTS : Sludge  System  - 
Completed 2024  
o Pulmuone Food Facility - California - WWTP : DAF - Completed 
2022 
o TECO Bayside Power Station – Forida - Demineralizer System 
Upgrade  (0.576 MGD Max)  Completed 2023  
o TECO - Polk Power Station -Reclaimed Water Project (TECO RTP)  
Original and Expansion 1 - Florida  - BWRO Systems  (3 x 2.4MGD)  
Completed  2015 | 2017  
o Ammonia and Urea Plant, Mary, Turkmenistan: Clarifiers, R.O. , 
Deionised  systems, Mixed Bed Polishers for process and power 
plant. Completed in Sept 2014  
o Grand Bahama Power Company, Grand Bahama: Containerized 
SWRO System.  Completed March 2008    

============================================================
--- PAGE 118 ---
============================================================
 Andrew L.   
Fuller  
Cont’ . 
 
 
 
Personnel  Resume  BW Water Americas Inc.  | 3 
 
o Saqqara, Egypt:  DMF, SWRO, UV, Demin, Deaerator for Oil 
Platform .  Completed June 2008   
o Altamira II, Tampico, Mexico: DMF, RO, Deaerator, Demin for 
Power  plant boiler feed. Completed in November 2002  
 
1995 - 2000: J. Wray and Nephew  - Kingston, Ja mica .  
- Overall responsibility for all plant maintenance (Electrical and 
Mechanical).  
- Supervised the water team for process water production.  
- Implemented annual budgets for plant maintenance, purchasing 
tools and equipment, and staff training.  
- Introduced innovative ideas to improve plant equipment efficiency 
in line with company goals.  
- Ensured the safety of operating equipment and maintained 
employee awareness of safety issues.  
- Responsible for maintaining the ISO 9002 quality system for the 
Engineering section.  
 
Note  (*): Company name changes:  
Nov.2023 - Present BW Water Americas Inc.  | Jul 2017 - Nov.2023  SafBon Water 
Technology  Inc. | Sept 2015 – July 2017 Doosan Hydro Technology  LLC/ Inc.  | Before  
Sept. 2015 American  Engineering Service  Inc.  
  

============================================================
--- PAGE 119 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.119 
 
18.2  PRELIMINARY ON SITE FIELD SERVICE PROGRAM  
To ensure the successful completion of commissioning and start-up activities, and to facilitate the 
subsequent achievement of Provisional and Final Acceptance , a final program and timeline will be 
developed and submitted following mutual agreement after system delivery. 
Below is a preliminary milestone schedule  based on current project requirements and conditions: 
 Delivery Period : Maximum of 300 calendar days  after the start date  
 Installation Supervision, Commissioning and Start-Up, Testing, and Training Period : 
Maximum of 21 calendar days , initiated upon ADASA’s formal request and confirmation by 
Adasa on Pre-check list that will state the required conditions and items needed by supplier 
(bidder) to go to site and initiate the on-site supervision services described in this proposal.  
This formal request from ADASA will occur within 180 calendar days  following receipt of the 
UHPRO system by ADASA.  
 On-Site Field Service Advance Notice : ADASA will notify the supplier 30 calendar days in 
advance  of the required site appearance date. 
 Documentation and Close-Out : within 30 calendar days  after completion of commissioning 
and start-up activities to submit all required documentation and fulfill all conditions necessary 
for Provisional Acceptance (substantial completion)  of the order (BAE- Section 41) 
 Final Acceptance: after warranty period  
Please refer to the Preliminary Project Execution Schedule  attached (see Section 11 of this proposal) 
for further details. 
In accordance with Technical Specifications P22-ET-09-000-001, Sections 9 and 10, and the applicable 
Sections 9 to 13 of the Technical Report P22-IT-09-000-001, the On-Site Field Service Program will 
define the key steps, requirements for: 
- Installation Supervision  
- Commissioning & Start-up, including On-site performance testing to verify proper operation of 
the supplied system 
- Training of ADASA personnel responsible for system operation 
- Project close-out activities required to obtain Provisional Acceptance 
- Warranty Period and Final Acceptance  
All commissioning and start-up activities will be conducted at the Taltal Desalination Plant, located within 
ADASA’s regional property at Guillermo Matta 221, Ciudad de Taltal, Región de Antofagasta. 

============================================================
--- PAGE 120 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.120 
 
18.3 RESOURCES AND ASSIGNED SPECIALISTS TO BE USED 
If our company is selected as the successful bidder for this project, Mr. Fuller will be responsible for 
selecting/assigning the field service team and coordinating with agreed and approved third parties 
(subvendors), if applicable, and the client to carry out all installation supervision, commissioning, start-
up, on-site performance testing, and client training activities. 
He will develop the final On-Site Field Service Program that was mentioned in section 18.2 of Proposal 
above where resources and assigned field service personnel and specialist will be identified: 
Here is preliminary Resources and Assigned Specialists Plan for the On-Site Field Service Program/ 
supporting the installation supervision, commissioning, start-up performance testing, and operator 
training of a containerized Ultra High-Pressure Osmosis (UHPRO) system for brine recycle treatment 
ADASA project  
 Resources and Assigned Specialists Plan (Preliminary-Sample Plan) 
I. Project Scope Overview 
This plan outlines the personnel and resources required to support the successful deployment and 
operational readiness of the containerized UHPRO system. The scope includes: 
 Check list and verification of requirement to initiate any on-site field service program  
 Installation supervision 
 Mechanical and electrical Start-up  
 Commissioning and performance testing 
 Operator training and handover 
 
II. Assigned Specialists and Roles 
Role/Activity  Specialist Responsibilities  Estimated 
Duration   Expected No. of 
people & No. trips  
Field Service 
Manager Principal in charge /Sr 
manager for field Svc. 
Scope  
(Andrew Fuller) Overall coordination, 
client liaison, reporting. 
Compliance checks, risk 
assessments  1 person,  
1Trip, if needed 
Installation 
Supervision Mechanical engineer  
and  
Electrical I&C engineer Supervision of 
mechanical assembly, 
piping, and skid 
placement  
PLC integration, I/O 
checks, instrumentation 
setup Within 9 
Business 
Days 1 to 2 People 
and 1 trip 

============================================================
--- PAGE 121 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.121 
 
Role/Activity  Specialist Responsibilities  Estimated 
Duration   Expected No. of 
people & No. trips  
Commissioning/ 
Start-up 
Performance 
testing and 
Operator Trainer Field service Engineer System flushing, 
pressure testing, 
membrane loading, 
performance validation,  
On-site training 
sessions, SOP 
handover, 
troubleshooting 
guidance Within 12 
business 
day  1 person 
and 1 trip 
III. Support Resources 
 Tools & Equipment xxx 
 Calibration kits 
 Flow meters and pressure gauges 
 Electrical testing tools 
 
IV. Documentation 
 Pre-check of Onsite field services activities Accreditation fo personal as needed 
 Schedule. 
 Installation drawings 
 Commissioning checklists 
 SOPs and training manuals 
 Performance test protocols 
 Final & close up documentation for acceptance  
 
V. Coordination with Client and Local Teams 
 Weekly progress meetings with client representatives x 
 Integration with local contractors for utilities and civil works 
 

============================================================
--- PAGE 122 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.122 
 
 
 
 
 
 
 
DOCUMENT No. 3 – 
GUARANTEED SEC VALUE  
 
 
 
 

============================================================
--- PAGE 123 ---
============================================================
 Confidential  
 
Technical Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F Rev.1 AUG. 19 2025 | Pg.123 
 
19. SIGNED DECLARATION OF THE SPECIFIC ENERGY 
CONSUMPTION (SEC) GUARANTEED VALUE 
(Ref.: Bases Administrativas Especiales (BAE), Section 20.1 – Document 3 “Declaración de Consumo 
Específico de Energía Eléctrica Garantizado (CEE Garantizado))” 
BW Water Americas Inc. (BWWA) has prepared Document 3 – “ Declaración de Consumo Específico 
de Energía Eléctrica Garantizado (CEE Garantizado” ” (in English Declaration of Guaranteed Specific 
Electrical Energy Consumption (CEE Guaranteed)) 
The revised signed Guaranteed SEC declaration letter is attached. 
 

============================================================
--- PAGE 124 ---
============================================================



================================================================================
## 8. OFERTA ECONOMICA BW WATER
================================================================================
# Oferta Economica BW Water

## Metadatos
- **Archivo origen**: OFERTA ECONOMICA BW WATER.pdf
- **Paginas**: 17
- **Fecha extraccion**: 2025-11-25

---

## Contenido Extraido


---

### Pagina 1
---
 
 
4520 Oak Fair Blvd, Suite 200 
Tampa, FL 33610 - USA 
www.bw-water.com.com   
 
 
 
To: Aguas Antofagasta S.A. (ADASA) Commercial Proposal for 
ADASA’s Taltal Desalination 
Plant – Brine Recovery Project  
- UHPRO System 
 
Client Ref.: Proceso de Licitación 12803 SUMINISTRO 
MÓDULO RO SEGUNDA ETAPA PARA SALMUERA - 
PLANTA DESALADORA TALTAL (ex 12783) 
BW Water Americas Inc. 
 
BWWA Ref. No: 20.24.6501.F Rev.1 
September 15, 2025 | Confidential  

---

### Pagina 2
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.2 
 
PROPRIETARY , PATENT NOTICE & CONFIDENTIALITY AGREEMENT  
 
This proposal and the concept of the system are the intellectual property of BW Water and its 
Affiliates and are subject to legal copyright. The contents of this proposal shall not be disclosed 
by the Recipient to any third party without the expressed written consent of BW Water groups. 
National and International patents protect core parts of our systems. 
BW Water group reserves the right to alter the proposed system to incorporate technical 
advances realized after the date of this proposal.   
 
BW Water’s information and the recommendations presented in this proposal (hereinafter 
referred to as "Confidential Information") are the work product of BW Water Gorup and are 
provided solely with the understanding and agreement that the information contained in this 
document is submitted for evaluation only. The recipient agrees not to reveal its contents 
except to those in Recipient’s organization necessary for evaluation and copies of this 
document may not be distributed outside of the Recipient organization. 
 
By receiving and accepting this proposal, the recipient agrees to the stated terms and 
conditions. 
 
  

---

### Pagina 3
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.3 
 
Contents 
1. COVER LETTER  ...................................................................................................... 4  
2. CLIENT REQUIRED FORM AND SUBMISSION  ..................................................... 6  
3. BWWA COMMERCIAL OFFER  ............................................................................... 8  
3.1 PRICE ....................................................................................................................... 8  
3.2 VALIDITY .................................................................................................................. 9  
3.3 DELIVERY AND SCHEDULES ................................................................................ 9  
3.4 TERMS OF PAYMENT ............................................................................................. 9  
3.5 WARRANTY ........................................................................................................... 10  
3.5.1 Warranty Exclusions ..................................................................................... 10  
3.6 FIELD SERVICE ..................................................................................................... 10  
3.7 MANDATORY/CRITICAL SPARE PARTS LIST FOR COMMISSIONING AND START-
UP PHASES .................................................................................................................. 11  
3.8 RECOMMENDED TWO-YEAR SPARE PARTS LIST (option) ............................. 13  
3.9 ATTACHMENTS ..................................................................................................... 15  
 
 

---

### Pagina 4
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.4 
 
1. COVER LETTER 
BW Water Americas Inc. (BWWA) is pleased to present its revised Commercial Proposal, following the 
discussion and clarification meeting held on September 17, 2025, and in response to the initial 
submission made on September 15, 2025. 
As instructed, the Sworn Statement (Declaración Jurada) and Itemized Budget (Presupuesto Itemizado) 
documents have been resubmitted without annotations, and the previously commented BAE document 
has been excluded from this submission. 
Following our successful completion of the prequalification process and the evaluation of our Technical 
Proposal Rev. 1, submitted on August 19, 2025, we received formal notification on August 26, 2025, 
confirming our approval to submit a commercial offer for the public tender: 
“Proceso de Licitación 12803 – SUMINISTRO MÓDULO RO SEGUNDA ETAPA PARA SALMUERA 
- PLANTA DESALADORA TALTAL (ex 12783)” 
This offer pertains to the supply of an Ultra-High-Pressure Reverse Osmosis (UHPRO)  system, 
including ancillary components, for Aguas Antofagasta S.A. (ADASA) , as part of the Brine Recovery 
Project at the Taltal Seawater Desalination Treatment Plant  in Chile. 
Our submission reflects BWWA’s commitment to becoming the selected vendor for this system 
package. It has been prepared in accordance with the instructions outlined in the “Bases 
Administrativas Especiales” (BAE), Sections 21 and 21.1 , and is based on our Technical Proposal 
(Rev. 1, dated August 19, 2025), which has been evaluated and accepted by ADASA. 
We are proposing a containerized UHPRO system  designed to treat 1,176 m³/day  of brine from the 
existing Taltal desalination plant. The system will produce desalinated water that meets the Client’s 
project requirements and supports the goal of increasing potable water production for human 
consumption, without increasing raw water extraction from existing wells. 
With over 35 years of global experience  in the water and wastewater industry, BWWA offers a robust, 
reliable, and efficient RO solution tailored to meet ADASA’s water quality and production needs. Our 
proposed solution, branded as Brine Positive , incorporates components from internationally 
recognized manufacturers and complies with the technical specifications and design drawings provided 
by the Client. 
Our scope of supply includes a standalone, containerized second-stage UHPRO system  capable of 
producing 21 m³/hour  at a 42.85% recovery rate , along with all necessary ancillary components to 
ensure a comprehensive and integrated solution. BWWA brings proven engineering expertise, in-house 
fabrication capabilities, and a global network of qualified service providers to deliver a high-performance 
system aligned with the Client’s goals. 

---

### Pagina 5
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.5 
 
We look forward to the opportunity to collaborate with ADASA and contribute to the successful delivery 
of this important infrastructure project. Should you require any further information or clarification, we 
remain at your disposal. 
Best regards, 
BW Water Americas Inc. 
 

---

### Pagina 6
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.6 
 
2. CLIENT REQUIRED FORM AND SUBMISSION  
(Ref.: BAE - Section 21 “Entrega de Ofertas Económicas”, Section 21.1 “Documentos que se deben 
incluir en las Ofertas”, Section 23 “Garantía de Seriedad de la Oferta”) 
In accordance with the instructions and requirements outlined in the BAE, the following forms and 
documents—except as noted below—have been submitted via ADASA’s Portal, which is the only 
authorized channel for transmitting the commercial offer package. 
1. Bid Bank Guarantee (Garantía de Seriedad de la Oferta) – Physical Document 
Delivery to ADASA’s Oficina de Partes 
Original document was delivered to the ADASA’ Oficinas de Partes before 2:00 PM Chile time  
As supporting documentation, we have submitted the following via the Portal under “Doc 2.1 – BID 
BOND / BANK GUARANTEE COPY”: 
 Copy of Bid bank guarantee (Ref. 2482725000023684, USD 26.000,00) 
 Signed Copy of proof of delivery of guarantee 
 
2. GROUP 1 (Referred to in the BAE as “SOBRE 1”) 
The following documents were uploaded via ADASA’s Portal in the designated section: 
 Doc1.1_01  – FORMULARIO_DE_COTIZACIÓN_LICITACIÓN_12803 (PDF) 
 Doc1.2_01  – DECLARACIÓN JURADA N°1 PROPUESTA ECONÓMICA (PDF) 
 Doc1.3_02  – FORMATO PRESUPUESTO ITEMIZADO 12803 (PDF) 
 Doc1.3_02  – FORMATO PRESUPUESTO ITEMIZADO 12803 (Excel – Native Format) 
 Doc1.4_OPTIONAL  – 2-YEAR RECOMMENDED SPARE PARTS (PDF) 
 Doc1.4_OPTIONAL  – 2-YEAR RECOMMENDED SPARE PARTS (Excel – Native Format) 
 Doc1.5 – BWWA COMMERCIAL PROPOSAL / OFFER (PDF) (This document) 
 
3. GROUP 2 (Referred to in the BAE as “SOBRE 2”) 
The following documents were uploaded via ADASA’s Portal in the designated section: 
 Doc2.1 – BID BOND / BANK GUARANTEE COPY (PDF) 
 Doc2.2 – ACLARACIONES (Forms 1 to 10) (PDF) 
 Doc2.3_02 – DECLARACIÓN JURADA N°2 CARPETA DOCUMENTOS ANEXOS (PDF) 

---

### Pagina 7
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.7 
 
 Doc2.4_03 – DECLARACIÓN JURADA N°3 CONFLICTO DE INTERÉS 12803 (PDF) 
 Doc2.5_04 – DECLARACIÓN JURADA N°4 CONFIDENCIALIDAD (PDF) 
 Doc2.6_05 – DECLARACIÓN JURADA N°5 PSEC 12803 (PDF) 
 Doc2.7_07 – DECLARACIÓN JURADA N°7 SUBCONTRATACIÓN 12803 (PDF) 
 Doc2.8_08 – DECLARACIÓN JURADA N°8 USO APROPIADO DE CIBERACTIVOS 12803 
(PDF) 
 Doc2.9_09 – DECLARACIÓN JURADA N°9 COMPROMISO CON LA SSO 12803 (PDF) 
 Doc2.10_10 – DECLARACIÓN JURADA N°10 PEP 12803 (PDF) 
 Doc2.11_11 – DECLARACIÓN JURADA N°11 DDHH ADASA 12803 (PDF) 
 
Note: Due to file size limitations, we are not including herein the copies of documents listed in Group 1 
and Group 2 above. These documents were individually submitted in their respective designated upload 
boxes. 
 

---

### Pagina 8
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.8 
 
3. BWWA COMMERCIAL OFFER 
3.1 PRICE 
BW Water Americas (BWWA) offers to furnish the proposed Brine Positive System solution as defined 
in our Technical Proposal Rev. 1, dated August 19, 2025, for the following price: 
 EXW Incoterms (Ex-Works – Manufacturing and Assembly Penang, Malaysia | 
Materials/Components (RO Membranes, South Korea))  
 
Item Description Qty. | 
Unit Total Value (USD) 
 
1 Design and supply of containerized UHPRO module system 
for brine recovery, as defined in Technical Proposal – 
Document No. 1, Section 4 1 
Unit/set $ 579,884.00 
2 Mandatory/Critical Spare Parts List for commissioning and 
start-up, as defined in Technical Proposal – Document No. 1, 
Section 14 and Commercial proposal section 3.12 (priced 
list)  1 
Unit/set $ 17,310.00 
3 Commissioning and Start-up Services, as defined in 
Technical Proposal – Document No. 2, Section 18 and 
related subsections. Also, Commercial proposal Section 3.11  1 
Unit/set $ 16,797.00 
 TOTAL Price USD - EXW Incoterms   $ 613,991.00 
 
 DDP Incoterms (Delivered Duty Paid – Taltal, Antofagasta, Chile) 
 
Item Description Qty. | 
Unit Total Price (USD) 
 
1 Design and supply of containerized UHPRO module system 
for brine recovery, as defined in Technical Proposal – 
Document No. 1, Section 4 1 
Unit/set $ 602,028.00 
2 Mandatory/Critical Spare Parts List for commissioning and 
start-up, as defined in Technical Proposal Section 14 and 
Commercial proposal section 3.12( priced updated list)  1 
Unit/set $ 17,310.00 
3 Commissioning and Start-up Services, as defined in 
Technical Proposal – Document No. 2, Section 18 and 
related subsections. Also, Commercial proposal Section 3.11  1 
Unit/set $ 16,798.00 
 TOTAL Price USD – DDP Incoterms   $ 636,136.00 

---

### Pagina 9
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.9 
 
 Options Pricing  
Item Description Qty. | 
Unit Total Value (USD) 
 
1 Recommended 2-year Spare Parts list.as defined in 
Technical Proposal – Section 15 and Commercial proposal 
section 3.13 (priced updated list) 1 
Unit/set $43,7090 
(EXW) 
3.2 VALIDITY 
This proposal is valid for ninety (90) days from the date of issue. After this period, pricing may be subject 
to escalation. 
3.3 DELIVERY AND SCHEDULES 
A final project execution schedule will be established based on the requirements stated in specs and a 
mutually agreed timeline following contract finalization. However, please refer to the preliminary 
chronograms provided in our Technical Proposal — Sections 11, 11.1, and 18.2 — which are based on 
current requirements and conditions. 
 Delivery terms offered: 
 Ex-Works Incoterm: BWWA’s sub vendors) 
 DPA Incoterm: Taltal, Antofagasta, Chile. 
3.4 TERMS OF PAYMENT 
The following initial payment schedule is proposed: 
a) Engineering Approval – 10% of Total Price (pro rata) 
Payable upon formal written approval by ADASA of critical engineering documents. A list of these 
documents is to be defined and mutually agreed upon. 
b) Purchase Orders for Main Equipment – Approval Stage – 30% of Total Price (pro rata) 
Payable once the Supplier has submitted confirmed purchase orders for the main equipment. 
c) Purchase Orders for Main Equipment – Manufacturing Stage – 30% of Total Price (pro rata) 
Payable once the Supplier has commenced manufacturing of the equipment. 
d) Factory Acceptance Tests (FAT) – 10% of Total Price 
Payable upon receipt of the FAT Approval Certificate issued by ADASA, confirming satisfactory 
completion of factory acceptance tests. 

---

### Pagina 10
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP.18 2025 | Pg.10 
 
e) Release of Order – 10% of Total Price 
Payable upon issuance of written shipping authorization (Release Certificate) by ADASA for the module. 
f) Provisional Acceptance – 10% of Total Price 
Final payment to be made upon ADASA’s formal approval of the Provisional Acceptance of the Order. 
Payment Terms: All payments are due Net 30 days from the date of invoice submission and shall be 
made via wire transfer to the Seller’s designated bank account. 
3.5 WARRANTY  
BWWA will provide a standard equipment warranty covering all furnished equipment for a period of 24 
months from the date of receipt of the Provisional Acceptance Certificate  issued by the Client to 36 
months from the date of the last shipment of goods — whichever occurs first. 
3.5.1 Warranty Exclusions 
BWWA’s responsibilities under this article do not extend to repairs, adjustments, alterations, 
replacements, or maintenance required due to: 
 Normal wear and tear resulting from regular operation of the project, or 
 The Buyer’s failure to operate or maintain the system in accordance with the provided Operation 
& Maintenance (O&M) Manual. 
The RO membranes warranty will be passed through directly from the manufacturer. 
No additional warranty will be provided by BWWA for these components. 
3.6 FIELD SERVICE 
Please refer to our Technical Proposal – Section 18  and related subsections for details on the 
following on-site technical supervision activities included in this project: 
 Installation supervision 
 Commissioning and start-up, including on-site performance testing and close-out activities 
 Training of ADASA personnel responsible for system operation 
Any additional field services beyond the final agreed scope of work will be available under the terms 
outlined in the attached field service policy. 
 

---

### Pagina 11
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP. 18 2025 | Pg.11 
 
3.7 MANDATORY/CRITICAL SPARE PARTS LIST FOR COMMISSIONING AND START-UP 
PHASES  
A preliminary priced list of mandatory/critical spares is presented in the table below.  
This list is aligned with Document P22-ET-09-000-001-0, Section 6 – Item “Suministro de Repuestos Mandatorios para Puesta en 
Marcha”, and with our Technical Proposal Rev. 1 dated August 19, 2025 – Section 14. 
 
Manufacturer  Part # Description  Qty. Unit Unit Price (USD) 
EXW terms Extended Amount  Notes 
Hardware 
Fil-Trek, Sysflo, or 
Equivalent tba Cartridge Filter 1 set  $                  6,120.00  $                 6,120.00 ET - Section 6 (related to 
Item 5.1.5). 
 tba tba Fuses used in the panels 1 set  $                     410.00  $                    410.00 ET - Section 6 (related to 
Item 5.4). 
Rosemount, E+H, 
Burkert or Equivalent  tba Pressure Transmitter 1 unit  $                  1,720.00  $                 1,720.00 Used in the HP system  
ET - Section 6 (related to 
Item 5.5.3). 
Rosemount , 
Thornton, or 
Equivalent tba Conductivity 
sensor/electrode 1 set  $                  1,180.00  $                 1,180.00 Used on the line of final 
permeate  
ET - Section 6 (related to 
Item 5.5.5). 
Flexitallic or 
Equivalent tba Seal/gasket kit 1 set  $                     400.00  $                    400.00 For HP Victaulic pipe 
ET - Section 6 (related to 
Item 5.2.2 
ABB, E+H, or 
Equivalent tba Flowmeter 1 unit  $                  4,840.00  $                 4,840.00  

---

### Pagina 12
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP. 18 2025 | Pg.12 
 
Manufacturer  Part # Description  Qty. Unit Unit Price (USD) 
EXW terms Extended Amount  Notes 
Ashcroft, Wika, or 
Equivalent tba Pressure Gauges, 
SS304/316 3 unit  $                     730.00  $                 2,190.00  
IFM or Equivalent tba Level Transmitter 1 unit  $                     450.00   
        
        
TOTAL - Mandatory Spares List   $              17,310.00   
 
 

---

### Pagina 13
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP. 18 2025 | Pg.13 
 
3.8 RECOMMENDED TWO-YEAR SPARE PARTS LIST (option) 
A preliminary priced list of recommended 2-year Spares is presented in the table below.  
This list is aligned with Document P22-ET-09-000-001-0, Section 6 – Item “Listado y Cotización Opcional de Repuestos para Dos 
Años”, and with our Technical Proposal Rev. 1 dated August 19, 2025 – Section 15. and file uploaded to ADASA Portal “Doc1.4 (PDF 
and excel versions) 
Manufacturer  Part No.  Description  Qty. Unit Unit Price (USD) 
EXW terms  Notes 
Hardware   
Tampa Rubber EPDM 
Gaskets or Equivalent Custom Part Set of Gaskets (Low Pressure – 
Plastic Pipe)  4 set  $                   240.00  $                    960.00   
Flexitallic or Equivalent  Custom Part Set pf Gaskets (High Pressure)  2 set  $                   400.00  $                    800.00   
Protec Arisawa 77DX Flexible Coupling, Style 77DX, 
2.5″, Duplex bolt & SS316 nut 20 unit  $                   150.00  $                 3,000.00   
Protec Arisawa 2081006 RO Vessel Head Assembly  1 unit  $               2,380.00  $                 2,380.00   
Protec Arisawa 4080474-1 RO Vessel Head Locking Ring  3 unit  $                   640.00  $                 1,920.00   
Protec Arisawa 6100442MK RO Vessel Seal Set  2 set  $                   510.00  $                 1,020.00   
Protec Arisawa 5080074 RO Membrane Adapters  4 unit  $                  580.00  $                 2,320.00   
Fedco or Equivalent MSD-130 repair 
kit SWRO High Pressure Pump 
Service Kit  1 set  $               9,560.00  $                 9,560.00   
Pulsafeeder, Prominent 
or Equivalent LB02SA-XXXX 
(or equal) Chemical Dosing Pump Repair 
Kit  2 set  $               1,780.00  $                 3,560.00   
Foxboro, E+H or 
Equivalent pH 10 (or equal)  pH Sensor  1 unit  $               2,060.00  $                 2,060.00   
Foxboro, E+H or 
Equivalent ORP 10 (or equal)  ORP Sensor  1 unit  $               2,060.00  $                 2,060.00   

---

### Pagina 14
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP. 18 2025 | Pg.14 
 
Manufacturer  Part No.  Description  Qty. Unit Unit Price (USD) 
EXW terms  Notes 
Thornton, E+H or 
Equivalent Cond. Sensor Conductivity Sensor  1 unit  $               1,370.00  $                 1,370.00   
Bray or Equivalent Series 63, 
120VAC Solenoid Valve  2 unit  $               1,650.00  $                 3,300.00   
Ashcroft, Wika or 
Equivalent Series 45, Monel  Pressure Gauge, Monel  2 unit  $                   730.00  $                 1,460.00   
Valves  
Bray or Equivalent S01-0200  3” Lined Butterfly Valve   1 unit  $               1,350.00  $                 1,350.00    
Asahi/America/Modenti
c  or Equivalent Type 57L 2.5” Lined Butterfly Valve   1 unit  $               1,290.00  $                 1,290.00    
Asahi/America/Modenti
c  or Equivalent Type 57L 2” Lined Ball Valve  1 unit  $               1,100.00  $                 1,100.00   
Asahi/America/Hydrose
al or Equivalent Type 57P 4” Plastic Butterfly Valve  1 unit  $                   550.00  $                    550.00   
Asahi/America/Hydrose
al or Equivalent Type 57P 3” Plastic Butterfly Valve  1 unit  $                   500.00  $                    500.00   
Asahi/America/Hydrose
al or Equivalent Type  21 2” Plastic Ball Valve  1 unit  $                   240.00  $                    240.00   
Asahi/America/Hydrose
al or Equivalent TB Series 1.5 Plastic Ball Valve  5 unit  $                   240.00  $                 1,200.00   
Asahi/America/Hydrose
al or Equivalent Type  21 1” Plastic Ball Valve  5 unit  $                   110.00  $                    550.00   
        
TOTAL – Recommended 2 Years Spares List   $         43,790.00 
 

---

### Pagina 15
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 Rev.18 2025 | Pg.15 
 
3.9 ATTACHMENTS 
The following documents are included after this page 
1. BWWA’s Field Service Policy  
 
 

---

### Pagina 16
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 Rev.18  2025 | Attach. 1  
 
 
 
 
 
 
 
Attachment 1 
 
 
 

---

### Pagina 17
---
 Confidential  
 
Commercial Proposal  
 
 
 
BW Water Americas Inc.  
BWWA Ref. No.20.24.6501.F (Commercial) Rev.1 SEP 18 2025 | Attach. 2  
 
 
 
 
 
 
 
Attachment 2 
 
 
 


================================================================================
## 9. PRESUPUESTO ITEMIZADO
================================================================================
# Presupuesto Itemizado - Licitacion 12803

## Metadatos
- **Archivo origen**: Doc1.3_02 Presupuesto Itemizado 12803_BWWASep.182025_s.pdf
- **Paginas**: 1
- **Fecha extraccion**: 2025-11-25

---

## Contenido Extraido


---

### Pagina 1
---
1 / 1
Linea DescripciónUnidad
de
MedidaCantidadPrecio Unitario
USDPrecio Total
USD
1 Suministro y Diseño Módulo RO Segunda Etapa para Salmuera Unidad 1 579,884.00 579,884.00
2 Repuestos Mandatorios según ET Unidad 1 17,310.00 17,310.00
3 Comisionamiento y Puesta en Marcha Unidad 1 16,797.00 16,797.00
TOTAL USD (*) 613,991.00
Linea DescripciónUnidad
de
MedidaCantidadPrecio Unitario
USDPrecio Total
USD
1 Suministro y Diseño Módulo RO Segunda Etapa para Salmuera Unidad 1 602,028.00 602,028.00
2 Repuestos Mandatorios según ET Unidad 1 17,310.00 17,310.00
3 Comisionamiento y Puesta en Marcha Unidad 1 16,797.00 16,798.00
TOTAL USD 636,136.00
Firma Representate Legal
Empresa Prestador de ServiciosFORMATO PRESUPUESTO ITEMIZADO 12803
A) 12803  SUMINISTRO Módulo RO Segunda Etapa para Salmuera - PD Taltal  (EXW)
PRECIO EX-WORKS : $613,991.00
INDICAR LUGAR ORIGEN:  Fabricación y montaje Penang, Malasia | Materials/componetes ( RO Membranas,  Corea del  Sur) 
PAIS: various ( Corea del Sur and Malasia)
MONEDA: USD DOLARES AMERICANOS
* Detalle a subir en el sistema de licitaciones de Aguas Antofagasta
B) 12803  SUMINISTRO Módulo RO Segunda Etapa para Salmuera - PD Taltal  -  ( VALOR DDP)  
PRECIO DDP:  $636,135.00
LUGAR DE ENTREGA:  SOBRE CAMION  EN PLANTA DESALADORA TAL TAL, ANTOFAGASTA.
MONEDA: USD DOLARES AMERICANOS
