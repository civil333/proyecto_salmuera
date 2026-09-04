# Correo — PLC/LCP Panel Recovery Plan: ADASA Response

**Estado:** ENVIADO (21-Jul-2026)
**Fecha:** 21-Jul-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water)
**Cadena:** **Reply-To** al thread "25007 Taltal: PLC/LCP Panel Delivery - Notice of Delay" (respuesta de BW del 20-jul 20:47, con las contestaciones de Billy Tan en azul). Cadena SEPARADA del correo de packing/EXW del mismo día.
**Script:** `crear_correo_plc_recovery_response.py` · **Output:** `2026-07-21_PLC-Panel-Recovery-Response.docx`

## Cuerpo (resumen)

Acusa el recovery plan del 20-jul como información y **mantiene expresa la reserva de responsabilidad/EOT** del correo del 07-jul: BW no aportó base que rebata el fundamento documentado (NEMA 4X/IP66 fijado por el propio LCP Datasheet aprobado P22-ET-09-007-005 Rev 1, no un requisito nuevo de ADASA). Tres puntos:

1. **Fecha única (no cumplido por BW):** el plan trae dos secuencias que no reconcilian entre sí ni con el marco 10/14/28-ago del 07-jul — (a) power-ON 5-ago, listo a embarcar 7-ago, Malasia ~21-ago, taller BW 23-ago; (b) terminación 24-ago, FAT taller 26-ago→5-sep, embalaje 6-sep, listo 7-sep. Se pide UNA secuencia integrada y fechada (dispatch enclosure → llegada Malasia → inicio taller → ventana FAT → panel completo → entrega a ensamble del módulo), una fecha comprometida por hito, que reemplace las dos líneas paralelas.
2. **FAT seco (Penang) vs aceptación funcional en sitio (Taltal):** se CONCUERDA con BW que el FAT es en seco — es lo que la ET pide (Section 8 - FAT: pruebas funcionales en seco + simulación de control PLC/HMI, disparo de bomba *simulado*) — y que el ensayo con agua (bomba HP bajo carga, performance del RO) es del **comisionamiento y las Pruebas de Desempeño en Taltal** (ET Section 9 y Section 10.2; ITP Rev 0 aprobado P22-BA-09-000-004, Section 10 - Commissioning y Section 11 - Performance Tests). Sobre esa base ADASA exige: (a) ejecutar el FAT seco completo per el ITP (dry functional + simulación PLC/HMI, incluido el disparo de bomba simulado) y registrarlo en el FAT report; (b) llevar al comisionamiento/Performance Tests de sitio los ítems que un FAT seco no puede cerrar (trips de devanado/rodamiento del motor, trip de vibración de la bomba HP, lazo cerrado de secuencia de control: rampa VFD, lazo de presión, bypass del turbo), sin cerrarlos en el FAT — el FAT Procedure detallado y el Performance Test procedure de sitio (ambos a aprobación de ADASA per el ITP) deben reflejar ese split; (c) el FAT y el Dispatch Release NO constituyen aceptación funcional/de desempeño — ésta queda en la prueba de 2 días en sitio, mandatoria para la Recepción Provisional. Nota de redacción: los tests se nombran por su función; sin la palabra "letter/carta" (solo emails/NT/RFI); sin IDs internos (OBS/NOTE/Code/TM).
3. **RFS del módulo:** BW concede que el RFS 12-sep excluye la bomba HP y que la fecha final depende de la entrega de la bomba. Se pide la fecha de RFS del módulo **inclusiva de la bomba** y mantener panel y bomba/turbos como líneas separadas; el recovery del panel no restaura por sí solo la fecha del módulo mientras los long-lead gobiernen.

## Verificación de fuentes

- Contenido del correo entrante VERIFICADO por extracción directa del PDF `CORREOS/RESPUESTA CORREO PLC-LCP PANEL DELIVERY.pdf` (texto en azul de Billy Tan = respuestas del proveedor). Las tres secuencias/fechas citadas son verbatim del azul.
- Correo original de ADASA (07-jul) VERIFICADO: `CORREOS/Julio 2026/2026-07-07/crear_correo_plc_delay_response.py` + `..._Descripcion.md`.
- LCP Datasheet Rev 1 = Código 1 en TM N25 (memoria `project_tm25_state`, `reference_et_tableros_nema4x_no_ss316l`). ET P22-ET-09-000-001-0 Section 5.4.1 (NEMA 4X) como soporte; NO se afirma requisito ET de material (CLAUDE.md 7.6; la ET Section 5.4.3 permite acero pintado).

## Contexto Interno (No enviar)

