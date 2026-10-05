---
titulo: Mapa de PROGRAMA y CONTRATO
fecha: 2026-10-05
estado: INTERNO
second_brain: skip
---

# PROGRAMA y CONTRATO

Administración del contrato C-4300 con BW Water: el contrato, lo comercial, los cronogramas y el seguimiento. Reordenado el 5-Oct-2026 por tema; antes eran diecinueve carpetas en un solo nivel, creadas por evento.

| Carpeta | Contenido |
|---|---|
| `CONTRATO C-4300/` | Contrato firmado, acta de reunión de inicio, `md/` con el contrato extraído y `VENTA BW WATER A DE NORA/` (notificación de la venta de la contraparte, mayo de 2026) |
| `COMERCIAL/` | `ESTADOS DE PAGO/` (EDP 1, EDP 2, EDP de ingeniería, carta de aumento de monto y `DOCUMENTOS BASE/`: formato, formulario de boleta de garantía y correo de instrucciones); `ADICIONALES DE INGENIERIA/` (change order 25007-PL-0001, OC I-330); `REPUESTOS DE 2 AÑOS/` (propuesta PL-0002 y OC I-333); `DESPACHO MEMBRANAS LG/` (cotizaciones de flete desde Corea); `_ANALISIS_COMERCIAL_04AGO.md` |
| `CRONOGRAMAS/` | Una carpeta por cronograma, con la fecha del documento al inicio: programas iniciales (oct-2025 a feb-2026), catch-up del 05-Mar (baseline contractual), mitigación y recovery del 22-May, progress update del 24-Jun, programa de fabricación del 01-Jul y progress update del 28-Ago. `FEDCO/` guarda el programa del proveedor de bombas y `_ANALISIS/` los análisis de programa de enero a marzo y la tabla comparativa de hitos |
| `REVISION SEMANAL PO EQUIPOS/` | Revisión de procura contra baseline, una carpeta por semana `SEMANA AAAA-MM-DD`; `Unprice PO/` con las órdenes de compra de BW Water a sus proveedores; scripts de diff de trackers y del programa de fabricación (CLAUDE.md sección 11) |
| `SEGUIMIENTO COMPROMISOS/` | Registro de compromisos P22-IT-06-000-006-0: `compromisos.yaml` y `hitos.yaml` son la fuente; el `.xlsx` se regenera. Copias previas en `_backups/` (CLAUDE.md sección 11.1) |
| `RFI/` | Una carpeta por RFI de BW Water, con el formulario respondido (CLAUDE.md sección 3.12) |
| `HITO BUREAU VERITAS/` | Tercero inspector de taller; mapa propio en su `_LEEME.md`. `PAQUETE_INSPECCION_BV/` no se mueve nunca |

## Dónde quedó cada ruta antigua

Los correos, transmittals y entradas antiguas de la Bitácora del README siguen citando las rutas previas al 5-Oct-2026. Esta tabla las resuelve. El registro archivo por archivo, con md5 de origen y destino, está en `_ARCHIVO/movimientos_orden_raiz_y_programa_2026-10-05.json`, en la raíz del proyecto.

| Ruta antigua (`PROGRAMA y CONTRATO/…`) | Ruta nueva (`PROGRAMA y CONTRATO/…`) |
|---|---|
| `02 C-4300 BW WATER - SUMINISTRO - 12803 v2_BWWA Signed (2).pdf` | `CONTRATO C-4300/` |
| `md/CONTRATO-C4300-BWWATER-SUMINISTRO.md` | `CONTRATO C-4300/md/` |
| `COMPRA DE BWWATER POR NORA/` | `CONTRATO C-4300/VENTA BW WATER A DE NORA/` |
| `DOCUMENTOS PARA EL ESTADO DE PAGO/` | el acta de inicio a `CONTRATO C-4300/`; `ESTADO DE PAGO 2/` (EEPP 24786) a `COMERCIAL/ESTADOS DE PAGO/EDP 2/`; el resto a `COMERCIAL/ESTADOS DE PAGO/DOCUMENTOS BASE/` |
| `ESTADOS DE PAGO/` | `COMERCIAL/ESTADOS DE PAGO/` |
| `ADICIONALES DE INGENIERIA/` | `COMERCIAL/ADICIONALES DE INGENIERIA/` |
| `REPUESTOS DE 2 AÑOS/` | `COMERCIAL/REPUESTOS DE 2 AÑOS/` |
| `_DUPLICADO_COTIZACION_REPUESTOS/` | `COMERCIAL/REPUESTOS DE 2 AÑOS/_retirado_2026-08-04/` |
| `DESPACHO MEMBRANAS LG/` | `COMERCIAL/DESPACHO MEMBRANAS LG/` |
| `_ANALISIS_COMERCIAL_04AGO.md` | `COMERCIAL/` |
| `pdf/` y `md/PROGRAMA-*.md` | `CRONOGRAMAS/2025-10 a 2026-02 PROGRAMAS INICIALES/pdf/` y `…/md/` |
| `05.03.26_12803_Taltal Water Treatment Plant.*` | `CRONOGRAMAS/2026-03-05 CATCH-UP/` |
| `PROGRAMA DE MITIGACION/` | `CRONOGRAMAS/2026-05-22 MITIGACION Y RECOVERY/` |
| `PROGRAMA 26-06-26/` | `CRONOGRAMAS/2026-06-24 PROGRESS UPDATE/` |
| `PROGRAMA DE FABRICACION 01-07-26/` | `CRONOGRAMAS/2026-07-01 PROGRAMA DE FABRICACION/` |
| `PROGRAMA DE SEGUIMIENTO RETRASOS/` | `CRONOGRAMAS/2026-08-28 PROGRESS UPDATE/` |
| `RESPUESTA DE FEDCO/` | `CRONOGRAMAS/FEDCO/` |
| `REVISIONES/` y `estado_compras_09-03-26.md` | `CRONOGRAMAS/_ANALISIS/` |
| `REVISION SEMANAL PO EQUIPOS/SEMANA DD-MM-AA/` | `REVISION SEMANAL PO EQUIPOS/SEMANA 20AA-MM-DD/`; `SEMANA  14-09-26` pasó a `SEMANA 2026-09-14` y `SEMANA (32) 10-08-26` a `SEMANA 2026-08-10` |
| `REVISION SEMANAL PO EQUIPOS/PO-0016155 UP (MEMBRANAS).pdf` | `REVISION SEMANAL PO EQUIPOS/Unprice PO/` |
| `REVISION SEMANAL PO EQUIPOS/TALTAL_Master Document and Drawing Deliverable List for submittal.xlsx` | `REVISION SEMANAL PO EQUIPOS/SEMANA 2026-04-28/` |
| `SEGUIMIENTO COMPROMISOS/compromisos.yaml.bak_*` | `SEGUIMIENTO COMPROMISOS/_backups/` |
| `RESPUESTAS/` | Eliminada: estaba vacía |
| `BV INSPECTION/` y `../REQUEST WITNESS INSPECTION/` | `HITO BUREAU VERITAS/` (ver `HITO BUREAU VERITAS/_historico/_EQUIVALENCIAS_RUTAS_ANTIGUAS.md`) |

Desde la raíz del proyecto llegaron `TABLA-COMPARATIVA-HITOS.xlsx` y `generar_tabla_hitos.py`, hoy en `CRONOGRAMAS/_ANALISIS/`.
