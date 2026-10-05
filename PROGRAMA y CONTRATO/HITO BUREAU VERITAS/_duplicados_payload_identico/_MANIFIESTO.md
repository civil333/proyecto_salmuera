---
titulo: Manifiesto de copias con payload identico
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# Copias con payload idéntico — frente Bureau Veritas

Ordenamiento del 5-Oct-2026. Cada archivo de esta carpeta conserva la ruta que tenía antes de la consolidación y es **byte a byte igual** (md5) a la copia canónica que se indica. Nada se borró. Los ZIP y el RAR de `contenedores/` tienen todo su contenido suelto en la estructura; dos ZIP de envíos distintos con el mismo contenido tienen md5 de contenedor distinto porque Outlook recomprime al adjuntar, por eso la deduplicación se hizo por el contenido.

Dos excepciones conservadas a propósito fuera de esta carpeta: el anexo de calibración del `IR008` y el del `IR009` son el mismo archivo (hallazgo documentado en el registro de inspecciones) y queda una copia en cada informe; y la oferta 600049 Rev 2 queda también en `02 PLAN DE INSPECCION/_fuentes_guia_bv/` porque es fuente de la guía del paquete.

| Tipo | Ruta de origen | md5 | Copia canónica |
|---|---|---|---|
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001 2/BW Water - PMI Witness NOI001.pdf` | `82aa50617515` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/BW Water - PMI Witness NOI001.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001 2/P22-BA-09-000-004_0_ITP.pdf` | `81f8dc64b331` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/P22-BA-09-000-004_0_ITP.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001.zip` | `6e4d6f02f7bf` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001/BW Water - PMI Witness NOI001.pdf` | `82aa50617515` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/BW Water - PMI Witness NOI001.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 01/RE_ 25007 TALTAL -  Request to witness inspection 001/P22-BA-09-000-004_0_ITP.pdf` | `81f8dc64b331` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/P22-BA-09-000-004_0_ITP.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 02/RE_ 25007 TALTAL -  Request to witness inspection 002.zip` | `af484625895e` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 03/Annex A - IR003.pdf` | `d3d4aa57dbc3` | `04 INFORMES BV/IR003 2026-08-13/Annex A - IR003.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 03/IR003-ADASA-BVM-13082026.pdf` | `b4dfac0c3113` | `04 INFORMES BV/IR003 2026-08-13/IR003-ADASA-BVM-13082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 03/IR004-ADASA-BVM-14082026.pdf` | `c1031a5211ab` | `04 INFORMES BV/IR004 2026-08-14/IR004-ADASA-BVM-14082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/Taltal Hydrotest Report BV W 20Aug.pdf` | `b6b26b47b7c6` | `04 INFORMES BV/IR005 2026-08-20/Taltal Hydrotest Report BV W 20Aug.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 05/Annex 1.pdf` | `7c839482107c` | `04 INFORMES BV/IR005 2026-08-20/Annex 1 - IR005 - Calibration Certifficate (PSPP-26605330).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 05/IR005-ADASA-BVM-20082026.pdf` | `56132c067c5e` | `04 INFORMES BV/IR005 2026-08-20/IR005-ADASA-BVM-20082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 06/Annex 1.pdf` | `bc3d1bc5b0cf` | `04 INFORMES BV/IR006 2026-08-21/Annex 1 - IR006 - Calibration Certifficate (PSPP-26605340).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 06/IR006-ADASA-BVM-21082026.pdf` | `d78ed86460c6` | `04 INFORMES BV/IR006 2026-08-21/IR006-ADASA-BVM-21082026.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/04-09-26/RE_ 25007 TALTAL -  Request to witness inspection 006.zip` | `08715b6336f4` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex 1 - IR005 - Calibration Certifficate (PSPP-26605330).pdf` | `7c839482107c` | `04 INFORMES BV/IR005 2026-08-20/Annex 1 - IR005 - Calibration Certifficate (PSPP-26605330).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex 1 - IR006 - Calibration Certifficate (PSPP-26605340).pdf` | `bc3d1bc5b0cf` | `04 INFORMES BV/IR006 2026-08-21/Annex 1 - IR006 - Calibration Certifficate (PSPP-26605340).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex 1 - IR007 - Coating Thickness Gauge Calibration.pdf` | `ca8524c93ba7` | `04 INFORMES BV/IR007 2026-08-24/Annex 1 - IR007 - Coating Thickness Gauge Calibration.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex 1 - IR008 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` | `5314062a3a83` | `04 INFORMES BV/IR008 2026-08-27/Annex 1 - IR008 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex 1 - IR009 - Pressure Gauge Calibration Certificate (PSPP-26605336).pdf` | `5314062a3a83` | `04 INFORMES BV/IR008 2026-08-27/Annex 1 - IR008 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex A - IR001.pdf` | `82aa50617515` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/BW Water - PMI Witness NOI001.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex A - IR003.pdf` | `d3d4aa57dbc3` | `04 INFORMES BV/IR003 2026-08-13/Annex A - IR003.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex/0006 (Cap)-TALTAL-PT-070826-05.pdf` | `1dc90a61eaa0` | `04 INFORMES BV/IR002 2026-08-07/Annex/0006 (Cap)-TALTAL-PT-070826-05.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex/0009-TALTAL-PT-070826-06.pdf` | `6f6c5cef11a1` | `04 INFORMES BV/IR002 2026-08-07/Annex/0009-TALTAL-PT-070826-06.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex/1139_001.pdf` | `ef3f28b5411e` | `04 INFORMES BV/IR002 2026-08-07/Annex/1139_001.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/Annex/Personal Certificate.pdf` | `392c04318dec` | `04 INFORMES BV/IR002 2026-08-07/Annex/Personal Certificate.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR001-ADASA-BVM-28072026.pdf` | `e38fed1bf919` | `04 INFORMES BV/IR001 2026-07-28/IR001-ADASA-BVM-28072026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR002-ADASA-BVM-07082026.pdf` | `15b118347ea2` | `04 INFORMES BV/IR002 2026-08-07/IR002-ADASA-BVM-07082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR003-ADASA-BVM-13082026.pdf` | `b4dfac0c3113` | `04 INFORMES BV/IR003 2026-08-13/IR003-ADASA-BVM-13082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR004-ADASA-BVM-14082026.pdf` | `c1031a5211ab` | `04 INFORMES BV/IR004 2026-08-14/IR004-ADASA-BVM-14082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR005-ADASA-BVM-20082026_Rev01.pdf` | `601fc57a712d` | `04 INFORMES BV/IR005 2026-08-20/IR005-ADASA-BVM-20082026_Rev01.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR006-ADASA-BVM-21082026_Rev01.pdf` | `d40522f3ce78` | `04 INFORMES BV/IR006 2026-08-21/IR006-ADASA-BVM-21082026_Rev01.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR007-ADASA-BVM-24082026.pdf` | `219052530c15` | `04 INFORMES BV/IR007 2026-08-24/IR007-ADASA-BVM-24082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR008-ADASA-BVM-27082026.pdf` | `097264f9a92c` | `04 INFORMES BV/IR008 2026-08-27/IR008-ADASA-BVM-27082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/BV Malasia (ADASA)/IR009-ADASA-BVM-28082026.pdf` | `394300c755c6` | `04 INFORMES BV/IR009 2026-08-28/IR009-ADASA-BVM-28082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR 10-09-26/Taltal Hydrotest Report BV W 10Sep[78].pdf` | `e8bd2745ea89` | `04 INFORMES BV/IR014 2026-09-10/Taltal Hydrotest Report BV W 10Sep.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR 11-09-26/25007_TALTAL_-__Request_to_witness_inspection_015.zip` | `41133677481c` | `contenido extraído a la estructura` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR 17 y 18}/RE__25007_TALTAL_-__Request_to_witness_inspection_008.zip` | `3a869275f940` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR001/Annex A - IR001.pdf` | `82aa50617515` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/BW Water - PMI Witness NOI001.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR002/Annex - IR002.zip` | `4198e259b3a3` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR017/_duplicado_payload_identico/Taltal Hydrotest Report BV W 22Sep[90].pdf` | `bc39369d22d6` | `04 INFORMES BV/IR017 2026-09-22/Taltal Hydrotest Report BV W 22Sep.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR018/_duplicado_payload_identico/Taltal Hydrotest Report BV W 23SEP 2[34].pdf` | `5eb62699d47d` | `04 INFORMES BV/IR018 2026-09-23/Taltal Hydrotest Report BV W 23SEP 2.pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/RECHAZADOS/RE_ 25007 TALTAL -  Request to witness inspection 006.zip` | `5e63656c4034` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/Taltal Hydrotest Report BV W 4Sep.pdf` | `cc0ea64b6785` | `04 INFORMES BV/IR012 2026-09-04/Taltal Hydrotest Report BV W 4Sep.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260820/Annex 1 - Calibration Certifficate (PSPP-26605330).pdf` | `7c839482107c` | `04 INFORMES BV/IR005 2026-08-20/Annex 1 - IR005 - Calibration Certifficate (PSPP-26605330).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260820/IR005-ADASA-BVM-20082026_Rev01.pdf` | `601fc57a712d` | `04 INFORMES BV/IR005 2026-08-20/IR005-ADASA-BVM-20082026_Rev01.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260821/Annex 1 - Calibration Certifficate (PSPP-26605340).pdf` | `bc3d1bc5b0cf` | `04 INFORMES BV/IR006 2026-08-21/Annex 1 - IR006 - Calibration Certifficate (PSPP-26605340).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260821/IR006-ADASA-BVM-21082026_Rev01.pdf` | `d40522f3ce78` | `04 INFORMES BV/IR006 2026-08-21/IR006-ADASA-BVM-21082026_Rev01.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260824/Annex 1 - Coating Thickness Gauge Calibration.pdf` | `ca8524c93ba7` | `04 INFORMES BV/IR007 2026-08-24/Annex 1 - IR007 - Coating Thickness Gauge Calibration.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/BV Chile - Report - (20-24 August 2026)/20260824/IR007-ADASA-BVM-24082026.pdf` | `219052530c15` | `04 INFORMES BV/IR007 2026-08-24/IR007-ADASA-BVM-24082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/RE_ 25007 TALTAL -  Request to witness inspection 006/Annex 1 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` | `5314062a3a83` | `04 INFORMES BV/IR008 2026-08-27/Annex 1 - IR008 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` |
| contenedor | `PROGRAMA y CONTRATO/BV INSPECTION/general/RE_ 25007 TALTAL -  Request to witness inspection 006/BV Chile - Report - (20-24 August 2026).zip` | `e06a35a6054f` | `contenido extraído a la estructura` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/RE_ 25007 TALTAL -  Request to witness inspection 006/IR008-ADASA-BVM-27082026.pdf` | `097264f9a92c` | `04 INFORMES BV/IR008 2026-08-27/IR008-ADASA-BVM-27082026.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/general/Taltal Hydrotest Report BV W 28Aug.pdf` | `617f593b6a69` | `04 INFORMES BV/IR009 2026-08-28/Taltal Hydrotest Report BV W 28Aug.pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/inspeccion 009/Annex 1 - Pressure Gauge Calibration Certificate (PSPP-26605336).pdf` | `5314062a3a83` | `04 INFORMES BV/IR008 2026-08-27/Annex 1 - IR008 - Pressure Gauge Calibration Certificate (PSPP-26605366).pdf` |
| duplicado | `PROGRAMA y CONTRATO/BV INSPECTION/inspeccion 009/IR009-ADASA-BVM-28082026.pdf` | `394300c755c6` | `04 INFORMES BV/IR009 2026-08-28/IR009-ADASA-BVM-28082026.pdf` |
| contenedor | `REQUEST WITNESS INSPECTION/RWI 01/RE_ 25007 TALTAL -  Request to witness inspection 001.zip` | `0a8988fbf7c5` | `contenido extraído a la estructura` |
| duplicado | `REQUEST WITNESS INSPECTION/RWI 01/ZIP_EXTRAIDO/Annex A.pdf` | `82aa50617515` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/BW Water - PMI Witness NOI001.pdf` |
| duplicado | `REQUEST WITNESS INSPECTION/RWI 01/ZIP_EXTRAIDO/IR001-ADASA-BVM-28072026.pdf` | `e38fed1bf919` | `04 INFORMES BV/IR001 2026-07-28/IR001-ADASA-BVM-28072026.pdf` |
| duplicado | `REQUEST WITNESS INSPECTION/RWI 01/ZIP_EXTRAIDO/md/IR001-ADASA-BVM-28072026_extracted.md` | `1e9650b7bb0a` | `04 INFORMES BV/IR001 2026-07-28/md/IR001-ADASA-BVM-28072026_extracted.md` |
| contenedor | `REQUEST WITNESS INSPECTION/RWI 02/25007 TALTAL -  Request to witness inspection 002.zip` | `3ba5ef36c3ac` | `contenido extraído a la estructura` |
| duplicado | `REQUEST WITNESS INSPECTION/RWI 02/ZIP_EXTRAIDO/P22-BA-09-000-004_0_ITP.pdf` | `81f8dc64b331` | `03 SOLICITUDES BW (RWI)/RWI 001 2026-07-28/P22-BA-09-000-004_0_ITP.pdf` |
