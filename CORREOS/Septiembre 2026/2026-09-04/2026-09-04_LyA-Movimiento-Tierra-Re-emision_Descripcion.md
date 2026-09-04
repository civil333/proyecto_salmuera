---
titulo: Pedido a L&A de re-emision del plano de Movimiento de Tierra tras el cambio de nivel
fecha: 2026-09-04
estado: BORRADOR
destinatario: L&A Ingenieria y Proyectos (Pablo Castillo)
type: correo
project: salmuera-taltal
---

# Movimiento de tierra pendiente tras el cambio de nivel — pedido a L&A

**Estado: BORRADOR.** Sin datos faltantes. Va como **Reply-To al hilo de la carta
`067-032-032-COR-TT-013`**, no como correo nuevo ni como transmittal: el stream OOCC no emite
transmittal desde el TM N4 y las entregas 8 a 12 se cerraron por correo.

## Que se pide

**Dos laminas del mismo codigo**, ambas en revision 0 del 22-06-2026:

| Documento | Titulo |
|---|---|
| `P22-DWG-00-001-001` LAM1 | Plano Movimiento de Tierra, Planta |
| `P22-DWG-00-001-001` LAM2 | Plano Movimiento de Tierra, Secciones y Detalle |

Mas una **consulta** sobre el cuadro de excavacion de `P22-DWG-00-002-003` LAM1 **revision 1**, que
L&A acaba de emitir.

## Por que, verificado plano por plano

El cambio: en `P22-DWG-00-002-003` LAM1 Rev 1 el sello de fundacion del contenedor pasa de **+5,150 a
+5,400** y la cara superior de **+6,050 a +6,300**. El **N.T.N. se mantiene en +6,000**, de modo que lo
que cambia es la profundidad de excavacion, que baja 250 mm.

| Donde | Que dice hoy | Por que queda superado |
|---|---|---|
| `00-001-001` LAM1, cuadro de cubicaciones, item 8 | Excavacion contenedor 38,02 m3, area 53,51 m2 | El sello sube 250 mm sobre esa area |
| `00-001-001` LAM1, cuadro de cubicaciones, item 7 | Excavacion TK CIP y equipos 5,01 m3 | La Rev 1 del `00-002-007` LAM1 la baja a 1,60 m3 |
| `00-001-001` LAM2, Secciones E y F | Fondo de excavacion del contenedor en EL. 5,15 | El sello vigente es +5,400 |
| `00-002-003` LAM1 **Rev 1** | Excavacion 38,02 / retiro 45,62 / relleno 30,03, iguales a la Rev 0 | El sello subio 250 mm en esa misma lamina |

El orden de magnitud que el correo menciona, unos 13 m3 menos de excavacion, sale de 53,51 m2 por
0,25 m. Se declara como estimacion de ADASA y se deja el calculo a L&A, porque la excavacion tiene
taludes y el volumen exacto no es el producto directo.

## Correccion de un pedido propio

El 04-09 se habia anotado que faltaban **tres** laminas, incluyendo `P22-DWG-00-002-001`
(Implantacion General). **Al verificarla no corresponde pedirla**: solo acota el nivel de terreno
natural por zona (+6,000 y +5,750), las coordenadas UTM y las notas generales, y el N.T.N. no se movio.
El correo lo dice explicitamente para que L&A no la re-emita sin necesidad. Son dos laminas, no tres.

## Punto de forma incluido

Las cinco laminas de la Rev 1 declaran "MODIFICACIONES INDICADAS" en la fila de su revision, que
describe el cambio y no el estado de emision; la fila de la Rev 0 conserva "APTO PARA CONSTRUCCION".
Se pide que el cajetin declare el estado en la fila vigente. Va como observacion de forma al final, sin
condicionar la aceptacion de las laminas.

## Contexto Interno (No enviar)

- El paquete que se licito llevaba, ademas de las 18 laminas Rev 0, **30 laminas en revisiones B, C y
  D** que nunca se retiraron. El usuario las esta eliminando de la carpeta original. Eso no se le
  reprocha a L&A en este correo: el armado del paquete es de ADASA.
- La Rev 1 tampoco actualizo `00-002-004` (fosa) ni `00-002-006` (drenajes). No se piden porque su cota
  no depende del sello del contenedor; si al recalcular el movimiento de tierra apareciera un efecto,
  se agrega.
- Barrido de idioma del stream OOCC: cero anglicismos de jerga ejecutiva, cero signo de seccion, cero
  oraciones sobre 50 palabras.

## Checklist previo al envio

- [ ] Enviar como respuesta al hilo de la carta `067-032-032-COR-TT-013`, no como correo nuevo
- [ ] Verificar la lista de copia contra el hilo, por si cambio desde junio
- [ ] Confirmar que no se adjunta nada: el correo se sostiene solo

## Checklist posterior al envio

- [ ] Cambiar el estado de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Abrir el compromiso de seguimiento con la fecha que L&A responda
- [ ] Registrar en la Bitacora del README
