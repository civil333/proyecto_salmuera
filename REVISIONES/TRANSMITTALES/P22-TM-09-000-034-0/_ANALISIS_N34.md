# Analisis interno — Transmittal N34 (P22-TM-09-000-034-0)

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.** Trazabilidad de la revision de las
> entregas E77 y E80. El instrumento que se envia es
> `P22-TM-09-000-034-0_TRANSMITTAL.md` y su Word.

**Fecha de analisis:** 18-Ago-2026
**Entregas cubiertas:** E73 (`25007-0073`), E77 (`25007-0077`) y E80 (`25007-0080`)
**Documentos:** 5
**Veredicto global propuesto:** 3 — To be revised (2 Codigo 1, 2 Codigo 2, 1 Codigo 3)

---

## 1. Recepcion y plazos

| Submittal | Emitido | Devolucion pedida por BW | Recibido por ADASA | Vencimiento real Clausula 37.2 |
|---|---|---|---|---|
| `25007-0073` | 11-Ago-2026 | — | 11-Ago-2026 | **20-Ago-2026** |
| `25007-0077` | 14-Ago-2026 | 17-Ago-2026 | **18-Ago-2026 07:49** | 27-Ago-2026 |
| `25007-0080` | 18-Ago-2026 | 21-Ago-2026 | 18-Ago-2026 09:58 | 27-Ago-2026 |

**Hecho contractual.** El `25007-0077` existe. El Transmittal N33, emitido el
17-Ago, pregunto por el porque la serie del proveedor saltaba del 0076 al 0078
y advirtio que, si el numero se habia emitido y no habia llegado, la recepcion
formal nunca ocurrio y los siete dias habiles de la Clausula 37.2 no habian
empezado a correr. Se confirma: el formulario lo fecha el 14-Ago y pide
devolucion al 17-Ago, un dia **antes** de que el documento llegara a ADASA. La
fecha de devolucion que trae el propio formulario es inejecutable. Los siete
dias habiles corren desde la recepcion efectiva del 18-Ago. Se declara sin
imputar.

**La `25007-0073` tampoco estaba ausente.** El README y el Transmittal N33 la
dan por inexistente. Esta en `ENTREGAS_BWWATER/ENTREGA 73/`, fechada el 11-Ago,
con dos documentos que llevaban siete dias sin responder y cuyo plazo de la
Clausula 37.2 vence el **miercoles 20-Ago**. Se incorpora a este transmittal por
decision del usuario. **Con esto la serie del proveedor no tiene numeros
ausentes.** Las dos afirmaciones del README se corrigen.

## 2. Higiene de carpeta (registro interno, no se emite)

- La carpeta de la E80 trae los dos archivos nativos `.dwg` que el Submittal
  Form no declara. **La lista real de la carpeta manda**; se anota, no se imputa.
- `ENTREGA 80/` conserva un residuo de copia SMB de 24 MB (`.smbdeleteAAA848590`)
  y el `Submittal Form_25007-0080.pdf` duplicado en la raiz y en `25007-0080-1/`.
- `P22-DWG-09-005-014` Rev B declara en su caratula "Page: 1 of 2" y el archivo
  trae tres paginas (la tercera es la hoja de comentarios consolidada).

---

## 3. `P22-DWG-09-005-011` Rev C — GA of Antiscalant Dosing Pump Skid

**Origen:** Codigo 2 en el Transmittal N26, con accion "to issue at IFC Rev 0 —
no new revision required". BW Water emitio de todos modos una revision
intermedia, fechada 13-Ago-2026, timbrada *Issued for Approval*. La revision
intermedia no se objeta: ADASA no la pidio pero tampoco la prohibio.

### Cierre punto por punto

| Punto N26 | Pedido | Declarado en la hoja consolidada | Verificado en la Rev C | Estado |
|---|---|---|---|---|
| OBS-01 (a) | Rotular cada bloque como fuerza por perno o total del grupo | "Reaction forces updated accordingly" | El bloque de notas 7.9.1 usa Σ y se titula TOTAL SEISMIC REACTION FORCES; el detalle rotula M10 HH BOLT C/W WASHER | **Cerrado** |
| OBS-01 (b) | Conciliar la fuerza por perno contra el informe de calculo endosado | "Reaction forces updated accordingly" | No concilia. Ver aritmetica abajo | **Declarado sin estarlo (2a vez)** |
| NOTE-01 | Informe de calculo endosado, entregable de otro documento | no declarado | La lamina sigue rotulando la nota 5 "BOLTING DETAILS TO BE FINALIZED AND ENDORSED." y la nota 7.9 "AS PER CALCULATION REPORT" | Abierto, cruzado (Seccion 3) |
| NOTE-02 | Verificacion positiva, sin accion | no declarado | — | Sin accion, correcto |

