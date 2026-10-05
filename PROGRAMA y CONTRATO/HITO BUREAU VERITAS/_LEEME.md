---
titulo: Mapa del frente Bureau Veritas — inspección de taller del módulo
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# Frente Bureau Veritas: inspección de taller en Penang

Domicilio único del frente desde el 5-Oct-2026. Antes vivía repartido en tres árboles que crecieron por hilo de correo: `REQUEST WITNESS INSPECTION/`, `PROGRAMA y CONTRATO/BV INSPECTION/` y esta carpeta. Los dos primeros se eliminaron tras moverse su contenido. Dónde quedó cada subcarpeta antigua está en `_historico/_EQUIVALENCIAS_RUTAS_ANTIGUAS.md`.

Bureau Veritas Chile es el tercero inspector contratado por ADASA (OC 836492, oferta 600049 Rev 3). La inspección la ejecuta la oficina de BV Malasia en el taller de BW Water en Penang, a pedido de BW Water mediante el formulario `AQ-QAM-F027` (Request to Witness Inspection, RWI).

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| `_ESTADO_OC_836492.md` | Jornadas contratadas contra ejecutadas, saldo, proyección al FAT y conciliación de facturación |
| `01 CONTRATO Y OC/` | `OC-836492.pdf`; correos de designación del tercero inspector (julio); `OFERTA 600049/` (Rev 0, 2 y 3); `CV INSPECTORES/`; `md/` con la OC y la oferta Rev 3 extraídas |
| `02 PLAN DE INSPECCION/` | Calendario de puntos Witness y Hold (`.xlsx`), captura de los documentos a enviar a BV, `PLAN_INSPECCION/` (plan de coordinación interno) y `_fuentes_guia_bv/` (script y fuentes de la guía del paquete) |
| `PAQUETE_INSPECCION_BV/` | **Lo que BV tiene en mano.** Publicado a Bureau Veritas por enlace Synology desde el 21-Jul-2026. **No se mueve, no se renombra y no se edita**: hacerlo rompe un enlace externo vivo. Una versión nueva de algo que esté ahí se deja aparte y se avisa |
| `03 SOLICITUDES BW (RWI)/` | Una carpeta por solicitud de BW Water, `RWI NNN AAAA-MM-DD`: formulario `AQ-QAM-F027` de cada día, firmado cuando existe, y el correo de solicitud |
| `04 INFORMES BV/` | `_REGISTRO_INSPECCIONES_BV.md` (todas las jornadas, resultado verificado por render, estado de los ensayos de presión). Una carpeta por informe, `IRNNN AAAA-MM-DD`, con el informe, su anexo, el registro de prueba del fabricante del mismo día y `md/`. `_render/` guarda las verificaciones visuales y `TESTING TRACKER 24-09-26/` el tracker de ensayos de BW |
| `05 CORREOS/` | Correos impresos que no son solicitud ni entrega de informe: `CORREOS VBV-BW/` (cadena del Request 001, julio), la discusión de presiones del 21-Ago, el set del 31-Ago tal como lo envió BV (RAR original y correo) y la respuesta de BW del 3-Sep con su Line List preliminar |
| `_analisis/` | Análisis internos del frente que no pertenecen a un solo informe |
| `_historico/` | El mapa anterior (`_ORIGEN.md`), la tabla de equivalencias de rutas y el registro archivo por archivo de la consolidación, con md5 de origen y destino |
| `_duplicados_payload_identico/` | Copias byte a byte iguales a una canónica y ZIP o RAR cuyo contenido ya está suelto, con `_MANIFIESTO.md`. No se borran |

## Solicitudes e informes

| RWI | Días | Informes BV |
|---|---|---|
| 001 | 28-Jul | `IR001` |
| 002 | 07-Ago | `IR002` |
| 003 | 13 y 14-Ago | `IR003`, `IR004` |
| 004 | 20 y 21-Ago | `IR005`, `IR006` |
| 005 | 24, 27 y 28-Ago | `IR007`, `IR008`, `IR009` |
| 006 | 2 al 4-Sep | `IR010`, `IR011`, `IR012` |
| 007 | 9 al 11-Sep | `IR013`, `IR014`, `IR015` |
| 008 | 17 y 18-Sep | `IR016` (un informe por dos jornadas) |
| 009 | 22 y 23-Sep | `IR017`, `IR018` |
| 010 | 8 y 9-Oct | pendiente |

Ojo con los asuntos de correo: BV Chile reutiliza la cadena `Request to witness inspection 006` para entregar informes de otros días, y titula con el número de informe (`… inspection 013`, `… 014`, `… 015`) correos que no corresponden a ninguna RWI de BW. El número de la RWI se lee en el formulario, no en el asunto.

## Cómo entra el material nuevo

- **Correo de BW Water o de Bureau Veritas:** se captura en `CORREOS/_RECIBIDOS/` (convención en su `_LEEME.md`, skill `correo-taltal`). El formulario de una RWI va a `03 SOLICITUDES BW (RWI)/`; el informe BV y su anexo, a `04 INFORMES BV/IRNNN AAAA-MM-DD/`, con una fila nueva en el registro; el registro de prueba que BW envía el mismo día va a la carpeta del informe de ese día, o queda en `adjuntos/` del correo hasta que el informe llegue.
- **Correos que envía ADASA sobre el frente:** viven en `CORREOS/<Mes AAAA>/<AAAA-MM-DD>/`, con su `_Descripcion.md`, y no se mueven. Los principales: `2026-07-07_Third-Party-Shop-Inspection-Notice`, `2026-07-14_BV-Fechas-Visitas-Penang`, `2026-07-21_BV-Weekly-Inspection-Plan`, `2026-07-25_BWWater-Inspection-Dossier-Request`, `2026-08-07_BV-Jornadas-Inspeccion`, `2026-08-10_Inspection-002-Records`, `2026-08-12_BV-Inspections-3-and-4`, `2026-08-14_BV-Inspection-004-Rescheduling`, `2026-08-17_BV-Inspection-004-Follow-Up`, `2026-08-20_Hydrotest-Report-20-Aug`, `2026-08-21_BV-Informe-IR006`, `2026-08-21_Pressure-Tests-21-Aug`, `2026-08-31_BV-Set-Informes`, `2026-08-31_HP-Tests-Programme` y `2026-09-16_BV-Survey-Turbocharger-Offset` (con `ADJUNTOS_BV-Survey/`).
- **Deduplicar por el contenido, nunca por el contenedor.** Outlook recomprime los adjuntos al reenviar, de modo que dos ZIP con el mismo contenido tienen md5 distinto.
