---
titulo: "Consulta a BW Water — paquete de reportería semanal y DDSR"
proyecto: salmuera-taltal
estado: ENVIADO
second_brain: skip
date: 2026-08-10
---

# Paquete de reportería semanal y Document and Drawing Status Report

**Estado: ENVIADO el lunes 10-Ago-2026.** Cadena de coordinación semanal.

> **Falta archivar el respaldo del enviado en esta carpeta**, y con él la hora exacta.

## Datos del envío

| Campo | Valor |
|---|---|
| Fecha | 10-Ago-2026 |
| Para | Eduardo Yamauchi, Fitri Indriyani (BW Water) |
| CC | Victor Gutiérrez, Ronald Pellejero, Jorge Guevara (ADASA); Jeryl F. Regulacion, Stephane Gehant (BW Water) |
| Asunto | 25007 Taltal - Weekly reporting package and Document and Drawing Status Report |
| Cadena | Coordinación semanal |
| Extensión | 145 palabras de cuerpo, una página |
| Adjuntos | Ninguno |

**Bureau Veritas no va en este correo**: el desempeño de reportería del proveedor frente a ADASA no se expone a un tercero contratado por ADASA. Lo que sí le compete, la jornada del 7-Ago, va en el correo conjunto `2026-08-10_Inspection-002-Records.docx`.

## Qué dice

**Distingue dos documentos que no son lo mismo**, que es lo que el correo tiene que dejar claro:

- **El informe de avance semanal sí ha estado llegando.** El último es el de la **semana 31**, que cubre del 27-Jul al 2-Ago y vino en el paquete del 3-Ago. Lo que falta es el de **esta semana, la 32**.
- **El DDSR es lo que lleva dos paquetes sin aparecer.** El más reciente que ADASA tiene es el del **20-Jul**; los paquetes del 27-Jul y del 3-Ago trajeron cada uno su informe de avance pero no el reporte de estado.

Explica por qué el DDSR importa —es la referencia con que ADASA sigue la posición de cada documento y las fechas de reemisión comprometidas, y el Transmittal N31 emitido hoy lo cita para tres planos con fecha vencida— y cierra preguntando por el paquete de esta semana con el informe de la semana 32, y si el reporte de estado viene con él.

> **Precisión que el usuario corrigió sobre el primer borrador.** La redacción inicial decía que el reporte llevaba dos semanas sin llegar, y eso mezclaba los dos documentos: daba a entender que no llegaba nada desde hacía dos semanas, cuando el informe de avance sí llegó las semanas 30 y 31. Reclamar de más sobre algo que sí se entregó debilita el punto que sí es cierto.

## Precisión que evita un reclamo débil

Los paquetes semanales se archivan los **martes** (mtime 21-Jul, 28-Jul, 4-Ago), de modo que hoy lunes **no se afirma que el de esta semana esté atrasado**, solo que no ha llegado. Lo verificable y afirmado es la ausencia del DDSR en los dos anteriores.

## Verificación de fuentes

| Afirmación | Fuente |
|---|---|
| Último DDSR: 20-Jul | `SEMANA 20-07-26/25007_Taltal_DDSR_2026.07.20.pdf`; no hay ninguno posterior en todo el proyecto |
| Los paquetes del 27-Jul y del 3-Ago trajeron informe de avance pero no DDSR | Listado de esas dos carpetas: `PROGRESS REPORT (WEEK 30)` y `(WEEK 31)` más el tracker, sin DDSR |
| El informe de la semana 31 cubre del 27-Jul al 2-Ago | Cabecera del propio PDF: *"Date: 7/27/2026 - 8/2/2026 (Week 31)"* |
| Esta semana no ha llegado nada | No existe carpeta `SEMANA 10-08-26` y nada de ese árbol se ha tocado desde el 04-Ago 17:28; barrido de todo el proyecto por DDSR, progress, tracker, fabrication schedule y coordination posteriores al 05-Ago: cero |
| El N31 cita el DDSR del 20-Jul para tres planos vencidos | Sección 3 de `P22-TM-09-000-031-0_TRANSMITTAL.md` |

## Contexto interno (no enviar)

**El correo del 5 de agosto que reclamaba la reportería nunca se envió**: quedó en `BORRADOR` y el respaldo de esa carpeta corresponde al transmittal N30. Por eso éste se redacta como primera consulta y **no dice "como pedimos el 5 de agosto"**. Conviene archivar aquel borrador como superado por éste.

**Lo que se dejó fuera a propósito.** El tracker de procura **sí cambia de contenido cada semana** pese a conservar el nombre de archivo — verificado por md5, son tres archivos distintos —, así que no se reclama. El Plazo de Entrega vencido y la exposición a multa viven en la cadena contractual y aquí le quitarían filo a la pregunta. No se propone reunión.

## Checklist

- [x] Cero em dash, sin fingerprints, ninguna oración sobre 40 palabras.
- [x] PDF desde Word real, una página. Metadatos limpios, idioma en-US.
- [x] Revisado y enviado.
- [x] Estado a `ENVIADO` y entrada de Bitácora.
- [ ] **Archivar el respaldo del enviado en esta carpeta**, con la hora.
- [ ] Archivar el borrador del 05-Ago (`crear_correo_reporting_gap.py`) como superado.
