---
tipo: Trazabilidad CCS — Documento Interno
transmittal: TM N10 — P22-TM-09-000-010-0
entrega: E18 / Submittal 25007-0018
fecha: 16-Mar-2026
nota: DOCUMENTO INTERNO — NO ENVIAR A BW WATER
referencia_compilado: Compilado-TM-N10.md (análisis detallado por documento)
---

# TRAZABILIDAD CCS — ENTREGA 18
## Consolidated Comment Sheets — Verificación ítem por ítem
## **NO ENVIAR — USO INTERNO ADASA**

---

## 1. Propósito y Alcance

Este documento verifica la afirmación del TM N10 Executive Summary:
> *"All responses [in the CCS] are acceptable except NOTE-05 (HMI Screenshots)"*

La verificación se hace ítem por ítem, identificando:
1. La observación original que generó cada CCS item (TM Nº / OBS-XX)
2. La respuesta literal de BW Water en el CCS
3. El veredicto de cierre: **CERRADO** / **PARCIAL** / **ABIERTO**
4. Los gaps residuales detectados al revisar el documento entregado

**Antecedente crítico:** En Entrega 13 (Valve List), BW Water declaró "Already revised" en CCS sin aplicar ninguna corrección. Se verificó que en Entrega 18 el patrón no se repite (TM N10 Approved as Noted confirma incorporación real).

**Fuente de datos CCS:**
- `ENTREGAS_BWWATER/ENTREGA 18/md/P22-LI-09-008-001-B_IO-List.md`
- `ENTREGAS_BWWATER/ENTREGA 18/md/P22-LI-09-008-004-A_Data-Transfer-List.md`
- `ENTREGAS_BWWATER/ENTREGA 18/md/P22-CD-09-004-001-C_Control-Architecture.md`

**Criterios de veredicto:**
- **CERRADO:** Respuesta confirma acción realizada; documento muestra la corrección; TM N10 no levantó nueva observación sobre ese punto específico.
- **PARCIAL:** Respuesta reconoce el issue; la acción fue ejecutada pero de forma incompleta o con error secundario; TM N10 levanta nueva observación derivada.
- **ABIERTO:** Respuesta es "will do" sin entrega efectiva, o respuesta genérica sin evidencia en el documento, o contradice lo observado.

---

## 2. I/O List Rev B — CCS Items 1 a 7

**Submittal referenciado:** CC P22-LI-09-008-001A
**Documento revisado en TM N10:** P22-LI-09-008-001 Rev B → *2 — Approved as Noted*

**Nota metodológica:** Los ítems 1–5 y 7 no muestran el comentario original de ADASA en el CCS (campo "Comment from Client" vacío). Solo el ítem 6 y 6(cont.) exhiben el texto original. Este es el mismo patrón de riesgo observado en Entrega 13, pero en este caso el resultado de TM N10 (Approved as Noted con observaciones puntuales) confirma que los items fueron efectivamente incorporados al documento.

