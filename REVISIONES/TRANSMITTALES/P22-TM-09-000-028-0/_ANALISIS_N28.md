# Análisis interno TM N28 — disposición por documento (NO ENVIAR)

Entrega E65 (25007-0065) + E66 (25007-0066). Familia de Control. Método: revisión adversarial por documento (4 refutadores) + verificación manual de los drivers + revisión CCS ítem-por-ítem (norma §6.5).

## Autoridad por tipo de dato (para clasificar cada punto)

| Dato | Documento que lo **desarrolla** (autoridad) |
|---|---|
| Tags de instrumento + rangos | Instrument List Rev E |
| Setpoints (alarma/trip) + acción de interlock | Alarm & Interlock List |
| Lógica de control, secuencia, rampa VFD, protecciones | Plant Control Philosophy |
| Canales I/O (tipo, dirección) | IO List |
| Tags/etapa de válvulas | Valve List / P&ID |

**Criterio §6.2 aplicado:** el comentario es sobre el documento. Si el punto lo **desarrolla otro documento** y aquí solo falta reflejarlo → el documento en revisión es **Code 2** (alinea al emitir Rev 0), no degrada a Code 3. Code 3 se reserva para cuando el **contenido propio** del documento (lo que ese documento desarrolla) está mal de raíz y exige nueva revisión.

---

## 1. Plant Control Philosophy Rev E (P22-BT-09-009-001) → Code 2

**Contenido propio (lógica) = CORRECTO y verificado:** bypass VE-09-002 por lazo de presión (no TDS), permissive HP Pump sin VE-09-007 dup/VE-09-014 espurio, SEC 4.71, salt-rejection sobre feed, array 6:4/70, HART a nivel de instrumento. Los hijos por fin existen (Sequence Chart 017 Rev A + Alarm List 015 Rev C).

