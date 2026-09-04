# COMPILADO INTERNO — TM N20 (E46 + E47)

**INTERNO ADASA — NO ENVIAR.** Fecha de trabajo: 10-Jun-2026. Entregas: 25007-0046 (28-May, 7 docs) + 25007-0047 (09-Jun, 13 docs). Total 20 documentos.

Contexto de urgencia: correo Yamauchi 10-Jun 9:52 pide aprobacion expedita de los 2 planos de panel PLC-LCP (fabricacion enclosure ~6 semanas, gatilla cadena hasta embarque a Chile). Propone revision por correo o reunion corta sobre material/dimensiones/diseno del enclosure.

## Tabla de disposicion (20 documentos)

| # | Doc | Rev | Titulo | Previo | Codigo TM N20 |
|---|-----|-----|--------|--------|----------------|
| 1 | P22-LI-09-008-003 | E | Instrument List | TM N17 Rev D Code 2 | **1** |
| 2 | P22-LI-09-008-004 | 1 | Data Transfer List (Modbus TCP/IP) | TM N17 Rev 0 Code 2 | **2** |
| 3 | P22-LI-09-008-012 | C | Pressure Transmitter Datasheet | TM N17 Rev B Code 2 | **1** |
| 4 | P22-LI-09-008-015 | B | Alarm & Interlock List | TM N17 Rev A Code 3 | **3** |
| 5 | P22-ET-09-007-005 | B | LCP Datasheet | TM N15 Rev A Code 3 | **2** |
| 6 | P22-CD-09-008-001 | A | PLC-LCP Outline Panel Drawing | Primera emision | **3** (driver panel) |
| 7 | P22-CD-09-008-002 | A | PLC/LCP Schematic Diagram | Primera emision | **2** (condicional) |
| 8 | P22-LI-09-007-001 | 0 | Electrical Load List (IFC) | TM N19 Rev B Code 1 | **1** |
| 9 | P22-LI-09-007-002 | 0 | Power Cable Schedule (IFC) | TM N19 Rev B Code 2 | **1** (OBS incorporada) |
| 10 | P22-ET-09-007-002 | 0 | DS Power & Control Cable (IFC) | TM N19 Rev B Code 1 | **1** |
| 11 | P22-CD-09-007-001 | 0 | Single Line Diagram (IFC) | TM N19 Rev B Code 2 | **1** (OBS+NOTE incorporadas, verificado visual) |
| 12 | P22-DWG-09-007-005 | 0 | Typical Installation Details (IFC) | TM N19 Rev C Code 2 | **1** (NOTE incorporada) |
| 13 | P22-LI-09-008-001 | 2 | I/O List | TM N19 Rev 1 Code 2 condicional | **3** (reversion contractual) |
| 14 | P22-LI-09-008-002 | 1 | IC Cable Schedule | TM N19 Rev 0 Code 3 | **3** (4 previas cerradas, QA nuevas) |
| 15 | P22-MTC-09-000-001 | A | Organization Chart | Primera emision | **1** (verificado visual) |
| 16 | P22-BA-09-000-001 | A | Project Schedule | Adoptado con reservas 09-Jun | **2** |
| 17 | P22-BA-09-000-005 | A | NDE Plan | Primera emision (responde TM N19 2.10 NOTE-01 parcial) | **3** |
| 18 | P22-BA-09-000-006 | A | PMI Procedure | Primera emision | **2** |
| 19 | P22-BA-09-000-007 | A | Welding Procedure | Primera emision | **2** |
| 20 | P22-BA-09-000-008 | A | Visual Procedure | Primera emision | **2** |

**Recuento: 8 Code 1 + 7 Code 2 + 5 Code 3. Veredicto: 3 — TO BE REVISED.**

## Drivers del veredicto

