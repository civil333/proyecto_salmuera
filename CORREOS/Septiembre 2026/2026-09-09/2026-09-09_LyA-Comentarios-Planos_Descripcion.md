---
titulo: Discrepancias entre planos a L&A, Movimiento de Tierra revision 1
fecha: 2026-09-09
estado: ENVIADO
destinatario: L&A Ingenieria y Proyectos (Pablo Castillo)
type: correo
project: salmuera-taltal
---

# Discrepancias entre planos, Movimiento de Tierra revision 1

**Estado: ENVIADO** el 09-09-2026. Fue como **respuesta al hilo de la carta
`067-032-032-COR-TT-015`**, con **cuatro PDF comentados adjuntos**. Reemision pedida al **viernes 11
de septiembre**.

## El criterio

Solo se comentan **discrepancias entre planos vigentes**: una misma excavacion o una misma cota
declarada con dos valores distintos en dos planos. La instruccion a L&A es siempre la misma, dejar
una sola cifra.

**El correo no repite los comentarios.** Para eso van los adjuntos: el cuerpo lleva una tabla de
cuatro filas, una por plano comentado, con el rango de identificadores y la materia en una linea. El
detalle de cada discrepancia vive en los recuadros. Son 340 palabras.

**Quedaron fuera**, por decision del usuario: los puntos de control documental, porque el cajetin ya
identifica la revision 1 y las nubes de revision estan puestas; las dos secciones de excavacion
ausentes en la lamina 2, que son omision de dibujo y no discrepancia; y el pedido del archivo nativo,
que se hara al acusar la reemision.

## Numeracion: serie unica del envio

**OBS-01 a OBS-07, corrida por el orden en que se leen los planos.** Cada identificador es unico en el
envio, de modo que la peticion se resume en una linea y las dos discrepancias que aparecen en dos
planos se citan entre si.

Los identificadores son de **este paquete de comentarios**, del 09-09-2026, no del historial de cada
plano. Los OBS-01 a OBS-03 que el `P22-DWG-00-001-001` uso en sus revisiones B y C son otra cosa y
quedaron cerrados al aceptarse la revision 0; la trazabilidad de este ciclo se hace por la fecha y la
carta.

## Que se envia

Cuatro `_CC_ADASA.pdf` generados con `doc-annotator` por
`INGENIERIA DE DETALLE OOCC/REVISIONES/TRANSMITTALES/P22-TM-00-010-005-0/COMENTARIOS/generar_cc_adasa_entrega14.py`.

| Adjunto | Observaciones | Materia |
|---|---|---|
| `P22-DWG-00-001-001-1-LAM 1_CC_ADASA.pdf` | OBS-01 a OBS-03 | Zona CIP, contenedor, y dos excavaciones que el cuadro no recoge |
| `P22-DWG-00-001-001-1-LAM 2_CC_ADASA.pdf` | OBS-04 y OBS-05 | Fondo de excavacion del estanque y de la fosa |
| `P22-DWG-00-002-003_1 LAM1_CC_ADASA.pdf` | OBS-06 | El otro lado de la discrepancia del contenedor |
| `P22-DWG-00-002-007_1 LAM1_CC_ADASA.pdf` | OBS-07 | El otro lado de la discrepancia de la zona CIP |

Siete observaciones sobre cuatro laminas, todas en naranja: no hay notas menores en este ciclo. La
**Implantacion General `P22-DWG-00-002-001` revision 1 se acepta sin comentarios** y se declara asi en
la apertura.

## Las cinco discrepancias

| ID | Un plano dice | El otro dice |
|---|---|---|
| OBS-01 y OBS-07 | `00-001-001` LAM1 item 7: 1,03 m3 | `00-002-007` LAM1: 1,60 m3 |
| OBS-02 y OBS-06 | `00-001-001` LAM1 item 8: 20,95 m3 | `00-002-003` LAM1: 38,02 m3 |
| OBS-03 | El cuadro no las recoge | `00-002-002` LAM4: 0,62 m3 y `00-002-007` LAM3: 4,25 m3 |
| OBS-04 | `00-001-001` LAM2 secciones A y B: EL. 5,35 | `00-002-002` LAM1: sello +5,350 con emplantillado de 5 cm, fondo 5,30 |
| OBS-05 | `00-001-001` LAM2 seccion B: EL. 4,30 | `00-002-004` LAM1: sello +4,305 con mejoramiento de 15 cm, fondo 4,155 |

Las dos primeras aparecen dos veces, una por cada lado, y sus recuadros se citan entre si con un
"Ver OBS-xx". La OBS-03 es una omision con la misma consecuencia practica: son 4,87 m3 que hoy faltan
en el respaldo de la partida 4.6.

## Verificacion de las fuentes

Todo lo que el correo afirma se leyo por render de los planos, que son vectorizados y no entregan sus
cuadros por extraccion de texto.

| Dato | Fuente |
|---|---|
| Item 7 en 1,03 m3 e item 8 en 20,95 m3 | Render del cuadro Cubicaciones Movimiento Tierra de la LAM1 |
| 1,60 m3 de la zona CIP y 38,02 del contenedor | Render de los cuadros de excavacion de `00-002-007 LAM1` y `00-002-003 LAM1` |
| 0,62 m3 de la bomba y 4,25 m3 de la cubierta CIP | Render de los cuadros de `00-002-002 LAM4` y `00-002-007 LAM3` |
| Fondos EL. 5,35 y EL. 4,30 | Render de las secciones A, B y F de la LAM2 |
| Sellos +5,350 y +4,305, emplantillado de 5 cm y mejoramiento M.H.A. de 15 cm | Extraccion posicional con la marca N.S.F. adyacente a la cota, y render de la elevacion de eje de `00-002-004 LAM1` |

Cierre de la anotacion: los siete identificadores presentes una sola vez cada uno, las cuatro
referencias cruzadas apareadas, y render PNG de los recuadros comprobando que el identificador y la
linea `Corregir:` salen completos y que el texto lee de izquierda a derecha. En paginas rotadas la
skill dibuja en el flujo de contenido y `page.annots()` devuelve cero, de modo que contar anotaciones
no sirve como verificacion.

## Contexto Interno (No enviar)

- El analisis completo, con la reconstruccion de la cantidad de la partida 4.6 y los puntos
  descartados, vive en
  `INGENIERIA DE DETALLE OOCC/REVISIONES/TRANSMITTALES/P22-TM-00-010-005-0/_ANALISIS_TRABAJO.md`.
- **El efecto economico no se menciona.** La partida 4.6 pasa de 115,10 a 90,58 m3 y eso se declara al
  contratista en la Nota Tecnica, no al proyectista.
- Las cuatro laminas **ya estan incorporadas** al paquete de ingenieria vigente, y sus `LEEME.txt`
  estan escritos en positivo: no narran el defecto ni mencionan observaciones abiertas.
- Barrido del stream OOCC: cero anglicismos, cero signo de seccion, cero oraciones sobre 50 palabras.

## Checklist previo al envio

- [x] Enviar como respuesta al hilo de la carta `067-032-032-COR-TT-015`
- [x] Adjuntar los cuatro `_CC_ADASA.pdf` de la carpeta COMENTARIOS del `P22-TM-00-010-005-0`
- [x] Verificar la lista de copia contra el hilo, por si cambio desde junio

## Checklist posterior al envio

- [x] Cambiar el estado de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Abrir el compromiso de seguimiento con vencimiento el viernes 11 de septiembre
- [ ] Pedir el archivo nativo al acusar la reemision
- [ ] Registrar en la Bitacora del README