### Aritmetica verificada por render a 300 dpi

Bloque total, nota 7.9.1 de la lamina, con cantidad de pernos = 10 (nota 7.2):

- Σ Fx = 1,0242 kN (SEISMIC SHEAR)
- Σ Fy = 1,4632 kN (DEAD LOAD, VERTICAL)
- Σ Fz = 1,0242 kN (BOLT SHEAR)

Detalle por perno, rotulo "M10 HH BOLT C/W WASHER":

- Fx ≈ 0,102 kN → 1,0242 / 10 = 0,10242 **concilia**
- Fy ≈ 0,146 kN → 1,4632 / 10 = 0,14632 **concilia**
- Fz ≈ 0,205 kN → 1,0242 / 10 = 0,10242 **no concilia, factor 2,00**

La Rev B tenia el mismo desajuste con factor 10 (total 0,2048 contra 0,205 por
perno). La Rev C corrigio Fx, agrego Fy y **dejo Fz sin conciliar**, ahora en
factor 2. El valor por perno no se movio entre revisiones.

Observacion subsidiaria, que no se emite como punto aparte: Σ Fz aparece
rotulada "(BOLT SHEAR)" con el mismo valor que Σ Fx "(SEISMIC SHEAR)", cuando
Fz en un anclaje suele ser traccion. Va como contexto dentro del mismo punto,
no como comentario nuevo.

### Disposicion

**Codigo 2 — Approved as noted.** El determinante de la Seccion 6.2 se cumple:
lo que queda es una cifra y su rotulo, incorporables al emitir Rev 0 sin
revision intermedia, y es la misma disposicion que ADASA dio en el N26. Se
mantiene el codigo pero el Status **declara que es la segunda vez** que el
bloque vuelve sin conciliar y que la hoja consolidada lo dio por corregido.

**Vinculo con el endoso profesional.** El punto pide conciliar contra el informe
de calculo endosado. El 17-Ago BW Water informo que el ingeniero chileno que le
certificaba los documentos no esta disponible, y la Rev C de esta lamina sigue
rotulando el detalle de anclaje como pendiente de endoso. Se declara en el
transmittal y se remite al correo del 18-Ago. **No se abre el eje del plazo de
entrega vencido ni la multa: es otra cadena.**

---

## 4. `P22-DWG-09-005-014` Rev B — GA of CIP / Flushing Tank

**Origen:** Codigo 2 en el Transmittal N26, misma accion "to issue at IFC Rev 0
— no new revision required". Revision intermedia fechada 14-Ago-2026.

### Cierre punto por punto

| Punto N26 | Pedido | Declarado | Verificado en la Rev B | Estado |
|---|---|---|---|---|
| OBS-01 | Agregar el TAG TK-09-001 | "Equipment tag added into the GA drawing" | La Rev A no traia `TK-09-001` en ninguna parte de la lamina; la Rev B lo incorpora en el cajetin | **Cerrado** |
| OBS-02 | Declarar que documento gobierna y conciliar la tabla de boquillas con el Datasheet aprobado | "Nozzle schedule reconciled with Datasheet" | Las tres entradas en disputa son identicas a las de la Rev A | **Declarado sin estarlo** |
| NOTE-01 | Cargas sismicas del anclaje, entregable de otro documento | no declarado | — | Abierto, cruzado (Seccion 3) |
| NOTE-02 | Verificacion positiva, sin accion | no declarado | — | Sin accion, correcto |

### Contraste contra el Datasheet aprobado `P22-ET-09-009-009` Rev B (Codigo 1, TM N3)

