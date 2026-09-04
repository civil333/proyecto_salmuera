# Correo — PLC/LCP Panel Delay: ADASA Position (respuesta al Notice of Delay)

**Estado:** ENVIADO (07-Jul-2026) — respaldo PDF en la carpeta
**Fecha:** 07-Jul-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water)
**Cadena:** **Reply-To** al thread "25007 Taltal: PLC/LCP Panel Delivery - Notice of Delay" (correo de Eduardo del 07-jul 00:35). Cadena SEPARADA de la NT de BV.
**Script:** `crear_correo_plc_delay_response.py` · **Output:** `2026-07-07_PLC-Panel-Delay-Position.docx`

## Cuerpo (resumen)

Acusa recibo del Notice y **reserva la posición de ADASA sobre la responsabilidad del atraso**. No acepta el encuadre "NEMA 4X = requisito nuevo de ADASA". Lidera con la contradicción vs el **documento aprobado de BW Water**: el LCP Datasheet P22-ET-09-007-005 Rev 1 especifica "nVent Hoffman Type FS FS66S, NEMA 4X/IP66"; el IP55 del Outline Rev A fue desviación de ese datasheet. Cita la ET P22-ET-09-000-001-0, Section 5.4.1 - Constructive Characteristics (NEMA 4X) como soporte, sin afirmar requisito ET de material. "Mínimo IP54" del TM N15 = piso, no techo.

Referencia además la **respuesta a la RFI-002 (25007-RO-RFI-0002) enviada el mismo día** (material del enclosure clarificado: exterior SS316L, internos galvanizados aceptables, Outline a reemitir en NEMA 4X/IP66) → refuerza que el requisito estaba en el datasheet aprobado desde siempre. Solicita, anclado a las cifras del Notice de Eduardo: (a) plan de recuperación reconciliando panel listo 10-ago vs completion 14-ago vs Malasia 28-ago, con fecha única; (b) confirmar que el FAT reducido de 10 a 5 días útiles mantiene el alcance completo; (c) impacto reconciliado sobre módulo listo (forecast 12-sep) + interacción con la HP Pump/turbos en ruta crítica (el recovery del panel no restaura la fecha del módulo si la bomba sigue gobernando), con cross-reference a la NT P22-NT-09-000-002-0.

**Verificación de fuentes (07-jul):** el spec del datasheet está VERIFICADO contra `ENTREGAS_BWWATER/ENTREGA 56/md/P22-ET-09-007-005_1...` (Rev 1, Código 1 en **TM N25**; en TM N24 fue Rev 0 Código 2): "Manufacturer nVent-Hoffman / Model Type FS FS66S series / Protection Category NEMA 4x, IP66". El verbatim del SLD ("METAL CLAD, NEMA4X/IP66") NO se pudo confirmar (el SLD P22-CD-09-007-01_B es un plano; su extracción no contiene esos términos) → se **eliminó** del correo; D3 se apoya solo en el datasheet aprobado. Si se quiere reincorporar el SLD, verificar el verbatim abriendo el plano.

## Contexto Interno (No enviar)

- Base de la refutación en memorias `reference_et_tableros_nema4x_no_ss316l`, `project_tm20_state`, `project_tm25_state`. El LCP Datasheet llegó a Rev 1 Código 1 (aprobado) en **TM N25** (en TM N24 fue Rev 0 Código 2) con NEMA 4X/IP66 → irrebatible.
- **Regla CLAUDE.md §7.6:** liderar con la contradicción de documentos aprobados; NO afirmar "la ET exige SS316L" (la ET §5.4.3 permite acero pintado). En el correo no se menciona material, solo el rating NEMA 4X/IP66 del datasheet aprobado y la ET NEMA 4X como soporte.
- Objetivo procesal: evitar que el Notice quede como precedente de atraso atribuible a ADASA (BAE Cláusula 43 multas; §9.1 origen del cambio = coordinación interna BW Water).
- Escrutinio del FAT comprimido (10→5 días) = insumo para que Bureau Veritas vigile la cobertura de los puntos ITP Sección 7.
- Enviar el mismo día que la NT de BV (cadenas separadas, cross-reference por código).
