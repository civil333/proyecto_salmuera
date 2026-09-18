---
titulo: Marco de revisión del procedimiento FAT del módulo (interno, no enviar)
codigo_documento_revisado: P22-BA-09-000-017
fecha: 2026-09-18
estado: INTERNO
type: analisis
project: salmuera-taltal
nota: >
  Absorbe la pauta de 21 filas de crear_guia_n40.py (17-Sep-2026) y la ancla a lo
  verificado en la ET, el PIE Base, el ITP Rev 0, las BAE y la NT-002. Sirve para la
  Rev A (TM N40) y para revisar la Rev B cuando llegue. Las citas en inglés van
  listas para el transmittal y el PDF anotado.
---

# 1. Qué es exigible y de dónde sale

La Oferta Técnica Rev.1 de BW Water no ofrece un alcance de FAT propio (el único rastro es "factory Testing, 5 days" en su cronograma), de modo que el alcance exigible es íntegramente el de la ET y sus documentos derivados. Jerarquía declarada en la NT-002: ET, Oferta Rev.1, ITP, BAE.

| Fuente | Cita para el transmittal | Qué fija |
|---|---|---|
| ET P22-ET-09-000-001-0 | Section 8 - Inspections During Manufacturing | Aviso de un mes; toda deficiencia se documenta y corrige por cuenta del proveedor antes de liberar los equipos |
| ET | Section 8.1 - Minimum Scope of Factory Acceptance Tests (FAT) | Prerrequisito: hidrostáticas de baja y alta presión completadas y aprobadas (PIE Sección 5). Siete bullets: (1) aprobación del procedimiento **detallado**; (2) visual, completitud y dimensional contra Layout y P&ID aprobados, con tie-ins de Section 5.6 y puntos de izaje; (3) integridad del montaje mecánico; (4) funcionales en seco: giro libre y sentido de rotación de bombas, actuación de válvulas automáticas, finales de carrera de manuales críticas; (5) instrumentación y control: TAG, **loop checks** al PLC, energización del tablero, HMI según ISA 101, **simulación avanzada y dinámica** con señales forzadas o simulador sobre los rangos operativos y transitorios, **escenarios de fallo obligatorios** (los tres que nombra son ejemplos: pérdida de señal de transmisor de presión crítico, disparo de bomba bajo carga, actuación de válvula de seguridad), secuencias de arranque, parada normal y de emergencia y CIP, alarmas críticas, interlocks, comunicaciones externas; (6) revisión documental preliminar: O&M preliminar, certificados de super dúplex, registros de pruebas previas incluidas las hidrostáticas, dossier; (7) conformidad SEC como Hold Point previo al embarque. Registro detallado en **un protocolo específico**; **Acta de Aprobación FAT** emitida por ADASA (PIE 7.9); el FAT no exime ni reemplaza las Pruebas de Desempeño de Section 10 |
| ET | Section 7 - Engineering and Documentation to be Developed During the Contract | La obligación de referencia unívoca (documento, sección, valor), frecuencia y **registro específico** recae sobre el **PIE Detallado**, que cita a los procedimientos FAT aprobados como fuente del criterio; el PIE Base (página 4) rechaza las referencias genéricas ('Según ET', 'Según plano'). Sobre el procedimiento FAT la exigencia entra por la **delegación del ITP Rev 0**: fila 7.1 'Submit detailed FAT Proc.', 7.3 'Key Points according to [Approved FAT Procedure]', 7.4 'Ref. Sequence in Proc. FAT PROV-PROC-FAT-001', 7.5 'PROV-PROC-FAT-001 detailing simulation'. Si el procedimiento devuelve el criterio a 'approved drawings', ningún documento lo fija. Sin aprobación de toda la documentación no hay liberación para transporte |
| PIE Base P22-IT-09-000-001-0 | Section 4 - Definition of Intervention Points; Section 13 - Inspection and Test Matrix, block 7 | H: no se avanza sin presencia y aprobación escrita del inspector, con notificación previa; W: notificación, puede avanzar si el inspector no asiste; R: revisión de registro |
| ITP P22-BA-09-000-004 Rev 0 (Código 1, TM N26) | rows 5.1, 5.2, 6.2, 7.1 to 7.9, 8.1 to 8.4 | 5.1 LP 7,5 bar (W); 5.2 HP 135 bar (H); 6.2 tableros (W); 7.1 procedimiento detallado (H); 7.2 visual (H); 7.3 dimensional (H); 7.4 funcional en seco (W); 7.5 PLC/HMI con simulación de fallos (H); 7.6 dossier preliminar (R); 7.7 SEC (H); 7.8 UT (W); 7.9 Acta FAT (H); 8.3 dossier (H); 8.4 Release for Dispatch (H), distinto del Acta. Registros con placeholder que el procedimiento debe reemplazar: PROV-PROC-FAT-001, PROV-CHK-FATV-001, PROV-CHK-FATD-001, PROV-LIST-DOSS-PRE-001, PROV-PROC-UT-001, PROV-DWG-UTP-001 |
| BAE 12803 | Clause 31 | 40% del precio contra el Acta FAT: a) procedimiento detallado aprobado (Hold, PIE 7.1); b) registros detallados de cada prueba; c) protocolo final |
| BAE | Clause 37 (cuerpo) y 37.1 | El aviso de 30 días vive en el **cuerpo de la 37**, condicionado a que exista inspección de terceros (sin tercero son 10 días); la 37.1 solo regula el acceso del tercero inspector, sin plazo. La 37.2 d) exige constancia documentada del aviso y de la asistencia o ausencia en los Witness |
| BAE | Clauses 38 and 39 | Expedición solo con Acta FAT, inspección pre-embarque, dossier aceptado y Certificado de Liberación |
| NT P22-NT-09-000-002-0 | Section 3.1 - Designation of the Third-Party Inspector; Section 3.3 - Notification and Coordination Protocol; Section 5 - Reservations | Bureau Veritas designado (3.1); aviso 30 días y respuesta ADASA 3 días hábiles (3.3); Hold sin presencia no procede; ningún punto se renuncia por omisión (5). La figura contractual que firma es 'ADASA o su representante' (PIE Base Sección 4), no Bureau Veritas por nombre |