| Entrada | GA Rev B | Datasheet Rev B | Estado |
|---|---|---|---|
| Abertura superior | MH — MANHOLE ID 533 mm | HH — Handhole DN300 top | En disputa |
| N42 | SPARE 1" | no figura | En disputa |
| N97 | TEMPERATURE SENSOR 1½" | no figura | En disputa |
| N01/N02/N03/N41/N75/N80/N81/N85/N90/N91/N94/N96 | 3"/4"/4"/1"/3"/4"/2"/6"/1"/1"/1½"/3" | DN80/DN100/DN100/DN25/DN80/DN100/DN50/DN150/DN25/DN25/DN40/DN80 | Consistentes |

Ninguno de los dos documentos cambio. El Datasheet tampoco fue reemitido: su
unica revision posterior a la Rev A es la Rev B de la E7, aprobada en Codigo 1.

**Matiz de equidad que debe ir en el texto.** El propio Datasheet es
inconsistente consigo mismo: su tabla de boquillas lista "HH Handhole DN300"
mientras su descripcion constructiva del estanque dice "Cover: Welded Conical
C/W Manhole Cover". Por eso el pedido del N26 no fue "corrija el plano" sino
"declare cual gobierna y concilie". Sigue sin declararse.

### Disposicion

**Codigo 2 — Approved as noted.** Uno de los dos puntos cerro; lo que queda es
una declaracion y el alineamiento del documento que pierda, incorporables al
emitir Rev 0. El contenido propio del plano no esta mal de raiz. La reemision
del Datasheet, si es el que pierde, se sigue como entregable cruzado.

### Lo que se RETIRA del transmittal

La primera version levanto una **NOTE-01** porque la caratula declara "Page 1 of
2" y el archivo trae tres paginas. **Sale**, y el hecho queda solo en este
analisis: es una **observacion nueva**, ajena al universo de los cuatro puntos
del TM N26, sobre un documento que se revisa unicamente por cierre de
comentarios. Ademas es housekeeping documental, que por regla no degrada.
Retirada a peticion del usuario, junto con la correccion del veredicto de la
Alarm and Interlock List; mismo modo de falla en los dos casos.

---

## 5. `P22-BA-09-000-013` Rev B — Quality Dossier Index

**Origen:** Codigo 3 en el Transmittal N30 con diez puntos (OBS-01 a OBS-06 y
NOTE-01 a NOTE-04) y accion "re-issue as Rev B".

**Alcance de esta revision:** a fondo, no solo cierre de comentarios. Es la
excepcion al criterio del N33, porque la funcion del documento es ser el
checklist del dossier y un capitulo que falta deja sin ubicacion un registro que
gatilla pago (items 8.3 y 8.4 del PIE Base).

**Lo que cambio.** De 27 capitulos (Rev A) a 49 (Rev B): A1, B1-B11, C1-C21,
D1-D13, E1-E3. Se agregaron dos columnas, "Doc No-REV/Status" e "ITP No.".

### Cierre punto por punto

| Punto N30 | En la hoja consolidada | Verificado en la Rev B | Estado |
|---|---|---|---|
| OBS-01 — numero, revision y estado de inclusion por linea, y referencia cruzada a la fila del ITP | "Revised as per comment" | Las dos columnas existen y estan mayormente vacias: la seccion B trae numero sin revision ni estado y sin fila de ITP; la C trae fila de ITP sin numero de documento; las D y E no traen ninguna de las dos. **El estado de inclusion no figura en ninguna linea** | **Cierre parcial** |
| OBS-02 — capitulo de preparacion para despacho | "Revised as per comment" | C9 (8.1) y C10 (8.2) agregados. Falta el packing list y no se nombra el marcado | Cerrado con residuo |
| OBS-03 — capitulo del Acta de Aprobacion FAT emitida por ADASA | "Revised as per comment. Section C21" | C21 se titula "Certificate Release ADASA" y referencia ITP 8.4, que es el **Release for Dispatch**. El Acta de Aprobacion FAT es la fila **7.9** del ITP y no tiene capitulo | **Declarado sin estarlo** |
| OBS-04 — donde se archiva el paquete de recipientes a presion | "Revised as per comment. Section D" | D6 "RO Pressure Vessel" | **Cerrado** |
| OBS-05 — certificados de fabricante y ensayos de fabrica de los equipos principales | "Revised as per comment. Section D and E" | D1-D13 equipo por equipo y E1-E3. No se nombran motores ni variadores | Cerrado con residuo |
| OBS-06 — calificacion del personal de inspeccion y calibracion de equipos de ensayo | **no declarado** | B3 a B6 pasaron a decir "/Tech Qualification /Calibration" y se agrego C18 "Testing and Inspection calibration certificate" | **Cerrado, sin declarar** |
| NOTE-01 — declarar si es el indice preliminar (ITP 7.6) o el final (ITP 8.3) | **no declarado** | No se declara. El documento cambio de nombre de "Fabrication and Testing Dossier Index" a "Quality Dossier Index" bajo el mismo codigo, sin decir cual de los dos es | **Abierto** |
| NOTE-02 — procedimientos B3, B4 y B6 sin someter | **no declarado** | Cerro por otra via: llegaron en la E75 y volvieron en Codigo 3 con el TM N32 | Cerrado por otra via, sigue en Seccion 3 |
| NOTE-03 — identificar spool por spool los certificados de colada del super duplex | **no declarado** | C1 "Material Traceability Report & MTCs" con ITP 2.1, sin la identificacion spool por spool | **Abierto** |
| NOTE-04 — capitulos de no conformidades y reparacion de soldadura | **no declarado** | C19 y C20 agregados, ambos con ITP 7.9 | **Cerrado, sin declarar** |

