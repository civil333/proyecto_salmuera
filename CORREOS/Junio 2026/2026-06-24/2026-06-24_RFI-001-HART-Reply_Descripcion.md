# Correo — Respuesta ADASA al RFI-001 (HART) — 24-Jun-2026

**Estado:** ENVIADO 24-Jun-2026
**Tipo:** Reply-To al thread del RFI-001 (cadena del propio RFI, separada de los transmittals)
**Para:** Billy Tan (BW Water / Engineering — emisor del RFI)
**CC:** Eduardo Yamauchi, Stephane Gehant, Jeryl F. Regulacion, Adzlan Bin Abd Rahim, Nick Huta, Sadeep Irugalbandara, Victor Gutierrez
**Asunto:** RE: RFI 25007-RO-RFI-0001 — Analog Input Modules and the 4-20 mA + HART instrumentation requirement (Section 5.5)
**Adjunto:** `RFI-001 Clarification AI Module with HART_ADASA_REPLY.docx` (form RFI con la sección Replied Information completada)

## Qué dice el correo (cover)

Acusa recibo del RFI y devuelve el form con la respuesta. Confirma en una línea que la configuración descrita (instrumentos 4-20mA+HART + HART por handheld en el lazo + 5069-IF8 leyendo solo 4-20 mA) cumple la ET Sección 5.5; que NO se requiere pass-through HART al PLC/SCADA, ni I/O HART-capable, ni asset management → sin hardware adicional. Deja la condición: todo instrumento debe ser 4-20mA+HART. Remite al form adjunto para la respuesta completa. Sin proponer reunión.

## Contexto Interno (No enviar)

- **Fondo ya calibrado en TM N24 (23-Jun).** La ET §5.5 exige 4-20mA+HART a nivel de instrumento, NO decodificación HART central en el PLC. El TM N21 OBS-01 había exigido una "HART acquisition path" en el PLC = **over-reach**, cerrado positivamente en TM N24.
- **Decisión del usuario sobre el rastro del TM N21:** confirmar citando el cierre del TM N24, **sin nombrar OBS-01 ni decir "retirada"** (limpieza suave, sin admitir over-reach por escrito). Aplicada tanto en el form como en el correo.
- **Condición defensiva:** la confirmación NO renuncia al requisito a nivel de instrumento — un instrumento solo-4-20mA sin HART sigue siendo hallazgo válido (precedente IFM VTV122, TM N12). El correo y el form lo dejan explícito.
- **No citar a BW Water:** lógica interna de Van Doorn, códigos OBS/Code, ni §N (verificado: §N=0, sin Van Doorn).
- **Verificación:** workflow `rfi001-hart-verify` (4 verificadores + síntesis) APROBADO 4/4 PASS, 0 obligatorias, sobre el texto del form. El cuerpo del correo es cover-only (no repite la sustancia del form, solo la línea de confirmación).