# 2. Matriz de cobertura y resultado sobre la Rev A

Resultado sobre `ENTREGAS_BWWATER/ENTREGA 95/md/P22-BA-09-000-017_A ... _extracted.md` (10 páginas, 8.182 caracteres). Páginas 1-based del PDF.

| # | Elemento exigible | Cita | Dónde debería estar | Rev A | Pág. | ID |
|---|---|---|---|---|---|---|
| 1 | Código y revisión propios, un solo número | ITP 7.1; precedente N38 | Portada | Doble número: P22-BA-09-000-017 en portada, PROV-PROC-FAT-001 en la hoja 2. **Ese número lo asigna el propio ITP Rev 0 aprobado**, así que no es error de BW Water: se pide alineación (código ADASA en cada página, número interno una vez), y el ITP deberá citar el código ADASA en su próxima revisión | 1-2 | OBS-01 |
| 2 | Procedimiento con formularios en blanco, no registro | ET 8.1; BAE 31 b); ITP 7.3 a 7.5 | Anexos | Sin ningún formulario; la Sección 8 nombra once registros, de los que **nueve** son formularios de BW Water (los otros dos son este procedimiento y el Acta que emite ADASA), y ninguno existe. Circularidad: el ITP delega puntos clave, secuencia y simulación al procedimiento, y el procedimiento los devuelve a 'approved drawings' | 10 | OBS-02 |
| 3 | Referencias por código y revisión | ITP 7.1 a 7.5 (delegación); precedentes N27 y N38 | Sección 3 | Genéricas ("Approved GA Drawings"); "Approved FAT Procedures" es autorreferencia; solo la ET y el PIE Base llevan código | 4 | OBS-01 |
| 4 | Criterios con valor, unidad y tolerancia | ET 8.1 ('detallado'); ITP 7.3 a 7.5 | Cada 5.x.2 | "As defined in approved dimensions", "according to approved datasheets", "full compliance": ninguno verificable | 5-9 | OBS-02 |
| 5 | Prerrequisito hidrostáticas LP/HP aprobadas | ET 8.1 párrafo inicial; ITP 5.1, 5.2 | Sección 4 | Ausente | 5 | OBS-04 |
| 6 | Visual y completitud contra P&ID y Layout por código y revisión | ET 8.1 (2); ITP 7.2 H | 5.1 | Lista de tipos de documento sin código; checklist PROV-CHK-FATV-001 no adjunto | 5-6 | OBS-05 |
| 7 | Dimensional con tolerancias, tie-ins (ET 5.6) e izaje | ET 8.1 (2); ITP 7.3 H | 5.2 | Puntos de inspección listados, sin tolerancias ni planos; izaje sí aparece; 'Nozzle orientations' y 'Structural interfaces' cubren los tie-ins de forma parcial, sin nombrarlos ni citar el Tie-In Point Layout P22-DWG-09-005-005 Rev 0 | 6 | OBS-05 |
| 8 | Integridad del montaje mecánico | ET 8.1 (3) | 5.1 | Cubierto de forma genérica ("Piping installed, Supports installed") | 5 | dentro de OBS-05 |
| 9 | Funcionales en seco: giro libre, rotación, válvulas, finales de carrera | ET 8.1 (4); ITP 7.4 W | 5.3 | "Operate equipment according to approved FAT sequence": la secuencia no existe; sin TAG, sin criterio de rotación ni de carrera | 6-7 | OBS-06 |
| 10 | TAG y loop checks al PLC | ET 8.1 (5); ITP 7.5 H | 5.4 | TAG presente en 5.1.1 ('Tags correctly attached') sin lista de instrumentos; loop checks ausentes | 7 | OBS-07 |
| 11 | Energización del tablero y PLC | ET 8.1 (5) | 5.4 | Cubierto por el FAT de tablero P22-PP-09-000-001 Rev C y su repetición comprometida en Penang (N38); el procedimiento del módulo debe **referenciarlo**, no repetirlo | 7 | OBS-07 (cláusula) |
| 12 | HMI según ISA 101 | ET 8.1 (5) | 5.4 | "Operator screens" sin criterio | 7 | OBS-07 |
| 13 | Simulación dinámica con señales forzadas o simulador | ET 8.1 (5); ITP 7.5 "detailing simulation" | 5.4 | "Perform simulation using approved PLC and HMI software": sin método, sin escenarios, sin rangos | 7 | OBS-07 |
| 14 | Escenarios de fallo simulados (obligatorios, ejemplos abiertos) | ET 8.1 (5) | 5.4 | No definidos: 'Alarm functions, Interlocks, Emergency functions' son encabezados, sin escenario de señal forzada | 7 | OBS-07 |
| 15 | Comunicaciones externas (cuatro señales de contacto al PLC de planta) | ET 8.1 (5) 'si aplica'; aplica porque las cuatro señales están en la I/O List Rev 6 (N19/N24) | 5.4 | Ausentes | 7 | OBS-07 |
| 16 | Documentos de control gobernantes por código y revisión | ITP 7.5 ('Control Philosophy [Doc. Code]') | 5.4 | Ninguno (Control Philosophy, Alarm and Interlock List, Control and Sequence Chart, I/O List, HMI) | 7 | OBS-07 |
| 17 | Revisión documental preliminar con lista | ET 8.1 (6); ITP 7.6 R | 5.5 | Lista genérica; sin PROV-LIST-DOSS-PRE-001 ni certificados de super dúplex por nombre | 7-8 | OBS-05 (cláusula) |
| 18 | SEC: componentes y certificados o declaraciones | ET 8.1 (7) Hold; ITP 7.7 H | 5.6 | Ítems de inspección genéricos; "Full compliance with applicable SEC regulations" sin lista de certificados | 8 | OBS-08 |
| 19 | UT: procedimiento y plan de puntos por código | ITP 7.8 W | 5.7 | "UT Measurement Plan" nombrado y no adjunto; sin cita del procedimiento P22-BA-09-000-016 (Rev C, Código 2 en N38, donde vive el criterio de espesor). El plano de puntos ya está pendiente desde la Sección 3 del N38: no se levanta como hallazgo nuevo, se pide citarlo | 8-9 | OBS-09 (MENOR) |
| 20 | Acta FAT (ITP 7.9) separada del Release for Dispatch (ITP 8.4) | ET 8.1 párrafo final; ITP 7.9, 8.3, 8.4; BAE 31, 38, 39; PIE Base Sección 4 (aprobación escrita en Hold); BAE 37.2 d) (constancia en Witness) | 5.8 y 7 | 5.8 "final FAT acceptance and release for shipment" los funde. Que el Acta la firme solo ADASA es correcto (es documento de ADASA); lo exigible es la casilla de aprobación escrita de 'ADASA o su representante' en cada Hold y la constancia de aviso y asistencia en cada Witness | 9 | OBS-10 |
| 21 | Responsabilidades y asistentes | **Sección 1 del propio documento** ('define ... responsibilities'); BAE 37.1 y NT-002 solo para el acceso del tercero | Sección nueva | Prometidas en la Sección 1 y no definidas; hay 'FAT Attendance Sheet' en la Sección 8 y 'Client Representative (ADASA)' en la 7 | — | OBS-03 |
| 22 | Marcado H/W por actividad y aviso previo | Ninguna fuente exige que el procedimiento los repita (viven en el ITP y en BAE 37); va como **'ADASA requests'** | Cada 5.x | Ausente | — | OBS-03 (pedido) |
| 23 | Secuencia y duración de las actividades | Secuencia: exigible por ITP 7.4 y por 5.3.1 del propio documento (OBS-06). Duración: sin fuente, solo pedido | Sección nueva | Ausente | — | OBS-06 / pedido |
| 24 | Instrumentos de prueba con modelo, serie y calibración | Solo 5.2.1 del propio procedimiento ("calibrated equipment"): sin cláusula contractual (la guía del 17-Sep lo tenía bien); precedente N37 anclado en el propio documento. Para el UT lo gobierna P22-BA-09-000-016 | Sección 4 o anexo | "Calibration Certificates" como documento disponible, sin lista | 5 | **NOTE-01** |
| 25 | Gestión de no conformidades y punch list | ET Section 8 | Sección 6 | Cubierto en dos líneas; formulario no adjunto | 9 | dentro de OBS-02 |
| 26 | FAT en seco declarado | ET 8.1 (4); reference_fat_seco_vs_sat_taltal | 5.3 | "without process fluid": correcto | 6 | NOTE-02 |
| 27 | Forma | — | Índice, 5.3.1 | "REFERENT"; "5.3.1Verification" | 3, 6 | OBS-01 |

