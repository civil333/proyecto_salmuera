---
titulo: Correo de cobertura del Transmittal N42, paquete de izaje y submittals 25007-0096, 0097, 0099 y 0100
fecha: 2026-10-07
estado: BORRADOR
type: correo
project: salmuera-taltal
second_brain: capture
---

# Correo de cobertura del Transmittal N42

**Archivo:** `2026-10-07_Transmittal-N42-Lifting-Package.docx`, generado por `crear_correo.py`. Tiene 263 palabras entre el saludo y los adjuntos, en inglés y en primera persona.

**Cadena:** la regular de transmittals. Puede ser Reply-All sobre el hilo del N40 o del N41, o un correo nuevo con el asunto del N42.

**Para:** Eduardo Yamauchi (BW Water). **CC:** Jeryl F. Regulacion (BW Water) y Víctor Gutiérrez (ADASA). 🔴 **Sin Adzlan Abd Rahim.** Su casilla no existe desde julio y rebota cada envío. Si se usa Responder a todos, hay que sacarlo a mano (`INT-13`).

**Adjuntos (directos, unos 6 MB):**

- `TRANSMITTAL N42 ADASA-BW_WATER.pdf`;
- `P22-DWG-09-005-019_A_GA_Module_Lifting_from_Top_CC_ADASA.pdf` (plano del yugo, extraído de la página 13 del addendum);
- `P22-CD-09-005-003_A_Lifting_Addendum_CC_ADASA.pdf`;
- `P22-DWG-09-005-006_A_Maintenance_Lifting_Points_CC_ADASA.pdf`;
- `P22-DWG-09-005-015_E_GA_Antiscalant_Dosing_Tank_CC_ADASA.pdf`.

El PDF del transmittal está en `REVISIONES/TRANSMITTALES/P22-TM-09-000-042-0/` y los anotados en su `COMENTARIOS/`.

## Resumen del cuerpo

1. Remite el N42: submittals 0096, 0097, 0099 y 0100, ocho documentos, veredicto 3.
2. **Plano del yugo `P22-DWG-09-005-019` Rev A, Código 3.** En primera persona, cita el correo del 15-Sep que lo pedía para el 17. Llegó como hoja 1 de 3 dentro del addendum, sin uniones, material, pesos ni datos de eslingas, y no permite fabricar. Se pide completo, hojas 1 a 3, como documento propio, en perfiles soldados nacionales IN o HN, con los empalmes y las uniones de esquina detallados y al menos una viga intermedia a medio largo.
3. **Addendum Rev A, Código 3.** Solo verifica las orejas. Se pide reemitirlo con código propio, con el diseño del marco, incluidos su torsión, su desangulación y el pandeo de los largueros, bajo las combinaciones NCh3171 del Criterio aprobado como mínimo y con la verificación local de los esquineros.
4. **Lifting Points Rev A, Código 3.** Rev B con viga carrilera o puntos fijos para las bombas y los dos turbocargadores.
5. **GA del estanque Rev E, Código 2.** Marca de nivel a 34" (864 mm) en la Rev 0.
6. **Cuatro documentos en Código 1**, sin acción: Piping Layout, Valve List, procedimiento FAT del tablero y HMI.
7. Una línea remite a los cuatro PDF anotados y a la Sección 3. Siguen los adjuntos y la firma.

## Verificación de fuentes

