---
titulo: Informe de ensayo hidrostatico del 20-Ago-2026 — analisis ADASA
codigo: Inspection Request 004 / Taltal Hydrotest Report BV W 20Aug
fecha: 2026-08-20
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Ensayo hidrostatico del 20-Ago-2026 — que dice el informe y que no cuadra

**Documento revisado:** `Taltal Hydrotest Report BV W 20Aug.pdf`, nueve paginas, recibido el 20-Ago. Sin texto extraible: son imagenes escaneadas, de modo que todo lo de abajo esta leido por render a 150 a 420 dpi.

**Contenido:** un Inspection Request Form `AQ-QAM-F027` firmado, dos informes de ensayo `AQ-QAM-F018` Rev 4 con sus hojas de adjuntos fotograficos, y cuatro certificados de calibracion Trescal.

---

## Lo que se ejecuto

| | Spool 1 | Spool 2 |
|---|---|---|
| Equipment Name | Super Duplex piping spool - Spool 1 | Super Duplex piping spool - Spool 2 |
| DWG / PID No. | `PI-0901-0006` | `PI-0901-0010` |
| Item ID / Line ID | **`DA-SSD-DN100-09-014`** | **`DA-SSD-DN100-09-003`** |
| Presion de ensayo | **7,5 bar** | **90 bar** |
| Horario | 3:39 pm a 4:09 pm | 9:55 am a 10:25 am |
| Caida de presion | 0 | 0 |
| Manometros | `FAC-MT-015` y `FAC-MT-070` | `FAC-MT-012` y `FAC-MT-013` |
| **Rango de esos manometros** | **0 a 16 bar** | **0 a 160 bar** |
| Escalones del grafico | 3,75 → 5,6 → 7,5 → 5,25 → 5 | 45 → 67,5 → 90 → 67 → 45 |
| Firma Bureau Veritas | Si, 20/08/2026 | Si, 20/08/2026 |

El Inspection Request declara `Inspection Item: 1 - HP piping pressure test`, jornada de 9:00 a 17:00 del 20-Ago en BW Water Penang, resultado **Accepted**, con firma y timbre de BW Water y de Bureau Veritas. Su nota manuscrita dice, literal: *"#7 has been done and found satisfactory during testing. Item 10: DA-SSD-DN100-09-003 and DA-SSD-DN100-09-014."*

---

## Lo conforme

**El Spool 2 esta bien ensayado.** La Line List `P22-LI-09-009-003` Rev 0 fija para `DA-SSD-DN100-09-003` (RO HP FEED PUMP DISCHARGE, super duplex SCH80S, DN100, diseño 60 barG) una hidrostatica de **90 barG**. Se ensayo exactamente a 90 barG, escalonado 45 → 67,5 → 90 con retencion de treinta minutos y caida nula, con manometros de rango 0 a 160 bar. No hay observacion que hacer.

**Bureau Veritas asistio y firmo.** Los dos informes y el Inspection Request llevan el timbre de la oficina de Malasia y la firma del inspector con fecha 20/08/2026. Es la primera jornada de esta serie con constancia completa de asistencia, y cierra por los hechos el reclamo de que las pruebas se ejecutaban sin testigo.

**La instrumentacion esta en regla.** Los cuatro manometros son WIKA calibrados por Trescal Malasia el 14-Jun-2026, con recalibracion al 14-Jun-2027, laboratorio acreditado SAMM y trazabilidad a NMIM y KRISS.

**El registro grafico presion contra tiempo si se produce.** Las hojas de adjuntos traen la fotografia de un `PRESSURE TEST RECORD CHART` dibujado a mano, con los escalones, las horas de inicio y termino de cada uno y las firmas de BW Water y del inspector. Esto **precisa la observacion abierta sobre el procedimiento `P22-BA-09-000-010`**: el grafico existe como practica, pero se levanta en un formulario que no tiene numero de documento ni revision y que el procedimiento no incorpora ni identifica. Lo que falta no es la practica, es el control documental de ese formulario.

---

## Lo que no cuadra

🔴 **El Spool 1 se ensayo a 7,5 barG, y ninguna linea de super duplex de este proyecto se ensaya a esa presion.**

Las once lineas de super duplex de la Line List Rev 0, que es la que el propio procedimiento de ensayo adjunta, tienen presion de hidrostatica de **75, 90, 120 o 135 barG**:

| Linea | Diseño barG | Hidrostatica barG |
|---|---|---|
| `DA-SSD-DN100-09-003` | 60 | 90 |
| `DA-SSD-DN100-09-004` | 80 | 120 |
| `DA-SSD-DN80-09-005` | 80 | 120 |
| `DA-SSD-DN80-09-006` | 90 | 135 |
| `DA-SSD-DN65-09-007` | 90 | 135 |
| `DA-SSD-DN65-09-008` | 50 | 75 |
| `DA-SSD-DN65-09-009` | 50 | 75 |
| `CP-SSD-DN100-09-014` | 80 | **120** |
| `CP-SSD-DN80-09-015` | 90 | 135 |
| `CP-SSD-DN80-09-044` | 80 | 120 |
| `CP-SSD-DN65-09-045` | 90 | 135 |

