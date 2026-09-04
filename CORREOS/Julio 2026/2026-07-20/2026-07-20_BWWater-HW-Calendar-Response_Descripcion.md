---
titulo: "Correo ADASA → BW Water — Revisión del calendario Hold/Witness de inspección BV"
codigo: "Correo de coordinación (sin código ADASA)"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-07-20
---

# Correo — Revisión del calendario Hold/Witness de BW Water (inspección Bureau Veritas)

**Estado:** ENVIADO (20-Jul-2026)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi, Magdier Arias, Stephane Gehant (BW Water)
**CC:** Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero (ADASA)
**Cadena:** reply-all al thread "RE: Taltal - Designation of Third-Party Shop Inspector and Inspection Schedule" (reply de Yamauchi del 15-Jul que suma a Magdier Arias). Cadena separada de los TM y de la réplica a la minuta 07-Jul. Inglés.
**Script:** `crear_correo_bv_calendar_bwwater.py` · **Output:** `2026-07-20_BWWater-HW-Calendar-Response.docx`

## Cuerpo (resumen)

Acusa la incorporación de Magdier Arias (Quality Manager de BW Water) y la recepción del calendario consolidado de Hold/Witness points (Excel "TALTAL Witness and Hold point plan date", creado por Mohd Adnin Bin Zulkaflee el 15-Jul). Confirma V1–V4 alineadas con las ventanas de la NT-002 y las toma como base para movilizar al inspector. **Adjunta el Recovery Schedule / Progress Update de BW Water del 14-Jul y lo declara como referencia fija y vinculante ("inamovible"): sus fechas de fabricación, FAT y despacho se toman como firmes y no deben seguir corriéndose, y el calendario H/W y la movilización del inspector quedan ancladas a él** (postura anti-slip). Abre 6 solicitudes, medidas contra ese programa fijo: (1) ubicar V5 y V6 en el programa fijo (ambas puestas en 09-Sep, pese a que el posicionamiento corre de mediados-Ago a inicios-Sep); (2) alinear el FAT al programa fijo (el calendario pone 16–18 Sep; el programa fijo cierra el FAT del sistema el 08-Sep con ready-to-ship 09–10 Sep) + fecha de Dispatch Release (Hold que gatilla el 40%) + que la reducción 10→5 días preserva el alcance mínimo del FAT; (3) **posición ADASA sobre atestiguamiento** — Bureau Veritas atestigua el FAT solo en el taller de Penang; ADASA NO asiste a ninguna prueba de bomba/turbos en la fábrica FEDCO (EE.UU.); a cambio, BW Water debe incluir todos los registros y certificados de las pruebas FEDCO en el dossier de entrega del equipo, junto con el resto de la documentación; (4) confirmar la Kick-off Meeting; (5) emitir las notificaciones formales H/W (BAE Cláusula 37, aviso 30 días — V1 el 28-Jul ya dentro de ventana); (6) reemitir los 3 procedimientos en Código 3 (009/010/011) antes de las ventanas de presión y pintura de mediados-Ago. Cierra: revisión en la weekly del 21-Jul y confirmación de movilización sobre esa base.

Formato: apertura + tabla de reconciliación de 7 filas (Visit / Scope / Planned date / ADASA note) + 6 solicitudes numeradas + cierre. Sin tablas de severidad, sin veredictos Code (es coordinación, no transmittal).

## Verificación de fuentes

- **Calendario H/W:** `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/TALTAL Witness and Hold point plan date.xlsx` (creator Mohd Adnin Bin Zulkaflee, 15-Jul). Las 7 fechas del correo == columna "Plan Inspection Date"; V1–V4 == ventanas NT-002.
- **Reply de BW Water:** `HITO BUREAU VERITAS/RE: Taltal - Designation of Third-Party Shop Inspector and Inspection Schedule.pdf` (Yamauchi 15-Jul, suma a Magdier Arias).
- **Programa BW Water 14-Jul:** `SEMANA 13-07-26/md/` (Recovery Schedule/Progress Update, Week 28, DDSR) + `ZIP_EXTRAIDO/Procurement tracking - BW Water 2906.xlsx`. Verificado: bomba HP + Feed/Interstage Turbo (Fedco, US) EAP Penang ~02-Sep (tracker filas 1/12/16; schedule tareas 221–232), install bomba 03-04 Sep (tarea 379); FAT del sistema (tarea 385) 24-Ago→08-Sep, System ready to ship (387) 09-10 Sep; LCP panel ex-work China 09-23 Ago (tareas 357/358).
- **NT / ITP:** NT P22-NT-09-000-002-0 (enviada 08-Jul); ITP P22-BA-09-000-004 Rev 0 aprobado (TM N26). Los 3 procedimientos: 009/010 Code 3 en TM N26, 011 Code 3 en TM N23.
- **Días de la semana:** 20-Jul = lunes, 21-Jul = martes, 28-Jul = lunes (verificados).

