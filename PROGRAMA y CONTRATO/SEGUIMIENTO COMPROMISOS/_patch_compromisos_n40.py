#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_patch_compromisos_n40.py — cierre parcial de PRG-50 y alta de PRG-53 tras el envio del
Transmittal N40 (18-Sep-2026). Edita compromisos.yaml como texto (preserva el formato a
mano del archivo) y luego hay que correr generar_excel_compromisos.py + openpyxl_lint.py.
CORRER DESPUES DE ENVIAR el transmittal. Idempotente: si PRG-53 ya existe, no hace nada.
"""
import re, sys, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "compromisos.yaml")
s = open(P, encoding="utf-8").read()
if "- id: PRG-53" in s:
    print("PRG-53 ya existe; nada que hacer"); sys.exit(0)

# --- PRG-50: recibido el 18-Sep y no aprobado -> CERRADO PARCIAL
blk_start = s.index("  - id: PRG-50\n")
blk_end = s.index("  - id: PRG-51\n")
blk = s[blk_start:blk_end]
blk2 = blk.replace("    estado: ABIERTO\n", "    estado: CERRADO PARCIAL\n", 1)
blk2 = blk2.replace("    fecha_cierre: null\n", "    fecha_cierre: 2026-09-18\n", 1)
blk2 = re.sub(r"    evidencia_cierre: null\n",
    '    evidencia_cierre: "E95, submittal 25007-0095 del 18-Sep-2026: P22-BA-09-000-017 Rev A Factory Acceptance Test Procedure, sometido para aprobacion en la fecha fijada. NO aprobado: Transmittal N40 (P22-TM-09-000-040-0, 18-Sep-2026) lo devuelve en Codigo 3, diez observaciones y dos notas; la Rev B se sigue en PRG-53"\n', blk2, 1)
blk2 = blk2.replace('    ref_cruzada: "BV-13, PRG-44, PRG-48"', '    ref_cruzada: "BV-13, PRG-44, PRG-48, PRG-53"', 1)
assert blk2 != blk, "PRG-50 sin cambios"
s = s[:blk_start] + blk2 + s[blk_end:]

# --- PRG-53 nuevo, despues de PRG-52
new = '''  - id: PRG-53
    frente: PROGRAMA
    obligado: BW WATER
    beneficiario: ADASA
    compromiso: "Re-emitir el procedimiento FAT del modulo P22-BA-09-000-017 en Rev B, completo y ejecutable, para aprobacion de ADASA"
    fecha_comprometida: 2026-09-25
    estado: ABIERTO
    criticidad: CRITICA
    criterio_cierre: "Rev B recibida que incorpore las diez observaciones y dos notas del TM N40: hojas de prueba paso a paso con valores de aceptacion y formularios de registro en blanco por actividad 5.1 a 5.8; lista de loop checks de la I/O List Rev 6; escenarios de simulacion y de fallo contra la Control Philosophy Rev 1 y la Alarm and Interlock List Rev 0; prerrequisito de hidrostaticas aprobadas; matriz de responsabilidades; referencias por codigo y revision; un solo numero de documento. Cierra cuando ADASA la apruebe (Codigo 1 o 2) y con ella el Hold Point 7.1"
    fuente_contractual: "ET P22-ET-09-000-001-0 Seccion 8.1 (procedimiento detallado, loop checks, escenarios de fallo obligatorios, protocolo especifico); BAE Clausula 31 a) (procedimiento detallado aprobado como Hold del 40 por ciento); ITP P22-BA-09-000-004 Rev 0 filas 7.1 (Hold de ADASA), 7.3, 7.4 y 7.5 (delegan al procedimiento los puntos clave, la secuencia y el detalle de la simulacion)"
    origen_fecha: FIJADA ADASA
    fecha_origen: 2026-09-18
    fecha_cierre: null
    consecuencia: "Sin procedimiento aprobado el FAT no abre formalmente (fila 7.1 Hold) y el tercero inspector no puede planificar el atestiguamiento; el FAT que BW Water apunta al 10-Oct depende de esta Rev B y de su aprobacion"
    accion_adasa: "Si la Rev B no llega el 25-Sep, recordatorio el lunes 28 en la cadena del N40 y constancia en la Seccion 3 del N41 de que el Hold 7.1 sigue abierto; si llega como otro esqueleto, Codigo 3 de nuevo con la cita de la circularidad ITP-procedimiento del N40. Al recibirla, revisar contra _MARCO_REVISION_FAT_NO_ENVIAR.md seccion 2 (matriz de 27 filas) y aprobar solo si cada actividad trae paso, valor y formulario"
    evidencia_origen: "Transmittal N40 (REVISIONES/TRANSMITTALES/P22-TM-09-000-040-0/), subseccion 2.1 y correo de cobertura del 18-Sep-2026 (CORREOS/Septiembre 2026/2026-09-18/), que fija el viernes 25-Sep-2026, cinco dias habiles de Malasia desde la emision"
    evidencia_cierre: null
    ref_cruzada: "PRG-50, BV-13"
    reprogramaciones: 0
    historial_fechas: "Fijada por ADASA el 18-Sep-2026 al viernes 25-Sep-2026 en el correo de cobertura del N40"
    nota: "La Rev A llego el 18-Sep como esqueleto de diez paginas que repite las filas del ITP como encabezados. Codigo 3 sostenido por verificacion adversarial. El PDF anotado y el marco de revision viven en la carpeta del N40"
'''
idx = s.index("  - id: PRG-52\n")
nxt = s.find("\n  - id: ", idx + 10)
if nxt == -1:
    # PRG-52 es el ultimo del bloque de compromisos: insertar antes del siguiente bloque de nivel superior o al final
    m = re.search(r"\n[A-Za-z_]+:\s*\n", s[idx:])
    ins = idx + m.start() + 1 if m else len(s)
else:
    ins = nxt + 1
s = s[:ins] + new + s[ins:]
open(P, "w", encoding="utf-8").write(s)
print("compromisos.yaml: PRG-50 CERRADO PARCIAL, PRG-53 agregado")