### El punto que fija el veredicto: OBS-03

La Especificacion Tecnica `P22-ET-09-000-001-0`, Section 8, dice literalmente
que la validacion de las FAT "se materializara mediante la emision de un **Acta
de Aprobacion FAT** por parte de ADASA, cuya emision constituye un hito de
control definido en el PIE Base Item **7.9**", y que "tanto el protocolo de
pruebas FAT generado por el Proveedor como el Acta de Aprobacion FAT emitida
por ADASA **formaran parte integral e indispensable del dossier final de calidad
del modulo**".

El ITP aprobado `P22-BA-09-000-004` Rev 0 lo confirma con dos filas distintas:

- **Fila 7.9** — "FAT Approval Certificate Issuance by ADASA", punto de
  detencion.
- **Fila 8.4** — "Release for Dispatch (Formal ADASA Certificate Issuance)",
  cuyo registro se llama exactamente "Certificate Release ADASA".

El C21 de la Rev B es la fila 8.4. El Acta de Aprobacion FAT de la fila 7.9
sigue sin capitulo. La hoja consolidada lo da por incorporado.

### El punto que impide disponer el documento: NOTE-01

El ITP distingue dos indices con nombre propio: el preliminar
`PROV-LIST-DOSS-PRE-001` de la fila **7.6**, que ADASA revisa, y el final
`PROV-LIST-DOSS-FIN-001` de la fila **8.3**, que es **punto de detencion para
ambas partes**. La Rev B no declara cual de los dos es. Sin esa declaracion no
se puede disponer si el documento descarga la 7.6 o la 8.3, y la 8.3 sostiene
el 40% del pago.

### Disposicion

**Codigo 3 — To be revised.** Dos razones, y la segunda es la que decide:

1. OBS-01, que es la observacion que motivo el Codigo 3 del N30, vuelve
   cosmeticamente cerrada: las columnas existen y el contenido que las hace
   utiles no. El indice sigue sin poder funcionar como checklist.
2. Si el documento se dejara ir a Rev 0, el proximo estado que ADASA veria
   seria el indice final en la fila 8.3, que es punto de detencion. No cabe
   pasar sin revision intermedia un entregable que gatilla pago cuando su
   observacion principal no cerro y otra se declaro cerrada sin estarlo.

**No se levantan** (verificado contra la solicitud original, regla
anti-invencion): la eliminacion de los capitulos C1 a C3 de la Rev A (planos GA,
planos de fabricacion y P&ID), que ADASA nunca pidio conservar y que la ET no
exige dentro del dossier; y la referencia ITP 7.9 en C19 y C20, que sigue la
cita que la propia NOTE-04 de ADASA uso.

**El indice no es el dossier.** El item 65 del Master Register, el Dossier de
Fabricacion y Pruebas como entregable de la ET Section 7, sigue en NOT DELIVERED
y este codigo no lo afecta.

---