| Item CCS | Observación original (TM / OBS) | Respuesta BW Water (literal) | Veredicto | Gap residual |
|----------|--------------------------------|------------------------------|-----------|--------------|
| 1 | TM N8 OBS-2 — IO List debe incorporar VT-09-001/002/003 (vibración) | "HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB" | **CERRADO** | Ninguno — VT09-001/002/003 presentes en Rev B ✓ |
| 2 | TM N8 OBS-2 — IO List debe incorporar TE-09-001/002/003/004 (RTD motores) | "HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB" | **PARCIAL** | TE vs TIT tag inconsistency → TM N10 OBS-01. Instrumentos presentes pero nomenclatura en conflicto con DTL |
| 3 | TM N7 OBS-03 / TM N3 — Solicitud de variables Modbus TCP/IP; IO List sin referencia a fieldbus | "HAS BEEN ADDED IN I/O LIST REV B. HAS BEEN ADDED IN P22-LI-09-008-004A Data Transfer List (Modbus TCP/IP)" | **CERRADO** | DTL Rev A entregado simultáneamente. TM N7 OBS-03 cerrado ✓ |
| 4 | TM N3 OBS-05 — FIT-09-001 duplicado; renombrar segundo flowmeter a FIT-09-002 | "HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB" | **CERRADO** | FIT-09-002 confirmado en IO List Rev B ✓ (TM N3 OBS-05 cerrado formalmente) |
| 5 | TM N7 OBS-05 / TM N3 — VFD electrical parameters sin punto AI; motor temperature solo DI (sin lectura continua) | "VFD ELECTRICAL PARAMETERS: VOLTAGE, CURRENT, POWER, FREQUENCY VIA ETHERNET IP INSTEAD OF AI. MOTOR TEMPERATURE RTD SENSOR WILL CONNECT TO 5069-IY4 FOR MONITORING AND TRENDING." | **PARCIAL** | VFD via EtherNet/IP aceptable. Motor RTD incorporado pero tag TE09-XXX en IO List vs TIT09-XXX en DTL → TM N10 OBS-01. La solución existe; la nomenclatura requiere unificación. |
| 6 | TM N7 OBS-05 (explícito) — "The specifications call for 3-wire RTDs for temperature control of pumps and motors. The current design only considers DI signals... it does not allow for online viewing of the equipment's operating temperature or the display of trends. It is requested that RTD-type I/O be considered and that displays showing the operating temperatures of the motors and pumps be included." | "MOTOR TEMPERATURE RTD SENSOR WILL CONNECT TO 5069-IY4 FOR MONITORING AND TRENDING." | **PARCIAL** | RTD a módulo 5069-IY4 confirmado — acción técnica correcta. Gap residual: tags TE vs TIT (TM N10 OBS-01). El monitoreo existe; la unificación documental entre IO List y DTL está pendiente. |
| 6 (cont.) | TM N3 OBS-04 (DO module status) + TM N3 OBS-05 (DI module enable) + TM N7 OBS-06/07 (explícito) — "Please send another list with variables to be controlled via fieldbus. The electrical variables for VFDs and the system's main electrical variable meter are missing. Controls are required for coordination with systems external to the module: A DO output that activates when the module stops normally or due to a fault (0=stopped; 1=running). A DI input that indicates to the module that it can operate (1=may operate; 0=must stop)." | "HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB. HAS BEEN ADDED IN P22-LI-09-008-004A Data Transfer List (Modbus TCP/IP)" | **PARCIAL** | DO (item 19) y DI (item 21) presentes en IO List Rev B. Mapeados en DTL. Gap residual: tipo de contacto especificado como "Dry Contact (N.O) 24VDC" → debe ser "relay contact" per confirmación Ronald 11-Mar-2026 → TM N10 NOTE-01 (MINOR). |
| 7 | TM N8 OBS-2 — IO List debe incorporar LIT-09-002 (CIP Tank Level Transmitter) | "HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB" | **CERRADO** | LIT-09-002 incorporado ✓ |

**Resumen IO List CCS:** 3 CERRADOS / 4 PARCIALES / 0 ABIERTOS

**Coherencia con TM N10 ES:** La afirmación "all responses acceptable" es correcta para IO List. Los gaps (OBS-01, NOTE-01) son consecuencias de la implementación, no de que BW Water ignorara el request.

---

## 3. Data Transfer List Rev A — CCS Items 1, 2 y 5

**Submittal referenciado:** TRANSMITTAL N3 ADASA-BW
**Documento revisado en TM N10:** P22-LI-09-008-004 Rev A → *2 — Approved as Noted*

**Contexto:** La DTL no existía antes de esta entrega. TM N3 solicitó el mapa Modbus TCP/IP. Los ítems del CCS responden a las observaciones del TM N3 sobre la ausencia del documento. Los ítems están numerados 1, 2 y 5 (los números originales del CCS de TM N3 que le aplican a este documento).

**Nota:** Los comentarios originales de ADASA no están completamente capturados en el CCS (campo vacío en ítems 1 y 2). Item 5 sí muestra el texto original.

