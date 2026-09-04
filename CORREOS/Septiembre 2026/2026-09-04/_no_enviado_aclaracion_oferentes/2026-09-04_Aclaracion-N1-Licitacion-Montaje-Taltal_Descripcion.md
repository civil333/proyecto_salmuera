---
titulo: Aclaracion N1 a los oferentes - revision 1 del paquete de licitacion de Montaje
fecha: 2026-09-04
estado: BORRADOR
destinatario: oferentes de la licitacion de Montaje Mecanico y Obras Civiles
type: correo
project: salmuera-taltal
---

# Aclaracion N°1 — Licitacion de Montaje Mecanico y Obras Civiles, PD Taltal

**Estado: BORRADOR.** Faltan dos datos que solo puede aportar el usuario, marcados en el
cuerpo con `[COMPLETAR]`: la lista de oferentes invitados y la decision sobre el plazo de
presentacion de ofertas.

## Resumen del cuerpo

Carta corta, en espanol, que comunica la emision de la **revision 1** del paquete
`P22-BL-06-000-001` y explica cuatro cosas:

1. **El cambio de fondo.** La fundacion del contenedor del modulo sube 250 mm, de la cota
   +6,050 a la +6,300, y con ella suben las cuatro cotas de conexion con el modulo. Tabla de
   tres columnas con las cotas de la revision 0 contra las de la revision 1. Las conexiones
   con el modulo existente no cambian.
2. **Las dos cantidades que cambian** en el Capitulo 4 del Formato: la fundacion del sistema
   CIP de 7,36 a 5,80 m3 y la excavacion de 115,1 a 111,7 m3. Se declara explicitamente que
   el Capitulo 1 no cambia de cantidades.
3. **Lo que se agrega**: el Cuadernillo de Soportes (Anexo A3), el Cuadernillo de Isometrias
   (11 isometrias en 31 hojas), el diagrama de flujo, los cuatro P&ID y seis planos de
   cañerias y de ubicacion de soportes.
4. **El Formato se reemplaza**: la planilla va con la columna de precio unitario en blanco y
   las formulas activas, en valores netos, y las ofertas deben presentarse sobre ella.

Cierra apuntando a la carpeta `0. CONTROL DE CAMBIOS` como punto de entrada.

## Verificacion de fuentes

| Dato del correo | Fuente verificada |
|---|---|
| Cotas de tie-in +8,500 / +8,850 | Render del Corte A de `P22-DWG-06-006-102` Rev 1 (E16) contra su Rev 0 |
| Cota de fundacion +6,300 y sello +5,400 | Texto de `P22-DWG-00-002-003` LAM1 Rev 1 (E12) contra su Rev 0 |
| Fundacion CIP 7,36 a 5,80 m3 | Cuadro de cubicacion de `P22-DWG-00-002-007` LAM1, leido por render en ambas revisiones |
| Excavacion 115,1 a 111,7 m3 | Delta del cuadro de excavacion de la zona CIP, de 5,01 a 1,60 m3 |
| Documentos que se agregan | Conteo en disco: el dossier A1 pasa de 15 a 58 archivos |
| El Formato sale sin precios | `generar_formato_presupuesto.py` en su modo por defecto; verificado celda a celda |

## Contexto Interno (No enviar)

- **El paquete distribuido tenia tres defectos** que esta revision corrige y que la carta no
  nombra como defectos, porque no corresponde exponerlos al oferente: al dossier mecanico le
  faltaban 43 de sus 58 archivos; la planilla del Formato que estaba en el repositorio llevaba
  **los precios unitarios internos de ADASA cargados**; y el plano `P22-DWG-06-006-103` viajo
  emitido "PARA REVISION DEL CLIENTE" en vez de para construccion. La carta presenta los dos
  primeros como incorporacion y reemplazo, que es lo que operativamente son.
- **Pendiente de confirmar antes de enviar:** que copia del Formato recibieron efectivamente
  los oferentes. Si viajo la valorizada, el asunto deja de ser de armado de paquete.
- **Ninguna de las ocho laminas nuevas declara su estado de emision** en el cajetin. Esta
  observado a los dos proyectistas y no se menciona en la carta.
- El P&ID de alimentacion Rev 1 llego solo en DWG; el paquete mantiene su Rev 0 y el BL lo
  declara en el Anexo A1.

## Checklist previo al envio

- [ ] Completar la lista de oferentes en el campo Para
- [ ] Decidir y escribir el plazo de presentacion de ofertas
- [ ] Confirmar que copia del Formato recibieron los oferentes
- [ ] Comprimir `Bases REV 1/` en ZIP y verificar que el enlace de descarga abre
- [ ] Verificar el enlace sobre el texto del correo enviado, no sobre el script
- [ ] Adjuntar o enlazar la planilla `P22-LI-06-000-002-1_Cambios-REV0-a-REV1.xlsx`

## Checklist posterior al envio

- [ ] Cambiar el estado de este archivo de BORRADOR a ENVIADO
- [ ] Dejar el respaldo del enviado en esta carpeta con la hora
- [ ] Registrar el envio en la Bitacora del README
