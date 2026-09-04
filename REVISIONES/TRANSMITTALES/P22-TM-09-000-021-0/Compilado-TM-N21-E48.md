# Compilado interno — TM N21 / ENTREGA 48 (BW Water)

**Estado:** TM N21 **ENVIADO** a BW Water el 11-Jun-2026. (Este Compilado es el análisis interno — NO ENVIAR a BW Water.)

> **CALIBRACIÓN DEL USUARIO (fijada):** Datasheet PLC/HMI = **Code 3** (HART); Grounding = **Code 2 con
> condición**; veredicto global TM = **3 — To Be Revised**. Cruces verificados (Modbus / RTD / ET HART).
**Submittal:** 25007-0048. **Fecha entrega:** 06-Jun-2026 (datasheet 09-Jun-2026). **TM:** P22-TM-09-000-021-0.
**Documentos:** 2 (ambos E&C — fuera de alcance Van Doorn).

> Método de lectura: marcas rojas del datasheet = anotaciones `Square` sobre las celdas comprometidas;
> texto extraído de la capa de texto (no OCR), spot-check visual de PLC/HMI OK. Grounding revisado vía
> CCS (texto) + render de planos (modo drawing). Baseline de comentarios previos verificado contra los
> `.md` reales de TM N1 / N19 / N20 (no contra síntesis de subagente).

## Tabla de disposición (códigos PROPUESTOS — a calibrar)

| Doc | Código | Rev | Responde a | Código propuesto | Driver |
|-----|--------|-----|------------|------------------|--------|
| Grounding Point & Power Panel Location Layout | P22-DWG-09-007-003 | F | TM N19 (Code 3 / Rev E) | **1 — Approved** | Schedule embebido cierra el item más antiguo (~88 d); aprobado as-is, emitir en Rev 0 (la revision history se completa al emitir). Sin CC_ADASA |

> **Recalibración del usuario (Grounding → Code 1):** la única pendiente (completar descripción + ECN del bloque de revisiones) es housekeeping que ocurre al emitir cualquier revisión, NO un defecto técnico que obligue a modificar el documento → no es Code 2. Estado **1 — Approved**; se indica en el transmittal que lo emitan en Rev 0. Sin anotación CC_ADASA (Code 1, §3.8). El veredicto global del TM se mantiene **3** (lo fija el datasheet).
| Datasheet of PLC and HMI Panel Component | P22-ET-09-008-001 | B | TM N1 (Code 2 / Rev A) | **3 — To Be Revised** | El panel no provee vía de adquisición HART para la instrumentación 4-20mA+HART que exige la ET 5.5; + reconciliar módulo RTD + typo portada |

**Veredicto global: 3 — To Be Revised** (peor código = 3, lo fija el datasheet por HART).

### Cruces verificados (Stage 1.5)
- **Modbus — CERRADO por referencia (válido).** La Control System Architecture P22-CD-09-004-001 Rev B trae el gateway **ProSoft PLX32-EIP-MBTCP** (EtherNet/IP interno del panel → Modbus TCP/IP al DCS ADASA; enlace LCP→DCS "by others" = ADASA). El cierre que BW Water declara en el CCS se sostiene → **no se levanta observación Modbus contra el datasheet**.
- **RTD — inconsistencia entre documentos (no hueco).** El rack real (Schematic Rev A BOM / LCP Datasheet Rev B) es: 1×5069-L320ER + 2×5069-IB16 + 1×5069-OB16 + **2×5069-IY4** + 5×5069-IF8 + 2×5069-OF4. Los 8 canales Pt-100 (IY4) **sí existen** en el LCP Datasheet Rev B; este datasheet de componentes omite el IY4 y no refleja la población real del rack → reconciliar.
- **HART — base reformulada.** ET 5.5 (P22-ET-09-000-001 línea 1311): "el protocolo de la instrumentación deberá ser 4-20mA + HART" = requisito sobre la instrumentación de campo. La observación defendible NO es "el 5069-IF8 viola la ET", sino que **el panel no provee ninguna vía de adquisición HART** (ni AI con HART ni multiplexor HART en el rack), por lo que la capacidad HART que la ET manda no la puede usar el sistema de control. Driver del Code 3.

