---
titulo: Registro consolidado de las inspecciones de taller de Bureau Veritas
codigo: Informes BVM-IR001 a BVM-IR009
fecha: 2026-08-31
estado: INTERNO
type: registro
project: salmuera-taltal
---

# Inspecciones de taller de Bureau Veritas — registro consolidado al 31-Ago-2026

Bureau Veritas Chile remitio el **lunes 31-Ago-2026 a las 14:47** el set completo de los nueve informes
emitidos hasta la fecha, con el `IR005` y el `IR006` en revision 01. Responde a la peticion de Luis Rivera
del viernes 28-Ago 14:42 por la cadena `RE: 25007 TALTAL - Request to witness inspection 006`.

Todo lo de abajo esta leido de los informes. Las casillas marcadas se verificaron **por render**, no por
texto extraido: el formulario `GM-SI-101 INSP002-En` Rev 3.1 dibuja sus casillas como vectores y el texto
plano no revela cual esta marcada.

---

## 1. Las nueve jornadas

| # | Informe | Fecha | Dia | Alcance declarado en la portada | Lo que realmente se ejecuto | Casilla de resultado marcada |
|---|---|---|---|---|---|---|
| 1 | `BVM-IR001-28072026` | 28-Jul | martes | PMI de material super duplex | Inspeccion visual y dimensional del material, mas PMI sobre el 10 % minimo del ITP | Satisfactory |
| 2 | `BVM-IR002-07082026` | 07-Ago | viernes | Fabricacion de spools, liquidos penetrantes, marco del skid, WPS y calificacion de soldadores | Lo declarado | Satisfactory |
| 3 | `BVM-IR003-13082026` | 13-Ago | jueves | Preparacion de pintura | Preparacion de pintura en el taller del proveedor de pintura, mas visual del marco y del contenedor | Satisfactory (Without comments) |
| 4 | `BVM-IR004-14082026` | 14-Ago | viernes | **Ensayo de presion de alta** | **El ensayo de alta no se ejecuto.** Su seccion E1 dice literal que el ensayo de alta no pudo realizarse por un problema de bridas ciegas. Se sustituyo por examen visual y dimensional de spools | Satisfactory (Without comments) |
| 5 | `BVM-IR005-20082026` Rev 01 | 20-Ago | jueves | Ensayo de presion de alta, dos spools | `DA-SSD-DN100-09-003` conforme a 90 barG; `CP-SSD-DN100-09-014` ensayada a 7,5 barG contra 120 exigidos | **Not Satisfactory** |
| 6 | `BVM-IR006-21082026` Rev 01 | 21-Ago | viernes | Ensayo de presion de alta, dos spools | `CP-SSD-DN80-09-015` y `CP-SSD-DN80-09-044` ensayadas a 7,5 barG contra 135 y 120 exigidos | **Not Satisfactory** |
| 7 | `BVM-IR007-24082026` | 24-Ago | lunes | Inspeccion de pintura del marco del skid | Verificacion de perfil tras granallado y espesor de pelicula seca. **La parte inferior del marco no alcanza los 355 micrones exigidos** | Satisfactory (Without comments) |
| 8 | `BVM-IR008-27082026` | 27-Ago | jueves | Ensayo de presion de **baja** | `DA-PVC-DN100-09-002`, diseno 5 barG, exigido 7,5, aplicado 7,6, retencion 30 min | Satisfactory (Without comments) |
| 9 | `BVM-IR009-28082026` | 28-Ago | viernes | Ensayo de presion de **baja** | `DA-PVC-DN100-09-001`, diseno 5 barG, exigido 7,5, aplicado 7,5, retencion 30 min | Satisfactory (Without comments) |

**Nueve jornadas consumidas** de las dieciocho de vigilancia que contrata la oferta `600049` Rev.3
(dieciocho de vigilancia mas siete de FAT, veinticinco en total). **Dato interno**, no se comunica: el
inspector figura entre los destinatarios de la cadena tecnica.

---

## 2. Los ensayos de presion, linea por linea

Presion exigida = **1,5 x presion de diseno**, columna de hidrostatica de la Line List `P22-LI-09-009-003`
Rev 0, aprobada en Codigo 1 en el Transmittal N29.