| Item CCS | Observación original (TM / OBS) | Respuesta BW Water (literal) | Veredicto | Gap residual |
|----------|--------------------------------|------------------------------|-----------|--------------|
| 1 | TM N3 — Solicitud de lista de variables Modbus TCP/IP (primera solicitud; DTL no existía) | "Has been added in P22-LI-09-008-004A Data Transfer List (Modbus TCP/IP)" | **PARCIAL** | DTL entregada con 189 ítems (64 DI, 16 DO, ~109 AI/AO). Gap residual: rangos de conductividad CIT-09-001/004/005 incorrectos para brine service (0–20 mS/cm vs 65–133 mS/cm real) → TM N10 OBS-02 (MAJOR). |
| 2 | TM N3 — Variables de fieldbus faltantes; nivel de tanques, señales de estado | "Has been added in P22-LI-09-008-004A Data Transfer List (Modbus TCP/IP)" | **PARCIAL** | DTL incluye 64 DI mapeados. Gap residual: items 22–23 en bloque DI asignan VE09-014-SI001/SIC001 (señales analógicas REAL, ya correctamente mapeadas en addresses 40039/40071) → error copy/paste. En esas posiciones debían ir LS09-001 (tank level HIGH) y LS09-002 (tank level LOW) — señales discretas del IO List items 128–129 que están completamente ausentes del mapa Modbus → TM N10 OBS-03 (MAJOR). |
| 5 | TM N3 OBS-04 + OBS-05 + TM N7 OBS-03 (explícito) — "Please send another list with variables to be controlled via fieldbus. The electrical variables for VFDs and the system's main electrical variable meter are missing. Controls are required for coordination with systems external to the module: (1) A DO output that activates when the module stops normally or due to a fault (0=stopped; 1=running). (2) A DI input that indicates to the module that it can operate (1=may operate; 0=must stop)." | "Has been added in P22-LI-09-008-004A Data Transfer List (Modbus TCP/IP). HAS BEEN ADDED IN I/O LIST — P22-LI-09-008-001 REVB" | **PARCIAL** | Enable Command (10001.7) y Running Status (00001.0) presentes en DTL ✓. VFD parameters en 40015–40027 ✓. Gap residual: tipo de contacto en IO List dice "Dry Contact 24VDC" — debe ser relay contact → TM N10 NOTE-01. Observación TM N7 OBS-03 formalmente cerrada con la entrega del documento. |

**Resumen DTL CCS:** 0 CERRADOS / 3 PARCIALES / 0 ABIERTOS

**Coherencia con TM N10 ES:** "All responses acceptable" es correcto — BW Water entregó un documento sustantivo con 189 ítems. Los gaps (OBS-02, OBS-03) son errores de contenido dentro del documento, no incumplimiento del request original.

---

## 4. Control Architecture Rev C — CCS Items 1 a 8

**Submittal referenciado:** TRANSMITTAL N4 ADASA-BW (27-Feb-2026)
**Documento revisado en TM N10:** P22-CD-09-004-001 Rev C → *2 — Approved as Noted*

**Contexto:** TM N4 revisó Control Architecture Rev B. El CCS en Rev C responde a las 8 observaciones de TM N4. La arquitectura es predominantemente gráfica; la verificación de algunos ítems (especialmente UPS) depende de información textual que el diagrama no provee.

