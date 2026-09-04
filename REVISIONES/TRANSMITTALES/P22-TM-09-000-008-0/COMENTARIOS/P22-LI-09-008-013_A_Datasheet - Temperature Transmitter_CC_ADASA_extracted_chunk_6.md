| Transducer | N/A |
| LCD display block | N/A |
| Analog input 1 | 45 |
| Analog Input 2 | 45 |
| PID 1 | 60 |


| Schedule entries | 25 |
| --- | --- |
| Links | 16 |
| Virtual Communications Relationships (VCR) | 12 |

Rosemount 644
June 2025
PID block
The transmitter provides control functionality with one PID function block in the transmitter. The PID block can be used
to perform single loop, cascade, or feedforward control in the field.
Turn-on time
Performance within specifications in less than 20 seconds after power is applied, when damping value is set to zero
seconds.
Status
If self-diagnostics detect a sensor burnout or a transmitter failure, the status of the measurement will be updated
accordingly. Status may also send the AI output to a safe value.
Power supply
Powered over FOUNDATION Fieldbus with standard Fieldbus power supplies. The transmitter operates between 9.0 and
32.0 Vdc, 12 mA maximum.
Alarms
The AI function block allows the user to configure the alarms to HI-HI, HI, LO, or LO-LO with hysteresis settings.
Backup Link Active Scheduler (LAS)
The transmitter is classified as a device link master, which means it can function as a LAS if the current link master
device fails or is removed from the segment.
The host or other configuration tool is used to download the schedule for the application to the link master device.
In the absence of a primary link master, the transmitter will claim the LAS and provide permanent control for the H1
segment.
FOUNDATION Fieldbus parameters
PROFIBUS® PA specifications
Function blocks
Physical block
The physical block contains physical transmitter information including manufacturer identification, device type,
software tag, and unique identification.
www.Emerson.com 23

