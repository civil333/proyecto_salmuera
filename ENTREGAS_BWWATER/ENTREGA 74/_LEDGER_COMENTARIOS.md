---
titulo: "Libro mayor de comentarios — ENTREGA 73 (25007-0074), HMI Display Screenshot Rev B"
proyecto: salmuera-taltal
estado: INTERNO — no se envía
second_brain: skip
date: 2026-08-10
---

# Libro mayor de comentarios — ENTREGA 73

> Documento interno de trabajo. **NO ENVIAR.** Registra cada comentario que ADASA emitió sobre este documento a lo largo de su historial y el estado de su cierre, verificado contra la Rev B.

## Alcance

La ENTREGA 73 (submittal `25007-0074`, emitido el lunes 10-Ago-2026) trae **un solo documento**: `P22-LI-09-008-016` *HMI Display Screenshot* **Rev B**, 80 páginas, fechado el viernes 24-Jul-2026 y emitido IFA.

Es la re-emisión de la Rev A que el Transmittal N22 calificó **Código 3 — To be revised**. Es además el entregable con el historial abierto más largo del proyecto: el compromiso nace en el Transmittal N4 bajo el código `P22-BREAD-09-008-001`, el N10 lo levanta como NOTE-05 por no haber llegado, el N22 recibe la Rev A y emite cinco observaciones, y los transmittals N27, N28, N29 y N30 lo arrastran sin comentarios nuevos. El N30 lo rotula *"Oldest open commitment in the project"*.

**Siete entradas a verificar:** las cinco observaciones y la nota del Transmittal N22, más el compromiso de origen del N4.

## Procedencia del texto

El texto literal de OBS-01 a OBS-05 se extrajo de `REVISIONES/TRANSMITTALES/P22-TM-09-000-022-0/COMENTARIOS/agregar_comentarios_hmi.py`, que es lo que efectivamente se escribió sobre el PDF anotado que recibió BW Water. No se usó el `.md` del transmittal, que parafrasea.

**Cotejo de la transcripción de BW Water:** las cinco observaciones que reproduce la Consolidated Comment Sheet de la Rev B (páginas 79 y 80) coinciden en sustancia con el texto emitido. No hay recortes.

## Estados

| Estado | Significado | Exige cita |
|---|---|---|
| **CERRADO** | La evidencia del Rev B cubre íntegra la acción pedida | Sí |
| **PARCIAL** | Cubre parte, o el documento se contradice a sí mismo | Sí |
| **NO LEVANTADO** | El defecto sobrevive, o el proveedor hizo algo distinto de lo pedido | Sí, de la ausencia |

Regla que gobierna: una respuesta del tipo *"has been added"* no cierra nada por sí sola. El cierre lo prueba la pantalla renderizada. Las 74 páginas de capturas del documento no tienen texto extraíble, de modo que **toda afirmación de presencia o de ausencia de este libro mayor está hecha sobre el render**, guardado en `render/`.

## Fuentes de verificación

| Fuente | Uso |
|---|---|
| Especificación Técnica `P22-ET-09-000-001-0`, Sección 5.4 | Requisito de origen: variables eléctricas junto al consumo específico, históricos y tendencias, parametrización con límites seguros, ISA-101 |
| Instrument List `P22-LI-09-008-003` Rev E | Cruce de TAG de instrumentos (38 filas) |
| Valve List `P22-LI-09-005-002` Rev D | Cruce de TAG de válvulas |
| Equipment List `P22-LI-09-005-001` Rev B | Cruce de TAG de equipos |
| Transmittal N10 | Registro de que el Digital Power Meter integra once parámetros eléctricos en la IO List y la Data Transfer List |

---

## Entradas

### OBS-01 — Pantalla de variables eléctricas y consumo específico · MAYOR · **PARCIAL**

**Lo que se pidió.** *"No screen for the electrical-variables meter (MVE) with the specific energy consumption in kWh/m³ that the Technical Specification requires."*

**Lo que responde BW Water.** *"Electrical calculation CEE/SEC has been added into HMI overview at revised rev.B section 7.1."*

**Lo que muestra el render.** La pantalla RO Overview (página 76, sección 7.1) trae una columna de indicadores con `TOTAL POWER 0.00 kWh` y `CEE/SEC 0.00 kWh/m3`, en columnas LIVE y TOTALIZER, junto a caudales, presiones diferenciales, rechazo de sales normalizado y recuperación.