**7,5 barG es la presion de ensayo de las lineas de PVC** de diseño 5 barG, y es el valor que la fila 5.1 del ITP asigna al sistema de baja presion.

🔴 **El TAG `DA-SSD-DN100-09-014` no existe en la Line List aprobada.** La serie `DA-SSD-DN100` solo tiene la `-003` y la `-004`. El correlativo `09-014` corresponde a **`CP-SSD-DN100-09-014`**, CIP FEED TO 1ST STAGE RO, super duplex SCH80S DN100, diseño 80 barG, **hidrostatica 120 barG**. El TAG aparece dos veces con el prefijo equivocado: en el formulario de ensayo y en la nota manuscrita del Inspection Request firmado, de modo que no es un error de tipeo suelto en una celda.

**El rango de los manometros prueba que el ensayo se planifico a baja presion.** `FAC-MT-015` y `FAC-MT-070` son de 0 a 16 bar: fisicamente no pueden medir 120 ni 135 barG. Y el item 5 del checklist del formulario — *"Pressure gauge/recorder ranges are > 1.5 and < 4 times the required test pressure?"* — esta marcado **Yes**, lo que solo es cierto si la presion requerida es 7,5 barG (16/7,5 = 2,1). Con 120 barG requeridos, ese mismo item tendria que haberse marcado No.

**Sea cual sea la lectura, hay un problema.** Si el spool ensayado es la `CP-SSD-DN100-09-014`, se sometio a menos de un decimosexto de la presion que la Line List exige, y el ensayo no la califica. Si es otra linea, el registro que entra al dossier la identifica con un TAG que no existe. Y en los dos casos la jornada se rotula **HP piping pressure test** y se acepta, con lo que un spool de alta queda declarado ensayado sin haberlo sido.

---

## La regla de presion de prueba y el hueco del procedimiento

Esta seccion se agrego el 20-Ago a raiz de una pregunta del usuario — si aceptar 90 barG contradecia lo aprobado — y es la que fija el encuadre de todo lo anterior.

### La cadena documental, de arriba abajo

| Documento | Estado | Que fija |
|---|---|---|
| **PIE Base** `P22-IT-09-000-001-0`, fila 5.2 | Base de licitacion, ADASA | *"Presion Prueba = **1.5 x P.diseño** = Y bar"*. El factor, con el valor como marcador a rellenar |
| **ITP** `P22-BA-09-000-004` Rev 0 | **Codigo 1, TM N26** | *"Test Pressure = 1.5 x Design Pressure (90 bar) = **135 bar**"*. Instancia el factor sobre el diseño MAS ALTO del circuito |
| **Line List** `P22-LI-09-009-003` Rev 0 | **Codigo 1, TM N29** | Desagrega linea por linea. Relacion 1,5 exacta en las **34 filas**. Seis valores: 135, 120, 90, 75, 7,5 y 3 barG |
| **Procedimiento** `P22-BA-09-000-010` Rev 1 | Codigo 1, TM N35 | Clausula 5.5.12: *"HP piping will test to 135 bar, and LP will test to 7.5 bar. Testing pressure will refer in approved line list"* |

**El factor es 1,5 y se aplica sobre la presion de DISEÑO, no sobre la de operacion.** Verificado por barrido del arbol completo: **el 1,25 no existe en este contrato**; su unica aparicion es el paso de rosca de un tornillo M8x1,25 en un datasheet de vibracion. La ET no escribe factor: remite al PIE en su Seccion 8.1.

### Por que los 90 barG del Spool 2 son conformes

`DA-SSD-DN100-09-003` opera a 51 barG y esta diseñada para **60**. La cadena es 60 x 1,5 = **90 barG**, que es lo ensayado. Conviene ver las cuatro combinaciones posibles del criterio, porque despeja la duda de raiz:

| Base | Factor 1,25 | Factor 1,5 |
|---|---|---|
| Operacion, 51 barG | 63,75 | 76,5 |
| **Diseño, 60 barG** | 75 | **90 ← lo ensayado** |

Los 90 barG son el valor **mas alto** de las cuatro. Bajo ninguna lectura del criterio se ensayo por debajo.

**Por que su diseño es 60 y no 90:** la bomba de alta descarga a 51 barG y son los turbochargers los que elevan el feed. El datasheet del Feed Turbocharger `P22-ET-09-009-007` Rev D declara *"Feed Boost Pressure 19,6 bar"*, de modo que 51 mas el boost da los 70 barG del feed de primera etapa. La presion de diseño de 60 barG para la descarga es coherente con el proceso.

### El hueco: un binomio contra una tabla de seis

La clausula 5.5.12 da dos instrucciones incompatibles en una sola frase. Y **el factor 1,5 no esta escrito en ninguna parte del procedimiento**: estaba en la Rev C, se perdio en la Rev D, y el TM N32 decidio no reclamarlo porque el TM N29 ya habia aprobado esa revision. El 20-Ago el taller aplico la rama de baja del binomio a un spool de super duplex.

