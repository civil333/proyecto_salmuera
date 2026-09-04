# COMPILADO INTERNO — TM N6 (NO ENVIAR A BW WATER)
## Análisis con asesoría Van Doorn | Uso exclusivo ADASA

**Fecha:** 27-Feb-2026
**Código:** P22-TM-09-000-006-0
**Submittal:** 25007-0013 (26-Feb-2026)
**Preparado por:** Luis Rivera | **Asesor:** Van Doorn

---

## Contexto Estratégico

Esta Entrega 13 es la primera entrega masiva de revisiones post-TM N2–N4. BW Water entregó 9 documentos técnicos que responden (parcialmente) a observaciones acumuladas de 22–51 días. El análisis muestra resolución de las críticas principales de PT-100 y PLC, pero introduce nuevos errores de TAG duplicado y una reducción cuestionable de rating de acoples en los turbochargers.

**Patrón BW Water:** Tienden a afirmar "Already revised" en el CCS sin haber efectivamente corregido los documentos. Esto se repite en OBS-02 y OBS-03 de la Valve List: BWW dice "noted, already revised" pero los duplicados persisten en Rev B. Este patrón requiere verificación exhaustiva de cada afirmación.

---

## Análisis Van Doorn por Documento

### 1. Utility Consumption List Rev B

**Van Doorn:** "El cambio de 60Hz a 50Hz en el PLC es lo mínimo esperado — lleva 22 días abierto para un cambio trivial. La nota sobre A/C (1W+1S) resuelve el problema de fondo pero el cálculo térmico de respaldo sigue sin entregarse. Sugiero marcar el ítem como 'approved as noted' pero incluir fecha límite de 10 días para entregar el cálculo térmico. La potencia 3.93 kWh/m3 está dentro del margen del contrato (4.71 ± 5% = 4.47 a 4.97 kWh/m3 — no aplica directamente aquí, es consumo de utilidades, no SEC). Limpiar."

**Posición ADASA:** Approved as Noted. Acción: A/C thermal calculation en plazo de 10 días.

### 2. Valve List Rev B

**Van Doorn:** "Esto es inaceptable. BW Water respondió 'already revised' a cuatro observaciones y tres siguen presentes en el documento. Peor aún, Rev B introduce DOS nuevos duplicados (VE-09-009 y VM-09-065) que no existían en Rev A. Esto indica falta de revisión interna adecuada antes de emitir el documento. El TAG duplicado de VM-09-015 (ítems 18 y 43) es el más crítico: afecta directamente SCADA/DCS y las pruebas de comisionamiento. La válvula del ítem 43 necesita un TAG único urgente.