---

## Documento 1 — Grounding Layout Rev F (P22-DWG-09-007-003)

Responde al TM N19 (Rev E, Code 3). El plano trae **CCS legible** (p2-3) + **Ground Cable Schedule
embebido** (p6-7, 48 filas) + planos (p4-7, rotados 270°).

### Cómo responde BW Water a cada comentario del TM N19

| Comentario ADASA (TM N19) | Respuesta BW (CCS) | Estado verificado en el plano |
|---|---|---|
| **OBS-01 (MAJOR, ~70-110 d)** — Ground Cable Schedule completo (PE IDs, sección/carga, ring-main, bonding equipotencial per NCh Elect. 4/2003 Sección 10.0) + distinción Cu desnudo/trenzado vs Cu/PVC aislado | "Grounding Schedule has been revised and added in RevF" | **CERRADO.** Schedule embebido p6-7 (48 conductores > sample 26): columnas PE Conductor ID / sección PE (mm²) / Cable Specification / Topology = "Ring Main" / Equipotential Bonding = "Yes" en todas las filas. Distinción Cu atendida: bonding tray-tray = "Cu Tinned Flexible Braided"; resto "Cu/PVC"; Material Take-Off (p5) lista Copper Earth Link / Cu/PVC / Cu Tinned Braided por separado |
| **Nota 5** ("relocation based on site condition") rebatida + main panel fijo | "Note 5 has been removed from RevF" | **CERRADO.** Cero ocurrencias de "indicative/relocation/site condition". Main panel P22-LCP-01 en tabla POWER PANEL LOCATION (p4), posición fija |
| **Eje normativo** — unificar a IEC 60364-5-54 (quitar NEC Table 250.122) | "Revised to replace NEC Table 250.122 with IEC 60364-5-54" | **CERRADO.** Cero "NEC Table 250.122" en el plano; notas de dimensionamiento citan IEC 60364-5-54. (Quedan NEC Art. 392.30(B)/352 pero son método de instalación de bandeja/conduit, no dimensionamiento → legítimas) |
| **OBS-02 (MINOR)** — revision history con descripción de cambios + ECN por Rev B→E | "The revision history table **will be updated**..." (tiempo futuro) | **NO ATENDIDO.** El cajetín Rev F sigue con "REVISED AS PER COMMENT" genérico en las 5 filas (B→F) y **columna ECN vacía**. BW Water lo promete a futuro, pero el entregable que debía traerlo ES esta Rev F |
| **NOTE-01 (MINOR)** — CCS legible (Rev E venía rasterizada) | "Reissued from electronic source at sufficient resolution" | **CERRADO.** CCS Rev F es texto extraíble/legible |

### Hallazgos / matices
- Contradicción reply-vs-documento en OBS-02: el "will be updated" se presenta como cierre cuando el
  documento que debía ejecutarlo es esta misma Rev F. Punto administrativo, no sustantivo.