### El riesgo corre en las dos direcciones

| Direccion | Consecuencia |
|---|---|
| Aplicar la rama de baja, 7,5 barG | El ensayo no califica y se repite. **Ya ocurrio** |
| Aplicar 135 barG a toda linea de super duplex | Sobrepresion en **siete de las once**: la descarga de la bomba de alta a **2,25 veces** su diseño, y las dos salidas de turbocharger a **2,7 veces** |

Es el mismo modo de falla del hallazgo critico del TM N27 —75 barG ordenados sobre una linea de PVC de 5 barG— ahora dentro del circuito de super duplex, aguas arriba y abajo de los dos Fedco HPB-60 `SIP-09-001` y `SIP-09-002`. Dato que suma como indicio, no como afirmacion: la tabla de acoplamientos Style S del datasheet del feed turbocharger declara presion de trabajo de **103 bar en DN65**, que es el diametro de las dos lineas de salida.

### Las once lineas de super duplex

| TAG | Descripcion | Oper. | Diseño | Prueba | Estado |
|---|---|---|---|---|---|
| `DA-SSD-DN100-09-003` | RO HP Feed Pump Discharge | 51 | 60 | **90** | Ensayada 20-Ago, conforme |
| `DA-SSD-DN100-09-004` | 1st Stage RO Feed | 70 | 80 | **120** | Pendiente |
| `DA-SSD-DN80-09-005` | 1st Stage RO Reject | 68 | 80 | **120** | Pendiente |
| `DA-SSD-DN80-09-006` | 2nd Stage RO Feed | 85 | 90 | **135** | Pendiente |
| `DA-SSD-DN65-09-007` | 2nd Stage RO Reject | 83 | 90 | **135** | Pendiente |
| `DA-SSD-DN65-09-008` | Interstage Turbocharger Brine Outlet | 46 | 50 | **75** | Pendiente |
| `DA-SSD-DN65-09-009` | Feed Turbocharger Brine Outlet | 1 | 50 | **75** | Pendiente |
| `CP-SSD-DN100-09-014` | CIP Feed to 1st Stage RO | 70 | 80 | **120** | Correlativo del Spool 1, por aclarar |
| `CP-SSD-DN80-09-015` | CIP Feed to 2nd Stage RO | 85 | 90 | **135** | Pendiente |
| `CP-SSD-DN80-09-044` | 1st Stage CIP Reject Out | 68 | 80 | **120** | Pendiente |
| `CP-SSD-DN65-09-045` | 2nd Stage CIP Reject Out | 83 | 90 | **135** | Pendiente |

Solo **cuatro** lineas se ensayan a 135 barG. Las veintitres plasticas van a 3 o 7,5 barG.

**Donde se emite cada cosa:** la regla, la tabla y la retencion de ensayos van en el **Transmittal N35**, subseccion del procedimiento de presion y Seccion 3, porque son disposicion documental; el incidente del Spool 1 y la peticion operativa van en el **correo de la cadena de inspecciones**. La tabla es identica en los dos y se compara automaticamente antes de emitir.

---

## Estado del Punto de Detencion

La fila 5.2 del ITP `P22-BA-09-000-004` Rev 0 es Punto de Detencion (H) y su certificado es el *Pressure Test report (Graphic P vs T)*. El ensayo se cumple linea por linea, contra la presion que la Line List asigna a cada una. Con la jornada del 20-Ago queda ensayada **una sola linea de alta**, la `DA-SSD-DN100-09-003`, a 90 barG. Las otras diez lineas de super duplex siguen pendientes, incluida la que el Spool 1 pretende cubrir.

---

## Lo que se pide

1. **Identificar el Spool 1 por su TAG de la Line List aprobada** y declarar la presion de hidrostatica que esa linea tiene asignada.
2. Si el spool pertenece al circuito de super duplex, **repetir el ensayo a la presion de la Line List**, con aviso escrito previo y con el inspector presente, por ser Punto de Detencion.
3. **Corregir el registro** del 20-Ago para que el TAG coincida con la Line List, y corregir tambien el item 5 del checklist si la presion requerida no era 7,5 barG.
4. **Declarar el plan de las lineas de super duplex que faltan**, con fechas, para poder programar la asistencia del inspector.
5. **Incorporar el `PRESSURE TEST RECORD CHART` al procedimiento** `P22-BA-09-000-010` como formulario controlado, con numero y revision, ya que es el que produce el certificado que exige la fila 5.2 del ITP.

---

## Que no se levanta

- El **formato manuscrito** del grafico. La ET no exige registrador electronico y el chart trae los escalones, las horas y las firmas. Objetar la forma sin requisito que lo sostenga es refutable.
- La **ausencia de Report No.** en los dos formularios `AQ-QAM-F018` y en el Inspection Request. Es aseo documental y se resuelve al armar el dossier; se menciona en la peticion de correccion del registro, no como observacion propia.
- El **Test Pack No. y el System/Package No. en N/A** del Inspection Request. Mismo criterio.
- La **duracion de la retencion**, treinta minutos en los dos ensayos, que supera los diez minutos que pide el procedimiento.