**Lo que falta.** **No aparece ni tensión ni corriente en ninguna de las 80 páginas.** La Sección 5.4 de la ET pide que el medidor de variables eléctricas entregue *"al menos Voltaje, Corriente y Potencias"* y que *"estas variables eléctricas deben estar presentes en una pantalla del HMI junto con el Consumo Específico"*. Llegó la mitad del requisito: el consumo, no las lecturas del medidor. El Transmittal N10 dejó registrado que la integración del Digital Power Meter estaba confirmada con **once parámetros eléctricos** en la IO List y en la Data Transfer List — el dato existe en el PLC y no se está desplegando.

**Punto secundario.** El rótulo `TOTAL POWER` se expresa en kWh, que es energía, en una columna rotulada LIVE. La potencia se mide en kW. Y `CEE/SEC` tiene valor en LIVE pero la celda TOTALIZER está vacía, mientras que `TOTAL POWER` sí trae las dos.

**Evidencia:** `render/nativo/p76_img2_799x530.png`.

---

### OBS-02 — Pantalla de tendencias · MAYOR · **CERRADO**

**Lo que se pidió.** *"No process-variable trending screen (the alarm history present is not a trend); add at least one for flow, pressure, conductivity and levels."*

**Lo que muestra el render.** Página 74, sección 5: pantalla de tendencias con gráfico de tiempo real e histórico, selector múltiple de TAG y botones `Move Left`, `Pause` y `Move Right` para desplazar la ventana histórica. El selector muestra `ORPIT-09-001A`, `CIT-09-001B`, `FIT-09-001`, `PIT-09-001` y `LIT-09-002`, y tiene flechas de desplazamiento. Cubre las cuatro familias que nombraba la observación: caudal, presión, conductividad y nivel. Es una pantalla distinta del historial de alarmas, que vive en la sección 4, página 73.

**Registro sin emitir.** El eje vertical usa una sola escala de −1.500 a 1.500 para todos los TAG con independencia de su unidad, de modo que una presión en bar y una conductividad en mS/cm quedan aplastadas contra el eje. Es un punto de legibilidad verificable en el FAT, no un incumplimiento de la observación.

**Evidencia:** `render/nativo/p74_img2_791x514.png`.

---

### OBS-03 — Consignas y parametrización con límites seguros · MAYOR · **CERRADO**

**Lo que se pidió.** *"No setpoint and parameterization screen with safe operating limits... add it **or document the faceplate path** by which the operator sets values and limits."*

**Lo que muestra el render.** BW Water cerró por la vía alternativa que la propia observación admitía. Página 23, sección 2.6: la pestaña *Maintenance* del faceplate de entrada analógica expone campos `Threshold (%)` y `Deadband` para los cuatro umbrales — `PV Hi-Hi`, `PV High`, `PV Low`, `PV Lo-Lo` — y documenta que al pulsar el nombre de un umbral se abre el faceplate `P_Gate`, donde se configuran retardo de disparo y retardos de estado. Página 75, sección 6: tres niveles de acceso, con Operador impedido de cambiar consignas de alarma y parámetros PID, Supervisor habilitado para consignas de alarma y arranque/parada, e Ingeniero habilitado además para P, I y D.

Entre ambas queda documentada la ruta completa: quién puede fijar valores y límites, y dónde.

**Registro sin emitir.** Las páginas de la sección 2.6 son la documentación de biblioteca de Rockwell reproducida literalmente, con el TAG genérico `FI101` y umbrales de ejemplo en porcentaje. Los límites seguros reales del proceso viven en la Alarm and Interlock List, no en este documento, así que su ausencia aquí no se le imputa.

**Evidencia:** `render/nativo/p23_img2_472x771.jpeg`, `render/nativo/p26_img2_647x880.jpeg`.

---

### OBS-04 — Conjunto de pantallas y consistencia de TAG · MAYOR · **PARCIAL**

**Lo que se pidió.** *"Only two process screens are delivered (RO Cartridge Filter, RO Feed/HP Pump); the module also requires an overview screen and screens for second-stage RO, CIP, dosing, energy recovery and brine, **with tags consistent with the approved P&ID and the Instrument List**."*

La observación tiene dos mitades. La primera se cumplió; la segunda no.

#### Conjunto de pantallas — cumplido

Seis pantallas de proceso contra las dos de la Rev A:

| Sección | Pantalla | Cubre |
|---|---|---|
| 7.1 | RO Overview | Vista general pedida |
| 7.2 | RO Feed | Absorbe el filtro de cartuchos `FIL-09-001` de la Rev A |
| 7.3 | RO System 1st Stage | Incluye el turbocharger de alimentación `SIP-09-001` (recuperación de energía) |
| 7.4 | RO System 2nd Stage | Segunda etapa, turbocharger interetapa `SIP-09-002` y la salida de rechazo |
| 7.5 | RO CIP | CIP |
| 7.6 | Antiscalant | Dosificación |

Recuperación de energía y salmuera quedan representadas dentro de las pantallas de etapa en vez de como pantallas propias. Es una solución razonable y satisface el propósito de la observación: la salmuera a drenaje aparece en la primera etapa con su válvula moduladora `VE-09-006`, y los dos turbochargers están dibujados en su circuito.

#### Consistencia de TAG — no cumplido

Seis defectos contra los listados aprobados. Cinco de las seis pantallas tienen al menos uno.

**1. La bomba de alta presión lleva el TAG de la bomba CIP.** En la pantalla RO Feed, la bomba entre el filtro de cartuchos y la primera etapa —flanqueada por el transmisor de vibración `VT-09-001` y las RTD de la bomba HP— está rotulada **`BH-09-002`**. La Equipment List asigna `BH-09-001` a la *RO HP Feed Pump* (Fedco MSD-7016, 93 kW) y `BH-09-002` a la *CIP Pump* (Grundfos CRN64-2, 11 kW). La pantalla RO CIP rotula correctamente su bomba `BH-09-002`. El mismo TAG queda sobre dos máquinas distintas y `BH-09-001` no aparece en ninguna pantalla.

**2. `TE-09-002` duplicado en la pantalla RO Feed.** Los dos indicadores de temperatura de la bomba HP leen ambos `TE-09-002`. La Instrument List define `TE-09-001` como *RO HP Pump Winding* y `TE-09-002` como *RO HP Pump Bearing*; `TE-09-001` no aparece en ninguna pantalla. La pantalla RO CIP resuelve bien el par equivalente, con `TE-09-003` en devanado y `TE-09-004` en rodamiento, lo que muestra que el patrón está entendido y se perdió solo aquí. El punto conecta con un frente abierto: la firma de la protección por RTD del FAT Procedure está retenida desde el Transmittal N27 esperando que la Plant Control Philosophy Rev 0 restituya el mapeo devanado/rodamiento que la Alarm and Interlock List, la IO List y el FAT ya sostienen.

**3. `VE-09-003` duplicado en la pantalla RO System 1st Stage.** Rotula dos válvulas distintas, la del ramal a *RO Permeate* y la del ramal a *Make-up CIP*. La Valve List Rev D tiene `VE-09-005` (SWRO Permeate 1st, DN80, mariposa motorizada), que no aparece en ninguna pantalla.

**4. `PIT-09-005` aparece en las dos pantallas de etapa.** La Instrument List lo define como *RO 2nd Stage Feed Pressure Transmitter*. En la pantalla de primera etapa está aguas arriba de `BOI-09-001`, que es donde corresponde a `PIT-09-003` (*RO 1st Stage Feed Pressure Transmitter*); `PIT-09-003` no aparece en ninguna pantalla.

**5. `FIT-09-005` aparece en la primera etapa y en el CIP.** Es el *CIP Cartridge Filter Discharge Flow Transmitter*, en la descarga de la bomba CIP. En la pantalla de primera etapa está en la línea de rechazo hacia drenaje de salmuera, que es la posición de `FIT-09-004` (*RO Train Reject Flow Transmitter*); `FIT-09-004` no aparece en ninguna pantalla.

**6. `LS-09-001` duplicado e invertido en la pantalla RO Overview.** El bloque Antiscalant muestra `TANK LSL — LS-09-001` y `TANK LSH — LS-09-001`. La Instrument List define `LS-09-001` como *Level Switch High* y `LS-09-002` como *Level Switch Low*, y la propia pantalla Antiscalant los dibuja bien, con `LS-09-001` arriba y `LS-09-002` abajo. La vista general duplica el TAG y además nombra "LSL" al que la lista define como alto. En un estanque de dosificación esa es la protección contra marcha en seco de `BDS-09-001` y `BDS-09-002`.

