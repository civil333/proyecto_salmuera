---
titulo: "Correo ADASA → BW Water — Respuesta a la invitación de FEDCO al pilot test"
codigo: "Correo de coordinación (sin código ADASA)"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: capture
type: correo
date: 2026-07-20
---

# Correo — Respuesta a la invitación de FEDCO al pilot test (bombas HP + turbos)

**Estado:** ENVIADO (20-Jul-2026)
**De:** Luis Rivera (ADASA) → **Para:** Eduardo Yamauchi (BW Water)
**CC:** Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero (ADASA) + Stephane Gehant (BW Water)
**Cadena:** Reply-To al thread "25007 Taltal: FEDCO - Pilot Testing" (correo de Yamauchi del 15-Jul-2026). Cadena propia, separada del calendario H/W, de los TM y del root-cause del atraso Fedco. Inglés.
**Script:** `crear_correo_fedco_pilot_reply.py` · **Output:** `2026-07-20_FEDCO-Pilot-Test-Reply.docx`

## Cuerpo (resumen)

FEDCO, vía Eduardo Yamauchi, invitó a Aguas de Antofagasta a asistir al pilot test de las bombas HP y turbocargadores en la fábrica de FEDCO (EE.UU.), "para dar visibilidad de la tecnología". ADASA declina: el atestiguamiento de ADASA, a través de Bureau Veritas, se limita al FAT en el taller de Penang; no se viaja a atestiguar pruebas de bomba/turbos en la fábrica FEDCO (EE.UU.). A cambio, se exige que toda la documentación de las pruebas de los equipos suministrados (protocolos de pilot y factory test, criterios de aceptación, resultados medidos y certificados) se incluya en el dossier de entrega del equipo, disponible para el inspector en Penang. Cierra "look forward to your comments". Transaccional, ~110 palabras, sin tabla.

**Consistencia (regla dura del usuario):** mismo lenguaje del punto 3 del correo del calendario Hold/Witness (borrador 20-Jul, `2026-07-20_BWWater-HW-Calendar-Response`): "Witnessing is limited to the Penang workshop" + "include the complete FEDCO test records in the equipment delivery dossier".

## Verificación de fuentes

- **Invitación FEDCO:** `PROGRAMA y CONTRATO/RESPUESTA DE FEDCO/25007 Taltal: FEDCO - Pilot Testing.pdf` (Yamauchi 15-Jul-2026; CC amplio del equipo de coordinación FEDCO de BW Water + Stephane Gehant).
- **Posición ADASA:** punto 3 del correo del calendario H/W (borrador 20-Jul) + memoria `project_bureau_veritas_inspection` + `project_fedco_fat_conflict_14may`.
- **Equipos FEDCO:** bomba HP BH-09-001, Feed Turbo SIP-09-001, Interstage Turbo SIP-09-002, fabricados en EE.UU., EAP Penang ~02-Sep (tracker 14-Jul).

## Contexto Interno (No enviar)

- El pilot test de FEDCO es demostración de tecnología en fábrica US, distinto del FAT integrado de aceptación (Penang). Declinar NO es desentenderse del equipo crítico atrasado: la mitigación es exigir toda la documentación + el witness del FAT integrado en Penang con Bureau Veritas.
- **Cadenas separadas (§3.4):** el atraso Fedco y su root-cause (bomba/turbos EAP Penang 02-Sep, anticipo 30% disputado, running-test-site Penang vs SAT) viven en el thread "Schedule Update" (correo root-cause ENVIADO 29-Jun). NO se mezclan aquí; este correo es solo la respuesta a la invitación del pilot test.
- Se envía el mismo día (20-Jul) que el correo del calendario H/W, pero en su propia cadena; cada correo es self-contained (no cross-referencia el documento del otro thread → evita el riesgo procesal de "referencia a un documento no recibido").
- Regla "no nombrar a BW Water": NO aplica (correo ES a BW Water).
- En la carpeta fuente hay también `Report - FEDCO - Delay Assessment.pdf` (contexto del atraso, no usado en esta respuesta).

## Checklist pre-envío

- [x] Metadatos Word limpios: creator/lastModifiedBy "Luis Rivera Gonzalez", company "Aguas Antofagasta", language en-US
- [x] Sin em-dash en prosa (5 em-dash, solo cabecera/firma); sin `§`
- [x] Coherencia de lenguaje con el punto 3 del correo del calendario
- [x] Render de control (1 página, layout OK)
- [x] Visto bueno del usuario
- [x] Confirmar destinatarios/emails en Outlook (Reply-To al thread del pilot test)
- [x] **ENVIADO 20-Jul-2026**; `BORRADOR` → `ENVIADO` hecho; README + memorias actualizados. Pendiente: dejar respaldo (PDF/.msg) del envío en carpeta