# 3. Lo que enseñan los ejemplos

| Elemento | Emerson 3297494-INST-PR-002 Rev 0 (2022, skids PDA) | CDM Smith 5000671-FDE-IN-PRO-0001 Rev B (2026, lógica PDA Fase II) | Registro FAT-300835 (2019, PLC planta modular Taltal) | Clasificación |
|---|---|---|---|---|
| Tabla paso / acción y resultado esperado / PASS-FAIL-N/A / desviación | Sí, por prueba (PAS-HTS-101 a 103) | Protocolo en anexo | Por canal: TAG, punto, desde/hacia, lectura PLC, activar, observaciones | **Exigible** vía "procedimiento detallado" (ET 8.1), registro específico (ET 7) y BAE 31 b) |
| Requisitos para comenzar: equipamiento y documentación con código y revisión | Sección 2.5, tabla de documentos | Sección 1.3 | Sección 1.0 a 4.0 | **Exigible** (ET Section 7 referencias unívocas; ET 8.1 prerrequisito hidrostático) |
| Equipos de prueba con serie y fecha de calibración en el propio formulario | Paso 1.2 de cada prueba | — | Sección 6.0 (Fluke 336, generador 4-20 mA, certificados) | **Exigible** como registro; el procedimiento mismo lo pide en 5.2.1 |
| Criterios numéricos (continuidad < 1 ohm, etc.) | Paso 2.10 | Valores de simulación por activo | Tensión por módulo | **Exigible** (ET 7: valor, unidad, tolerancia) |
| Personal involucrado y personas nominadas con firma | Secciones 2.3 y 6 | — | Sección 7.0 | **Exigible** como matriz de responsabilidades (BAE 37.1, NT-002); las firmas individuales son deseables |
| Manejo de desviaciones: índice, hoja, cambios de alcance | Secciones 2.6.1 a 2.6.4 y apéndices 2-3 | Objetivo 2 | — | Deseable; el mínimo exigible es la punch list y su cierre (ET 8; ITP 7.9) |
| Definiciones, clasificación de alarmas, estados operativos, modos | — | Secciones 2 y 3, tablas 1-4 | — | Deseable en el procedimiento; **exigible** que la simulación pruebe contra la Alarm and Interlock List y la Control Philosophy aprobadas |
| Hoja de firmas de cierre por prueba (revisado, aprobado, fecha) | Sección 3 y 5 | — | Sección 7.0 | **Exigible** (protocolo específico y Acta, ET 8.1) |
| Orden de ejecución y tiempos | Secuencia 1.1 a 1.3 | — | — | Deseable; lo exigible es el aviso de H/W (NT-002) |

