---
titulo: Reclamo de reportería semanal a BW Water — DDSR ausente y cronograma colapsado
codigo: Reclamo reportería semanal
fecha: 2026-08-05
estado: BORRADOR
second_brain: skip
---

# Reclamo de reportería semanal — DDSR y cronograma completo

**Estado: BORRADOR.** No enviado.

| Campo | Valor |
|---|---|
| Archivo | `2026-08-05_Weekly-Reporting-Gap.docx` · **1 página, 180 palabras** · inglés |
| Para | Eduardo Yamauchi (BW Water) |
| CC | Andrew Sia, Magdier Arias, Víctor Gutiérrez, Jorge Guevara, Ronald Pellejero |
| Asunto | 25007 Taltal - Weekly reporting package: DDSR and full schedule print |
| Cadena | **Coordinación semanal**, no la de transmittals |
| Adjuntos | Ninguno |

## Por qué va en cadena separada

El TM N30 salió hoy por la cadena regular de transmittals. Este reclamo es sobre **reportería de gestión**, no sobre revisión documental, y su interlocutor operativo es el equipo de coordinación semanal. Mezclarlo con el transmittal diluiría ambos.

## Los dos puntos

1. **El DDSR falta por segunda semana consecutiva.** No vino en el paquete del 27-Jul ni en el del 03-Ago. El último que ADASA tiene es del 20-Jul, de modo que la cifra de avance documental con la que se trabaja lleva dieciséis días.
2. **El cronograma del 04-Ago llegó colapsado a 4 páginas**, contra las 11 del 14-Jul y las 12 del 27-Jul, y sin las filas de detalle de ingeniería. Además llegó **fuera del paquete semanal**. Los hitos críticos sí están y se usaron; lo que ya no se puede es seguir el camino crítico tarea por tarea.

Se pide reponer ambos en el paquete del **lunes 10-Ago**.

## Lo que deliberadamente NO dice

- **Nada del atraso del Plazo de Entrega ni de la exposición a multa.** Eso pertenece a la cadena contractual y tiene su propio instrumento; meterlo aquí convertiría un reclamo de reportería en una escalación y le quitaría filo a las dos peticiones.
- **Ningún reproche por las fechas del cronograma.** El documento del 04-Ago se aceptó como el vigente; lo que se objeta es su formato y su vía de entrega, no su contenido.
- **Ninguna mención al Change Log vacío ni al Milestone Tracker congelado.** Son hallazgos reales y están registrados, pero abrir tres frentes en un correo de una página no los resuelve ninguno.

## Verificación de fuentes

| Afirmación | Verificado contra |
|---|---|
| DDSR ausente en dos paquetes | Listado de directorio de `SEMANA 27-07-26/` y `SEMANA 03-08-26/` |
| Último DDSR del 20-Jul | Registro del proyecto y `_ANALISIS_PROGRAMA_04AGO.md` |
| 4 páginas contra 11 y 12 | Conteo directo sobre los tres PDF: 04-Ago = 4 págs / 13.195 chars; 27-Jul = 12 / 51.135; 14-Jul = 11 |
| El cronograma llegó fuera del paquete | Está en `PROGRAMA DE MITIGACION/`, no en `SEMANA 03-08-26/` |

## Checklist pre-envío

- [x] `anti-ia`: VERDE — 180 palabras, 9 oraciones, media 20,0, sigma 8,8, cero fingerprints. Las dos apariciones de `critical` son *"critical milestones"* y *"critical path"*, vocabulario de cronograma
- [x] Metadatos Word limpios (`docx_metadata`, autoría Luis Rivera Gonzalez, en-US)
- [x] PDF de una página desde Word real
- [ ] Confirmar destinatarios y que va por la cadena de coordinación semanal, no por la de transmittals
- [ ] Enviar

## Checklist post-envío

- [ ] `BORRADOR` → `ENVIADO` aquí y en el README
- [ ] Dejar el respaldo del envío en esta carpeta
- [ ] Cerrar o actualizar `PRG-23` en `compromisos.yaml` según la respuesta