## 6. `P22-LI-09-008-015` Rev 0 — Alarm and Interlock List

**Origen:** Codigo 2 en el Transmittal N28 con cuatro puntos. Llega en Rev 0,
de modo que la revision es **binaria contra la condicion**: no hay mecanismo de
Codigo 2 sobre un Rev 0. Trae hoja de comentarios consolidada completa, con los
cuatro puntos.

| Punto N28 | Declarado | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| OBS-01 — el disparo de vibracion 10,0 mm/s satura en un transmisor de 0 a 8,9 mm/s; bajar el disparo o re-rangear el transmisor **en la Instrument List** y confirmar el valor | "the maximum range will re-configure to 12 mm/s RMS in the rev.0" | Item 6.0 declara rango 0,0 a 12,0 mm/s y el 6.1 el disparo en 10,0. Dentro del documento cierra. **Pero la Instrument List Rev E, aprobada en Codigo 1 en el Transmittal N20, sigue listando `VT-09-001` en 0,0 a 8,9 mm/s rms** y no fue reemitida | **Cerrado en este documento, abierto en el que gobierna** |
| OBS-02 — la alarma del interruptor de entrada apunta a `P22-PLC01-XT001`, que no existe en la IO List | "Tag number has been revised to P22-PLC01-XA001" | Items 34.0 y 34.1 con `P22-PLC01-XA001`, condicion "Breaker Open Contact", accion alarma mas parada del sistema | **Cerrado** |
| NOTE-01 (a) — unificar `VIT-09-001` a `VT-09-001` | "typo error ... revised in rev.0" | Cero ocurrencias de `VIT-09-001`; tres de `VT-09-001` | **Cerrado** |
| NOTE-01 (b) — alarmar las fallas de VE-09-014, VE-09-016 y las dos dosificadoras | "All related valves and dosing pump fault alarm are added to the rev.0" | Las cuatro filas existen. **Dos llegan con el TAG mal formado**: `VE09-014-XT001` y `VE09-016-XT001`, sin el guion que llevan las trece filas de valvula restantes y que la IO List Rev 5 usa. Verificado por render a 300 dpi de la pagina 8: las dos filas nuevas estan en rojo y sin guion, mientras `VE-09-012`, `VE-09-013` y `BDS-09-001` lo llevan | **Cerrado con defecto propio** |
| NOTE-02 (a) — declarar el diferencial numerico de falla de sobrealimentacion del turbocargador | "No changes in rev.0" mas la explicacion | Items 13.5 y 13.6, `PIT-09-007.SP1` y `.SP2` en 10,0 bar con la condicion `(PIT-09-007 - PIT-09-005)` | **Cerrado** |
| NOTE-02 (b) — unificar los sub-tags de `FIT-09-005` | "typo error ... revised" | El patron `.FAHH/.FAH` desaparecio; items 26.1 a 26.7 en `.AHH/.AH/.AL/.ALL/.SP1/.SP2/.SP3` | **Cerrado** |
| NOTE-02 (c) — renumerar los items duplicados 5.7 y 13.4 | "revised" | Cada numero aparece una sola vez | **Cerrado** |
| NOTE-02 (d) — confirmar el rango de `TIT-09-006` | "Transmitter range will calibrated to 100C at 20mA" | Item 23.0 con rango 0,0 a 100,0 C | **Cerrado** |

### El pendiente que queda, y donde vive

BW Water eligio la segunda de las dos rutas que el Transmittal N28 ofrecio:
re-rangear el transmisor. La ruta exigia hacerlo **en la Instrument List**. La
Alarm List Rev 0 declara 12,0 mm/s; la **Instrument List Rev E sigue en 8,9 mm/s
rms** con el sensor Wilcoxon PCH420V-M12, y es documento aprobado en Codigo 1.
Mientras no se reemita, la definicion aprobada del instrumento satura por debajo
del disparo y el enclavamiento "Stop HP Pump" por vibracion sigue sin poder
actuar sobre un motor de 93 kW. La hoja consolidada no menciona la reemision.

**El defecto vive en la Instrument List, no en la lista revisada.** La Alarm List
Rev 0 es coherente consigo misma: el item 6.0 declara el rango de 0 a 12,0 mm/s
y el 6.1 pone el disparo en 10,0, dentro de ese rango. A este documento no cabe
pedirle nada mas.