Los dos ejemplos de ADASA (Emerson y CDM Smith) son el estándar interno de la empresa: un procedimiento FAT trae la instrucción paso a paso y su formulario de registro en el mismo documento. El registro de 2019 muestra la forma del loop check que ADASA ya usó en Taltal. Ninguno de los tres se cita a BW Water; sirven para calibrar qué significa "detallado".

# 4. Lo que NO se observa

- Que el FAT sea en seco: la prueba con agua y la bomba bajo carga van a comisionamiento y Pruebas de Desempeño en Taltal (ET Sections 9 y 10.2; ITP 10 y 11). El disparo de bomba bajo carga se **simula**.
- Decodificación HART central en el PLC (over-reach del N21, retirado en N24).
- Cableado directo para I/O de campo soft: el esquema Ethernet/IP está aceptado desde el N20; solo las cuatro señales de coordinación con el PLC de planta van por contacto de relé.
- Una presión de prueba única para el super dúplex: va por línea, 1,5 × diseño según la Line List.
- Pruebas Fedco en Estados Unidos: ADASA no las atestigua; los registros van al dossier.
- Los tres escenarios de fallo de la ET como lista cerrada: son ejemplos.
- El uso del FAT como base del SIT de reconexión en sitio: pedido de ADASA sin cita contractual; va como "ADASA requests", nunca como incumplimiento.
- Rigor BIM, formatos de los ejemplos, nombres internos (Van Doorn, PRG-xx, BV-xx, costo de Bureau Veritas).