## Contexto Interno (No enviar)

- **Linkage con BV:** a BV (correo 14-Jul) se prometió V2–V6 "puede variar en días" y confirmación final el 24-Jul. V5/V6 a 09-Sep NO es variar en días (salto ~2 semanas + fusión de dos visitas) → obliga a re-planificar el booking del inspector y ajustar la confirmación del 24-Jul. El FAT 16–18 Sep sí cae dentro de la banda 14–19 Sep ya anunciada a BV.
- **FAT muestra 3 días** (16-17-18 Sep) vs **7 jornadas de FAT** contratadas a BV (oferta 600049) — se pregunta duración/alcance sin exponer el dato comercial de BV.
- **Slip fresco vs el plan interno 07-Jul:** V5/V6 y FAT corridos ~1 semana más; el skid (mild steel) sigue 0% sin PR/PO, gated por el cálculo sísmico aún Code 3 (P22-CD-09-005-001 Rev B).
- **RO Vessel hydro "DONE at factory":** el vessel (Protec Arisawa, España) llegó Penang 04-Jul con hidrostática hecha → el procedimiento 009 gobierna una prueba ya ejecutada (se necesita aprobado + registros para aceptación, no atestiguamiento). No se detalla en el correo.
- **Bombas CIP (NTK):** aéreo directo a sitio 02-13 Sep, no a Penang → fuera del FAT testificado (gap de alcance interno; no se comunica aquí).
- **Posición FEDCO (decisión del usuario 18-Jul):** ADASA solo participa del FAT en Penang con Bureau Veritas. Si las pruebas de la bomba/turbos FEDCO son en EE.UU., ADASA NO las atestigua; a cambio se exige toda la documentación de las pruebas FEDCO en el dossier de entrega del equipo. En el correo el punto 3 pasó de pregunta a declaración de posición + solicitud de dossier.
- **Cadenas separadas:** la posición contractual del atraso PLC y la disputa FAT 10→5 días viven en la réplica a la minuta 07-Jul (ENVIADA 13-Jul). Aquí el frente FAT 10→5 se encuadra como **pregunta de coordinación del calendario** (no reapertura de multas/extensión), por decisión del usuario de sumarlo.
- **Regla "no nombrar a BW Water":** NO aplica aquí (correo ES a BW Water); sí aplica en correos a BV.

## Checklist pre-envío

- [x] `anti-ia revisar` (VERDE ~5%, sin correcciones; em-dash solo en cabecera/firma)
- [x] Metadatos Word limpios: creator/lastModifiedBy "Luis Rivera Gonzalez", company "Aguas Antofagasta", language en-US, Application "Microsoft Office Word"
- [x] Barrido `§`/Van Doorn sobre `.py` = 0
- [x] Coherencia fechas: 7 filas == "Plan Inspection Date"; cifras del cuerpo == Recovery Schedule 14-Jul
- [x] Visto bueno del usuario al borrador
- [x] Render de control (revisor-docx) de la tabla
- [x] Confirmar destinatarios/emails exactos en Outlook (reply-all al thread)
- [x] **ENVIADO 20-Jul-2026**; pasar `BORRADOR` → `ENVIADO` hecho; README + memoria `project_bureau_veritas_inspection` actualizados. Pendiente: dejar respaldo (PDF/.msg) del envío en la carpeta

## Compromiso generado

Tras la respuesta de BW Water (calendario reconciliado + Kick-off + notificaciones H/W) y la weekly del 21-Jul, **ADASA envía a BV la confirmación final de V2–V6 el viernes 24-Jul-2026**.
