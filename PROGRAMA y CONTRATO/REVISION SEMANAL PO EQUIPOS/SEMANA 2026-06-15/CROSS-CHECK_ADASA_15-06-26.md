# Cross-check ADASA — Procurement Tracker BW Water (Semana 15-Jun-2026)

> Análisis overlay ADASA del `Copy of Procurement tracking - BW Water 1506.xlsx` contra baseline 05-Mar-2026 y Project Schedule Rev A (08-Jun). Comparación slip-a-slip vs semana 08-Jun (tracker 1006, dentro del zip de progreso). Metodología CLAUDE.md §11.

## 1. Resumen por clasificación

| Clasif. | Cant. | Ítems |
|---|---|---|
| **CRITICAL** | 5 | RO Pressure Vessel (Protec); HP Feed Pump BH-09-001 (Fedco); Feed Turbo SIP-09-001 (Fedco); Interstage Turbo SIP-09-002 (Fedco); PLC Panel (KVC) |
| **WARNING** | 6 | Instrument Set (Emerson/IFM); RO Cartridge Filter FIL-09-001 (TK Solution); CIP Cartridge Filter FIL-09-002 (TK Solution); RO Membranes (LG); CIP/Flushing Pumps BH-09-002 (Grundfos); Structural Frames (BW Water) |
| **OK** | 9 | CIP Heater; Container (done); CIP Tank; Antiscalant Tank (done); Antiscalant Pumps (done); Static Mixer; Piping SS/Super duplex; Valve Sets (Delco); Gasket (nuevo) |

## 2. Top-3 alertas

1. **RO Pressure Vessel (Protec Arisawa) — dato de tracker obsoleto en el ítem que gobierna la ruta crítica.** Tracker: EAP Penang **29-May** (fecha pasada, sin "actual arrival"). Project Schedule Rev A: ex-works España **23-Jun** → Penang **02-Ago** (versión sin estampa ASME). **~65 días de inconsistencia.** Acción: BW Water debe corregir el tracker a la fecha post-ASME. Deadline: próximo tracker / reunión hoy.
2. **Fedco (HP Pump BH-09-001 status D + Feed/Interstage Turbo).** Anticipo 30% sin resolver (rechazado por ADASA como causal, BAE Cl.27/31/32/35/46). EAP tracker 05-Ago / schedule 09-Ago → ventana running-test→EXW Penang (15-Ago) de **6–10 días**. Acción: confirmación escrita de resolución del anticipo + plan de evidencia de running test (ventana ~2 d, 10–11 Ago). Deadline: reunión hoy.
3. **PLC Panel (KVC Industrial).** Status E con contradicción de ingeniería sin cerrar: PLC/LCP Outline Panel Rev B = Code 3 (enclosure SS316L NEMA4X/IP66 vs sheet steel IP55). Riesgo de fabricar el enclosure equivocado. EAP 29-Jul vs cierre de contenedor ~03-Ago. Acción: confirmar material y emitir Outline Rev B. Deadline: 19-Jun.

## 3. Bottleneck — Fedco (vendor único, 4 ítems en ruta crítica)

HP Feed Pump (BH-09-001) + Feed Turbo (SIP-09-001) + Interstage Turbo (SIP-09-002) — todos Fedco, EAP ~05–09 Ago, running test 10–11 Ago, EXW Penang 15-Ago. Concentración de un solo proveedor sobre el cierre del FAT. El anticipo 30% es el blocker activo; mientras no se resuelva por escrito, BH-09-001 sigue en D y la ventana de pre-embarque (~6 d) no tiene holgura.

## 4. Slips vs semana 08-Jun (tracker 1006)

**El tracker está prácticamente estático semana-a-semana.** Sin cambios de fecha (PO/EAP) en ningún ítem. Cambios estructurales:
- **Nuevo ítem:** Gasket (item 21, SJP Sealing, PO 14-Jun, EAP 29-Jun, lead 2 sem) — OK.
- PLC Panel perdió su número de ítem (renumeración; ahora sin "#").

> El que el tracker no registre movimiento ni se reconcilie con el Schedule Rev A (08-Jun) es en sí un hallazgo: la herramienta de monitoreo no refleja el cambio mayor del periodo (ruta de los tubos de presión post-ASME).

## 5. Variances vs baseline 05-Mar (PO fuera de ventana)

| Ítem | Ventana baseline | PO Date | Slip PO | Estado |
|---|---|---|---|---|
| RO High Feed Pump (Fedco) | Mar 4–10 | 15-May | ~+66 d | D |
| CIP/Flushing Cartridge Filter (TK Solution) | Mar 23–27 | 10-Jun | ~+75 d | E |
| Valve Sets (Delco) | Apr 20–24 | 26-May | ~+32 d | C |
| RO Cartridge Filter (TK Solution) | May 4–8 | 10-Jun | ~+33 d | E |

## 6. Notas operativas (data quality)

1. **Status "E" (Enabled = PO pending issuance) con PO Date ya cargada** en 5 ítems: Instrument Set (29-Abr), CIP Cartridge Filter (10-Jun), RO Cartridge Filter (10-Jun), CIP/Flushing Pumps (13-May), PLC Panel (12-May). Contradicción legend↔dato. Pedir aclaración: ¿la PO está emitida o no? **Afecta directamente el hito de pago 15% (EP-2 = OCs confirmadas).**
2. **Static Mixer:** PO Date `06-May-2025` (typo de año; debería ser 2026).
3. **RO Membranes (LG):** tracker EAP 03-Ago "direct to Taltal"; el Schedule Rev A las ubica ~19-Ago (manuf. fin 29-Jul + 21 d seafreight). Reconciliar: si llegan 19-Ago no alcanzan el EXW Penang 15-Ago → entrega escalonada / directa a sitio.
4. **Structural Frames/Supports (BW Water in-house):** "ready 1-Jul tras cálculo sísmico". Depende del Stress & Flexibility analysis de cañerías HP, que en el DDSR figura **Not submitted** (plan 29-Jun).

## 7. Lectura ejecutiva

La fabricación va sobre una ruta crítica recuperada (EXW Penang 15-Ago, fin 19-Nov, dentro de Cl.27), pero **el tracker no es confiable como instrumento de monitoreo**: no refleja el cambio de los tubos de presión post-ASME (su dato más importante), mantiene status ambiguos (E con PO cargada) que tocan el pago del 15%, y está estático semana-a-semana. Los tres focos de riesgo —vessel (dato obsoleto), Fedco (anticipo 30% + ventana 6 d) y PLC Panel (enclosure sin definir)— concentran la exposición al EXW 15-Ago.
