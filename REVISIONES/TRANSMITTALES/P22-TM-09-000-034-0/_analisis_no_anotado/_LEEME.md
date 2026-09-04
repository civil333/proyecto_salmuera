# Traza interna — NO EMITIR

Anotaciones generadas y **retiradas** del Transmittal N34.

## `P22-LI-09-008-015` Alarm and Interlock List Rev 0

Se anoto con dos observaciones cuando el documento estaba dispuesto en **Codigo
3**. El usuario objeto el veredicto y se corrigio a **Codigo 1**, de modo que el
`CC_ADASA` no corresponde: un Codigo 1 no lleva PDF anotado.

Motivo de la correccion, en los terminos de `feedback_rev0_solo_code1_o_code3`:
ante un Rev 0 la pregunta es si el defecto es intrinseco al documento o vive en
otro.

- **El rango de vibracion vive en la Instrument List** `P22-LI-09-008-003` Rev E,
  que sigue en 0 a 8,9 mm/s rms. La Alarm List Rev 0 es coherente en si misma
  (rango 0 a 12,0 y disparo en 10,0). Va a la Seccion 3 del transmittal, con el
  valor vinculante declarado por ADASA en 0 a 12 mm/s rms.
- **Los TAG `VE09-014-XT001` y `VE09-016-XT001` sin guion** son housekeeping
  documental, que por regla no degrada por si solo. Van como una linea del bloque
  de accion del Codigo 1, para corregir en la proxima emision natural.

El hallazgo del TAG **es real y esta verificado por render a 300 dpi** de la
pagina 8: las dos filas nuevas estan en rojo y sin guion, mientras `VE-09-012`,
`VE-09-013` y `BDS-09-001` lo llevan, y la IO List Rev 5 tambien. Si reaparece en
el dossier o en la configuracion del PLC, la evidencia esta aca.

Archivos: `agregar_comentarios_alarm_interlock_rev0.py`, el PDF fuente y el
`CC_ADASA` generado.