- Objetivo procesal: que BW no consolide el atraso como EOT atribuible a ADASA (BAE / origen del cambio = desviación del Outline propio de BW). BW guardó silencio sobre el frente de responsabilidad → la reserva queda sin rebatir; se deja constancia explícita para no perder ese punto por omisión.
- **Recalibración del "peligro" (corrección del usuario):** el FAT seco NO es una imposición de BW — es lo que la ET pide (Section 8) y el ensayo con agua es del SAT en Taltal (ET Section 9/10.2 + ITP Rev 0 Section 10-11), lo correcto y la única vía dada la secuencia de montaje. El riesgo real NO es el FAT seco, sino (i) que no quede amarrado el alcance/criterios del ensayo de sitio y (ii) que el FAT / Dispatch Release / hito de pago 40% se tomen como aceptación funcional. Por eso el correo concuerda con el split y reserva que FAT/Dispatch ≠ aceptación. Bureau Veritas atestigua el FAT **seco** en Penang (per NT-002); el ensayo con agua lo atestigua ADASA en Taltal (ITP Rev 0 Section 11, Witness/Hold).
- **Mapa de trazabilidad (impacto sobre comentarios emitidos por transmittal):**
  - **CERRADOS — la respuesta NO los reabre** (son la defensa contra el EOT): enclosure IP55→NEMA 4X/IP66 (Outline P22-CD-09-008-001 Rev C, Code 2 en N27, gate resuelto vía RFI-002); material SS316L exterior + gland plates / internos galvanizados aceptados (RFI-002); HART (cerrado como over-reach en Sección 3 N24, DS PLC&HMI Rev C Code 2 en N26); LCP Datasheet P22-ET-09-007-005 Rev 1 Code 1 en N25.
  - **IMPACTADOS por el FAT seco — cierre diferido de FAT a SAT (ITP Rev 0 Section 10-11, no NT-002):** la condición de firma de las pruebas RTD del FAT Procedure Hardware Rev A (P22-PP-09-000-001, Code 2 en N27, ya condicionada a CP Rev 0) y la familia de Control (CP / Alarm & Interlock List / Sequence Chart / IO List, todos Code 2 en N28, pendientes de Rev 0 coordinada). El FAT seco no puede verificar físicamente el trip winding/bearing, el trip de vibración "Stop HP Pump" (VIT-09-001) ni la lógica de secuencia/lazo de presión → se difieren al comisionamiento y Performance Tests de sitio (ITP Rev 0 Section 10 - Commissioning y Section 11 - Performance Tests), no se cierran en el FAT.
  - **Anclaje contractual correcto:** el ensayo con agua/running de la bomba NO va en Penang (per ET Section 8, FAT seco); va en Taltal per ET Section 9/10.2 e ITP Rev 0 Section 10-11 (con Hold de ADASA sobre el procedimiento 11.1 y el informe final 11.5). La prueba running de la bomba en fábrica FEDCO (EE.UU.) — que ADASA declinó atestiguar — entra al dossier (correo 20-Jul). **Apalancamiento:** el FAT Procedure de sistema/software detallado y el Performance Test procedure de sitio siguen pendientes de aprobación de ADASA (Hold ITP 7.1 y 11.1) — ahí se fija el split seco/húmedo antes de que ocurran.
- Las dos líneas de tiempo contradictorias probablemente mezclan la ruta del enclosure/System Integrator (KVC) con la del taller BW; no asumir cuál es la buena — exigir la reconciliación a BW, no interpretarla nosotros.
- Enviar como Reply-To a la cadena del panel; NO fusionar con el correo de packing/EXW (cadena separada, CLAUDE.md 3.3.1/3.4).

## Checklist pre-envío

- [x] To/CC: enviado como **reply-all al hilo** → CC = solo los 8 de BW Water (Jeryl, David Chee, Nick Huta, Billy Tan, Lokman, Sadeep, Elaine, Stephane). **Los CC internos ADASA (Victor Gutierrez, Ronald Pellejero) que agregaba el borrador NO quedaron en el envío** (el hilo entrante no los tenía). Si se requiere visibilidad interna, reenviar por separado.
- [ ] Asunto exacto "RE: 25007 Taltal: PLC/LCP Panel Delivery - Notice of Delay"
- [ ] 100% inglés; sin símbolo de sección; sin Van Doorn ni códigos internos OBS/Code
- [ ] `anti-ia revisar` sin frases-firma prohibidas
- [ ] Metadatos Word limpios (autor Luis Rivera Gonzalez / company Aguas de Antofagasta / en-US)
- [x] Tras envío: BORRADOR → ENVIADO (21-Jul-2026, 10:20; martes); README actualizado; **respaldo archivado**: `Elementos enviados_ Luis Rivera Gonzalez - Outlook.pdf` (cuerpo coincide verbatim con el borrador).