1. **PLC-LCP Outline Rev A (Code 3)** — contradiccion de material/IP dentro del propio paquete panel: Panel Specification Sheet (pag. 2) declara SHEET STEEL pintado RAL 7035 (herrajes CRS, placas zinc, solo plinto SUS316L) + PROTECTION CLASS IP55 + ventilacion forzada, mientras el LCP Datasheet Rev B declara nVent Hoffman FS66S **SS316L sin pintar, NEMA 4X/IP66**, ambiente "Harsh Industrial/Highly Corrosive", y el SLD Rev 0 IFC anota "P22-LCP-001 (METAL CLAD, NEMA4X/IP66)". ET — Caracteristicas constructivas de tableros exige NEMA 4X o equivalente IP. Es LA decision que gatilla la fabricacion (correo Yamauchi): sin Rev B del outline alineada, no hay release.
2. **Plant Control Philosophy Rev D — 4o ciclo consecutivo sin entregar.** La condicion suspensiva del Code 2 condicional del I/O List Rev 1 (TM N19) caduco: reversion a Code 3 explicita en TM N19 linea "Failure to deliver Rev D... reverts this acceptance to Code 3". Hoy bloquea: I/O List Rev 2, IC Cable Schedule Rev 1, Alarm & Interlock Rev B y condiciona el Schematic Rev A. Los remedies C-4300 reservados en TM N19 (14 dias desde 25-May) vencieron el 08-Jun.
3. **NDE Plan Rev A (Code 3)** — silencio total sobre el alcance vessel: sin hidrostatica de fabrica (1800 psi x 1.1 carta Protec), sin base ASME X/waiver 02-Jun, sin dossier ni punto de testigo. Ademas faltan los procedimientos Hydrostatic, Preservation y FAT + ITP Rev C (TM N19 2.10 OBS-01 CRITICAL sigue abierta).

## Detalle por documento (hallazgos verificados)

### 1. Instrument List Rev E — Code 1
4 items TM N17 cerrados: OBS-01 Wilcoxon justificado (12.7 mm/s peak = 8.9 mm/s rms, conversion 0.707, CCS pag. 3); NOTE-01 "No impact to procurement schedule" por escrito; NOTE-02 working medium "-" en items 7/18/19; NOTE-03 header CCS corregido a 25007 Taltal. Sin cambios de alcance (38 instrumentos). NOTA para Seccion 3: TIT-09-006 span 0-600 C (consistente en IL/DTL/A&I; rango de elemento PT100 plausible, operativo 0-100) — pedir confirmacion de configuracion, no degrada.

### 2. Data Transfer List Rev 1 — Code 2
Cerrados: NOTE-01 (Commissioning Reference: ADASA Master / PLC Slave / Big-Endian AB-CD / word swap OFF / byte swap OFF / IP 192.168.0.1) y NOTE-02 (rms). NUEVO OBS-01 MAJOR **(corregido vs agente)**: registro 30019 (item 143, CIT09-002) declara escala "0-20 uS/cm" — un span 0-20 uS/cm no puede leer permeado de 200-1000 uS/cm ni alarmar al AHH 800 uS/cm del A&I Rev B; el span del instrumento es 0-20000 uS/cm (= 0-20 mS/cm, IL Rev E). El registro 30021 (item 145, CIT09-003, "0-20 mS/cm") es numericamente consistente pero en unidad distinta a la convencion uS/cm del A&I. Armonizar ambos registros a un solo span declarado (0-20000 uS/cm o 0-20 mS/cm). NOTE nueva MINOR: confirmar span 0-600 C del registro TIT09-006 (item 152). Accion en IFC Rev 0, sin nueva revision.

### 3. Pressure Transmitter Datasheet Rev C — Code 1
OBS-01 cerrada (Hastelloy C PIT-001..008 con "No Impact to procurement schedule" escrito; PIT-009 SS316L); NOTE-01 cerrada (fila mal rotulada: ahora "Material - Diaphragm"; Aluminium solo housing — coherente con guia vendor). Rangos/tags cruzados limpios contra IL Rev E. 4-20 mA HART, IP66/67, NEMA 4X, SIL3.