| # | Hallazgo | ¿Lo desarrolla…? | Clasificación | 
|---|---|---|---|
| OBS-01 | Tablas de instrumentos con **TE-09-001=Bearing / TE-09-002=Winding** (y 003/004 CIP) — al revés del resto | Instrument List Rev E (tags) + Alarm List/IO List coinciden 001=Winding | **OTRO doc → alinear.** La CP solo refleja el mapeo de tags; debe espejar el Instrument List Rev E. No degrada. |
| OBS-02 | Temp devanado Alarm 130/Trip 155 vs Alarm List 120/140; cita "Class B" con 155°C (Class F) | Setpoints = Alarm List | **OTRO → alinear** al Alarm List (140). El "Class B/155" es texto propio → corrección de 1 línea al emitir |
| OBS-03 | Vibración 4.5/7.1 vs Alarm List 7.0/10.0 | Setpoints = Alarm List | **OTRO → alinear** (ojo: el valor del Alarm List también se corrige, ver doc 2) |
| OBS-04 | Protección baja presión descarga 45 bar/5s + 50 bar/3s descrita en CP, ausente del Alarm List | Implementación de setpoint = Alarm List | **OTRO** → el Alarm List la incorpora o la CP la retira → Sección 3 |
| NOTE-01/03 | Tabla de referencias no fija los hijos por código/rev; typos FIT-09-003→002, VE-09-014/**010**→016, LI-09-002 | Tags = Instrument/Valve List | OTRO + housekeeping propio menor |

**Veredicto CP: Code 2 — Approved as Noted.** Su lógica (lo que la CP desarrolla) es correcta; todo lo observado es reflejar tags/setpoints que desarrollan el Instrument List y el Alarm List. Se incorpora al emitir Rev 0, sin nueva revisión. **Nota dura (seguridad):** el reflejo del swap winding/bearing debe hacerse sí o sí (TE-09-001=Winding, TE-09-002=Bearing) — sensor de seguridad.

## 2. Alarm and Interlock List Rev C (P22-LI-09-008-015) → Code 2

**Cierres verificados:** unidades µS/cm permeado (N17) corregidas; rodamiento AHH 95/AH 90 (verificado a mano); simetría vibración turbos; 6 respuestas CCS reales (verificado). El swap RTD quedó bien AQUÍ (001=Winding, 002=Bearing).

| # | Hallazgo | ¿Lo desarrolla…? | Clasificación |
|---|---|---|---|
| OBS-01 | **VIT-09-001 AHH=10.0 mm/s sobre rango 0–8.9** → el trip por vibración (exigido por la CP) nunca dispara [verificado] | El **setpoint** es PROPIO del Alarm List; el **rango** lo desarrolla el Instrument List/datasheet | **PROPIO (valor).** Corrección de su propio valor (bajar AHH a ≤8.9) o pedir re-rango del transmisor. Un valor → incorporable a Rev 0 |
| OBS-02 | Tag alarma MCCB **XT001** no existe en IO List (es **XA001** "Close States") | Tag/punto = IO List | **OTRO → alinear** el tag al IO List → Sección 3 |
| NOTE-01/08 | VIT vs VT prefijo; faltan alarmas de falla VE-09-014/016 + dosificadoras; dup ítems; sufijo .FAHH; masking flujo bajo sin condición; SP diferencial boost no declarado; TIT-09-006 sobre-rangeado | Tags = Instrument List; completitud propia = Alarm List | OTRO (tags) + completitud propia menor |

**Veredicto Alarm List: Code 2.** El único punto verdaderamente propio (vibración AHH) es una **corrección de un valor** a incorporar en Rev 0; el resto son alineaciones de tag (OTRO doc) o completitudes menores. **Nota dura:** el AHH de vibración debe quedar alcanzable (≤ fondo de escala) o re-rangear el sensor — es un trip de protección de máquina.

## 3. Control and Sequence Chart Rev A (P22-LI-09-008-017, NUEVO) → Code 2

**Contenido propio (pasos/secuencia) = correcto:** cubre A1 Group Control, A2 Servicio (arranque/normal/paro/ESD), A3 CIP, A4 Flushing; los permissives coinciden 1:1 con la CP. Documento nuevo → sin CCS (esperado).

| # | Hallazgo | ¿Lo desarrolla…? | Clasificación |
|---|---|---|---|
| OBS-01 | Nota 5 enuncia el bypass VE-09-002 por **"Low TDS value"** (la CP lo prohíbe: es por lazo de presión) | Lógica bypass = CP | **OTRO → alinear** a la CP (el "(SP:62 Bar)" ya es presión) |
| OBS-02 | Aborto Stage-2 a **90 bar** vs AHH 93 bar del Alarm List | Setpoint = Alarm List | OTRO → alinear (93) |
| OBS-03 | Rampa VFD **1 Hz/s** vs 0.1–0.3 Hz/s de la CP | Rampa VFD = CP | OTRO → alinear |
| OBS-04 | Flushing **40 m³/h** único vs 48/36 (Stage1 / Stage1+2) del Alarm List | Setpoint = Alarm List | OTRO → alinear |
| OBS-05 | VE-09-010 rotulada "2nd Stage" (es 1st Stage CIP Return); mapeo etapa inconsistente CP/IO/Alarm | Etapa de válvula = Valve List/IO List | OTRO → alinear |
| OBS-06 | Succión step 2 **1.5 bar** (es la alarma AL) vs SP1 1.75 bar del Alarm List | Setpoint = Alarm List | OTRO → alinear |
| OBS-07 | Step 7 usa "PIT-09-002 ≤ 0 bar" (SP inexistente) | Criterio propio del chart, pero alinea a un SP real | PROPIO (menor) → corregir a SP existente |
| OBS-08 | Fórmula de brine flow con "/100" espurio (da 0.28 vs 28 m³/h) | Fórmula propia del chart | PROPIO (menor) → corregir |
| NOTE-01/06 | PHIT-09-006 rotulada "Temperature"; numeración; VE-09-002 "On/Off" siendo modulante; criterio fin flushing sin tag; paginación 8→9 | tags/housekeeping | OTRO + propio menor |

**Veredicto Sequence Chart: Code 2.** Es el documento con más ítems, pero **todos son alinear a los documentos que desarrollan cada dato** (CP para lógica/rampa, Alarm List para setpoints, Valve List para etapa) + 2 correcciones propias menores (fórmula, criterio step 7). Estructura y pasos (lo que el chart desarrolla) son correctos → incorporable a Rev 0.

## 4. IO List Rev 5 (P22-LI-09-008-001, IFC) → Code 2 (revierte a Code 1 si el heater está fuera de alcance)

**Cierres verificados:** conteo BOOL dosificadoras (N25) corregido; RUNNING FROM = LCP (no HMI); 4 señales de coordinación hardwired relay-contact; Pt-100 devanado+rodamiento ambos motores; vibración donde corresponde (ET §5.5.6); CCS real; sin TBD/placeholders.

| # | Hallazgo | ¿Lo desarrolla…? | Clasificación |
|---|---|---|---|
| OBS-01 | El interlock "Stop heater" del Alarm List no tiene canal de salida (DO/BOOL) del calefactor REL-09-001 en el IO List | Canal I/O = IO List (si el PLC controla el heater) | **PROPIO si el PLC lo controla** → agregar el punto en Rev 0 (Code 2). **Si el heater está fuera del alcance del PLC** → IO List correcto as-is (Code 1) y se corrige el Alarm List |
| NOTE-01/03 | tags VIT/ORPIT vs Instrument List; alineación Valve List/P&ID (huecos VE-09-001/011/015) | Tags/Valve List | OTRO → Sección 3 |

**Veredicto IO List: Code 2** (agregar el punto del heater o confirmar fuera de alcance → Code 1). El resto son tags cross-doc → Sección 3.

---

## Veredicto global TM N28: **2 — Approved as Noted** · Tally **4 Code 2** (IO List revierte a 3 Code 2 + 1 Code 1 si el heater se confirma fuera de alcance)

**Titular:** la familia de Control por fin se entregó completa (el Sequence Chart 017 llevaba 6-7 ciclos vencido) y cada documento es correcto en **lo que él desarrolla**; lo pendiente es una **reconciliación cruzada** de tags/setpoints entre los cuatro, que se incorpora al emitir Rev 0. Ningún documento requiere nueva revisión intermedia.

**Riesgo a cubrir en el correo/Sección 2 (advisor):** como los 4 van a Rev 0 y varias notas son "alinear entre ellos", deben re-emitirse como **conjunto coordinado** en una sola pasada, con dos definiciones que hoy no están cerradas en ninguno: (a) el **valor único de trip de vibración de la bomba HP** (hoy el Alarm List pone 10.0 inalcanzable, la CP 7.1) alcanzable dentro del rango del sensor o re-rangear; (b) el **mapeo winding/bearing** uniforme (Winding=001, Bearing=002) en la CP igual que en Alarm List/IO List/Instrument List. Con esas dos definiciones fijadas, la reconciliación a Rev 0 es determinista.

**Sección 3 (arrastre):** la condición de firma RTD del FAT Rev A (N27) queda **abierta** hasta que la CP Rev 0 refleje el mapeo correcto (los hijos ya lo tienen); el O&M Manual Rev B (N27 Code 3) sigue gated hasta que la familia cierre a Rev 0. Otros: HP/LP Pressure Test Rev D (75 bar PVC), UHPRO Structural Calc Rev B, GA Antiscalant Tank Rev C, Equipment Layout Rev D, SLD a reemitir, container base-bolt, Module Seismic.

**CC_ADASA:** los 4 documentos llevan CC_ADASA (Code 2 siempre lleva, §3.8). IO List: solo OBS-01 sobre el propio doc (NOTE cross-doc a Sección 3).
