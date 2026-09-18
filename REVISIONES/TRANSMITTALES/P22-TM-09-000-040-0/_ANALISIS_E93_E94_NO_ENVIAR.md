---
titulo: Análisis interno de las ENTREGAS 93 y 94 (no enviar)
fecha: 2026-09-18
estado: INTERNO
type: analisis
project: salmuera-taltal
nota: >
  Verificación de las condiciones previas sobre los trece documentos de los submittals
  25007-0093 (recibido el 14-Sep-2026) y 25007-0094 (17-Sep-2026). Regla aplicada:
  el universo es el conjunto de IDs del transmittal que dispuso el código anterior; el
  cierre se prueba sobre el documento (texto extraído o render), no sobre la hoja de
  comentarios; lo que ya estaba en la revisión aprobada no se levanta. Decisión del
  usuario para el TM N40: Rev 0 siempre Código 1 más NOTE por lo no levantado; el
  Schematic Rev C (IFA) Código 2 reiterado.
---

# 1. Resultado

| Doc | Título | Rev / For | Anterior | Condición previa | Verificación | Código N40 |
|---|---|---|---|---|---|---|
| P22-ET-09-009-009 | Datasheet of CIP Tank | 0 IFC | B, N3, C1 | Cruzada del N34 (GA CIP Tank Rev B): MH 533 mm, N42 Spare, N97 Temperature Sensor; declarar qué documento gobierna | Nozzle schedule del Rev 0 trae MH Manhole 533 mm top, N42 Spare DN25 side, N97 DN40 side (Sensor); la hoja de comentarios declara "BW has revised to align with the GA of CIP Tank". Cerrado sobre el documento y declarado | **1** |
| P22-DWG-09-008-001 | Instrument Location Layout | 0 IFC | D, N37, C2 (4º ciclo) | OBS-01 bloque de revisiones sin descripción y fila Rev C reescrita; OBS-02 Equipment Layout no declarado en notas | Render del cajetín (hoja 1): filas B, C y D leen "REVISED AS PER CONSOLIDATED COMMENT SHEET", Rev C vuelve a APR.17.26, Rev 0 "ISSUED FOR CONTRUCTION" SEP.10.26; la hoja de comentarios queda encuadernada como hoja 4 del plano. OBS-01 cerrado con la convención que BW Water propuso. Render del bloque de notas: "EQUIPMENT LAYOUT REV D - P22-DWG-09-005-003", más P&ID Rev 0 e Instrument List Rev F. OBS-02 cerrado. **Residual de forma:** la celda DRAWING STATUS sigue en "ISSUED FOR APPROVAL" en las dos hojas mientras la fila Rev 0 dice construcción, y "CONTRUCTION" va sin la S | **1 + NOTE** |
| P22-CD-09-008-002 | PLC/LCP Schematic Diagram | **C IFA** | B, N37, C2 (2º ciclo) | OBS-01 CIP Heater Running (ítem 109 de la I/O List Rev 6) sin terminal; OBS-02 BOM hoja 28 con 2711P-T10C21D8S; NOTE-01 cita "I/O List RevB" | Render hoja 37 (índice 37, 0-based): entrada 7 del módulo -A3, bornes DITB2 15/16, tag XB002 "CIP Heater Running". OBS-01 cerrado. Render hoja 28: fila 11 HMI1 Touch Screen 2711P-T10C21D8S. **OBS-02 no cerrado** y la respuesta propone revisar el datasheet PLC/HMI aprobado hacia el -D8S ("is fully sufficient"), con el código equivocado (llama "P22-ET-09-008-001 RevC PLC/LCP Panel Outline Drawing" al Outline, que es P22-CD-09-008-001). NOTE-01: BW Water reconoce el error de cita ("typo"); la hoja de comentarios de la Rev C ya no repite la cita errada. Diff B a C sobre el texto: además del borne del calefactor no hay cambios técnicos. **Hallazgo tardío (anotaciones del PDF fuente):** los TAG XA007, XA008 y XB002 de las entradas 5 a 7 de la hoja 37 y el recuadro rojo son anotaciones FreeText y Polygon del PDF, no contenido del plano: no viajan con el nativo ni con una impresión sin comentarios → NOTE-01 (la cita errada de la hoja de comentarios pasa a NOTE-02) | **2 reiterado** (tercer ciclo) |
| P22-LI-09-009-001 | Utility Consumption List | 0 IFC | C, N22, C1 | Ninguna | Diff Rev C a Rev 0: solo la fila de revisión. Contenido igual | **1** |
| P22-LI-09-009-002 | Chemical Consumption List | 0 IFC | A, N3, C1 | Ninguna | Antiscalant 0,5 ppm, 0,02 kg/h, 0,59 kg/día; ácido cítrico 20.000 ppm, 204 kg/ciclo; NaOH 1.000 ppm, 10,2 kg/ciclo: iguales a la Rev A | **1** |
| P22-LI-09-009-003 | Line List | **2** IFC | 1, N38, C1 | Dos medidas invertidas: CP-SSD-DN80-09-049 (1ª etapa, 54 m³/h) y CP-SSD-DN65-09-048 (2ª etapa, 36 m³/h) | Rev 2: 09-049 DN80 54 m³/h y 09-048 DN65 36 m³/h; historial "Corrected sizes of Line 09-049 and 09-048". Cumplida. DA-PVC-DN65-09-016 sigue en 1/2/3 bar (el 75 bar del N27 no vuelve) | **1** |
| P22-ET-09-009-001 | Datasheet UHPRO System | 0 IFC | B, N2, C1 | Ninguna | Etapa 1: LG SW 400 SR (1.200 psi) en BPV-8-1200-SP-7 x6; etapa 2: LG SW 400R G2 UHP (1.800 psi) en BPV-8-1800-SP-7 x4; 7 elementos por vessel. Igual a la Rev B (verificado por posición en el PDF de la Rev B; el resumen antiguo en md tenía las etapas invertidas y no el documento). Coherente con el ensayo hidrostático del N27 (6 a 91 bar, 4 a 136,5 bar) | **1** |
| P22-ET-09-009-003 | Datasheet CIP / Flushing Pump | 0 IFC | B, N2, C2 | OBS-02 (N2): "different motor specs, verify compatibility" | Rev 0: motor Innomotics IEC 160MB, 11 kW, 2 polos, 2.940-2.950 rpm, arranque VFD externo (la Rev B ya decía VFD), P1 10,11 kW a 48,1 Hz, P2 8,99 kW, PTC. Un solo juego de datos de motor, consistente con la curva. Cerrado | **1** |
| P22-ET-09-009-004 | Datasheet Antiscalant Dosing Pump | 0 IFC | B, N3, C1 | Ninguna | ProMinent GMXa 1602, 0,02 L/h operación, 2,3 L/h máx, 16 barg, PP/PTFE/cerámica, 230 V, 24 W: iguales a la Rev B | **1** |
| P22-ET-09-009-005 | Datasheet RO Cartridge Filter | 0 IFC | E, N22, C1 | Ninguna propia; certificado FRP al dossier | Diff Rev E a Rev 0: agrega la fila "Gasket Material: EPDM" y reexpresa la tasa de filtración (11,1 m³/h/m² sobre 0,20 m² por cartucho = 2,22 m³/h por cartucho de 40", equivalente al 0,557 m³/h por 10" de la Rev E). Sin cambio de fondo | **1** |
| P22-ET-09-009-006 | Datasheet CIP Cartridge Filter | 0 IFC | E, N24, C1 | NOTE-01 (N24): confirmar junta de la tapa en EPDM | Modelo 31SBFX4-040A-**E**; la guía de pedido del mismo datasheet asigna "E - EPDM" al sufijo de la junta de la tapa; fila 34 Gasket Material EPDM. Cerrado sobre el documento | **1** |
| P22-ET-09-009-010 | Datasheet Antiscalant Dosing Tank | 0 IFC | B, N4, C2 | OBS-11: capacidad del P&ID (0,25 m³) vs datasheet (0,34 / 0,27); OBS-14: validación de 0,5 ppm vía CT-001, "tank approval subject to satisfactory response" | P&ID Rev 0 (E89, hoja 12) rotula TK-09-002 "VOL: 0.34 m3 (Effective: 0.27)": OBS-11 cerrada en el P&ID. CT-001 Rev .1 acepta el 0,5 ppm en principio con cuatro observaciones que viven en esa consulta, no en el datasheet. Capacidad sin cambio | **1** |
| P22-ET-09-009-011 | Datasheet CIP Tank Heater | 0 IFC | B, N3, C1 | Ninguna | Quantic Logic VEMA, 20 kW, 380 V trifásico, SS316 en partes húmedas, PT100: iguales a la Rev B | **1** |

