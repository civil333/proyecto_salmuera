---
titulo: Auditoria de emision para construccion de los entregables de BW Water
fecha: 2026-09-09
estado: BORRADOR
destinatario: Eduardo Yamauchi (BW Water Americas)
type: correo
project: salmuera-taltal
---

# Auditoria documento por documento y reclamo de emision en revision 0

**Estado: BORRADOR.** Sin datos faltantes. Correo en ingles a Eduardo Yamauchi, con copia a
Victor Gutierrez y Jeryl Regulacion. **Plazo pedido: viernes 11 de septiembre**, que es el que
la reunion de hoy fijo para cerrar los hitos documentales.

## Que dice el correo

| Bloque | Contenido |
|---|---|
| Apertura | Ancla en la conversacion de hoy: se fijo el viernes 11 para cerrar los hitos documentales y se conversaron dos planos de estanques, que resultan ser parte de un conjunto mayor |
| Hallazgo | De los 72 documentos de ingenieria, **46 nunca se emitieron para construccion**, y **34** de esos no tienen ninguna observacion abierta. Mediana de 184 dias desde la aprobacion, maximo 267 |
| El argumento | **La regla la escribio BW Water**, en la hoja de comentarios del plano de puesta a tierra Rev E del 12 de mayo. Se cita literal |
| El DDSR | Bloque nuevo: el registro con que BW Water gestiona la revision **no mide la emision**. Sus doce columnas no tienen ninguna de emision para construccion y las cadenas IFC y Rev 0 no aparecen. Su ponderador da 100 % a un aprobado sin mirar la revision, y **34 de los documentos de las tablas figuran ahi al 100 %** |
| Tabla 1 | Los 34 en Codigo 1 sin emitir, en 25 filas: los diez datasheets de instrumentos van agrupados por rango de codigo |
| Tabla 2 | Los 12 en Codigo 2 sin emitir, con su condicion abierta en una clausula |
| Tabla 3 | Los 7 de calidad y fabricacion en revision de letra, separados como pidio el usuario |
| Tabla 4 | Los 7 entregables de la Seccion 7 que no se han recibido |
| Bloque 5 | Los 11 documentos en revision numerica cuyo cajetin sigue diciendo que son para aprobacion |
| Se pide | **Todo emitido en revision 0 al viernes 11**: los 34 sin cambio de contenido, los 12 con su condicion, los 7 de calidad, el cajetin de los 11 y los 7 entregables faltantes. Lo que no alcance, con fecha declarada ese mismo dia **en el DDSR**, que tiene columna para eso |

## De donde sale cada cifra

Ninguna se escribio a mano. El generador importa `auditar()` de
`REVISIONES/EVALUACIONES/auditar_documentos_bw.py`, que clasifica los 113 items del Master
Deliverable Register cruzandolo con los formularios de submittal y con el cajetin de cada PDF. El
respaldo con la tabla completa es `_AUDITORIA_REV0_2026-09-09.md`, que **no se envia**.

| Cifra | Valor | Como se obtiene |
|---|---|---|
| Items auditados | 113 | Filas de la hoja Master Register |
| Ingenieria / calidad / sin codigo | 72 / 17 / 24 | Tipo del codigo: DWG, LI, ET, CD, BT contra BA, PP, MTC |
| Sin emitir para construccion | 46 de 72 | Revision no numerica y veredicto 1 o 2 |
| Documentos al 100 % en el DDSR estando sin emitir | 34 | Columna `Weight (%)` del DDSR del 07-09 |
| Filas del DDSR con fecha planificada | 10 de 73, seis de ellas el 11-Sep | Tercera fecha de cada fila |
| De ellos en Codigo 1 | 34 | Los anteriores con veredicto 1 |
| Mediana y maximo de dias | 184 y 267 | Primer ciclo con Codigo 1 o 2 en la hoja Revision History, contra el 09-09-2026 |
| Revisiones sometidas como IFA | 49 | Columna `Sub. For` del formulario de la entrega vigente |
| Cajetin que se contradice | 11 | Revision numerica con `ISSUED FOR APPROVAL` en el PDF |

## Revision de estilo

Pasado por la skill `anti-ia` en modo `revisar`. El original salio **AMARILLO**: sobraba
extension (926 palabras de prosa para un correo cuyo nucleo son cuatro tablas), llevaba la
cascada de ordinales en el pedido, y fallaba dos reglas duras del perfil, el em dash y el
punto y coma, que el corpus del autor tiene en cero. La version final queda **VERDE** con
**627 palabras**, un tercio menos, y con los ocho rasgos del registro de correspondencia en
banda: mediana de oracion 18,5 contra 18 del perfil, percentil 90 en 35,1 contra 35,
parentesis 6,38 por mil contra 6,18, y cero em dash, punto y coma y ornamento. La voz pasa a
primera persona, que es lo que manda ese registro.

Veredicto persistido en `.anti-ia-2026-09-09/veredicto.md`, con la linea de cobertura
auditada en verde por `inventory.py --check-veredicto`.

## Las tres citas, verificadas sobre el PDF

