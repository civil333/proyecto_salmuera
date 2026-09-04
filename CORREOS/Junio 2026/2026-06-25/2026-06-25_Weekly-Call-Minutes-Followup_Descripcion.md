# Descripción — Correo seguimiento minuta Weekly Coordination Call (25-Jun-2026)

**Estado:** ENVIADO 25-Jun-2026 (jueves) — respaldo `ENVIADO A BW WATERS.pdf` en la carpeta.
**Fecha:** 25-Jun-2026 (jueves)
**Tipo:** Follow-up / insistencia, corto, ejecutivo, inglés.
**Cadena:** Reply-All al thread "25007 Project Taltal - Weekly Coordination Call" (la call del martes 23-Jun). Cadena separada del thread "Meeting Notes" 16-Jun donde fue el correo de accountability del 22-Jun.
**Output:** `2026-06-25_Weekly-Call-Minutes-Followup.docx`
**Script:** `crear_correo_minuta_weekly_call_25jun.py`

## Destinatarios
- **To:** Eduardo Yamauchi, Jeryl F. Regulacion, Adzlan Bin Abd Rahim, Nick Huta, Sadeep Irugalbandara, Stephane Gehant, Lokman Hakim Bin Mat — BW Water Americas Inc.
- **CC:** Victor Gutierrez — ADASA

## Contexto Interno (No enviar)

El martes 23-Jun-2026 se realizó la Weekly Coordination Call. Luis pidió la minuta ese mismo día ("we look forward to receiving the minutes of today's meeting"). Al jueves 25-Jun no hay respuesta de Eduardo Yamauchi.

La minuta es el registro de dos compromisos que ADASA necesita por escrito y que son críticos en plazo:
1. **Cronograma ajustado** por el retraso de Fedco — re-secuenciado para absorber el slip de BH-09-001 (bomba HP) + SIP-09-001/002 (turbochargers).
2. **Reporte oficial, en formato de reporte**, del por qué y cómo ocurrió el retraso de Fedco, con las acciones de recuperación.

Por qué importa el reporte: BW Water maneja tres fechas distintas para los mismos equipos Fedco (tracker EAP Penang 05-Ago / Progress Report Week 25 completion 21-Ago / Project Schedule Rev A manufacturing finish 09-Ago), y la fecha de 21-Ago choca con el EXW Penang 14-15 Ago. El reporte debe cerrar esa contradicción y fundar el cronograma re-secuenciado.

## Decisión de diseño

El correo no solo persigue la minuta. Deja por escrito, dentro del propio hilo, los dos compromisos con su nombre y exige fecha de emisión comprometida. Así ADASA conserva el registro contractual aunque la minuta de BW Water se demore o no recoja esos puntos.

## Parámetros (confirmados con el usuario)
- **Plazo:** fecha firme — minuta para el viernes 26-Jun; confirmar fecha de emisión de cada entregable Fedco para el mismo 26-Jun. (26-Jun-2026 = viernes, verificado.)
- **Alcance:** foco — solo minuta + los 2 compromisos Fedco. NO se re-abren los pendientes del 22-Jun (spare parts quotes / ex-work details / invoice status), que viven en su propia cadena.

## Reglas aplicadas
- 100% inglés (BW Water). Sin proponer reunión. Sin referencias internas (§N / OBS / Code). Bold inline en sujetos clave. Sin emojis. Tono firme, no acusatorio.
- TAGs de equipos (BH-09-001, SIP-09-001/002) son tags BW Water compartidos — permitido citarlos.
- Em-dash solo en header/firma (etiqueta); cero em-dash en prosa. Ítems numerados con colon (estilo del correo 22-Jun).
- Verificación pre-envío: `anti-ia revisar` → VERDE. Metadatos Word limpios (docx_metadata).

## Post-envío
BORRADOR → ENVIADO en este .md; respaldo PDF/.msg en la carpeta; actualizar README.md (tablas de correos).
