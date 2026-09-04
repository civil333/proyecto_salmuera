---
titulo: Inspeccion 06 del 21-Ago-2026 — analisis ADASA del informe BVM-IR006
codigo: Informe BVM-IR006-21082026 / Annex 1
fecha: 2026-08-21
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Inspeccion 06 del 21-Ago-2026 — que se ensayo y contra que no se contrasto

**Documentos revisados:** `IR006-ADASA-BVM-21082026.pdf` (seis paginas, con texto extraible),
`Annex 1.pdf` (cuatro paginas escaneadas, leidas por render a 170 dpi) y el correo de remision de
Carlo Montecinos del 21-Ago 07:55 hora de Chile.

**Que es:** el informe de tercero inspector de Bureau Veritas, formato `GM-SI-101 INSP002-En` Rev 3.1,
de la jornada del 21 de agosto en el taller de Penang. Inspector Mohamad Fakhrul Radzi Bin Zainal,
coordinador Ahmad Hazwan, aprobado por Wan Mohd Adli W Yahya. Trabajo BVM 26/1366, Orden de Compra
836492.

---

## Lo que se ejecuto

| | Spool 1 | Spool 2 |
|---|---|---|
| Identificacion en el informe | **`CP-SSD-DN80-09-015`** (Jt 01 y 02) | **`CP-SSD-DN80-09-044`** (Jt 03 y 04) |
| Presion de diseno declarada | **5,0 bar** | **5,0 bar** |
| Presion de ensayo | **7,5 bar** | **7,5 bar** |
| Retencion | 30 minutos | 30 minutos |
| Caida de presion | Ninguna | Ninguna |
| Escalones de las fotografias | 3,75 → 5,6 → 7,5 → 5,25 → 5,0 | mismo registro |
| Manometros | `PSPP-26605337` y `PSPP-26605340` | mismos dos |

Titulo de la jornada en el informe: *"Witnessed **High Pressure** piping pressure test"*.

---

## Contra la Line List aprobada

Fuente primaria: `P22-LI-09-009-003` Rev 0, la que el propio procedimiento de ensayo
`P22-BA-09-000-010` adjunta y nombra por codigo y revision. Verificada en
`ENTREGAS_BWWATER/ENTREGA 63/md/P22-BA-09-000-010_C HP and LP Pressure Test Procedure_extracted.md`,
filas 286 y 298.

| Linea | Material | Servicio | Diseno barG | Hidrostatica barG |
|---|---|---|---|---|
| `CP-SSD-DN80-09-015` | SUPER DUPLEX STEEL SCH80S, DN80 | CIP FEED TO 2ND STAGE RO | **90** | **135** |
| `CP-SSD-DN80-09-044` | SUPER DUPLEX STEEL SCH80S, DN80 | 1ST STAGE CIP REJECT OUT | **80** | **120** |

🔴 **Los 5,0 barG que el informe declara como presion de diseno no corresponden a ninguna de las dos
lineas.** Ese es el valor de diseno de las lineas de PVC del modulo, cuya hidrostatica es de 7,5 barG.

🔴 **Las dos lineas se ensayaron a una decimoctava y a una decimosexta parte de su presion de hidrostatica** (7,5 contra 135 barG y 7,5 contra 120 barG).
Ninguno de los dos ensayos califica el tramo de super duplex.

**Diferencia con la jornada del 20 de agosto:** alli el TAG registrado, `DA-SSD-DN100-09-014`, no
existia en la Line List, de modo que la identidad de la linea quedaba abierta y ADASA pregunto antes
de exigir. Aca los dos TAG existen, son super duplex SCH80S y estan en la lista aprobada. La regla
anti-invencion se cumple afirmando, porque el hecho y la identidad estan los dos verificados.

---

## Los manometros

Certificados Trescal Malasia del `Annex 1`, leidos por render:

| Certificado | Equipo | Modelo | Rango | Calibracion | Recalibracion |
|---|---|---|---|---|---|
| `PSPP-26605340` | `FAC-MT-015` | WIKA EN 837-1, serie 8801GB5K | **0 bar a 16 bar** | 14-Jun-2026 | 14-Jun-2027 |
| `PSPP-26605337` | `FAC-MT-070` | WIKA 232.50.100, serie 50055918 | **0 bar a 16 bar** | 14-Jun-2026 | 14-Jun-2027 |

Son **los mismos dos manometros** del Spool 1 del 20 de agosto. Con rango de 16 bar es fisicamente
imposible ensayar a 120 o a 135 barG. La jornada se rotula como ensayo de alta presion.

Laboratorio acreditado SAMM 325, trazabilidad a NMIM y KRISS. La instrumentacion esta en regla; lo
que no calza es su rango contra la presion que las lineas exigen.

---

## Que marco Bureau Veritas en el informe

Verificado por render de la pagina 1 a 400 dpi, no por lectura del texto plano.

| Campo | Marca |
|---|---|
| Resultado de la inspeccion | **Satisfactory with comments (Pending)** |
| Open Non Conformities | **No** |
| Open Punch List Items | **No** |
| Release Note Issued | No |
| BV Traceability Stamping | No |

