# Correo — Bureau Veritas: Plan de inspección de taller (Penang) por semanas

**Estado:** BORRADOR (21-Jul-2026)
**Fecha:** 21-Jul-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Luis Rodrigo Arcila Quezada (Bureau Veritas Chile, Luis.arcila@bureauveritas.com)
**CC:** Mohd Adnin Zulkifli + Lokman Hakim Mat (QAQC Penang) + Magdier Arias + Eduardo Yamauchi + Stephane Gehant (BW Water) + Victor Gutierrez / Jorge Guevara / Ronald Pellejero (ADASA)
**Cadena:** correo NUEVO (asunto propio "Taltal SWRO Module - Weekly Shop Inspection Plan at Penang"), NO reply al hilo de BW Water (BV no está en ese hilo; evita arrastrarle el historial interno de BW).
**Script:** `crear_correo_bv_weekly_inspection.py` · **Output:** `2026-07-21_BV-Weekly-Inspection-Plan.docx`

## Cuerpo (resumen)

Correo conjunto ADASA→Bureau Veritas copiando al equipo QAQC de Penang de BW Water. **Apertura en primera persona:** Luis escribe para *conectar* a Bureau Veritas con el QAQC de Penang (Mohd Adnin / Lokman) y que coordinen la inspección directo (saludo a los tres). Presenta el plan de inspección de taller **por semanas** (no por día, como el correo anterior del 18/20-Jul): 6 semanas de vigilancia de calidad + la semana de FAT, con **3 visitas por semana** en las de vigilancia (6×3 = 18 QAQC + 7 FAT = 25 jornadas, oferta BV 600049 Rev 2). Tabla semanal (Week / Window / Weekly milestone / Visits) con el alcance de cada semana per NT-002 Section 3.2:

- W1 (27-31 Jul): spools SDX/SS316, PMI SDX, calificación soldadores, VT welds, recepción de material.
- W2 (3-7 Ago): NDE (RT/PT/UT) de welds HP, dimensional del skid.
- W3 (10-14 Ago): hidrostática LP + HP 135 bar (Hold), RO vessel (Hold), coating DFT.
- W4 (17-21 Ago): coating estructura, ensamble final de cañería e instrumentos, DFT final.
- W5 (24-28 Ago): posicionamiento de equipos en contenedor, alineación cañería HP.
- W6 (31 Ago-4 Sep): CSC container, posicionamiento/alineación bomba HP + turbos (llegan ~2 Sep), inicio integración/terminación del panel.
- FAT (~7-12 Sep): procedimiento, visual, dimensional, dry functional, PLC/HMI + fault sim, SEC, UT HP, ADASA FAT Certificate, packing, Dispatch Release (7 jornadas).

Las fechas-día exactas dentro de cada semana las fijan las notificaciones formales Hold/Witness del taller (BAE Clause 37). Coordinación (3 puntos): (1) BV confirma movilización Semana 1 (firme) + disponibilidad hasta el FAT (jornada lun-jue); (2) el equipo de Penang confirma preparación semana a semana y cursa las notificaciones H/W; (3) kick-off BV+ADASA+BW antes de la Semana 1.

## Verificación de fuentes

- **Contactos QAQC Penang** VERIFICADOS del correo de Magdier Arias (21-Jul 10:33), `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/RE_ Taltal ... _ Luis Rivera - Outlook.pdf`: Mohd Adnin Zulkifli (Senior QAQC, MohdAdnin.Zulkaflee@bw-water.com), Lokman Hakim Mat (Project Engineer, lokmanhakim.mat@bw-water.com).
- **Destinatario BV** (Luis Arcila) y oferta 600049 Rev 2 (25 jornadas = 18 QAQC + 7 FAT): correo del 14-Jul `CORREOS/Julio 2026/2026-07-14/` + oferta en `HITO BUREAU VERITAS/oferta rev 2/`.
- **Alcance semanal** per NT-002 Section 3.2 (`REVISIONES/NOTAS_TECNICAS/P22-NT-09-000-002-0...`).
- **Programa sin cambios**: verificado contra el paquete Week 29 (20-Jul, `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 20-07-26/`) vs la referencia fija del 14-Jul → ninguna ventana V1-V6/FAT se movió; bomba HP + turbos siguen llegando 2-Sep.

## Contexto Interno (No enviar)

- **Cambio de postura registrado:** este correo UNE a Bureau Veritas y BW Water en el mismo hilo, abandonando la separación previa (no nombrar a BW Water a BV, ver `feedback_bv_no_nombrar_bw_water`). Es deliberado: el inspector debe coordinar directo con el QAQC de Penang. Por eso aquí SÍ se nombra a BW Water (está copiada).
- **Por qué semanas y no días:** decoupla del baile de fechas-día (BW puso V5/V6 en 09-Sep y el FAT 16-18 Sep en su calendario H/W; ADASA lo objetó). Definir la actividad de la semana + 3 visitas/semana deja que el día exacto flexione dentro de la semana vía las notificaciones H/W, sin re-litigar cada fecha.
- **Banderas de riesgo vivas (Week 29, no mueven fechas aún):** bomba HP FEDCO en estatus D (reposición de caja de bornes, sigue 2-Sep); spools y estructura del skid 0% al 20-Jul; Project Schedule revisado pendiente 23-Jul. La confirmación de V2-V6 a BV se comprometió para el **Vie 24-Jul** (tras el weekly del 21-Jul + calendario H/W).
- **No citado a BV:** jornadas/costos de la oferta (solo la referencia 600049); el enlace del hito de pago 40% (relación ADASA-BW) — el Dispatch Release va solo como Hold Point del ITP.
- Los 3 procedimientos Code 3 (009/010/011) se mantienen en el hilo de BW Water; no se arrastran a este correo de BV.

## Checklist pre-envío

- [ ] To = Arcila (BV); CC con los 2 contactos de Penang + Magdier/Eduardo/Stephane (BW) + ADASA
- [ ] Asunto propio (correo nuevo, no reply al hilo de BW)
- [ ] Tabla de 7 filas; "3 visits" en semanas de vigilancia; "7 days" en FAT
- [ ] 100% inglés; sin em-dash; sin símbolo de sección; sin IDs internos; sin jornadas/costos BV
- [ ] Metadatos Word limpios (autor Luis Rivera Gonzalez / Aguas de Antofagasta / en-US)
- [ ] Adjuntar (opcional) el calendario/tabla de referencia si se desea
- [ ] Tras envío: BORRADOR → ENVIADO, respaldo PDF/.msg, actualizar README
