# COMPILADO INTERNO — TM N7 (NO ENVIAR A BW WATER)
## Análisis con asesoría Van Doorn | Uso exclusivo ADASA

**Fecha:** 08-Mar-2026
**Código:** P22-TM-09-000-007-0
**Submittal:** 25007-0014 (06-Mar-2026)
**Preparado por:** Luis Rivera | **Asesor:** Van Doorn

---

## 1. Información de la Entrega

| Código | Título | Tipo | Rev | Estado anterior |
|--------|--------|------|-----|----------------|
| P22-CD-09-005-002 | A/C Thermal Calculation | Cálculo | B | Pendiente 51+ días (TM N2/N4) |
| P22-DWG-09-005-004 | Piping Layout | Plano | A | Nuevo |
| P22-DWG-09-005-005 | Tie-In Point Layout | Plano | A | Nuevo |
| P22-BT-09-009-001 | Control Philosophy | Desconocido ("BT") | A | Nuevo |

**Nota:** El Submittal Form 25007-0014 identifica P22-BT-09-009-001 como "Plant Control Philosophy."

---

## 2. Análisis Técnico por Documento

### 2.1 P22-CD-09-005-002 — A/C Thermal Calculation Rev B

**Van Doorn:** "El cálculo cumple parcialmente lo solicitado. El VFD está incluido correctamente. Sin embargo, el cálculo sigue siendo minimalista: sólo considera el motor HPP y el VFD, ignorando la carga térmica del panel de control, los instrumentos, la iluminación y cualquier otro equipo eléctrico dentro del contenedor. BW Water pregunta razonablemente cuál era la base de los 11-15 kW de ADASA — si no tenemos respaldo, admitir que fue una estimación conservadora y centrar la observación en la falta de documentación de cargas adicionales.

El problema más serio: el cálculo dice 'we recommend using a 2.5 HP unit' (singular). El Piping Layout muestra dos unidades externas. Pero la relación entre ambos no está explicitada en ningún documento: ¿es cada unidad de 2.5 HP para el 100% de la carga? ¿o son dos unidades más pequeñas en paralelo? Para un n+1 que funcione, cada unidad SOLA debe cubrir el 100% de la carga. El cálculo debe confirmarlo.

Posición: 3 — To be Revised. No se puede cerrar este ítem con el documento actual."

**Análisis adicional ADASA:**
- VFD ya incluido (1.70 kW de 5.96 kW total).
- Margen de 15%: de 1.70 TR a 1.955 TR → unidad 2.01 TR. Margen neto sobre carga no calculada: ~0.3 TR (1 kW). Insuficiente si hay equipos adicionales relevantes.
- Piping Layout confirma 2 unidades externas → n+1 físicamente presente pero no documentado en el cálculo.
- ET §5.1.11 requiere A/C configuración n+1. Este ítem venía cerrado en Utility List Rev B. El pendiente era el cálculo de respaldo. Rev B no cierra completamente.

**Veredicto:** 3 — To be Revised

**Acciones requeridas BW Water:**
1. Incluir TODAS las cargas eléctricas dentro del contenedor: panel de control/PLC, instrumentos, analizadores, iluminación, cualquier otra fuente de calor.
2. Explicitar configuración n+1: CADA unidad de 2.5 HP debe ser capaz de soportar la carga total sola (100% de la carga).

---

### 2.2 P22-DWG-09-005-004 — Piping Layout Rev A

**Van Doorn:** "Inicialmente esto parecía un Piping Layout aceptable, pero hay que revisar con cuidado contra los requisitos de TM N5 OBS-01. El problema es serio: TM N5 exigió que TODO el equipamiento CIP y dosificación antiscalant quedara en UN SOLO footprint externo de máximo 3.5 metros, alineado a un lado específico del módulo.