Resumen de la inspeccion, punto 1: *"Witnessed Pressure Piping Pressure Test of SDSS Piping spool,
and found satisfactory at time of inspection."* Punto 2: *"Result of testing on hold until BW Water
clarify with ADASA line list issues."* La misma salvedad se repite como punto 7 de la seccion E1, y
el punto 5 de esa seccion declara el ensayo *"satisfactory and acceptable"*.

**Calibracion del reclamo.** El informe **no** marca "Satisfactory without comments" y deja escrita la
salvedad, de modo que afirmar que reportaron todo sin problemas seria refutable. Lo objetable es otra
cosa: el ensayo se declara satisfactorio y aceptable, no se levanta No Conformidad ni punto de lista
de pendientes, y el dato de presion de diseno contradice el documento aprobado.

🔴 **La Line List no figura en la seccion B del informe**, que es la de documentacion de referencia.
Esa seccion lista el formulario `AQ-QAM-F027`, el ITP `P22-BA-09-000-004` Rev 0, un
`P22-BA-09-000-001` Rev 0 rotulado como Technical Specification, y el procedimiento
`P22-BA-09-000-010` Rev 0. El procedimiento que si citan es el que remite a la Line List por codigo
y revision para fijar la presion de ensayo.

---

## ADASA le entrego la Line List a Bureau Veritas

La **Guia del Paquete de Inspeccion de Taller** `ADASA-BV-PAQUETE-INSPECCION` Rev 1, del 21 de julio
de 2026, seccion 3.4, tabla de Ingenieria de referencia — Proceso y Mecanica:

> `P22-LI-09-009-003` · Line List · Rev **0** · Vigente (IFC) — Codigo 1 (N29) ·
> **"Visitas 2-3 — soldadura/hidrostatica"**

El archivo esta en
`PROGRAMA y CONTRATO/HITO BUREAU VERITAS/PAQUETE_INSPECCION_BV/05_INGENIERIA_REFERENCIA/PROCESO_MECANICA/P22-LI-09-009-003_0 Line List.pdf`.
No es un documento que el inspector debiera haber pedido: ADASA se lo entrego hace un mes y lo
asigno expresamente a la hidrostatica.

---

## Lo que la oferta de Bureau Veritas obliga

Oferta `600049` Rev.3 del 07-Jul-2026, contratada por la Orden de Compra 836492:

| Seccion | Texto literal |
|---|---|
| 3 — Alcance general | *"El reporte denominado 'Informe de Inspeccion' que es enviado **al dia siguiente** concluida la visita de inspeccion y que informa de forma inmediata si la visita fue satisfactoria y sus principales observaciones... y cuales (si hubiera) son las desviaciones encontradas"* |
| 3.2 — Consideraciones al servicio | *"Las No Conformidades o desviaciones detectadas por el inspector seran informados al Fabricante con copia a AGUAS ANTOFAGASTA, **en la misma visita**. Bajo la modalidad de informe **'Flash Report'** via correo electronico"* |
| 3.2 | *"Para una rauda comunicacion se enviara un **Flash Report inmediatamente terminada** la visita de inspeccion"* |

🔴 **No hubo Flash Report en la jornada del 20 ni en la del 21.** Es lo que queda en pie de este
bloque, y es reclamable: un carrete de super duplex ensayado a la presion de las lineas de PVC es una
desviacion, y la seccion 3.2 obliga a avisarla en la misma visita.

> ⚠️ **CORRECCION del 21-Ago.** Una version anterior de este analisis afirmaba que el informe de la
> jornada del 20 de agosto no habia llegado. **Es falso.** El `BVM-IR005-20082026` lo remitio Emylia
> Rosli el 20-Ago 23:35 hora de Chile, con Luis Rivera en copia, por la cadena
> `RE: 25007 TALTAL - Request to witness inspection 004`. Llego **dentro del plazo** de la seccion 3.
> El reclamo del plazo se retiro del correo antes de emitirlo. Analisis de ese informe en
> `../INSPECTION 05/_ANALISIS_INSPECCION_05.md`.

---

## Cronologia, que es lo que agrava el cuadro

| Momento | Hecho |
|---|---|
| 20-Ago 23:01 Malasia (11:01 Chile) | ADASA emite el correo de la hidrostatica: **ningun ensayo mas del circuito de super duplex** hasta confirmar por escrito la presion de cada linea. Bureau Veritas va en el To |
| 21-Ago 09:13 Malasia (20-Ago 21:13 Chile) | Adnin responde a su propio equipo: *"Please help to explain why we test this spool at 7.5bar. This spool that has two flange class, 900# and 150#. **We also have the same spool that will be test today**"* |
| 21-Ago, jornada de 9:00 a 17:00 | Se ensayan los dos spools a 7,5 barG. El inspector asiste y da la jornada por satisfactoria |
| 21-Ago 19:55 Malasia (07:55 Chile) | Carlo Montecinos remite el informe |

Adnin anuncio por escrito que iba a repetir el ensayo cuestionado el mismo dia, y lo hizo, con la
retencion de ADASA ya en su poder.

---