# 5. Regla de código y decisión sobre la Rev A

| Situación | Código |
|---|---|
| No es un procedimiento detallado ejecutable: criterios sin valor, secuencia ausente, registros sin definir (N23 sobre procedimientos QA; N37 "this revision is not a procedure") | **3**, re-emitir |
| Contenido completo, correcciones documentales incorporables al emitir (FAT de tablero Rev A, N27) | 2 |
| Nada cambia | 1 |

**Rev A: Código 3, re-emitir como Rev B.** Fundamento en tres líneas: no es el procedimiento detallado que exigen ET Section 8.1, BAE Clause 31 a) e ITP row 7.1; omite los loop checks y los escenarios de fallo que ET Section 8.1 hace obligatorios; y es circular con el ITP (las filas 7.3, 7.4 y 7.5 delegan al procedimiento los puntos clave, la secuencia y el detalle de la simulación, y el procedimiento los devuelve a 'approved drawings'). El prerrequisito de hidrostáticas queda como OBS-02, no como driver: la ET impone la condición al acto del FAT y su inserción en el texto es una línea. Consecuencia declarada: el Hold Point 7.1 sigue abierto, el FAT no abre formalmente y Bureau Veritas recibe el procedimiento aprobado, no este borrador. Plazo de la Rev B fijado en el correo: viernes 25-Sep-2026.

