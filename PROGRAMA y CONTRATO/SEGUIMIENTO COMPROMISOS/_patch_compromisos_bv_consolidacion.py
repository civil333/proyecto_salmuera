#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_patch_compromisos_bv_consolidacion.py — registra en compromisos.yaml la consolidacion del
frente Bureau Veritas del 5-Oct-2026: rutas nuevas bajo PROGRAMA y CONTRATO/HITO BUREAU VERITAS/,
la reemision BV del 7-Sep (cierra BV-24 y casi todo BV-25), la conciliacion de facturacion
(BV-28) y el aumento de monto de la OC 836492 que exige el FAT (BV-30, nuevo).
Edita el archivo como texto (preserva el formato a mano) y luego hay que correr
generar_excel_compromisos.py + openpyxl_lint.py. Idempotente: si BV-30 ya existe, no hace nada.

Fuentes: PROGRAMA y CONTRATO/HITO BUREAU VERITAS/_ESTADO_OC_836492.md y
04 INFORMES BV/_REGISTRO_INSPECCIONES_BV.md (secciones 1, 2 y 4).
"""
import os
import sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compromisos.yaml")
s = open(P, encoding="utf-8").read()
if "  - id: BV-30\n" in s:
    print("BV-30 ya existe; nada que hacer")
    sys.exit(0)

H = "PROGRAMA y CONTRATO/HITO BUREAU VERITAS/"
I = H + "04 INFORMES BV/"
RUTAS = [
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 05/IR005-ADASA-BVM-20082026.pdf",
     I + "IR005 2026-08-20/IR005-ADASA-BVM-20082026.pdf"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 06/IR006-ADASA-BVM-21082026.pdf",
     I + "IR006 2026-08-21/IR006-ADASA-BVM-21082026.pdf"),
    ("archivado y ordenado en PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/ con analisis",
     "archivado en " + I + " con analisis"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/_REGISTRO_INSPECCIONES_BV.md secciones 3 y 4; renders de verificacion en RESUMEN BV/_render/",
     I + "_REGISTRO_INSPECCIONES_BV.md secciones 3 y 5; renders de verificacion en 04 INFORMES BV/_render/"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/AQ-QAM-F027 Inspection Request_TALTAL project (004).pdf",
     H + "03 SOLICITUDES BW (RWI)/RWI 004 2026-08-20 y 21/AQ-QAM-F027 Inspection Request_TALTAL project (004).pdf"),
    ("PROGRAMA y CONTRATO/HITO BUREAU VERITAS/OC-836492.pdf", H + "01 CONTRATO Y OC/OC-836492.pdf"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/_ANALISIS_HYDROTEST_20AGO.md",
     I + "IR005 2026-08-20/_ANALISIS_HYDROTEST_20AGO.md"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 04/Taltal Hydrotest Report BV W 20Aug.pdf",
     I + "IR005 2026-08-20/Taltal Hydrotest Report BV W 20Aug.pdf"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/INSPECTION 05/_ANALISIS_INSPECCION_05.md e INSPECTION 06/_ANALISIS_INSPECCION_06.md",
     I + "IR005 2026-08-20/_ANALISIS_INSPECCION_05.md e IR006 2026-08-21/_ANALISIS_INSPECCION_06.md"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/_REGISTRO_INSPECCIONES_BV.md", I + "_REGISTRO_INSPECCIONES_BV.md"),
    ("PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/IR007/IR007-ADASA-BVM-24082026.pdf",
     I + "IR007 2026-08-24/IR007-ADASA-BVM-24082026.pdf"),
    ("REQUEST WITNESS INSPECTION/RWI 10/", H + "03 SOLICITUDES BW (RWI)/RWI 010 2026-10-08 y 09/"),
]
for viejo, nuevo in RUTAS:
    assert viejo in s, f"no encontre la ruta {viejo!r}"
    s = s.replace(viejo, nuevo)
for raiz in ("PROGRAMA y CONTRATO/BV INSPECTION", "REQUEST WITNESS INSPECTION/"):
    assert raiz not in s, f"quedo una ruta vieja: {raiz}"


def bloque(cid):
    a = s.index(f"  - id: {cid}\n")
    b = s.find("\n  - id:", a + 5)
    c = s.find("\n  # ====", a + 5)
    fin = min(x for x in (b, c, len(s)) if x != -1)
    return a, fin


def reemplazar(cid, cambios):
    global s
    a, b = bloque(cid)
    blk = s[a:b]
    for viejo, nv in cambios:
        assert viejo in blk, f"{cid}: no encontre {viejo!r}"
        blk = blk.replace(viejo, nv, 1)
    s = s[:a] + blk + s[b:]


REEMISION = ("reemision del 7-Sep-2026 que remitio Jaime Martinez a las 18:43 por la cadena del Request 006, "
             "en respuesta al correo ADASA del 31-Ago, archivada en " + I + "IR005 2026-08-20/, IR006 2026-08-21/ e "
             "IR007 2026-08-24/, subcarpeta REEMISION BV 2026-09-07/")

reemplazar("BV-24", [
    ("    estado: CERRADO PARCIAL\n", "    estado: CERRADO\n"),
    ("    fecha_cierre: 2026-08-31\n", "    fecha_cierre: 2026-09-07\n"),
    ("con la marca del carrete visible\"",
     "con la marca del carrete visible. Las dos que faltaban se completaron con la " + REEMISION +
     ": los dos informes declaran Revision No. 1, marcan Not Satisfactory y Open Non Conformities Yes, y levantan la "
     "No Conformidad en su seccion G (verificado por render y por texto el 5-Oct-2026). Las tres lineas quedaron "
     "ademas conformes a su presion: CP-SSD-DN80-09-044 en el BVM-IR011 del 3-Sep y CP-SSD-DN100-09-014 y "
     "CP-SSD-DN80-09-015 en el BVM-IR013 del 9-Sep\""),
])

reemplazar("BV-25", [
    ("    estado: ABIERTO\n", "    estado: CERRADO PARCIAL\n"),
    ("    fecha_cierre: null\n", "    fecha_cierre: 2026-09-07\n"),
    ("    evidencia_cierre: null\n",
     "    evidencia_cierre: \"" + REEMISION[0].upper() + REEMISION[1:] + ". Cumplido, verificado por render y por texto el "
     "5-Oct-2026: (1) BVM-IR005 y BVM-IR006 Rev 1 marcan Not Satisfactory y Open Non Conformities Yes, con la No "
     "Conformidad en la seccion G y estado Open; (2) BVM-IR007 Rev 1, primera reemision de ese informe, pasa a Not "
     "Satisfactory con No Conformidad por los 355 micrones de la parte inferior del marco; (3) los tres declaran Revision "
     "No. 1 y su propio numero en los encabezados. PENDIENTE: la No Conformidad no lleva numero propio (se identifica "
     "como item 1 de la seccion G de cada informe), el cuadro resumen del 31-Ago no se reemitio con la fila de la visita "
     "del 14-Ago corregida, y ningun informe posterior registra el cierre formal de las tres No Conformidades\"\n"),
    ("Plazo al viernes 4 de septiembre\"",
     "Plazo al viernes 4 de septiembre. Cumplido en lo sustantivo el lunes 7-Sep, tres dias despues del plazo\""),
    ("de modo que el numero erroneo esta en el nombre del archivo y no en el ensayo\"",
     "de modo que el numero erroneo esta en el nombre del archivo y no en el ensayo. La reemision del 7-Sep llego "
     "archivada en una carpeta rotulada RECHAZADOS; el buzon no muestra respuesta de ADASA a ese correo\""),
])

reemplazar("BV-28", [
    ("    accion_adasa: \"Cotejar las siete fechas (28-Jul; 7, 13, 20, 21, 24 y 27-Ago) contra _REGISTRO_INSPECCIONES_BV.md y la OC 836492, y responder\"\n",
     "    accion_adasa: \"Responder remitiendo a la OC 836492, que BV parece desconocer: pregunta si ADASA emitira una OC "
     "global o una OC por visita, cuando la OC esta emitida desde el 14-Jul y el BVM-IR001 la cita. Pedir el estado de "
     "pago de julio y agosto por 9 jornadas (USD 8.793 netos) y no por las 7 que lista BV, a la que le faltan el 14-Ago "
     "(BVM-IR004) y el 28-Ago (BVM-IR009). Septiembre suma 10 jornadas (USD 9.770) aun no presentadas\"\n"),
    ("    evidencia_origen: \"Correo de Jaime Martinez del 1-Oct-2026 11:12 (CORREOS/_RECIBIDOS/Octubre 2026/)\"\n",
     "    evidencia_origen: \"Correo de Jaime Martinez del 1-Oct-2026 11:12 (CORREOS/_RECIBIDOS/Octubre 2026/); "
     "conciliacion en " + H + "_ESTADO_OC_836492.md, seccion Facturacion\"\n"),
    ("    ref_cruzada: \"BV-26\"\n", "    ref_cruzada: \"BV-26, BV-30\"\n"),
])

reemplazar("BV-29", [
    ("porque no habia puntos de testigo\"",
     "porque no habia puntos de testigo. Si BV atiende las dos jornadas, el saldo de la OC 836492 baja a 4 jornadas "
     "contra las 7 del FAT (ver BV-30)\""),
])

NUEVO = f'''  - id: BV-30
    frente: BUREAU VERITAS
    obligado: ADASA
    beneficiario: ADASA
    compromiso: "Tramitar con Abastecimiento el aumento de monto de la OC 836492 a Bureau Veritas para cubrir el atestiguamiento del FAT: la proyeccion de 28 jornadas (19 ejecutadas, 2 del RWI 010 y 7 de FAT) excede en 3 jornadas, USD 2.931 netos, las 25 contratadas"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: ALTA
    criterio_cierre: "OC 836492 ampliada, u OC complementaria emitida, por al menos el deficit vigente a la fecha, antes de la primera jornada del FAT"
    fuente_contractual: "Oferta BV 600049 Rev.3 (item 5.a, 18 jornadas de acompanamiento; item 5.b, 7 jornadas de FAT; adicionales al mismo valor unitario de USD 977); Orden de Compra 836492 de monto cerrado en una sola linea"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-10-05
    fecha_cierre: null
    consecuencia: "El acompanamiento contratado se agoto el 23-Sep con 19 jornadas contra 18. Sin ampliacion, el saldo de 6 jornadas (USD 5.862) no cubre las 7 del FAT, y menos si BV atiende el RWI 010. Cada visita de acompanamiento adicional antes del FAT agranda el deficit en USD 977"
    accion_adasa: "Presentar a Abastecimiento {H}_ESTADO_OC_836492.md con la proyeccion, y actualizar el deficit cada vez que BW Water solicite una visita nueva"
    evidencia_origen: "{H}_ESTADO_OC_836492.md; {I}_REGISTRO_INSPECCIONES_BV.md seccion 1"
    evidencia_cierre: null
    ref_cruzada: "BV-13, BV-28, BV-29"
    reprogramaciones: 0
    historial_fechas: "Abierto el 5-Oct-2026 al consolidar el frente Bureau Veritas. SIN FECHA: el plazo depende de la fecha del FAT, que no esta fijada (FAT Procedure del modulo en Codigo 3 en el Transmittal N41)"
    nota: "Compromiso de ADASA"
'''
a, b = bloque("BV-29")
s = s[:b] + "\n" + NUEVO.rstrip("\n") + s[b:]
open(P, "w", encoding="utf-8").write(s)
print("compromisos.yaml actualizado: 12 rutas, BV-24 CERRADO, BV-25 CERRADO PARCIAL, BV-28 y BV-29 ampliados, BV-30 nuevo")