1. **La regla del proveedor**, pagina 4 de
   `ENTREGAS_BWWATER/ENTREGA 42/P22-DWG-09-007-003_E ....pdf`: *"Description "Issued For Approval"
   remaining the same until the document/drawing is approved and then will change to "Issued For
   Construction - Rev0""*.
2. **La leyenda del formulario** `PEM-F013` Rev 3 define `FA`, `FR`, `FI`, `IFC` y `AB`. **`IFA` no
   aparece en ella**, y BW Water lo usa desde el submittal 25007-0019.
3. **Los tres datasheets Fedco** de la entrega 90: revision 0, sometidos `IFC` en el formulario, y con
   `Issued for: ISSUED FOR APPROVAL` dentro del documento.

## Contexto Interno (No enviar)

- **Lo que se dejo fuera por decision del usuario**, y sigue disponible si el frente escala: el idioma
  castellano de la Clausula 6 de la BAE, que admite ingles solo en la oferta tecnica; el hito de pago
  del 10 % que exige la totalidad de la ingenieria aprobada; la multa de la Clausula 43.1 letra a),
  0,05 % diario por atraso en la ingenieria de la Seccion 7; y la frase de la ET segun la cual sin
  toda la documentacion aprobada el proveedor no puede liberar los equipos para transporte. El cierre
  del correo lleva una reserva generica para no renunciar a ninguno al no invocarlos.
- **La defensa previsible de BW Water es que nunca se le fijo una fecha**, y en sentido estricto es
  cierta: los transmittals instruyeron *issue directly at IFC Rev 0* sin plazo. La frase
  *"ADASA has not set a date for these reissues until now, and that is what this email fixes"* esta
  puesta a proposito para desactivar esa respuesta antes de que llegue, y la clausula de cierre pide
  fecha comprometida para lo que no alcance a emitirse.
- **ADASA si lo pidio una vez y no lo persiguio.** El correo del 07-May-2026 a Eduardo y Andrew Sia
  pidio *"a binding date for Spanish IFC Rev 0 of the full Section 1 set"*. La fecha nunca llego y el
  pedido **nunca entro al Registro de Compromisos**, de modo que dejo de seguirse. Es un defecto de
  gestion propio y se corrige creando el compromiso.
- **El Project Schedule quedo fuera de la tabla 3** porque su seguimiento se retiro del ciclo de
  transmittals en el N36 y se lleva por la reunion semanal. Incluirlo reabriria algo que ya se cerro.
- **El paquete de calidad sirve de contraste y el correo lo dice**: ese si esta migrando a revision 0,
  lo que demuestra que el proveedor sabe hacerlo y que el problema no es de capacidad.
- La lista de instrumentos y la de valvulas, que gobiernan la interfaz de control y la compra, siguen
  en revision F y D respectivamente, aprobadas desde el 15 de abril.

- **La minuta del 9 no es oponible.** Es un resumen automatico generado desde la grabacion, sin
  membrete, sin firma y con los asistentes rotulados como Speaker 1, Speaker 2. En ella **no se hablo
  de revision 0 ni del DDSR**: cero menciones de ambos. Por eso el correo cita la conversacion y el
  cierre del viernes, y no invoca la minuta como acuerdo sobre la emision.
- 🔴 **Dos correcciones al registro de ADASA que la auditoria destapo y que habrian arruinado el
  correo.** El `P22-CD-09-005-001` esta emitido en revision 0 desde la entrega 71 del 6 de agosto, y
  los propios transmittals N37 y N38 lo declaran asi; el Master Register lo tenia en Rev B del N29 y
  la tabla 2 lo habria reclamado como no emitido. Y la **entrega 91 trae la Valve List Rev E y el GA
  del estanque de antiescalante Rev D**, sin revisar todavia: el correo lo reconoce en una linea en
  vez de afirmar que la revision del registro es la ultima que enviaron.
- 🔴 **El DDSR declara dos planos en revision 0 que nunca llegaron**: el Cable Tray Layout, que ADASA
  tiene en Rev C, y el GA del estanque de lavado CIP, en Rev B. Verificado sobre el arbol de entregas:
  no existe archivo en revision 0 de ninguno de los dos. El correo lo pregunta en vez de afirmarlo.
- **Sobre la viabilidad del plazo.** Son 53 documentos a emitir en dos dias y los 12 con observacion
  exigen incorporar cambios antes de emitir. La clausula de cierre pide que lo que no alcance venga
  con fecha ese mismo dia, de modo que el viernes haya documentos o fechas y no silencio.
- **Municion que la reunion agrego y no se usa:** Eduardo confirmo alli que el procedimiento SAT y el
  dossier final se entregaran en espanol. Sostiene el frente del idioma de la Clausula 6, que sigue
  fuera del correo por decision del usuario.

## Checklist previo al envio

- [ ] Confirmar que el plazo del viernes 11 sale tal cual, con 53 documentos por emitir en dos dias
- [ ] Revisar que el nombre del cargo del remitente sea el vigente
- [ ] Verificar que las cuatro tablas se pegan legibles en Outlook y no pierden los bordes

## Checklist posterior al envio

- [ ] Cambiar el estado de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Fijar el `PRG-48` con vencimiento al 11 de septiembre
- [ ] Registrar en la Bitacora del README