### 4. Alarm & Interlock List Rev B — Code 3
Cerrados TM N17: OBS-01 (uS/cm reconciliado items 11/19, setpoints en banda permeado), OBS-02 (LS-09-002 = LSL), OBS-03 (ambos turbos AHH 6.0 mm/s -> Stop HP Pump), NOTE-01 (seccion digital items 34-51). NUEVOS (verificados):
- OBS-01 MAJOR: asignacion Winding/Bearing INVERTIDA vs IL Rev E en ambos trenes: IL TE-09-001=Winding/TE-09-002=Bearing (items 8/9) y TE-09-003=Winding/TE-09-004=Bearing (items 31/32); A&I declara TE-09-001=Bearing (AHH 90 C, item 27) / TE-09-002=Winding (AHH 140 C, item 28) y TE-09-003=Bearing (item 29) / TE-09-004=Winding (item 30). Con setpoints de trip distintos, el interlock actua sobre el sensor equivocado. Reconciliar IL+A&I+I/O List+datasheet motor (Fedco/Grundfos).
- OBS-02 MAJOR: TM N17 NOTE-02 sin aplicar — CCS pag. 8 dice "vendor confirmed to raise AHH to 95 C" pero item 27.1 mantiene 90.0 C. El doc contradice su propio CCS.
- OBS-03 MAJOR: tag PHIT-09-001 (item 25) vs PHIT-09-006 (IL Rev E item 35, DTL item 155). Tag divergente para el mismo analizador = falla de trazabilidad.
- NOTE-01 MINOR: TIT-09-005 (item 23) vs TIT-09-006 (IL item 28).
- NOTE-02 MINOR: LIT-09-002 rango 0-10 m con setpoints en % (95/90/30/15) sin declarar base.
Umbrella Rev D: setpoints no validables contra Control Philosophy vigente. Re-emitir Rev C.

### 5. LCP Datasheet Rev B — Code 2
TM N15: OBS-01 CERRADA (cover sheets por componente; 2x 5069-IY4 = 8 canales universales RTD-capaces + RTD1/RTD2 12 terminales = 4+4 Pt-100 a 3 hilos, per Schematic BOM); OBS-02 CERRADA (pag. 3: FS66S, SS316L, NEMA 4X/IP66, UL508A/IEC60529, "Harsh Industrial/Highly Corrosive"); OBS-03 PARCIAL — el datasheet sigue sin declarar consumo total del panel (Load List Rev 0 declara SAI-09-001 2.0 kW). Accion IFC Rev 0: declarar consumo de panel. El datasheet es el documento que gobierna el enclosure (vs Outline contradictorio).

### 6. PLC-LCP Outline Panel Drawing Rev A — Code 3 (DRIVER PANEL)
- OBS-01 CRITICAL: Panel Spec Sheet (pag. 2, verificada a 300 dpi): MAKE Hoffman (nVent); MODEL "SS FREESTANDING"; SIZE 1000+800(W) x 600(D) x 2000(H), QTY 1; COLOR GRAY RAL 7035; MATERIAL **SHEET STEEL** (frame/roof/rear/gland 2.0 mm, door 2.0, mounting plate 2.5 zinc-plated, plinth SUS316L 2.5); hinges/handle CRS 2.0; PROTECTION CLASS **IP55**; ENVIRONMENT "For Outdoor Use". Contradice LCP DS Rev B (SS316L/NEMA4X/IP66 sin pintar) + SLD Rev 0 + ET (NEMA 4X o equivalente). Para Taltal costero el material es decision de fabricacion: resolver ANTES del release.
- OBS-02 MAJOR: cooling por ventilador admision izq + extraccion der + filtro (pag. 2 fila 13 y pag. 3) — incompatible con IP66/NEMA4X salvo conjuntos filtro-ventilador con rating declarado; reconciliar con clase de proteccion y con AC Thermal Calc (carga LCP 0.14 kW; panel dentro del contenedor con HVAC: aclarar "Outdoor Use").
- OBS-03 MINOR: PANEL WEIGHT = placeholder "[Insert actual panel weight here / TBD]".
- NOTE-01 MINOR: portada "PD Tattal" (typo) + codigo ADASA impreso "P22-ET-09-008-001" (debe ser P22-CD-09-008-001).
Dimensiones verificadas: vistas pag. 3 1798 ancho x ~2000 alto x 600 prof. consistentes con spec sheet (1000+800). Re-emitir Rev B alineando el spec sheet al datasheet; documento que gatilla fabricacion (correo 10-Jun).