Para VE-09-008, el problema es aún más grave: materiales totalmente diferentes (CE3MN ANSI 900# vs DI/SS420 ANSI 150#) con el mismo TAG. Esto es un error de ingeniería que podría causar una selección incorrecta durante procurement.

Recomendación: Emitir Rev C urgente. No aceptar menos de Rev C con todos los duplicados resueltos antes de autorizar cualquier compra de válvulas."

**Posición ADASA:** 3 - To be Revised. Acción: Emitir Rev C con todos los TAGs únicos y corrección de prefijos VM→VE donde corresponda.

### 3. HP Pump Rev C

**Van Doorn:** "Los Pt-100 en devanados es lo que necesitábamos documentado. Bien. El tema de potencia ya está suficientemente claro: 93 kW nameplate, 78.5 kW en punto de diseño. La Utility List refleja esto correctamente. Los 83 kW y 85 kW del FEDCO proposal son referencias internas del fabricante — no son inconsistencias sino métricas distintas (FLA rating vs VFD sizing). No es necesario hacer más observaciones sobre potencia en este documento. Approved with note sobre los valores FEDCO para evitar futuras confusiones."

**Posición ADASA:** 2 - Approved as Noted.

### 4. Feed Turbocharger Rev C

**Van Doorn:** "El acople de 1200 psi para servicio a 69.5 bar (1,009 psi) me preocupa. El margen es solo 19%, lo que no cumple los estándares típicos de diseño de presión (mínimo 1.5x para ASME). La justificación de BWW ('out of stock') es una excusa logística, no un criterio de ingeniería. Esto necesita justificación formal, un cálculo de ingeniería o un documento del proveedor FEDCO/Piedmont que confirme el MAWP real del acople Style D superduplex a las condiciones de servicio (temperatura, fluido corrosivo, ciclado de presión).

El tema de vibración en turbochargers: el HP Pump CCS dice 'same will be done for turbochargers' pero el DS del turbocharger no lo confirma. Necesitamos que el datasheet del turbocharger lo diga explícitamente.

Recomendación: 3 - To be Revised. No aprobar la reducción de coupling sin justificación técnica formal."

**Investigación técnica adicional (27-Feb-2026):** Análisis profundo posterior confirmó que la posición debe escalarse a 4 — Rejected por los siguientes fundamentos adicionales:
1. El acople de 1,200 psi (82.7 bar) tiene rating **inferior** a la presión de diseño del sistema de 120 bar (1,740 psi) per ET §5.2.2 — déficit de 540 psi. No es solo un margen insuficiente: el componente literalmente no cubre el MAWP del sistema.
2. El Victaulic Style 77DX tiene un techo absoluto de 1,200 psi — **no existe un Style 77 de 2,000 psi**. El baseline Rev B (2,000 psi) usaba casi con certeza un **Piedmont Pacific Style H**, producto diseñado explícitamente por el fabricante para "HPB Energy Recovery turbochargers." Rev C usa el Style D (1,200 psi), producto para RO estándar. Son dos clases de producto distintas — el argumento "out of stock" colapsa porque el Style H sigue disponible.
3. FEDCO HPB-60 tiene dos versiones: Standard (83 bar = 1,200 psi) y Ultra (124 bar = 1,800 psi). Debe confirmarse qué versión fue entregada.
4. Material de sello Buna N vs EPDM requerido por ET §5.2.2 — incumplimiento contractual y riesgo documentado de corrosión en salmuera concentrada.

**Posición ADASA:** **4 — Rejected.**

### 5. Interstage Turbocharger Rev C

**Van Doorn:** "La situación es mejor que en el Feed Turbocharger. El margen de 1800 psi para 84.8 bar (1,230 psi) da un factor de 1.46x, que si bien es levemente inferior al 1.5x teórico, está en el rango de lo discutible para un acople de alta calidad superduplex. Yo lo aprobaría con nota, condicionado a confirmación del MAWP real por parte del fabricante. El tema de vibración es idéntico al Feed Turbocharger."

**Posición ADASA:** 2 - Approved as Noted.

### 6. Cartridge Filter Rev C

**Van Doorn:** "12 cartuchos está bien justificado técnicamente. El cambio de orientación de boquillas es un update interno de diseño que debe reflejarse en el layout de piping. El FRP es correcto para el servicio de brine concentrada. Aprobado."

**Posición ADASA:** 2 - Approved as Noted.

### 7. Static Mixer Rev B

**Van Doorn:** "El FRP está bien. La L/D mejorada con 750 mm de longitud es adecuada para la mezcla de antiescalante. El CoV de 0.05 indica una muy buena uniformidad de mezcla. El TAG discrepante (MZE-09-001 vs MZE-09-009) es el tema pendiente — necesitamos P&ID actualizado para cerrar esto. El tema de velocidad es una confusión de metodología: el fabricante calcula velocidad en la sección del mixer (1.84 m/s), no en la tubería. Aprobado condicionado a clarificación del TAG."

**Posición ADASA:** 2 - Approved as Noted.

---

## Trazabilidad Observaciones TM N2–N5

### Cerradas en E13

| Obs | Descripción | Resuelto en |
|-----|-------------|------------|
| TM N4 OBS-05 | PLC 60Hz | Utility List Rev B |
| TM N2/N4 A/C n+1 | A/C configuración | Utility List Rev B |
| TM N3 OBS-06/07/08 | Pt-100 devanados y rodamientos HP Pump | HP Pump Rev C |
| TM N3 OBS-01 | Vibration sensor mounting HP Pump | HP Pump Rev C |
| TM N4 OBS-06 | Power inconsistency HP Pump | Utility List Rev B + HP Pump Rev C |
| TM N3 OBS-ValveList | VM-09-015 DN100 actuación eléctrica | Valve List Rev B (ítem 18) |
| OBS-04 Valve List | Duplicado VE-09-010 | Valve List Rev B |
| OBS-05 Valve List | Area codes VM-07-xxx | Valve List Rev B |
| TM N3 Static Mixer | Material FRP vs PVC | Static Mixer Rev B |

### Abiertas post E13 (para TM N6 Sección 4)

| Obs | Origen | Descripción | Días | Acción requerida |
|-----|--------|-------------|------|----------------|
| TM N2 | A/C thermal calc | Cálculo no entregado | 51 | Entrega en 10 días |
| TM N2 | Modbus TCP Memory Map | No en E13 | 51 | Requerir urgente |
| TM N3 | IO List coordination signals | No en E13 | 30 | Requerir con IO List Rev |
| TM N4 | UPS no en BOM | No en E13 | 22 | Confirmar o incluir |
| TM N5 | Layout CIP externo footprint | No en E13 | 4 | Con Layout Rev B |
| TM N6 NUEVO | Valve List Rev C: duplicados 02, 03, 07, 08 | E13 incompleto | 0 | Rev C urgente |
| TM N6 NUEVO | Feed Turbocharger: coupling 1200 psi — **RECHAZADO** (ver OBS-05 TM6) | E13 rechazado | 0 | Rev D con acople ≥2000 psi o alternativa técnica equivalente |
| TM N6 NUEVO | Turbochargers vibration mounting explicit | No en DS | 0 | Confirmar en Rev D |

---

## Notas de Escalonamiento

1. **Valve List:** Si Rev C no resuelve todos los duplicados, bloquear aprobación de procurement de válvulas per compromiso "No POs antes de aprobación" (Reunión 18-Feb-2026).
2. **Feed Turbocharger coupling:** RECHAZADO en TM6 (OBS-05, veredicto 4). BW Water debe emitir Rev D con acople ≥2,000 psi (Piedmont Style H) o alternativa equivalente (bridada CL900 / soldada per Oferta Rev1). Si insisten en rating alternativo, exigir solicitud formal de desviación con justificación técnica per ET §6. Bloquear aprobación de fabricación del turbocharger hasta resolver.
3. **IO List:** La ausencia de IO List actualizado (post-respuesta inline BWW 17-Feb) empieza a bloquear coordinación eléctrica. Próximo paso: incluir como item en TM N6 Required Actions.

---

*Documento interno ADASA — Confidencial — No distribuir a BW Water*
*27-Feb-2026*