El Piping Layout muestra el CIP (tank, pump, heater, cartridge filter) en la Section 2-2 — un extremo del módulo. Y el antiscalant dosing (TK-09-002, BDS-09-001/002) aparece en la Section 3-3 — el extremo OPUESTO, donde además están el Local Control Panel y las unidades de A/C. La distancia entre esos dos sectores es prácticamente la longitud completa del módulo (11,150 mm / 36'-7"). Eso viola flagrantemente el límite de 3.5 m del footprint.

Esto no es un tema menor de layout — es un incumplimiento directo del requisito que ADASA especificó explícitamente en TM N5. El veredicto debe ser 3 — To be Revised.

Además, sigue pendiente el Equipment Layout Rev B, que es el documento correcto para mostrar el footprint dimensionado del área CIP externa. Este Piping Layout no lo reemplaza."

**Análisis técnico — Comparación con TM N5 OBS-01:**

| Requisito TM N5 OBS-01 | Lo que muestra el Piping Layout Rev A | Cumple |
|------------------------|---------------------------------------|--------|
| Footprint único ≤ ancho módulo × 3.5 m | CIP en Section 2-2, antiscalant en Section 3-3 (extremos opuestos, ~11 m de separación) | **NO** |
| CIP Tank en footprint externo | Section 2-2 (TK-09-001) | Parcial |
| CIP Pump en footprint externo | Section 2-2 (BH-09-002) | Parcial |
| CIP Cartridge Filter en footprint externo | Section 2-2 (FIL-09-002) | Parcial |
| Antiscalant injection unit en mismo footprint | Section 3-3 (TK-09-002, BDS-09-001/002) — extremo opuesto | **NO** |
| Alineación al lado especificado por ADASA | No verificable desde extracción de texto | Incierto |
| Equipos con dimensiones métricas del footprint | No se muestran dimensiones del footprint CIP externo como unidad | Incompleto |

**Positivos del Piping Layout (sin perjuicio del veredicto):**
- Dos unidades A/C externas visibles → confirma n+1 físicamente.
- Líneas DA-SSD para HP → coherente con ET §5.2 (ANSI 900# en acero duplex).

**Veredicto:** 3 — To be Revised

**Acción requerida:** Rev B debe consolidar CIP Tank, CIP Pump, CIP Cartridge Filter, Antiscalant Dosing Tank y Antiscalant Dosing Pump Skid en un único sector externo contiguo, dentro de footprint ≤ ancho contenedor × 3.5 m, alineado al lado del módulo especificado en el markup de ADASA (TM N5 Attachment P).

---

### 2.3 P22-DWG-09-005-005 — Tie-In Point Rev A

**Van Doorn:** "Documento útil para la coordinación con la planta SWRO principal. El esquema es correcto arquitecturalmente: todos los tie-ins son a baja presión (ANSI 150#), lo que es coherente con que la presión de proceso se genera dentro del módulo. Sin embargo, hay tres problemas menores:

1. El tie-in N°1 (antiscalante DN15) está incompleto — ni tag, ni estándar de flange.
2. Los identificadores P8-001, P9-001 etc. no están cruzados con el P&ID ADASA. Son etiquetas de línea BW Water internas.
3. No se especifica la presión de diseño en el battery limit de alimentación de brine (TP-DA P8-001, DN100). Si la salmuera SWRO llega a presión superior a 19.6 bar (ANSI 150# limit), hay un problema de rating. Necesitamos confirmar esta presión.

No rechazaría el documento, pero necesita las correcciones menores."

**Análisis adicional ADASA (corrección post-compilado):**

El Tie-In Point Rev A fue elaborado sobre el Piping Layout Rev A, que incumple TM N5 OBS-01. Los tie-in points N°1 (DN15) y N°2 (TP-AS DN25) corresponden al antiscalant dosing system ubicado en Section 3-3 del Piping Layout. Una vez que el Piping Layout Rev B consolide CIP + antiscalant en un footprint único, esos tie-ins cambiarán de ubicación. El Tie-In Point Rev B debe ser redibujado sobre el Piping Layout Rev B corregido.

Adicionalmente, la tabla de seis tie-ins no incluye conexión de make-up water para el CIP externo (línea CP-PVC-DN80-09-019 visible en el Piping Layout). BW Water debe confirmar si el make-up CIP requiere tie-in externo.

**Veredicto corregido:** 3 — To be Revised (antes: 2 — Approved as Noted)

---

### 2.4 P22-BT-09-009-001 — Control Philosophy Rev A

**Van Doorn:** "Este documento tiene problemas serios. El más crítico: dice UPS de 30 minutos. El ET dice 8 horas. Esto no es ambigüedad — es un incumplimiento contractual directo, 16 veces menor que lo requerido. Una pérdida de suministro de red en un sitio remoto como Taltal puede durar muchas horas. Con 30 minutos, el sistema de control se cae y la planta queda inoperativa.

El segundo problema: Modbus TCP no aparece en ninguna parte de las 48 páginas. Este documento se llama 'Control Philosophy' pero no aborda la interfaz de comunicación con la planta SWRO/SCADA principal. El Memory Map de Modbus TCP lleva 65+ días pendiente desde TM N2. El Control Philosophy debería al menos describir las variables a exportar y confirmar el protocolo.

El tercer problema: los tags VE-07-014 vs VE-09-014 y VE-07-016 vs VE-09-016. Un '07' vs '09' en el área code es una inconsistencia que afecta la coordinación SCADA y la Valve List. Si estos son el mismo equipo, el tag debe ser único y consistente.

El código 'BT' es otro problema — menor pero real. No existe en el sistema de codificación. Hay que aclararlo.

Los documentos companion (Operating Sequence Charts, Alarm Setpoint List) son necesarios para completar la revisión. Con solo el Control Philosophy no se puede verificar la lógica de control completa.

Posición: 3 — To be Revised. Los temas de UPS y Modbus TCP son los más urgentes."

**Análisis adicional ADASA:**
- UPS 30 min vs ET 8 horas: **INCUMPLIMIENTO CONTRACTUAL DIRECTO** (ET L1088-1089).
- Modbus TCP: no mencionado en 48 páginas. Ítem pendiente 65+ días. El Control Philosophy debería al menos referenciar la arquitectura de comunicación con el SCADA de la planta.
- Tags VE-07-014/VE-09-014: La tabla de instrumentos (Section 3.1.2) usa VE-07-014, el texto operacional (Section 3.1.3) usa VE-09-014. Área code 07 vs 09 son distintas áreas. Requiere resolución en Valve List Rev C simultáneamente.
- Código "BT": No existe en sistema P22. Según el Submittal Form, el documento type listado es sin especificar (campo "Doc. Type" = "Plant Control Philosophy" sin código tipo estándar).
- Nota positiva: UPS confirmado EN SCOPE (sección 1.3). Responde parcialmente a TM N4 pendiente sobre UPS en BOM — está en el sistema, pero con capacidad insuficiente.

**Veredicto:** 3 — To be Revised

**Análisis cruce TM N3 → Control Philosophy Rev A:**

En TM N3 (28-Ene-2026) ADASA formuló 5 observaciones al IO List (P22-LI-09-008-001 Rev A). Cuatro de esas observaciones siguen STILL PENDING (39 días) sin que BW Water emita Rev B. Al revisar el Control Philosophy Rev A, se constata que el documento tampoco incorpora las correcciones correspondientes. El Control Philosophy es el documento donde la lógica de esas señales debe quedar descrita.

| Obs TM N3 | Descripción | Estado en Control Phil. Rev A |
|-----------|-------------|-------------------------------|
| OBS-01 | TE09-001/002-XB001: switches DI en lugar de transmisores continuos 4-20mA+HART | ❌ AUSENTE — solo TSH como interruptor DI, sin AI de temperatura de motores |
| OBS-03 | Variables eléctricas VFD (V, I, P, f) ausentes en IO List | ❌ AUSENTE — solo speed feedback AI y fault DI |
| OBS-04 | DO Module Status (0=parado, 1=operando) hacia sistema externo | ❌ AUSENTE — sin señal de estado hacia sistema externo |
| OBS-05 | DI External Enable general del módulo | ❌ PARCIAL — solo permissives de tanques (permeate/off-spec), NO un enable general |

**Observaciones nuevas para TM N7 §3.4 (OBS-5, OBS-6, OBS-7):**

- **OBS-5 (CRÍTICA):** El Control Philosophy no describe monitoreo continuo de temperatura en motores HP Pump ni CIP Pump. La ET §5.3 (L1032) exige Pt-100 en devanados y rodamientos de todos los motores. Las señales TE09-001-XB001 y TE09-002-XB001 son interruptores ON/OFF (DI), no transmisores 4-20mA (AI). Origen: TM N3 OBS-01 — IO List Rev A recibida en Entrega 8 (Submittal 25007-0008), 39 días pendiente.

- **OBS-6:** El Control Philosophy no define ninguna señal DO que reporte el estado operativo del módulo a sistemas externos. TM N3 OBS-04 solicitó explícitamente esta señal (0=parado, 1=operando) — IO List Rev A recibida en Entrega 8 (Submittal 25007-0008), 39 días pendiente sin incorporación en ningún documento.

- **OBS-7:** El Control Philosophy incluye permissives de producto desde cliente (permeate tank permissive / off-spec tank permissive — §3.3.2 interno), pero no describe una DI de habilitación operacional general del módulo. TM N3 OBS-05 solicitó un enable general (1=puede operar, 0=debe detenerse) que permita a la planta SWRO inhibir el arranque o forzar la parada — IO List Rev A recibida en Entrega 8 (Submittal 25007-0008), 39 días pendiente. La Rev B debe distinguir entre permissives de producto (ya existentes) y el enable operacional del módulo (faltante).

---

## 3. Notas Van Doorn — Uso Interno ADASA

**Sobre el patrón BW Water en E14:**
"Esta entrega mezcla documentos que deberían haberse entregado hace meses (el A/C calc) con documentos nuevos (los planos y el Control Philosophy). Es positivo recibir el Control Philosophy — es el primer documento de control del sistema que vemos. El problema es que tiene errores que sugieren que no fue revisado contra el ET antes de submitarlo. El UPS de 30 minutos es demasiado obvio para haberlo pasado por alto — sugiere que el ingeniero que redactó el doc no tenía el ET o no lo leyó.

Los planos son aceptables para IFA. El Piping Layout y el Tie-In Point son documentos preliminares normales.

Mi recomendación estratégica: en el TM N7, mantener el lenguaje técnico directo. Los temas de UPS y Modbus TCP son los que necesitan resolución más urgente para el avance del proyecto. El veredicto 3 es correcto — no hay razón para rechazar la entrega completa cuando la mayoría de los documentos son aprobables con notas, pero los dos documentos de cálculo/control necesitan revisión."

---

## 4. Estado de Observaciones Pendientes de TMs Anteriores

| Obs | Origen | Descripción | Estado en E14 | Días desde origen |
|-----|--------|-------------|--------------|-------------------|
| A/C Thermal Calculation | TM N2 | Cálculo de respaldo térmico | **RECIBIDO — BAJO REVISIÓN (Rev B necesita correcciones)** | 65 |
| Modbus TCP Memory Map | TM N2 | Mapa de registros para integración SCADA | **STILL PENDING** — Control Philosophy no lo aborda | 65 |
| IO List Update | TM N3 | Señales Ethernet IP y digital stop | **STILL PENDING** | 44 |
| UPS in BOM | TM N4 | UPS 8h autonomía en scope | **PARCIALMENTE CERRADO** — UPS en scope confirmado (Control Phil. §1.3) pero capacidad es 30 min vs 8h requeridas | 37 |
| Equipment Layout Rev B (CIP footprint) | TM N5 | Footprint CIP externo | **PARCIALMENTE CERRADO** — Piping Layout muestra CIP externo. Equipment Layout específico puede seguir pendiente | 15 |
| Valve List Rev C (4 duplicados) | TM N6 | VM-09-015, VE-09-008, VE-09-009, VM-09-065 | **STILL PENDING** — No en E14 | 9 |
| Feed TC Rev D (coupling ≥2000 psi) | TM N6 | Acople Feed Turbocharger | **STILL PENDING** — No en E14 | 9 |
| Interstage TC FEDCO confirmation | TM N6 | MAWP coupling por fabricante | **STILL PENDING** | 9 |
| Vibration mounting TC | TM N6 | Explicit mounting en datasheets | **STILL PENDING** | 9 |
| CT-001 respuesta ADASA | TM N5 | Consulta técnica formal | **STILL OPEN — VENCIDO** | 27+ |

---

## 5. Determinación de Veredicto

| Documento | Veredicto individual |
|-----------|---------------------|
| P22-CD-09-005-002 A/C Thermal Calc Rev B | 3 — To be Revised |
| P22-DWG-09-005-004 Piping Layout Rev A | **3 — To be Revised** (CIP footprint no consolidado per TM N5 OBS-01) |
| P22-DWG-09-005-005 Tie-In Point Rev A | **3 — To be Revised** (corregido — ver §2.3) |
| P22-BT-09-009-001 Control Philosophy Rev A | 3 — To be Revised |

**Veredicto Global TM N7: 3 — To be Revised**

(4 de 4 documentos requieren revisión → Veredicto 3, per CLAUDE.md §6.2)
**Stats finales: 4× Code 3, 0× Code 2**

---

## 6. Observaciones Críticas para el Transmittal

Para TM N7 (documento externo a BW Water), incluir:

1. **UPS 30 min vs 8h:** Observación crítica — incumplimiento directo del ET.
2. **A/C Calc n+1 no explicitado:** Solicitar Rev C con todas las cargas y confirmación n+1.
3. **Control Philosophy tags discrepantes:** VE-07-014 vs VE-09-014 — resolución requerida.
4. **Modbus TCP:** Requerir fecha de entrega del Memory Map (65+ días).
5. **Tie-in N°1 incompleto.**
6. **Valve List Rev C, Feed TC Rev D:** Marcar como STILL PENDING en sección 4.

---

*Documento interno ADASA — Confidencial — No distribuir a BW Water*
*08-Mar-2026*
