---
titulo: Inspeccion 05 del 20-Ago-2026 — analisis ADASA del informe BVM-IR005
codigo: Informe BVM-IR005-20082026 / Annex 1
fecha: 2026-08-21
estado: INTERNO
type: analisis
project: salmuera-taltal
---

# Inspeccion 05 del 20-Ago-2026 — el informe que resolvio el TAG y declaro conforme el ensayo

> **Este informe llego el 20-Ago y ADASA no lo tuvo a la vista al escribir el correo de esa
> tarde.** Vino por la cadena `RE: 25007 TALTAL - Request to witness inspection 004`, distinta de las
> dos que se estaban revisando. De ahi salio una afirmacion equivocada en un borrador posterior —que
> el informe del 20-Ago no habia llegado— que se corrigio antes de emitir. Ver la seccion final.

**Documentos revisados:** `IR005-ADASA-BVM-20082026.pdf` (ocho paginas, con texto extraible),
`Annex 1.pdf` (ocho paginas escaneadas, leidas por render) y el correo de remision de Emylia Rosli.

**Recepcion:** correo de **Emylia Rosli**, Bureau Veritas Malasia, del **20-Ago 23:35 hora de Chile**
(21-Ago 11:35 en Penang), dirigido a Mohd Adnin con Bureau Veritas, BW Water y **Luis Rivera en
copia**. Informe fechado **20 de agosto**. **Cumple el plazo de la seccion 3 de la oferta 600049
Rev.3**, que pide el informe al dia siguiente de concluida la visita.

**Que es:** informe de tercero inspector, formato `GM-SI-101 INSP002-En` Rev 3.1. Inspector Mohamad
Fakhrul Radzi Bin Zainal, coordinador Ahmad Hazwan, aprobado por Wan Mohd Adli W Yahya. Trabajo
BVM 26/1366, Orden de Compra 836492. `Previous Inspection: 14th August 2026`, coherente con el
`IR004-ADASA-BVM-14082026` que ya obra en el proyecto: la cadena de informes no tiene hueco.

---

## Lo que se ejecuto

Seccion E1 punto 3:

| Nº | Identificacion en el informe | Diseno declarado | Ensayo | Duracion |
|---|---|---|---|---|
| 1 | `DA-SSD-DN100-09-003` (Jt 06 y 07) | 60,0 bar | **90,0 bar** | 30 min |
| 2 | **`CP-SSD-DN100-09-014`** (Jt 01 y 02) | **5,0 bar** | **7,5 bar** | 30 min |

Escalones fotografiados: 45 → 67,5 → 90 → 63 → 60 para el primero, con marca de tiempo 10:36; y
3,75 → 5,6 → 7,5 → 5,25 → 5,0 para el segundo, con marca 15:18. Titulo de la jornada:
*"Witnessed **High Pressure** piping pressure test"*.

---

## 🔴 El hallazgo principal: el informe resuelve el TAG y aun asi no cruza la presion

**El formulario del fabricante registro el Spool 1 como `DA-SSD-DN100-09-014`**, numero que **no
existe** en la Line List: la serie `DA-SSD-DN100` solo tiene la `-003` y la `-004`. **El BVM-IR005 lo
escribe como `CP-SSD-DN100-09-014`**, que si existe. El inspector corrigio el prefijo y **tuvo el
numero correcto delante**.

Con ese numero, la Line List `P22-LI-09-009-003` Rev 0 asigna:

| Linea | Material | Servicio | Diseno barG | Hidrostatica barG |
|---|---|---|---|---|
| `CP-SSD-DN100-09-014` | SUPER DUPLEX STEEL SCH80S, DN100 | CIP FEED TO 1ST STAGE RO | **80** | **120** |

El informe consigno **5,0 y 7,5**. Bastaba una fila de la tabla que ADASA le habia entregado un mes
antes. Ese es el nucleo del reclamo al tercero inspector: no es un TAG mal transcrito, es la ausencia
del contraste contra el documento que gobierna el parametro.

**Consecuencia para el frente con el proveedor:** la primera peticion del correo del 20-Ago,
identificar el Spool 1 por su TAG de la Line List, **queda respondida por el propio informe de
tercero**. El correo del 21-Ago la retira y la reemplaza por la repeticion del ensayo a 120 barG.

---

## Que marco Bureau Veritas

Verificado por render a 400 dpi de la pagina 1, no por lectura del texto plano.

| Campo | Marca |
|---|---|
| Resultado de la inspeccion | 🔴 **Satisfactory (Without comments)** |
| Open Non Conformities | **No** |
| Open Punch List Items | **No** |
| Release Note Issued | No |
| BV Traceability Stamping | No |

Resumen de **una sola linea**: *"Witnessed High Pressure Piping Pressure Test of SDSS Piping spool
and found satisfactory at time of inspection."* **No hay salvedad de ningun tipo.** La nota sobre la
line list aparece **solo en el BVM-IR006**, del dia siguiente, que ademas marca *Satisfactory with
comments*.

🔴 **Ni la Line List ni el P&ID figuran en la seccion B**, la de documentacion de referencia. Esa
seccion lista el formulario `AQ-QAM-F027`, el ITP `P22-BA-09-000-004` Rev 0, un `P22-BA-09-000-001`
Rev 0 rotulado como Technical Specification, y el procedimiento `P22-BA-09-000-010` Rev 0. Mismo
hueco que en el IR006.

---

## Los manometros: no es falta de instrumentacion

Seccion D del informe, cuatro equipos, contra los certificados Trescal del `Annex 1` leidos por
render:

| Certificado | Equipo | Modelo | Rango |
|---|---|---|---|
| `PSPP-26605330` | `FAC-MT-012` | WIKA 232.50.100 | **0 a 160 bar** |
| `PSPP-26605335` | `FAC-MT-013` | WIKA 232.50.100 | **0 a 160 bar** |
| `PSPP-26605337` | `FAC-MT-070` | WIKA 232.50.100 | 0 a 16 bar |
| `PSPP-26605340` | `FAC-MT-015` | WIKA EN 837-1 | 0 a 16 bar |

**Los dos de alta estaban en la mesa y se usaron esa misma manana** para el ensayo a 90 barG. El
punto 6 de la seccion E1 declara que el inspector reviso los certificados. Y el 21-Ago solo se
llevaron los dos de 16 bar, de modo que esa jornada se planifico de entrada como ensayo de baja
presion.

**Corrige un planteo previo:** la peticion de "confirmar que el taller dispone de manometros de rango
adecuado" estaba mal formulada. Los tiene. La pregunta correcta es por que se aplico el criterio de
baja presion.

---

## El registro fotografico no identifica lo ensayado

Verificado por render de las paginas 5 a 8. **Ninguna imagen muestra una marca, un numero de spool ni
un rotulo.** La *"General view of High Pressure Piping Pressure Test for piping spool Item No:
CP-SSD-DN100-09-014 (Jt01 & 02)"* es un carrete embridado sobre el piso, sin identificacion visible;
las demas son primeros planos de la caratula del manometro y de los adhesivos de calibracion.

En el `BVM-IR006` el defecto es mas visible todavia: **una sola fotografia rotulada al pie con dos
numeros de linea distintos**, `CP-SSD-DN80-09-015` y `CP-SSD-DN80-09-044`.

Las marcas de tiempo impresas si son coherentes con los horarios declarados. Lo que falta es la
identidad del objeto, que es justo lo que ADASA no puede verificar por su cuenta a 17.000 km.

---

## El patron: el circuito CIP se esta ensayando como sistema de baja presion

Las cuatro lineas CIP de super duplex de la Line List Rev 0:

| Linea | DN | Servicio | Diseno | Hidrostatica | Estado |
|---|---|---|---|---|---|
| `CP-SSD-DN100-09-014` | DN100 | CIP Feed to 1st Stage RO | 80 | **120** | ensayada a 7,5 el 20-Ago |
| `CP-SSD-DN80-09-015` | DN80 | CIP Feed to 2nd Stage RO | 90 | **135** | ensayada a 7,5 el 21-Ago |
| `CP-SSD-DN80-09-044` | DN80 | 1st Stage CIP Reject Out | 80 | **120** | ensayada a 7,5 el 21-Ago |
| `CP-SSD-DN65-09-045` | DN65 | 2nd Stage CIP Reject Out | 90 | **135** | 🔴 **pendiente** |

**Tres de cuatro, en dos jornadas consecutivas, las tres con 5,0 barG de diseno declarado.** Y la
cuarta es precisamente la otra linea que el **Transmittal N30** nombro en el quiebre de
especificacion no declarado, junto con la `-09-044`. El quiebre deja de ser una observacion de plano:
es la causa fisica de tres ensayos que no califican, y el criterio que los produjo sigue vigente.

Encaja con la justificacion del proveedor del 21-Ago: *"This spool that has two flange class, 900#
and 150#"*. Los carretes CIP mezclan PVC clase 150 con super duplex clase 900, y el taller los ensaya
a la presion del PVC.

---

## Lo que se pide, y donde

El detalle de las peticiones vive en los dos correos del 21-Ago
(`CORREOS/Agosto 2026/2026-08-21/`) y en el analisis de la inspeccion 06.

- **Al proveedor:** retencion de `CP-SSD-DN65-09-045`; declarar por escrito que presion de diseno usa
  para el circuito CIP y de que documento la toma; el listado de todo spool ya ensayado; repetir los
  tres; y responder el quiebre de especificacion del N30.
- **Al tercero inspector:** contrastar cada ensayo contra el P&ID y la Line List antes de firmar;
  fotografiar la marca de identificacion del carrete; reemitir el IR005 y el IR006; levantar una No
  Conformidad que cubra los tres.

---

## Que no se levanta

- **El plazo del informe.** Llego el mismo dia de la jornada, dentro de lo que exige la oferta.
- **El desempeno en terreno.** El inspector asistio, firmo, reviso los certificados de calibracion y
  fotografio los escalones. Lo que falla es el contraste documental y la via de aviso.
- **El formato del informe.** Es la plantilla de Bureau Veritas, que la propia oferta autoriza en su
  seccion 3.
- **El codigo `P22-BA-09-000-001`** rotulado como Technical Specification en la seccion B, cuando la
  Especificacion Tecnica del modulo es `P22-ET-09-000-001-0`. Aseo documental.

---

## Nota de procedencia del error corregido

El barrido inicial busco el informe del 20-Ago en `PROGRAMA y CONTRATO/BV INSPECTION/` y en la cadena
del `Request to witness inspection 003/004`, y concluyo que no existia. **El informe estaba en el
correo, en una tercera cadena.** Leccion operativa: **una ausencia no se afirma sin barrer todas las
cadenas de correo del frente**, porque cada actor remite por la suya — el proveedor por la del
Request, Bureau Veritas Chile por la del reporte, y Bureau Veritas Malasia por la del Request
original. Ver `feedback_tercero_inspector_se_mide_por_su_oferta`.