Tally E93 + E94: **12 Código 1 + 1 Código 2**. Ningún CC_ADASA para los Código 1; uno para el Schematic Rev C.

# 2. Lo que va al texto del transmittal y no al PDF

- **Instrument Location Layout Rev 0, NOTE en el Status:** DRAWING STATUS "ISSUED FOR APPROVAL" contra la fila Rev 0 "ISSUED FOR CONTRUCTION". Housekeeping (`feedback_code1_housekeeping_rev0`): no degrada; se escribe literal para que quede en el registro y se dice que es Código 1 y no 3 por eso. Sin CC_ADASA.
- **Schematic Rev C, Status:** reconoce el cierre del borne del calefactor y del error de cita, reafirma el terminal 2711P-T10C22D9P del datasheet PLC/HMI P22-ET-09-008-001 Rev 0 (dos puertos Ethernet RJ45 y 1 GB), rechaza revisar ese datasheet al -D8S, constancia del tercer ciclo (N20, N37, N40). `Action to issue at IFC Rev 0 — no new revision required:` sustituir el ítem 11 de la BOM por el -D9P (OBS-01), dibujar los tres TAG en el plano (NOTE-01) y citar el Outline por su código en la hoja de comentarios (NOTE-02).
- **CIP Tank datasheet, Status:** se acepta que el GA P22-DWG-09-005-014 gobierna y que el datasheet se alineó a él; cierra la dependencia del N34 en lo que toca al datasheet.
- **Antiscalant Dosing Tank, Status:** el residual de la consulta CT-001 sigue en la cadena de la consulta.
- **Correo de cobertura, una línea:** décimo y undécimo lote consecutivo con devolución pedida a tres días corridos; el de la E93 se pidió para el 11-Sep y el archivo llegó el 14.

