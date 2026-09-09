---
titulo: Correo de cobertura del Transmittal N39
fecha: 2026-09-09
estado: BORRADOR
destinatario: Eduardo Yamauchi (BW Water)
cadena: transmittals
type: correo
project: salmuera-taltal
---

# Correo de cobertura — Transmittal N39

**Archivo:** `2026-09-09_Transmittal-N39.docx` · **Script:** `crear_correo_tm39.py`
**Adjunto:** `TRANSMITTAL N39 ADASA-BW_WATER.docx` (P22-TM-09-000-039-0)

## Resumen del cuerpo

Tres párrafos, 235 palabras.

1. **El adjunto y el veredicto.** Transmittal N39 sobre los submittals 25007-0091 y 25007-0092, tres documentos. Veredicto 2, un Código 1 y dos Código 2, ningún Código 3. Ninguno vuelve a revisión. Se declara que los tres son re-emisiones y que ADASA revisó cada uno solo contra los comentarios que ya había levantado.
2. **La única consecuencia con fecha.** `VM-09-065` sigue en PVC sobre la línea `CP-SS316-DN150-09-022`, que la Line List Rev 1 lleva en 316L. Esa Line List la aprobó ADASA en Código 1 en el N38, y esa válvula es la única DN150 del circuito CIP. Las válvulas se compran contra esa lista, de modo que el material tiene que quedar zanjado antes de que salga la orden de compra y no solo al emitir la Rev 0.
3. **El segundo Código 2 y los plazos.** La fila de marcación de nivel del estanque de antiescalante sigue sin tamaño y sin elevación. Los dos puntos se incorporan al emitir cada documento en Revisión 0, sin revisión de aprobación adicional. Los dos formularios vuelven a pedir devolución en tres días corridos contra los siete hábiles de la Cláusula 37.2, con lo que van ocho y nueve seguidos. ADASA devuelve dentro de plazo igual.

Cierra con el enlace de descarga y las dos viñetas de los PDF anotados.

## Verificación de fuentes

| Afirmación del correo | Fuente | Verificado |
|---|---|---|
| Submittals 25007-0091 y 25007-0092, tres documentos | Formularios de la E91 y la E92 | Sí |
| Veredicto 2, un Código 1 y dos Código 2 | `P22-TM-09-000-039-0_TRANSMITTAL.md`, Response Summary | Sí |
| `CP-SS316-DN150-09-022` en 316L en la Line List Rev 1 | Line List Rev 1, aprobada en Código 1 en el TM N38 | Sí |
| `VM-09-065` en PVC y única DN150 del circuito CIP | Valve List Rev E, página 2; rótulo a 16 puntos del TAG en el P&ID Rev 0, hoja 11 | Sí, por extracción por coordenadas |
| Fila LEVEL MARKING sin tamaño ni elevación | GA Rev D, tabla NOZZLE SPECIFICATIONS, verificado por render PNG | Sí |
| Octavo y noveno formulario pidiendo tres días corridos | Serie de formularios desde la E83 | Sí |
| Siete días hábiles de revisión | Cláusula 37.2 del contrato | Sí |

Las fechas quedaron comprobadas contra el día de la semana: la E91 llegó el **viernes 4**, la E92 el **martes 8**, el correo sale el **miércoles 9**, y bajo la Cláusula 37.2 los dos períodos vencen el **martes 15** y el **jueves 17** de septiembre.

## Contexto Interno (No enviar)

- **La distribución es más acotada que la del N37 y el N38**, que llevaban la lista completa de BW Water. La fijó el usuario al planificar el N39: Eduardo Yamauchi como destinatario, con copia a Jeryl Regulacion y Victor Gutierrez. **Confirmar antes de enviar** si se mantiene o se vuelve a la lista larga.
- **El correo no narra el avance.** Los tres documentos cierran el punto que los tenía detenidos, y eso no se cuenta: el usuario no quiere enviar una visión de cómo va el proyecto. Los cierres viven en la Sección 3 del transmittal, bajo "Closing with this transmittal".
- **Sin cifras de multa y sin invocar ningún umbral.** Los plazos de revisión se registran como hecho, al final y en una cláusula, no como reclamo.
- El `PRG-46` del registro de compromisos **no se cierra** con este transmittal: de los tres cambios que BW Water comprometió por escrito, la succión CIP no quedó reflejada.
- El punto del número de documento del procedimiento de radiografía es housekeeping y por eso no degradó el veredicto, pero entra a la Sección 3 para que no se pierda.

## Checklist pre-envío

- [ ] **Publicar la carpeta `COMENTARIOS` del N39 y pegar el enlace**, luego **regenerar** el `.docx`. El `DOWNLOAD_LINK` sigue en placeholder y el script avisa.
- [ ] Verificar el enlace **sobre el `.docx` emitido y después de pegarlo en Outlook**. Van cuatro enlaces perdidos en el pegado, y ni en texto plano se salvaron.
- [ ] Confirmar la distribución.
- [ ] Exportar el PDF del transmittal **desde Microsoft Word**, para que el índice se actualice. LibreOffice deja el marcador de posición.
- [ ] Enviar por la cadena de los transmittals, en Reply-To.

## Checklist post-envío

- [ ] `BORRADOR` → `ENVIADO` en este archivo.
- [ ] Dejar el respaldo del enviado (PDF o `.msg`) en esta carpeta.
- [ ] Correr `update_register_n39.py`. Tally esperado **68 / 19 / 2 / 0**, y en la misma corrida la corrección de la fila `P22-CD-09-005-001` a Rev 0 desde la E71.
- [ ] Entrada de bitácora en el README, más el Estado Vigente y el Índice de Transmittales.