| Linea | Jornada | Informe | Diseno barG | Exigida barG | Aplicada barG | Estado |
|---|---|---|---|---|---|---|
| `DA-SSD-DN100-09-003` | 20-Ago | `IR005` Rev 01 | 60 | **90** | 90 | **Conforme** |
| `CP-SSD-DN100-09-014` | 20-Ago | `IR005` Rev 01 | 80 | **120** | 7,5 | No califica, se repite |
| `CP-SSD-DN80-09-015` | 21-Ago | `IR006` Rev 01 | 90 | **135** | 7,5 | No califica, se repite |
| `CP-SSD-DN80-09-044` | 21-Ago | `IR006` Rev 01 | 80 | **120** | 7,5 | No califica, se repite |
| `DA-PVC-DN100-09-002` | 27-Ago | `IR008` | 5 | 7,5 | 7,6 | Conforme |
| `DA-PVC-DN100-09-001` | 28-Ago | `IR009` | 5 | 7,5 | 7,5 | Conforme |

### Estado del Punto de Detencion de la fila 5.2 del ITP

De las **once lineas de super duplex** del proyecto: **una conforme**, **tres a repetir**, **siete sin
ensayar**. Las siete pendientes son `DA-SSD-DN100-09-004` (120), `DA-SSD-DN80-09-005` (120),
`DA-SSD-DN80-09-006` (135), `DA-SSD-DN65-09-007` (135), `DA-SSD-DN65-09-008` (75),
`DA-SSD-DN65-09-009` (75) y `CP-SSD-DN65-09-045` (135), esta ultima bajo retencion escrita desde el
20-Ago y cuarta linea del circuito CIP.

**Desde el 20 de agosto no se ha ejecutado ningun ensayo de super duplex.** Las dos jornadas de la semana
del 24 al 28 se destinaron a ensayos de baja presion sobre cañeria de PVC.

### La jornada del viernes 28 de agosto

El `AQ-QAM-F027 Inspection Request Form` de ese dia declara **Inspection Item: 1- HP and LP pressure
test**, ventana de 09:00 a 17:00 en Penang, y se cerro como **Accepted** con la sola nota manuscrita de
que el ensayo de baja presion del spool de PVC se realizo y resulto satisfactorio, linea
`DA-PVC-DN100-09-001`. La solicitud cubria alta y baja; se ejecuto solo la baja y el formulario se
acepto igual. Es el mismo defecto de forma que ADASA pidio corregir el 12 de agosto: un solo bloque de
resultado que cubre un alcance cumplido a medias.

El registro del fabricante de ese dia es el `AQ-QAM-F018` Rev 4, que es el formulario controlado que el
Transmittal N35 dio por incorporado: `PI-0800-0001 - Spool 1`, 7,5 bar de 10:15 a 10:45, caida cero,
manometros `FAC-MT-068` y `FAC-MT-070`, firmado por el fabricante y timbrado por Bureau Veritas. **Su
casilla `Report No.` esta vacia.**

---

## 3. Que cambio en la reemision del `IR005` y del `IR006`

Las seis peticiones de ADASA del 21-Ago, contrastadas contra los documentos recibidos:

| Peticion del 21-Ago | Estado | Evidencia |
|---|---|---|
| Reemitir los dos informes con la presion de diseno de la Line List | **Cumplida** | La tabla de la seccion E1 declara ahora 80/120, 90/135 y 80/120 contra los 7,5 barG aplicados, y marca las tres lineas como no satisfactorias |
| Contrastar cada ensayo contra el P&ID y la Line List antes de firmar | **Cumplida** | El P&ID `P22-DWG-09-009-002` Rev D y la Line List `P22-LI-09-009-003` Rev 0 entran a la seccion B de los dos reemitidos y de los dos informes de presion posteriores |
| Fotografiar la marca de identificacion del carrete | **Cumplida desde el `IR008`** | Los informes del 27 y del 28 traen una fotografia rotulada como vista de la identificacion del carrete, con la marca manuscrita visible. Las reemisiones no la incorporan de forma retroactiva |
| **Levantar una No Conformidad que cubra los tres ensayos** | **Abierta** | Ver abajo |
| Incorporar el P&ID y la Line List a todo informe de presion | **Cumplida** | `IR005` Rev 01, `IR006` Rev 01, `IR008` e `IR009` |
| Instruir que la fila 5.2 es Punto de Detencion y que la retencion sigue vigente | **Sin constancia** | Ninguno de los informes posteriores lo menciona |

🔴 **La No Conformidad sigue sin levantarse, y la reemision quedo internamente contradictoria.** Los dos
informes reemitidos marcan la casilla **Not Satisfactory (NCR raised during the inspection)** y, tres
lineas mas abajo, marcan **Open Non Conformities: No**, con la seccion G en `N/A`. La casilla marcada
declara que se levanto una No Conformidad durante la inspeccion; el resto del formulario declara que no
existe ninguna. Sin ella, el dossier no llevara el registro de la desviacion.

**Lo que si cambio en el resultado, y es sustantivo:** el `IR005` pasa de `Satisfactory (Without
comments)` a `Not Satisfactory`, y el `IR006` de `Satisfactory with comments (Pending)` a `Not
Satisfactory`. La objecion de fondo del 21 de agosto quedo acogida.