**ADASA declara el valor vinculante** (decision del usuario, regla del proyecto
para un dato que dos documentos declaran distinto): el rango vinculante de
`VT-09-001` es **0 a 12 mm/s rms**, y la reemision de la Instrument List
`P22-LI-09-008-003` se exige a ese valor. No se pregunta cual gobierna: preguntar
deja el disparo por vibracion sin definir un ciclo mas, con fabricacion en curso.

### Disposicion

**Codigo 1 — Approved.** Sobre un Rev 0 la pregunta no es si hay observaciones
sino si el defecto es **intrinseco al documento o vive en otro**. Los dos
pendientes caen del lado que no degrada:

- El rango vinculante se corrige en **otro** documento -> Seccion 3, aunque la
  Instrument List ya este aprobada en Codigo 1 (ahi la accion es que *esa* se
  corrija).
- Los dos TAG sin guion son **housekeeping documental**, que por regla nunca
  degrada por si solo. Las cuatro filas de alarma que el comentario pedia estan;
  lo que falta son dos guiones. Van como **una linea del bloque de accion**, para
  corregir en la proxima emision natural, sin `CC_ADASA`.

> **Registro del modo de falla.** La primera version de este analisis codifico el
> documento **3 — To be revised**, y el usuario lo objeto. Fue over-reach en los
> dos frentes: degradar por un defecto que vive en otro documento, y tratar como
> sustantivo un housekeeping de dos caracteres. La regla esta en
> `feedback_rev0_solo_code1_o_code3` y el precedente son los dos primeros Rev 0
> del proyecto, ambos Codigo 1 en el TM N29 con sus residuales declarados para la
> proxima emision. Segunda vez que el criterio se aplica de mas sobre un Rev 0.

---

## 7. `P22-LI-09-008-017` Rev 0 — Control and Sequence Chart

**Origen:** Codigo 2 en el Transmittal N28 con siete puntos. Revision binaria.
La hoja consolidada trae seis filas: **falta OBS-06**, que sin embargo cerro.

| Punto N28 | Declarado | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| OBS-01 — la Nota 5 dispara el bypass del turbocargador por "Low TDS value" cuando la Control Philosophy lo gobierna por el lazo de presion | "revised in rev.0 note 5" | La Nota 5 dice ahora que `VE-09-002` se controla por el lazo PID de presion con `PIT-09-005` y que el TDS solo selecciona el setpoint y no inicia ni cierra el bypass | **Cerrado** |
| OBS-02 — el aborto por sobrepresion de la segunda etapa dispara a 90 bar contra los 93 bar de la Alarm List | "Setpoint 93 bar has been revised" | "exceeds 93 bar, instantly abort the sequence" | **Cerrado** |
| OBS-03 — la rampa del variador declara 1 Hz/s contra los 0,1 a 0,3 Hz/s de la Control Philosophy | "revised to 0.1 to 0.3 Hz/sec" | Las seis rampas de la secuencia de servicio pasan a 0,1 a 0,3 Hz/s | **Cerrado** |
| OBS-04 — el enjuague usa 40 m3/h fijos contra los setpoints por etapa de la Alarm List | "stated in flushing sequence with added note 9" | La Nota 9 declara 48 m3/h para etapa 1 y 36 m3/h para etapa 1 mas 2, controlados por `FIT-09-005` en PID y citando la Alarm List | **Cerrado** |
| OBS-05 — `VE-09-010` con tres asignaciones de etapa distintas | "revised in rev.0" | `VE-09-009` = segunda etapa y `VE-09-010` = primera, como fija la IO List Rev 5 | **Cerrado** |
| OBS-06 — permisivo de succion 1,5 contra SP1 1,75 bar; criterio del paso 7; formula de caudal de salmuera con un `/100` espurio | **no declarado** | 1,75 bar; el paso 7 pasa a `PIT-09-002 <= SP`; la formula queda `(Global Permeate Flow SP / Global Recovery Rate) x (1 - Global Recovery Rate)`, sin `/100` | **Cerrado, sin declarar** |
| NOTE-01 — `PHIT-09-006` rotulado como transmisor de temperatura; `VE-09-002` como valvula on/off; numeros duplicados; caratula "Page 1 of 8" | "housekeeping correction have been revised" | `PHIT-09-006` figura como analizador de pH; el rotulo de transmisor de temperatura queda solo en `TIT-09-006`, que es correcto; la caratula dice "Page: 1 of 9" | **Cerrado** |