**Instrumentos aprobados sin pantalla.** Además de los desplazados por los duplicados, no se despliegan `PIT-09-008` (*RO Train Reject Pressure*, que sí figura en el resumen de alarmas) ni `FIT-09-002` (*RO 2nd Stage Permeate Flow*).

**Evidencia:** `render/nativo/p76_img2`, `p76_img3`, `p77_img2`, `p77_img3`, `p78_img2`, `p78_img3`; recortes ampliados en `render/crop_feed_pump.png`, `render/zoom_ro_feed_TE.png`, `render/zoom_st1_VE003.png`, `render/zoom_ovw_LS.png`, `render/crop_st1_pit_fit.png`, `render/crop_st1_fit005.png`.

---

### OBS-05 — Evidencia de conformidad ISA-101 · MENOR · **CERRADO**

**Lo que se pidió.** *"ISA-101 conformance (screen hierarchy, state colour-coding, alarm prioritization) is declared but not evidenced; demonstrate it in the next revision and reserve the full visual verification for the Factory Acceptance Test."*

**Lo que responde BW Water.** *"All the HMI graphical, user interface desgined are based Rockwell HMI software developed process library. All are complied with ISA-101."* Es, palabra por palabra, la misma declaración de la Rev A: la respuesta no agrega nada a lo que se objetó.

**Pero el cuerpo del documento sí lo evidencia**, y el veredicto se decide por el documento, no por la hoja de respuestas:

- **Codificación de color por estado.** Cada sección de faceplate abre enumerando el icono de cada estado: entrada digital normal y en alarma (sección 2.5), entrada analógica en Low Low, Low, High, High High, no reconocida y normal (sección 2.6), bomba con variador detenida, arrancando, en marcha, en falla y con falla de arranque o parada (sección 2.8), válvula moduladora al 0, 50 y 100 por ciento y en desviación (sección 2.9), secuenciador en espera y completado (sección 2.10).
- **Priorización de alarmas.** La página 26 documenta cuatro prioridades con icono propio —Urgent, High, Medium y Low— más los iconos de reconocimiento requerido y de salida de alarma. Las pantallas de proceso las usan: en la primera etapa, `FIT-09-003` lleva el marcador rojo de Urgent y `PIT-09-009` el amarillo.
- **Jerarquía de pantallas.** El panel de navegación de la sección 3 está presente al pie de todas las pantallas y articula vista general, pantallas de proceso, lista de alarmas, tendencias y sesión de usuario.

Se cierra. La verificación visual completa queda reservada al FAT, como la propia observación estableció.

**Registro sin emitir.** El resumen de alarmas de la página 73 despliega todas las filas sobre una única banda roja, sin diferenciación visible de prioridad, lo que contrasta con el esquema de cuatro niveles de la página 26. Es punto de verificación en el FAT, no defecto del documento.

**Evidencia:** `render/nativo/p26_img2_647x880.jpeg`, `render/nativo/p73_img3_801x530.png`, `render/nativo/p77_img2_801x529.png`.

---

### NOTE-01 (N22) y NOTE-05 (N4) — El compromiso histórico · **CERRADO como compromiso**

El compromiso abierto en el Transmittal N4 bajo el código `P22-BREAD-09-008-001`, levantado como NOTE-05 en el N10 y registrado en el N22 como materialmente entregado con la Rev A, **queda cumplido en sustancia con la Rev B**: el conjunto de pantallas existe y está documentado.

Lo que sigue abierto no es la existencia del entregable sino su corrección: las variables eléctricas de OBS-01 y los seis TAG de OBS-04. El compromiso más antiguo del proyecto deja de estar abierto como compromiso y pasa a ser una condición de emisión.

**Efecto sobre el Operating and Maintenance Manual.** El manual está retenido desde el Transmittal N27 esperando estas pantallas. Con el conjunto completo, la dependencia deja de ser de existencia y pasa a ser de contenido: los TAG que el manual reproduzca deben ser los corregidos, no los de esta Rev B.

---

## Recuento

| Estado | Entradas |
|---|---|
| CERRADO | OBS-02, OBS-03, OBS-05, NOTE-01 / NOTE-05 |
| PARCIAL | OBS-01, OBS-04 |
| NO LEVANTADO | ninguna |
| **Total verificado** | **7 de 7** |

Ninguna entrada quedó sin cita.
