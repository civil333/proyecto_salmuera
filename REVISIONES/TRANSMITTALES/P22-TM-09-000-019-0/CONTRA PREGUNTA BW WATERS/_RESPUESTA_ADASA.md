---
second_brain: skip
type: otro
project: salmuera-taltal
date: 2026-06-03
---

# Respuesta ADASA a la contra-pregunta BW Water (Grounding Layout Rev E)

Puntero de trazabilidad del ciclo TM N19. **El documento final (correo) NO vive aquí** — se redactó y envió como correspondencia del proyecto.

## Entrante (BW Water)

- **Correo:** Eduardo Yamauchi, Ma 02-Jun-2026 23:05, reenviando consulta de Billy Tan (EIC, 28-May). Thread "25007 Taltal: Ground cable schedule clarification".
- **Adjuntos en esta carpeta:** `comment.xlsx` (4 preguntas + 2 sub-puntos), `Ground Cable Schedule sample.pdf` (26 conductores), `P22-DWG-09-007-003_E_Grounding_CC_ADASA.pdf` (plano anotado por ADASA), `TM N19 Grounding ADASA comment.pdf`.
- **Objeto:** aclaraciones sobre los comentarios de ADASA al plano **Grounding & Power Panel Location Layout Rev E (P22-DWG-09-007-003)**, Code 3 en el TM N19, antes de emitir el Rev F.

## Saliente (ADASA) — ENVIADO 03-Jun-2026

- **Ubicación del correo:** `CORREOS/Junio 2026/2026-06-03/`
  - `2026-06-03_Grounding-RevF-Clarification_Descripcion.md` (fuente + Contexto Interno No enviar)
  - `crear_correo_grounding_clarification.py`
  - `2026-06-03_Grounding-RevF-Clarification.docx`
- **Formato:** correo réplica punto-por-punto (inglés), Reply-To al thread.
- **Esencia de la respuesta:**
  1. La dependencia de layout que cita BW Water (TM N11 OBS-03) ya está resuelta — Equipment Layout (P22-DWG-09-005-003) y Piping Layout (P22-DWG-09-005-004) **Code 2 aprobados desde TM N15 (22-Abr)**; no hay Rev C formal. Proceder con Rev F. **Main panel (LCP/P22-LCP-01) fijo**, se rebate la nota 5 del plano.
  2. El Ground Cable Schedule adjunto cierra materialmente OBS-01 → incorporarlo al Rev F (en el plano o como anexo); reconciliar Cu desnudo/trenzado/barra vs Cu/PVC aislado con el Material Take-Off del plano.
  3. CCS description corregida: cierre condicionado a legibilidad.
  4. Designar método de grounding por carga (IEC 60364-5-54) + reconciliar NEC Table 250.122 (pág.2) vs IEC (pág.3).
  5. Revision history: descripción de cambios + ECN por cada Rev B→E.
  6. Screenshots permitidos si legibles.
  - **Plazo Rev F:** extensión corta a **Mi 17-Jun-2026**. El correo no nombra la reserva C-4300 (instrucción del usuario).

## Próximo hito

- **Grounding Layout Rev F** de BW Water esperado el **Mi 17-Jun-2026** (se revisará en un transmittal posterior).

Trazabilidad completa: README §9 (entrada 03-Jun) + tabla de seguimiento #065; memoria `project_tm19_grounding_clarification_revF`.
