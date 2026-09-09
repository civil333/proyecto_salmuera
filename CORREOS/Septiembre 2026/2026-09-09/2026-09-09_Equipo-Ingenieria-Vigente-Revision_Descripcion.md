---
titulo: Ingenieria vigente para construccion, revision del equipo antes de emitirla al contratista
fecha: 2026-09-09
estado: BORRADOR
destinatario: Equipo de proyecto de Aguas Antofagasta
type: correo
project: salmuera-taltal
---

# Revision interna del paquete de ingenieria vigente

**Estado: BORRADOR.** Sin datos faltantes. Comparte la Nota Tecnica `P22-NT-06-000-001-0` y el paquete
`INGENIERIA VIGENTE PARA CONSTRUCCION` con el equipo, para revision antes de emitirlo al contratista
del montaje. Comentarios pedidos al **viernes 11 de septiembre**.

## Que se comparte

| Pieza | Estado |
|---|---|
| Nota Tecnica `P22-NT-06-000-001-0` revision 0 | 16 paginas, con la tabla de vigencia de los 55 documentos y las 14 partidas del Formato. Unico documento de control |
| Paquete `INGENIERIA VIGENTE PARA CONSTRUCCION` | **55 documentos en 88 archivos**, reconstruido y verificado hoy |
| Planilla `P22-LI-06-000-002-1` | **Ya no viaja**: la nota la absorbio el 09-09-2026 y queda como respaldo interno en `BORRADOR_REV0` |

El correo declara lo sustantivo en cuatro parrafos: que se comparte para revision, que contiene el
paquete, que cambio respecto de lo cotizado, y la advertencia del modelo de 6,4 gigabytes que se
entrega por enlace.

## Cifras que el correo declara

| Dato | Valor |
|---|---|
| Documentos y archivos del paquete | 55 en 88, con la nota como unico archivo de la carpeta 0 |
| Laminas civiles | 18, diez en revision 0 y ocho en revision 1 |
| Partida 4.2, fundacion del sistema CIP | de 7,36 a 5,80 m3 |
| Partida 4.6, excavacion comun | de 115,10 a **90,58 m3** |

## Contexto Interno (No enviar)

- **La partida 4.6 se corrigio dos veces.** La Nota Tecnica declaraba 111,70 desde el 4 de septiembre.
  Los 115,10 del Formato contractual se reconstruyeron y calzan como 95,96 por 1,2, es decir volumen
  retirado esponjado, mientras la partida se mide por metro cubico excavado. Manteniendo ese criterio,
  la cantidad vigente es 90,58 sobre 75,48 excavados. La nota declara el criterio en una frase, sin
  explicar el error anterior.
- **Hay una reemision pedida a L&A al viernes 11.** El correo del 9 de septiembre le pidio resolver
  siete discrepancias entre planos, `OBS-01` a `OBS-07`. Dos de ellas afectan cantidades: la excavacion
  del contenedor y la de la zona del sistema CIP. **Nada de eso aparece en la Nota Tecnica ni en los
  `LEEME.txt`**, por decision del usuario: el paquete declara las cantidades que rigen y de que plano
  sale cada una, sin exponer que hay un plano por corregir.
- **La cifra de la zona CIP que rige es 1,60**, la del `P22-DWG-00-002-007` LAM1, y no los 1,03 del
  plano de movimiento de tierra. Se eligio la del plano que define la geometria de esa fundacion, que
  ademas es la que la nota venia declarando. Si L&A concilia a la baja, la partida 4.6 pasaria a 89,89.
- **El paquete estaba incompleto en el equipo Windows**: tenia 35 de 88 archivos porque las carpetas de
  los P&ID, las isometrias, el cuadernillo de soportes y los anexos de la ET de HDPE estaban vacias. Se
  reconstruyo con `construir_paquete_construccion.py`, al que se le hizo portable la raiz y se le
  corrigio el bloque del modelo, que todavia copiaba la maqueta de abril.
- El correo del 4 de septiembre dirigido al contratista **queda intacto en su carpeta**, para reusarlo
  cuando se emita, con el nombre de la empresa.

## Checklist previo al envio

- [ ] Comprimir el paquete sin el archivo de nube de puntos y verificar que el ZIP abre
- [ ] Generar el enlace de Synology para `MODULO COMPLETO (nube puntos).nwd` y pegarlo en el correo
- [ ] Adjuntar el PDF de la Nota Tecnica
- [ ] Confirmar que la carpeta `0. CONTROL DE CAMBIOS` del ZIP lleva el PDF de la nota

## Checklist posterior al envio

- [ ] Cambiar el estado de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Registrar en la Bitacora del README