============================================================
--- PAGE 222 ---
============================================================
Rosemount 644
June 2025
Transducer block
The transducer block contains the actual temperature measurement data, including sensor 1 and terminal
temperature. It includes information about sensor type and configuration, engineering units, linearization, re-ranging,
damping, temperature correction, and diagnostics.
Analog Input block (AI)
The AI block processes the measurement and makes it available on the PROFIBUS segment. Allows filtering, alarming,
and engineering unit changes.
Turn-on time
Performance within specifications in less than 20 seconds after power is applied, when damping value is set to zero
seconds.
Powersupply
Powered over PROFIBUS® with standard Fieldbus™ power supplies. The transmitter operates between 9.0 and 32.0
Vdc,12 mA maximum.
Alarms
The AI function block allows the user to configure the alarms to HI-HI, HI, LO, or LO-LO with hysteresis settings.
4–20 mA/HART® specifications
Power supply
External power supply required. Transmitters operate on 12.0–42.4 Vdc transmitter terminal voltage (with 250 ohm
load, 18.1  Vdc power supply voltage is required). Transmitter power terminals rated to 42.4 Vdc.
Figure 2: Load Limitations
Maximum load = 40.8 × (supply voltage - 12.0)(1)
4−20 mA dc
1240
1100
1000
)s
m HART and Analog
h 750
o operating range
(
d
a 500
o
L
250 Analog only
0 operating range
10 18.1 30 42.4
12.0 Min
(1) Without transient protection (optional).
Note
HART® Communication requires a loop resistance between 250 and 1100 ohms. Do not communicate with the
transmitter when power is below 12 Vdc at the transmitter terminals.
24 www.Emerson.com

============================================================
--- PAGE 223 ---
============================================================

| Description | Operating limit(1) | Storage limit(1) |
| --- | --- | --- |
| With LCD display(2) | –40 to 185 °F<br>–40 to 85 °C | –50 to 185 °F<br>–45 to 85 °C |
| Without LCD display | –40 to 185 °F<br>–40 to 85 °C | –58 to 250 °F<br>–50 to 120 °C |


| Units - mA | Min | Max | Rosemount | Namur |
| --- | --- | --- | --- | --- |
| High alarm | 21 | 23 | 21.75 | 21 |
| Low alarm(1) | 3.5 | 3.75 | 3.75 | 3.6 |
| High saturation | 20.5 | 20.9(2) | 20.5 | 20.5 |
| Low saturation(1) | 3.7(3) | 3.9 | 3.9 | 3.8 |


| Sensor options | Sensor<br>reference | Input ranges | | Minimum span (1) | | Digital<br>accuracy (2) | | D/A accuracy(3)(4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2-, 3-, 4-wire RTDs | | °C | °F | °C | °F | °C | °F | |
| Pt 100 (α = 0.00385) | IEC 751 | –200 to<br>850 | –328 to<br>1562 | 10 | 18 | ± 0.1 | ± 0.18 | ± 0.03% of span |
| Pt 200 (α = 0.00385) | IEC 751 | –200 to<br>850 | –328 to<br>1562 | 10 | 18 | ± 0.15 | ± 0.27 | ± 0.03% of span |
| Pt 500 (α = 0.00385) | IEC 751 | –200 to<br>850 | –328 to<br>1562 | 10 | 18 | ± 0.19 | ± 0.34 | ± 0.03% of span |

Rosemount 644
June 2025
Temperature limits
(1) The lower operating and storage temperature limit of a transmitter with option code BR6 is –76 °F (–60 °C).
(2) LCD display may not be readable and display updates will be slower at temperatures below –22 °F (–30 °C).
Hardware and software failure mode
The Rosemount 644 features software driven alarm diagnostics and an independent circuit, which is designed to
provide backup alarm output if the microprocessor software fails. The alarm direction (HI/LO) is user-selectable using
the failure mode switch. If failure occurs, the position of the switch determines the direction in which the output is
driven (HI or LO). The switch feeds into the digital-to-analog (D/A) converter, which drives the proper alarm output
even if the microprocessor fails. The values at which the transmitter software drives its output in failure mode depends
on whether it is configured to standard, custom, or NAMUR-compliant (NAMUR recommendation NE 43, June 1997)
operation. Table 16 shows the configuration alarm ranges.
Table 16: Available Alarm Range
(1) Requires 0.1 mA gap between low alarm and low saturation values.
(2) Rail mount transmitters have a high saturation max of 0.1 mA less than the high alarm setting, with a max value of 0.1 mA less than
the high alarm max.
(3) Rail mount transmitters have a low saturation min of 0.1 mA greater than the low alarm setting, with a minimum of 0.1 mA greater
than the low alarm min.
Custom alarm and saturation level
Custom factory configuration of alarm and saturation level is available with option code C1 for valid values. These
values can also be configured in the field using a Field Communicator.
Turn-on time
Performance within specifications in less than six seconds after power is applied, when damping value is set to zero
seconds.
Standard accuracy
Table 17: Rosemount 644 Transmitter Accuracy
www.Emerson.com 25

============================================================
--- PAGE 224 ---
============================================================

| Table 17: Rosemount 644 Transmitter Accuracy (continued) | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pt 1000 (α = 0.00385) | IEC 751 | –200 to<br>300 | –328 to<br>572 | 10 | 18 | ± 0.19 | ± 0.34 | ± 0.03% of span |
| Pt 100 (α = 0.003916) | JIS 1604 | –200 to<br>645 | –328 to<br>1193 | 10 | 18 | ± 0.1 | ± 0.18 | ± 0.03% of span |
| Pt 200 (α = 0.003916) | JIS 1604 | –200 to<br>645 | –328 to<br>1193 | 10 | 18 | ± 0.27 | ± 0.49 | ± 0.03% of span |
| Ni 120 | Edison Curve<br>No. 7 | –70 to<br>300 | –94 to<br>572 | 10 | 18 | ± 0.15 | ± 0.27 | ± 0.03% of span |
| Cu 10 | Edison Copper<br>Winding No. 15 | –50 to<br>250 | –58 to<br>482 | 10 | 18 | ± 1.40 | ± 2.52 | ± 0.03% of span |
| Pt 50 (α=0.00391) | GOST 6651-94 | –200 to<br>550 | –328 to<br>1022 | 10 | 18 | ± 0.30 | ± 0.54 | ± 0.03% of span |
| Pt 100 (α=0.00391) | GOST 6651-94 | –200 to<br>550 | –328 to<br>1022 | 10 | 18 | ±0.1 | ± 0.18 | ± 0.03% of span |
| Cu 50 (α=0.00426) | GOST 6651-94 | –50 to<br>200 | –58 to<br>392 | 10 | 18 | ± 1.34 | ± 2.41 | ± 0.03% of span |
| Cu 50 (α=0.00428) | GOST 6651-94 | –185 to<br>200 | –301 to<br>392 | 10 | 18 | ± 1.34 | ± 2.41 | ± 0.03% of span |
| Cu 100 (α=0.00426) | GOST 6651-94 | –50 to<br>200 | –58 to<br>392 | 10 | 18 | ± 0.67 | ± 1.20 | ± 0.03% of span |
| Cu 100 (α=0.00428) | GOST 6651-94 | –185 to<br>200 | –301 to<br>392 | 10 | 18 | ± 0.67 | ± 1.20 | ± 0.03% of span |
| Thermocouples (5) | | | | | | | | |
| Type B (6) | NIST<br>Monograph<br>175, IEC 584 | 100 to<br>1820 | 212 to<br>3308 | 25 | 45 | ± 0.77 | ± 1.39 | ± 0.03% of span |
| Type E | NIST<br>Monograph<br>175, IEC 584 | –200 to<br>1000 | –328 to<br>1832 | 25 | 45 | ± 0.20 | ± 0.36 | ± 0.03% of span |
| Type J | NIST<br>Monograph<br>175, IEC 584 | –180 to<br>760 | –292 to<br>1400 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.03% of span |
| Type K (7) | NIST<br>Monograph<br>175, IEC 584 | –180 to<br>1372 | –292 to<br>2501 | 25 | 45 | ± 0.50 | ± 0.90 | ± 0.03% of span |
| Type N | NIST<br>Monograph<br>175, IEC 584 | –200 to<br>1300 | –328 to<br>2372 | 25 | 45 | ± 0.50 | ± 0.90 | ± 0.03% of span |
| Type R | NIST<br>Monograph<br>175, IEC 584 | 0 to 1768 | 32 to<br>3214 | 25 | 45 | ± 0.75 | ± 1.35 | ± 0.03% of span |
| Type S | NIST<br>Monograph<br>175, IEC 584 | 0 to 1768 | 32 to<br>3214 | 25 | 45 | ± 0.70 | ± 1.26 | ± 0.03% of span |
| Type T | NIST<br>Monograph<br>175, IEC 584 | –200 to<br>400 | –328 to<br>752 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.03% of span |
| Type L | DIN 43710 | –200 to<br>900 | –328 to<br>1652 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.03% of span |
| Type U | DIN 43710 | –200 to<br>600 | –328 to<br>1112 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.03% of span |

Rosemount 644
June 2025
Table 17: Rosemount 644 Transmitter Accuracy (continued)
26 www.Emerson.com

============================================================
--- PAGE 225 ---
============================================================

| Table 17: Rosemount 644 Transmitter Accuracy (continued) | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Type C | W5Re/W26Re<br>ASTM E 988-96 | 0 to 2000 | 32 to<br>3632 | 25 | 45 | ± 0.70 | ± 1.26 | ± 0.03% of span |
| Type L | GOST R<br>8.585-2001 | –200 to<br>800 | –392 to<br>1472 | 25 | 45 | ± 0.25 | ± 0.45 | ± 0.03% of span |
| Other input types | | | | | | | | |
| Millivolt input | | –10 to 100 mV | | 3 mV | | ± 0.015 mV | | ± 0.03% of span |
| 2-, 3-, 4-wire Ohm input | | 0 to 2000 ohms | | 20 ohm | | ± 0.45 ohm | | ± 0.03% of span |


| Sensor options | Sensor reference | Input range<br>(°C) | Temperature effects per<br>1.0 °C (1.8 °F) change in<br>ambient temperature(1)(2)(3) | Range | D/A effect (4) |
| --- | --- | --- | --- | --- | --- |
| 2-, 3-, 4-wire RTDs | | | | | |
| Pt 100 (α = 0.00385) | IEC 751 | –200 to 850 | 0.003 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 200 (α = 0.00385) | IEC 751 | –200 to 850 | 0.004 °C (0.0072 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 500 (α = 0.00385) | IEC 751 | –200 to 850 | 0.003 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 1000 (α = 0.00385) | IEC 751 | –200 to 300 | 0.003 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |

Rosemount 644
June 2025
Table 17: Rosemount 644 Transmitter Accuracy (continued)
(1) No minimum or maximum span restrictions within the input ranges. Recommended minimum span will hold noise within accuracy
specification with damping at zero seconds.
(2) Digital accuracy: Digital output can be accessed by the Field Communicator.
(3) Total analog accuracy is the sum of digital and D/A accuracies.
(4) Applies to HART®/4–20 mA devices.
(5) Total digital accuracy for thermocouple measurement: sum of digital accuracy +0.25 °C (0.45 °F) (cold junction accuracy).
(6) Digital accuracy for NIST Type B is ±3.0 °C (±5.4 °F) from 100 to 300 °C (212 to 572 °F).
(7) Digital accuracy for NIST Type K is ±0.7 °C (±1.3 °F) from –180 to –90 °C (–292 to –130 °F).
Accuracy example (HART devices)
When using a Pt 100 (α = 0.00385) sensor input with 0 to 100 °C span:
■ Digital accuracy = ± 0.1 °C
■ D/A accuracy = ± 0.1 °C of 100 °C or ± 0.1 °C
■ Total accuracy = ± 0.13 °C
Accuracy example (FOUNDATION™ Fieldbus and PROFIBUS® PA devices)
When using a Pt 100 (α = 0.00385) sensor input:
■ Total accuracy = ±0.15 °C
■ No D/A accuracy effects apply.
Table 18: Ambient Temperature Effect
www.Emerson.com 27

============================================================
--- PAGE 226 ---
============================================================

| Table 18: Ambient Temperature Effect (continued) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Sensor options | Sensor reference | Input range<br>(°C) | Temperature effects per<br>1.0 °C (1.8 °F) change in<br>ambient temperature(1)(2)(3) | Range | D/A effect (4) |
| Pt 100 (α = 0.003916) | JIS 1604 | –200 to 645 | 0.003 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 200 (α = 0.003916) | JIS 1604 | –200 to 645 | 0.004 °C (0.0072 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Ni 120 | Edison Curve No. 7 | –70 to 300 | 0.003 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Cu 10 | Edison Copper<br>Winding No. 15 | –50 to 250 | 0.03 °C (0.0054 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 50 (α = 0.00391) | GOST 6651-94 | –200 to 550 | 0.004 °C (0.0072 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Pt 100 (α = 0.00391) | GOST 6651-94 | –200 to 550 | 0.002 °C (0.0036 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Cu 50 (α = 0.00426) | GOST 6651-94 | –50 to 200 | 0.008 °C (0.0144 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Cu 50 (α = 0.00428) | GOST 6651-94 | –185 to 200 | 0.008 °C (0.0144 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Cu 100 (α = 0.00426) | GOST 6651-94 | –50 to 200 | 0.004 °C (0.0072 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Cu 100 (α = 0.00428) | GOST 6651-94 | –185 to 200 | 0.004 °C (0.0072 °F) | Entire<br>sensor<br>input<br>range | 0.001% of span |
| Thermocouples | | | | | |
| Type B | NIST Monograph 175,<br>IEC 584 | 100 to 1820 | 0.014 °C | T ≥ 1000 °C | 0.001% of span |
| | | | 0.032 °C – (0.0025% of (T –<br>300)) | 300 °C ≤ T<br>< 1000 °C | 0.001% of span |
| | | | 0.054 °C – (0.011% of (T –<br>100)) | 100 °C ≤ T<br>< 300 °C | 0.001% of span |
| Type E | NIST Monograph 175,<br>IEC 584 | –200 to 1000 | 0.005 °C + (0.00043% of T) | All | 0.001% of span |
| Type J | NIST Monograph 175,<br>IEC 584 | –180 to 760 | 0.0054 °C + (0.00029%of T) | T ≥ 0 °C | 0.001% of span |

Rosemount 644
June 2025
Table 18: Ambient Temperature Effect (continued)
28 www.Emerson.com

============================================================
--- PAGE 227 ---
============================================================

| Table 18: Ambient Temperature Effect (continued) | | | | | |
| --- | --- | --- | --- | --- | --- |
| Sensor options | Sensor reference | Input range<br>(°C) | Temperature effects per<br>1.0 °C (1.8 °F) change in<br>ambient temperature(1)(2)(3) | Range | D/A effect (4) |
| | | | 0.0054 °C + (0.0025% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| Type K | NIST Monograph 175,<br>IEC 584 | –180 to 1372 | 0.0061 °C + (0.00054% of T) | T ≥ 0 °C | 0.001% of span |
| | | | 0.0061 °C + (0.0025% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| Type N | NIST Monograph 175,<br>IEC 584 | –200 to 1300 | 0.0068 °C + (0.00036% of T) | All | 0.001% of span |
| Type R | NIST Monograph 175,<br>IEC 584 | 0 to 1768 | 0.016 °C | T ≥ 200 °C | 0.001% of span |
| | | | 0.023 °C – (0.0036% of T) | T < 200 °C | 0.001% of span |
| Type S | NIST Monograph 175,<br>IEC 584 | 0 to 1768 | 0.016 °C | T ≥ 200 °C | 0.001% of span |
| | | | 0.023 °C – (0.0036% of T) | T < 200 °C | 0.001% of span |
| Type T | NIST Monograph 175,<br>IEC 584 | –200 to 400 | 0.0064 °C | T ≥ 0 °C | 0.001% of span |
| | | | 0.0064 °C +(0.0043% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| DIN Type L | DIN 43710 | –200 to 900 | 0.0054 °C + (0.00029% of T) | T ≥ 0 °C | 0.001% of span |
| | | | 0.0054 °C + (0.0025% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| DIN Type U | DIN 43710 | –200 to 600 | 0.0064 °C | T ≥ 0 °C | 0.001% of span |
| | | | 0.0064 °C + (0.0043% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| Type W5Re/W26Re | ASTM E 988-96 | 0 to 2000 | 0.016 °C | T ≥ 200 °C | 0.001% of span |
| | | | 0.023 °C – (0.0036% of T) | T < 200 °C | 0.001% of span |
| GOST Type L | GOST R 8.585-2001 | -200 to 800 | 0.007 °C | T ≥ 0 °C | 0.001% of span |
| | | | 0.007 °C + (0.003% of<br>absolute value T) | T < 0 °C | 0.001% of span |
| Other input types | | | | | |
| Millivolt input | | –10 to 100 mV | 0.0005 mV | Entire<br>sensor<br>input<br>range | 0.001% of span |
| 2-, 3-, 4-wire Ohm | | 0 to 2000 Ω | 0.0084 Ω | Entire<br>sensor<br>input<br>range | 0.001% of span |

Rosemount 644
June 2025
Table 18: Ambient Temperature Effect (continued)
(1) Change in ambient is with reference to the calibration temperature of the transmitter 68 °F (20 °C) from factory.
(2) Ambient temperature effect specification valid over minimum temperature span of 50 °F (28 °C).
(3) Ambient temperature effects are tripled for temperature below –40 °C.
(4) Does not apply to FOUNDATION Fieldbus.
Temperature effects example (HART devices)
When using a Pt 100 (α = 0.00385) sensor input with a 0–100 °C span at 30 °C ambient temperature:
■ Digital temperature effects: 0.003 °C x (30 – 20) = 0.03 °C
■ D/A effects: [0.001% of 100] x (30 – 20) = 0.01 °C
www.Emerson.com 29

============================================================
--- PAGE 228 ---
============================================================

| Sensor options | Sensor<br>reference | Input ranges | | Minimum<br>span(1) | | Digital accuracy(2) | | D/A<br>accuracy(3)(4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2-, 3-, 4-wire RTDs | | °C | °F | °C | °F | °C | °F | |
| Pt 100 (α = 0.00385) | IEC 751 | –200 to 850 | –328 to 1562 | 10 | 18 | ± 0.08 | ± 0.14 | ± 0.02% of span |
| Pt 200 (α = 0.00385) | IEC 751 | –200 to 850 | –328 to 1562 | 10 | 18 | ± 0.22 | ± 0.40 | ± 0.02% of span |
| Pt 500 (α = 0.00385) | IEC 751 | –200 to 850 | –328 to 1562 | 10 | 18 | ± 0.14 | ± 0.25 | ± 0.02% of span |
| Pt 1000 (α = 0.00385) | IEC 751 | –200 to 300 | –328 to 572 | 10 | 18 | ± 0.10 | ± 0.18 | ± 0.02% of span |
| Pt 100 (α = 0.003916) | JIS 1604 | –200 to 645 | –328 to 1193 | 10 | 18 | ± 0.08 | ± 0.14 | ± 0.02% of span |
| Pt 200 (α = 0.003916) | JIS 1604 | –200 to 645 | –328 to 1193 | 10 | 18 | ± 0.22 | ± 0.40 | ± 0.02% of span |
| Ni 120 | Edison Curve<br>No. 7 | –70 to 300 | –94 to 572 | 10 | 18 | ± 0.08 | ± 0.14 | ± 0.02% of span |
| Cu 10 | Edison Copper<br>Winding No. 15 | –50 to 250 | –58 to 482 | 10 | 18 | ± 1.00 | ± 1.80 | ± 0.02% of span |
| Pt 50 (α = 0.00391) | GOST 6651-94 | –200 to 550 | –328 to 1022 | 10 | 18 | ± 0.20 | ± 0.36 | ± 0.02% of span |
| Pt 100 (α = 0.00391) | GOST 6651-94 | –200 to 550 | –328 to 1022 | 10 | 18 | ± 0.08 | ± 0.14 | ± 0.02% of span |
| Cu 50 (α = 0.00426) | GOST 6651-94 | –50 to 200 | –58 to 392 | 10 | 18 | ± 0.20 | ± 0.36 | ± 0.02% of span |
| Cu 50 (α = 0.00428) | GOST 6651-94 | –185 to 200 | –301 to 392 | 10 | 18 | ± 0.34 | ± 0.61 | ± 0.02% of span |
| Cu 100 (α = 0.00426) | GOST 6651-94 | –50 to 200 | –58 to 392 | 10 | 18 | ± 0.17 | ± 0.31 | ± 0.02% of span |
| Cu 100 (α = 0.00428) | GOST 6651-94 | –185 to 200 | –301 to 392 | 10 | 18 | ± 0.17 | ± 0.31 | ± 0.02% of span |
| Thermocouples(5) | | | | | | | | |
| Type B(6) | NIST<br>Monograph<br>175, IEC 584 | 100 to 1820 | 212 to 3308 | 25 | 45 | ± 0.75 | ± 1.35 | ± 0.02% of span |
| Type E | NIST<br>Monograph<br>175, IEC 584 | –200 to 1000 | –328 to 1832 | 25 | 45 | ± 0.20 | ± 0.36 | ± 0.02% of span |
| Type J | NIST<br>Monograph<br>175, IEC 584 | –180 to 760 | –292 to 1400 | 25 | 45 | ± 0.25 | ± 0.45 | ± 0.02% of span |
| Type K(7) | NIST<br>Monograph<br>175, IEC 584 | –180 to 1372 | –292 to 2501 | 25 | 45 | ± 0.25 | ± 0.45 | ± 0.02% of span |

Rosemount 644
June 2025
■ Worst case error: Digital + D/A + Digital Temperature Effects + D/A Effects = 0.1 °C + 0.03 °C + 0.03 °C + 0.01 °C =
0.17 °C
■ Total probable error: = 0.11 °C
Temperature effects examples (FOUNDATION Fieldbus devices and PROFIBUS PA)
When using a Pt 100 (α = 0.00385) sensor input at 30 °C span at 30 °C ambient temperature:
■ Digital temperature effects: 0.003 °C × (30 – 20) = 0.03 °C
■ D/A effects: No D/A effects apply.
■ Worst case error: Digital + Digital temperature effects = 0.10 °C + 0.03 °C = 0.13 °C
■ Total probable error: = 0.104 °C
Table 19: Transmitter accuracy when ordered with option code P8
30 www.Emerson.com

============================================================
--- PAGE 229 ---
============================================================

| Table 19: Transmitter accuracy when ordered with option code P8 (continued) | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Type N | NIST<br>Monograph<br>175, IEC 584 | –200 to 1300 | –328 to 2372 | 25 | 45 | ± 0.40 | ± 0.72 | ± 0.02% of span |
| Type R | NIST<br>Monograph<br>175, IEC 584 | 0 to 1768 | 32 to 3214 | 25 | 45 | ± 0.60 | ± 1.08 | ± 0.02% of span |
| Type S | NIST<br>Monograph<br>175, IEC 584 | 0 to 1768 | 32 to 3214 | 25 | 45 | ± 0.50 | ± 0.90 | ± 0.02% of span |
| Type T | NIST<br>Monograph<br>175, IEC 584 | –200 to 400 | –328 to 752 | 25 | 45 | ± 0.25 | ± 0.45 | ± 0.02% of span |
| DIN Type L | DIN 43710 | –200 to 900 | –328 to 1652 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.02% of span |
| DIN Type U | DIN 43710 | –200 to 600 | –328 to 1112 | 25 | 45 | ± 0.35 | ± 0.63 | ± 0.02% of span |
| Type W5Re/W26Re | ASTM E 988-96 | 0 to 2000 | 32 to 3632 | 25 | 45 | ± 0.70 | ± 1.26 | ± 0.02% of span |
| GOST Type L | GOST R<br>8.585-2001 | –200 to 800 | –392 to 1472 | 25 | 45 | ± 0.25 | ± 0.45 | ± 0.02% of span |
| Other input types | | | | | | | | |
| Millivolt input | | –10 to 100 mV | | 3 mV | | ± 0.015 mV | | ± 0.02% of span |
| 2-, 3-, 4-wire Ohm input | | 0 to 2000 ohms | | 20 ohm | | ± 0.35 ohm | | ± 0.02% of span |

Rosemount 644
June 2025
Table 19: Transmitter accuracy when ordered with option code P8 (continued)
(1) No minimum or maximum span restrictions within the input ranges. Recommended minimum span will hold noise within accuracy
specification with damping at zero seconds.
(2) Digital accuracy: Digital output can be accessed by the Field Communicator.
(3) Total Analog accuracy is the sum of digital and D/A accuracies.
(4) Applies to HART/4–20 mA devices.
(5) Total digital accuracy for thermocouple measurement: sum of digital accuracy +0.25 °C (0.45 °F) (cold junction accuracy).
(6) Digital accuracy for NIST Type B is ±3.0 °C (±5.4 °F) from 100 to 300 °C (212 to 572 °F).
(7) Digital accuracy for NIST Type K is ±0.7 °C (±1.3 °F) from –180 to –90 °C (–292 to –130 °F).
Reference accuracy example (HART only)
When using a Pt 100 (α = 0.00385) sensor input with a 0 to 100 °C span: Digital Accuracy would be ±0.08 °C, D/A
accuracy would be ±0.02% of 100 °C or ±0.02 °C, Total = ±0.1 °C.
Differential capability exists between any two sensor types (dual-sensor option)
For all differential configurations, the input range is X to Y where:
■ X = Sensor 1 minimum – Sensor 2 maximum
■ Y = Sensor 1 maximum – Sensor 2 minimum
www.Emerson.com 31

============================================================
--- PAGE 230 ---
============================================================

| HART® device shown with captivated screw terminals | FOUNDATION Fieldbus and PROFIBUS® device shown with standard<br>compression screw terminals |
| --- | --- |
| 60 (2.4)<br>C<br>33 (1.3)<br>D<br>59 (2.3)<br>B<br>24 (.96)<br>A<br>E<br>59 (2.3)<br>31 (1.2) | 60 (2.4)<br>C 33 (1.3)<br>B 23 (1.0)<br>F<br>D<br>E<br>59 (2.3)<br>26 (1.0) |
| A. Failure mode switch<br>B. Meter connector<br>C. Sensor terminals | D. Communication terminals<br>E. Power terminals<br>F. Simulation switch |

Rosemount 644
June 2025
Dimensional drawings
Figure 3: Rosemount 644H (DIN A Head Mount)
Note
Dimensions are in millimeters (inches).
32 www.Emerson.com

============================================================
--- PAGE 231 ---
============================================================

| Transmitter exploded view | |
| --- | --- |
| | |
| Display compartment | Terminal compartment |
| G<br>F | H<br>I<br>J |
| A. Nameplate<br>B. Cover<br>C. Housing with electronics module<br>D. LCD display<br>E. Display cover | F. Failure mode switch<br>G. Meter connector<br>H. Sensor terminals<br>I. Communication terminals<br>J. Power terminals |

Rosemount 644
June 2025
Figure 4: Rosemount 644 Field Mount
www.Emerson.com 33

============================================================
--- PAGE 232 ---
============================================================
Rosemount 644
June 2025
Note
Dimensions are in millimeters (inches).
Figure 5: Mounting kits for Rosemount 644H
B
C
A
A. Top hat rail grooves
B. G-rail grooves
C. Screw holes for mounting to a wall
34 www.Emerson.com

============================================================
--- PAGE 233 ---
============================================================

| G-Rail (asymmetric) | Top hat rail (symmetric) |
| --- | --- |
| D<br>E<br>F | D<br>E<br>F |
| D. Mounting hardware<br>E. Transmitter<br>F. Rail clip | |
| Note<br>Kit (part number 00644-5301-0010) includes mounting hardware and both types of rail kits. | |
| | |
| | |
| | |
| Note<br>Part number 03044-4103-0001. | |
| | |

Rosemount 644
June 2025
Figure 6: Rosemount 644H Rail Clips
www.Emerson.com 35

============================================================
--- PAGE 234 ---
============================================================

| Threaded-sensor universal head<br>(option code J5, J6, J7 or J8) | DIN style sensor connection head<br>(option code R1, R2, R3 or R4) |
| --- | --- |
| 112<br>(4.4)<br>96<br>(3.8)<br>95<br>(3.7)<br>C 7<br>(3.<br>103 (4.0) with<br>LCD Display<br>75<br>(2.9)<br>D | 104<br>(4.0)<br>8<br>0)<br>128 (5.0) with<br>LCD Display<br>100<br>(3.9) |

Rosemount 644
June 2025
Figure 7: Threaded-Sensor Universal Head and DIN Style Sensor Connection Head
B
A
A. Standard cover
B. Display cover
C. LCD display
D. SST “U” Bolt Mounting, 2-in. pipe (shipped with connection heads J5-J8 when ordered without assembly option XA)
Note
Dimensions are in millimeters (inches).
36 www.Emerson.com

============================================================
--- PAGE 235 ---
============================================================
Rosemount 644
June 2025
Figure 8: Threaded Sensor Universal Head, 3-conduit (Opti
on code J1 or J2)
LKS
COIND
LKM
COIKD
]
TKIT
CNIQD
\
LKMIQ COIKD
with g^_ ~over
SPIT
CNIOD
A. Standard cover
B. Display cover
Note
Dimensions are in millimeters (inches).
www.Emerson.com
37

============================================================
--- PAGE 236 ---
============================================================

| HART® device shown with transient protector (Option code T1) | FOUNDATION Fieldbus device shown with transient protector<br>(Option code T1) |
| --- | --- |
| 59<br>(2.3)<br>33<br>(1.3)<br>A<br>C<br>68<br>(2.7)<br>24<br>(0.96)<br>D<br>B F<br>40 G<br>(1.6)<br>31<br>(1.2)<br>F | 33<br>(1.3)<br>A<br>E<br>67<br>(2.7)<br>38<br>(1.5)<br>C<br>D<br>F<br>59 G<br>(2.3)<br>26<br>(1.0)<br>F |

Rosemount 644
June 2025
Figure 9: Device shown with Transient Protector
A. Sensor terminals
B. Failure mode switch
C. Meter connector
D. Power terminals
E. Simulation switch
F. Transient protector
G. Ground wire
Note
Dimensions are in millimeters (inches).
Option code T1 requires the use of J1, J2, J3 or J4 enclosure option.
38 www.Emerson.com

============================================================
--- PAGE 237 ---
============================================================

| Sanitary housing (option code S1, S2, S3, S4) | |
| --- | --- |
| Standard cover | LCD display cover |
| A B C<br>80 76<br>(3.1) 33 (1.3) (3.0)<br>28 (1.1)<br>25<br>(1.0)<br>45<br>24 (1.8)<br>(0.96)<br>70<br>(2.8) | D B C<br>61<br>(2.4) (14 .7 9) 33 (1.3) (37 .6 0)<br>28 (1.1)<br>25<br>74 (1.0)<br>(2.9) 45<br>(1.8)<br>70<br>(2.8) |
| A. Standard cover<br>B. O-ring<br>C. Housing<br>D. LCD display cover | |

Rosemount 644
June 2025
Accessory dimensional drawings
Figure 10: Stainless Steel Housing for Biotechnology, Pharmaceutical Industries, and Sanitary Applications
Note
Dimensions are in millimeters (inches).
www.Emerson.com 39

============================================================
--- PAGE 238 ---
============================================================

| LCD display | Enhanced display with LOI |
| --- | --- |
| B<br>A<br>C | A<br>D<br>C<br>B |
| A. LCD display<br>B. Rosemount 644 Transmitter<br>C. Display rotation<br>D. LCD display with LOI | |

Rosemount 644
June 2025
Figure 11: Display
Note
Dimensions are in millimeters (inches).
40 www.Emerson.com

============================================================
--- PAGE 239 ---
============================================================

| Option Code B4 Bracket for enclosures J1, J2, J3, and J4 | Option code B4 bracket for enclosures D1 and D2 |
| --- | --- |
| | |
| 100<br>(3.9) 60<br>(2.4) 30<br>(1.2)<br>25<br>(1.0)<br>25<br>(1.0)<br>25<br>(1.0)<br>2<br>(0.065)<br>112<br>(4.4)<br>76<br>(3.0)<br>4<br>(0.14) | |
| | |

Rosemount 644
June 2025
Figure 12: Optional Mounting
Note
Dimensions are in millimeters (inches).
www.Emerson.com 41

============================================================
--- PAGE 240 ---
============================================================

| Option Code B5 Bracket for enclosures J1, J2, J3, and J4 | Option code B5 bracket for enclosures D1 and D2 |
| --- | --- |
| | |
| 60 60<br>(2.4) (2.4)<br>175<br>(6.9)<br>19<br>71 (0.75)<br>(2.8)<br>19<br>156 (0.75) 2<br>(6.2) (0.083)<br>71<br>(2.8) | |

Rosemount 644
June 2025
Note
Dimensions are in millimeters (inches).
Configuration
Transmitter configuration
The transmitter is available with standard configuration setting for either HART®, FOUNDATION™ Fieldbus or PROFIBUS®
PA. The configuration settings and block configuration may be changed in the field with Emerson DeltaV™, AMS Suite,
Field Communicator or other host or configuration tool.
42 www.Emerson.com

============================================================
--- PAGE 241 ---
============================================================

| Sensor type | RTD, Pt 100 (α=0.00385, 4-wire) |
| --- | --- |
| 4 mA value | 0 °C |
| 20 mA value | 100 °C |
| Output | Linear with temperature |
| Saturation levels | 3.9/20.5 mA |
| Damping | 5 seconds |
| Line voltage filter | 50 Hz |
| Alarm | High (21.75 mA) |
| LCD display (when installed) | Engineering units and mA |
| Tag | See Tagging. |

Rosemount 644
June 2025
Table 20: Standard HART® configuration
Unless specified, the transmitter will be shipped as follows:
Table 21: Standard FOUNDATION Fieldbus configuration
Unless otherwise specified, the transmitter will be shipped as follows:
Sensor type: RTD, Pt 100 (α=0.00385, 4-wire)
Damping: 5 seconds
Units of measurement: °C
Line voltage filter: 50 Hz
Software tag: See Tagging
Function block tags:
■ Resource block: Resource
■ Transducer block: Transducer
■ LCD display block: LCD display
■ Analog input blocks: AI 1300, AI 1400
PID block: PID 1500
Alarm limits of AI 1300, AI 1400
■ HI-HI: Infinity
■ HI: Infinity
■ LO: Infinity
■ LO-LO: Infinity
Local display (when installed): Engineering units of temperature
www.Emerson.com 43

============================================================
--- PAGE 242 ---
============================================================
Rosemount 644
June 2025
Figure 13: Standard Block Configuration
■ T1= sensor temperature
■ Tb= terminal temperature
Final stations
AI blocks are scheduled for one second. AI blocks are linked as shown in Figure 13.
Table 22: Standard PROFIBUS® PA configuration
Unless specified, the transmitter will be shipped as follows:
Device address: 126
Sensor Type: RTD, Pt 100 (α=0.00385, 4-wire)
Damping: 5 seconds
Units of measurement: °C
Line voltage filter: 50 Hz
Software tag: see Tagging.
Alarm limits:
■ HI-HI: Infinity
■ HI: Infinity
■ LO: - Infinity
■ LO-LO: Infinity
Local display (when installed): Engineering units of temperature
Custom configuration
Custom configurations are to be specified when ordering. This configuration must be the same for all sensors. The
table lists the necessary requirements to specify a custom configuration:
44 www.Emerson.com

============================================================
--- PAGE 243 ---
============================================================

| Option code | Customization available |
| --- | --- |
| C1: Factory Configuration Data (CDS required) | ■ Date: day/month/year<br>■ Descriptor: 8 alphanumeric characters<br>■ Message: 32 alphanumeric characters<br>■ Hardware tag: 18 characters<br>■ Software tag: 8 characters<br>■ Sensor type and connection<br>■ Measurement range and units<br>■ Damping value<br>■ Failure mode: High or Low<br>■ Hot Backup: Mode and PV<br>■ Sensor drift alert: Mode, limit and units |
| ...M4 or M5 | ■ Display configuration: Select what will be shown on the LCD<br>display. |
| ...DC, A1, CN, or C8 | ■ Custom alarm and saturation levels: Choose custom High<br>and Low alarm and saturation levels. |
| ...DC | ■ Security information: Write protection, HART® Lock and LOI<br>password |
| C2:Transmitter – sensor matching | ■ The transmitters are designed to accept Callendar-Van Dusen<br>constants from a calibrated RTD. Using these constants, the<br>transmitter generates a custom curve to match the sensor-<br>specific curve. Specify a Rosemount RTD sensor model<br>on the order with a special characterization curve (V or<br>X8Q4 option). These constants will be programmed into the<br>transmitter with this option. |
| A1, CN, or C8: Alarm level configuration | ■ A1: NAMUR Alarm and saturation levels, with high alarm<br>configured<br>■ CN: NAMUR Alarm and saturation levels, with low alarm<br>configured<br>■ C8: Low alarm (standard Rosemount alarm and saturation<br>values) |
| Q4: Three-point calibration with certificate | ■ Calibration certificate. Three-point calibration at 0, 50, and<br>100% with certificate. |
| C4: Five-point calibration | ■ Will include five-point calibration at 0, 25, 50, 75, and<br>100% analog and digital output points. Use with Calibration<br>Certificate Q4. |
| HR7: HART Revision configuration | ■ Your Rosemount 644 head mount and field mount are HART<br>revision selectable. Order the HR7 code to configure your<br>device to operate in HART Revision 7 mode. Your device is<br>also configurable in the field. Refer to the Rosemount 644<br>Quick Start Guide or Reference Manual for more instructions.<br>■ Long software tag: 32 characters |

Rosemount 644
June 2025
Table 23: HART® Protocol
www.Emerson.com 45

============================================================
--- PAGE 244 ---
============================================================

| Option code | Requirements/specification |
| --- | --- |
| C1: Factory configuration data (CDS required) | Date: day/month/year<br>Descriptor: 16 alphanumeric characters<br>Message: 32 alphanumeric characters |
| C2: Transmitter – sensor matching | The transmitters are designed to accept Callendar-Van Dusen<br>constants from a calibrated RTD. Using these constants, the<br>transmitter generates a custom curve to match the sensor-<br>specific curve. Specify a Series 65, 65, or 78 RTD sensor on the<br>order with a special characterization curve (V or X8Q4 option).<br>These constants will be programmed into the transmitter with<br>this option. |
| C4: Five-point calibration | Will include five-point calibration at 0, 25, 50, 75, and 100%<br>analog and digital output points. Use with Calibration Certificate<br>Q4. |
| Q4: Three-point calibration with certificate | Calibration certificate. Three-point calibration with certificate. |


| Option code | Requirements/specification |
| --- | --- |
| C1: Factory Configuration Data (CDS required) | Date: day/month/year<br>Descriptor: 16 alphanumeric characters<br>Message: 32 alphanumeric characters |
| C2: Transmitter – Sensor Matching | The transmitters are designed to accept Callendar-Van Dusen<br>constants from a calibrated RTD. Using these constants, the<br>transmitter generates a custom curve to match the sensor-<br>specific curve. Specify a Series 65, or 78 RTD sensor on the<br>order with a special characterization curve (V or X8Q4 option).<br>These constants will be programmed into the transmitter with<br>this option. |
| C4: Five-point calibration | Will include five-point calibration at 0, 25, 50, 75, and 100%<br>analog and digital output points. Use with Calibration Certificate<br>Q4. |
| Q4: Three-point calibration with certificate | Calibration certificate. Three-point calibration with certificate. |

Rosemount 644
June 2025
Table 24: FOUNDATION Fieldbus Protocol
Table 25: PROFIBUS® PA
46 www.Emerson.com

============================================================
--- PAGE 245 ---
============================================================
Rosemount 644
June 2025
Product certifications
For Rosemount 644 product certifications, see the Rosemount 644 Temperature Transmitter Quick Start Guide.
European Directive Information
A copy of the EU Declaration of Conformity can be found at the end of the Quick Start Guide. The most recent revision
of the EU Declaration of Conformity can be found at Emerson.com/Rosemount.
Ordinary Location Certification
As standard, the Rosemount 644 Temperature Transmitter has been examined and tested to determine that the design
meets the basic electrical, mechanical, and fire protection requirements by a Nationally Recognized Test Laboratory
(NRTL) as accredited by the Federal Occupational Safety and Health Administration (OSHA).
North America
The US National Electrical Code® (NEC) and the Canadian Electrical Code (CEC) permit the use of Division marked
equipment in Zones and Zone marked equipment in Divisions. The markings must be suitable for the area
classification, gas, and temperature class. This information is clearly defined in the respective codes.
www.Emerson.com 47

============================================================
--- PAGE 246 ---
============================================================
00813-0100-4728
Rev. WG
June 2025
For more information: Emerson.com/global
©2025 Emerson. All rights reserved.
Emerson Terms and Conditions of Sale are available
upon request. The Emerson logo is a trademark and
service mark of Emerson Electric Co. Rosemount is a
mark of one of the Emerson family of companies. All
other marks are the property of their respective owners.