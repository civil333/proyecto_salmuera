# Correo — Fechas de visitas de inspección en Penang para Bureau Veritas Chile

**Estado:** ENVIADO (martes 14-Jul-2026)
**Fecha:** 14-Jul-2026 (martes)
**De:** Luis Rivera (ADASA) → **Para:** Luis Rodrigo Arcila (Bureau Veritas Chile)
**CC:** Víctor Gutiérrez (ADASA)
**Cadena:** responde a la consulta de BV por las fechas oficiales de las visitas en Malasia (para reservar inspectores/pasajes). Idioma español, es-CL.
**Script:** `crear_correo_bv_fechas.py` · **Output:** `2026-07-14_BV-Fechas-Visitas-Penang.docx`

## Cuerpo (resumen)

Confirma la **Visita 1 (lunes 27 – viernes 31 de julio)** para movilización inmediata y entrega la tabla completa de ventanas V1–V6 + FAT. Las Visitas 2 a 6 van "Planificada — puede variar en días" (decisión del usuario 14-Jul: enviar el calendario completo indicando que puede variar, sin anticipar corrimientos semanales); la **confirmación final se compromete para el viernes 24-Jul** (cierre de la semana siguiente), tras revisar el calendario H/W que BW Water entrega el viernes 17-Jul (weekly del martes 21-Jul). Se declara que los ajustes esperados son del orden de días para cada visita de tres jornadas, no reprogramaciones de semanas. FAT: base 7–12 Sep con posible desplazamiento de una semana (14–19 Sep), porque la bomba HP y los 2 turbocargadores llegan a Penang el 02-Sep y las pruebas funcionales corren después de su instalación. **Regla del usuario (14-Jul): NO nombrar a BW Water en correos a BV** — se usa "el fabricante" / "taller de fabricación (Penang)"; verificado 0 menciones en el Word final.

## Verificación de fuentes

- Ventanas V1–V6 + FAT: NT P22-NT-09-000-002-0 (enviada a BW Water el 08-Jul-2026 17:39, `CORREOS/Julio 2026/2026-07-07/ENVIO ADASA POR BUREAU VERITAS.pdf`).
- Validación contra status update BW Water 14-Jul: `PROGRAMA y CONTRATO/REVISION SEMANAL PO EQUIPOS/SEMANA 13-07-26/md/` (Recovery Schedule 14-Jul, Week 28, DDSR 13-Jul, tracker procurement).
- Llegadas a Penang: bomba HP + turbos 02-Sep (tracker filas 1/12/16, schedule líneas 221–232); panel LCP 23-Ago (línea 354–358); spools SDX en taller desde 10-Jul (Week 28).
- Días de semana verificados: 17-Jul = viernes, 21-Jul = martes, 27-Jul = lunes.

## Contexto Interno (No enviar)

- **Solo V1 es firme.** El schedule 14-Jul corre estructura del skid a 8–15-Ago (PO aún pendiente de cálculo sísmico — tracker degradó frames de C a E), pintura a 17–24-Ago e hidrostáticas fuera de la ventana V3 anunciada (10–14-Ago): V3 se corre ~1 semana.
- **FAT:** el bloque FAT de BW Water en papel termina el 08-Sep con ex-works 09–10-Sep, pero con la bomba instalándose el 03–04-Sep quedan 3–4 días hábiles para un FAT testificado de 7 jornadas (oferta BV) — infactible. De ahí la banda 07–12-Sep base + desplazamiento a 14–19-Sep. NO se adelanta a BV la inconsistencia interna del schedule de BW Water; solo la banda de fechas.
- **Slips silenciosos detectados** (tracker 13-Jul vs 22-Jun, Change Log vacío): pump y 2 turbos 05-Ago→02-Sep (+28d); panel PLC 29-Jul→23-Ago (+25d); frames 01-Jul→20-Jul (+19d, C→E). Ex-works Penang 15-Ago (Recovery Rev A)→09/10-Sep (+26d); Performance Test termina 15-Dic (baseline 19-Nov).
- **Bombas CIP (NTK) van por airfreight directo a sitio (02–13-Sep), no a Penang** → fuera del FAT testificado; misma familia del gap del panel en KVC. Decisión de alcance pendiente (interno; no se comunica a BV en este correo).
- Costos/jornadas de la cotización BV no se mencionan (interno ADASA-BV ya conocido por ambas partes; el correo solo cita la referencia 600049).
- **Dos frentes abiertos con BW Water que impactan a BV y vencen el mismo 17-Jul** (réplica a la minuta del 07-Jul, ENVIADA 13-Jul): (a) BW Water declaró FAT de 10 → 5 días hábiles, NO acordado por ADASA (confirmación escrita pendiente de que el alcance completo se preserva); (b) sitio del FAT de la bomba Fedco sin confirmar ("at FEDCO and manufacturing in Penang" = 2 sitios) — BV fue contratado asumiendo Penang; un segundo sitio es alcance/costo adicional y bloquea la asignación de inspectores. Ninguno se adelanta a BV en este correo; ambos se resuelven en el mismo ciclo del 17/21-Jul.

## Checklist pre-envío

- [x] Visto bueno del usuario al borrador (14-Jul, con 2 ajustes: V2–V6 "puede variar en días" + confirmación final viernes 24-Jul; sin nombrar a BW Water)
- [x] `anti-ia revisar` aplicado (14-Jul: VERDE, checklist express; corregida repetición léxica "calendario" ×4 → ×3; em-dash solo en cabecera/firma, precedente aceptado)
- [x] Barrido "BW Water" sobre el Word final = 0 menciones
- [x] ENVIADO 14-Jul-2026 — README actualizado
- [ ] Pendiente: dejar respaldo del envío (PDF/.msg de Outlook) en esta carpeta

## Compromiso generado

**ADASA debe enviar a BV la confirmación final de las Visitas 2–6 el viernes 24-Jul-2026**, alimentada por el calendario H/W del fabricante (vence viernes 17-Jul) y la weekly del martes 21-Jul.