| Item CCS | Observación original (TM / OBS) | Respuesta BW Water (literal) | Veredicto | Gap residual |
|----------|--------------------------------|------------------------------|-----------|--------------|
| 1 | TM N4 — Digital Power Meter, VFD y Motorized Valve no declarados como dispositivos TCP/IP en arquitectura Rev B | "NO. DIGITAL POWER METER, VFD AND MOTORIZED VALVE IS COMMUNICATE THROUGH TCP/IP." | **CERRADO** | TCP/IP confirmado y visible en Rev C. TM N10 acepta. IO List Items 1–11 (Power Meter) y DTL addresses correspondientes confirman integración ✓. Nota: respuesta tiene "NO." inicial que parece traducción — el sentido es "NOTE / Confirmación". |
| 2 | TM N4 — Revisión general de arquitectura; incluye UPS autonomía (req. 8 horas per ET — Control and Automation System) | "HAS REVISED IN CONTROL SYSTEM ARCHITECTURE — P22-CD-09-004-001 REVC" | **PARCIAL** | Respuesta genérica. Rev C es predominantemente gráfica; no se puede extraer especificación UPS ni cálculo de capacidad del diagrama. TM N7 OBS-01 requirió 8 horas (vs 30 min declarados en Control Philosophy Rev A). TM N10 OBS-04 (MAJOR): sin evidencia escrita de cumplimiento → BW Water debe proporcionar confirmación + cálculo. |
| 3 | TM N4 — Consulta sobre redundancia de controlador | "BASED ON TENDER PROPOSAL OUR OFFER IS ONLY STANDALONE PLC CPU INSTEAD OF CONTROLLER REDUNDANCY." | **CERRADO** | Posición de BW Water clara y consistente con Technical Offer Rev1. TM N10 acepta ✓. No genera requisito adicional. |
| 4 | TM N4 + TM N7 OBS-08 — HMI screen design, layout y compliance ISA 101 no declarado en arquitectura Rev B; solicitud de screenshots | "WILL SUBMIT IN HMI DISPLAY SCREENSHOT P22-BREAD-09-008-001" | **ABIERTO** | Documento P22-BREAD-09-008-001 NO entregado en Entrega 18. Comprometido desde TM N4; reiterado en TM N10 NOTE-05. Requerido para verificar ISA 101 compliance y diseño HMI per ET — Control and Automation System. Candidato prioritario para TM N11. |
| 5 | TM N4 — IO List no había sido sometida a revisión | "THIS HAS BEEN SUBMITTED IN I/O LIST — P22-LI-09-008-001" | **CERRADO** | IO List Rev B entregada en Entrega 18 y revisada en TM N10 ✓. |
| 6 | TM N4 — Data Transfer List (Modbus TCP/IP) no había sido sometida | "THIS HAS BEEN SUBMITTED IN Data Transfer List (Modbus TCP/IP) — P22-LI-09-008-004" | **CERRADO** | DTL Rev A entregada en Entrega 18 y revisada en TM N10 ✓. TM N7 OBS-03 cerrado. |
| 7 | TM N4 — Elemento faltante en diagrama de arquitectura (identificado en revisión Rev B) | "HAS ADDED IN CONTROL SYSTEM ARCHITECTURE — P22-CD-09-004-001 REVC" | **CERRADO** | TM N10 acepta Rev C Approved as Noted ✓. La adición no generó nueva observación específica. |
| 8 | TM N4 — Segundo elemento faltante en arquitectura Rev B | "HAS ADDED IN CONTROL SYSTEM ARCHITECTURE — P22-CD-09-004-001 REVC" | **CERRADO** | Ídem item 7 ✓. |

**Resumen Control Architecture CCS:** 5 CERRADOS / 2 PARCIALES / 1 ABIERTO

**Coherencia con TM N10 ES:** "All responses acceptable except NOTE-05" es correcto para los ítems 1–3 y 5–8. La excepción NOTE-05 (ítem 4) es el único ABIERTO genuino. El ítem 2 (UPS) es PARCIAL — la respuesta se acepta pero la verificación de cumplimiento está pendiente (OBS-04).

---

## 5. Tabla Resumen Consolidada

| Documento | Items CERRADO | Items PARCIAL | Items ABIERTO | Total items |
|-----------|:-------------:|:-------------:|:-------------:|:-----------:|
| I/O List Rev B | 3 | 4 | 0 | 7 (+1 cont.) |
| Data Transfer List Rev A | 0 | 3 | 0 | 3 |
| Control Architecture Rev C | 5 | 2 | 1 | 8 |
| **TOTAL** | **8** | **9** | **1** | **18+1** |

**Interpretación:** 47% CERRADO, 50% PARCIAL, 3% ABIERTO.

El alto porcentaje PARCIAL no indica rechazo — indica que BW Water ejecutó la acción solicitada, pero la verificación al revisar el documento reveló deficiencias secundarias. Esta es la distinción clave con la Entrega 13 (Valve List), donde las respuestas "Already revised" no tenían ninguna evidencia de corrección. En Entrega 18, todos los PAR-CIALES tienen evidencia de acción.

---

## 6. Candidatos TM N11 — Derivados del CCS Entrega 18

Los siguientes issues surgen directamente de la verificación del CCS y deben tener seguimiento en TM N11:

### 6.1 Prioridad MAJOR (derivados de CCS PARCIALES)

