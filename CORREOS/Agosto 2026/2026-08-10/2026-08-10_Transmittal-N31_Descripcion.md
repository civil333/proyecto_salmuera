---
titulo: "Correo de cobertura — Transmittal N31 (submittals 25007-0072 y 25007-0074)"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: skip
date: 2026-08-10
---

# Correo de cobertura — Transmittal N31

**Estado: ENVIADO el lunes 10-Ago-2026 a las 15:33.** Respaldo en esta carpeta: `respaldo envio transmittal 31.pdf`.

## Datos del envío, tomados del respaldo

| Campo | Valor |
|---|---|
| Fecha y hora | lunes 10-Ago-2026 15:33 |
| Asunto | ADASA – Taltal Brine Module: Technical Review Transmittal N31 (25007-0072/0074) |
| Para | Eduardo Yamauchi, Fitri Indriyani (BW Water); Victor Gutiérrez, Ronald Pellejero, Jorge Guevara (ADASA) |
| CC | Allan Valentos, Jeryl F. Regulacion, Nick Huta, Sadeep Irugalbandara, David Chee Keat Swee, Andrew Sia, Adzlan Bin Abd Rahim, Tanya Figueroa |
| Cadena | Regular de transmittals |
| Adjunto | `TRANSMITTAL N31 ADASA-BW_WATER.pdf`, 9 páginas |
| Por enlace | Los tres `CC_ADASA`: Tie-In Point Layout, GA of SWRO System Skid y HMI Display Screenshot |

> El asunto y la distribución que salieron difieren del borrador del script, que proponía un asunto más largo y una copia más corta. Manda lo enviado.

## 🔴 El párrafo del enlace no salió en el cuerpo

Verificado sobre el respaldo: los únicos hipervínculos del correo enviado son los de la firma corporativa y los de Outlook. **La URL de Synology no aparece**, ni la frase que la introduce. Es la segunda vez seguida: pasó igual en el N30.

Consecuencia práctica: los tres `CC_ADASA` solo son alcanzables por el enlace **impreso** en la Sección 4 del PDF adjunto, que sí salió. **Acción pendiente:** una línea de respuesta sobre este mismo hilo con el enlace, para que no dependa de que abran el PDF.

## Qué dice

Cuatro bloques, 311 palabras, una página. Una línea de veredicto —**2 — Approved as noted**— con los dos submittals; la disposición en una cláusula por documento; **el hincapié**; y el primer punto a atacar.

**El hincapié es el mensaje del correo:** diez condiciones de aprobaciones de ADASA siguen sin incorporar en **cinco documentos ya emitidos a Rev 0 para construcción** — seis de los procedimientos PMI, Visual, Painting y HP and LP Pressure Test de la ENTREGA 71, y cuatro de la Plant Control Philosophy de esta entrega. Y por qué importa, en una frase: sobre un Rev 0 ya no queda código con que devolverlo, la corrección solo cabe en la próxima emisión, y mientras tanto se fabrica y se inspecciona contra el documento tal como está. Cierra pidiendo confirmación de cómo y cuándo se cierra cada uno de los diez puntos.

El primer punto es el mapeo de sensores de temperatura, porque el mismo error aparece en dos documentos y mantiene retenida la firma de protección por RTD del FAT Procedure desde el Transmittal N27.

No repite el fundamento de cada punto, ni los seis TAG del HMI, ni el detalle de la Sección 3: eso vive en el transmittal. No propone reunión.

## Aritmética que debe cuadrar con el transmittal

| Dónde | Qué dice |
|---|---|
| Correo | diez condiciones en cinco documentos a Rev 0 |
| Transmittal, Sección 3 | seis condiciones en cuatro de los cinco documentos de la ENTREGA 71 |
| Transmittal, Sección 2 | cuatro condiciones de la Plant Control Philosophy |

Seis más cuatro son diez; cuatro documentos más uno son cinco. **Si cambia alguna de esas cifras, hay que cambiarla en los dos documentos.** El RO Vessel Hydrostatic Test Procedure Rev 0 no entra en el recuento: su condición se cumplió y quedó Código 1, y su punto de vigencia de calibración es un pedido nuevo.

## Verificación de fuentes

- Veredictos y textos: `REVISIONES/TRANSMITTALES/P22-TM-09-000-031-0/P22-TM-09-000-031-0_TRANSMITTAL.md`.
- Verificación punto por punto de la E72: `ENTREGAS_BWWATER/ENTREGA 72/_LEDGER_COMENTARIOS.md`.
- Verificación punto por punto de la E73: `ENTREGAS_BWWATER/ENTREGA 73/_LEDGER_COMENTARIOS.md`.
- Destinatarios: memoria `reference_contactos_bw_water`.

## Contexto interno (no enviar)

El alcance del transmittal lo acotaste a los comentarios históricos no levantados. Todo lo que las dos entregas trajeron de nuevo quedó registrado en los `_HALLAZGOS_DETERMINISTAS.md` de cada una y **no se emite**.

La Plant Control Philosophy no lleva código por decisión tuya: sobre un Rev 0 solo caben Código 1 o Código 3, y devolver a revisión un documento ya emitido para construcción sube el conflicto. El correo evita cualquier palabra que suene a devolución y se limita a declarar los puntos abiertos.

El procedimiento hidrostático quedó Código 1 aun cuando el certificado de calibración que adjunta está fechado el 12-Dic-2025 y el ensayo se ejecutó el 17-Jun-2026, cinco días después del intervalo de seis meses que fija la cláusula 4 del propio procedimiento. Esa validez se pide como punto propio en la Sección 3, no como degradación del código.

## Checklist antes de enviar

- [x] Enlace Synology puesto en `crear_correo_tm31.py` y en `crear_transmittal.py`, y los dos documentos regenerados. El enlace es único y coincide en ambos.
- [x] PDF del transmittal generado desde Word real, 8 páginas, con el índice resuelto y sin el marcador de campo. Correo en PDF, 1 página.
- [x] `anti-ia` modo `revisar` sobre el `.md` del transmittal: una antítesis retórica corregida, el resto limpio.
- [x] Subir los tres `CC_ADASA` a la carpeta compartida del enlace.
- [🔴] **Verificar que el párrafo del enlace salga al pegar el cuerpo en Outlook.** **Falló.** No salió, igual que en el N30. Ver arriba.

## Checklist después de enviar

- [x] Estado a `ENVIADO` con la hora, el asunto y la distribución reales.
- [x] Respaldo del enviado en esta carpeta: `respaldo envio transmittal 31.pdf`.
- [x] Updater del Master Register corrido: 51 Código 1 / 29 Código 2 / 5 Código 3 / 0 Código 4, más un documento sin código; transmittals a 31 y entregas a 73.
- [x] Entrada de Bitácora del README a `ENVIADO` y fila en el Índice de Transmittales.
- [ ] **Responder el propio hilo con el enlace de descarga**, porque no salió en el cuerpo.
