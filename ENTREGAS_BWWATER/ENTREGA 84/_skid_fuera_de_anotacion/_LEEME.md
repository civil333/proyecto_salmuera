# GA of SWRO System Skid Rev 0 — anotacion retirada del Transmittal N36

> **TRAZA INTERNA. Nada de esta carpeta se emite.**

## Que hay aqui

| Archivo | Que es |
|---|---|
| `P22-DWG-09-005-008_0_GA_SWRO_System_Skid_CC_ADASA.pdf` | El PDF anotado que se genero y **no se emite** |
| `agregar_comentarios_ga_swro_skid_rev0.py` | El script que lo produjo, con sus dos entradas OBS-01 y OBS-02 |
| `skid_p2.png` | Render de verificacion de las dos anotaciones |

El PDF fuente no se duplica aqui: es `25007-0084/P22-DWG-09-005-008_0 GA of SWRO System Skid.pdf`, en esta misma entrega, y la copia local era byte-identica.

## Por que se retiro

**Decision del usuario, 26-Ago-2026.** El documento se disponia en **Codigo 3** y paso a **Codigo 1**, y un Codigo 1 no lleva PDF anotado.

Las dos razones, en orden de peso:

1. **Esta en Rev 0, emitido para construccion.** No se devuelve a revision por un defecto de forma. Sobre un Rev 0 el Codigo 3 queda reservado a un defecto **sustantivo de contenido** que obligue a rehacer el documento. Devolverlo detendria un plano que ya gobierna fabricacion.
2. **Los dos puntos abiertos son de cita, no de contenido.** Ninguno cambia una cota, un material, un rating ni una cantidad del skid, y los documentos referidos siguen siendo identificables.

**Lo que NO cambio es el tono.** Bajar el codigo no es bajar la exigencia: el transmittal enuncia los dos puntos con fuerza en su Resumen Ejecutivo y en la subseccion del documento, deja constancia de que de las tres referencias pedidas en el TM N31 solo una se corrigio, y escribe literal el codigo correcto para que quede en el registro aunque el plano no se reemita.

## La evidencia verificada, que se conserva

| Referencia | Pedido del TM N31 | Estado en la Rev 0 |
|---|---|---|
| Nota 7 | Line List a `P22-LI-09-009-003` | **Cerrado** en las dos hojas |
| Nota 6 | Instrument List de Rev D a Rev E | **Cierre parcial.** Hoja 2 dice `REV.E`; **Hoja 1 sigue en `REV.D`**, de modo que el mismo plano remite la misma matriz de instrumentos a dos revisiones |
| Nota 8 | Codigo valido en vez de `P22-ET-09-006-01` | **No cerrado.** Sin cambio en las dos hojas. El codigo correcto es `P22-ET-09-006-001` |

**La respuesta de BW Water a la nota 8 se refuta a si misma.** Contestaron que un pantallazo demuestra que el numero ya se habia sometido antes, y adjuntaron esa captura como ultima pagina del archivo: escribe el codigo con **tres digitos**, `P22-ET-09-006-001`, y la fila siguiente es `P22-ET-09-006-002 Painting Specification`.

El cierre punto por punto sigue en el `_LEDGER_COMENTARIOS.md` de esta entrega, que no se toca.

## Regla que se aplico

Al retirar un veredicto, el `CC_ADASA` se retira con el y la evidencia verificada se conserva por si el punto reaparece: no se borra. El destino habitual es una subcarpeta del propio transmittal; aqui se movio a la carpeta de la entrega, junto al documento que comenta, siguiendo el criterio que el usuario fijo el mismo dia para el cronograma.
