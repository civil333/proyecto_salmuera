---
titulo: Equivalencia de rutas antiguas del frente Bureau Veritas
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# Rutas antiguas del frente Bureau Veritas y dónde quedó su contenido

El 5-Oct-2026 el frente se consolidó en `PROGRAMA y CONTRATO/HITO BUREAU VERITAS/` y se eliminaron las dos raíces que ya no se usaban: `REQUEST WITNESS INSPECTION/` y `PROGRAMA y CONTRATO/BV INSPECTION/`. Los documentos históricos (correos enviados, análisis de transmittals, entradas antiguas de la Bitácora) siguen citando esas rutas; esta tabla dice dónde está hoy cada cosa, relativo a la raíz del frente. El detalle archivo por archivo, con md5 de origen y destino, está en `movimientos_consolidacion_2026-10-05.json`, en esta misma carpeta.

Las subcarpetas `HITO BUREAU VERITAS/oferta/`, `oferta rev 2/`, `md/`, `PLAN_INSPECCION/`, `_fuentes_guia_bv/` y `CORREOS VBV-BW/` pasaron a `01 CONTRATO Y OC/OFERTA 600049/` y `CV INSPECTORES/`, `01 CONTRATO Y OC/md/`, `02 PLAN DE INSPECCION/PLAN_INSPECCION/`, `02 PLAN DE INSPECCION/_fuentes_guia_bv/` y `05 CORREOS/CORREOS VBV-BW/`.
## `REQUEST WITNESS INSPECTION/`

| Subcarpeta antigua | Dónde quedó su contenido (relativo a la nueva ruta) |
|---|---|
| `(raíz)` | `_analisis` (1); `_historico` (1) |
| `RWI 01` | `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RWI 01/ZIP_EXTRAIDO` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `RWI 01/ZIP_EXTRAIDO/md` | `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RWI 01/_duplicado_payload_identico` | `_duplicados_payload_identico/_avisos_previos` (1) |
| `RWI 02` | `03 SOLICITUDES BW (RWI)/RWI 002 2026-08-07` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RWI 02/ZIP_EXTRAIDO` | `03 SOLICITUDES BW (RWI)/RWI 002 2026-08-07` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RWI 02/ZIP_EXTRAIDO/md` | `03 SOLICITUDES BW (RWI)/RWI 002 2026-08-07/md` (1) |
| `RWI 02/md` | `03 SOLICITUDES BW (RWI)/RWI 002 2026-08-07/md` (1) |
| `RWI 09` | `03 SOLICITUDES BW (RWI)/RWI 009 2026-09-22 y 23` (2) |
| `RWI 10` | `03 SOLICITUDES BW (RWI)/RWI 010 2026-10-08 y 09` (2) |


## `PROGRAMA y CONTRATO/BV INSPECTION/`

