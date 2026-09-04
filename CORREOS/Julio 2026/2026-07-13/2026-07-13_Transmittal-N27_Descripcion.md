# Correo de remisión — Transmittal N27 (re-escopeado E63+E64)

**Estado:** ENVIADO 13-Jul-2026
**Fecha:** 13-Jul-2026 (lunes)
**Cadena:** thread regular de transmittals (no Reply-To a un thread de proveedor)
**Archivo:** `2026-07-13_Transmittal-N27.docx` | Script: `crear_correo_tm27.py`
**Formato:** ejecutivo compacto (1 página, ~247 palabras). Lead con veredicto; safety item = única acción arriba en bold; cierres y pendientes en una línea cada uno; sin párrafos que dupliquen.

## Qué remite

Transmittal N27 (P22-TM-09-000-027-0) — **re-escopeado**: empezó como E63 (2 docs) en BORRADOR; al llegar la E64 (4 docs, 13-Jul) con el correo aún sin enviar se folded E64 en el N27 (no se abrió N28). Submittals 25007-0063 (E63) + 25007-0064 (E64), **6 documentos**.

**Veredicto: 3 — To Be Revised. Tally 5 Code 2 + 1 Code 3.**

| Documento | Rev | Code | Nota |
|-----------|-----|------|------|
| HP and LP Pressure Test Procedure | C | **3** | **Único driver.** Adjunta la Line List en vez de escribir la presión → ordena 75 bar sobre `DA-PVC-DN65-09-016` (PVC SCH 80 DN65, opera 1 bar). Re-issue Rev D; HP hidrostática Hold Point |
| RO Vessel Hydrostatic Test Procedure | C | **2** | Cierra el CRITICAL del N26: test report real a 91,01/136,52 bar (= 1,1× diseño), certs de calibración. Housekeeping: presión numérica en cuerpo + ventana de manómetro |
| Painting Procedure | B | **2** | Cierra N23 (equivalencia Jotun + C5-M); solo formulario de inspección |
| PLC/LCP Outline Panel Drawing | C | **2** | Resuelve el gate del enclosure (N20/N25): SS316L/NEMA 4X per RFI-002; hoja 5 material spec, hoja 14 CCS. Cable clamp TBC, fila MATERIAL, typos |
| PLC/LCP FAT Procedure - Hardware | A | **2** | Nuevo. Sólido; cobertura ET verificada vs IO List Rev 4 + Load List. Driver de la nota = planos gobernantes con código ET→CD |
| Operating and Maintenance Manual | A | **2** | Nuevo. Servible; CIP cross-ref, recovery 42/42,86, modelo membrana, boilerplate |

**6 CC_ADASA** (1 Code 3 + 5 Code 2, ningún Code 1). El Outline (plano A3) anotado con posicionamiento 2D explícito en la franja libre + verificación por render PNG.

## Escalación incluida (lo del párrafo "Outstanding")

Vencidos con deadline consolidado **viernes 17-Jul-2026** (RO Vessel Hydro y Outline ya NO están — llegaron en E64):
- Grounding Layout Rev F (venció 17-Jun)
- Tabla FAT/SAT (venció 15-Jun)
- Hijos del Control Philosophy (7º ciclo)
- 3 planos mecánicos de ruta (vencieron 26-Jun)
- UHPRO Structural Calc Rev B + GA Antiscalant Dosing Tank Rev C + Equipment Layout Rev D

## Contexto Interno (No enviar)

- **Los 2 gates que cierran** son la mejor noticia del ciclo: el paquete QA/fabricación del N23 (NDE en N26, RO Vessel Hydro + Painting aquí; solo HP/LP sigue) y el gate del enclosure del N20/N25 (Outline Rev C). El único Code 3 es el HP/LP (safety).
- **Over-reach corregidos por la verificación adversarial** (4 agentes, uno por doc E64, corridos ANTES de generar): (1) retirada la falsa bandera del "52 bar bajo" del O&M — es la descarga de la bomba HP + boost de turbo, correcto (Oferta opera ~53-54 bar; 120 bar = rating máximo de membrana, no operación); (2) NO afirmar qué manómetro midió el ensayo de 136,5 bar (el doc no mapea gauge↔vessel) → reformulado a "ninguno cae en la ventana 1,5×–4×"; (3) refutado el "reuso de tags" del FAT — son sufijos de tags compuestos únicos de la IO List (138 puntos verificados).
- **No reabrir lo concedido:** waiver ASME 02-Jun; soft-I/O Ethernet/IP aceptado en N20 (no exigir hardwire al RUNNING de dosificadoras); HART a nivel instrumento (no HART central en el PLC); internos galvanizados/CRS del enclosure aceptados en RFI-002.
- **Enmarcar el RO Vessel Hydro Code 2 como housekeeping**, NO como "CRITICAL aún abierto" (el CRITICAL está resuelto con evidencia).
- Cross-doc trackeados en Section 3: Line List reconciliada, **SLD a reemitir** (compromiso de BW en la hoja 14 del Outline), tabla de pernos de base (input fundación OOCC), Module Seismic Calc.
- El correo es 247 palabras (1 página) — formato ejecutivo (regla permanente, ver `feedback_correos_remision_ejecutivos`).

## Pendiente antes de enviar

1. **Reemplazar el link Synology** (`PENDIENTE_LINK_SYNOLOGY_N27`) en `crear_transmittal.py` y `crear_correo_tm27.py`, y regenerar ambos `.docx`.
2. **Entregar** los 6 CC_ADASA + el transmittal por el link Synology (o adjuntar si se decide directo).
3. Tras envío: marcar este `.md` como ENVIADO, dejar respaldo (PDF/.msg de "Elementos enviados"), actualizar README.
