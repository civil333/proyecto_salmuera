---
titulo: Correo de cobertura del Transmittal N40 — FAT Procedure del módulo y submittals 25007-0093 a 0095
fecha: 2026-09-18
estado: ENVIADO
type: correo
project: salmuera-taltal
---

# Correo de cobertura — Transmittal N40

**Archivo:** `2026-09-18_Transmittal-N40-FAT-Procedure.docx` (generado por `crear_correo.py`, 248 palabras con encabezado y firma, unas 110 de cuerpo, inglés, primera persona). Versión ejecutiva pedida por el usuario el 18-Sep: los detalles viven en el transmittal.
**Cadena:** regular de transmittals (Reply-All sobre el hilo del N39 o correo nuevo con el asunto del N40).
**Para:** Eduardo Yamauchi (BW Water). **CC:** Jeryl F. Regulacion (BW Water), Víctor Gutiérrez (ADASA).
**Adjuntos (directos, sin enlace Synology; 6 MB en total):** `TRANSMITTAL N40 ADASA-BW_WATER.pdf`, `P22-BA-09-000-017_A_FAT_Procedure_CC_ADASA.pdf` (181 kB), `P22-CD-09-008-002_C_PLC_LCP_Schematic_CC_ADASA.pdf` (4,9 MB). Los tres viven en `REVISIONES/TRANSMITTALES/P22-TM-09-000-040-0/` y su `COMENTARIOS/`.

## Resumen del cuerpo

1. Remite el N40: submittals 0093 a 0095, catorce documentos, veredicto 3.
2. Tres viñetas, una por bloque: FAT Procedure Rev A Código 3, no es el procedimiento detallado de ET 8.1 e ITP 7.1, **Rev B al viernes 25 de septiembre de 2026**, Hold Point 7.1 hasta la aprobación; Schematic Rev C Código 2, terminal 2711P-T10C22D9P reafirmado y el datasheet aprobado no se revisa, reemplazar la fila 11 en Rev 0; doce documentos Código 1 sin acción.
3. Una línea: las observaciones están itemizadas en los dos PDF anotados. Adjuntos y firma.

Quedó fuera del correo, por decisión del usuario, lo que el transmittal ya lleva o no corresponde a la cobertura: la lista de defectos del FAT, la explicación del -D8S, el agradecimiento por la entrega en fecha y la constancia de la devolución pedida a tres días corridos (el archivo de la E93 llegó el 14-Sep, tres días después de la fecha que pedía su formulario; ADASA revisa en los siete días hábiles de la Cláusula 37.2). Ese último punto queda registrado aquí para el N41 si el patrón sigue.

## Verificación de fuentes

- Plazo Rev B: cinco días hábiles de Malasia desde el viernes 18-Sep = viernes 25-Sep-2026.
- Plazo de ADASA: BAE 37.2, siete días hábiles desde el día hábil siguiente a la recepción; 18 y 19 feriados en Chile; E93 (14-Sep) vence el 24-Sep, E94 y E95 el 29-Sep. El correo no escribe estas fechas, solo la regla.
- Terminal -D9P: TM N30, datasheet `P22-ET-09-008-001` Rev 0 (filas 15 y 18: dos puertos Ethernet RJ45, 1 GB).
- "Llegó en la fecha acordada el miércoles": minuta `P22-MI-10-000-002-0` del 17-Sep, acción 1 de Penang (entrega el 18-Sep). El 16-Sep se había pedido para el 18 por correo (`CORREOS/Septiembre 2026/2026-09-16/`).
- Return Date del Submittal Form 0093: 11-Sep-26; archivo en disco el 14-Sep 11:33.

## Contexto Interno (No enviar)

- Decisión del usuario del 18-Sep: emitir hoy; flujo estándar (Luis / Luis / Víctor en el cajetín); sin Sección 3 de pendientes (al N41); Rev 0 de E93/E94 siempre Código 1 más NOTE; Schematic Código 2 reiterado; solo lo exigible al transmittal.
- El verificador adversarial cambió el tercer motivo del encabezado (de prerrequisito hidrostático a circularidad con el ITP), bajó los instrumentos de prueba a NOTE-02 y corrigió la cuenta de formularios (nueve, no once). Detalle en `_MARCO_REVISION_FAT_NO_ENVIAR.md`, sección 6.
- Compromisos: `PRG-50` (procedimiento FAT) recibido el 18-Sep y no aprobado; nace `PRG-53` (Rev B al 25-Sep, FIJADA ADASA). `BV-13` y `H-03` siguen sin fecha nueva de FAT hasta que BW Water la escriba con el cronograma del 23 o 24-Sep.
- Master Register tras el N40 (esperado): **71 Código 1 / 16 Código 2 / 3 Código 3 / 0 Código 4**, 113 ítems y 90 entregados (la fila 85 del FAT pasa de NOT DELIVERED a Delivered con Código 3; Instrument Location Layout, CIP Pump y Antiscalant Dosing Tank suben de 2 a 1). Tres códigos corridos se corrigen en el mismo updater (-009-009, -009-010, -009-011).
- No se nombra a Bureau Veritas en el correo ni en el transmittal ("third-party inspector"): la figura contractual es "ADASA o su representante".

**ENVIADO el viernes 18-Sep-2026 a las 12:59:52 hora de Chile.** Respaldo: `TALTAL - Transmittal N40 - Module Factory Acceptance Test Procedure and submittals 25007-0093 to 0095.pdf` en esta carpeta; los tres adjuntos viajaron (verificado en el respaldo).

## Checklist

**Antes de enviar:** [ ] abrir el PDF del transmittal y comprobar el índice actualizado y el cajetín (fecha 18-Sep-2026, Luis / Luis / Víctor); [ ] los tres adjuntos cargados; [ ] destinatarios y copia; [ ] fecha del header = fecha de la carpeta (18-Sep).
**Después de enviar:** [x] guardar el respaldo del enviado (PDF o .msg) en esta carpeta con la hora; [x] `estado: ENVIADO` aquí y en `P22-TM-09-000-040-0_TRANSMITTAL.md`; [x] correr `REVISIONES/EVALUACIONES/update_register_n40.py`; [x] `compromisos.yaml` (PRG-50, PRG-53) y regenerar el Excel; [x] README (Estado Vigente, Bitácora, Índice de Transmittales); [x] memorias.