# 6. Correcciones del verificador adversarial (18-Sep-2026)

Diecisiete refutaciones, ninguna toca el código. Las que cambiaron el texto emitido: (1) la obligación de referencia unívoca de ET Section 7 recae en el PIE Detallado, no en el procedimiento, y la vía correcta es la delegación del ITP Rev 0 (filas 7.1, 7.3, 7.4, 7.5), que pasó a ser la tercera razón del encabezado en lugar del prerrequisito hidrostático; (2) son nueve formularios y no once; (3) PROV-PROC-FAT-001 lo asigna el ITP aprobado y se pide alineación, no corrección; (4) el aviso de 30 días vive en el cuerpo de la Cláusula 37, condicionado a inspección de terceros; (5) los instrumentos de prueba no tienen cláusula y bajan a NOTE-02 anclada en 5.2.1 del propio documento; (6) OBS-08 se ancla en la promesa de la Sección 1 del documento y el marcado H/W y el aviso van como pedido; (7) OBS-09 deja de objetar la firma única del Acta (es documento de ADASA) y pide la aprobación escrita de 'ADASA o su representante' en cada Hold y la constancia de aviso y asistencia en cada Witness (BAE 37.2 d); (8) OBS-07 se reduce a citar el procedimiento -016 y el plano de puntos, que ya estaba pendiente desde el N38; (9) la energización del tablero está cubierta por el FAT de tablero Rev C y su repetición en Penang: se referencia, no se declara ausente; (10) las comunicaciones externas se justifican ('si aplica') con las cuatro señales de la I/O List Rev 6; (11) TAG, tie-ins, responsabilidades y escenarios de fallo se reescribieron de 'ausente' a 'parcial' o 'no definido' donde el texto trae encabezados. Numeración final: OBS-01 a OBS-10, NOTE-01 y NOTE-02.

# 7. Ajuste de cajas y renumeración (18-Sep-2026, pedido del usuario)

Los cuadros del PDF se acortaron al patrón "ID: qué está mal. Correct: qué hacer", se ajustaron al alto real del texto y se llevaron al espacio libre de la página (junto a las listas de viñetas), con el helper `COMENTARIOS/_ajustar_cajas.py`. La causa del espacio vacío es `_calc_height` de doc-annotator, que asume 45 caracteres por línea y cuenta las líneas de 46 a 50 como dos. **Los IDs se renumeraron por orden de aparición** (página y posición del ancla), de modo que la matriz de la sección 2 ya lleva los IDs definitivos; en la sección 6 los IDs citados son los anteriores a la renumeración: OBS-10 → OBS-01 (dos números), OBS-01 → OBS-02 (no detallado), OBS-08 → OBS-03 (responsabilidades), OBS-02 → OBS-04 (hidrostáticas), NOTE-02 → NOTE-01 (instrumentos), OBS-04 → OBS-06 (funcional en seco), NOTE-01 → NOTE-02 (alcance en seco), OBS-03 → OBS-07 (control), OBS-06 → OBS-08 (SEC), OBS-07 → OBS-09 (UT), OBS-09 → OBS-10 (Acta). OBS-05 no cambia. En el Schematic, NOTE-01 pasa a ser los TAG como anotaciones del PDF y NOTE-02 el código equivocado en la hoja de comentarios.