### Lo que se verifico y NO se levanta

La pagina 8, secuencia de operacion CIP, conserva dos "Ramp up at 1 Hz/Sec.", en
el arranque de la bomba CIP y en el de la bomba de enjuague. **No es hallazgo.**
El limite de 0,1 a 0,3 Hz/s de la Control Philosophy Rev 1 esta escrito en la
seccion de la bomba de alta `BH-09-001` —cita `PIT-09-001`, `PIT-09-002`,
`VT-09-001` y el NPSH de 4,2 m— y la Control Philosophy **no fija rampa para
`BH-09-002`**. Exigirlo seria over-reach: aplicacion de la regla anti-invencion
de la Seccion 6.2 del CLAUDE.md.

### Disposicion

**Codigo 1 — Approved.** Los siete puntos cerraron, uno de ellos sin que la hoja
consolidada lo declarara. Sin `CC_ADASA`.

---

## 8. Resumen de disposicion


| Documento | Rev | Entrega | Codigo | Que falta |
|---|---|---|---|---|
| `P22-LI-09-008-015` Alarm and Interlock List | 0 | E73 | **1** | Nada en este documento. Reemision de la Instrument List al rango vinculante -> Seccion 3; dos TAG a la proxima emision natural |
| `P22-LI-09-008-017` Control and Sequence Chart | 0 | E73 | **1** | Nada |
| `P22-BA-09-000-013` Quality Dossier Index | B | E77 | **3** | Llenar las columnas de revision y estado, agregar el capitulo del Acta de Aprobacion FAT, y declarar si es el indice de la fila 7.6 o de la 8.3 |
| `P22-DWG-09-005-011` GA of Antiscalant Dosing Pump Skid | C | E80 | **2** | Conciliar Fz por perno con el bloque total (2a vez) |
| `P22-DWG-09-005-014` GA of CIP / Flushing Tank | B | E80 | **2** | Declarar que documento gobierna la abertura superior y las boquillas N42 y N97 |

**Veredicto global: 3 — To be revised.** Recuento: 2 Codigo 1, 2 Codigo 2,
1 Codigo 3. El veredicto lo fija **un solo documento**, el Quality Dossier Index.

Llevan `CC_ADASA` los **tres** documentos con observaciones abiertas: los dos
Codigo 2 por la regla de que todo Codigo 2 se anota, y el Codigo 3 por
definicion. Los dos Codigo 1 no llevan. El `CC_ADASA` de la Alarm and Interlock
List y su script quedan como traza interna en `_analisis_no_anotado/`.

## 9. Lo verificado y NO emitido, por documento

Registro para no repetir el modo de falla, y para tener trazabilidad si el
defecto reaparece en el dossier o en terreno.

| Documento | Hallazgo verificado | Por que no se emite |
|---|---|---|
| Alarm and Interlock List Rev 0 | Los TAG `VE09-014-XT001` y `VE09-016-XT001` sin guion no resuelven contra la IO List Rev 5 | Housekeeping documental; va como una linea del bloque de accion, sin degradar ni anotar |
| GA of CIP / Flushing Tank Rev B | La caratula declara dos paginas y el archivo trae tres | Observacion nueva, fuera del universo del TM N26 |
| Quality Dossier Index Rev B | El titulo cambio de "Fabrication and Testing Dossier Index" a "Quality Dossier Index" bajo el mismo codigo | Se pliega a la OBS-03 (cual de los dos indices es), no como punto propio |
| Quality Dossier Index Rev B | La Rev B elimino los capitulos C1 a C3 de la Rev A (planos GA, planos de fabricacion y P&ID) | ADASA nunca pidio conservarlos y la ET no los exige dentro del dossier: regla anti-invencion |
| Control and Sequence Chart Rev 0 | Dos rampas de 1 Hz/s en la secuencia CIP | La Control Philosophy no fija rampa para `BH-09-002`; el limite de 0,1 a 0,3 Hz/s es de la bomba de alta |
