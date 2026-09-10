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
| Nota Tecnica `P22-NT-06-000-001-0` revision 0 | 16 paginas, con la tabla de vigencia de los 55 documentos y las 14 partidas del Formato. Unico documento de control. Revisada el 10-09-2026 con la ENTREGA 15 de L&A y los nativos DWG |
| Paquete `INGENIERIA VIGENTE PARA CONSTRUCCION` | **55 documentos en 154 archivos**, cada plano en PDF y en DWG; reconstruido y verificado el 10-09-2026 |
| Planilla `P22-LI-06-000-002-1` | **Ya no viaja**: la nota la absorbio el 09-09-2026 y queda como respaldo interno en `BORRADOR_REV0` |

El correo declara lo sustantivo en cuatro parrafos: que se comparte para revision, que contiene el
paquete, que cambio respecto de lo cotizado, y la advertencia del modelo de 6,4 gigabytes que se
entrega por enlace.

## Cifras que el correo declara

| Dato | Valor |
|---|---|
| Documentos y archivos del paquete | 55 en 154, con la nota como unico archivo de la carpeta 0 y 66 DWG junto a sus PDF |
| Laminas civiles | 18, diez en revision 0 y ocho en revision 1 |
| Partida 4.2, fundacion del sistema CIP | de 7,36 a 5,80 m3 |
| Partida 4.6, excavacion comun | de 115,10 a **90,64 m3** |

## Contexto Interno (No enviar)

- **La partida 4.6 se corrigio dos veces.** La Nota Tecnica declaraba 111,70 desde el 4 de septiembre.
  Los 115,10 del Formato contractual se reconstruyeron y calzan como 95,96 por 1,2, es decir volumen
  retirado esponjado, mientras la partida se mide por metro cubico excavado. Manteniendo ese criterio,
  la cantidad vigente es 90,58 sobre 75,48 excavados. La nota declara el criterio en una frase, sin
  explicar el error anterior.
- **La reemision de L&A llego el 10-09 (ENTREGA 15, carta TT-016)** y cerro seis de las siete
  discrepancias; la OBS-05 volvio como "no aplica" con razon (el rotulo M.H.A. del plano de la fosa
  es el muro, no un mejoramiento). Con eso la zona CIP rige en **1,03** (L&A unifico en la cifra del
  movimiento de tierra), el estanque sube a 4,84, el total excavado queda en 75,53 y la partida 4.6 en
  **90,64**. La nota y los `LEEME.txt` siguen declarando solo lo que rige, sin narrar el ciclo de
  comentarios. Verificacion en `INGENIERIA DE DETALLE OOCC/REVISIONES/TRANSMITTALES/P22-TM-00-010-005-0/_ANALISIS_TRABAJO.md`.
- **El paquete lleva desde el 10-09 cada plano en PDF y en DWG** (66 nativos), por instruccion del
  usuario; la nota lo declara en el contenido del paquete.
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