| Afirmación | Fuente | Verificado |
|---|---|---|
| El correo del 15-Sep pidió el plano del yugo con fecha del 17 | `CORREOS/Septiembre 2026/2026-09-15/2026-09-15_Lifting-Addendum-Reply_Descripcion.md`; compromiso `PRG-49` | Sí. ENVIADO el 15-Sep, plazo jueves 17 |
| Llegó como hoja 1 de 3 del `P22-DWG-09-005-019`, dentro del addendum | `ENTREGAS_BWWATER/ENTREGA 99/`, página 13 del addendum, cajetín "1 OF 3" | Sí, por render (`render/dwg019_A_cajetin_1de3.png`) |
| Sin uniones del marco, material, pesos ni datos de eslingas | Página 13, tabla *Steel Structure* y notas | Sí, por render y capa de texto |
| El addendum solo verifica las orejas | Páginas 3 a 12, *Padeye Design Calculation* | Sí, por render página a página |
| Marca de nivel 864 mm = 34" | GA Rev E, vista 1 `864 [2'-10"]` y `0.27 m³` | Sí. 864 / 25,4 = 34,0 |
| Día de la semana | `datetime`: 7-Oct-2026 es miércoles | Sí |

## Contexto Interno (No enviar)

- **Decisiones de Luis del 5-Oct:**
  - un solo N42 con las cuatro entregas;
  - reclamar el plano del yugo citando el correo del 15-Sep;
  - en las reemisiones, solo verificar el levantamiento de los comentarios anteriores, sin comentarios nuevos salvo errores garrafales;
  - el patrón de devolución a tres días corridos queda fuera.
- **Qué cambió de código durante la revisión.**
  - El Piping Layout Rev E pasó por Código 2, por el rótulo `CP-PVC-DN150-09-022` contra la Line List Rev 2, y volvió a Código 1 por la regla de las reemisiones.
  - La Valve List Rev 0 pasó por Código 3 y volvió a Código 1 tras la verificación adversarial. El N38 aceptó la línea 316L solo por disponibilidad de una reducción de PVC, y ninguna fuente exige la válvula en acero.
  - El plano del yugo pasó a documento propio en Código 3, a pedido de Luis.
  - Los dos hallazgos que no se emiten quedan en los ledgers de la E96 y la E100, y en `COMENTARIOS/_no_emitido/`.
- **Plazos de la Cláusula 37.2.** La E96 venció el 1-Oct y la E97 el 2-Oct. La E99 vence el 8-Oct y la E100 el 13-Oct, por el feriado del 12. El correo no escribe estas fechas.
- **El correo no fija fecha para el paquete de izaje.** El `PRG-49` lleva vencido desde el 17-Sep. Si Luis quiere fijarla, va como una frase en la primera viñeta, y el compromiso se actualiza con origen FIJADA ADASA.
- **La Sección 3 corrige la Tabla 1 del N39.** Los GA de los turbocargadores (`P22-DWG-09-005-012` y `-013`, Rev A) siguen en Código 3 desde el N10 (OBS-06 y OBS-07, montaje del transductor de vibración). El Master Register los da por aprobados y se corrige en el updater del N42.
- **El procedimiento de preservación y embalaje se cita por la BAE Cláusula 38 y la ET Sección 7, pág. 30.** El N37 lo había citado como Cláusula 41, siguiendo la referencia "ref. BAE Cl. 41" de la propia ET. El texto contractual vive en la 38, pág. 63, y su verificación en la inspección pre-embarque es Punto de Espera para el Dispatch Release.

## Checklist pre-envío

- [ ] Regenerar el Word y el PDF del transmittal el mismo miércoles, porque la fecha la pone el template: `python3 crear_transmittal.py` y luego `_HERRAMIENTAS/exportar_pdf_word_mac.sh`.
- [x] ~~Gate `anti-ia revisar` sobre el transmittal, los cuadros y este correo.~~ VERDE. Veredictos en `.anti-ia-2026-10-07/` de las dos carpetas.
- [ ] Sacar a Adzlan de la distribución si se usa Responder a todos.
- [ ] Adjuntar los cinco PDF.

## Checklist post-envío

- [ ] `BORRADOR` a `ENVIADO` aquí y en el frontmatter del transmittal, con la hora.
- [ ] Dejar el respaldo del enviado en esta carpeta y verificar sobre él que viajaron los cinco adjuntos.
- [ ] Correr `update_register_n42.py` con el `TALLY_ESPERADO` declarado antes, más el respaldo `_pre-N42.xlsx`. Incluye las filas de los GA de turbos y el alta del plano del yugo `P22-DWG-09-005-019`.
- [ ] Actualizar `compromisos.yaml`: `PRG-49` (con el plano del yugo en Código 3), `PRG-54` y `PRG-55`. Después regenerar el Excel y correr `openpyxl_lint.py`.
- [ ] README: fila del N42 en el Índice de Transmittales y entrada de Bitácora, con aprobación de Luis.
- [ ] Memorias `project_tm42_state.md` y `transmittals.md`.
