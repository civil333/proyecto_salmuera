---
codigo: CORREO-INTERNO-2026-03-10-RONALD
tipo: Correo interno
fecha: 2026-03-10
autor: Luis Rivera
destinatario: Ronald (Disciplina Control/Instrumentacion)
asunto: "Control Philosophy Rev A — TM N7 | Comentarios ADASA listos — pendiente tu validacion"
estado: BORRADOR
adjunto: P22-BT-09-009-001_Rev A_CC_ADASA.pdf
---

# Control Philosophy Rev A — TM N7 | Comentarios ADASA listos — pendiente tu validacion

**Para:** Ronald
**De:** Luis Rivera
**Fecha:** 10 de marzo de 2026
**Asunto:** Control Philosophy Rev A — TM N7 | Comentarios ADASA listos — pendiente tu validacion

---

Ronald, termine de revisar la Control Philosophy Rev A (P22-BT-09-009-001) para el TM N7. Salieron bastantes cosas — te paso el resumen para que veas si tienes algo que agregar antes de que lo despachemos.

## Hallazgos — Control Philosophy Rev A

- **UPS:** Declaran 30 minutos de autonomia. La ET exige 8 horas. No conformidad contractual directa.
- **Temperatura motores:** No hay monitoreo continuo. La ET §5.3 exige Pt-100 en devanados y rodamientos de todos los motores. TE-09-001/002 son switches DI (on/off), no transmisores AI — no alcanzan.
- **Consumo energetico:** No hay MVE integrado al PLC para calcular CEE (kWh/m3). Es una garantia contractual — sin esto no podemos verificar nada en comisionamiento.
- **Protocolo:** La CP declara solo 4-20mA, pero la Arquitectura Rev B ya tiene red EtherNet/IP con gateway PLX32. HART tampoco esta declarado y la ET §5.5 lo exige.
- **Permisivo cliente:** BW Water definio 2 DI individuales (Sec 3.3.3). La interfaz correcta es 1 DI de habilitacion general desde ADASA + 1 DO de estado del modulo hacia nosotros.
- **Permisivo arranque HP:** No hay umbral de presion minima como condicion de arranque. El PLC arrancaria la bomba con presion insuficiente desde ADASA — riesgo de cavitacion.
- **Modbus TCP/IP:** La interfaz no esta descrita en ningun lugar de la CP.
- **ISA 101:** No declarado como estandar de diseno HMI. La ET lo exige.
- **Tags antiscalant:** Discrepancia entre VE-07-014/016 y VE-09-014/016.
- **Codigo "BT":** No esta definido en el sistema de codificacion P22.

## Lo que necesito de ti

- Revisar el PDF con los comentarios marcados:
  `REVISIONES/TRANSMITTALES/P22-TM-09-000-007-0/COMENTARIOS/P22-BT-09-009-001_Rev A_CC_ADASA.pdf`
- Si tienes algo que agregar desde tu lado, avísame y lo incluimos
- Si esta OK, confirma y despachamos el TM N7 tal como esta

Gracias,
Luis

---

## Contexto Interno (No enviar)

El TM N7 cubre 4 documentos de la Entrega 14 (06-Mar-2026):
- P22-DWG-09-009-007-A — A/C Unit Dimensional Drawing Rev A
- P22-DWG-09-009-008-A — Piping Layout Rev A
- P22-DWG-09-009-016-A — Tie-In Layout Rev A
- P22-BT-09-009-001-A — Control Philosophy Rev A ← este correo cubre solo este documento

Los otros 3 documentos (planos de mecanica/layout) tienen sus propias observaciones no cubiertas en este correo.
Ronald es jefe de disciplina control/instrumentacion — sus comentarios aplican principalmente a la Control Philosophy.

El DOCX del TM N7 (`TRANSMITTAL N7 ADASA-BW_WATER.docx`) y el PDF comentado ya estan generados y listos para despacho.
El TM N7 incluye 12 observaciones totales sobre la Control Philosophy — este correo resume todas ellas.
