#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_patch_compromisos_postvacaciones.py — registra en compromisos.yaml lo ocurrido entre el
17-Sep y el 5-Oct-2026 (ausencia de Luis Rivera; comunicacion a cargo de Victor Gutierrez).
Edita el archivo como texto (preserva el formato a mano) y luego hay que correr
generar_excel_compromisos.py + openpyxl_lint.py. Idempotente: si PRG-54 ya existe, no hace nada.

Fuentes: correos capturados en CORREOS/_RECIBIDOS/ (Septiembre y Octubre 2026), informes
BVM-IR016 a IR018 en PROGRAMA y CONTRATO/BV INSPECTION/RESUMEN BV/, Transmittal N41 en
REVISIONES/TRANSMITTALES/P22-TM-09-000-041-0/ y la puesta al dia
REVISIONES/EVALUACIONES/_PUESTA_AL_DIA_2026-10-05.md.
"""
import os
import sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compromisos.yaml")
s = open(P, encoding="utf-8").read()
if "- id: PRG-54" in s:
    print("PRG-54 ya existe; nada que hacer")
    sys.exit(0)


def bloque(cid, sig):
    a = s.index(f"  - id: {cid}\n")
    b = s.index(f"  - id: {sig}\n") if sig else len(s)
    return a, b


def reemplazar(cid, sig, cambios):
    global s
    a, b = bloque(cid, sig)
    blk = s[a:b]
    nuevo = blk
    for viejo, nv in cambios:
        assert viejo in nuevo, f"{cid}: no encontre {viejo!r}"
        nuevo = nuevo.replace(viejo, nv, 1)
    s = s[:a] + nuevo + s[b:]


# --- corte
s = s.replace("  corte: 2026-09-17\n", "  corte: 2026-10-05\n", 1)

# --- PRG-51: el reensayo con testigo y la verificacion de los turbos ocurrieron; el informe de BW no
reemplazar("PRG-51", "BV-26", [
    ("    estado: ABIERTO\n", "    estado: CERRADO PARCIAL\n"),
    ("    fecha_cierre: null\n", "    fecha_cierre: 2026-09-23\n"),
    ("    evidencia_cierre: null\n",
     '    evidencia_cierre: "Cumplidos por otra via los puntos (4) y (5): el informe BVM-IR016 de Bureau Veritas (17 y 18-Sep, remitido el 23-Sep) declara ambos turbos conformes a planos y hojas de datos aprobados y ubica la discrepancia en la interfaz del spool; los dos spools modificados se reensayaron con testigo de BV: DA-SSD-DN65-09-008 a 75 bar el 22-Sep (BVM-IR017) y DA-SSD-DN100-09-004 a 120 bar el 23-Sep (BVM-IR018), ambos satisfactorios. BW Water nunca entrego el informe escrito: faltan los desfases medidos antes del corte (el spool ya estaba cortado cuando llego el inspector), la causa raiz documentada y el cronograma de recuperacion. Las isometricas de los spools modificados se siguen en PRG-55"\n'),
    ('    ref_cruzada: "PRG-21, PRG-22, BV-13, PRG-50"', '    ref_cruzada: "PRG-21, PRG-22, BV-13, PRG-50, PRG-55, BV-26"'),
])

# --- BV-26: informe del levantamiento entregado sin el registro previo al corte ni instrumentos
reemplazar("BV-26", "BV-27", [
    ("    estado: ABIERTO\n", "    estado: CERRADO PARCIAL\n"),
    ("    fecha_cierre: null\n", "    fecha_cierre: 2026-09-23\n"),
    ("    evidencia_cierre: null\n",
     '    evidencia_cierre: "Informe BVM-IR016 (17 y 18-Sep-2026), remitido por Jaime Martinez el 23-Sep con comentarios del inspector: turbos conformes a los planos y hojas de datos aprobados, discrepancia en la interfaz del spool, causa raiz solo aparente; el spool ya estaba cortado al llegar, de modo que no hay desfases medidos ni fotos previas al corte (punto 1 incumplido por hechos de BW Water, no del inspector). No cubre instrumentos contra la Instrument List ni equipos contra la Equipment List (puntos 2 y 3 parciales) ni trae Flash Report. Agrega un hallazgo propio: la Line List debe revisarse contra el P&ID y aprobarse por ADASA"\n'),
])

# --- PRG-52: membranas, coordinacion en curso por Abastecimiento/Proyectos
reemplazar("PRG-52", "PRG-53", [
    ('    nota: "El 16-Sep BW Water pidio cerrar las membranas, incluido su retiro, y los repuestos de dos anos; ADASA espera cerrarlo la semana del 21"',
     '    nota: "El 16-Sep BW Water pidio cerrar las membranas, incluido su retiro, y los repuestos de dos anos; ADASA espera cerrarlo la semana del 21. Al 5-Oct: Jorge Guevara cotiza con Matcargo el flete LCL desde Busan (2 pallets de membranas LG; QUOTE MC1098 del 1-Oct en CLP, salidas desde Busan el 2-Oct); falta el valor de la mercaderia para el seguro, que el contrato no desglosa. Antecedentes en PROGRAMA y CONTRATO/DESPACHO MEMBRANAS LG/. Los repuestos se ordenaron con la OC I-333 (COM-10)"'),
])

# --- PRG-53: Rev B recibida en fecha y devuelta en Codigo 3 por el N41
reemplazar("PRG-53", None, [
    ("    estado: ABIERTO\n", "    estado: CERRADO PARCIAL\n"),
    ("    fecha_cierre: null\n", "    fecha_cierre: 2026-09-25\n"),
    ("    evidencia_cierre: null\n",
     '    evidencia_cierre: "E98, submittal 25007-0098 del 25-Sep-2026: P22-BA-09-000-017 Rev B, recibida en la fecha fijada. NO aprobada: Transmittal N41 (P22-TM-09-000-041-0, emitido por Victor Gutierrez el 2-Oct-2026) la devuelve en Codigo 3; cierran OBS-04 y NOTE-02, OBS-03 con comentarios, y siguen abiertas OBS-01, 02, 05, 06, 07, 08, 09, 10 y NOTE-01. La Rev C se sigue en PRG-54"\n'),
    ('    ref_cruzada: "PRG-50, BV-13"', '    ref_cruzada: "PRG-50, BV-13, PRG-54"'),
])

# --- BV-13: la fecha del FAT siguio moviendose sin declaracion escrita
a, b = bloque("BV-13", "BV-14") if "  - id: BV-14\n" in s else bloque("BV-13", None)
blk = s[a:b]
i = blk.index("    historial_fechas: ")
j = blk.index("\n", i)
linea = blk[i:j]
assert linea.endswith('"'), "BV-13: historial_fechas sin comillas de cierre"
linea2 = linea[:-1] + (' -> 17-Sep: BW Water apunta el FAT al 10-Oct y lo reprograma con el cronograma posterior '
                       'al retrabajo -> 24-Sep: el resumen Read AI de la reunion semanal lo da para el 5 al 7-Oct '
                       '-> 28-Sep: Victor Gutierrez informa a BV el 7-Oct en el mejor caso o la semana del 12-Oct. '
                       'Al 5-Oct no hay fecha declarada por escrito y el procedimiento sigue en Codigo 3 (N41)"')
s = s[:a] + blk.replace(linea, linea2, 1) + s[b:]

NUEVOS = '''  - id: PRG-54
    frente: PROGRAMA
    obligado: BW WATER
    beneficiario: ADASA
    compromiso: "Re-emitir el procedimiento FAT del modulo P22-BA-09-000-017 en Rev C con las observaciones abiertas del TM N41"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: CRITICA
    criterio_cierre: "Rev C con formularios de registro por actividad 5.1 a 5.8 con valores de aceptacion; instrumentos de medicion con certificado de calibracion; tolerancias dimensionales y documentos por codigo y revision; equipos por TAG con secuencia de prueba; loop checks de la I/O List Rev 6 y escenarios segun Control Philosophy Rev 1 y Alarm and Interlock List Rev 0; componentes SEC con certificado; aprobacion escrita en cada Hold y aviso y asistencia en cada Witness. Cierra con aprobacion de ADASA en Codigo 1 o 2"
    fuente_contractual: "ET P22-ET-09-000-001-0 Seccion 8.1; BAE Clausula 31 a); ITP P22-BA-09-000-004 Rev 0 fila 7.1 (Hold de ADASA)"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-10-02
    fecha_cierre: null
    consecuencia: "El FAT no abre formalmente sin procedimiento aprobado, y BW Water lo planifica para el 5 al 7-Oct o la semana del 12-Oct"
    accion_adasa: "Fijar por escrito la fecha de la Rev C: el N41 no la fijo"
    evidencia_origen: "Transmittal N41 (REVISIONES/TRANSMITTALES/P22-TM-09-000-041-0/) y su lista de observaciones del 2-Oct-2026"
    evidencia_cierre: null
    ref_cruzada: "PRG-53, BV-13"
    reprogramaciones: 0
    historial_fechas: "El N41 del 2-Oct-2026 devuelve la Rev B sin fecha para la Rev C: SIN FECHA"
    nota: "Emitido por Victor Gutierrez en formato abreviado (lista de observaciones como adjunto, sin PDF anotado)"
  - id: PRG-55
    frente: PROGRAMA
    obligado: BW WATER
    beneficiario: ADASA
    compromiso: "Entregar las isometricas de los spools modificados DA-SSD-DN100-09-004 y DA-SSD-DN65-09-008 y, si cambian el Piping Layout, emitirlo en Rev F"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: ALTA
    criterio_cierre: "Isometricas de fabricacion de los dos spools tal como quedaron, y Piping Layout P22-DWG-09-005-004 Rev F si la modificacion lo afecta, o declaracion escrita de que no lo afecta"
    fuente_contractual: "ET P22-ET-09-000-001-0 Seccion 7 (isometricas de las lineas de alta presion)"
    origen_fecha: COMPROMISO VERBAL-MINUTA
    fecha_origen: 2026-09-24
    fecha_cierre: null
    consecuencia: "Sin isometricas no hay plano contra el cual ADASA o el inspector contrasten los spools ya reensayados, y el layout aprobado puede no representar lo construido"
    accion_adasa: "Pedido por escrito por Victor Gutierrez el 24-Sep (hilo de la 0096) y reiterado el 1-Oct sin respuesta. Exigir fecha en el N42"
    evidencia_origen: "Correos de Victor Gutierrez del 24-Sep 12:00 y 1-Oct 08:47 (CORREOS/Octubre 2026/2026-10-01/); resumen Read AI de la reunion del 24-Sep: accion de Lokman Hakim"
    evidencia_cierre: null
    ref_cruzada: "PRG-51"
    reprogramaciones: 0
    historial_fechas: "Comprometido en la reunion del 24-Sep sin fecha: SIN FECHA"
    nota: "Segun la Line List Rev 2, el 09-004 es la alimentacion de la primera etapa RO (80 barG de diseno, 120 de prueba) y el 09-008 la salida de salmuera del turbo interetapa (50 y 75 barG); el W39 dice que se montaron al Feed Turbocharger"
  - id: PRG-56
    frente: PROGRAMA
    obligado: BW WATER
    beneficiario: ADASA
    compromiso: "Implementar el control de los actuadores Delco por 4-20 mA aceptado en el RFI-003 y reflejarlo en los documentos de control"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: ALTA
    criterio_cierre: "Modulos 5069-IF8 y 5069-OF4 instalados en el tablero, y reemision coherente de la I/O List, el PLC/LCP Schematic, la Valve List y el procedimiento FAT de hardware con el protocolo efectivo de cada actuador, incluidos los on/off"
    fuente_contractual: "ET P22-ET-09-000-001-0 Section 5.2.3 - Actuators (protocolo Ethernet de preferencia, no obligatorio)"
    origen_fecha: COMPROMISO ESCRITO BW
    fecha_origen: 2026-09-24
    fecha_cierre: null
    consecuencia: "La Valve List Rev 0 recibida el 1-Oct sigue declarando Ethernet IP para los 13 actuadores Delco; si los documentos no se alinean, el FAT se prueba contra un protocolo que no existe"
    accion_adasa: "Respuesta al RFI-003 enviada por Victor Gutierrez el 24-Sep (acepta 4-20 mA sin asumir costo ni plazo). Revisar en el N42 la Valve List Rev 0 y el FAT de hardware contra lo aceptado"
    evidencia_origen: "RFI 25007-RO-RFI-0003 y respuesta de ADASA (PROGRAMA y CONTRATO/RFI/RFI 3/)"
    evidencia_cierre: null
    ref_cruzada: "PRG-54"
    reprogramaciones: 0
    historial_fechas: "BW Water estimo 7 a 14 dias de implementacion en el RFI del 23-Sep, sin fecha de termino: SIN FECHA"
    nota: "Inconsistencia de cantidades: el correo dice 4 modulantes y 9 on/off, el formulario 13 modulantes y la Valve List Rev 0 2 modulantes y 11 on/off"
  - id: COM-10
    frente: COMERCIAL
    obligado: BW WATER
    beneficiario: ADASA
    compromiso: "Confirmar la orden de compra I-333 de repuestos para dos anos y coordinar su preparacion y entrega"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: MEDIA
    criterio_cierre: "Aceptacion escrita de la OC I-333 por BW Water con plazo de entrega de los repuestos"
    fuente_contractual: "OC I-333 del 30-Sep-2026; propuesta 25007-PL-0002 rev.0"
    origen_fecha: COMPROMISO ESCRITO BW
    fecha_origen: 2026-09-30
    fecha_cierre: null
    consecuencia: "Sin aceptacion no hay plazo de entrega de los repuestos"
    accion_adasa: "Cotejar la OC contra la propuesta y la carta de aumento de monto (repuestos USD 51.224,50) y pedir la aceptacion con plazo"
    evidencia_origen: "Correo de Victor Gutierrez del 30-Sep 14:50 y respuesta de Eduardo Yamauchi del 30-Sep 21:44 (PROGRAMA y CONTRATO/REPUESTOS DE 2 AÑOS/OC I-333/)"
    evidencia_cierre: null
    ref_cruzada: "PRG-52"
    reprogramaciones: 0
    historial_fechas: "BW Water responde 'we will review and revert' sin fecha: SIN FECHA"
    nota: "OC emitida por Abastecimiento el 30-Sep y remitida por Jorge Guevara"
  - id: BV-28
    frente: BUREAU VERITAS
    obligado: ADASA
    beneficiario: BUREAU VERITAS
    compromiso: "Responder a Bureau Veritas como se facturan las siete visitas de julio y agosto en Malasia (EDP, OC global u OC por visita)"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: MEDIA
    criterio_cierre: "Respuesta escrita a Jaime Martinez con la modalidad de facturacion, cotejada contra el registro de inspecciones y la OC 836492"
    fuente_contractual: "Oferta BV 600049 Rev.3; Orden de Compra 836492"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-10-01
    fecha_cierre: null
    consecuencia: "Sin respuesta BV no puede facturar y el saldo de jornadas contratadas queda sin conciliar"
    accion_adasa: "Cotejar las siete fechas (28-Jul; 7, 13, 20, 21, 24 y 27-Ago) contra _REGISTRO_INSPECCIONES_BV.md y la OC 836492, y responder"
    evidencia_origen: "Correo de Jaime Martinez del 1-Oct-2026 11:12 (CORREOS/_RECIBIDOS/Octubre 2026/)"
    evidencia_cierre: null
    ref_cruzada: "BV-26"
    reprogramaciones: 0
    historial_fechas: "Pedido sin plazo: SIN FECHA"
    nota: "Compromiso de ADASA"
  - id: BV-29
    frente: BUREAU VERITAS
    obligado: ADASA
    beneficiario: BUREAU VERITAS
    compromiso: "Decidir y comunicar si Bureau Veritas atiende el Request to witness inspection 010 (instalacion de equipos, 8 y 9-Oct)"
    fecha_comprometida: 2026-10-07
    estado: ABIERTO
    criticidad: ALTA
    criterio_cierre: "Instruccion escrita a Bureau Veritas, con copia a BW Water, antes de la primera jornada"
    fuente_contractual: "ITP P22-BA-09-000-004 Rev 0; Oferta BV 600049 Rev.3 (jornadas contratadas); BAE Clausula 37 (aviso de inspeccion)"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-10-05
    fecha_cierre: null
    consecuencia: "Si no se responde, BV Malasia puede movilizar o no sin instruccion de ADASA, y la jornada consume o no saldo contratado"
    accion_adasa: "Responder en la cadena del RWI 010; el aviso llego con tres dias corridos"
    evidencia_origen: "Correo de Adnin Zulkaflee del 5-Oct-2026 02:57 (CORREOS/_RECIBIDOS/Octubre 2026/) y formularios en REQUEST WITNESS INSPECTION/RWI 10/"
    evidencia_cierre: null
    ref_cruzada: "BV-13"
    reprogramaciones: 0
    historial_fechas: "Fijada por ADASA al dia anterior a la primera jornada"
    nota: "El 28-Sep Victor pidio a BV una sola visita de avance esa semana, porque no habia puntos de testigo"
  - id: INT-13
    frente: INTERNO ADASA
    obligado: ADASA
    beneficiario: ADASA
    compromiso: "Sacar a Adzlan Abd Rahim de la lista de distribucion de los transmittals y confirmar con BW Water quien lo reemplaza"
    fecha_comprometida: null
    estado: ABIERTO
    criticidad: BAJA
    criterio_cierre: "Proximo transmittal emitido sin adzlan.abdrahim@bw-water.com y sin aviso de no entrega"
    fuente_contractual: "Sin clausula: higiene de la lista de distribucion"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-10-05
    fecha_cierre: null
    consecuencia: "Cada transmittal desde el N29 genera un aviso de no entrega que enumera a todos los destinatarios de BW Water y parece un rechazo global"
    accion_adasa: "Aplicar en el N42 y en los correos de cobertura"
    evidencia_origen: "Avisos de no entrega del N29 al N40; detalle del error: adzlan.abdrahim@bw-water.com 550 5.4.1 Recipient address rejected"
    evidencia_cierre: null
    ref_cruzada: ""
    reprogramaciones: 0
    historial_fechas: "Sin fecha: se aplica en el proximo envio"
    nota: "postmaster@bw-water.com informo el 21-Jul que la casilla no existe"
'''
s = s.rstrip("\n") + "\n" + NUEVOS
open(P, "w", encoding="utf-8").write(s)
print("compromisos.yaml: corte 2026-10-05; PRG-51, PRG-53 y BV-26 CERRADO PARCIAL; BV-13 y PRG-52 "
      "actualizados; nuevos PRG-54, PRG-55, PRG-56, COM-10, BV-28, BV-29, INT-13")