| Issue | Origen CCS | Observación TM N10 | Acción requerida BW Water |
|-------|-----------|-------------------|--------------------------|
| Unificación tags TE vs TIT para RTDs motores | IO List items 2, 5, 6 / DTL items 1, 5 | OBS-01 (MAJOR) | IO List Rev C + DTL Rev B + IL Rev C con tag único por instrumento; confirmar servicio TIT-09-003 |
| Rangos conductividad CIT-09-001/004/005 incorrectos para brine | DTL items 1, 2 | OBS-02 (MAJOR) | DTL Rev B + IL Rev C con rangos correctos (65–133 mS/cm); evaluar tecnología toroidal para CIT-09-001/004 |
| Level alarms LS09-001/002 ausentes del mapa Modbus; VE09-014 duplicado en DI block | DTL item 2 | OBS-03 (MAJOR) | DTL Rev B: remover duplicado, agregar LS09-001/002 en addresses 10002.5–10002.6 |
| UPS 8-hour autonomy — sin verificación en documento | Control Arch item 2 | OBS-04 (MAJOR) | Confirmación escrita + load list + battery bank calculation |

### 6.2 Prioridad MINOR (derivados de CCS PARCIALES)

| Issue | Origen CCS | Observación TM N10 | Acción requerida BW Water |
|-------|-----------|-------------------|--------------------------|
| Tipo de contacto: "Dry Contact 24VDC" → debe ser "relay contact" | IO List item 6 (cont.) / DTL item 5 | NOTE-01 (MINOR) | IO List Rev C items 19 y 21: actualizar a "relay contact" |

### 6.3 ABIERTO — Comprometido no entregado

| Issue | Origen CCS | Observación TM N10 | Deadline sugerido |
|-------|-----------|-------------------|--------------------|
| HMI Display Screenshots P22-BREAD-09-008-001 | Control Arch item 4 | NOTE-05 | Entrega 19 (deadline a acordar) |

---

## 7. Verificación de Coherencia con TM N10 Executive Summary

**Afirmación TM N10 ES:** *"All responses are acceptable except NOTE-05 (HMI Screenshots)"*

**Veredicto de esta trazabilidad:**

La afirmación es **técnicamente correcta** con la siguiente matización:

1. **"All responses acceptable"** — En los 18 ítems CCS, BW Water ejecutó la acción solicitada en todos los casos excepto NOTE-05. Ninguno es un "Already revised" vacío (patrón Entrega 13).

2. **"Except NOTE-05"** — Correcto. P22-BREAD-09-008-001 fue comprometido pero no entregado. Es el único ABIERTO genuino.

3. **Matización no reflejada en ES:** Los ítems PARCIALES muestran que la ejecución tuvo errores secundarios (tag inconsistency, conductivity ranges, level alarms missing, UPS no verificable). Estos no invalidan las respuestas CCS, pero generaron 4 nuevas observaciones MAJOR en TM N10 (OBS-01, OBS-02, OBS-03, OBS-04). La ES no contradice esto — describe el estado CCS, no el estado del documento revisado.

4. **Riesgo de precedente:** La DTL Rev A (primer entrega de este documento) tiene 2 MAJOR en el primer review. Si se repite el patrón de ranges incorrectos en Rev B, será el segundo CCS con implementación incompleta. Monitorear en TM N11.

---

## 8. Patrón de Documentación CCS — Evaluación de Riesgo

| Patrón | Entrega 13 (Valve List) | Entrega 18 (IO List + DTL + Control Arch) |
|--------|------------------------|-------------------------------------------|
| Comentario original ADASA visible en CCS | Parcialmente | Parcialmente (solo items 6/6cont. IO List e item 5 DTL) |
| Items sin comentario original ("HAS BEEN ADDED") | Sí | Sí (IO List items 1–5, 7; DTL items 1–2) |
| Corrección efectivamente aplicada al documento | **NO** | **SÍ** — confirmado por TM N10 |
| Veredicto general | Riesgo realizado | Riesgo mitigado |

**Conclusión:** El patrón de ítems sin comentario original persiste en Entrega 18. La diferencia con Entrega 13 es que en este caso el contenido fue efectivamente incorporado. ADASA debe continuar verificando el documento (no solo el CCS) en cada entrega — esta trazabilidad confirma que ese enfoque es el correcto.

---

*Generado: 16-Mar-2026 | Revisado por: Luis Rivera | Para uso interno ADASA*
*Referencia: Compilado-TM-N10.md §6 (auditoría CCS resumida) + P22-TM-09-000-010-0_TRANSMITTAL.md*