### 7. PLC/LCP Schematic Diagram Rev A — Code 2 (condicional)
71 laminas. Wiring regs: 380V 50Hz 3PH+N+PE, control 24VDC, main disconnect 400A, SCCR 36kA, cables 600V (pag. 4, verificada visual). Rack: 5069-L320ER + 2xIB16 (32 DI) + OB16 (16 DO) + 2xIY4 (8 AI universal/RTD) + 5xIF8 (40 AI) + 2xOF4 (8 AO); 276 terminales; RTD1/RTD2 12 term. (3 hilos). MCC: 2x PowerFlex 753 (HP 20F1ANC205 ~205A frame 6, adecuado para 93 kW; CIP), NSX400F/NSX250F (36 kA consistente SCCR), Acrel APM800. Asignaciones consistentes con I/O List Rev 2. NOTE-01: aceptacion condicional (mismo mecanismo I/O List TM N19) — divergencias de senal que introduzca Control Philosophy Rev D propagan al cableado del panel; capacidad spare debe absorberlas. Accion IFC Rev 0: confirmar asignacion I/O sin cambios tras Rev D.

### 8-12. Paquete electrico IFC Rev 0 — todos Code 1
- Load List Rev 0 = Rev B sin cambios (23 cargas, 144 kW c/SF, 312 A; SEC 3.97 kWh/m3). Fila rev "1/6/2026 ISSUED FOR CONSTRUCTION".
- Power Cable Schedule Rev 0: OBS-01 TM N19 INCORPORADA — REL-09-001 en dos cables explicitos: item 2 FEEDER(3P+N)->Heater Control Panel, item 3 Heater Control Panel->Heater Element (10 mm2 4G); CCS pag. 2 lo documenta; consistente con SLD Rev 0.
- DS Power & Control Cable Rev 0 = Rev B sin cambios (5 familias, IEC 60228/EN 50525, UL/CE/RoHS).
- SLD Rev 0: VERIFICADO VISUAL pag. 3 — nube de revision "P22-LCP-001 (METAL CLAD, NEMA4X/ IP66, FLOOR STANDING TYPE)" + SPD "Uc-415Vac / Imax-50kA" en alimentador 400A 4P MCCB. OBS-01 y NOTE-01 TM N19 incorporadas. (El CCS decia "stated in Rev B" pero la anotacion esta en nube Rev 0 — incorporada de facto.)
- Typical Installation Details Rev 0: NOTE-01 TM N19 incorporada — tabla pag. 10 metodo por tipo de carga (METHOD 1-3 bandejas, 4 skid/estructura, 5 bombas/motores, 6 paneles/JB, 7 instrumentos) + nota 6 IEC 60364-5-54.
Nota interna (no para transmittal): la cita de TM N19 a "ET 5.4.4" para SPD era mas amplia que el texto ET (5.4.4 no exige SPD); no re-citar ET como fuente vinculante del SPD.

### 13. I/O List Rev 2 — Code 3 (reversion contractual)
Cerrados: OBS-01 (analizadores 220VAC->24VDC, cruzado contra IL Rev E items 2/3/35), NOTE-01 (VFD freq/energy items 38/39/116/117), NOTE-02 (IN REMOTE dosing items 129/135 soft IO Ethernet/IP). OBS-02: condicion suspensiva caducada (Rev D no entregada, 4o ciclo) -> reversion a Code 3 per clausula explicita TM N19. QA menor: gaps numeracion (no hay 128 ni 134), fila Rev 2 ausente del historial de revisiones (solo 0 y 1), dosing RUNNING declarado DI pero ruteado Ethernet/IP.

### 14. IC Cable Schedule Rev 1 — Code 3
4 items TM N19 cerrados (VFD comms ahora Cu/PE/S/UTP/PUR 4P 0.38 Ethernet/IP items 13/66; dosing IN REMOTE items 77/80; LSH/LSL items 75/76; columna Full Tag No.). NUEVOS (verificados lineas 151-162):
- OBS MAJOR: numeros de item DUPLICADOS pag. 4 — "54" (VE09-006-COM y VE09-003-COM), "55" (VE09-006-PWR y VE09-003-PWR), "56" (PIT09-005-AI y VE09-004-COM).
- OBS MAJOR: descripciones copy-paste erroneas en filas PWR de valvulas — VE09-006-PWR y VE09-003-PWR (y otras: items 44/46/48/57/59/74/84) describen "RO 2ND STAGE CIP FEED MOTORIZED VALVE POWER" siendo valvulas distintas.
- OBS MINOR: Function "PIT" en LIT09-002 (item 60) y TIT09-006 (item 61).
- NOTE MINOR: construccion de cable RTD divergente HP (Cu/PE/S/UTP/PUR) vs CIP (Cu/PVC/OS/PVC); VT09-001 remark "2 Wire, 24VDC" vs I/O List "2 Wire, 4-20mA (Loop Power)".
+ umbrella Rev D ("Rev 1 cannot reach IFC status while Plant Control Philosophy Rev D is still under Code 3"). Re-emitir Rev 2.

