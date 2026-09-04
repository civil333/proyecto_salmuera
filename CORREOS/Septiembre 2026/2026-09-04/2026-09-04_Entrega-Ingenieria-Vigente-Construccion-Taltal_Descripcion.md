---
titulo: Remision de la NT P22-NT-06-000-001-0 y de la ingenieria vigente al contratista
fecha: 2026-09-04
estado: BORRADOR
destinatario: contratista adjudicado del montaje mecanico y obras civiles
type: correo
project: salmuera-taltal
---

# Remision de la Nota Tecnica y la ingenieria vigente para construccion, PD Taltal

**Estado: BORRADOR.** Falta un dato que solo puede aportar el usuario, marcado en el cuerpo
con `[COMPLETAR]`: el nombre del contratista adjudicado.

## Resumen del cuerpo

Correo de cobertura de 135 palabras, en espanol, en registro de correspondencia (primera
persona). Remite dos cosas: la **Nota Tecnica P22-NT-06-000-001-0** y el paquete
`INGENIERIA VIGENTE PARA CONSTRUCCION`.

No repite la sustancia de la nota. Solo pide revisarla antes de emitir ordenes de compra de
accesorios y bridas y antes de iniciar fundaciones, declara que la propia nota es el punto de
entrada del paquete (remitiendo a la planilla de la carpeta 0 para la revision que rige documento
por documento) y fija el acuse al viernes 11 de septiembre de 2026.

**La sustancia vive en la Nota Tecnica**, no en el correo:
`BASES DE LICITACION MONTAJE MECANICO-OOCC/NOTAS_TECNICAS/P22-NT-06-000-001-0/`.

## Verificacion de fuentes

Las fuentes de cada dato estan verificadas en la Nota Tecnica y en su registro. Lo unico que
el correo afirma por si mismo es la fecha del acuse.

| Dato del correo | Fuente verificada |
|---|---|
| Viernes 11 de septiembre de 2026 | 5 dias habiles desde el viernes 04-09-2026, dia de la semana comprobado |
| Fecha de vigencia 04-09-2026 | Fecha de emision del paquete y de la planilla P22-LI-06-000-002-1 |

## Actualizacion del 04-09-2026 tras la revision de isometrias

El **correo no cambia**: es carta de cobertura y no repite sustancia, de modo que su cuerpo sigue
siendo valido. Lo que crecio es la **Nota Tecnica, de 6 a 7 paginas**, con tres incorporaciones:

1. **Encuadre correcto de la brida.** La NT decia que los flange LJ "se reemplazan" por flange
   suelto. Es la misma pieza (LJ = Lap Joint = flange suelto, perforaciones ASME B16.5 clase 150 en
   ambos documentos); lo que la revision 1 del listado agrega es el material, acero galvanizado por
   inmersion, que las isometrias no declaran. Para el material rige el listado.
2. **Empaquetaduras**, que bajan de 45 a 42 unidades y no estaban declaradas.
3. **Subseccion nueva sobre el cuadernillo de isometrias**: siete de once identicas, cuatro que
   cambian de revision, tres hojas nuevas, y la advertencia de que en `006-011` seis de siete hojas
   cambiaron de numero, por lo que el cotejo contra el juego anterior se hace por contenido.

## Actualizacion posterior: se elimino el indice del paquete

El `00_INDICE.txt` que iba en la raiz **se elimino**. Habia crecido hasta ser una segunda nota
tecnica en texto plano, con dos bloques que duplicaban las secciones de cambios y de vigencia de la
NT. Su contenido propio (lo que hay en cada carpeta, las notas de formato y la lista de los once
documentos con revision posterior) se absorbio en la NT, que pasa a ser el unico punto de entrada.
Respaldo del indice en `BORRADOR_REV0/_00_INDICE_absorbido_por_la_NT.txt.bak`. La NT quedo en 8
paginas.

## Contexto Interno (No enviar)

- **Ni el correo ni la nota dicen que el paquete de licitacion estaba mal armado.** La vigencia
  se declara en positivo: rige la revision que este paquete entrega y cualquier anterior queda
  reemplazada. La causa, que el paquete acumulo tandas sin retirar la anterior y no llevaba
  indice, queda solo en el registro interno. Decision del usuario del 04-09-2026.
- **La fundacion de la cubierta CIP si se cotizo.** Es la partida 4.3 del Formato, 2,38 m3 y
  $2.287.747, con los 24 pernos F-1554 incluidos. Lo que no tiene partida en ninguna parte del
  Formato es la estructura metalica. La nota lo declara asi, sin hablar de descope.
- **El Formato de Presupuesto viajo con los precios unitarios de ADASA cargados**, y en el
  Capitulo 4 como formula visible del tipo `=739414*1.3`. Ya esta adjudicado y no tiene remedio;
  queda registrado y no se menciona.
- **El BL contractual no desciende del `.md` del repositorio.** Lo edito Jorge Valdes el
  25-06-2026 sobre el Word. Por eso ni el correo ni la nota remiten revision alguna de las Bases.
- **Ninguna de las ocho laminas nuevas declara su estado de emision** en el cajetin. Observado a
  los dos proyectistas, no mencionado.
- **Dos laminas civiles no se re-emitieron** pese al cambio de nivel, ambas del
  `P22-DWG-00-001-001`. Estan pedidas a L&A por correo del 04-09-2026 y se entregaran despues.

## Checklist previo al envio

- [ ] Completar el nombre del contratista en el campo Para
- [ ] Adjuntar el PDF de la NT P22-NT-06-000-001-0
- [ ] Comprimir `INGENIERIA VIGENTE PARA CONSTRUCCION/` en ZIP y verificar que abre
- [ ] Verificar el enlace de descarga sobre el texto del correo enviado, no sobre el script
- [ ] Confirmar que la planilla de control de cambios viaja dentro del ZIP

## Checklist posterior al envio

- [ ] Cambiar el estado de este archivo de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Registrar el envio en la Bitacora del README
- [ ] Abrir el seguimiento del acuse con vencimiento el 11-09-2026