- DRAWING STATUS del cajetín = "ISSUED FOR APPROVAL" (no IFC) — coherente con Rev F para aprobación.
- Confirmar que la no-aplicación del Method 1 (declarada por BW Water: "Method 2 to 7 in use, Method 1
  not applied") no deja sin método la barra de tierra principal.

### Código propuesto: **2 — Approved as Noted**
Tres ejes mayores (schedule, main panel/nota 5, IEC) + NOTE-01 cerrados as-is; resta solo OBS-02
(completar DESCRIPTION + ECN del bloque REVISIONS), corrección menor al propio documento incorporable al
emitir Rev 0 sin nueva revisión intermedia (criterio §6.2).
**Action to issue at IFC Rev 0 — no new revision required:** reemplazar "REVISED AS PER COMMENT" genérico
por una descripción real de cambios + referencia ECN por cada Rev B→F en el bloque de revisiones.
> Alternativa estricta (a calibrar): tratar el "will be updated" como punto comprometido y no ejecutado →
> Code 3. Recomendación: Code 2 con condición explícita (lo sustantivo, el schedule de ~70-110 d, ya
> cerró; solo resta trazabilidad administrativa en el cajetín).

---

## Documento 2 — Datasheet PLC and HMI Panel Component Rev B (P22-ET-09-008-001)

Rev A se entregó en E1 (TM N1, 16-Dic-2025) → Code 2 ("verificar disponibilidad Modbus TCP/RTU"). No se
revisó de nuevo hasta esta Rev B. Es el datasheet de componentes mayores del panel PLC/HMI.

### Selección de componentes COMPROMETIDA (specs en rojo + páginas-resumen BW)

| Componente | Modelo comprometido | Datos clave (rojo) |
|---|---|---|
| **Controlador PLC** | Allen-Bradley **5069-L320ER / L320ERM** (CompactLogix 5380) | 2 MB memoria, 16 módulos locales / 31 nodos, 18-32 Vdc, 8.5 W, **comms 2× EtherNet/IP**, c-UL-us/CE/IECEx/CCC |
| **Entrada digital (DI)** | **5069-IB16** | 16 ch 12/24 Vdc sinking, 10-32 Vdc, 3.9 W |
| **Salida digital (DO)** | **5069-OB16** | 16 ch sourcing, 0.5 A/ch, 3.25 W |
| **Entrada analógica (AI)** | **5069-IF8** | 8 ch corriente/voltaje, 0-20/4-20 mA; nota: "agregar resistor externo 250 Ω para HART"; 2.1-2.4 W |
| **Salida analógica (AO)** | **5069-OF4 / 5069-OF8** | 4/8 ch corriente/voltaje |
| **HMI** | PanelView Plus 7 Performance **2711P-T10C22D9P** | 10.4" TFT touch, dual Ethernet, 24 Vdc, 50 W, **comms EtherNet/IP** |

### Cómo responde al comentario previo (CCS, p2)
- TM N1 (único comentario: verificar Modbus TCP/RTU) → **Reply BW:** "MODBUS TCP/RTU has been verified in
  Control System Architecture (P22-CD-09-004-001-B) and closed in Technical Review Transmittal N4 1.3.3."
  → Cierre **por referencia cruzada**. A verificar (ver Hallazgo 3).

### Hallazgos nuevos (ADASA) — cada uno con su requisito

1. **(DRIVER Code 3) Sin vía de adquisición HART en el panel.** ET 5.5 (línea 1311): "el protocolo de la
   instrumentación deberá ser 4-20mA + HART". El módulo AI comprometido **5069-IF8** lee 4-20mA pero **no
   decodifica HART** (su propia nota agrega un resistor de 250 Ω solo para un equipo HART externo en el
   lazo). El rack completo (CPU + 2×IB16 + OB16 + 2×IY4 + 5×IF8 + 2×OF4) **no incluye ninguna AI con HART
   ni multiplexor HART** → la capacidad HART que la ET exige a la instrumentación no la puede usar el
   sistema de control. Acción: proveer adquisición HART (tarjeta AI HART-capaz o multiplexor HART) o
   justificar formalmente la omisión. (Base reformulada: la observación es la **falta de vía HART en el
   panel**, no que el 5069-IF8 "viole" la ET — así no la rebate BW Water con "nuestros transmisores sí son
   HART".)
2. **Reconciliar módulo RTD (Pt-100 motores) — VERIFICADO.** El rack real (Schematic Rev A BOM + LCP
   Datasheet Rev B) incluye **2× 5069-IY4** = 8 canales Pt-100 motores (winding/bearing). Este datasheet de
   componentes mayores **omite el 5069-IY4** (solo lista IB16/OB16/IF8/OF4/OF8) y no refleja la población
   real del rack. No es hueco (el IY4 existe en el LCP Datasheet) → es inconsistencia documental: incorporar
   el 5069-IY4 a este datasheet o referenciar explícitamente el LCP Datasheet/Schematic para el rack del
   proyecto.
3. **Modbus — CERRADO (no se levanta).** Verificado: la Control System Architecture P22-CD-09-004-001 Rev B
   trae el gateway ProSoft PLX32-EIP-MBTCP (EtherNet/IP→Modbus TCP/IP al DCS). El cierre por referencia del
   CCS de BW Water se sostiene. (Solo dejar trazado, fuera del TM, el Modbus memory map que sigue pendiente
   como entregable separado de la arquitectura.)
4. **Typo de portada (QA, NOTE).** La carátula (p1) dice "Second Stage RO Module for Brine – PD **Tattal**"
   (debe ser **Taltal**) — mismo typo señalado en TM N20 NOTE-01 para el Outline. Corrección menor.

### Aporte colateral útil
El datasheet entrega el consumo por módulo (controlador 8.5 W, IB16 3.9 W, OB16 3.25 W, IF8 2.1-2.4 W,
OF8 5.3 W, HMI 50 W) → insumo para el **consumo total de panel** que quedó pendiente en TM N20 (acción del
LCP Datasheet, no de este documento). Mantener trazado.

### Nota sobre "planos" del datasheet
Las páginas con dibujo (dimensiones p8; diagramas de cableado p11/17/23/24/30/31) son **diagramas de
catálogo Rockwell/NHP** (referencia del fabricante), no planos de diseño del proyecto. Se leyeron por su
capa de texto + spot-check visual; no requieren tratamiento de plano de proyecto. El único plano de
proyecto de la entrega es el Grounding Layout (Documento 1, revisado en modo drawing).

### Código: **3 — To Be Revised** (CALIBRADO)
La selección de hardware (CompactLogix 5380 + PanelView Plus 7) es coherente, pero el documento debe
revisarse (Rev C) por la falta de vía de adquisición HART y la inconsistencia del rack. **Acción in Rev C:**
(a) proveer adquisición HART (AI HART-capaz o multiplexor HART) o justificar formalmente la omisión frente
a ET 5.5; (b) incorporar el módulo RTD 5069-IY4 (2 unidades / 8 canales Pt-100) y reflejar la población
real del rack, consistente con el LCP Datasheet Rev B y el Schematic; (c) corregir el typo de portada "PD
Tattal" → "PD Taltal". Modbus NO se observa (cerrado por la Control System Architecture Rev B).
> Lo anterior fija el veredicto global del TM = 3. Resto de comentario histórico retirado tras calibración:
> veredicto global del TM.

---

## Puntos a calibrar contigo (antes de emitir el TM)
1. **Datasheet — HART:** ¿ET 5.5 exige HART nativo en la AI del PLC (→ Code 3) o se admite multiplexor /
   HART solo en campo (→ Code 2 clarificación)? Define el código del datasheet y el veredicto global.
2. **Datasheet — módulo RTD:** ¿levantamos la ausencia del 5069-IY4 como observación de consistencia, o
   se asume cubierto por el LCP Datasheet Rev B (P22-ET-09-007-005) y solo se pide reconciliar?
3. **Grounding — OBS-02:** ¿Code 2 con condición (pragmático, lo sustantivo ya cerró) o Code 3 estricto
   (punto comprometido y reincidente no ejecutado en el propio Rev F)?
4. **Modbus:** ¿verificamos nosotros la Control System Architecture (P22-CD-09-004-001-B) para confirmar
   la interfaz MODBUS TCP/IP antes de aceptar el cierre por referencia, o lo pedimos como confirmación a BW?
5. Severidades de las observaciones del datasheet (MAJOR/MINOR) para los CC_ADASA de Stage 2.

## Pendiente Stage 2 (tras calibrar)
TM N21 (.md inglés + DOCX template-adasa), CC_ADASA anotados (Grounding OBS-02; Datasheet HART/RTD/Modbus/
typo), correo de remisión, anti-ia, actualización Master Register (`generar_excel_registro_v4.py`) y READMEs.
