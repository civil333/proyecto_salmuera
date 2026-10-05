---
titulo: Ledger de revisión — ENTREGA 100 (submittal 25007-0100)
fecha: 2026-10-05
estado: INTERNO
type: ledger
project: salmuera-taltal
second_brain: skip
---

# Ledger de revisión — ENTREGA 100

> **DOCUMENTO INTERNO ADASA — NO ENVIAR.**

Submittal `25007-0100`, emitido el jueves 1-Oct-2026, devolución pedida el domingo 4-Oct. El plazo de la Cláusula 37.2, descontando el feriado del lunes 12, vence el martes 13-Oct. Un documento: **Valve List `P22-LI-09-005-002` Rev 0**, IFC, tres páginas, con hoja de comentarios en la página 3. Viene de Código 2 en el N39 (Rev E).

## Cierre punto por punto contra el N39 (Sección 2.1)

| Pedido, literal | Declarado en la hoja | Verificado en la Rev 0 | Estado |
|---|---|---|---|
| "state the body, trim and seat material of VM-09-065 against the CIP pump suction line as the approved Line List defines it, and its end connection and rating (OBS-01 on the annotated PDF)" | "Noted, updated VM-09-072 valve material and VM-09-065 Pipe Material." | Fila VM-09-065, página 2: DN150, BUTTERFLY VALVE, manual, **body PVC, trim PVC, disc PVC, seat EPDM**, servicio CIP, **pipe SS316L**, Lug, SCH10, ANSI 150#. **Cambió solo la columna de material de cañería** (de PVC SCH80 a SS316L SCH10). La válvula sigue en PVC sobre la línea `CP-SS316-DN150-09-022`, que la Line List Rev 1 y la Rev 2, ambas aprobadas en Código 1, llevan en 316L | **Cerrado**: la Rev 0 declara el material de la válvula frente a la línea, que es lo pedido (ver abajo) |

**Verificación adversarial del 5-Oct: el Código 3 no se sostiene.** El N38 aceptó el cambio de la succión CIP a 316L *"because an eccentric PVC reducer could not be sourced"*, como sustitución por disponibilidad y no por servicio. La Line List gobierna la cañería, no la válvula. La ET Sección 5.2.1 describe otra mariposa (disco super dúplex, asiento PTFE, cuerpo de fundición gris, wafer, solo de 3" a 4"), y la VM-09-065 está en PVC lug desde la Rev D aprobada en el N18, como las demás mariposas del circuito CIP. La condición del N39 pedía declarar el material de la válvula frente a la línea, y la Rev 0 lo declara: PVC y EPDM, lug ANSI 150, sobre la línea SS316L.

La VM-09-072, que se cambió a SS316L con extremo socket weld sin que nadie lo pidiera, es según el verificador el drenaje DN15 de la misma línea 022 en el P&ID Rev 0 (no comprobado aquí). El criterio de BW Water sería coherente: lo que se suelda a la cañería de acero pasa a acero, y la mariposa, apernada, sigue en PVC.

## Disposición

**Código 1**, sin CC_ADASA. El script y el PDF que se alcanzaron a generar quedan en `REVISIONES/TRANSMITTALES/P22-TM-09-000-042-0/COMENTARIOS/_no_emitido/`. En la tabla de levantamiento del transmittal, el OBS-01 del N39 figura como cerrado. Si ADASA tuviera una razón técnica para exigir la válvula en acero, el camino es una consulta técnica, no retener un documento emitido para construcción.
