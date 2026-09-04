# Qué se emite y qué no, en esta carpeta

El TM N30 se re-escopeó a tres submittals. Esta carpeta contiene los tres juegos de anotación, pero **solo dos se adjuntan al correo**.

## Se emiten

| Archivo | Documento | Código | Anotaciones |
|---|---|---|---|
| `P22-BA-09-000-013_A_CC_ADASA.pdf` | Fabrication and Testing Dossier Index Rev A (E69) | 3 | 10 — OBS-01 a OBS-06, NOTE-01 a NOTE-04 |
| `P22-DWG-09-005-004_C_CC_ADASA.pdf` | Piping Layout Rev C (E70), las 22 páginas | 2 | 9 — OBS-01 a OBS-06, NOTE-01 a NOTE-03 |

**Un solo anotado cubre dos subsecciones del transmittal.** Los planos de taller `25007-ME-PI-0901-0006` a `-0016` no son un archivo aparte: son las páginas 5 a 21 del mismo PDF del Piping Layout. Por eso los identificadores corren **correlativos a lo largo de todo el archivo** y no se reinician por subsección — dos observaciones distintas no pueden compartir ID dentro de un mismo documento anotado. El reparto:

- Subsección del Piping Layout: `OBS-02`, `OBS-03`, `NOTE-01` a `NOTE-03`
- Subsección del conjunto de taller: `OBS-01`, `OBS-04`, `OBS-05`, `OBS-06`

## NO se emite

`P22-ET-09-008-001_0_DS_PLC_HMI_CC_ADASA.pdf` — el Datasheet of PLC and HMI Panel Component quedó en **Código 1 — Approved**, y un documento Código 1 no lleva PDF anotado. Este archivo se generó durante la revisión, cuando el veredicto de trabajo era Código 2, y **queda como traza interna**: no se adjunta, no se menciona en la Sección 4 y no se sube a ninguna parte.

Su contenido quedó superado por la verificación adversarial: la observación del terminal de operación no se redacta como pregunta a BW Water sino como **declaración vinculante de ADASA**, y la corrección cae en los otros cuatro documentos, no en el revisado.

Tampoco hay anotado del **3D Model Rev A**, que es Código 2: un `.nwd` no admite el formato de anotación de los planos. Sus observaciones van íntegras en el texto de la subsección 2.5 y la Sección 4 lo declara.

## Dos cosas que costaron una corrección y conviene no repetir

**Las anotaciones se salen de la hoja sin avisar.** El primer intento sobre el Dossier Index apiló nueve cajas de quince líneas en la página del índice; las últimas quedaron en y=1725 sobre una A4 de 842 puntos, es decir invisibles en el PDF emitido, y el script terminó sin error. El texto de una anotación es la **instrucción y su fuente**, no el argumento completo —ese vive en la Sección 2 del transmittal— y en documentos de pocas páginas hay que **repartir con `offset_y` explícito** y comprobar por render que todas caen dentro.

**En páginas rotadas `page.annots()` miente.** Las láminas 1 a 3 del Piping Layout tienen `rotation=270` y devuelven cero anotaciones aunque estén dibujadas, porque la skill escribe en el content stream. La única verificación válida es el **render PNG**: comprobar que el ID y el texto se leen completos y de izquierda a derecha.

## Regenerar

```bash
python agregar_comentarios_dossier_index.py
python agregar_comentarios_piping_layout.py
```

El script del Piping Layout lleva el *fast-save guard* (`garbage=1, deflate=False`) que ese PDF necesita: son 22 láminas A1 con 430.141 vectores y 13,9 MB, y la recompresión total del guardado por defecto no converge.
