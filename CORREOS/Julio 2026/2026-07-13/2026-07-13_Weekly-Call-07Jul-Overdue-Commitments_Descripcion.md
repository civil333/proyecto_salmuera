# Correo — Weekly Call 07-Jul-2026: Overdue Commitments and Record Corrections

**Estado:** ENVIADO 13-Jul-2026 | **Fecha:** lunes 13-Jul-2026 (día verificado) | **De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water)
**CC:** Victor Gutierrez (ADASA); Jeryl F. Regulacion, Adzlan Bin Abd Rahim, Nick Huta, Sadeep Irugalbandara, Stephane Gehant, Lokman Hakim Bin Mat (BW Water)
**Cadena:** Reply-All al thread *"25007 Project Taltal - Weekly Coordination Call - Notes 07-Jul-2026"* (07-Jul, 16:13). **Separada** del TM N27 (mismo día, cadena regular de transmittales).
**Script (cuerpo):** `crear_correo_minuta_07jul_followup.py` → `2026-07-13_Weekly-Call-07Jul-Overdue-Commitments.docx`

---

## Qué exige (4 bloques)

1. **Acuse.** Recibidas E63 (10-Jul) y E64 (13-Jul), 6 docs → disposición en el TM N27. ADASA cerró sus 3 acciones el día de la reunión (RFI-002, posición del atraso del panel PLC, NT de inspección de tercero P22-NT-09-000-002-0).
2. **Repuestos — no recibidos en 4,5 meses.** 3 compromisos de BW incumplidos (16-Jun, 30-Jun, 10-Jul). Exige: mandatoria (USD 17.310, ya contratada) **separada** de la recomendada 2 años (USD 43.790 EXW); kits de turbocharger SIP-09-001/002 (ausentes desde el origen); validez de precios. **Enviar HOY con lo que tengan** (preliminar/presupuestario donde falte cotización firme), para incorporar el costo al presupuesto del proyecto; balance con fecha firme a seguir. **Deadline: fin de jornada de HOY, lunes 13-Jul.**
3. **Otros vencidos del 10-Jul.** I/O List, cronograma actualizado (~12-Sep), weekly fabrication report, document status report + los 4 entregables de ingeniería que el TM N27 reitera. **Deadline: viernes 17-Jul.**
4. **Correcciones de registro.** (a) Rechaza la causa "cambio a NEMA 4X" del atraso del panel → carta del 07-Jul. (b) FAT 10→5 días no acordado; confirmación escrita pendiente. (c) Sitio del FAT Fedco al 17-Jul (bloquea a los inspectores de BV). + Reclama las 2 acciones que el acta de BW omite (layouts + modelo 3D; anclaje sísmico al frame).

---

## Verificación de fuentes

| Afirmación del correo | Fuente verificada |
|---|---|
| E63 recibida 10-Jul (HP/LP Rev C + Painting Rev B) | `Submittal Form_25007-0063.pdf`, Issue Date 10-Jul-26 |
| E64 recibida 13-Jul (RO Vessel Hydro Rev C, O&M Rev A, PLC/LCP FAT Rev A, Outline Rev C) | `Submittal Form_25007-0064.pdf`, Issue Date 13-Jul-26 |
| Nada más llegó entre el 08 y el 13-Jul | Barrido de archivos por fecha de modificación |
| "to be released next Monday" | `MINUTA DE REUNION 16-06-26_extracted.md` |
| "submit the complete two-year spare parts package by 03-Jul-2026" | `MINUTA DE REUNION 30-06-26.pdf` (verbatim) |
| "waiting for final quotations" / "I/O List (target July 10)" / FAT 10→5 / causa NEMA 4X / FAT en FEDCO y Penang | `MINUTA DE REUNION 07-07-26 (OFICIAL BWWATERS).pdf` |
| USD 17.310 (mandatorios) y USD 43.790 EXW (2 años) | `OFERTA ECONOMICA BW WATER_extracted.md` |
| Solicitud original 26-Feb + kits de turbocharger nunca incluidos | `CORREOS/Febrero 2026/2026-02-26/...Turbocharger-Kits.md` |
| El FAT 10→5 ya se cuestionó por escrito el 07-Jul | `CORREOS/Julio 2026/2026-07-07/crear_correo_plc_delay_response.py`, punto b) |

`anti-ia revisar`: **VERDE, 5%** (sin fingerprints tras corregir 3 repeticiones U-09).

---

## Contexto Interno (No enviar)

**Por qué el correo, y por qué separado del TM N27.** El acta oficial de BW (07-Jul) no asigna un solo responsable y borró las 4 acciones que más le exigen (repuestos con separación de mandatorios, layouts + 3D, anclaje sísmico, RFI-002); introdujo 2 que le favorecen (causa NEMA 4X, FAT 10→5). **Callar la causa NEMA 4X = dejar en pie la base de un claim de extensión de plazo.** Ese es el fondo de las correcciones de registro.

**Trampas evitadas (anti-invención):**
- Painting Rev B **sí llegó** el 10-Jul (E63) → no se reclama.
- IP estática del PLC es **acción de ADASA** (Data Transfer List P22-LI-09-008-004 Rev 1, 192.168.0.1 / ADASA = Modbus master) → no se le imputa a BW.
- FAT 10→5 **no es frente nuevo**: la carta del 07-Jul ya pidió confirmación de alcance → se trata como pendiente.
- Repuestos citados **por nombre + monto**, no por sección: la oferta los numera 3.12/3.13; los correos 26-Feb/26-Mar citaron mal "3.8" (si hay que citar, usar 3.12/3.13).

**Riesgo de alcance (BV).** BW declara FAT "at FEDCO **and** Penang" (2 sitios), ubicación sin confirmar. Bureau Veritas se contrató asumiendo Penang → un segundo sitio es costo/alcance extra, no presupuestado.

**Pendiente antes de enviar:**
- Confirmar que el **TM N27 sale primero o el mismo día** (el correo lo referencia 2×; si se posterga, cambiar a "our review of submittals 0063 and 0064 is in progress").
- Verificar la lista de CC contra el thread real de Outlook.

**Post-envío:** `Estado` → ENVIADO en este archivo; respaldo (PDF de "Elementos enviados" o `.msg`) en la carpeta; actualizar README.