## El argumento de las dos clases de brida confirma un hallazgo abierto

El **Transmittal N30**, subseccion del conjunto de planos de taller `25007-ME-PI-0901`, levanto
literalmente sobre `CP-SSD-DN80-09-044` y `CP-SSD-DN65-09-045`:

> *"Undeclared specification break between the super duplex and PVC systems. On sheets 5, 6, 7 and 9
> the boundary between the two systems sits at an ANSI 150# flanged joint adjacent to a single
> motorised butterfly valve, with no specification break symbol and no line number split. The spools
> titled CP-SSD-DN65-09-045 and CP-SSD-DN80-09-044 incorporate PVC SCH 80 pipe while the approved
> Line List classifies both lines as super duplex at 80 to 90 barG design and 120 to 135 barG
> hydrotest, and rates the PVC lines at 5 barG design and 7.5 barG hydrotest."*

La explicacion del proveedor **es** ese hallazgo. Mientras la linea siga siendo una sola en la Line
List aprobada, se ensaya a la presion que esa lista le asigna. La brida clase 150 no cambia esa
presion; lo que hace es mostrar que el quiebre no esta declarado ni protegido. Y deja abierta una
pregunta que nadie ha respondido: como se protege el tramo de PVC del lado de alta con la valvula
motorizada cerrada.

---

## El patron CIP, visible solo al cruzar los dos informes

Con el `BVM-IR005` a la vista, las dos lineas de esta jornada dejan de ser un caso aislado. **Tres de
las cuatro lineas CIP de super duplex se ensayaron a 7,5 barG en dos jornadas consecutivas, y las
tres traen 5,0 barG de presion de diseno en el registro:**

| Linea | Jornada | Informe | Diseno real | Hidrostatica real |
|---|---|---|---|---|
| `CP-SSD-DN100-09-014` | 20-Ago | BVM-IR005 | 80 | **120** |
| `CP-SSD-DN80-09-015` | 21-Ago | BVM-IR006 | 90 | **135** |
| `CP-SSD-DN80-09-044` | 21-Ago | BVM-IR006 | 80 | **120** |
| `CP-SSD-DN65-09-045` | pendiente | — | 90 | **135** |

El taller esta tratando el circuito CIP completo como sistema de baja presion. La cuarta linea es la
otra que el Transmittal N30 nombro en el quiebre de especificacion, y por eso la retencion explicita
sobre ella encabeza las peticiones del correo al proveedor.

## Estado del Punto de Detencion

La fila 5.2 del ITP `P22-BA-09-000-004` Rev 0 es Punto de Detencion. Al cierre del 21 de agosto sigue
ensayada **una sola** linea de super duplex, la `DA-SSD-DN100-09-003` a 90 barG el 20 de agosto. Las
otras diez estan pendientes, incluidas las dos que la jornada del 21 pretende cubrir.

---

## Lo que se pide

**A BW Water,** por la cadena del Request to witness inspection 003/004, con plazo al lunes 24 de
agosto:

1. La confirmacion escrita pedida el 20 de agosto, vencida hoy.
2. El listado de **todo** spool de super duplex ensayado hasta la fecha, con TAG, presion, fecha,
   manometro y rango.
3. La respuesta al quiebre de especificacion del Transmittal N30.
4. Repetir a la presion de la Line List los ensayos de `CP-SSD-DN80-09-015`, `CP-SSD-DN80-09-044` y
   el spool del 20 de agosto.
5. Corregir los registros del 20 y del 21, incluido el item 5 del checklist de rango de manometro.
6. Confirmar que el taller dispone de manometros de rango adecuado para 120 y 135 barG.

**A Bureau Veritas,** por su propia cadena y sin nombrar al fabricante, con el mismo plazo:

1. Reemitir el `BVM-IR006-21082026` con la presion de diseno de la Line List.
2. Levantar la No Conformidad.
3. El informe del 20 de agosto y el Flash Report de ambas jornadas.
4. Incorporar la Line List a la documentacion de referencia de todo informe de ensayo de presion.
5. Instruir al inspector sobre la vigencia de la retencion.
6. Reserva de ADASA sobre la validez del atestiguamiento de los dias 20 y 21.

---

## Que no se levanta

- **El desempeno del inspector en terreno.** Asistio, firmo, reviso los certificados de calibracion,
  documento los escalones con fotografias y dejo escrita la salvedad de la line list. Lo que falla
  es el contraste documental y la via de aviso, no la presencia.
- **El formato del informe.** Es la plantilla `GM-SI-101 INSP002-En` Rev 3.1 de Bureau Veritas, que la
  propia oferta autoriza en su seccion 3.
- **El codigo `P22-BA-09-000-001` rotulado como Technical Specification** en la seccion B. La
  Especificacion Tecnica del modulo es `P22-ET-09-000-001-0`. Es aseo documental y se resuelve al
  reemitir; no se levanta como observacion propia.
- **La revision del procedimiento** `P22-BA-09-000-010`, citada como Rev 0 cuando el Transmittal N35
  del 20 de agosto aprobo la Rev 1 en Codigo 1. El informe se emitio antes de que esa aprobacion
  llegara al taller.
