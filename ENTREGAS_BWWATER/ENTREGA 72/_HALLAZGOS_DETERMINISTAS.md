---
titulo: "Hallazgos y veredictos propuestos — ENTREGA 72 (25007-0072)"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-10
---

# Hallazgos y veredictos — ENTREGA 72

> Documento interno de trabajo. **NO ENVIAR.** Complementa el [libro mayor](_LEDGER_COMENTARIOS.md), que verifica el cierre de lo que estaba abierto. Aquí va lo que la entrega trajo de nuevo y la disposición de cada documento.

## Disposición

| Documento | Rev | Disposición | Determinante |
|---|---|---|---|
| Plant Control Philosophy `P22-BT-09-009-001` | 0 | **Sin código** | Una de cinco condiciones levantada. Decisión del usuario: no se codifica un documento ya emitido para construcción; se declaran los puntos abiertos con su razón |
| RO Vessel Hydrostatic Test Procedure `P22-BA-09-000-009` | 0 | **1 — Approved** | Presiones vinculantes declaradas y certificado único en rango. Ver más abajo el punto de la vigencia, que puede cambiar esto |
| Tie-In Point Layout `P22-DWG-09-005-005` | B | **2 — Approved as noted** | Las tres vistas de elevación llegaron; falta la presión de diseño en la alimentación |
| GA of SWRO System Skid `P22-DWG-09-005-008` | B | **2 — Approved as noted** | El cuadro llegó completo; tres referencias de documento mal citadas en las notas nuevas |

## Punto que puede cambiar el veredicto del procedimiento hidrostático

El certificado 26993 que ahora se adjunta está **calibrado el 12 de diciembre de 2025**. La cláusula 4 del propio procedimiento, *Calibration of the measurement and test equipment*, dice: *"Auxiliary pressure gauge will be calibrated of equipment every 6 months period or whenever there is reason to believe that the readings are in error."* El informe de ensayo lleva fecha **17 de junio de 2026** (`Pedido cliente BW-PO-2026M184 R1; PV/26/0919 Fecha 17/06/2026`).

Seis meses desde el 12 de diciembre vencen el 12 de junio. **El ensayo se ejecutó cinco días después**, de modo que el certificado que se adjunta para acreditar el manómetro no cubre la fecha en que se usó, según la regla que fija el mismo procedimiento.

No es lo que pedía la observación —que era identificar el manómetro y adjuntar su certificado dentro del rango de 1,5 a 4 veces—, así que en sentido estricto es hallazgo nuevo. Pero recae sobre la evidencia misma que se acaba de aceptar, y el ensayo hidrostático de los recipientes es punto Hold del ITP cuyo dossier alimenta este certificado.

## Lo que la entrega trajo sin que se le pidiera

Registro interno. **Nada de esto se emite.**

**La hoja de comentarios de la filosofía de control declara el submittal equivocado.** Su encabezado dice `Submittal No.: 25007-0014` en las tres hojas, cuando la entrega es la `25007-0072`. El `25007-0014` fue la entrega de la Rev A, en enero.

**Dos válvulas con la misma descripción en la filosofía de control.** Página 55, ítems 8 y 9: `VE-09-008` y `VE-09-009` figuran las dos como *"Motorized Valve - CIP Return from RO Stage 1 with Limit Switches"*. La Valve List Rev D las distingue.

**El esquema del ensayo hidrostático prescribe un manómetro que no sirve para uno de los dos recipientes.** El rótulo *"PRESSURE GAUGE: ASME [0-160 bares]"* de la PDF página 9 da 1,76 veces para el ensayo de 91,0 bar del `BPV81200SP7`, que cumple, y 1,17 veces para el de 136,5 bar del `BPV81800SP7`, que no. Queda como residual del Código 1 y se trackea en la Sección 3 del transmittal.

## Tres confirmaciones cruzadas que refuerzan la revisión del HMI

La E72 aporta evidencia independiente sobre los TAG que la revisión del HMI Rev B encontró mal, y conviene que el transmittal la aproveche porque proviene de documentos del propio proveedor:

- La filosofía de control, página 55, ítem 6, identifica `VE-09-005` como *"Motorized Valve - CIP Make-up / Chemical Fill with Limit Switches"*. Es la válvula que el HMI rotula por segunda vez como `VE-09-003` en el ramal de make-up CIP.
- El GA of SWRO System Skid Rev B, lámina 3, rotula sobre el skid `PIT-09-003`, `FIT-09-004` y `VE-09-005`, que son exactamente tres de los TAG que el HMI perdió al duplicar otros.
- La filosofía de control, página 55, confirma `BH-09-002` como bomba CIP y la página 36 confirma `BH-09-001` como bomba de alimentación de alta presión, que es el intercambio de identidad que el HMI comete en su pantalla de alimentación.

## Condiciones a escribir en el transmittal

**Plant Control Philosophy Rev 0 — puntos abiertos, sin código.** Cuatro, con su razón concreta:

1. El par de RTD de la bomba CIP sigue invertido en la página 55, sección 3.4.2: rodamiento `TE-09-003` y devanado `TE-09-004`, contra la Instrument List Rev E que los define al revés. La corrección se aplicó a la bomba de alta y no a la de CIP, y la página 36 del mismo documento cuenta a `TE-09-003` entre los devanados.
2. La alarma de vibración de la bomba de alta queda en 7,1 mm/s contra los 7,0 de la Alarm and Interlock List Rev C, y el disparo de los dos turbochargers en 7,1 contra los 6,0 de esa lista.
3. El disparo de devanado de 140 °C quedó sin clase de aislación declarada: la cita de Clase B se eliminó en vez de confirmarse la clase.
4. La tabla de documentos de referencia de la página 5 sigue diciendo *SEPARATE DOCUMENT* donde ya corresponden `P22-LI-09-008-017` Rev A y `P22-LI-09-008-015` Rev C.

**Tie-In Point Layout Rev B — Código 2.** Declarar la presión de diseño en el punto de conexión de alimentación `TP-DA P8-001`, para verificar compatibilidad con ANSI 150#, y completar la clase y el estándar de brida del punto `TP-AS P11-001`, que siguen en guion.

**GA of SWRO System Skid Rev B — Código 2.** Corregir las tres referencias de las notas nuevas: la nota 6 cita la Instrument List en Rev D cuando la vigente es Rev E; la nota 7 cita `P22-LI-09-009-00` cuando la Line List aprobada es `P22-LI-09-009-003`; y la nota 8 cita `P22-ET-09-006-01`, que no es un código válido de la codificación del proyecto.

**RO Vessel Hydrostatic Test Procedure Rev 0 — Código 1**, con el rótulo del manómetro del esquema trackeado en la Sección 3.

## Trazas

`md/` con la extracción de los cuatro documentos · `render/` con las tres hojas de comentarios de la filosofía de control, sus páginas de RTD, el certificado de calibración y las láminas de los dos planos.