| Subcarpeta antigua | Dónde quedó su contenido (relativo a la nueva ruta) |
|---|---|
| `(raíz)` | `04 INFORMES BV/IR010 2026-09-02` (1) |
| `INSPECTION 01` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001 2` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `INSPECTION 01/md` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/md` (1) |
| `INSPECTION 02` | `03 SOLICITUDES BW (RWI)/RWI 003 2026-08-13 y 14` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `INSPECTION 02/md` | `03 SOLICITUDES BW (RWI)/RWI 003 2026-08-13 y 14/md` (1) |
| `INSPECTION 02/png` | `03 SOLICITUDES BW (RWI)/RWI 003 2026-08-13 y 14/png` (1) |
| `INSPECTION 03` | `04 INFORMES BV/IR003 2026-08-13` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (3) |
| `INSPECTION 04` | `03 SOLICITUDES BW (RWI)/RWI 004 2026-08-20 y 21` (2); `04 INFORMES BV/IR004 2026-08-14/COPIA RE-GUARDADA 2026-08-18` (1); `04 INFORMES BV/IR005 2026-08-20` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `INSPECTION 04/md` | `03 SOLICITUDES BW (RWI)/RWI 004 2026-08-20 y 21/md` (2) |
| `INSPECTION 04/render_hydrotest` | `04 INFORMES BV/IR005 2026-08-20/render_hydrotest` (19) |
| `INSPECTION 05` | `03 SOLICITUDES BW (RWI)/RWI 004 2026-08-20 y 21` (1); `04 INFORMES BV/IR005 2026-08-20` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `INSPECTION 06` | `04 INFORMES BV/IR006 2026-08-21` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `RESUMEN BV` | `04 INFORMES BV` (1); `04 INFORMES BV/IR010 2026-09-02` (1); `05 CORREOS/2026-08-31 Set BV IR001 a IR009` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/03-09-26` | `04 INFORMES BV/IR011 2026-09-03` (2); `04 INFORMES BV/IR012 2026-09-04` (1) |
| `RESUMEN BV/04-09-26` | `04 INFORMES BV/IR012 2026-09-04` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/BV Malasia (ADASA)` | `04 INFORMES BV/IR011 2026-09-03` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (16) |
| `RESUMEN BV/BV Malasia (ADASA)/Annex` | `_duplicados_payload_identico/ (con su ruta de origen)` (4) |
| `RESUMEN BV/IR 09-09-26` | `04 INFORMES BV/IR013 2026-09-09` (2) |
| `RESUMEN BV/IR 10-09-26` | `04 INFORMES BV/IR014 2026-09-10` (3); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/IR 11-09-26` | `04 INFORMES BV/IR015 2026-09-11` (2); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/IR 17 y 18}` | `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/IR 17-09-26` | `04 INFORMES BV/IR016 2026-09-17 y 18` (1) |
| `RESUMEN BV/IR 18-09-26` | `04 INFORMES BV/IR016 2026-09-17 y 18` (1) |
| `RESUMEN BV/IR001` | `04 INFORMES BV/IR001 2026-07-28` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/IR001/md` | `04 INFORMES BV/IR001 2026-07-28/md` (1) |
| `RESUMEN BV/IR002` | `04 INFORMES BV/IR002 2026-08-07` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/IR002/Annex/Annex` | `04 INFORMES BV/IR002 2026-08-07/Annex` (4) |
| `RESUMEN BV/IR002/md` | `04 INFORMES BV/IR002 2026-08-07/md` (1) |
| `RESUMEN BV/IR003` | `04 INFORMES BV/IR003 2026-08-13` (2) |
| `RESUMEN BV/IR003/md` | `04 INFORMES BV/IR003 2026-08-13/md` (1) |
| `RESUMEN BV/IR004` | `04 INFORMES BV/IR004 2026-08-14` (1) |
| `RESUMEN BV/IR004/md` | `04 INFORMES BV/IR004 2026-08-14/md` (1) |
| `RESUMEN BV/IR005` | `04 INFORMES BV/IR005 2026-08-20` (4) |
| `RESUMEN BV/IR005/md` | `04 INFORMES BV/IR005 2026-08-20/md` (3) |
| `RESUMEN BV/IR006` | `04 INFORMES BV/IR006 2026-08-21` (3) |
| `RESUMEN BV/IR006/md` | `04 INFORMES BV/IR006 2026-08-21/md` (2) |
| `RESUMEN BV/IR007` | `04 INFORMES BV/IR007 2026-08-24` (2) |
| `RESUMEN BV/IR007/md` | `04 INFORMES BV/IR007 2026-08-24/md` (1) |
| `RESUMEN BV/IR008` | `04 INFORMES BV/IR008 2026-08-27` (2) |
| `RESUMEN BV/IR008/md` | `04 INFORMES BV/IR008 2026-08-27/md` (1) |
| `RESUMEN BV/IR009` | `04 INFORMES BV/IR009 2026-08-28` (3) |
| `RESUMEN BV/IR009/md` | `04 INFORMES BV/IR009 2026-08-28/md` (2) |
| `RESUMEN BV/IR016` | `04 INFORMES BV/IR016 2026-09-17 y 18` (1) |
| `RESUMEN BV/IR017` | `04 INFORMES BV/IR017 2026-09-22` (3) |
| `RESUMEN BV/IR017/_duplicado_payload_identico` | `_duplicados_payload_identico/ (con su ruta de origen)` (1); `_duplicados_payload_identico/_avisos_previos` (1) |
| `RESUMEN BV/IR018` | `04 INFORMES BV/IR018 2026-09-23` (3) |
| `RESUMEN BV/IR018/_duplicado_payload_identico` | `_duplicados_payload_identico/ (con su ruta de origen)` (1); `_duplicados_payload_identico/_avisos_previos` (1) |
| `RESUMEN BV/RECHAZADOS` | `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `RESUMEN BV/TESTING PLAN 08-09-10` | `03 SOLICITUDES BW (RWI)/RWI 007 2026-09-09 al 11` (5) |
| `RESUMEN BV/TESTING TRACKER 24-09-26` | `04 INFORMES BV/TESTING TRACKER 24-09-26` (1) |
| `RESUMEN BV/_render` | `04 INFORMES BV/_render` (25) |
| `general` | `05 CORREOS/2026-08-21 RE 003-004 presiones de ensayo` (1); `_duplicados_payload_identico/ (con su ruta de origen)` (1) |
| `general/BV Chile - Report - (20-24 August 2026)/20260820` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `general/BV Chile - Report - (20-24 August 2026)/20260821` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `general/BV Chile - Report - (20-24 August 2026)/20260824` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
| `general/RE_ 25007 TALTAL -  Request to witness inspection 006` | `_duplicados_payload_identico/ (con su ruta de origen)` (3) |
| `inspeccion 009` | `_duplicados_payload_identico/ (con su ruta de origen)` (2) |