### 15. Organization Chart Rev A — Code 1
Verificado visual (extraccion ilegible por rotacion): estructura completa con nombres — Sponsor Fadey, PM Eduardo, Director Shane, Project Engr Sadeep, Interface Mgr Stephanie, PM Fabricacion Adzlan; ramas Process/Detail Eng, E&C, Supply Chain, Fabrication (Samsul Annuar), QUALITY (Quality Mgr Magdier USA + QA/QC Mgr Adnin ASIA), Planner/Doc Control (Celestina/Allan/Tanya), EHS (Sivanes), Project Control (Elizaveta/Ai Nee). Canales de comunicacion Americas<->Asia declarados. Colores = region (no TBC). Hallazgos del agente (FAT/QA no identificados, ilegibilidad) DESCARTADOS tras verificacion visual. Correcto as-is.

### 16. Project Schedule Rev A — Code 2
Mismo Rev A adoptado como baseline de recovery con reservas (carta ADASA 09-Jun). Disposicion consistente con esa carta (no re-litigar): incorporar al documento en IFC Rev 0 (a) la base ASME del waiver 02-Jun (ruta sin estampa, ex-works Espana 23-Jun) y (b) la actividad de prueba hidrostatica de vessels en fabrica (1800 psi x 1.1) + hidrostatica de sistema previa a FAT (ET — Inspecciones, 8.1). Hitos ancla (23-Jun / Penang 02-Ago / EXW 15-Ago / fin 19-Nov) ya verificados el 09-Jun contra PDF nativo.

### 17. NDE Plan Rev A — Code 3
Cobertura soldadura piping/estructural OK (HP Super Duplex: 100% VT, 100% PT raiz+final, 10% RT butt, UT espesores, PMI >=10%; LP PVC y estructural 100% VT; ASME V Art.9/B31.3/AWS D1.1/DVS 2202-1; personal SNT-TC-1A/ISO 9712). PERO: OBS-01 CRITICAL silencio total sobre alcance vessel (sin hidrostatica fabrica, sin ASME X/waiver, sin dossier/testigo — el gap exacto de TM N19 2.10); OBS-02 MAJOR sin puntos W/H de ADASA (ET — "ADASA se reserva el derecho de testificar estas pruebas (Punto W)"); OBS-03 MINOR ediciones de normas en placeholder + titulo "general NDE plan"; NOTE: criterio de aceptacion UT/RT para Super Duplex sin citar. Re-emitir Rev B.

### 18. PMI Procedure Rev A — Code 2
LIBS SciAps Z-200/902C+, API 578/582, 5 certificados tecnicos. Gaps a incorporar en IFC Rev 0: mapear alcance al circuito HP Super Duplex Taltal >=10% con aceptacion UNS S32750 y punto W ADASA (ET — Inspecciones); declaracion de aplicabilidad (doc subcontratista XESSB generico refineria, PTS/HF acid no aplican); clausula de calificacion copy-paste del NDE Plan (corregir a calificacion operador PMI: OEM + mock-up).

### 19. Welding Procedure Rev A — Code 2
WPS/PQR ASME IX: FAC/WPS-06-20 GMAW S275JR estructural; FAC/WPS-09-24 GTAW SA-790 UNS S32750 (ER2594, impact test); 6 soldadores 6G Super Duplex. Gaps IFC Rev 0: declarar metodo de union LP/termoplastico (NDE Plan cita DVS 2202-1 => existen juntas termoplasticas no cubiertas); OBS rango de espesores: PQR cupon 2.77 mm califica hasta 5.54 mm (QW-451) vs WPS declara hasta 14.02 mm — aportar cupon que califique el rango o restringir WPS; NOTE: sin limites de heat input / numero de ferrita para 2507 (critico corrosion salmuera).

### 20. Visual Procedure Rev A — Code 2
VT directo 600 mm/30 grados, >=100 fc per ASME V Art. 9, aceptacion B31.3 341.3.2 + AWS D1.1. Gaps IFC Rev 0: calificacion del inspector VT no declarada (SNT-TC-1A/ISO 9712, consistente con NDE Plan); alcance dice "steel and thermoplastic welds" pero sin criterio DVS 2202-1; formularios QAM-F004/F005 y QAM-P008/P009 referenciados no adjuntos.