# 3. Registro de ADASA (acción propia, no observación)

El Master Register lleva tres códigos corridos que hay que realinear en `update_register_n40.py`: fila 13 "DS CIP Tank" dice P22-ET-09-009-010 y es **-009**; fila 14 "DS Antiscalant Dosing Tank" dice -011 y es **-010**; fila 15 "DS CIP Tank Heater" dice -014 y es **-011**. La fila 39 (Utility Consumption) arrastra "A/C thermal calc Rev C still pending", ya cerrado. La fila 85 "Procedimiento FAT" (NOT DELIVERED) pasa a ser la del P22-BA-09-000-017 Rev A.

# 4. Evidencia

Renders en el scratchpad de la sesión: `instrloc_p1_titleblock.png`, `instrloc_p1_right_top.png`, `schem_p37.png`, `schem_p28.png`. Extracciones en `ENTREGAS_BWWATER/ENTREGA 93/md/` y `ENTREGA 94/md/`; revisiones aprobadas previas en `ENTREGA 6/md`, `ENTREGA 7/md`, `ENTREGA 8/md`, `ENTREGA 10/md`, `ENTREGA 49/md`, `ENTREGA 54/md` (Rev E del filtro CIP extraída hoy), `ENTREGA 86/md` (Schematic Rev B). P&ID Rev 0 leído por texto directo del PDF de la E89 (sin extracción a md).