---

## 4. Defectos de control documental del set

- 🔴 **`Revision No. 0` en los once documentos, reemisiones incluidas.** El `IR005` y el `IR006`
  reemitidos siguen declarando revision 0 en su campo de revision: la revision 01 solo existe en el
  nombre del archivo. El dossier no podra distinguir cual version gobierna.
- 🔴 **El numero de informe del `IR005` aparece en el encabezado interior de otros tres documentos.** El
  `IR006` Rev 01, el `IR007` y el `IR008` llevan `BVM-IR005-20082026` en paginas interiores. En el
  `IR007` son **las cinco** paginas interiores: solo la portada lleva su propio numero.
- **`IR007`: la casilla marcada contradice su propio resumen.** Marca `Satisfactory (Without comments)`
  mientras su resumen declara el resultado no satisfactorio y su seccion E1 registra que la parte
  inferior del marco no alcanza los 355 micrones. Ademas deja No Conformidades y punch list en `No`. Es
  el mismo defecto que ADASA objeto el 21 de agosto sobre el `IR005`, repetido tres dias despues.
- **El anexo del `IR008` es byte a byte el mismo archivo que el del `IR009`.** Su nombre declara
  `PSPP-26605366` y el certificado que contiene es el `PSPP-26605336`, manometro `FAC-MT-068` WIKA
  232.50.100 de 0 a 16 bar. Los dos informes declaran en su seccion D los manometros `PSPP-26605336` y
  `PSPP-26605337`, de modo que el numero del **nombre del archivo** es el erroneo y el certificado del
  `-337` no viene adjunto en ninguna de las dos jornadas. Es traza documental, no defecto de ensayo.
- **El `IR004` se rotula en portada como ensayo de presion de alta** y marca `Satisfactory (Without
  comments)` sobre una jornada en la que ese ensayo no se ejecuto. El resumen si describe lo que se hizo;
  el rotulo de alcance, no.
- **El `IR004` acepto ajuste, examen visual y dimensional contra los planos de taller
  `25007-ME-PI-0901-0007`, `-0009` y `-0010`**, que pertenecen al conjunto de diecisiete laminas nunca
  sometidas a revision y estampadas FOR CONSTRUCTION que levanto el Transmittal N30. Sigue abierto en
  `PRG-21`.

## 5. Lo favorable, que tambien consta

El inspector asistio a las nueve jornadas, firmo y timbro los registros del fabricante, reviso los
certificados de calibracion, y fotografio los escalones de presion con hora. La instrumentacion es WIKA
calibrada por Trescal Malasia el 14-Jun-2026 con recalibracion al 14-Jun-2027, laboratorio acreditado
SAMM y trazabilidad a NMIM y KRISS. Los ensayos de baja presion del 27 y del 28 estan bien ejecutados y
bien registrados, y **cierran la parte de baja presion del alcance que el Inspection Request 003 habia
recortado el 5 de agosto**.

## 6. Discrepancias del resumen que acompaña al set

El correo de remision del 31-Ago trae un cuadro de las nueve visitas. Dos filas no coinciden con los
informes que el mismo correo adjunta:

| Fila | Dice el resumen | Dice el informe |
|---|---|---|
| Visita 4, 14-Ago | Ensayo de presion de alta atestiguado, resultado Satisfactorio | El ensayo de alta no se ejecuto; se sustituyo por examen visual y dimensional |
| Visita 7, 24-Ago | Resultado **Satisfactorio**, con la observacion describiendo un resultado no satisfactorio | La casilla marcada es `Satisfactory (Without comments)` y el resumen del informe declara el resultado no satisfactorio |

La fila 7 arrastra la contradiccion del propio formulario; la fila 4 es del resumen.

---

## 7. Como quedo ordenada la carpeta

Una carpeta por informe, `IR001` a `IR009`, cada una con el informe, su anexo y una subcarpeta `md/`.
El `IR005` y el `IR006` conservan **las dos revisiones**, porque la comparacion entre ellas es la
evidencia del cierre parcial. El `IR005` incorpora ademas el registro del fabricante del 20-Ago y el
`IR009` el del 28-Ago. Los renders de verificacion estan en `_render/`.

`BV Malasia (ADASA)/` se conserva intacta: es el paquete tal como lo remitio Bureau Veritas Chile.
Las carpetas `INSPECTION 01` a `06`, `general/` e `inspeccion 009` se mantienen como estan, porque
crecieron por hilo de correo y el mapa del frente (`REQUEST WITNESS INSPECTION/_ORIGEN.md`) las
referencia; sus copias son payload identico al recibido, verificado por hash md5.