## Seccion 3 — Carry-forward (pendientes previos)

| Origen | Item | Estado al 10-Jun |
|--------|------|-------------------|
| TM N18 2.1 / TM N19 S3 | Plant Control Philosophy Rev D | **ABIERTO — 4o TM consecutivo.** Plazo de 14 dias (TM N19, 25-May) vencio el 08-Jun sin entrega. Consecuencia materializada en este TM: I/O List revierte a Code 3 per condicion TM N19; IC Cable Schedule y A&I List no pueden consolidar IFC; Schematic condicionado. Remedies C-4300 reservados siguen vigentes |
| TM N11 OBS-03 / TM N19 2.5 | Grounding Layout Rev F (schedule NCh Elect. 4/2003 Seccion 10.0) | ABIERTO — Rev F comprometida para Mie 17-Jun (aclaracion ADASA 03-Jun); ~86 dias. Hold Point SEC sigue gated |
| TM N4 NOTE-05 | HMI Screenshots | ABIERTO — ~126 dias, compromiso mas antiguo del proyecto |
| TM N19 2.10 | ITP Offsite Rev C + declaracion ASME X + procedimientos Hydrostatic, Preservation y FAT con fechas | ABIERTO — esta entrega trae NDE/PMI/Welding/Visual (4 de 7); faltan Hydrostatic, Preservation, FAT e ITP Rev C; el alcance vessel sigue sin reflejarse en NINGUN documento del set (condiciones del waiver 02-Jun) |
| TM N19 2.12/2.13 | Cartridge Filters Rev E / Rev D | ABIERTO — pendiente cierre NT-001 (tabla FAT/SAT + pendientes 15-Jun) |

Cerrados por E46/E47 (resumen): TM N14 NOTE-02 voltaje analizadores (~96 dias); TM N15 OBS-01/02 LCP datasheet; TM N17 IL OBS-01+3 NOTEs, DTL 2 NOTEs, PTx OBS+NOTE, A&I OBS-01/02/03+NOTE-01; TM N19 PCS OBS-01, SLD OBS-01+NOTE-01, TID NOTE-01, IO OBS-01+NOTE-01/02, ICCS 4 items.

Tracked for IFC Rev 0 que SIGUEN pendientes (ningun avance en E46/E47): PSV-09-002 relief sizing; P&ID CIP Tank dual-value; CIT-09-004 loop response note; AC Thermal margin statement (+13.3%); Motor Datasheet Pt-100; Cable Tray tabla S1-S7; PQP FAT Approval Certificate specimen. Nuevos a trackear: TIT-09-006 confirmacion span 0-600 C; consumo panel LCP en datasheet.

## Respuesta al correo Yamauchi 10-Jun (carril panel)

ADASA acepta la via de revision por correo. El paquete panel NO es aprobable as-is: la decision unica que bloquea fabricacion es material/IP del enclosure (Outline IP55 sheet steel pintado vs Datasheet+SLD+ET SS316L NEMA4X/IP66). Si BW Water confirma por escrito que el enclosure es el del datasheet (FS66S SS316L NEMA4X/IP66) y re-emite el Outline Rev B con el spec sheet alineado (+ peso real + reconciliacion cooling/IP), el release de fabricacion puede darse con el Rev B — sin esperar ciclo completo. El Schematic Rev A va Code 2 (no bloquea fabricacion del enclosure; condicionado a Rev D para el cableado). LCP Datasheet Code 2 (solo falta declarar consumo).

## Notas internas (no enviar)

- Correccion a agente B: la anotacion NEMA4X/IP66 del SLD SI esta (nube Rev 0, verificada visual) — su "provisional Code 2" se resuelve a Code 1.
- Correccion a agente C: el registro defectuoso del DTL es 30019 (CIT09-002, "0-20 uS/cm"), no 30021; 30021 (0-20 mS/cm) es numericamente correcto. OBS redactada en consecuencia.
- Correccion a agente D: Org Chart legible y completo en el PDF nativo — sus OBS-01/02 descartadas; Code 1.
- Hallazgos agente A verificados 1:1 contra extracciones (duplicados, swap winding/bearing en ambos trenes, PHIT, 90 vs 95 C).
